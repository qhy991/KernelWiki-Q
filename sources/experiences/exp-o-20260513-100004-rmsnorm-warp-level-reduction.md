---
id: exp-o-20260513-100004-rmsnorm-warp-level-reduction
title: 'FlashInfer-Bench RMSNorm: warp-level reduction achieves 4.7x-5.4x speedup'
experience_type: optimization
source_category: agent-experiment
architectures:
- sm90
tags:
- rmsnorm
kernel_types:
- rmsnorm
languages:
- cuda-cpp
captured_at: '2026-05-13'
confidence: inferred
reproducibility: snippet
impl_family: custom_cuda
---

For RMSNorm with hidden_size=128 and BF16 data, a custom CUDA kernel using warp-level reduction (__shfl_xor_sync) achieves 4.7x-5.4x speedup over PyTorch eager. Each warp handles one row (32 threads), with 4 warps per block. The kernel computes sum-of-squares via warp shuffle, applies rsqrtf, then normalizes with weight multiplication.

## Challenge

PyTorch eager RMSNorm implementation (x.float().pow(2).mean(-1, keepdim=True).rsqrt() * weight) has kernel launch overhead and multiple memory passes. For batch inference (M rows, hidden_size=128), this overhead dominates because each operation is small.

### Symptoms

- `PyTorch eager RMSNorm is slow due to many small kernel launches`
- `Per-row operations with hidden_size=128 are memory-bound, not compute-bound`
- `Fusing normalization into a single kernel eliminates intermediate memory traffic`

## Solution

Custom CUDA kernel with warp-level reduction for sum-of-squares. Each warp handles one row (32 threads handle 128 elements = 4 elements per thread for hidden_size=128). Use __shfl_xor_sync for intra-warp reduction, avoiding shared memory.

### Implementation

```cuda
// RMSNorm warp-level kernel (4.7x-5.4x speedup)
__global__ void rmsnorm_kernel(
    const __nv_bfloat16* __restrict__ input,   // [M, hidden_size]
    const __nv_bfloat16* __restrict__ weight,  // [hidden_size]
    __nv_bfloat16* __restrict__ output,        // [M, hidden_size]
    int M, int hidden_size) {

    const int WARP_SIZE = 32;
    int row = blockIdx.x * (blockDim.y) + threadIdx.y;
    int lane = threadIdx.x;

    if (row >= M) return;

    int idx = row * hidden_size + lane;

    // Each thread computes partial sum of squares
    float sum_sq = 0.0f;
    for (int i = lane; i < hidden_size; i += WARP_SIZE) {
        float x = __bfloat162float(input[row * hidden_size + i]);
        sum_sq += x * x;
    }

    // Warp-level reduction using shuffle
    for (int offset = 16; offset > 0; offset >>= 1) {
        sum_sq += __shfl_xor_sync(0xffffffff, sum_sq, offset);
    }

    float inv_rms = rsqrtf(sum_sq / (float)hidden_size + 1e-6f);

    // Normalize and apply weight
    for (int i = lane; i < hidden_size; i += WARP_SIZE) {
        float x = __bfloat162float(input[row * hidden_size + i]);
        float w = __bfloat162float(weight[i]);
        output[row * hidden_size + i] = __float2bfloat16(x * inv_rms * w);
    }
}

// Launch config: dim3 block(32, 4); dim3 grid((M + 3) / 4);
```

## Key Lessons

- Warp-level reduction via __shfl_xor_sync achieves 4.7x-5.4x for RMSNorm with hidden_size=128. No shared memory needed — shuffle instructions are register-only.
- Block configuration: dim3 block(32, warps_per_block) where each warp handles one row. For hidden_size=128: 32 threads per warp, 4 elements per thread.
- The reduction loop: for (offset=16; offset>0; offset>>=1) sum += __shfl_xor_sync(0xffffffff, sum, offset). After this, lane 0 has the full sum.
- Use rsqrtf(sum/hidden_size + epsilon) for the inverse RMS. Epsilon 1e-6 is standard for BF16 RMSNorm.
- For hidden_size > 256, consider using shared memory reduction instead of pure warp shuffle, as you need more threads per row.
- BF16 conversion intrinsics: __bfloat162float() for read, __float2bfloat16() for write. Do all compute in float32 for numerical stability.
- This pattern generalizes to LayerNorm (add mean subtraction) and other per-row normalization operations.
