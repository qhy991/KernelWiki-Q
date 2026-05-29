---
id: exp-r-20260506-150003-gemm-cublaslt-api-misuse
title: 'SOL-ExecBench GEMM: cuBLASLt API misuse causing compilation failure'
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
impl_family: cublaslt
---

Using cuBLASLt API (cublasLtMatmul, cublasLtMatmulDesc_t) without proper includes or on incompatible CUDA versions causes undefined identifier errors. Prefer cublasGemmEx which is simpler and more portable.

## Challenge

Agent generates code using cuBLASLt API (cublasLtMatmul, cublasLtMatmulDesc_t, cublasLtSetStream) which requires specific headers and CUDA version support. Missing #include <cublasLt.h> or incompatible CUDA toolkit causes compilation failures.

### Symptoms

- `'cublasLtMatmulDesc_t' was not declared in this scope`
- `'cublasLtSetStream' is not a member of 'cublasLtMatmulDesc_t'`
- `undefined identifier errors for cuBLASLt types`
- `Compilation fails but code looks syntactically correct`

## Solution

Replace cuBLASLt API calls with cublasGemmEx which is simpler, more portable, and supports the same INT8/BF16 Tensor Core operations. cublasGemmEx only requires #include <cublas_v2.h>.

### Implementation

```cuda
1. Use cublasGemmEx instead of cublasLtMatmul:
   - Only needs #include <cublas_v2.h>
   - Same Tensor Core support via CUBLAS_GEMM_DEFAULT_TENSOR_OP
   - Simpler API: single function call, no descriptor setup
2. For INT8 C=A@B^T (row-major), use swap mapping:
   int32_t alpha = 1, beta = 0;
   cublasGemmEx(handle,
       CUBLAS_OP_T, CUBLAS_OP_N, N, M, K,
       &alpha,
       B, CUDA_R_8I, K, A, CUDA_R_8I, K,
       &beta, C, CUDA_R_32I, N,
       CUDA_R_32I, CUBLAS_GEMM_DEFAULT_TENSOR_OP);
3. For BF16 C=A@B^T (row-major), use SAME swap mapping:
   float alpha = 1.0f, beta = 0.0f;
   cublasGemmEx(handle,
       CUBLAS_OP_T, CUBLAS_OP_N, N, M, K,
       &alpha,
       B, CUDA_R_16BF, K, A, CUDA_R_16BF, K,
       &beta, C, CUDA_R_16BF, N,
       CUBLAS_COMPUTE_32F, CUBLAS_GEMM_DEFAULT_TENSOR_OP);
4. NOTE: Use CUDA_R_32I for INT8 compute, CUBLAS_COMPUTE_32F for BF16 compute.
   Do NOT use CUBLAS_COMPUTE_32I — it is a different enum type that causes compile errors.
5. If cuBLASLt is truly needed, add #include <cublasLt.h> and verify CUDA toolkit version
```

## Key Lessons

- Prefer cublasGemmEx over cuBLASLt API for GEMM tasks - simpler, more portable, same Tensor Core support.
- cuBLASLt requires #include <cublasLt.h> and specific CUDA toolkit version - avoid unless needed for advanced features.
- cublasGemmEx only needs #include <cublas_v2.h> - always available with CUDA toolkit.
- CUBLAS_GEMM_DEFAULT_TENSOR_OP enables Tensor Core usage in cublasGemmEx.
- If compilation fails with undefined cuBLASLt identifiers, switch to cublasGemmEx immediately.
- Do not spend multiple steps debugging cuBLASLt API issues - switch to cublasGemmEx and move on.
