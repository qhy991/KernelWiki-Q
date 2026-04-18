# Phase 3 SHA-pinned strict verify audit log

Captured: 2026-04-17T23:37:21Z (R25 refresh: same 7 pytorch PRs refetched again after the R25 atomic-swap changes; the gh abbreviation cache flipped between sessions, so local diff.patch bytes needed re-alignment with the upstream 12-char abbreviation.)
Command : `python3 scripts/verify_verbatim.py --strict`
Exit    : 0 (documented contract: 0 = full-corpus upstream byte-match; 1 = --strict content mismatch; 2 = env failure)

## Environment

```
gh version 2.90.0 (2026-04-16)
  ✓ Logged in to github.com account DongyunZou (/home/dongyun/.config/gh/hosts.yml)
```

## Scope

- 91 asset bundles under `artifacts/` (94 post-R27 − 3 Triton PRs
  dropped in R30 because their titles carried non-Blackwell vendor
  prefixes — `[ROCm]` for pr-pytorch-170190, `[Intel GPU]` for
  pr-pytorch-163388, `[XPU]` for pr-vllm-39088; `architectures:
  [sm100]` was incidental Triton-backend coverage, not Blackwell
  kernel authorship. Also dropped the synthesized pseudo-code
  `ping-pong-scheduling-from-fa4-blog.cu` from `artifacts/kernels/
  ping-pong-scheduling/full/` — it contained placeholders like
  `issue_mma`, `wait_mma`, and should not have been published under
  `mode: extracted` per the Codex R30 P1 finding.)
- 301 files with `mode: verbatim` or `mode: upstream-patch` and no `size_cap_truncated` marker (was 310; minus the files in the 3 dropped vendor-prefixed PR bundles and the pseudo-code file in ping-pong-scheduling/full)

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
