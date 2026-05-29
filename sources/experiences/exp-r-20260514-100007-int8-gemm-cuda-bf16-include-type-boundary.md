---
id: exp-r-20260514-100007-int8-gemm-cuda-bf16-include-type-boundary
title: 'SOL-ExecBench INT8 GEMM: cuda_bf16.h include and host/device type boundary'
experience_type: repair
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
impl_family: custom_cuda
---

INT8 GEMM dequant kernels that output bfloat16 require #include <cuda_bf16.h> for __nv_bfloat16 and __float2bfloat16 intrinsics. Using at::BFloat16 in kernel.cu causes 'identifier at is undefined' because nvcc cannot see ATen types. The type boundary is strict: device code uses __nv_bfloat16 / uint16_t, host code uses at::BFloat16.

## Challenge

Agent writes dequantization kernels using bfloat16 intrinsics (__float2bfloat16, __bfloat16_as_ushort) without including cuda_bf16.h, or uses at::BFloat16 directly in .cu files. nvcc cannot resolve ATen types, causing compilation failure.

### Symptoms

- `error: identifier "__float2bfloat16" is undefined`
- `error: identifier "__bfloat16_as_ushort" is undefined`
- `error: identifier "nv_bfloat16" is undefined`
- `error: identifier "at" is undefined (when using at::BFloat16 in .cu)`
- `error: global-scope qualifier (leading "::") is not allowed`

## Solution

Include <cuda_bf16.h> in kernel.cu. Use __nv_bfloat16 or uint16_t for bfloat16 data in device code. Never use at::BFloat16 or torch:: types in .cu files. Cast between host and device types at the boundary in main.cpp.

### Implementation

```cuda
## kernel.cu — Device code uses CUDA-native bfloat16 types
```cpp
#include <cuda_runtime.h>
#include <cuda_bf16.h>     // REQUIRED for __float2bfloat16, __nv_bfloat16
#include <cublas_v2.h>
#include <cstdint>

// Dequant kernel writing bfloat16 output
__global__ void dequant_kernel(
    const int32_t* workspace,
    const float* scale_a,
    const float* scale_b,
    uint16_t* C_bf16,        // Use uint16_t* for bfloat16 bits
    int M, int N) {
    int row = blockIdx.y * blockDim.y + threadIdx.y;
    int col = blockIdx.x * blockDim.x + threadIdx.x;
    if (row >= M || col >= N) return;
    float val = (float)workspace[row * N + col] * scale_a[row] * scale_b[col];
    C_bf16[row * N + col] = __bfloat16_as_ushort(__float2bfloat16(val));
}

// Alternative: use __nv_bfloat16* directly
// __nv_bfloat16* C_bf16 = ...;
// C_bf16[idx] = __float2bfloat16(val);
```

## main.cpp — Host code uses ATen types
```cpp
#include <torch/extension.h>
#include "kernel.h"

void run(..., torch::Tensor C) {
    // Cast ATen pointer to raw type for kernel call
    gemm_int8_dequant_cuda(
        ..., 
        static_cast<uint16_t*>(C.data_ptr<at::BFloat16>()),  // host-side cast
        // OR if C is float32:
        // C.data_ptr<float>(),
        ...);
}
```

## Type boundary rules:
// DEVICE (.cu)              HOST (.cpp)
// __nv_bfloat16          ↔ at::BFloat16
// uint16_t (bf16 bits)   ↔ at::BFloat16
// int8_t                 ↔ torch.int8 tensor
// int32_t                ↔ torch.int32 tensor
// float                  ↔ torch.float32 tensor
// cudaStream_t           ↔ at::cuda::getCurrentCUDAStream()

## DO NOT:
// #include <torch/extension.h>  in kernel.cu
// Use at::BFloat16 in kernel.cu
// Use torch::Tensor in kernel.cu
// Forget #include <cuda_bf16.h> when using __float2bfloat16
```

## Key Lessons

- kernel.cu MUST include <cuda_bf16.h> when using __float2bfloat16, __bfloat16_as_ushort, or __nv_bfloat16. Without this header, these intrinsics are undefined.
- Never use at::BFloat16, torch::Tensor, or any ATen type in kernel.cu. nvcc cannot resolve ATen namespaces. Use __nv_bfloat16 or uint16_t for bfloat16 data in device code.
- The type boundary between host (.cpp) and device (.cu) is strict: host uses ATen types (at::BFloat16, torch::Tensor), device uses CUDA native types (__nv_bfloat16, int8_t, uint16_t, cudaStream_t).
- For bfloat16 output, write uint16_t bits via __bfloat16_as_ushort(__float2bfloat16(val)) or assign __nv_bfloat16 directly. Both require cuda_bf16.h.
- The host-device type cast happens in main.cpp: static_cast<uint16_t*>(C.data_ptr<at::BFloat16>()) bridges ATen and CUDA bfloat16 representations.
