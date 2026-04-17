# Phase 3 SHA-pinned strict verify audit log

Captured: 2026-04-17T18:38:43Z
Command : `python3 scripts/verify_verbatim.py --strict`
Exit    : 0 (0 = full-corpus upstream byte-match; 1 = content mismatch under --strict; 2 = env failure)

## Environment

```
gh version 2.90.0 (2026-04-16)
  ✓ Logged in to github.com account DongyunZou (/home/dongyun/.config/gh/hosts.yml)
```

## Scope

- 76 asset bundles under `artifacts/`
- 294 files with `mode: verbatim` or `mode: upstream-patch` and no `size_cap_truncated` marker (every one is fetched from upstream and byte-compared)

## stdout

```
Verified 76 bundle(s).
All verbatim/upstream-patch assets match upstream.
```

## Interpretation

`exit=0` = every verbatim / upstream-patch file in the corpus byte-matches its upstream at the pinned SHA. AC-2's strongest check passes.

## Reproducibility

This log is the committed evidence for AC-2's upstream byte-match requirement. A reviewer who wants to re-run the audit should:

1. Install gh CLI and run `gh auth login`.
2. From the repo root: `python3 scripts/verify_verbatim.py --strict`.
3. Compare the exit code + stdout line count to what is recorded above.

The verifier is deterministic given the same upstream state. The only legitimate reasons for drift since this log was captured would be: an upstream amend (caught by the merge_commit_sha prefix check and reported as byte mismatch), or upstream repo/content deletion (caught as env error at exit 2).
