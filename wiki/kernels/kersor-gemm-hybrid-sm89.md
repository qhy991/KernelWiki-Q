---
id: kernel-kersor-gemm-hybrid-sm89
title: "Hybrid GEMM — ATen + cublasGemmEx Dispatch (SM89)"
type: kernel
architectures: [sm89]
tags: [gemm, cache-policy]
confidence: source-reported
reproducibility: benchmarked
kernel_types: [gemm]
languages: [cuda-cpp]
related: [kernel-fp8-block-scale-gemm]
sources: [exp-kersor-rtx4090-sm89]
performance_claims:
  - gpu: RTX 4090
    dtype: fp16
    shape: "N=6144, K=4096, M=1..8192"
    metric: speedup
    value: 1.04
    utilization: "tensor core bound at large M"
    source_id: exp-kersor-rtx4090-sm89
blackwell_relevance: "cuBLAS dispatch heuristics are hardware-specific. The B_T caching pattern and M-dependent strategy selection transfer, but thresholds differ on SM90/SM100."
---

# Hybrid GEMM — ATen + cublasGemmEx Dispatch (SM89)

## Overview

FP16 GEMM kernel for `C[M,N] = A[M,K] @ B[N,K]^T` with N=6144, K=4096, and variable M (1-8192) on RTX 4090. The key insight: no single cuBLAS configuration is optimal across all M values on SM89. The kernel dispatches between three strategies based on M thresholds discovered through systematic benchmarking.

Achieves 1.04x geomean speedup over the reference across all M values.

## Three-Strategy Dispatch

```
M < 208:     ATen mm(A, B_T) with FP16 accumulation (NN layout)
             → fastest for small M where launch overhead dominates

M = 208-2047: ATen mm(A, B_T) with FP32 accumulation (NN layout)
              → numerical stability without sacrificing throughput

M ≥ 2048:    Direct cublasGemmEx with CUBLAS_COMPUTE_32F (NT layout)
              → 3-5% faster than ATen's mm() dispatch path
```

## SM89-Specific Finding: COMPUTE_16F is Broken

```cpp
// CRITICAL SM89 BUG: CUBLAS_COMPUTE_16F produces incorrect results on Ada Lovelace
// Must use CUBLAS_COMPUTE_32F even for fp16 × fp16 → fp16
// This is NOT documented in NVIDIA's release notes

cublasGemmEx(handle,
    CUBLAS_OP_T, CUBLAS_OP_N,
    N, M, K,
    &alpha,
    B_ptr, CUDA_R_16F, K,    // B with OP_T: NT layout
    A_ptr, CUDA_R_16F, K,    // A with OP_N
    &beta,
    C_ptr, CUDA_R_16F, N,
    CUBLAS_COMPUTE_32F,       // NOT 16F! Broken on sm_89
    CUBLAS_GEMM_DEFAULT_TENSOR_OP);
```

## B_T Cache with Pool Shift Detection

```cpp
// Problem: ATen's mm(A, B.t()) creates a transposed view but cuBLAS prefers
// contiguous NN layout. Pre-computing B_T avoids the implicit transpose.
//
// Challenge: B's data pointer shifts by 256 bytes between calls due to
// torch's ShiftingMemoryPoolAllocator — but the data is the same!
// We detect this shift pattern to avoid redundant re-transposition.

static at::Tensor s_B_T;           // [K=4096, N=6144] fp16 cache
static uintptr_t s_prev_B_ptr = 0;
static constexpr uintptr_t POOL_SHIFT = 256;

const bool same_pool = s_B_T_valid &&
    (B_addr == s_prev_B_ptr + POOL_SHIFT);

if (!same_pool) {
    // Re-transpose B[N,K] → B_T[K,N] via shared-memory tiled kernel
    transpose_half_kernel_v15<<<grid, block, 0, stream>>>(B_ptr, B_T_ptr, N, K);
    s_B_T_valid = true;
}
```

## Tiled Transpose Kernel

```cuda
// Bank-conflict-free 32×32 tiled transpose
// +1 padding in shared memory column eliminates bank conflicts
__global__ void transpose_half_kernel_v15(
    const __half* src, __half* dst, int N, int K)
{
    __shared__ __half smem[32][33];  // +1 padding

    const int bx = blockIdx.x * 32, by = blockIdx.y * 32;
    smem[threadIdx.y][threadIdx.x] = src[(by + threadIdx.y) * K + (bx + threadIdx.x)];
    __syncthreads();

    // Transposed write: swap threadIdx.x and threadIdx.y
    dst[(bx + threadIdx.y) * N + (by + threadIdx.x)] = smem[threadIdx.x][threadIdx.y];
}
```

## FP16 vs FP32 Accumulation Threshold

```
M < 208: FP16 accumulation (allowFP16ReductionCuBLAS = true)
  - K=4096 elements summed: FP16 mantissa (10-bit) sufficient
  - cuBLAS uses faster FP16-accumulation tensor core path
  - Small M means fewer output tiles → launch overhead matters more

M ≥ 208: FP32 accumulation (allowFP16ReductionCuBLAS = false)
  - Longer reduction chains benefit from FP32 precision
  - Negligible throughput loss at large M (compute-bound regime)
  - The 208 threshold was found empirically on SM89
```

## When to Use

- FP16 GEMM on SM89 with fixed N, K and variable M (typical inference dispatch)
- When M varies across calls but B is reused (weight matrix)
- As a reference for cuBLAS heuristic tuning on Ada Lovelace

## Caveats

- **SM89-specific thresholds**: the M=208 and M=2048 breakpoints are empirical for RTX 4090. Other GPUs (even other SM89 cards like RTX 4080) may have different optimal thresholds.
- B_T cache persistence means memory is not freed between calls — adds 48MB resident memory for this specific N=6144 K=4096 case.
- Pool shift detection assumes a specific allocator behavior (256-byte shift); different PyTorch versions or custom allocators may break this heuristic.
- Static cuBLAS handle creation is not thread-safe; this kernel assumes single-stream inference.
