---
id: exp-o-20260508-160202-gemm-strategy-dispatch-by-shape
title: No single GEMM path dominates all shapes
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
impl_family: cublas,torch,cutlass
---

## Challenge

No single GEMM path dominates all shapes. A static implementation can underperform or fail for specific size regimes.

## Key Lessons

- Optimization should be policy-driven by shape/dtype, not by one favorite backend.
- Stable fallback paths are mandatory for step-budget efficiency.
