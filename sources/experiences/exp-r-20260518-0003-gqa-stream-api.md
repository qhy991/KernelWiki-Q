---
id: exp-r-20260518-0003-gqa-stream-api
title: 'GQA paged decode: wrong CUDA stream API (c10 vs at) and missing cuda_runtime.h'
experience_type: repair
source_category: agent-experiment
architectures:
- sm90
tags:
- attention
kernel_types:
- attention
languages:
- cuda-cpp
captured_at: '2026-05-18'
confidence: inferred
reproducibility: concept
---

GQA paged decode: wrong CUDA stream API (c10 vs at) and missing cuda_runtime.h

## Key Lessons

- Use at::cuda::getCurrentCUDAStream() — the public PyTorch CUDA API
- Never use c10::cuda::getCurrentCUDAStream() — it's an internal namespace
- Always #include <ATen/cuda/CUDAContext.h> in .cpp files that call CUDA stream APIs
- Always #include <cuda_runtime.h> in .h files that declare cudaStream_t parameters
- cudaStream_t is a CUDA runtime type, not a PyTorch type — it needs the CUDA runtime header
