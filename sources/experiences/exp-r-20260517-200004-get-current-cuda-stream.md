---
id: exp-r-20260517-200004-get-current-cuda-stream
title: getCurrentCUDAStream is not a member of at::cuda
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

- Prefer getting the CUDA stream inside kernel.cu, not main.cpp — this keeps main.cpp CUDA-free and avoids API version issues.
- If you must use it in main.cpp: c10::cuda::getCurrentCUDAStream() returns a CUDAStream object.
- To get raw cudaStream_t from CUDAStream: call .stream() method on the returned object.
- at::cuda::getCurrentCUDAStream without arguments is deprecated; use c10::cuda version or pass device index.
- Never cast CUDAStream to void* — use .stream() to get the raw cudaStream_t handle.
- On PyTorch 2.6+: c10::cuda::getCurrentCUDAStream(device.index()) is the safest API.
