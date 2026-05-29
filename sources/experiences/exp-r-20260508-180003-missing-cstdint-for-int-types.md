---
id: exp-r-20260508-180003-missing-cstdint-for-int-types
title: exp-r-20260508-180003-missing-cstdint-for-int-types
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
captured_at: '2026-05-08'
confidence: inferred
reproducibility: concept
techniques:
- fine-grained-quantization
impl_family: cublas
---

## Key Lessons

- Always include <cstdint> in kernel.h when the interface uses int8_t or int32_t.
- CUDA headers do not transitively provide std integer types.
- For BF16 solutions, use void* in kernel.h to avoid needing CUDA bf16 headers.
