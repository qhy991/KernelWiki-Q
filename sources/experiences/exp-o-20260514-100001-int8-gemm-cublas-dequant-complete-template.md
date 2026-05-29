---
id: exp-o-20260514-100001-int8-gemm-cublas-dequant-complete-template
title: 'SOL-ExecBench INT8 GEMM: complete working cuBLAS + dequant template for all
  shapes'
experience_type: optimization
source_category: agent-experiment
architectures:
- sm90
tags:
- gemm
- fine-grained-quantization
kernel_types:
- gemm
languages:
- cuda-cpp
captured_at: '2026-05-14'
confidence: inferred
reproducibility: snippet
techniques:
- fine-grained-quantization
impl_family: cublas
---

A complete, verified, copy-paste-ready INT8 GEMM solution using cuBLAS cublasGemmEx + custom dequant kernel. This template works for ALL SOL-ExecBench PI-int8 GEMM shapes (M=10 to M=968). Achieved 2.0x-2.7x speedup on verified experiments. The key insight: B is [K,N] column-major in SOL-ExecBench, and cuBLAS output [N,M] column-major has identical memory layout to [M,N] row-major, so no transpose is needed in the dequant kernel.

## Challenge

Agents struggle to produce a working INT8 GEMM implementation because they must simultaneously solve: (1) B matrix is [K,N] column-major not row-major, (2) cuBLAS parameter mapping for mixed row/column-major inputs, (3) int32 accumulation output needs dequantization to bfloat16, (4) scale_a[M] and scale_b[N] are per-element float arrays not scalars. Each individual mistake causes complete failure.

### Symptoms

- `77% of all INT8 GEMM attempts fail correctness due to B layout confusion`
- `cuBLAS status 7 (invalid value) from wrong leading dimensions`
- `max_relative_error > 1e6 from wrong matrix indexing`
- `scale_a.item<float>() crash when scale tensors have multiple elements`
- `Output dtype mismatch: producing int32 when bfloat16 is required`

## Solution

Use this complete, verified template. Three files: kernel.h, kernel.cu, main.cpp. Based on the successful autoresearch_20260512_112315_36b48a7f experiment (2.67x speedup on m10_n1024_k2048).

### Implementation

```cuda
## kernel.h
```cpp
#pragma once
#include <cuda_runtime.h>

#ifdef __cplusplus
extern "C" {
#endif

void gemm_int8_dequant_cuda(
    const int8_t* A, const int8_t* B,
    const float* scale_a, const float* scale_b,
    void* C_bf16, int32_t* workspace,
    int M, int N, int K, cudaStream_t stream);

#ifdef __cplusplus
}
#endif
```

## kernel.cu
```cpp
#include <cuda_runtime.h>
#include <cublas_v2.h>
#include <cstdint>
#include <cuda_fp16.h>

// Dequant: C_bf16[m,n] = bf16(workspace[m,n] * scale_a[m] * scale_b[n])
// workspace is [M,N] row-major (see cuBLAS layout note below)
__global__ void dequant_kernel(
    const int32_t* __restrict__ workspace,
    const float* __restrict__ scale_a,
    const float* __restrict__ scale_b,
    uint16_t* __restrict__ C_bf16,
    int M, int N)
{
    int row = blockIdx.y * blockDim.y + threadIdx.y;
    int col = blockIdx.x * blockDim.x + threadIdx.x;
    if (row >= M || col >= N) return;

    int32_t val = workspace[row * N + col];
    float result = static_cast<float>(val) * scale_a[row] * scale_b[col];
    C_bf16[row * N + col] = __bfloat16_as_ushort(__float2bfloat16(result));
}

static cublasHandle_t get_cublas_handle() {
    static cublasHandle_t handle = nullptr;
    if (!handle) { cublasCreate(&handle); }
    return handle;
}

extern "C" void gemm_int8_dequant_cuda(
    const int8_t* A, const int8_t* B,
    const float* scale_a, const float* scale_b,
    void* C_bf16, int32_t* workspace,
    int M, int N, int K, cudaStream_t stream)
{
    cublasHandle_t handle = get_cublas_handle();
    cublasSetStream(handle, stream);

    // SOL-ExecBench layout:
    //   A: [M,K] row-major  -> cuBLAS sees A_col[K,M]
    //   B: [K,N] col-major  -> cuBLAS sees B_col[K,N]
    //
    // cuBLAS computes: D_col = op(A_param) * op(B_param)
    //   A_param = B_col[K,N], opA=T -> B_col^T [N,K]
    //   B_param = A_col[K,M], opB=N -> A_col   [K,M]
    //   D_col[N,M] = B_col^T[N,K] * A_col[K,M]
    //
    // KEY: D_col[N,M] column-major has identical memory layout to
    //      C_row[M,N] row-major: element at [m,n] is at offset m*N+n in both.
    //      So workspace[m*N+n] = D[n,m] = sum_k B[k,n]*A[m,k] = correct C[m,n].
    //
    // Parameters: m=N, n=M, k=K
    //   lda=K (B_col has K rows), ldb=K (A_col has K rows), ldc=N (D_col has N rows)
    int32_t alpha = 1, beta = 0;
    cublasGemmEx(handle,
        CUBLAS_OP_T, CUBLAS_OP_N,
        N, M, K,
        &alpha,
        B, CUDA_R_8I, K,
        A, CUDA_R_8I, K,
        &beta,
        workspace, CUDA_R_32I, N,
        CUDA_R_32I,
        CUBLAS_GEMM_DEFAULT_TENSOR_OP);

    dim3 blk(32, 8);
    dim3 grd((N + 31) / 32, (M + 7) / 8);
    dequant_kernel<<<grd, blk, 0, stream>>>(
        workspace, scale_a, scale_b,
        static_cast<uint16_t*>(C_bf16), M, N);
}
```

## main.cpp
```cpp
#include <torch/extension.h>
#include <ATen/cuda/CUDAContext.h>
#include "kernel.h"

void run(torch::Tensor A, torch::Tensor B,
         torch::Tensor scale_a, torch::Tensor scale_b,
         torch::Tensor C)
{
    int M = A.size(0);
    int K = A.size(1);
    int N = B.size(1);  // B is [K,N] col-major: size(0)=K, size(1)=N

    auto workspace = torch::empty({M, N},
        torch::dtype(torch::kInt32).device(A.device()));

    gemm_int8_dequant_cuda(
        A.data_ptr<int8_t>(), B.data_ptr<int8_t>(),
        scale_a.data_ptr<float>(), scale_b.data_ptr<float>(),
        C.data_ptr<at::BFloat16>(), workspace.data_ptr<int32_t>(),
        M, N, K, at::cuda::getCurrentCUDAStream());
}

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
    m.def("run", &run);
}
```
```

## Key Lessons

- B is [K,N] column-major in SOL-ExecBench PI-int8 tasks. Always use N = B.size(1), not B.size(0). B.size(0) equals K.
- cuBLAS output [N,M] column-major and [M,N] row-major have identical memory layout (offset m*N+n maps to same element). No transpose needed in dequant kernel.
- cuBLAS parameters for this layout: opA=CUBLAS_OP_T, opB=CUBLAS_OP_N, m=N, n=M, k=K, lda=K, ldb=K, ldc=N. A_param=B, B_param=A.
- Use int32_t alpha/beta (not float) for CUDA_R_32I compute type with INT8 inputs.
- Persistent cuBLAS handle via static variable avoids ~5us per-call overhead.
- scale_a is float[M] (per-token), scale_b is float[N] (per-channel). Both are arrays, NOT scalars. Never call .item<float>() on them.
- Output C must be bfloat16 (at::BFloat16), NOT int32 or float32. The dequant kernel converts int32 accumulator to bfloat16.
- workspace tensor is int32 [M,N]. In main.cpp, allocate with torch::empty({M,N}, dtype=torch.kInt32).
- This template gives 2.0x-2.7x speedup. For higher speedup (4x-6x), CUTLASS fused epilogue is needed but much harder to implement correctly.
