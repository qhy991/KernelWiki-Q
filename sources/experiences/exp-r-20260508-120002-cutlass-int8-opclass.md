---
id: exp-r-20260508-120002-cutlass-int8-opclass
title: CUTLASS 2.x INT8 GEMM compilation fails with namespace errors or static assertio
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
reproducibility: snippet
techniques:
- tile-scheduling
- fine-grained-quantization
impl_family: cutlass
---

## Challenge

CUTLASS 2.x INT8 GEMM compilation fails with namespace errors or static assertions. 5 out of 21 compile failures are CUTLASS configuration issues.

## Key Lessons

- For INT8 GEMM, always prefer cuBLAS cublasGemmEx over CUTLASS.
- If CUTLASS is required, use OpClassSimt + Sm80 + GemmShape<128,128,64>.
- Ensure matrix dimensions are compatible with tile shapes (K divisible by tile_K).
