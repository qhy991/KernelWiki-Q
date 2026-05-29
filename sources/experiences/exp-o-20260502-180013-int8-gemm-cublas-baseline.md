---
id: exp-o-20260502-180013-int8-gemm-cublas-baseline
title: 'SOL-ExecBench INT8 GEMM: cuBLAS baseline strategy'
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
captured_at: '2026-05-02'
confidence: inferred
reproducibility: concept
techniques:
- fine-grained-quantization
impl_family: cublas
---

For SOL-ExecBench INT8 GEMM (PI-int8) tasks, start with cuBLAS cublasGemmEx as the primary implementation; CUTLASS INT8 has high template instantiation failure rate and should only be attempted after a working cuBLAS baseline is established.

## Challenge

SOL-ExecBench PI-int8 GEMM tasks (C = A @ B.T with int8 inputs, int32 output) show a systematic pattern of failed CUTLASS INT8 implementations. CUTLASS INT8 template instantiation fails with incomplete type errors (mma_tensor_op_policy.h), while cuBLAS cublasGemmEx compiles reliably. Multiple experiments across different INT8 GEMM shapes (m10_n1024_k2048, m50_n2560_k1024, m768_n4304_k1152) all failed verification with CUTLASS-first strategies. A working baseline is needed before attempting more advanced optimizations.

## Solution

Adopt a cuBLAS-first strategy for INT8 GEMM: use cublasGemmEx with CUDA_R_8I inputs, CUDA_R_32I compute type, and CUBLAS_GEMM_DEFAULT_TENSOR_OP for Tensor Core utilization. Only consider CUTLASS or custom kernels after establishing a correct cuBLAS baseline.

Implementation pattern for SOL-ExecBench PI-int8 GEMM:
1. Use cublasGemmEx with handle reuse (create once, use across calls)
2. Row-major to column-major mapping via equivalence: C_row^T = B_row * A_row^T
3. cuBLAS params: m=N, n=M, k=K, both CUBLAS_OP_N, lda=K, ldb=K, ldc=N
4. Input types: CUDA_R_8I, output type: CUDA_R_32I, compute: CUDA_R_32I
5. Algorithm: CUBLAS_GEMM_DEFAULT_TENSOR_OP
6. DPS=true mode: void run(A, B, C) with C pre-allocated
7. For small M (M<=16): reference pads M to 17 for torch._int_mm, kernel should handle M=10 directly

## Key Lessons

- For INT8 GEMM on SOL-ExecBench, cuBLAS cublasGemmEx is the recommended first implementation. CUTLASS INT8 should only be attempted after a working cuBLAS baseline exists.
- INT8 GEMM problem definition: C[M,N] = A[M,K]_int8 @ B[N,K]_int8^T → C[M,N]_int32. Reference uses torch._int_mm(A, B.T). The B.T is critical — LLMs often miss this transpose.
- cuBLAS INT8 parameter mapping: treat as C_col[N,M] = B_col[N,K] * A_col[K,M], so m=N, n=M, k=K, a=B, b=A, both OP_N, lda=K, ldb=K, ldc=N.
- INT8 GEMM requires int32 accumulation (CUDA_R_32I as computeType). Never use CUDA_R_8I for compute — it will overflow.
- For small batch sizes (M=10), cuBLAS Tensor Core overhead may dominate. Consider checking if the speedup is positive before committing to this approach.
- Handle reuse is critical for small GEMM: cublasCreate once per session, not per call. Per-call handle create/destroy can make small GEMM 60x slower (see exp_r_20260502_180006_cublaslt_handle_overhead).
