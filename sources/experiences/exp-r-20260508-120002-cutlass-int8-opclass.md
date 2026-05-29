---
id: exp-r-20260508-120002-cutlass-int8-opclass
title: exp-r-20260508-120002-cutlass-int8-opclass
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

## Key Lessons

- For INT8 GEMM, always prefer cuBLAS cublasGemmEx over CUTLASS.
- If CUTLASS is required, use OpClassSimt + Sm80 + GemmShape<128,128,64>.
- Ensure matrix dimensions are compatible with tile shapes (K divisible by tile_K).
