---
id: exp-r-20260517-200002-kernel-h-missing-cuda-runtime
title: kernel.h uses cudaStream_t but does not include cuda_runtime.h
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

- Every header file must be self-contained: include everything needed for its own declarations.
- kernel.h must #include <cuda_runtime.h> if it uses cudaStream_t, dim3, or any CUDA pointer type.
- kernel.h must #include <cuda_bf16.h> if it uses __nv_bfloat16* in declarations.
- kernel.h must #include <cuda_fp16.h> if it uses __half* in declarations.
- The include order in kernel.h: standard headers first, then CUDA headers, then PyTorch headers.
- Alternative approach: keep kernel.h clean by declaring only torch::Tensor-based interfaces; hide all CUDA types inside kernel.cu's implementation. This avoids CUDA headers in kernel.h entirely.
