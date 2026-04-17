#!/usr/bin/env python3
"""Collect contest submission code into artifacts/contests/<contest>/<problem>/submissions/<rank-N-author>/.

Phase 3 tasks 9/10. For each `sources/contests/**/*.md` file, iterate its
`submissions[*]` entries and, where a public, author-republished code source
exists (GitHub repo, personal blog's published code, participant's shared
repo), fetch the code into the implicit submission bundle. Otherwise set
`submission_truth: unavailable` with a concrete `code_unavailable_reason`
citing exactly why the code is not locally retrievable.

Strategy:
  - Drive collection from a per-contest manifest, `data/contest-sources.yaml`,
    that maps each submission (contest / problem / rank / author) to an
    optional `origin_url` + kind ({github-file, inline-from-blog, discord-only, unavailable-public}).
  - For github-file: fetch via `gh api contents/...?ref=<sha>`.
  - For inline-from-blog: look up the originating blog in sources/blogs/ and
    copy the matching extracted code from artifacts/blogs/<slug>/code/.
  - For discord-only / unavailable-public: set submission_truth=unavailable
    and write the reason.

By default the manifest is empty, which means all submissions remain
`unavailable` with a structural reason. When an entry gains a concrete source,
add it to data/contest-sources.yaml and re-run.
"""

import argparse
import base64
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
import yaml

REPO = Path(__file__).resolve().parent.parent
CONTESTS_SRC = REPO / "sources" / "contests"
CONTESTS_ART = REPO / "artifacts" / "contests"
MANIFEST = REPO / "data" / "contest-sources.yaml"


def sha256_of(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_gh(args):
    res = subprocess.run(["gh"] + list(args), stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    return res.stdout


def rank_author_slug(rank, participant):
    participant_slug = re.sub(r"[^a-z0-9]+", "-", participant.lower()).strip("-") or "anon"
    return f"rank-{rank}-{participant_slug}"


def load_md(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^(---\s*\n)(.*?)(\n---\s*\n)(.*)", text, re.DOTALL)
    if not m:
        return None
    return m, yaml.safe_load(m.group(2)) or {}, text


def save_md(path, original_match, fm):
    new_fm = yaml.dump(fm, allow_unicode=True, sort_keys=False, default_flow_style=False).rstrip()
    path.write_text(original_match.group(1) + new_fm + original_match.group(3) + original_match.group(4), encoding="utf-8")


def load_manifest():
    if not MANIFEST.is_file():
        return {}
    return yaml.safe_load(MANIFEST.read_text(encoding="utf-8")) or {}


def collect_one(contest_page, sub_idx, sub, manifest):
    """Returns (new_sub_dict, wrote_any_files: bool, error: str|None)."""
    contest_slug = contest_page.parent.name
    problem_slug = contest_page.stem
    rank = sub.get("rank")
    participant = sub.get("participant") or "anon"
    ra_slug = rank_author_slug(rank, participant)

    # Consult manifest: data/contest-sources.yaml structured as:
    # {contest: {problem: {rank-N-author-slug: {kind, origin_url, ...}}}}
    entry = ((manifest.get(contest_slug) or {}).get(problem_slug) or {}).get(ra_slug)
    if not entry:
        # No manifest entry — remain unavailable with structural reason.
        new_sub = dict(sub)
        new_sub["submission_truth"] = "unavailable"
        new_sub["code_unavailable_reason"] = (
            "No public author-republished source declared in data/contest-sources.yaml; "
            "add an entry if a public URL becomes available."
        )
        new_sub.pop("code_path", None)
        return new_sub, False, None

    kind = entry.get("kind")
    origin_url = entry.get("origin_url", "")
    bundle_dir = CONTESTS_ART / contest_slug / problem_slug / "submissions" / ra_slug

    new_sub = dict(sub)
    files_list = []

    # For unavailable kinds, never create the bundle directory.
    if kind in ("discord-only", "unavailable-public"):
        if bundle_dir.is_dir():
            for f in bundle_dir.iterdir():
                if f.is_file():
                    f.unlink()
            try:
                bundle_dir.rmdir()
            except OSError:
                pass
        new_sub["submission_truth"] = "unavailable"
        new_sub["code_unavailable_reason"] = entry.get("reason", f"kind={kind}; no public code")
        new_sub.pop("code_path", None)
        return new_sub, False, None

    bundle_dir.mkdir(parents=True, exist_ok=True)

    # Clear any stale bundle contents before rewriting. Without this, a
    # manifest edit that renames or drops a submission file leaves the old
    # file in place, which (a) pollutes the bundle with orphan code and
    # (b) trips validate.py's drift detection on subsequent runs.
    for stale in bundle_dir.iterdir():
        if stale.is_file():
            stale.unlink()
        else:
            shutil.rmtree(stale)

    try:
        if kind == "github-file":
            repo = entry["upstream_repo"]
            sha = entry.get("upstream_sha") or "HEAD"
            files_spec = entry.get("files", [])
            for fs in files_spec:
                src_path = fs["upstream_path"]
                out_name = fs.get("local_name") or src_path.split("/")[-1]
                out = bundle_dir / out_name
                data = run_gh(["api", f"/repos/{repo}/contents/{src_path}?ref={sha}"])
                doc = json.loads(data)
                if doc.get("type") != "file":
                    return new_sub, False, f"non-file response for {repo}:{src_path}"
                out.write_bytes(base64.b64decode(doc["content"]))
                files_list.append({
                    "local_path": out_name,
                    "role": "upstream-file",
                    "mode": "verbatim",
                    "upstream_path": src_path,
                    "sha256": sha256_of(out),
                })
            truth = "official-submission" if entry.get("official") else "author-published-posthoc"
            # Write PROVENANCE.yaml
            prov = {
                "origin_url": origin_url,
                "upstream_repo": repo,
                "upstream_sha": sha,
                "license": entry.get("license", "inherits-from-upstream"),
                "retrieved_at": "2026-04-17",
                "asset_mode": "verbatim",
                "size_cap_truncated": False,
                "generated_by": "scripts/collect_contest_code.py",
                "source_contest_id": f"contest-{contest_slug}-{problem_slug}",
                "files": files_list,
            }
            (bundle_dir / "PROVENANCE.yaml").write_text(
                yaml.dump(prov, sort_keys=False, allow_unicode=True, default_flow_style=False),
                encoding="utf-8",
            )
            new_sub["submission_truth"] = truth
            new_sub["code_path"] = f"artifacts/contests/{contest_slug}/{problem_slug}/submissions/{ra_slug}/{files_list[0]['local_path']}"
            new_sub.pop("code_unavailable_reason", None)
            return new_sub, True, None

        elif kind == "inline-from-blog":
            blog_slug = entry["blog_slug"]
            blog_bundle = REPO / "artifacts" / "blogs" / blog_slug
            blog_code_dir = blog_bundle / "code"
            if not blog_code_dir.is_dir():
                return new_sub, False, f"blog code bundle {blog_slug} not extracted yet"
            # Load the blog's MANIFEST.yaml so we can copy the real heading_path
            # for each file into the contest bundle's PROVENANCE.yaml (instead of
            # writing a placeholder inheritance string).
            blog_manifest_path = blog_bundle / "MANIFEST.yaml"
            blog_manifest_files = {}
            if blog_manifest_path.is_file():
                try:
                    bm = yaml.safe_load(blog_manifest_path.read_text(encoding="utf-8")) or {}
                    for e in (bm.get("files") or []):
                        lp = e.get("local_path")
                        if lp and lp.startswith("code/"):
                            blog_manifest_files[lp[len("code/"):]] = e
                except yaml.YAMLError:
                    pass
            # Copy each named file into the submission bundle
            want = set(entry.get("files") or [])
            for f in sorted(blog_code_dir.iterdir()):
                if f.name == "PROVENANCE.yaml" or not f.is_file():
                    continue
                if want and f.name not in want:
                    continue
                dst = bundle_dir / f.name
                shutil.copy(f, dst)
                heading = blog_manifest_files.get(f.name, {}).get("heading_path") or f"(heading not recorded in {blog_slug}/MANIFEST.yaml)"
                files_list.append({
                    "local_path": f.name,
                    "role": "extracted-block",
                    "mode": "extracted",
                    "upstream_path": f"sources/blogs/{blog_slug}.md",
                    "heading_path": heading,
                    "sha256": sha256_of(dst),
                })
            if not files_list:
                return new_sub, False, "no matching files in blog bundle"
            prov = {
                "origin_url": origin_url,
                "upstream_repo": f"blog/{blog_slug}",
                "upstream_sha": "none",
                "license": "inherits-from-source-blog",
                "retrieved_at": "2026-04-17",
                "asset_mode": "extracted",
                "size_cap_truncated": False,
                "generated_by": "scripts/collect_contest_code.py",
                "source_contest_id": f"contest-{contest_slug}-{problem_slug}",
                "files": files_list,
            }
            (bundle_dir / "PROVENANCE.yaml").write_text(
                yaml.dump(prov, sort_keys=False, allow_unicode=True, default_flow_style=False),
                encoding="utf-8",
            )
            new_sub["submission_truth"] = "reconstructed-from-blog"
            new_sub["code_path"] = f"artifacts/contests/{contest_slug}/{problem_slug}/submissions/{ra_slug}/{files_list[0]['local_path']}"
            new_sub.pop("code_unavailable_reason", None)
            return new_sub, True, None

        else:
            return new_sub, False, f"unknown kind '{kind}'"
    except subprocess.CalledProcessError as e:
        return new_sub, False, f"gh failed: {e.stderr.decode(errors='replace').strip()[:120]}"
    except Exception as e:
        return new_sub, False, f"{type(e).__name__}: {e}"


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    manifest = load_manifest()
    wrote = 0
    unavailable = 0
    fails = []

    for contest_md in sorted(CONTESTS_SRC.rglob("*.md")):
        loaded = load_md(contest_md)
        if not loaded:
            continue
        mmatch, fm, _ = loaded
        subs = fm.get("submissions") or []
        if not subs:
            continue
        new_subs = []
        changed = False
        for i, sub in enumerate(subs):
            if not isinstance(sub, dict):
                new_subs.append(sub)
                continue
            if args.dry_run:
                new_subs.append(sub)
                continue
            new_sub, ok, err = collect_one(contest_md, i, sub, manifest)
            if err:
                fails.append(f"{contest_md.relative_to(REPO)}[{i}]: {err}")
            if ok:
                wrote += 1
            elif new_sub.get("submission_truth") == "unavailable":
                unavailable += 1
            if new_sub != sub:
                changed = True
            new_subs.append(new_sub)
        if changed:
            fm["submissions"] = new_subs
            save_md(contest_md, mmatch, fm)

    print(f"Collected code for {wrote} submissions; marked {unavailable} as unavailable.")
    if fails:
        print(f"\n{len(fails)} soft failure(s):")
        for f in fails:
            print(f"  {f}")


if __name__ == "__main__":
    main()
