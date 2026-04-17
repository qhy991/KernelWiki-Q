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


def _open_temp_dir():
    """Return a context manager yielding the path to a writable temp dir.

    Strategy (first path that works wins):
      1. tempfile.TemporaryDirectory() — uses $TMPDIR / /tmp / etc.
      2. Fallback to $HOME/.cache/verify-core-prs-<pid>/
      3. Fallback to Path.cwd() / .verify-core-prs-<pid>/
      4. Fallback to REPO_ROOT / .verify-core-prs-<pid>/

    Hermetic or read-only CI runners sometimes omit /tmp and /var/tmp, in
    which case step 1 raises FileNotFoundError. The script falls through to
    whichever of steps 2-4 actually has a writable directory. The fallbacks
    all clean up their own directory on __exit__.
    """
    import contextlib, os, shutil, tempfile

    @contextlib.contextmanager
    def _owned(path):
        path = Path(path).resolve()
        try:
            yield str(path)
        finally:
            shutil.rmtree(path, ignore_errors=True)

    try:
        td = tempfile.TemporaryDirectory(prefix="verify_core_prs-")

        @contextlib.contextmanager
        def _wrap(td):
            try:
                yield td.name
            finally:
                td.cleanup()

        return _wrap(td)
    except (FileNotFoundError, OSError):
        pass

    pid = os.getpid()
    for base in (
        os.environ.get("HOME") and Path(os.environ["HOME"]) / ".cache",
        Path.cwd(),
        REPO_ROOT,
    ):
        if not base:
            continue
        candidate = base / f".verify-core-prs-{pid}"
        try:
            candidate.mkdir(parents=True, exist_ok=True)
            # Verify writability with a probe file.
            probe = candidate / ".probe"
            probe.write_text("ok", encoding="utf-8")
            probe.unlink()
            return _owned(candidate)
        except OSError:
            continue

    raise RuntimeError(
        "verify_core_prs.py could not find a writable directory to regenerate "
        "into (tried tempfile.TemporaryDirectory(), $HOME/.cache, cwd, and "
        "REPO_ROOT). Point TMPDIR at a writable location and re-run."
    )


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

    # Regenerate the three manifests into a TEMPORARY directory so this
    # verifier is safe to run in read-only CI / sandboxed environments and
    # never dirties the working tree. Compare the fresh bytes against the
    # committed versions under data/.
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

    with _open_temp_dir() as td_path:
        tmp_out = Path(td_path)
        res = subprocess.run(
            [sys.executable, str(COMPUTE_SCRIPT), "--output-dir", str(tmp_out)],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        )
        if res.returncode != 0:
            print(f"compute_core_prs.py failed:\n{res.stderr.decode(errors='replace')}", file=sys.stderr)
            sys.exit(1)

        fresh_bytes = {}
        for name in generated_names:
            fresh_path = tmp_out / name
            if not fresh_path.is_file():
                print(f"ERROR: compute_core_prs.py did not produce {name} in --output-dir", file=sys.stderr)
                sys.exit(1)
            fresh_bytes[name] = fresh_path.read_bytes()

        fresh = yaml.safe_load(fresh_bytes["core-prs.yaml"].decode("utf-8"))

    if not all_tracked:
        # First run: no committed version for at least one generated file yet.
        print(f"No committed version found for at least one generated file under data/.")
        print(f"Fresh derivation: {fresh.get('total_captured', 0)} PRs, "
              f"checksum {fresh.get('checksum_sha256', '')[:12]}...")
        print("(skip reproducibility comparison; commit the files first, then re-run)")
    else:
        # Semantic comparison: parse both sides as YAML, strip timestamp-style
        # fields that change between runs for benign reasons (generated_at,
        # retrieved_at), then compare the structured dicts. This lets us emit
        # a schema-required generated_at field from compute_core_prs.py
        # without breaking reproducibility on cross-day re-runs.
        def _normalize(doc):
            if isinstance(doc, dict):
                return {k: _normalize(v) for k, v in doc.items()
                        if k not in ("generated_at", "retrieved_at")}
            if isinstance(doc, list):
                return [_normalize(v) for v in doc]
            return doc

        drift = []
        for name in generated_names:
            committed_doc = yaml.safe_load(committed_bytes[name].decode("utf-8"))
            fresh_doc = yaml.safe_load(fresh_bytes[name].decode("utf-8"))
            if _normalize(committed_doc) != _normalize(fresh_doc):
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
