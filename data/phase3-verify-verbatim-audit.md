# Phase 3 SHA-pinned strict verify audit log

Captured: 2026-04-17T21:29:28Z (refreshed after Round 17 bundle backfill; Round 19 dropped 2 diff.patch-only bundles and refetched pr-sglang-21780 via the relaxed allowlist)
Command : `python3 scripts/verify_verbatim.py --strict`
Exit    : 0 (documented contract: 0 = full-corpus upstream byte-match; 1 = --strict content mismatch; 2 = env failure)

## Environment

```
gh version 2.90.0 (2026-04-16)
  ✓ Logged in to github.com account DongyunZou (/home/dongyun/.config/gh/hosts.yml)
```

## Scope

- 91 asset bundles under `artifacts/` (76 pre-R17 + 17 Triton-universe
  PRs fetched in Round 17 + 1 Round-18 key-file backfill for
  pr-vllm-22738 − 2 bundles dropped in Round 19 after the
  tests/benchmarks skip tightening removed pr-sglang-20305 and
  pr-vllm-39644 from the core set; pr-sglang-21780 refetched with
  key-files via the R18 relaxed allowlist)
- 312 files with `mode: verbatim` or `mode: upstream-patch` and no `size_cap_truncated` marker

## stdout

```
Verified 91 bundle(s).
All verbatim/upstream-patch assets match upstream.
```

## Exit-code contract (Round 6)

`scripts/verify_verbatim.py` classifies `gh` stderr via a substring allow-list
(`_ENV_ERROR_HINTS`) that covers the DNS / TCP / TLS / proxy / auth / rate-limit
failure modes as well as generic transport strings like `error connecting`,
`failed to connect`, `couldn't connect`, `cannot reach`, and equivalents. A hit
raises `EnvError` and contributes to the `ENV:` stream (exit 2); any other
failure contributes to the `WARN:` stream (exit 1 under `--strict`).

Reproducing an environment failure here (by prepending a fake `gh` shim that
emits `error connecting to api.github.com`) makes the verifier emit
`ENV:` lines and return `exit 2`, confirming the contract end-to-end on the
path Codex's review environment takes.

## Reproducibility

1. Install gh CLI and run `gh auth login`.
2. From the repo root: `python3 scripts/verify_verbatim.py --strict`.
3. Compare the exit code + stdout against this log. In a network-capable
   environment the expected exit is 0 and the stdout is
   "Verified 76 bundle(s). / All verbatim/upstream-patch assets match upstream."
4. In an offline environment the verifier correctly exits 2 (`ENV:` stream),
   NOT 1 — proving the contract separates env failure from content mismatch.
