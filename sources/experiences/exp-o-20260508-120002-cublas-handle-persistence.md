---
id: exp-o-20260508-120002-cublas-handle-persistence
title: exp-o-20260508-120002-cublas-handle-persistence
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
captured_at: '2026-05-08'
confidence: inferred
reproducibility: concept
techniques:
- fine-grained-quantization
impl_family: cublas
---

## Key Lessons

- Always use persistent cuBLAS handles — never create/destroy per call.
- thread_local static handle is the recommended pattern for kernel.cu.
- at::cuda::getCurrentCUDABlasHandle() is simplest when PyTorch binding is available.
- Remember to set stream: cublasSetStream(handle, stream) after getting handle.
