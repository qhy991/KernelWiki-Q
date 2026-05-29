---
id: exp-r-20260508-160102-gemm-contiguous-stride-correctness
title: exp-r-20260508-160102-gemm-contiguous-stride-correctness
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
reproducibility: snippet
techniques:
- fine-grained-quantization
impl_family: cublas,torch
---

## Key Lessons

- Data layout sanity is a correctness prerequisite, not an optimization detail.
- Use contiguous tensors as the single source of truth for dimensions and pointers.
