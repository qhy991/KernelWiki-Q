---
id: exp-r-20260517-200000-nv-bfloat16-in-cpp
title: CUDA BF16 type in .cpp wrapper causes host compiler error
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
captured_at: '2026-05-17'
confidence: inferred
reproducibility: concept
impl_family: custom_cuda
---

## Key Lessons

- main.cpp must be pure host C++: only torch::Tensor, pybind11, and standard C++ types. No CUDA-specific types.
- kernel.cu holds all CUDA device code: __global__ kernels, __device__ helpers, data pointer casts to CUDA types, kernel launch calls.
- kernel.h bridges .cpp and .cu: declare host-callable functions. If any parameter uses CUDA types (cudaStream_t, __nv_bfloat16*), the header must #include <cuda_runtime.h> (and cuda_bf16.h if needed).
- The run() function in main.cpp should call a function declared in kernel.h and defined in kernel.cu — this keeps .cpp free of CUDA types.
- For BF16: use torch::BFloat16 in main.cpp, cast to __nv_bfloat16* inside kernel.cu's run() implementation.
