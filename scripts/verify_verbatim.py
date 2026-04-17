#!/usr/bin/env python3
"""Byte-match every asset_mode=verbatim / upstream-patch file against upstream.

Walks artifacts/*/PROVENANCE.yaml, finds each files[*] whose mode is 'verbatim'
or 'upstream-patch', fetches the upstream content via `gh api` (for verbatim)
or `gh pr diff` (for upstream-patch), and compares bytes.

Exit codes:
  0 — all verbatim/upstream-patch assets match their pinned upstream
  1 — at least one mismatch (reported to stderr)
  2 — invocation / environment error (missing gh, network, bad input)

Usage:
  scripts/verify_verbatim.py            # warn-only
  scripts/verify_verbatim.py --strict   # fail on any mismatch
  scripts/verify_verbatim.py --bundle artifacts/prs/cutlass/PR-2161
"""

import argparse
import hashlib
import subprocess
import sys
from pathlib import Path
import yaml
import base64
import json

REPO_ROOT = Path(__file__).resolve().parent.parent
ARTIFACTS_DIR = REPO_ROOT / "artifacts"


def run_gh(args):
    """Run gh CLI. Return stdout bytes on success, raise RuntimeError on failure."""
    try:
        res = subprocess.run(
            ["gh"] + list(args),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
        )
        return res.stdout
    except FileNotFoundError:
        raise RuntimeError("gh CLI not found; install from https://cli.github.com/")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"gh {' '.join(args)} failed: {e.stderr.decode(errors='replace')}")


def fetch_verbatim(upstream_repo, upstream_sha, upstream_path):
    """Fetch a single file's bytes from GitHub at the pinned SHA."""
    # gh api /repos/{owner}/{repo}/contents/{path}?ref={sha}
    endpoint = f"/repos/{upstream_repo}/contents/{upstream_path}?ref={upstream_sha}"
    out = run_gh(["api", endpoint])
    data = json.loads(out)
    if "content" not in data:
        raise RuntimeError(f"no content in response for {upstream_repo}:{upstream_path}@{upstream_sha}")
    return base64.b64decode(data["content"])


def fetch_upstream_patch(upstream_repo, pr_number):
    """Fetch the PR's diff via gh pr diff."""
    # Format: gh pr diff <N> -R owner/repo
    out = run_gh(["pr", "diff", str(pr_number), "-R", upstream_repo])
    return out


def iter_bundles(scope):
    if scope:
        yield Path(scope).resolve()
        return
    if not ARTIFACTS_DIR.is_dir():
        return
    for prov in ARTIFACTS_DIR.rglob("PROVENANCE.yaml"):
        yield prov.parent


def verify_bundle(bundle_root):
    prov_path = bundle_root / "PROVENANCE.yaml"
    if not prov_path.is_file():
        return [f"{bundle_root.relative_to(REPO_ROOT)}: missing PROVENANCE.yaml"]
    try:
        prov = yaml.safe_load(prov_path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as e:
        return [f"{prov_path.relative_to(REPO_ROOT)}: YAML parse error: {e}"]

    upstream_repo = prov.get("upstream_repo")
    upstream_sha = prov.get("upstream_sha")
    errors = []

    for i, entry in enumerate(prov.get("files") or []):
        if not isinstance(entry, dict):
            continue
        mode = entry.get("mode")
        if mode not in ("verbatim", "upstream-patch"):
            continue
        if entry.get("size_cap_truncated"):
            continue
        lp = entry.get("local_path")
        if not lp:
            continue
        local_path = bundle_root / lp
        if not local_path.is_file():
            errors.append(f"{bundle_root.relative_to(REPO_ROOT)}/{lp}: local file missing")
            continue
        local_bytes = local_path.read_bytes()

        try:
            if mode == "verbatim":
                upstream_path = entry.get("upstream_path")
                if not (upstream_repo and upstream_sha and upstream_path):
                    errors.append(
                        f"{bundle_root.relative_to(REPO_ROOT)}/{lp}: verbatim mode requires "
                        f"upstream_repo + upstream_sha + upstream_path"
                    )
                    continue
                upstream_bytes = fetch_verbatim(upstream_repo, upstream_sha, upstream_path)
            else:  # upstream-patch
                # derive PR number from bundle path: artifacts/prs/<repo>/PR-<N>/
                parts = bundle_root.parts
                if "PR-" not in bundle_root.name:
                    errors.append(
                        f"{bundle_root.relative_to(REPO_ROOT)}/{lp}: upstream-patch mode requires "
                        f"bundle name like PR-<N>"
                    )
                    continue
                pr_num = bundle_root.name.replace("PR-", "")
                upstream_bytes = fetch_upstream_patch(upstream_repo, pr_num)
        except RuntimeError as e:
            errors.append(f"{bundle_root.relative_to(REPO_ROOT)}/{lp}: upstream fetch failed: {e}")
            continue

        if upstream_bytes != local_bytes:
            local_sha = hashlib.sha256(local_bytes).hexdigest()[:12]
            upstream_sha12 = hashlib.sha256(upstream_bytes).hexdigest()[:12]
            errors.append(
                f"{bundle_root.relative_to(REPO_ROOT)}/{lp}: {mode} byte mismatch "
                f"(local {local_sha}..., upstream {upstream_sha12}...)"
            )
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--strict", action="store_true", help="Exit 1 on any mismatch (default: warn-only exit 0)")
    parser.add_argument("--bundle", help="Verify a single bundle root instead of all")
    args = parser.parse_args()

    if not ARTIFACTS_DIR.is_dir():
        print("No artifacts/ directory; nothing to verify.")
        sys.exit(0)

    all_errors = []
    bundles_checked = 0
    for bundle in iter_bundles(args.bundle):
        bundles_checked += 1
        errs = verify_bundle(bundle)
        all_errors.extend(errs)

    print(f"Verified {bundles_checked} bundle(s).")
    if all_errors:
        for e in all_errors:
            print(f"  WARN: {e}", file=sys.stderr)
        print(f"\n{len(all_errors)} mismatch(es) found.", file=sys.stderr)
        sys.exit(1 if args.strict else 0)
    print("All verbatim/upstream-patch assets match upstream.")
    sys.exit(0)


if __name__ == "__main__":
    main()
