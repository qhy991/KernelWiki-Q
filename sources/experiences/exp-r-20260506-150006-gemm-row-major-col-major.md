---
id: exp-r-20260506-150006-gemm-row-major-col-major
title: 'SOL-ExecBench GEMM: row-major to column-major transpose pattern'
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

SOL-ExecBench GEMM uses row-major storage (C = A[M,K] @ B[N,K]^T) but cuBLAS expects column-major. Incorrect transpose mapping produces wrong results or crashes.

## Challenge

cuBLAS uses column-major (Fortran) ordering while SOL-ExecBench uses row-major (C) ordering. Incorrect mapping between the two leads to: (1) wrong output values, (2) segfaults from out-of-bounds access, (3) correct-looking but transposed output.

### Symptoms

- `Correctness check fails with large max_relative_error`
- `Output matrix appears transposed or shuffled`
- `Segfault during GEMM execution`
- `Speedup << 1.0 (slower than reference)`

## Solution

For SOL-ExecBench GEMM: C[M,N] = A[M,K]_row @ B[N,K]_row^T, use this cuBLAS mapping:

### Implementation

```cuda
cuBLAS col-major convention for C=A@B^T:

1. A_row[M,K] in memory = A_col[K,M] with lda=K
   B_row[N,K] in memory = B_col[K,N] with ldb=K  
   C_row[M,N] in memory = C_col[N,M] with ldc=N

2. Want: C_col = B_col^T @ A_col
   cublasGemmEx(handle,
       CUBLAS_OP_T,    // transa: transpose B_col
       CUBLAS_OP_N,    // transb: no transpose on A_col
       N,              // m = rows of op(A) = N
       M,              // n = cols of op(B) = M
       K,              // k = inner dim
       &alpha,
       B,              // A pointer = B data
       K,              // lda = K
       A,              // B pointer = A data
       K,              // ldb = K
       &beta,
       C,              // C pointer
       N,              // ldc = N
       ...);

3. Key mnemonic: swap A and B pointers, swap m and n dimensions.
```

## Key Lessons

- cuBLAS col-major: for C=A@B^T (row-major), swap A/B pointers and set m=N, n=M, k=K.
- lda=K (stride of input rows), ldb=K, ldc=N (stride of output rows).
- CUBLAS_OP_T on B data, CUBLAS_OP_N on A data - transa operates on the FIRST argument (B).
- Common mistake: keeping m=M, n=N - this produces transposed output.
- Always verify with a small test case (e.g., 2x3 @ 3x2) before running full benchmark.
- If correctness fails with large error, check transpose mapping first.
