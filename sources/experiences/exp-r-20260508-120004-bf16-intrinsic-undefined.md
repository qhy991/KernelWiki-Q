---
id: exp-r-20260508-120004-bf16-intrinsic-undefined
title: exp-r-20260508-120004-bf16-intrinsic-undefined
experience_type: repair
source_category: agent-experiment
architectures:
- sm90
tags:
- layer-norm
kernel_types:
- layer-norm
languages:
- cuda-cpp
captured_at: '2026-05-08'
confidence: inferred
reproducibility: snippet
impl_family: custom_cuda
---

## Key Lessons

- Always include both <cuda_bf16.h> and <cuda_bf16.hpp> when using bf16 in custom kernels.
- For GEMM workloads, prefer cublasGemmEx which handles bf16 data internally.
