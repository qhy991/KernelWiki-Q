#!/usr/bin/env python3
"""Fetch cleaned PR bundles into artifacts/prs/<repo>/PR-<N>/ (Phase 3 task5).

For each PR in data/core-prs.yaml (or a user-supplied subset), the script:
  1. Reads sources/prs/<repo>/PR-<N>.md to get repo + pr + merge_sha.
  2. Calls `gh pr diff <N> -R <repo>` to capture the whole-PR patch.
  3. Calls `gh api /repos/<repo>/pulls/<N>/files` to get the file list.
  4. For each file whose path matches the kernel allowlist, fetches the
     file's content at the merge SHA via `gh api contents/...?ref=<sha>`
     and writes it under artifacts/prs/<repo>/PR-<N>/key-files/<upstream-path>.
  5. Emits PROVENANCE.yaml with bundle-level defaults + per-file manifest.
  6. Enforces the size caps:
       - per-file 1 MiB: file content replaced with a stub + files[*].size_cap_truncated: true
       - bundle-total 5 MiB: diff.patch omitted, PROVENANCE.yaml.size_cap_truncated: true
  7. Writes the bundle path back into the source PR page's frontmatter as
     `artifact_dir: artifacts/prs/<repo>/PR-<N>`.

Modes:
  --pilot          : fetch 20 PRs spread across the 5 tracked repos, write
                     data/phase3-size-budget.yaml from the aggregate, and stop.
  --all            : fetch every entry in data/core-prs.yaml (lower-bound).
  --ids X Y Z      : fetch only the listed PR IDs (debugging).
  --dry-run        : print intent, do not call gh or write files.
"""

from __future__ import annotations

import argparse
import base64
import fnmatch
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
ARTIFACTS = REPO_ROOT / "artifacts" / "prs"
CORE_PATH = REPO_ROOT / "data" / "core-prs.yaml"
BUDGET_PATH = REPO_ROOT / "data" / "phase3-size-budget.yaml"
SOURCES_PRS = REPO_ROOT / "sources" / "prs"

FILE_SIZE_CAP = 1 * 1024 * 1024  # 1 MiB
BUNDLE_SIZE_CAP = 5 * 1024 * 1024  # 5 MiB

# Kernel-file allowlist (plan §4.1 + clarifications)
KERNEL_EXTS_C = {".cu", ".cuh", ".cpp", ".cxx", ".cc", ".h", ".hpp", ".hxx", ".inl"}
KERNEL_EXTS_PTX = {".ptx"}
KERNEL_EXTS_PY_STRICT = {".py", ".pyx"}  # only when path matches keyword
KERNEL_PY_KEYWORDS = ("kernel", "triton", "cute", "ops", "csrc")

# Skip all of these entirely
SKIP_GLOBS = (
    "tests/**", "test/**", "*_test.cu", "*_test.cpp", "*_tests.py",
    "docs/**", "**/README*", "**/CHANGELOG*", "**/release_notes*",
    ".github/**", "ci/**", "**/conftest.py",
)


def run_gh(args, capture=True):
    try:
        res = subprocess.run(
            ["gh"] + list(args),
            stdout=subprocess.PIPE if capture else None,
            stderr=subprocess.PIPE,
            check=True,
        )
        return res.stdout if capture else b""
    except FileNotFoundError:
        raise RuntimeError("gh CLI not found; install https://cli.github.com/")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"gh {' '.join(args)} failed: {e.stderr.decode(errors='replace').strip()}")


def load_core_prs():
    if not CORE_PATH.is_file():
        raise RuntimeError(f"missing {CORE_PATH.relative_to(REPO_ROOT)}; run scripts/compute_core_prs.py first")
    data = yaml.safe_load(CORE_PATH.read_text(encoding="utf-8"))
    return [e["id"] for e in data.get("prs", []) if "id" in e]


def read_pr_page(pid):
    # pid = pr-<repo>-<N>, but <repo> may have hyphens — sanity: look up by id, not path.
    for md in SOURCES_PRS.rglob("PR-*.md"):
        try:
            text = md.read_text(encoding="utf-8")
        except OSError:
            continue
        m = re.match(r"^---\s*\r?\n(.*?)\r?\n---", text, re.DOTALL)
        if not m:
            continue
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError:
            continue
        if fm.get("id") == pid:
            return md, fm, text
    return None, None, None


def path_allowed(path):
    """Return True iff path should be captured as a kernel file."""
    posix = path.replace("\\", "/")
    # Explicit skips first
    for g in SKIP_GLOBS:
        if fnmatch.fnmatch(posix, g):
            return False
    suffix = "." + posix.rsplit(".", 1)[-1].lower() if "." in posix.rsplit("/", 1)[-1] else ""
    if suffix in KERNEL_EXTS_C or suffix in KERNEL_EXTS_PTX:
        return True
    if suffix in KERNEL_EXTS_PY_STRICT:
        return any(kw in posix.lower() for kw in KERNEL_PY_KEYWORDS)
    if suffix in {".json"} and "cutlass_configs" in posix:
        return True
    return False


def fetch_content_at_sha(repo, path, sha):
    """Fetch single file's bytes at pinned SHA. Returns bytes OR raises."""
    endpoint = f"/repos/{repo}/contents/{path}?ref={sha}"
    out = run_gh(["api", endpoint])
    data = json.loads(out)
    if data.get("type") != "file" or "content" not in data:
        raise RuntimeError(f"unexpected response for {repo}:{path}@{sha[:10]}: type={data.get('type')}")
    return base64.b64decode(data["content"])


def fetch_pr_file_list(repo, pr_num):
    """Return list of dicts {filename, status, patch?, sha?} for the PR."""
    # /repos/{owner}/{repo}/pulls/{N}/files; paginated
    results = []
    page = 1
    while True:
        out = run_gh(["api", f"/repos/{repo}/pulls/{pr_num}/files?per_page=100&page={page}"])
        chunk = json.loads(out)
        if not isinstance(chunk, list) or not chunk:
            break
        results.extend(chunk)
        if len(chunk) < 100:
            break
        page += 1
        if page > 20:  # guard against runaway pagination
            break
    return results


def fetch_pr_whole_diff(repo, pr_num):
    """Return the whole-PR patch as bytes via `gh pr diff`."""
    return run_gh(["pr", "diff", str(pr_num), "-R", repo])


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def emit_bundle(repo, pr_num, pr_id, merge_sha, file_list, whole_diff, dry_run=False):
    """Write a bundle and return (bundle_dir_rel, total_bytes, num_files, truncated)."""
    # Repo short name: "NVIDIA/cutlass" -> "cutlass"; keep lowercase
    repo_short = repo.split("/")[-1].lower()
    bundle = ARTIFACTS / repo_short / f"PR-{pr_num}"
    bundle_rel = bundle.relative_to(REPO_ROOT)

    if dry_run:
        kept = [f for f in file_list if path_allowed(f.get("filename", ""))]
        print(f"  DRY-RUN {pr_id}: {len(kept)}/{len(file_list)} files would be captured")
        return bundle_rel, 0, len(kept), False

    # Prepare payload
    captured_files = [f for f in file_list if path_allowed(f.get("filename", ""))]
    files_entries = []

    if bundle.exists():
        # Remove old content (except hook scripts, none expected)
        import shutil
        shutil.rmtree(bundle)
    bundle.mkdir(parents=True, exist_ok=True)
    keyfiles_dir = bundle / "key-files"

    bundle_total = 0

    # Whole-patch file
    diff_bytes = whole_diff
    if diff_bytes is not None:
        diff_path = bundle / "diff.patch"
        diff_path.write_bytes(diff_bytes)
        bundle_total += len(diff_bytes)
        files_entries.append({
            "local_path": "diff.patch",
            "role": "pr-diff",
            "mode": "upstream-patch",
            "sha256": sha256_bytes(diff_bytes),
        })

    # Per-file content at merge SHA
    for f in captured_files:
        filename = f.get("filename", "")
        status = f.get("status", "")
        if status == "removed":
            # Skip deleted files
            continue
        try:
            content = fetch_content_at_sha(repo, filename, merge_sha)
        except RuntimeError as e:
            print(f"    WARN: skipping {filename}: {e}", file=sys.stderr)
            continue
        local_rel = f"key-files/{filename}"
        out_path = bundle / local_rel
        # Per-file cap: truncate
        truncated = False
        if len(content) > FILE_SIZE_CAP:
            stub = (
                f"/* size_cap_truncated: upstream file is {len(content)} bytes "
                f"(> {FILE_SIZE_CAP}). Re-fetch upstream at {repo}:{filename}@{merge_sha} "
                f"to read the full content. */\n"
            ).encode("utf-8")
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_bytes(stub)
            content_for_sha = stub
            truncated = True
        else:
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_bytes(content)
            content_for_sha = content
        bundle_total += len(content_for_sha)
        entry = {
            "local_path": local_rel,
            "role": "upstream-file",
            "mode": "verbatim",
            "upstream_path": filename,
            "sha256": sha256_bytes(content_for_sha),
        }
        if truncated:
            entry["size_cap_truncated"] = True
        files_entries.append(entry)

    # Bundle cap: drop diff.patch if over
    bundle_truncated = False
    if bundle_total > BUNDLE_SIZE_CAP:
        diff_path = bundle / "diff.patch"
        if diff_path.is_file():
            drop_bytes = diff_path.stat().st_size
            diff_path.unlink()
            bundle_total -= drop_bytes
            # Remove the diff.patch entry from files_entries
            files_entries = [e for e in files_entries if e.get("local_path") != "diff.patch"]
            bundle_truncated = True

    # Write PROVENANCE.yaml
    prov = {
        "origin_url": f"https://github.com/{repo}/pull/{pr_num}",
        "upstream_repo": repo,
        "upstream_sha": merge_sha,
        "license": "inherits-from-upstream",
        "retrieved_at": _today(),
        "asset_mode": "verbatim",
        "size_cap_truncated": bundle_truncated,
        "generated_by": "scripts/fetch_pr_diff.py",
        "source_pr_id": pr_id,
        "files": files_entries,
    }
    (bundle / "PROVENANCE.yaml").write_text(
        yaml.dump(prov, sort_keys=False, allow_unicode=True, default_flow_style=False),
        encoding="utf-8",
    )

    return bundle_rel, bundle_total, len(files_entries), bundle_truncated


def _today():
    from datetime import date
    return date.today().isoformat()


def update_pr_page(md_path, original_text, bundle_rel):
    """Add or update `artifact_dir:` in the PR page frontmatter."""
    m = re.match(r"^(---\s*\r?\n)(.*?)(\r?\n---\s*\r?\n)(.*)", original_text, re.DOTALL)
    if not m:
        return False
    fm_text = m.group(2)
    try:
        fm = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError:
        return False
    fm["artifact_dir"] = str(bundle_rel)
    # Drop any banned peer pointers if they accidentally existed
    for banned in ("diff_path", "code_path", "patch_path", "key_file_path"):
        fm.pop(banned, None)
    new_fm = yaml.dump(fm, allow_unicode=True, sort_keys=False, default_flow_style=False).rstrip()
    md_path.write_text(m.group(1) + new_fm + m.group(3) + m.group(4), encoding="utf-8")
    return True


def select_pilot_ids(all_ids, all_prs_by_id):
    """Spread 20 PRs across the 5 tracked repos (4 per repo when available)."""
    buckets = {}
    for pid in all_ids:
        fm = all_prs_by_id.get(pid)
        if not fm:
            continue
        repo = (fm.get("repo") or "").split("/")[-1].lower()
        buckets.setdefault(repo, []).append(pid)
    pilot = []
    for repo in ("cutlass", "sglang", "vllm", "flashinfer", "pytorch"):
        ids = buckets.get(repo, [])[:4]
        pilot.extend(ids)
    # If we ended up with < 20, pad from remaining ids
    if len(pilot) < 20:
        for pid in all_ids:
            if pid not in pilot:
                pilot.append(pid)
                if len(pilot) >= 20:
                    break
    return pilot[:20]


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--pilot", action="store_true", help="Pilot: 20 PRs across 5 repos, then write size budget + stop")
    parser.add_argument("--all", action="store_true", help="Fetch every PR in data/core-prs.yaml")
    parser.add_argument("--ids", nargs="+", metavar="PR_ID", help="Fetch only these PR IDs")
    parser.add_argument("--dry-run", action="store_true", help="Print intent, do not call gh or write files")
    parser.add_argument("--max-pr", type=int, default=None, help="Stop after N PRs (safety gate)")
    args = parser.parse_args()

    core_ids = load_core_prs()
    # Load all PR pages once
    all_prs_by_id = {}
    for md in SOURCES_PRS.rglob("PR-*.md"):
        try:
            text = md.read_text(encoding="utf-8")
        except OSError:
            continue
        m = re.match(r"^---\s*\r?\n(.*?)\r?\n---", text, re.DOTALL)
        if not m:
            continue
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError:
            continue
        if fm.get("id"):
            all_prs_by_id[fm["id"]] = fm

    if args.ids:
        targets = list(args.ids)
    elif args.pilot:
        targets = select_pilot_ids(core_ids, all_prs_by_id)
        print(f"Pilot set: {len(targets)} PRs")
    elif args.all:
        targets = list(core_ids)
    else:
        parser.error("must pass --pilot, --all, or --ids")
    if args.max_pr:
        targets = targets[:args.max_pr]

    pilot_stats = []
    ok = 0
    for i, pid in enumerate(targets, start=1):
        fm = all_prs_by_id.get(pid)
        if not fm:
            print(f"  SKIP {pid}: no source page found")
            continue
        repo = fm.get("repo")
        pr_num = fm.get("pr")
        merge_sha = fm.get("merge_sha")
        if not (repo and pr_num and merge_sha):
            print(f"  SKIP {pid}: missing repo/pr/merge_sha in source page")
            continue

        print(f"[{i}/{len(targets)}] {pid}  ({repo}#{pr_num} @ {merge_sha[:10]})")
        if args.dry_run:
            continue
        try:
            file_list = fetch_pr_file_list(repo, pr_num)
        except RuntimeError as e:
            print(f"    WARN: file-list fetch failed: {e}", file=sys.stderr)
            continue
        try:
            whole_diff = fetch_pr_whole_diff(repo, pr_num)
        except RuntimeError as e:
            print(f"    WARN: diff fetch failed: {e}; continuing without diff.patch", file=sys.stderr)
            whole_diff = None

        try:
            bundle_rel, total, nfiles, truncated = emit_bundle(
                repo, pr_num, pid, merge_sha, file_list, whole_diff
            )
        except Exception as e:
            print(f"    ERROR: bundle emission failed: {e}", file=sys.stderr)
            continue

        print(f"    -> {bundle_rel} ({nfiles} files, {total/1024:.1f} KiB, truncated={truncated})")
        # Update source PR page with artifact_dir
        md_path, _fm, original_text = read_pr_page(pid)
        if md_path:
            update_pr_page(md_path, original_text, bundle_rel)
        ok += 1
        pilot_stats.append({
            "pr_id": pid,
            "repo": repo,
            "pr_number": pr_num,
            "bundle_bytes": total,
            "num_files": nfiles,
            "truncated": truncated,
        })

    print(f"\nFetched {ok}/{len(targets)} PRs successfully.")

    if args.pilot and pilot_stats:
        total_bytes = sum(s["bundle_bytes"] for s in pilot_stats)
        avg_bundle = total_bytes / len(pilot_stats)
        # Extrapolate
        core_total = len(core_ids)
        proj_lower = int(avg_bundle * min(80, core_total) * 1.25)  # lower-bound with 25% headroom
        proj_upper = int(avg_bundle * 460 * 1.25)
        budget = {
            "generated_by": "scripts/fetch_pr_diff.py --pilot",
            "pilot_size": len(pilot_stats),
            "pilot_total_bytes": total_bytes,
            "avg_bundle_bytes": int(avg_bundle),
            "core_prs_total": core_total,
            "lower_bound_projection_mib": round(proj_lower / (1024 * 1024), 2),
            "upper_bound_projection_mib": round(proj_upper / (1024 * 1024), 2),
            "active_ceiling_mib": 25 if proj_lower < 25 * 1024 * 1024 else (60 if proj_upper < 60 * 1024 * 1024 else proj_upper // (1024 * 1024) + 10),
            "pilot_entries": pilot_stats,
        }
        BUDGET_PATH.write_text(yaml.dump(budget, sort_keys=False, allow_unicode=True, default_flow_style=False), encoding="utf-8")
        print(f"\nWrote {BUDGET_PATH.relative_to(REPO_ROOT)}")
        print(f"  Avg bundle: {avg_bundle/1024:.1f} KiB")
        print(f"  Lower-bound projection: {budget['lower_bound_projection_mib']} MiB")
        print(f"  Upper-bound projection: {budget['upper_bound_projection_mib']} MiB")
        print(f"  Active ceiling: {budget['active_ceiling_mib']} MiB")


if __name__ == "__main__":
    main()
