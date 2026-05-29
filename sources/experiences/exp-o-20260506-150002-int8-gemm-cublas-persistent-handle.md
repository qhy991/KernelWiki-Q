---
id: exp-o-20260506-150002-int8-gemm-cublas-persistent-handle
title: 'SOL-ExecBench INT8 GEMM: cuBLAS with persistent handle'
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
captured_at: '2026-05-06'
confidence: inferred
reproducibility: concept
techniques:
- fine-grained-quantization
impl_family: cublas
---

For SOL-ExecBench INT8 GEMM (M=10, N=1024, K=4096), cuBLAS cublasGemmEx with persistent handle achieves 3.83x speedup by eliminating per-call handle creation overhead.

## Challenge

cuBLAS handle creation/destruction per kernel call causes significant overhead for small GEMM. The overhead (cublasCreate/cublasDestroy) can dominate execution time, reducing speedup to 0.017x (60x slower than baseline).

### Symptoms

- `cuBLAS GEMM with per-call handle: 0.017x speedup (60x slower)`
- `High latency variance between runs`
- `cublasCreate/cublasDestroy in profiler shows significant time`

## Solution

Create cuBLAS handle once per session and reuse across all GEMM calls. Use cublasGemmEx with CUDA_R_8I inputs, CUDA_R_32I compute type, and CUBLAS_GEMM_DEFAULT_TENSOR_OP algorithm.

Implementation pattern for SOL-ExecBench PI-int8 GEMM:
1. Create cublasHandle_t once at initialization
2. Reuse handle for all GEMM calls in the session
3. cublasGemmEx parameters:
   - transa=CUBLAS_OP_N, transb=CUBLAS_OP_N
   - m=N, n=M, k=K (row-major to col-major mapping)
   - alpha=1.0f, beta=0.0f
   - Atype=CUDA_R_8I, Btype=CUDA_R_8I
   - Ctype=CUDA_R_32I, computeType=CUDA_R_32I
   - algo=CUBLAS_GEMM_DEFAULT_TENSOR_OP
4. Row-major C[M,N] = A[M,K] @ B[N,K]^T maps to:
   - col-major: C_col[N,M] = B_col[N,K] * A_col[K,M]
   - so m=N, n=M, k=K, a_ptr=B, b_ptr=A, c_ptr=C
5. Performance: 3.83x speedup, latency 0.022ms vs reference 0.084ms

## Key Lessons

- cuBLAS handle creation overhead is critical for small GEMM: create once, reuse across calls.
- cuBLAS cublasGemmEx with CUDA_R_8I and CUBLAS_GEMM_DEFAULT_TENSOR_OP achieves near-peak Tensor Core utilization.
- Row-major to col-major mapping: for C[M,N] = A[M,K] @ B[N,K]^T, use m=N, n=M, k=K, a=B, b=A.
- INT8 GEMM requires CUDA_R_32I as computeType for accumulation - never use CUDA_R_8I.
- For M=10, cuBLAS achieves 3.83x speedup with proper handle reuse and Tensor Core utilization.
- Handle creation overhead can make small GEMM 60x slower - always profile handle overhead.
