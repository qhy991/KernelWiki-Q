---
id: exp-r-20260508-120001-aten-getCurrentCUDAStream
title: exp-r-20260508-120001-aten-getCurrentCUDAStream
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
captured_at: '2026-05-08'
confidence: inferred
reproducibility: snippet
impl_family: cublas
---

## Challenge

Compiler error: 'getCurrentCUDAStream' is not a member of 'at::cuda' or 'torch::cuda'. This is the #1 most frequent compilation error across 82 autoresearch experiments (6 out of 21 compile failures).

## Key Lessons

- kernel.cu must never include ATen or torch headers — only CUDA runtime and library headers.
- cudaStream_t should be passed as a parameter to kernel functions, not obtained inside .cu files.
- The three-file split (kernel.h / kernel.cu / main.cpp) is mandatory for SOL-ExecBench cuda_cpp solutions.
