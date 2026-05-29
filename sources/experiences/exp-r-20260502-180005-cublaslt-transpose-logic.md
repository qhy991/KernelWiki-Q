---
id: exp-r-20260502-180005-cublaslt-transpose-logic
title: sol_execbench_bf16_gemm
experience_type: repair
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
captured_at: '2026-05-02'
confidence: inferred
reproducibility: concept
techniques:
- fine-grained-quantization
impl_family: cublas
---

cuBLAS row-major GEMM transpose logic error: wrong transa/transb and m/n/k mapping for C = A @ B.T

### Symptoms

- `Compiles successfully but results are numerically wrong`
- `max_relative_error > 90 (completely wrong matrix)`
- `transa/transb set incorrectly for row-major data`

## Challenge

SOL-ExecBench GEMM defines C = A @ B.T, A=[M,K] row-major, B=[N,K] row-major. LLM confuses row-major to column-major mapping when calling cublasGemmEx, producing INCORRECT_NUMERICAL results (max_error=99.4).


## Solution

Use the UNIVERSAL swap mapping for cublasGemmEx (verified 34/34 benchmarks for both INT8 and BF16):

transa=CUBLAS_OP_T, transb=CUBLAS_OP_N
m=N, n=M, k=K
A_ptr=B (swap!), lda=K
B_ptr=A (swap!), ldb=K
C_ptr=C, ldc=N

Why: A_rm[M,K]=A_cm[K,M], B_rm[N,K]=B_cm[K,N], C_rm[M,N]=C_cm[N,M]
Need: C_cm = B_cm^T @ A_cm
So: op(A_arg)=B_cm^T (transa=T on B), op(B_arg)=A_cm (transb=N on A)
Result: [N,K]@[K,M] = [N,M] = C_cm correct

## Key Lessons

- UNIVERSAL rule for row-major C=A@B.T: swap A/B pointers, swap m/n. transa=OP_T, transb=OP_N.
- Never use transa=T, transb=T (double transpose) — it's incorrect for this problem.
- Never use non-swap mapping (m=M, n=N) — it produces completely wrong results.
- The swap mapping works identically for both INT8 and BF16 — only data/compute types differ.
- See exp_o_20260508_120001 for the authoritative reference with full code examples.
