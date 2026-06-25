---
id: kernel-kersor-mla-decode-sm89
title: "MLA Paged Decode — 8-Token Unrolled Split-K (SM89)"
type: kernel
architectures: [sm89]
tags: [mla, attention, decode, paged-kv-cache, split-k, vectorized-loads, cache-policy]
confidence: source-reported
reproducibility: benchmarked
kernel_types: [mla, attention, decode]
languages: [cuda-cpp]
related: [kernel-flashmla, kernel-kersor-mla-prefill-sm89, kernel-kersor-gqa-decode-sm89]
sources: [exp-kersor-rtx4090-sm89]
performance_claims:
  - gpu: RTX 4090
    dtype: bf16
    shape: "batch=64, heads=16, ckv=512, kpe=64, page_size=1, avg_L=variable"
    metric: latency
    value: 0.1105 ms
    utilization: "near memory bandwidth ceiling"
    source_id: exp-kersor-rtx4090-sm89
blackwell_relevance: "Techniques transfer to SM90/SM100 decode: unrolled scattered loads, split-K decomposition, and streaming cache hints are architecture-independent memory-bound optimizations. SM100 TMA would replace manual ld.global.cs."
artifact_dir: artifacts/kernels/kersor-mla-decode-sm89
---

# MLA Paged Decode — 8-Token Unrolled Split-K (SM89)

## Overview

Custom MLA (Multi-head Latent Attention) decode kernel optimized for NVIDIA RTX 4090 (SM89, Ada Lovelace) with paged KV cache at page_size=1. The key challenge is that page_size=1 means every token's KV entry is at a random DRAM location — the access pattern is fully scattered, making memory latency hiding critical.

The kernel achieves 0.1105ms latency at batch=64, outperforming naive implementations by 116.7x. Since FlashInfer's MLA kernels are SM80-only, this is the first optimized MLA decode implementation on SM89.

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│  Host Dispatch (adaptive K selection)                    │
│  avg_L ≤ 32:  small-L path (SMEM staging, 1 CTA/head)  │
│  avg_L 33-63: mid-range (split-K=4)                    │
│  avg_L ≥ 64:  split-K=16 (main path)                   │
│  avg_L ≥ 2048: split-K=32 (long sequences)             │
└──────────┬────────────────────────────────┬─────────────┘
           │                                │
    ┌──────▼───────┐                ┌───────▼───────┐
    │  Pass 1:     │                │  Pass 2:      │
    │  Split-K     │                │  Online merge │
    │  attention   │                │  (streaming)  │
    │  per chunk   │                │               │
    └──────────────┘                └───────────────┘
```

## Key Design: 8-Token Unrolled Inner Loop

The most important optimization for scattered page_size=1 access: issue 8 independent `ld.global.cs` loads simultaneously before any synchronization, allowing the memory subsystem to service up to 8 outstanding DRAM requests per iteration.

```cuda
// 8-token unrolled main loop — 0.25 syncs/token (vs 0.5 for 4-token)
for (; local_tok < chunk_len8; local_tok += 8) {
    // Issue all 8 CKV loads simultaneously (each to a random DRAM page)
    const int pi0 = kv_indices[abs_beg + local_tok + 0];
    // ... pi1 through pi7 ...

    // 8 × ld.global.cs.v2.u32 — streaming hint, L1 bypass
    float k0_0, k0_1, k0_2, k0_3;
    // ... k1 through k7 ...
    LOAD_CKV_CS(pi0, k0_0, k0_1, k0_2, k0_3, t)
    LOAD_CKV_CS(pi1, k1_0, k1_1, k1_2, k1_3, t)
    // ... all 8 issued before any sync ...
    LOAD_CKV_CS(pi7, k7_0, k7_1, k7_2, k7_3, t)

    // 8 KPE loads (streaming)
    LOAD_KPE_CS(pi0, p0, t) ... LOAD_KPE_CS(pi7, p7, t)

    // 8 partial dot products + 8 warp reduces
    float d0 = qn0*k0_0 + qn1*k0_1 + qn2*k0_2 + qn3*k0_3;
    // ... d1 through d7 ...

    // Write 8 warp partial sums to smem → ONE __syncthreads
    __syncthreads();  // sync #1 of 2 per 8 tokens

    // Read cross-warp sums → 8 logits → 8 online softmax updates
    SOFTMAX_UPDATE(l0, k0_0, k0_1, k0_2, k0_3)
    // ... through l7 ...

    __syncthreads();  // sync #2 of 2
}
```

## CKV Load: ld.global.cs (Streaming Cache Hint)

```cuda
// ld.global.cs = "cache streaming" — marks data as likely single-use
// On SM89: bypasses L1, uses L2 streaming allocation
// Prevents L1 pollution from the large scattered KV working set

#define LOAD_CKV_CS(pi, a0, a1, a2, a3, t_id)                         \
{                                                                       \
    const __nv_bfloat16* _src = ckv_cache + (int64_t)(pi) * DIM_CKV   \
                                           + (t_id) * 4;               \
    uint2 _v;                                                          \
    asm volatile("ld.global.cs.v2.u32 {%0,%1},[%2];"                  \
                 :"=r"(_v.x),"=r"(_v.y):"l"(_src));                   \
    // Unpack 4 bf16 values from uint2                                  \
    const __nv_bfloat16* _r = reinterpret_cast<const __nv_bfloat16*>(&_v); \
    (a0) = __bfloat162float(_r[0]); (a1) = __bfloat162float(_r[1]);   \
    (a2) = __bfloat162float(_r[2]); (a3) = __bfloat162float(_r[3]);   \
}
```

## Split-K Decomposition

```
KV sequence (L tokens, page_size=1):
┌───────────────────────────────────────────────────┐
│ chunk 0  │ chunk 1  │ chunk 2  │ ... │ chunk K-1 │  (K = 16 or 32)
└───────────────────────────────────────────────────┘
     │           │           │                 │
     ▼           ▼           ▼                 ▼
  Pass1 CTA  Pass1 CTA  Pass1 CTA  ...    Pass1 CTA
  (m, d, acc) (m, d, acc) (m, d, acc)      (m, d, acc)
     │           │           │                 │
     └───────────┴───────────┴─────────────────┘
                         │
                   Pass2 CTA: streaming online merge
                   (exp2f rescale, no sync needed)
```

Each Pass1 CTA writes `[m, d, acc[512]]` to workspace — log-sum-exp max + denominator + unnormalized accumulator. Pass2 streams through all K chunks with online softmax merge (single pass, no sorting needed).

## Adaptive Dispatch

```
avg_L ≤ 32:   small-L SMEM path (no split-K, direct SMEM staging)
              → single CTA per (batch, head), cooperative token loading
              → 1168 bytes SMEM (fits DIM_CKV + DIM_KPE + warp partials)

avg_L 33-63:  mid-range split-K=4
              → moderate parallelism without excessive workspace

avg_L ≥ 64:   split-K=16 (main production path)
              → 16 CTAs per (batch, head) for full SM utilization

avg_L ≥ 2048: split-K=32 (long sequences)
              → 32 chunks exploits full GPU parallelism
```

## Register Budget

```
8-token unroll register pressure:
  8 × (kc0..kc3) + 8 KPE values + 8 dot products = 48 additional regs at peak
  Total: 64 registers/thread, 0 spills
  SM89 with 64 regs × 128 threads = 8192 regs/block → 8 blocks/SM max

Trade-off vs 4-token unroll (V8):
  V8: 48 regs → 10 blocks/SM (higher occupancy)
  V11: 64 regs → 8 blocks/SM (20% less occupancy)
  But: 2× better sync efficiency + 2× more outstanding loads
  For memory-bound: fewer syncs dominates occupancy for large L.
```

## Performance

| Dispatch Path | avg_L | Latency | Notes |
|---|---|---|---|
| small-L | ≤32 | <0.05ms | Single CTA, SMEM staging |
| split-K=16 | 64-2048 | ~0.11ms | Main production path |
| split-K=32 | >2048 | ~0.15ms | Long-context |

## When to Use

- MLA decode on SM89 (Ada Lovelace) — no FlashInfer MLA support on this arch
- Paged KV cache with page_size=1 (fully scattered access pattern)
- Batch sizes where split-K provides sufficient parallelism (≥16 useful)
- BF16 precision with FP32 accumulation

## Caveats

- SM89-specific tuning: occupancy and register budgets differ on SM90/SM100
- Page_size=1 only; larger page sizes would benefit from cp.async/TMA bulk loads instead of scalar ld.global.cs
- The 2-base (exp2f/log2f) arithmetic requires consistent log-base across pass1 and pass2
- sm_scale is pre-multiplied by LOG2E (1.4426950408889634) at kernel entry
