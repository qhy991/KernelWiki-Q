---
id: exp-r-20260508-180002-cutlass-extreme-aspect-ratio
title: exp-r-20260508-180002-cutlass-extreme-aspect-ratio
experience_type: repair
source_category: agent-experiment
architectures:
- sm90
tags:
- gemm
- tile-scheduling
- fine-grained-quantization
kernel_types:
- gemm
languages:
- cuda-cpp
- cute-dsl
captured_at: '2026-05-08'
confidence: inferred
reproducibility: concept
techniques:
- tile-scheduling
- fine-grained-quantization
impl_family: cutlass
---

## Solution

Switch to cuBLAS cublasGemmEx for these problem sizes. cuBLAS handles all matrix dimensions correctly.

## Key Lessons

- CUTLASS has a hard limitation on extreme aspect ratios: M must be large enough for tile iterations to be non-zero.
- For M<=16 or N>=8192, always use cuBLAS instead of CUTLASS.
- This error occurs at compile time (static_assert), not runtime.
