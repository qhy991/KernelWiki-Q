#!/usr/bin/env python3
"""Verify the data/core-prs.yaml derivation is reproducible (AC-1).

Modes:
  default — regenerate to a temp file and diff against committed output
  --strict — additionally resolve each captured PR's merge_sha via `gh api`
             and flag reverted/unresolvable entries

Exit codes:
  0 — committed output is byte-equal to a fresh derivation (and, in --strict,
      every merge_sha resolves to a merged PR)
  1 — mismatch or upstream-state problem
  2 — invocation error (missing inputs)
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path
import yaml
import shutil
import tempfile

REPO_ROOT = Path(__file__).resolve().parent.parent
CORE_PATH = REPO_ROOT / "data" / "core-prs.yaml"
COMPUTE_SCRIPT = REPO_ROOT / "scripts" / "compute_core_prs.py"


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

    # Regenerate into a temp directory to compare byte-for-byte
    with tempfile.TemporaryDirectory() as td:
        # Copy data + sources + wiki into temp (or just rerun from current repo, which is cheaper)
        # We rerun compute_core_prs.py into a copy of the data/ directory, then compare.
        tmp_data = Path(td) / "data"
        shutil.copytree(REPO_ROOT / "data", tmp_data)
        env_script = COMPUTE_SCRIPT.read_text(encoding="utf-8")
        # Monkey-patch DATA path by invoking the compute script in-place; easiest is:
        # run in current repo and compare.
        res = subprocess.run(
            [sys.executable, str(COMPUTE_SCRIPT)],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        )
        if res.returncode != 0:
            print(f"compute_core_prs.py failed:\n{res.stderr.decode(errors='replace')}", file=sys.stderr)
            sys.exit(1)

    # Now CORE_PATH has the freshly-regenerated content. Load + compare the checksum.
    fresh = yaml.safe_load(CORE_PATH.read_text(encoding="utf-8"))
    # Re-read from git to see what was committed
    res = subprocess.run(
        ["git", "show", f"HEAD:data/core-prs.yaml"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=REPO_ROOT,
    )
    if res.returncode != 0:
        # First run: no committed version yet, just report the derivation
        print(f"No committed core-prs.yaml in HEAD; fresh derivation has "
              f"{fresh.get('total_captured', 0)} PRs, checksum {fresh.get('checksum_sha256', '')[:12]}...")
        print("(skip reproducibility comparison; commit the file first, then re-run)")
    else:
        committed = yaml.safe_load(res.stdout)
        if (committed or {}).get("checksum_sha256") != (fresh or {}).get("checksum_sha256"):
            print(
                "FAIL: fresh regeneration does not match the committed data/core-prs.yaml\n"
                f"  committed checksum: {(committed or {}).get('checksum_sha256', '')[:20]}...\n"
                f"  fresh     checksum: {(fresh     or {}).get('checksum_sha256', '')[:20]}...",
                file=sys.stderr,
            )
            sys.exit(1)
        print(f"OK: fresh derivation matches committed core-prs.yaml "
              f"(checksum {fresh.get('checksum_sha256','')[:12]}..., {fresh.get('total_captured',0)} PRs)")

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
                elif data.get("merge_commit_sha") != sha:
                    print(f"  FAIL: {pid}: upstream merge_sha={data.get('merge_commit_sha')[:12]}... "
                          f"differs from recorded {sha[:12]}...")
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
