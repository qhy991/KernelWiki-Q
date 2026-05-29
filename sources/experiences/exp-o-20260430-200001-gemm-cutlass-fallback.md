---
id: exp-o-20260430-200001-gemm-cutlass-fallback
title: 'SOL-ExecBench BF16 dense GEMM: fallback from CUTLASS to cuBLAS'
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
confidence: source-reported
reproducibility: concept
impl_family: cublas
speedup: 1.69x to 2.27x
---

On SOL-ExecBench BF16 dense GEMM tasks, CUTLASS is worth trying first, but the robust fallback path is usually cuBLAS cublasGemmEx rather than forcing CUTLASS to win.

## Challenge

Several SOL-ExecBench BF16 GEMM tasks started from a CUTLASS-oriented plan, but the default CUTLASS path was either slower than the reference implementation or showed numerical instability when using a basic SIMT-style configuration. The system needed a fallback that preserved correctness and still improved latency.

## Solution

Try CUTLASS first for GEMM-like tasks, but if the first CUTLASS candidate is slower than reference or shows correctness drift, fall back immediately to a plain cuBLAS BF16 GEMM baseline using cublasGemmEx with FP32 accumulation and Tensor Core mode.

The reliable path was a manifest-backed cuda_cpp solution with row-major A[M,K], row-major B[N,K], and output C[M,N] for C = A @ B^T. The stable fallback used cuBLAS row-major/column-major mapping with CUBLAS_OP_T / CUBLAS_OP_N as needed, FP32 accumulation, and a persistent or reused cuBLAS handle. This route repeatedly produced passing correctness with meaningful speedup, whereas insisting on CUTLASS SIMT as the primary implementation did not.

## Results

- **speedup_range**: 1.69x to 2.27x
- **correctness**: passed
- **max_relative_error**: 0.0
- **max_absolute_error**: 0.0

## Key Lessons

- For SOL-ExecBench BF16 dense GEMM, CUTLASS is a candidate, not a commitment; if the first CUTLASS implementation is slower or numerically unstable, fallback early.
- The most reliable fallback is plain cublasGemmEx with FP32 accumulation and Tensor Core mode, not a more complex descriptor-heavy path.
- For row-major SOL problems defined as C = A @ B.T with A[M,K] and B[N,K], robust row-major/column-major mapping matters more than aggressively using a custom kernel.
- Repeated experiments showed that a simple cuBLAS BF16 GEMM baseline can beat reference latency while preserving exact correctness on these tasks.
