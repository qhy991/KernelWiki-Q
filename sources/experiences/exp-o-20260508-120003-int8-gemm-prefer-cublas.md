---
id: exp-o-20260508-120003-int8-gemm-prefer-cublas
title: INT8 GEMM has 19.2% pass rate overall (5/26 attempts)
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
impl_family: cublas
---

## Challenge

INT8 GEMM has 19.2% pass rate overall (5/26 attempts). CUTLASS-based approaches have very low pass rate due to template configuration complexity. Which approach should be default for INT8 GEMM?

## Key Lessons

- Default to cuBLAS cublasGemmEx for INT8 GEMM.
- Only consider CUTLASS if cuBLAS fails AND the CUTLASS template has been verified to compile.
- If using CUTLASS: OpClassSimt + Sm80 + GemmShape<128,128,64> is the only verified combination.
