# KernelWiki — Blackwell & Hopper Kernel Optimization Knowledge Base

> **Knowledge cutoff: 2026-04-27.** All upstream PRs, blog snapshots, and version-claim entries are anchored to upstream state on or before this date (recorded in [`data/refresh-cutoff.yaml`](data/refresh-cutoff.yaml)). Triton claims pin to release **3.6.0** (released 2026-01-21); CUTLASS claims pin to **4.5.0** (released 2026-03-27); see [`data/tool-versions.yaml`](data/tool-versions.yaml) for all tracked tools. To advance the cutoff, run `scripts/refresh_candidate_ledger.py`, regenerate PR pages, and bump the cutoff date file.

A structured knowledge base of NVIDIA Blackwell (SM100, B200) and Hopper (SM90, H100) GPU kernel optimization, packaged as a Claude Code skill. The repository root **is** the skill directory — clone it directly into `~/.claude/skills/` and it works out of the box.

## Install as a Claude Code Skill

```bash
git clone git@github.com:DongyunZou/KernelWiki.git ~/.claude/skills/KernelWiki
pip install -r ~/.claude/skills/KernelWiki/requirements.txt
```

That's it. The skill auto-registers (because `SKILL.md` lives at the clone root), and the query scripts auto-resolve the wiki root to their own directory — no environment variable required.

Smoke test:

```bash
cd ~/.claude/skills/KernelWiki
python3 scripts/query.py --tag nvfp4 --type kernel --compact
python3 scripts/get_page.py kernel-flash-attention-4 --frontmatter-only
```

Optional override for relocating the scripts:

```bash
export BLACKWELL_WIKI_ROOT=/path/to/KernelWiki
```

## What's Here

- **2,179 PR references** from NVIDIA/cutlass (32), sgl-project/sglang (645), vllm-project/vllm (833), flashinfer-ai/flashinfer (583), pytorch/pytorch (85), deepseek-ai/DeepGEMM (1) — Jan 2025 – Apr 2026
- **48 synthesized wiki pages** — hardware features, techniques, kernel case studies, problem patterns, DSL guides, migration guides
- **20 community blog summaries**, **11 official doc summaries**, **7 competition pages** (GPU Mode NVFP4 hackathon, FlashInfer MLSys 2026)
- **89 verbatim/extracted/derived asset bundles** under `artifacts/` (PR diffs, kernel files, blog code) — pinned to upstream SHAs via `PROVENANCE.yaml`
- **6 auto-generated cross-reference indices** — by problem / technique / hardware feature / repo / kernel type / language
- **6 candidate ledgers** tracking 4,222 merged PRs with include/defer/exclude decisions
- **Hybrid version-claim registry** ([`data/version-claims.yaml`](data/version-claims.yaml)) — per-page `version_sensitive: <id>` pointers + central registry, validated for bidirectional consistency

## Query Tools

All tools run from the skill root, no env var needed.

| Tool | Purpose |
|---|---|
| `scripts/query.py` | Unified search across 2,265 pages (keywords + filters + alias-aware) |
| `scripts/get_page.py` | Fetch any page by `id` or path; `--follow-sources` expands cited sources |
| `scripts/grep_wiki.py` | Regex text search across wiki bodies and PR pages |

Examples:

```bash
python3 scripts/query.py "ping-pong attention" --limit 5
python3 scripts/query.py --tag UMMA --type hardware --compact          # alias → tcgen05
python3 scripts/query.py --architecture B200 --type kernel             # alias → sm100
python3 scripts/get_page.py kernel-flash-attention-4 --follow-sources
python3 scripts/grep_wiki.py "tcgen05\\.fence" --only wiki
```

## Companion Docs

- [`SKILL.md`](SKILL.md) — Skill entry point: when to engage, 5 navigation paths, output contract.
- [`references/primer.md`](references/primer.md) — Topic map: hardware features, techniques, kernels, symptoms → canonical page IDs.
- [`references/schema.md`](references/schema.md) — Frontmatter schema, confidence rules, reproducibility ladder, controlled vocabulary, canonical aliases.
- [`references/examples.md`](references/examples.md) — 10 worked query patterns (user question → command sequence → synthesis).
- [`CLAUDE.md`](CLAUDE.md) — Extended schema + navigation reference for Claude Code.
- [`index.md`](index.md) — Human-facing curated top-level index.

## Architecture

Three layers (inspired by [Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)):

1. **`sources/`** — Raw data. Immutable summaries of PRs, blogs, docs, contests.
2. **`wiki/`** — Synthesized knowledge pages. Cross-referenced by `id`. All have YAML frontmatter.
3. **`queries/`** — Auto-generated cross-reference indices. Do not edit manually; regenerate via `scripts/generate-indices.py`.

Supporting files:
- `data/schemas.yaml` — Required/optional fields per page type
- `data/tags.yaml` — Controlled vocabulary (80+ tags)
- `data/aliases.yaml` — Canonical → synonym mappings
- `data/version-claims.yaml` — Central registry for version-sensitive claims (DEC-1 hybrid)
- `data/tool-versions.yaml` — Snapshot of tracked tool releases (Triton, CUTLASS, CUDA, PTX, …)
- `data/refresh-cutoff.yaml` — Single source of truth for the knowledge cutoff date
- `candidates/` — Reviewed PR candidate ledgers (per repo)
- `artifacts/` — Verbatim / extracted / derived asset bundles, each with `PROVENANCE.yaml`

## Maintenance Tooling

| Script | Purpose |
|---|---|
| `scripts/validate.py` | Validate YAML frontmatter, enforce schema, check link integrity |
| `scripts/generate-indices.py` | Regenerate `queries/*.md` from frontmatter |
| `scripts/generate-pr-pages.py` | Batch-generate source PR pages from candidate ledgers |

```bash
pip install -r requirements.txt
python3 scripts/validate.py            # reports 2265 files / 89 bundles / 6 ledgers, 0 errors
python3 scripts/generate-indices.py    # regenerate query indices
```

## Quality Gates (knowledge cutoff: 2026-04-27)

- 2,265 files, 2,217 source IDs, 0 validation errors
- 89 asset bundles validated (verbatim=64, extracted=13, derived=12)
- 6 candidate ledgers normalized
- 0 broken links across all internal references
- All `verified` wiki pages have official-doc + upstream-code evidence (enforced by `evidence_basis` field)
- All technique/kernel/language pages have compilable code snippets (`reproducibility >= snippet`)
- All Hopper-inclusive pages explain their `blackwell_relevance`
- Version-sensitive claims (Triton 3.6, CUTLASS 4.5, etc.) carry `version_sensitive: <id>` pointers resolving to the central registry

## Scope Rules

- **Blackwell-first** — SM100 content is primary. SM90 requires explicit `blackwell_relevance` field.
- **Kernel-only** — No distributed-system topics (DeepEP, DualPipe, EPLB are out of scope).
- **English canonical** — All content in English.
- **First-class DSLs** — CuTe DSL, CUDA C++, PTX, Triton. TileLang / cuTile / JAX-Pallas mentioned but no dedicated guides.

## Repository Layout

```
KernelWiki/                             (= ~/.claude/skills/KernelWiki/)
├── SKILL.md                           # Skill entry point
├── README.md                          # This file
├── CLAUDE.md                          # Extended navigation + schema reference
├── index.md                           # Curated top-level index
├── requirements.txt                   # PyYAML
│
├── scripts/                           # Query tools + maintenance tooling
│   ├── query.py                       # Unified search
│   ├── get_page.py                    # Page fetcher
│   ├── grep_wiki.py                   # Regex search
│   ├── _wiki_root.py                  # Shared root resolver
│   ├── validate.py                    # Schema validator
│   ├── generate-indices.py            # Query-index generator
│   └── generate-pr-pages.py           # Batch PR page generator
│
├── references/                        # Skill knowledge layer
│   ├── primer.md                      # Topic map
│   ├── schema.md                      # Condensed schema reference
│   └── examples.md                    # 10 worked query patterns
│
├── data/                              # Schema + vocabulary
│   ├── schemas.yaml
│   ├── tags.yaml
│   └── aliases.yaml
│
├── candidates/                        # Reviewed PR ledgers (ingestion source of truth)
│   ├── cutlass.yaml
│   ├── sglang.yaml
│   ├── vllm.yaml
│   ├── flashinfer.yaml
│   ├── pytorch.yaml
│   └── deepgemm.yaml
│
├── sources/                           # Layer 1: raw data
│   ├── prs/{repo}/PR-{N}.md
│   ├── contests/{contest}/
│   ├── docs/
│   └── blogs/
│
├── wiki/                              # Layer 2: synthesized knowledge
│   ├── hardware/
│   ├── techniques/
│   ├── kernels/
│   ├── patterns/
│   ├── languages/
│   └── migration/
│
└── queries/                           # Layer 3: auto-generated indices
    ├── by-problem.md
    ├── by-technique.md
    ├── by-hardware-feature.md
    ├── by-repo.md
    ├── by-kernel-type.md
    └── by-language.md
```

## License

Summaries and wiki syntheses in this repository are derivative works citing upstream PRs, blogs, and docs. The tooling (`scripts/`, `references/`, `data/`) is MIT-style; see individual files for any exceptions.
