---
id: kernel-kersor-gqa-decode-sm89
title: "GQA Paged Decode — Split-K with Cache Policy Differentiation (SM89)"
type: kernel
architectures: [sm89]
tags: [gqa, attention, decode, paged-kv-cache, split-k, cache-policy, vectorized-loads, pipeline-stages]
confidence: source-reported
reproducibility: benchmarked
kernel_types: [gqa, attention, decode]
languages: [cuda-cpp]
related: [kernel-kersor-mla-decode-sm89, technique-vectorized-loads]
sources: [exp-kersor-rtx4090-sm89]
performance_claims:
  - gpu: RTX 4090
    dtype: bf16
    shape: "batch=64, qo_heads=32, kv_heads=8, head_dim=128, page_size=1"
    metric: latency
    value: 0.1109 ms
    utilization: "near memory bandwidth ceiling"
    source_id: exp-kersor-rtx4090-sm89
blackwell_relevance: "Cache policy differentiation (ld.global.cg for streaming K, cp.async for V) and split-K attention are general memory-bound patterns. SM100 would use TMA + TMEM instead of manual ld.global.cg."
artifact_dir: artifacts/kernels/kersor-gqa-decode-sm89
---

# GQA Paged Decode — Split-K with Cache Policy Differentiation (SM89)

## Overview

Grouped-Query Attention (GQA) paged decode kernel for RTX 4090 (SM89) with GQA ratio 4:1 (32 query heads, 8 KV heads). The kernel uses a warp-per-query-head layout where each of the 4 warps in a 128-thread block handles one query head sharing the same KV head. Split-K=16 provides parallelism across the KV sequence dimension.

Key innovation: differentiated L1 cache policies for K vs V loads — K uses synchronous `ld.global.cg` (L1-bypass) while V uses `cp.async` (asynchronous DMA to SMEM), reflecting their different memory access patterns.

## Architecture

```
Grid: (NUM_KV_HEADS=8, batch_size, NUM_SPLITS=16)
Block: 128 threads = 4 warps (one per GQA query head sharing same KV head)

SMEM layout (single-buffer, 8 KB):
  smem_k[T_PIPE=16][HEAD_DIM=128] BF16 = 4096 bytes
  smem_v[T_PIPE=16][HEAD_DIM=128] BF16 = 4096 bytes
  Total = 8192 bytes = 8 KB

Split-K: strided access pattern
  Token i of split s = kv_indices[page_start + s + i * NUM_SPLITS]
  → better cache utilization than contiguous splitting
```

## Cache Policy Differentiation

```cuda
// K-cache: synchronous ld.global.cg (L1-bypass, L2-only)
// Rationale: K values used once for dot product, then discarded.
//            L1 caching would pollute the cache for V reads.
#pragma unroll
for (int r = 0; r < ROWS_PER_WARP; r++) {
    int pg = page_ids[r];
    int base_offset = pg * kv_stride + kv_head_offset + lane_base;
    uint2 kv_tmp;
    const uint2* src_k = reinterpret_cast<const uint2*>(k_cache + base_offset);
    asm volatile("ld.global.cg.v2.u32 {%0,%1}, [%2];"
                 : "=r"(kv_tmp.x), "=r"(kv_tmp.y)
                 : "l"(src_k));
    *reinterpret_cast<uint2*>(smem_k + row * HEAD_DIM + lane_base) = kv_tmp;
}

// V-cache: asynchronous cp.async (DMA to SMEM, overlaps with K computation)
// Rationale: V values needed after K dot products complete.
//            cp.async overlaps V transfer with K->score computation.
#pragma unroll
for (int r = 0; r < ROWS_PER_WARP; r++) {
    int pg = page_ids[r];
    int base_offset = pg * kv_stride + kv_head_offset + lane_base;
    __pipeline_memcpy_async(
        smem_v + row * HEAD_DIM + lane_base,
        v_cache + base_offset,
        sizeof(__nv_bfloat16) * DIMS_PER_LANE);  // 8 bytes
}
__pipeline_commit();
__pipeline_wait_prior(0);
```

## Vectorized SMEM Access (uint2 / LDS.64)

```cuda
// Each lane processes 4 bf16 elements (DIMS_PER_LANE=4, HEAD_DIM=128, 32 lanes)
// Load via uint2 reinterpret: single LDS.64 instruction (halves LDS count vs 2x LDS.32)

__device__ __forceinline__ void load4_bf16_smem_u2(
    const __nv_bfloat16* ptr, float* r0, float* r1, float* r2, float* r3)
{
    uint2 raw = *reinterpret_cast<const uint2*>(ptr);
    *r0 = __bfloat162float(__nv_bfloat16_raw{(unsigned short)(raw.x & 0xFFFF)});
    *r1 = __bfloat162float(__nv_bfloat16_raw{(unsigned short)(raw.x >> 16)});
    *r2 = __bfloat162float(__nv_bfloat16_raw{(unsigned short)(raw.y & 0xFFFF)});
    *r3 = __bfloat162float(__nv_bfloat16_raw{(unsigned short)(raw.y >> 16)});
}
```

## 4-Token Unrolled Score + Accumulate

```cuda
// Process 4 tokens per iteration: amortizes sync overhead
// 4 K reads → 4 dot products → 4 warp_reduce_sum → 4 logits
// 4 V reads → online softmax update → accumulate P×V

__device__ __forceinline__ void process_4tok(
    const __nv_bfloat16* smem_k_buf, const __nv_bfloat16* smem_v_buf,
    int tok_base, const float* q_reg, float* acc,
    float& running_max, float& running_sum,
    float sm_scale_log2, int lane_id)
{
    // K reads: 4 × LDS.64
    float k0[4], k1[4], k2[4], k3[4];
    load4_bf16_smem_u2(smem_k_buf + (tok_base+0)*128 + lane_off, ...);
    // ... k1, k2, k3

    // 4 dot products + warp_reduce_sum
    float dot0=0.f, dot1=0.f, dot2=0.f, dot3=0.f;
    for (int d = 0; d < 4; d++) {
        dot0 += q_reg[d] * k0[d]; ...
    }
    dot0 = warp_reduce_sum(dot0); ...

    // 2-base logits: multiply by sm_scale * LOG2E
    float logit0 = dot0 * sm_scale_log2; ...

    // V reads: 4 × LDS.64
    float v0[4], v1[4], v2[4], v3[4];

    // Online softmax: joint update for all 4 tokens
    float new_max = fmaxf(running_max, fmaxf(fmaxf(logit0, logit1), fmaxf(logit2, logit3)));
    float exp_prev = exp2f(running_max - new_max);
    float e0 = exp2f(logit0 - new_max); ...

    running_sum = running_sum * exp_prev + e0 + e1 + e2 + e3;
    running_max = new_max;

    for (int d = 0; d < 4; d++)
        acc[d] = acc[d] * exp_prev + e0*v0[d] + e1*v1[d] + e2*v2[d] + e3*v3[d];
}
```

## Split-K Reduce

```cuda
// Pass 2: merge NUM_SPLITS=16 partial results per (batch, head)
// Grid: (batch_size, NUM_QO_HEADS=32), Block: HEAD_DIM=128 threads
// Each thread handles one dimension of the output vector

for (int s = 0; s < NUM_SPLITS; s++) {
    float lse_s = __ldg(lse_base + s);
    if (lse_s <= -FLT_MAX * 0.5f) continue;
    float w = __expf(lse_s - g_max);
    W += w;
    out_acc += w * __bfloat162float(__ldg(partial_base + s * HEAD_DIM + tid));
}
output[...] = __float2bfloat16(out_acc / W);
```

## Block-Table Index Prefetch

```cuda
// Prefetch page indices into registers before issuing loads
// Avoids dependent load chains: index → address → data
int page_ids[ROWS_PER_WARP];
#pragma unroll
for (int r = 0; r < ROWS_PER_WARP; r++) {
    int tok_global = tile_start + warp_row_start + r;
    page_ids[r] = (row < tile_tokens)
        ? __ldg(idx_base + tok_global * NUM_SPLITS) : -1;
}
```

## Tile Processing Dispatch

```
tile_tokens = min(T_PIPE=16, local_count - tile_start)

Binary decomposition for efficient tail handling:
  n8 = tile_tokens / 8    → process_4tok × 2
  n4 = (tile_tokens/4) & 1 → process_4tok × 1
  n2 = (tile_tokens/2) & 1 → process_2tok × 1
  n1 = tile_tokens & 1     → process_1tok × 1

This covers all possible tile_tokens (1-16) without branches in the hot path.
```

## When to Use

- GQA decode on SM89 with paged KV cache
- GQA ratios where warp-per-head fits the block size (ratio=4 with 128 threads)
- High KV sequence lengths where split-K provides necessary parallelism
- BF16 precision inference

## Caveats

- Fixed GQA ratio=4 (NUM_QO_HEADS=32, NUM_KV_HEADS=8); other ratios need kernel modification
- Single-buffer SMEM (no overlap between current tile load and previous tile compute)
- `__launch_bounds__(128, 2)`: tuned for SM89's 65536 registers/SM; different on other archs
- The `ld.global.cg` for K + `cp.async` for V combination was found empirically — K-only bypass + V async is optimal; applying .cg to both regresses performance
