#!/usr/bin/env python3
"""Verify the data/core-prs.yaml derivation is reproducible (AC-1).

Modes:
  default — regenerate in memory and diff against committed bytes
  --strict — additionally resolve each captured PR's merge_sha via `gh api`
             and flag reverted / unresolvable / prefix-mismatched entries

Exit codes:
  0 — every committed manifest is byte-equal to a fresh in-memory derivation
      (and, in --strict, every merge_sha prefix-matches upstream)
  1 — mismatch or upstream-state problem
  2 — invocation error (missing inputs, no gh, etc.)

Runs in fully read-only sandboxes: the reproducibility check imports
compute_core_prs.compute_manifests() directly and holds the regenerated
bytes in memory rather than shelling out + writing to a temp directory.
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CORE_PATH = REPO_ROOT / "data" / "core-prs.yaml"

# Import the in-memory regenerator.
sys.path.insert(0, str(REPO_ROOT / "scripts"))
import compute_core_prs  # noqa: E402


def run_gh(args):
    try:
        res = subprocess.run(["gh"] + list(args), stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return res.stdout
    except FileNotFoundError:
        raise RuntimeError("gh CLI not found")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"gh {' '.join(args)} failed: {e.stderr.decode(errors='replace')}")


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--strict", action="store_true", help="Also resolve merge_sha via gh api")
    args = parser.parse_args()

    if not CORE_PATH.is_file():
        print(f"ERROR: {CORE_PATH.relative_to(REPO_ROOT)} does not exist; run scripts/compute_core_prs.py first", file=sys.stderr)
        sys.exit(2)

    # Snapshot the committed bytes of every generated manifest under data/.
    generated_names = ("core-prs.yaml", "cute-dsl-universe.yaml", "triton-universe.yaml")
    all_tracked = True
    committed_bytes = {}
    for name in generated_names:
        path = REPO_ROOT / "data" / name
        if path.is_file():
            committed_bytes[name] = path.read_bytes()
        else:
            committed_bytes[name] = None
            all_tracked = False

    # Regenerate the three manifests ENTIRELY IN MEMORY. This keeps the
    # verifier usable in fully read-only sandboxes (no /tmp, no $HOME/.cache,
    # no writable cwd, no writable REPO_ROOT) — the original bug Codex
    # raised in Rounds 12 / 15 against the subprocess-plus-temp-dir design.
    try:
        fresh_bytes = compute_core_prs.compute_manifests()
    except RuntimeError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(2)
    # Sanity-check that compute_manifests() produced exactly the expected
    # manifest set; a mismatch would indicate a generator/verifier drift bug.
    missing = [name for name in generated_names if name not in fresh_bytes]
    if missing:
        print(f"ERROR: compute_manifests() did not produce {missing}", file=sys.stderr)
        sys.exit(1)

    fresh = yaml.safe_load(fresh_bytes["core-prs.yaml"].decode("utf-8"))

    if not all_tracked:
        # First run: no committed version for at least one generated file yet.
        print(f"No committed version found for at least one generated file under data/.")
        print(f"Fresh derivation: {fresh.get('total_captured', 0)} PRs, "
              f"checksum {fresh.get('checksum_sha256', '')[:12]}...")
        print("(skip reproducibility comparison; commit the files first, then re-run)")
    else:
        # Byte-for-byte comparison: compute_core_prs.py guarantees
        # byte-identical output for unchanged inputs (no timestamp stamping),
        # so any difference at this level is a real regeneration divergence.
        drift = []
        for name in generated_names:
            if committed_bytes[name] != fresh_bytes[name]:
                drift.append(Path("data") / name)
        if drift:
            print("FAIL: fresh regeneration does not match the committed generated files:",
                  file=sys.stderr)
            for p in drift:
                print(f"  drifted: {p}", file=sys.stderr)
            print(
                "\n(If you believe the drift is legitimate, re-run "
                "scripts/compute_core_prs.py and commit the updated files; "
                "re-run this verifier to confirm.)",
                file=sys.stderr,
            )
            sys.exit(1)
        # Cross-check internal consistency: total_captured must match len(prs),
        # and the embedded checksum_sha256 must re-compute correctly.
        import hashlib as _hl
        prs_list = fresh.get("prs") or []
        if fresh.get("total_captured") != len(prs_list):
            print(
                f"FAIL: data/core-prs.yaml total_captured={fresh.get('total_captured')} "
                f"does not match len(prs)={len(prs_list)}",
                file=sys.stderr,
            )
            sys.exit(1)
        # The checksum algorithm in compute_core_prs.py hashes the yaml.dump of
        # prs_list. Re-dump with the same options and compare.
        checksum_body = yaml.dump(prs_list, allow_unicode=True, sort_keys=False,
                                  default_flow_style=False)
        expected = _hl.sha256(checksum_body.encode("utf-8")).hexdigest()
        if fresh.get("checksum_sha256") != expected:
            print(
                f"FAIL: embedded checksum_sha256 does not match re-computed hash\n"
                f"  embedded   : {fresh.get('checksum_sha256', '')[:20]}...\n"
                f"  re-computed: {expected[:20]}...",
                file=sys.stderr,
            )
            sys.exit(1)
        print(f"OK: all 3 generated manifests (core-prs, cute-dsl-universe, "
              f"triton-universe) match committed bytes; internal checksum + "
              f"total_captured are consistent (checksum {fresh.get('checksum_sha256','')[:12]}..., "
              f"{fresh.get('total_captured',0)} PRs)")

    # --strict: resolve merge_sha via gh api
    if args.strict:
        issues = 0
        pr_entries = (fresh or {}).get("prs") or []
        # Load sources/prs/**/*.md to find each PR's merge_sha + repo
        sources_prs = {}
        for md in (REPO_ROOT / "sources" / "prs").rglob("PR-*.md"):
            import re as _re
            try:
                text = md.read_text(encoding="utf-8")
            except OSError:
                continue
            m = _re.match(r"^---\s*\n(.*?)\n---", text, _re.DOTALL)
            if not m:
                continue
            try:
                fm = yaml.safe_load(m.group(1)) or {}
            except yaml.YAMLError:
                continue
            if fm.get("id"):
                sources_prs[fm["id"]] = fm

        print(f"Resolving merge_sha for {len(pr_entries)} PRs via gh api...")
        for e in pr_entries:
            pid = e.get("id")
            fm = sources_prs.get(pid)
            if not fm:
                print(f"  WARN: {pid}: page not found in sources/prs/")
                issues += 1
                continue
            sha = fm.get("merge_sha")
            repo = fm.get("repo")
            pr_num = fm.get("pr")
            if not (sha and repo and pr_num):
                print(f"  WARN: {pid}: missing merge_sha / repo / pr number")
                issues += 1
                continue
            try:
                out = run_gh(["api", f"/repos/{repo}/pulls/{pr_num}"])
                data = json.loads(out)
                if not data.get("merged"):
                    print(f"  FAIL: {pid}: upstream state is not merged (state={data.get('state')})")
                    issues += 1
                else:
                    # sources/prs/**/*.md stores abbreviated 8-char merge_sha
                    # values; gh returns the full 40-char merge_commit_sha.
                    # Accept the stored value as a valid prefix of either the
                    # full merge_commit_sha or head.sha — same convention
                    # scripts/verify_verbatim.py uses.
                    upstream_merge = str(data.get("merge_commit_sha") or "")
                    upstream_head = str((data.get("head") or {}).get("sha") or "")
                    ok = any(
                        upstream and upstream.startswith(sha)
                        for upstream in (upstream_merge, upstream_head)
                    )
                    if not ok:
                        print(
                            f"  FAIL: {pid}: recorded merge_sha={sha[:12]}... does not prefix-match "
                            f"upstream merge_commit_sha={upstream_merge[:12]}... or head.sha={upstream_head[:12]}..."
                        )
                        issues += 1
            except RuntimeError as ex:
                print(f"  WARN: {pid}: gh fetch failed: {ex}")
                issues += 1

        if issues:
            print(f"\n{issues} strict-mode flag(s).")
            sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
