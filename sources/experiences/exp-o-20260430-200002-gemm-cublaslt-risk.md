---
id: exp-o-20260430-200002-gemm-cublaslt-risk
title: 'SOL-ExecBench BF16 GEMM: cuBLASLt is a risky first fallback'
experience_type: optimization
source_category: agent-experiment
architectures:
- sm90
tags:
- gemm
kernel_types:
- gemm
languages:
- cuda-cpp
captured_at: '2026-04-30'
confidence: inferred
reproducibility: concept
impl_family: cublaslt
---

When CUTLASS is abandoned, jumping directly to cuBLASLt often introduces descriptor/API compile failures. Use cublasGemmEx first unless a known-good cuBLASLt template already exists.

## Challenge

After abandoning CUTLASS on a BF16 GEMM task, the agent switched to a more complex cuBLASLt implementation. The descriptor-based API introduced multiple compile blockers before the code even reached correctness measurement.

## Solution

Treat cuBLASLt as a second-stage optimization only. The first fallback from CUTLASS should be cublasGemmEx. Only move to cuBLASLt after a correctness-passing cuBLAS baseline exists and only when using a known-good local template.

The failed route mixed cublasLt descriptor handles, matrix layouts, search helpers, and stream APIs in one step. That produced compile-time type mismatches and undefined-symbol errors. The system lost time on API plumbing instead of measuring kernel performance.

## Key Lessons

- cuBLASLt should not be the first fallback from CUTLASS on SOL-ExecBench BF16 GEMM unless a validated local template is available.
- Descriptor-heavy cuBLASLt code is high-risk for compile blockers and can waste the whole round before correctness is even tested.
- A simple cublasGemmEx baseline gives a much better correctness-to-effort ratio than an ad hoc cuBLASLt rewrite.
- If cuBLASLt is pursued later, do it only after a passing cublasGemmEx baseline is already frozen.
