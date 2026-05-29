---
id: exp-r-20260518-0001-gqa-cuda-syntax-in-cpp
title: 'GQA paged decode: __nv_bfloat16 and CUDA types in .cpp files'
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

## Key Lessons

- Never put __nv_bfloat16, __nv_bfloat162, cudaStream_t, __global__, blockIdx, threadIdx, or <<<>>> in .cpp files
- Use void* in .h launcher declarations, cast to __nv_bfloat16* inside .cu implementation
- Use at::cuda::getCurrentCUDAStream() (not c10::cuda::...) in host code
- Include <cuda_runtime.h> in .h files and .cu files, not in .cpp files
- The SOL-ExecBench static_gate checks for CUDA syntax in .cpp files BEFORE compilation — fix the sources, don't try to bypass the gate
