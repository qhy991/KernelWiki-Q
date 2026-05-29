---
id: exp-r-20260508-180002-cutlass-extreme-aspect-ratio
title: Switch to cuBLAS cublasGemmEx for these problem sizes. cuBLAS handles all matrix
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

## Challenge

CUTLASS GEMM compilation fails with 'static assertion failed: Number of iterations must be non-zero' in pitch_linear_thread_map.h when M is very small (<=16) and N is very large (>=8192).


## Solution

Switch to cuBLAS cublasGemmEx for these problem sizes. cuBLAS handles all matrix dimensions correctly.

## Key Lessons

- CUTLASS has a hard limitation on extreme aspect ratios: M must be large enough for tile iterations to be non-zero.
- For M<=16 or N>=8192, always use cuBLAS instead of CUTLASS.
- This error occurs at compile time (static_assert), not runtime.
