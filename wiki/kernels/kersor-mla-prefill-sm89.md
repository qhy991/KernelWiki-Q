---
id: kernel-kersor-mla-prefill-sm89
title: "MLA Paged Prefill — FlashAttention-2 Tiled with Fused Dual GEMM (SM89)"
type: kernel
architectures: [sm89]
tags: [mla, attention, prefill, paged-kv-cache, vectorized-loads, kernel-fusion]
confidence: source-reported
reproducibility: benchmarked
kernel_types: [mla, attention, prefill]
languages: [cuda-cpp]
related: [kernel-flashmla, kernel-kersor-mla-decode-sm89, kernel-kersor-gqa-decode-sm89]
sources: [exp-kersor-rtx4090-sm89]
performance_claims:
  - gpu: RTX 4090
    dtype: bf16
    shape: "heads=16, ckv=512, kpe=64, page_size=1, variable seqlen"
    metric: latency
    value: 189.9 ms
    utilization: "compute-bound for long sequences"
    source_id: exp-kersor-rtx4090-sm89
blackwell_relevance: "FlashAttention-2 tiling pattern transfers directly. SM100 would benefit from tcgen05.mma for the score/output GEMMs and TMA for KV tile staging. The fused dual-GEMM (CKV+KPE in single loop) pattern applies to any MLA implementation."
artifact_dir: artifacts/kernels/kersor-mla-prefill-sm89
---

# MLA Paged Prefill — FlashAttention-2 Tiled with Fused Dual GEMM (SM89)

## Overview

Custom MLA prefill attention kernel for RTX 4090 (SM89) implementing FlashAttention-2 online softmax with tiled KV processing. The key MLA-specific challenge: each attention score requires two dot products — one over the 512-dim compressed KV (CKV) and one over the 64-dim positional encoding (KPE) — which are fused into a single KV-token loop to avoid redundant SMEM staging.

Achieves 189.9ms geomean latency across 38 FlashInfer-Bench workloads with variable sequence lengths and causal masking.

## Tiling Strategy

```
SMEM budget analysis (sm_89 limit: 100 KB per block):
  Kc tile  [TKV=64 × 512] BF16 = 65,536 bytes
  Kpe tile [TKV=64 ×  64] BF16 =  8,192 bytes
  Total SMEM                     = 73,728 bytes = 72 KB ✓

Q storage: registers only (not SMEM)
  Q-tile = 16 rows (4 per warp × 4 warps)
  Per-thread: qn_reg[4][16] + qp_reg[4][2] = 72 floats = 288 bytes in registers

Block configuration:
  128 threads = 4 warps × 32 lanes
  Each lane owns: 16 CKV elements + 2 KPE elements
  Grid: (max_q_tiles, NUM_HEADS=16, batch_size)
```

## Fused Dual GEMM (CKV + KPE)

```cuda
// score[i,j] = q_nope[i] @ Kc[j] + q_pe[i] @ Kpe[j]
// Both computed in a single pass over the KV tile, avoiding double SMEM load

for (int kv_j = 0; kv_j < TKV; kv_j++) {
    float partial = 0.0f;

    // CKV partial dot product: 16 elements per lane
    #pragma unroll
    for (int e = 0; e < 16; e++) {
        partial += qn_reg[r][e] *
            __bfloat162float(smem_kc[kv_j * 512 + lane * 16 + e]);
    }

    // KPE partial dot product: 2 elements per lane (fused, same iteration)
    #pragma unroll
    for (int e = 0; e < 2; e++) {
        partial += qp_reg[r][e] *
            __bfloat162float(smem_kpe[kv_j * 64 + lane * 2 + e]);
    }

    // Warp-level all-reduce → full logit (all 32 lanes contribute)
    logits[r][kv_j] = warp_reduce_sum(partial) * sm_scale;
}
```

## Cooperative KV Tile Loading (128-bit Vectorized)

```cuda
// smem_kc: 64 × 512 = 32768 BF16 = 4096 uint4 loads
// 4096 / 128 threads = 32 uint4 per thread (F09: 128-bit vectorized)
#pragma unroll 4
for (int i = 0; i < 32; i++) {
    const int u4_idx   = tid * 32 + i;
    const int bf16_idx = u4_idx * 8;
    const int kv_row   = bf16_idx / 512;
    const int kv_col   = bf16_idx % 512;

    if (kv_row < valid_kv) {
        // Paged gather: indirect page lookup per KV token
        const int page_id = kv_indices[kv_start + kv_tile_start + kv_row];
        uint4 tmp;
        load_bf16x8(ckv_cache + page_id * 512 + kv_col, tmp);
        *reinterpret_cast<uint4*>(&smem_kc[kv_row * 512 + kv_col]) = tmp;
    } else {
        *reinterpret_cast<uint4*>(&smem_kc[kv_row * 512 + kv_col]) = {0,0,0,0};
    }
}
```

## FlashAttention-2 Online Softmax

```cuda
// Per Q-row state: (row_max, row_sum, acc_o[16])
// Updated per KV tile with rescaling

float tile_max = -FLT_MAX;
for (int kv_j = 0; kv_j < TKV; kv_j++)
    tile_max = fmaxf(tile_max, logits[r][kv_j]);

float new_max = fmaxf(row_max[r], tile_max);
float alpha   = __expf(row_max[r] - new_max);  // rescale factor

// Rescale existing accumulator
for (int e = 0; e < 16; e++)
    acc_o[r][e] *= alpha;

// Accumulate weighted KV values for this tile
for (int kv_j = 0; kv_j < TKV; kv_j++) {
    float w = __expf(logits[r][kv_j] - new_max);
    for (int e = 0; e < 16; e++)
        acc_o[r][e] += w * __bfloat162float(smem_kc[kv_j*512 + lane*16 + e]);
}

row_sum[r] = alpha * row_sum[r] + tile_sum;
row_max[r] = new_max;
```

## Causal Mask with Early Exit

```cuda
// Causal condition: KV position j must be ≤ query position i
// abs_q_pos = prefix_len + q_row_base + local_row
// abs_kv_pos = kv_tile_start + kv_j

// Early tile exit: if entire KV tile is past all Q rows, skip
const int max_abs_q_pos = prefix_len + q_row_base + (valid_q_rows - 1);
if (kv_tile_start > max_abs_q_pos) break;  // all remaining tiles are masked
```

## LSE Output Format

```cuda
// F13: 2-base log-sum-exp (consistent with FlashInfer conventions)
// lse = (row_max + log(row_sum)) * LOG2E
float lse_val = (row_max[r] + __logf(row_sum[r])) * 1.4426950408889634f;
lse[global_row * NUM_QO_HEADS + head_idx] = lse_val;
```

## Performance Characteristics

| Bottleneck | Regime | Notes |
|---|---|---|
| Memory-bound | Short sequences (L < 256) | KV tile loading dominates |
| Compute-bound | Long sequences (L > 1024) | Q×K dot products dominate |
| Mixed | Mid-range (256-1024) | Balanced load/compute |

## When to Use

- MLA prefill on SM89 where no FlashInfer support exists
- Variable-length batched prefill with causal masking
- Paged KV cache (any page size, optimized for page_size=1)
- BF16 precision with FP32 internal accumulation

## Caveats

- `__launch_bounds__(128, 1)`: only 1 block per SM due to 72KB SMEM — compute throughput relies entirely on ILP within the single block
- No software pipelining of KV tile loads (single-buffered SMEM) — a double-buffer would overlap next-tile loads with current-tile compute
- The `expf`-based softmax (not `exp2f`) means no fast-math gain from 2-base during the main loop — only the final LSE uses LOG2E
- Fixed Q-tile=16 may underutilize for very short sequences; the kernel relies on batch parallelism for those cases
