---
id: exp-r-20260513-100002-int8-gemm-cublas-lda-wrong
title: 'SOL-ExecBench INT8 GEMM: cuBLAS leading dimension mismatch for col-major B'
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
captured_at: '2026-05-13'
confidence: inferred
reproducibility: snippet
techniques:
- fine-grained-quantization
impl_family: cublas
---

When passing B[K,N] col-major to cuBLAS cublasGemmEx, the leading dimension (lda) for B must be N (the number of columns in column-major storage), NOT K. Using lda=K causes cuBLAS to read B with wrong stride, producing INCORRECT_NUMERICAL results.

## Challenge

Agent computes cuBLAS parameters for INT8 GEMM C=A@B (A:[M,K] row-major, B:[K,N] col-major) but sets lda=K for B matrix. For a column-major matrix [K,N], the leading dimension is N (stride between columns), not K.

### Symptoms

- `INCORRECT_NUMERICAL with moderate errors (1.0-100.0 relative error, not 1e8)`
- `cuBLAS call succeeds (no crash), but results are partially wrong`
- `Error is smaller than total layout confusion but still fails tolerance checks`

## Solution

For cuBLAS cublasGemmEx with A[M,K] row-major and B[K,N] col-major:
- Treat as C_col = B_col^T * A_col^T in cuBLAS column-major convention
- m=N, n=M, k=K
- A_param = B_ptr, lda=N (B is [K,N] col-major, leading dim = N)
- B_param = A_ptr, ldb=K (A is [M,K] row-major = [K,M] col-major^T, leading dim = K)
- C_param = C_ptr, ldc=N (output [M,N] row-major = [N,M] col-major, leading dim = N)
- opA=CUBLAS_OP_N, opB=CUBLAS_OP_N

### Implementation

```cuda
cublasGemmEx(handle,
    CUBLAS_OP_N, CUBLAS_OP_N,
    N, M, K,          // m=N, n=M, k=K
    &alpha,
    B, CUDA_R_8I, N,  // A_param=B, lda=N (B is [K,N] col-major)
    A, CUDA_R_8I, K,  // B_param=A, ldb=K (A is [M,K] row-major)
    &beta,
    C, CUDA_R_32I, N, // C, ldc=N
    CUBLAS_COMPUTE_32I, CUBLAS_GEMM_DEFAULT_TENSOR_OP);
```

## Key Lessons

- cuBLAS leading dimension for a column-major [rows, cols] matrix is rows (the stride between consecutive columns). For B[K,N] col-major: lda = N (NOT K). For A[M,K] row-major = [K,M] col-major^T: lda = K.
- The cuBLAS parameter mapping for C=A@B where A:[M,K] row-major, B:[K,N] col-major is: m=N, n=M, k=K, A_param=B(N), B_param=A(K), opA=OP_N, opB=OP_N, ldc=N.
- If cuBLAS produces wrong results without crashing, check leading dimensions first — wrong lda causes misaligned reads, not segfaults.
- Never assume lda = K just because K is the 'inner dimension'. lda is always the stride of the leading dimension of the matrix as stored in memory.
