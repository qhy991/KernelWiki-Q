---
id: kernel-kersor-fused-rmsnorm-sm89
title: "Fused RMSNorm — Warp-Per-Row and Multi-Row CTA (SM89)"
type: kernel
architectures: [sm89]
tags: [rmsnorm, kernel-fusion, vectorized-loads]
confidence: source-reported
reproducibility: benchmarked
kernel_types: [rmsnorm, fused-kernel]
languages: [cuda-cpp, triton]
related: [kernel-kersor-mla-decode-sm89, technique-vectorized-loads]
sources: [exp-kersor-rtx4090-sm89]
performance_claims:
  - gpu: RTX 4090
    dtype: bf16
    shape: "hidden_size=128, batch variable"
    metric: speedup
    value: 9.31
    utilization: "memory-bound, high occupancy"
    source_id: exp-kersor-rtx4090-sm89
  - gpu: RTX 4090
    dtype: bf16
    shape: "hidden_size=2048, batch variable"
    metric: speedup
    value: 9.38
    utilization: "memory-bound, 6 CTAs/SM"
    source_id: exp-kersor-rtx4090-sm89
blackwell_relevance: "RMSNorm patterns are architecture-independent. The warp-per-row approach for small hidden dims and multi-row CTA packing for larger dims transfer directly to SM90/SM100."
---

# Fused RMSNorm — Warp-Per-Row and Multi-Row CTA (SM89)

## Overview

Two complementary RMSNorm kernels optimized for different hidden dimensions on RTX 4090, each achieving ~9.3x speedup over the PyTorch eager reference. The small-hidden kernel (h=128) uses a pure CUDA warp-per-row design with zero shared memory. The large-hidden kernel (h=2048) uses Triton with occupancy-tuned num_warps and multi-row CTA packing.

Both replace 9 eager PyTorch operations (cast, pow, mean, add, rsqrt, mul, mul, cast) with a single fused kernel.

## CUDA Kernel: h=128 (Warp-Per-Row)

```cuda
// Design: 1 warp (32 threads) per row, 8 rows per block (256 threads)
// hidden=128: 32 threads × 4 bf16 elements = 128 (exact coverage)
// Reduction: warp-shuffle butterfly (no shared memory needed)
// Memory: 768 bytes/row (256B input + 256B weight + 256B output)

__global__ void __launch_bounds__(256, 6) rmsnorm_h128_fused(
    const __nv_bfloat16* hidden_states,  // [batch, 128]
    const __nv_bfloat16* weight,         // [128]
          __nv_bfloat16* output,          // [batch, 128]
    int batch_size, float eps)
{
    const int row  = blockIdx.x * 8 + (threadIdx.x / 32);
    const int lane = threadIdx.x % 32;
    if (row >= batch_size) return;

    // Vectorized load: 2 × bfloat162 = 4 bf16 values per thread
    const __nv_bfloat162* hs_row = ...;
    __nv_bfloat162 hs0 = __ldg(hs_row + lane);
    __nv_bfloat162 hs1 = __ldg(hs_row + lane + 32);

    float2 f0 = __bfloat1622float2(hs0);
    float2 f1 = __bfloat1622float2(hs1);
    float x0=f0.x, x1=f0.y, x2=f1.x, x3=f1.y;

    // Sum of squares + warp-shuffle reduce (5-step butterfly)
    float sum_sq = x0*x0 + x1*x1 + x2*x2 + x3*x3;
    sum_sq = warp_reduce_sum(sum_sq);  // all 32 lanes get same result

    // Normalize
    float inv_rms = rsqrtf(sum_sq / 128.0f + eps);

    // Load weight, apply, store as bfloat162
    __nv_bfloat162 w0 = __ldg(w_ptr + lane);
    __nv_bfloat162 w1 = __ldg(w_ptr + lane + 32);
    float2 wf0 = __bfloat1622float2(w0), wf1 = __bfloat1622float2(w1);

    out_row[lane]    = __float22bfloat162_rn({x0*inv_rms*wf0.x, x1*inv_rms*wf0.y});
    out_row[lane+32] = __float22bfloat162_rn({x2*inv_rms*wf1.x, x3*inv_rms*wf1.y});
}
```

Key properties:
- **Zero shared memory**: warp-shuffle covers entire 128-element row
- **`__launch_bounds__(256, 6)`**: forces compiler to budget for 6 blocks/SM occupancy
- **bfloat162 vectorization**: 2 elements per load/store instruction (LDG.64 transactions)
- **8 rows/block**: maximizes block-level parallelism for small batch sizes

## Triton Kernel: h=2048 (Fused Add + RMSNorm)

```python
@triton.jit
def _fused_rms_kernel_large(
    hs_ptr, res_ptr, w_ptr, out_ptr,
    N, eps, stride_hs, stride_res, stride_out,
    BLOCK_SIZE: tl.constexpr,   # = 2048 = N (no masking needed)
):
    row = tl.program_id(0)
    offsets = tl.arange(0, BLOCK_SIZE)

    hs  = tl.load(hs_ptr  + row * stride_hs  + offsets).to(tl.float32)
    res = tl.load(res_ptr + row * stride_res + offsets).to(tl.float32)
    w   = tl.load(w_ptr + offsets).to(tl.float32)

    x       = hs + res          # Fused add (saves separate kernel launch)
    sum_sq  = tl.sum(x * x, axis=0)
    inv_rms = tl.rsqrt(sum_sq / BLOCK_SIZE + eps)
    y       = x * inv_rms * w

    tl.store(out_ptr + row * stride_out + offsets, y.to(tl.bfloat16))
```

Dispatch strategy:
```python
if M <= 128:
    # Multi-row CTA: 4 rows per block, weight loaded once and reused
    _fused_rms_kernel_small[(cdiv(M, 4),)](... num_warps=4)
else:
    # Single-row: num_warps=8 → 6 CTAs/SM (vs 3 with num_warps=16)
    _fused_rms_kernel_large[(M,)](... num_warps=8)
```

## Occupancy Analysis (SM89)

```
CUDA h=128 kernel:
  256 threads/block × 6 blocks/SM = 1536 threads/SM
  SM89 limit: 1536 threads/SM → 100% occupancy
  Registers: bounded by __launch_bounds__(256, 6) → compiler targets ≤42 regs/thread

Triton h=2048 kernel:
  num_warps=8 = 256 threads/block
  6 CTAs/SM achievable (confirmed by autotuner)
  vs num_warps=16 (512 threads) which gives only 3 CTAs/SM
  → 2× more CTAs means better memory latency hiding for this BW-bound kernel
```

## Multi-Row CTA for Small Batches

```python
# Weight is loaded ONCE per CTA, reused across ROWS_PER_CTA=4 rows
# Reduces grid size by 4× → fewer CTA launches → faster scheduling
@triton.jit
def _fused_rms_kernel_small(..., ROWS_PER_CTA: tl.constexpr):
    w = tl.load(w_ptr + offsets).to(tl.float32)  # load once
    for i in tl.static_range(ROWS_PER_CTA):
        row = cta_id * ROWS_PER_CTA + i
        if row < M:
            hs = tl.load(...)
            ...
            tl.store(...)
```

## When to Use

- RMSNorm (with or without fused residual add) on SM89
- Hidden sizes 128-2048 (covers DeepSeek MLA head dims and transformer hidden dims)
- Memory-bound: focus on occupancy and vectorized access, not compute

## Caveats

- h=128 CUDA kernel is fixed at hidden_size=128 exactly (warp coverage assumption)
- Triton kernel requires BLOCK_SIZE=N (no partial-block masking) — hidden must be power-of-2 or handled by tl.constexpr specialization
- Pre-warm at import time eliminates JIT overhead but adds ~100ms startup cost
- Output buffer caching across calls assumes same (M, N, device) signature
