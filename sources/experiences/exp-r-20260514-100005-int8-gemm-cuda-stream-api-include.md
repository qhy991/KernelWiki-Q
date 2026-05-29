---
id: exp-r-20260514-100005-int8-gemm-cuda-stream-api-include
title: 'SOL-ExecBench INT8 GEMM: CUDA stream API and .cu/.cpp file responsibility'
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
impl_family: cublas
---

The most common compilation failure in INT8 GEMM experiments (~65% of build errors) is incorrect CUDA stream acquisition. Agents write at::cuda::getCurrentCUDAStream() in .cu files or without the required header. ATen APIs are only available in main.cpp (compiled by g++), not in kernel.cu (compiled by nvcc). The .cu file must only contain pure CUDA code and extern C bridge functions.

## Challenge

Agents mix ATen/C++ APIs into .cu files, causing compilation failures. The three-file SOL-ExecBench template (kernel.h, kernel.cu, main.cpp) has a strict responsibility split: kernel.cu is compiled by nvcc and can only use CUDA/C APIs; main.cpp is compiled by g++ and has full ATen/PyTorch access. Violating this split causes 'not a member' errors.

### Symptoms

- `error: 'getCurrentCUDAStream' is not a member of 'at::cuda'`
- `error: namespace "at::cuda" has no member "getCurrentCUDAStream"`
- `error: identifier "at" is undefined (in kernel.cu)`
- `error: 'torch' has not been declared (in kernel.cu)`
- `fatal error: 'ATen/cuda/CUDAContext.h' file not found (nvcc cannot find ATen headers)`

## Solution

Follow the strict three-file responsibility model. CUDA stream acquisition goes in main.cpp. kernel.cu receives the stream as a cudaStream_t parameter through the extern C bridge function.

### Implementation

```cuda
## File responsibility model for SOL-ExecBench CUDA kernels:

### kernel.h — C-compatible declarations ONLY
```cpp
#pragma once
#include <cuda_runtime.h>
#ifdef __cplusplus
extern "C" {
#endif
void gemm_int8_dequant_cuda(
    const int8_t* A, const int8_t* B,
    const float* scale_a, const float* scale_b,
    void* C, int32_t* workspace,
    int M, int N, int K, cudaStream_t stream);  // stream as parameter
#ifdef __cplusplus
}
#endif
```

### kernel.cu — Pure CUDA code ONLY (no ATen, no torch)
```cpp
#include <cuda_runtime.h>
#include <cublas_v2.h>
#include <cstdint>
#include "kernel.h"
// Do NOT include <torch/extension.h> or <ATen/...> here!
// Do NOT call at::cuda::getCurrentCUDAStream() here!

extern "C" void gemm_int8_dequant_cuda(
    const int8_t* A, const int8_t* B,
    const float* scale_a, const float* scale_b,
    void* C, int32_t* workspace,
    int M, int N, int K, cudaStream_t stream) {
    // Use the stream parameter directly
    cublasHandle_t handle = get_cublas_handle();
    cublasSetStream(handle, stream);
    // ...
}
```

### main.cpp — ATen/PyTorch APIs live HERE
```cpp
#include <torch/extension.h>
#include <ATen/cuda/CUDAContext.h>  // Required for getCurrentCUDAStream
#include "kernel.h"

void run(torch::Tensor A, torch::Tensor B,
         torch::Tensor scale_a, torch::Tensor scale_b,
         torch::Tensor C) {
    // Get CUDA stream here in main.cpp, pass to kernel
    auto stream = at::cuda::getCurrentCUDAStream();
    gemm_int8_dequant_cuda(
        A.data_ptr<int8_t>(), B.data_ptr<int8_t>(),
        scale_a.data_ptr<float>(), scale_b.data_ptr<float>(),
        C.data_ptr(), workspace.data_ptr<int32_t>(),
        M, N, K, stream);
}
```
```

## Key Lessons

- kernel.cu is compiled by nvcc and can only use CUDA/C APIs (cuda_runtime.h, cublas_v2.h, stdint.h). Never include torch/extension.h or ATen headers in .cu files.
- main.cpp is compiled by g++ and has full ATen/PyTorch access. ATen APIs like at::cuda::getCurrentCUDAStream() ONLY work here.
- The bridge between .cu and .cpp is extern C functions that take cudaStream_t as a parameter. kernel.h declares these with extern C guards.
- If you see 'getCurrentCUDAStream is not a member of at::cuda', the fix is: (1) move the call to main.cpp, (2) add #include <ATen/cuda/CUDAContext.h>, (3) pass stream to kernel as cudaStream_t parameter.
- Required includes in main.cpp for CUDA stream: #include <torch/extension.h> and #include <ATen/cuda/CUDAContext.h>. Both are required.
