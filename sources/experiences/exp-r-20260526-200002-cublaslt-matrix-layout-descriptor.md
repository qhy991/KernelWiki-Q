---
id: exp-r-20260526-200002-cublaslt-matrix-layout-descriptor
title: 'SOL-ExecBench GEMM: cublasLt matrix layout descriptor leading dimension error'
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
captured_at: '2026-05-26'
confidence: inferred
reproducibility: concept
impl_family: cublaslt
---

cublasLtMatrixLayoutCreate with incorrect leading dimension (ld) causes massive correctness errors (max_error=37666). For row-major tensors, ld must equal the number of columns, not rows.

### Symptoms

- `max_relative_error=37666 or similar extremely large values`
- `Kernel compiles and runs without CUDA errors`
- `Results are completely wrong, not just slightly off`
- `cublasLtMatrixLayoutCreate used with ld=rows instead of ld=cols for row-major data`

## Solution

For SOL-ExecBench row-major tensors with C[M,N] = A[M,K] @ B.T[K,N] (B stored as [N,K]):

Option 1 — Use CUBLASLT_ORDER_ROW with correct ld:
  cublasLtMatrixLayoutCreate(&layoutA, type, M, K, K);  // ld=K (cols of A)
  cublasLtMatrixLayoutCreate(&layoutB, type, K, N, N);  // ld=N (cols of B.T)
  cublasLtMatrixLayoutCreate(&layoutC, type, M, N, N);  // ld=N (cols of C)
  cublasLtMatrixLayoutSetAttribute(..., CUBLASLT_MATRIX_LAYOUT_ORDER, &rowOrder, ...);

Option 2 (RECOMMENDED) — Avoid cublasLt entirely, use cublasGemmEx with the universal swap mapping:
  transa=CUBLAS_OP_T, transb=CUBLAS_OP_N
  m=N, n=M, k=K
  A_ptr=B (swap!), lda=K
  B_ptr=A (swap!), ldb=K
  C_ptr=C, ldc=N

The swap mapping is verified across 34/34 SOL-ExecBench GEMM benchmarks.

## Key Lessons

- cublasLtMatrixLayoutCreate(layout, type, rows, cols, ld): the 'ld' parameter is the leading dimension — for row-major it equals the number of COLUMNS, for col-major it equals the number of ROWS.
- cuBLAS/cublasLt assumes column-major by default. For row-major data, either set CUBLASLT_MATRIX_LAYOUT_ORDER to CUBLASLT_ORDER_ROW, or use the pointer-swap trick with cublasGemmEx.
- If max_relative_error is in the thousands/millions (not just >1), the issue is almost certainly wrong memory layout/stride, not precision.
- The simplest correct approach for SOL-ExecBench row-major GEMM is cublasGemmEx with the swap mapping (see exp_r_20260502_180005_cublaslt_transpose_logic). cublasLt adds complexity with no performance benefit for standard shapes.
