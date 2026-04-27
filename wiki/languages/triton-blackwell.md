---
id: lang-triton
title: "Triton on Blackwell"
type: language
tags: [triton, attention, moe, gated-delta-net]
related: [kernel-nsa, kernel-gated-delta-net, kernel-fused-moe, lang-cute-dsl]
sources: [doc-triton-3.6-blackwell, pr-sglang-22079, pr-sglang-21019, pr-sglang-5390, pr-sglang-21595, pr-pytorch-175826, blog-nsa, blog-gated-delta-net, blog-flash-attention-4]
reproducibility: snippet
architectures: [sm100, sm90]
confidence: verified
evidence_basis:
  - evidence_type: official-doc
    source_id: doc-triton-3.6-blackwell
  - evidence_type: upstream-code
    source_id: pr-sglang-22079
version_sensitive:
  id: vs-triton-3.6-blackwell-tcgen05
blackwell_relevance: "As of Triton 3.6+, Triton has native Blackwell (SM100) lowering through tcgen05 + TMEM via descriptor/TMA warp-specialized matmul, Gluon multi-CTA / 2CTA, and tl.dot_scaled. This page documents which lowering surfaces are first-class on Blackwell vs which are still gluon-only or workload-dependent."
---

## Overview

Triton is used for many attention and linear-attention kernels (NSA, GatedDeltaNet, FLA). Starting with Triton 3.6 (released `2026-01-21`), Triton ships native Blackwell (SM100) lowering through `tcgen05.mma` + Tensor Memory (TMEM). The earlier framing — "Triton compiler generates wgmma, not tcgen05" — was correct for Triton 3.5 and earlier but is no longer correct on 3.6+. See the "Pre-3.6 historical context" subsection below for the historical framing; the rest of this page describes the current 3.6+ behavior.

When to use Triton on Blackwell:
- Rapid prototyping (Triton's fast turnaround still beats CuTe-DSL for exploration)
- Memory-bound kernels (bandwidth is bottleneck, not compute)
- Linear / sparse attention (GatedDeltaNet, FLA, NSA) where Triton's grid scheduling is convenient
- Block-scaled matmul on Blackwell via `tl.dot_scaled` (NVFP4 / MXFP families) — first-class hardware-accelerated path
- Warp-specialized descriptor/TMA matmul kernels following the Triton persistent matmul tutorial pattern

Use CuTe-DSL / CUTLASS / FA-4 / TRT-LLM instead when:
- Peak-performance compute-bound matmul or attention on Blackwell. SGLang `pr-sglang-5390` measured a CUTLASS `tcgen05_mla` backend ~27% faster than the Triton MLA decode baseline on Blackwell.
- Production routing where vendor kernels are mature: SGLang `pr-sglang-21595` changes Blackwell datacenter multimodal attention default from `triton_attn` to FA-4.

## Triton 3.6+ Blackwell path

The 3.6 release adds Blackwell-native infrastructure for `tcgen05.mma`, TMEM allocation/copy/load/store, and warp-specialization plumbing. Source-of-record: [`doc-triton-3.6-blackwell`](../../sources/docs/triton-3.6-blackwell.md). Per-pathway breakdown with verified-vs-needs-verification status: [`data/triton-3.6-evidence.md`](../../data/triton-3.6-evidence.md).

Verified lowering surfaces (with caveats):

1. **Descriptor/TMA + `tl.range(warp_specialize=True)` + `tl.dot`** — strongest checked `tl.*`-surface evidence. The official Triton persistent matmul tutorial states the warp-specialized mode "only works on Blackwell right now"; backed by warp-specialization aref plumbing (PRs `#8262`, `#7826`, `#8009`, `#8123`, `#8534`, `#8451`, `#8651`) and Blackwell TMEM / `tcgen05` backend work (PRs `#8136`, `#8148`, `#8202`, `#8386`, `#8421`, `#8495`, `#8102`, `#8338`, `#8225`).

2. **`tl.dot_scaled` block-scaled matmul** — hardware-accelerated by fifth-generation Tensor Cores on compute capability 10. The 3.6 dialect doc exposes `ttng.tc_gen5_mma_scaled` with TMEM-token semantics plus `ttng.tmem_copy`. Source PRs: Gluon NVIDIA `tcgen05 mma scaled` (`#8393`); frontend fixes (`#8564`, `#8658`); shared TMEM/tcgen05 backend (`#8136`, `#8148`, `#8202`). Format coverage centered on NVFP4 / MXFP per the official block-scaled matmul tutorial.

3. **Gluon front-end + `gl.warp_specialize` + `num_ctas`** — the most explicit Blackwell-native surface. Initial 2-CTA cluster support landed in `#8644`, `#8653`; `num_ctas` plumbing in `#8645`; Gluon-side `tcgen05 mma scaled` in `#8393`. The release notes describe 2-CTA / cluster as initial support, so cluster-scope kernels via Gluon should be treated as early-stage.

Surfaces still in needs-verification territory:
- Plain `tl.dot` matmul without warp specialization or descriptor/TMA structure: the 3.6 release contains the infrastructure, but checked sources do not prove that arbitrary plain `tl.dot` kernels automatically use the TMEM-backed tcgen05 path on SM100. Treat plain `tl.dot` on Blackwell as "uses the new infrastructure when applicable" rather than as a blanket equivalence.
- Fused attention forward kernels using `warp_specialize=True` in the Triton tutorial path lower through the shared warp-specialization / aref / TMEM stack, but coverage parity for non-persistent / non-descriptor `tl.dot` kernels and backward paths is not equally documented.

### What changed vs the pre-3.6 framing

Before Triton 3.6, the Blackwell story was: the compiler generated `wgmma.mma_async`, accumulators stayed in registers, and direct `tcgen05` / TMEM access was unavailable from `tl.*`. Pages and inclusion-policy text written under that premise are obsolete. The current premise is: **`tcgen05` + TMEM lowering paths exist on SM100, but coverage and performance leadership are workload-dependent**.

## Triton on Blackwell — verified upstream-code anchor

The primary in-corpus downstream evidence that Triton matmul kernels are landing for Blackwell post-3.6 is [`pr-sglang-22079`](../../sources/prs/sglang/PR-22079.md): a Triton attention kernel performing actual `tl.dot(q, k)` and `tl.dot(p, v)` matmul on `architectures: [sm100, sm90]`, merged on `2026-04-03` (well after the Triton 3.6.0 release date of `2026-01-21`). It is the SGLang `extend_attention` Triton kernel for the Gemma4 NVFP4 attention path, with frontmatter tags `[attention, fp4, gemm, nvfp4]`. The kernel ships verbatim under `artifacts/prs/sglang/PR-22079/key-files/python/sglang/srt/layers/attention/triton_ops/extend_attention.py` and exercises the `tl.dot` lowering surface that 3.6 added Blackwell `tcgen05` infrastructure for.

A secondary anchor — [`pr-sglang-21019`](../../sources/prs/sglang/PR-21019.md), a Qwen3.5 GDN projection fused split/reshape/cat kernel merged 2026-03-20 — is retained for context. It is `tl.load` / `tl.store` only (memory rearrangement, no `tl.dot`), so it demonstrates "Triton on SM100 post-3.6" but not the matmul lowering path.

The strongest possible demonstrations — explicit inspectable PTX showing `tcgen05.mma` emission, or kernels using `tl.dot_scaled` / `warp_specialize` with descriptor/TMA structure — were not found locally in any tracked-repo PR. They currently live in the upstream Triton tutorials. A future refresh round should backfill such an anchor if one becomes available in tracked downstream repos.

## FlashInfer-Bench: AI-Generated Triton Performance

The following table reflects benchmark snapshots from when the original page was written (Triton 3.5 era) and is preserved for historical reference. It does NOT reflect the 3.6+ tcgen05 path.

| Model | Avg Speedup vs FlashInfer | Resolved % |
|---|---|---|
| Gemini 2.5 Pro | 0.628x | 73.1% |
| GPT-5 | 0.467x | 92.3% |
| Claude Opus 4.1 | 0.456x | 73.1% |

A re-run on Triton 3.6 with FlashInfer-Bench is not yet available locally; future refresh rounds should update this table or remove it in favor of a pointer to the live leaderboard.

## GatedDeltaNet Decode in Triton

```python
@triton.jit
def gated_delta_net_decode(
    Q, K, V, Gate, State, Output,
    qk_dim: tl.constexpr, v_dim: tl.constexpr, d: tl.constexpr,
):
    """Single-token decode: O(d^2) per token."""
    head_id = tl.program_id(0)
    # Load recurrent state S: [qk_dim*d, v_dim*d]
    s = tl.load(State + head_id * qk_dim * d * v_dim * d + offsets)
    q = tl.load(Q + offsets)
    k = tl.load(K + offsets)
    v = tl.load(V + offsets)
    g = tl.load(Gate + head_id)

    # Delta rule: S = g*S + k @ (v - S^T @ k)^T
    sk = tl.dot(tl.trans(s), k)
    delta_v = v - sk
    s = g * s + tl.dot(k[:, None], delta_v[None, :])
    o = tl.dot(tl.trans(s), q)

    tl.store(State + offsets, s)
    tl.store(Output + offsets, o)
```

## NSA Sparse Attention in Triton

```python
@triton.jit
def sparse_attention_fwd(Q, K, V, Output, TopK_Indices,
                         block_size: tl.constexpr, topk: tl.constexpr):
    """Attend to top-k sparse token blocks only."""
    qid = tl.program_id(0)
    q = tl.load(Q + qid * d + tl.arange(0, d))
    acc = tl.zeros([d], dtype=tl.float32)
    for i in range(topk):
        bidx = tl.load(TopK_Indices + qid * topk + i)
        k_block = tl.load(K + bidx * block_size * d + offsets)
        v_block = tl.load(V + bidx * block_size * d + offsets)
        scores = tl.dot(q[None, :], tl.trans(k_block))
        # softmax + accumulate...
```

## Pre-3.6 historical context

> The text in this subsection describes Triton 3.5 and earlier. It is preserved for historical accuracy and is NOT a current statement about Triton 3.6+ behavior. Do not cite it as current limitations.

Triton on Blackwell — Triton 3.5 and earlier:

1. **No direct tcgen05 access**: Triton compiler generates wgmma, not tcgen05.
2. **No TMEM**: accumulators stay in registers.
3. **CPU launch overhead**: impacts small-batch decode latency.
4. **Workaround**: CUDA graphs (vLLM default for GatedDeltaNet).

These four bullets describe the world before Triton 3.6.0 landed (`2026-01-21`). The first two are no longer correct on 3.6+; see the "Triton 3.6+ Blackwell path" subsection above. CPU launch overhead and CUDA-graph workarounds remain workload-relevant on small-batch decode paths regardless of compiler era.

## Blackwell Triton Examples (verbatim upstream code shipped locally)

The following Triton files ship **verbatim** under `artifacts/prs/` (pinned at each PR's merge SHA). Each PR is in the `triton-in-policy` capture lane defined by `data/inclusion-policy.yaml` — i.e., SM100-integration, memory-bound, or backend-fallback scope (not pure Hopper Triton).

| File | Purpose | PR |
|---|---|---|
| [`artifacts/prs/flashinfer/PR-1025/key-files/flashinfer/triton/format_conversion.py`](../../artifacts/prs/flashinfer/PR-1025/key-files/flashinfer/triton/format_conversion.py) | FP8 / FP16 format conversion Triton kernels for FlashInfer | flashinfer#1025 |
| [`artifacts/prs/sglang/PR-20910/key-files/python/sglang/jit_kernel/norm.py`](../../artifacts/prs/sglang/PR-20910/key-files/python/sglang/jit_kernel/norm.py) | Normalization kernels (memory-bound SM100 Triton) | sglang#20910 |
| [`artifacts/prs/sglang/PR-21019/key-files/python/sglang/jit_kernel/triton/gdn_fused_proj.py`](../../artifacts/prs/sglang/PR-21019/key-files/python/sglang/jit_kernel/triton/gdn_fused_proj.py) | GatedDeltaNet fused projection (linear-attention) Triton kernel; primary upstream-code anchor for the Triton 3.6+ Blackwell path (`pr-sglang-21019`, merged 2026-03-20) | sglang#21019 |

The full 42-PR universe is enumerated in `data/triton-universe.yaml`. Entries marked `captured: false` do not ship locally because they fall outside the three in-policy sub-scopes (see the policy file for reasons).
