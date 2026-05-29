---
id: exp-o-20260506-150004-bf16-gemm-cublas-tensor-core
title: 'SOL-ExecBench BF16 GEMM: cuBLAS Tensor Core optimization for small batch'
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
captured_at: '2026-05-06'
confidence: inferred
reproducibility: concept
impl_family: cublaslt
---

BF16 GEMM with small batch (M=10~50) achieves 1.4x~2.2x speedup using cuBLAS cublasGemmEx with CUBLAS_GEMM_DEFAULT_TENSOR_OP and persistent handle.

## Challenge

SOL-ExecBench BF16 GEMM tasks with small batch size (M=10~50, N=1024~8192, K=1024~4096) face challenges: (1) Tensor Core overhead for small M, (2) cuBLAS handle creation overhead per call, (3) row-major to col-major layout confusion, (4) torch.mm wrapper only achieves ~1.17x.

### Symptoms

- `torch.mm(A, B.T, out=C) achieves only 1.17x for BF16 GEMM`
- `cuBLASLt handle created/destroyed per call causes slowdown`
- `Row-major to column-major transpose errors produce incorrect results`
- `CUTLASS BF16 template instantiation fails for small M`

## Solution

Use cuBLAS cublasGemmEx with persistent handle and CUBLAS_GEMM_DEFAULT_TENSOR_OP. Key: correct row-major to column-major transpose for C = A @ B^T.

Implementation for SOL-ExecBench PI-bf16 GEMM:
1. Handle: static or thread_local cublasHandle_t, created once
2. Stream: cublasSetStream(handle, at::cuda::getCurrentCUDAStream())
3. Row-major GEMM C[M,N] = A[M,K] @ B[N,K]^T:
   - cuBLAS col-major: m=N, n=M, k=K
   - op(A_cublas)=T on B data (lda=K), op(B_cublas)=N on A data (ldb=K)
   - ldc=N for output
4. Types: CUDA_R_16BF input, CUDA_R_32F compute
5. Algorithm: CUBLAS_GEMM_DEFAULT_TENSOR_OP
6. Performance by problem shape:
   - m10_n8192_k1024: 2.20x (0.025ms vs 0.054ms ref)
   - m50_n1024_k4096: 1.73x
   - m50_n1024_k2048: 2.01x (0.033ms vs 0.067ms ref)
   - m10_n1024_k2048: 1.37x

## Key Lessons

- BF16 GEMM with cuBLAS cublasGemmEx + CUBLAS_GEMM_DEFAULT_TENSOR_OP achieves 1.4x~2.2x for small batch sizes.
- Larger N (e.g., N=8192) yields higher speedup because Tensor Core utilization improves.
- torch.mm wrapper is insufficient for optimization tasks - only achieves ~1.17x because it IS the reference baseline.
- Persistent cuBLAS handle is critical - per-call cublasCreate/cublasDestroy adds ~0.5-1ms overhead.
- Row-major to column-major mapping: for C=A@B^T, cuBLAS parameters are m=N, n=M, k=K, A=B_ptr, lda=K, B=A_ptr, ldb=K, ldc=N.
- BF16 accumulation uses CUDA_R_32F compute type - FP32 accumulation for BF16 inputs.
- Use at::cuda::getCurrentCUDAStream() for stream, NOT c10::cuda::getCurrentCUDAStream().
