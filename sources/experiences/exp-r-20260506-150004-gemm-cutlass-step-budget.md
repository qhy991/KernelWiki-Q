---
id: exp-r-20260506-150004-gemm-cutlass-step-budget
title: 'SOL-ExecBench GEMM: CUTLASS template debugging exhausts step budget'
experience_type: repair
source_category: agent-experiment
architectures:
- sm90
tags:
- gemm
kernel_types:
- gemm
languages:
- cuda-cpp
captured_at: '2026-05-06'
confidence: inferred
reproducibility: snippet
impl_family: cublas
---

CUTLASS INT8/BF16 GEMM template instantiation errors consume 20+ steps per attempt. For small batch GEMM, cuBLAS is faster to implement and achieves comparable speedup.

## Challenge

Agent attempts CUTLASS INT8/BF16 GEMM implementation but gets stuck in template instantiation error loops. CUTLASS requires precise type matching, architecture specification, and include paths. Debugging these errors consumes most of the step budget (typically 52 steps) before verification can run.

### Symptoms

- `Step budget exhausted after 52 steps with no verified result`
- `Multiple compilation attempts with different CUTLASS template parameters`
- `Errors: incomplete type, no matching overloaded function, template argument deduction failed`
- `Agent spends steps on CUTLASS include path fixes instead of working solution`

## Solution

For GEMM optimization tasks, implement cuBLAS solution FIRST as baseline, then only attempt CUTLASS if cuBLAS baseline is already verified and more optimization is needed.

### Implementation

```cuda
1. Step allocation for GEMM tasks:
   - Steps 1-8: cuBLAS cublasGemmEx implementation + verify
   - Steps 9-15: If cuBLAS works, try CUTLASS only if additional speedup is needed
   - Steps 16-52: Only if CUTLASS is clearly beneficial
2. CUTLASS requirements checklist (verify ALL before coding):
   - Include path: -I/home/qinhaiyan/cutlass/include in compile_options
   - Architecture: match GPU SM version (Sm80, Sm89, etc.)
   - Type matching: ElementA=uint8_t, ElementB=uint8_t, ElementC=int32_t for INT8
   - Layout: RowMajor vs ColumnMajor must match actual data layout
3. If CUTLASS fails 3 compilation attempts, switch to cuBLAS immediately
```

## Key Lessons

- CUTLASS GEMM template debugging can consume 20+ steps - start with cuBLAS instead.
- cuBLAS cublasGemmEx achieves 1.4x~3.8x for small batch GEMM - good enough for most tasks.
- Only attempt CUTLASS after a verified cuBLAS baseline exists.
- Limit CUTLASS debugging to 3 compilation attempts before falling back.
- CUTLASS requires -I/home/qinhaiyan/cutlass/include in compile_options - check this first.
- Step budget allocation: 8 steps for cuBLAS, 15 for CUTLASS, only if needed.
- For INT8 GEMM M<=50, cuBLAS with persistent handle is the recommended first approach.
