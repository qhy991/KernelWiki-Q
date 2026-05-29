---
id: exp-r-20260508-120005-cutlass-int8-alignment
title: exp-r-20260508-120005-cutlass-int8-alignment
experience_type: repair
source_category: agent-experiment
architectures:
- sm90
tags:
- gemm
- fine-grained-quantization
- vectorized-loads
kernel_types:
- gemm
languages:
- cuda-cpp
- cute-dsl
captured_at: '2026-05-08'
confidence: inferred
reproducibility: snippet
techniques:
- fine-grained-quantization
- vectorized-loads
impl_family: cutlass
---

## Key Lessons

- For CUTLASS INT8, ensure K % tile_K == 0 and K % 16 == 0.
- Use smaller tile shapes when alignment is uncertain.
- Prefer cuBLAS over CUTLASS for INT8 GEMM to avoid alignment issues.
