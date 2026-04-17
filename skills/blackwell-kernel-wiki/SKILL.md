---
name: blackwell-kernel-wiki
description: Use when the user asks about optimizing NVIDIA Blackwell (SM100, B200) or Hopper (SM90, H100) GPU kernels — tcgen05/TMEM/CLC/NVFP4/2-SM cooperative, warp specialization, FlashAttention-4, DeepGEMM, FlashMLA, MoE, grouped GEMM, CuTe-DSL/PTX/Triton on Blackwell, or wants concrete PR references from CUTLASS/SGLang/vLLM/FlashInfer/PyTorch. Do NOT use for generic CUDA Q&A that is not Blackwell/Hopper-specific, host-side framework integration, or distributed systems (DeepEP/EPLB/DualPipe).
argument-hint: "[natural-language-question] | [--tag foo --type kernel] | [page-id]"
allowed-tools: "Bash,Read,Grep,Glob"
---

# Blackwell Kernel Wiki

Query a structured, cross-referenced knowledge base of GPU kernel optimization for NVIDIA Blackwell (SM100) and Hopper (SM90) — 460+ merged PRs, 48 wiki synthesis pages, 7 competitions, 20 blogs, 10 doc summaries.

## When To Use This Skill

Trigger this skill when the user asks about:

- **Blackwell/SM100 kernel programming** — tcgen05.mma, TMEM, CLC, 2-SM cooperative, NVFP4, FP8/FP4 block scaling, PDL/GDC
- **Kernel implementations** — FlashAttention-4, DeepGEMM, FlashMLA, NSA, GatedDeltaNet, NVFP4 GEMM/GEMV, fused MoE, gated dual GEMM
- **Performance patterns** — low SM utilization, memory-bound, register pressure, compute-bound, tail effects, pipeline stalls
- **DSLs for Blackwell** — CuTe DSL, CUDA C++ with PTX inline, Triton on Blackwell
- **Hopper → Blackwell migration** — wgmma → tcgen05, register → TMEM accumulators
- **PR references** — "how did vLLM/SGLang/FlashInfer/CUTLASS/PyTorch implement X for SM100?"
- **Competition solutions** — GPU Mode NVFP4 hackathon, FlashInfer MLSys 2026 submissions

Do NOT use this skill for:

- Generic CUDA questions unrelated to Blackwell/Hopper tensor cores
- Host-side framework integration (model loading, request routing, scheduling policy)
- Distributed systems topics — DeepEP, EPLB, DualPipe are out of scope

## Runtime Setup

Commands below use `$SKILL_DIR/scripts/...`. Resolve it once:

```bash
# The skill's own directory. Works both when the skill lives at
# skills/blackwell-kernel-wiki/ inside the wiki repo, and when it's installed
# at ~/.claude/skills/blackwell-kernel-wiki/ (with BLACKWELL_WIKI_ROOT set).
SKILL_DIR=$(find ~/.claude/skills/blackwell-kernel-wiki . -maxdepth 6 \
            -type d -name blackwell-kernel-wiki 2>/dev/null | head -1)
```

If the skill is installed outside the wiki repo, also set:

```bash
export BLACKWELL_WIKI_ROOT=/absolute/path/to/blackwell-kernel-wiki
```

The scripts auto-detect the wiki root when running inside a checkout; the env
override is only needed when the skill directory is separated from the data.

## How To Query (Navigation)

Use query paths in order of specificity. All paths live under the wiki root
(the repository containing `data/`, `wiki/`, `sources/`, `queries/`).

### Path 1: Unified search (preferred for natural language)

```bash
python3 "$SKILL_DIR/scripts/query.py" "how to fuse gate-up dual GEMM on Blackwell"
python3 "$SKILL_DIR/scripts/query.py" --tag nvfp4 --type kernel
python3 "$SKILL_DIR/scripts/query.py" --repo cutlass --limit 20
python3 "$SKILL_DIR/scripts/query.py" --symptom tail-effect --compact
```

Filters: `--type`, `--tag`, `--repo`, `--language`, `--architecture`,
`--symptom`, `--confidence`, `--limit`, `--compact`, `--paths-only`. Tag
filters accept aliases — `--tag UMMA` matches `tcgen05`, `--tag B200` matches
`sm100`, etc.

### Path 2: Fetch a specific page by id or path

```bash
python3 "$SKILL_DIR/scripts/get_page.py" kernel-flash-attention-4
python3 "$SKILL_DIR/scripts/get_page.py" pr-cutlass-2472
python3 "$SKILL_DIR/scripts/get_page.py" kernel-flash-attention-4 --follow-sources
python3 "$SKILL_DIR/scripts/get_page.py" kernel-flash-attention-4 --body-only
```

### Path 3: Regex text search across wiki bodies and PR pages

```bash
python3 "$SKILL_DIR/scripts/grep_wiki.py" "tcgen05\\.fence"
python3 "$SKILL_DIR/scripts/grep_wiki.py" "2-CTA backward" --only wiki
python3 "$SKILL_DIR/scripts/grep_wiki.py" "nvfp4" "block_scale" --any
```

### Path 4: Pre-built cross-reference indices

The wiki root ships auto-generated indices under `queries/`:

- `queries/by-problem.md` — symptom → pattern page → candidate techniques
- `queries/by-technique.md` — 15 techniques with architectures, confidence, reproducibility, source count
- `queries/by-hardware-feature.md` — tcgen05/tmem/clc/tma/nvfp4/etc. → related wiki + PR pages
- `queries/by-kernel-type.md` — gemm/attention/moe/mla/gated-delta-net → pages
- `queries/by-language.md` — cute-dsl/cuda-cpp/ptx/triton → guide page + related kernels/sources
- `queries/by-repo.md` — all 460 PRs across cutlass/sglang/vllm/flashinfer/pytorch

Read any of them with `python3 "$SKILL_DIR/scripts/get_page.py" queries/by-technique.md` or the `Read` tool directly.

### Path 5: Primer, schema, examples

Three companion docs under `$SKILL_DIR/references/`:

- `primer.md` — topic map: hardware features, techniques, symptoms, canonical page IDs. Read this first when the user question is broad.
- `schema.md` — condensed frontmatter schema, confidence rules, reproducibility ladder, controlled vocabulary, canonical aliases.
- `examples.md` — 10 worked query patterns mapping user questions → command sequences → synthesis.

## Output Pattern

When answering from this KB:

1. **Cite specific pages** with paths (e.g., `wiki/kernels/flash-attention-4.md`) and IDs (`kernel-flash-attention-4`).
2. **Follow `sources:` fields** to trace claims back to PRs/blogs/docs.
3. **Respect confidence levels** — `verified` > `source-reported` > `inferred` > `experimental`. Call out when a claim is `experimental` or `inferred`.
4. **Include code snippets** from wiki pages when they exist — technique/kernel/language pages are guaranteed `snippet`-reproducibility (validator-enforced).
5. **Report performance claims with all six fields** — `gpu`, `dtype`, `shape`, `metric`, `value`, `source_id`.

## Knowledge Base Contents (as of 2026-04-17)

- **545 total markdown pages** — 460 PR references + 48 wiki synthesis + 20 blogs + 10 docs + 7 contests
- **5 candidate ledgers** in `candidates/` — 3,928 merged PRs classified (include/defer/exclude) Jan 2025 – Apr 2026
- **6 auto-generated query indices** in `queries/`
- **Controlled vocabulary** (80+ tags) in `data/tags.yaml`, alias map in `data/aliases.yaml`
- **Validator** `scripts/validate.py` — 545 files / 0 errors / 1,642 links / 0 broken
- **Blackwell-first** — SM90 pages only appear when they carry explicit `blackwell_relevance`

## Quality Guarantees

- Every `verified` page has official-doc + upstream-code evidence
- Every technique/kernel/language page has a compilable snippet
- Every PR page has `inclusion_reason` and `status: merged`
- All Hopper-inclusive pages have explicit `blackwell_relevance`
