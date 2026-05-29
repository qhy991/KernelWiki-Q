---
id: exp-r-20260513-100008-bf16-static-gate-cuda-type-in-cpp
title: 'SOL-ExecBench BF16 output: __nv_bfloat16 type in .cpp file triggers static
  gate error'
experience_type: repair
source_category: agent-experiment
architectures:
- sm90
tags:
- gemm
kernel_types:
- gemm
languages:
- cuda-cpp
captured_at: '2026-05-13'
confidence: inferred
reproducibility: snippet
impl_family: custom_cuda
---

SOL-ExecBench compiles .cpp files with g++ (host compiler) and .cu files with nvcc. Using CUDA-specific types like __nv_bfloat16, __half, or kernel launch syntax in .cpp files triggers: 'static_gate_error: main.cpp contains CUDA-only construct __nv_bfloat16. .cpp wrapper files are compiled by the host compiler'. Move all CUDA types and kernel logic to .cu files.

## Challenge

Agent writes main.cpp that uses __nv_bfloat16 type for BF16 data pointer access (e.g., reinterpret_cast<__nv_bfloat16*>(C.data_ptr())). The .cpp file is compiled by g++ which does not understand CUDA-specific types.

### Symptoms

- `static_gate_error: 'main.cpp' contains CUDA-only construct '__nv_bfloat16'`
- `.cpp wrapper files are compiled by the host compiler`
- `Compile smoke fails before actual compilation starts`

## Solution

Keep main.cpp clean with only PyTorch C++ types (torch::Tensor, at::BFloat16). Use void* for passing data pointers to kernel launcher. Put all CUDA-specific types (__nv_bfloat16, __half, cudaMalloc, kernel launches) in kernel.cu.

### Implementation

```cuda
// kernel.h (clean C++ header):
#pragma once
#include <cuda_runtime.h>
void gemm_launcher(const void* A, const void* B, void* C,
                   int M, int N, int K, cudaStream_t stream);

// main.cpp (NO CUDA types):
#include <torch/extension.h>
#include "kernel.h"
void run(const torch::Tensor& A, const torch::Tensor& B, torch::Tensor& C) {
    gemm_launcher(A.data_ptr(), B.data_ptr(), C.data_ptr(),
                  A.size(0), B.size(0), A.size(1),
                  at::cuda::getCurrentCUDAStream());
}
PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) { m.def("run", &run); }

// kernel.cu (CUDA types allowed):
#include "kernel.h"
#include <cuda_bf16.h>
void gemm_launcher(const void* A, const void* B, void* C, ...) {
    auto a = reinterpret_cast<const __nv_bfloat16*>(A);
    auto c = reinterpret_cast<__nv_bfloat16*>(C);
    // ... kernel logic ...
}
```

## Key Lessons

- SOL-ExecBench .cpp files are compiled by g++, NOT nvcc. Never use CUDA-only types (__nv_bfloat16, __half, dim3, <<<>>>) in .cpp files.
- The static gate checks for CUDA-only constructs in .cpp files and rejects them before compilation. This is a pre-compilation safety check.
- Use void* in kernel.h function signatures to pass data pointers between .cpp and .cu. Reinterpret_cast to CUDA types only inside .cu files.
- Common CUDA-only types to avoid in .cpp: __nv_bfloat16, __half, half2, cudaError_t (beyond what's in cuda_runtime.h), dim3.
- kernel.h can include <cuda_runtime.h> (which is available to both host and device compiler). But <cuda_bf16.h> and <cuda_fp16.h> are CUDA-only.
- For BF16 data access in .cu: reinterpret_cast<__nv_bfloat16*>(tensor.data_ptr()) or reinterpret_cast<__nv_bfloat16*>(tensor.data_ptr<at::BFloat16>()).
