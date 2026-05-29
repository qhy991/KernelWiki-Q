---
id: exp-r-20260526-200001-cublaslt-compute-type-precision
title: 'SOL-ExecBench GEMM: cublasLt COMPUTE_TYPE precision mismatch causing correctness
  failure'
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

Using CUBLAS_COMPUTE_16F with cublasLtMatmul causes FP16 intermediate accumulation, producing max_relative_error=55+ on large matrices. Must use CUBLAS_COMPUTE_32F for FP32 accumulation to maintain correctness.

### Symptoms

- `max_relative_error >> 1 (values like 55, 37666)`
- `Kernel compiles and launches successfully`
- `Small matrices (N<128) may pass correctness checks while large matrices fail`
- `cublasLtMatmulDescSetAttribute with CUBLASLT_MATMUL_DESC_COMPUTE_TYPE set to CUBLAS_COMPUTE_16F`

## Challenge

cublasLtMatmul with CUBLAS_COMPUTE_16F performs FP16 intermediate accumulation. For large GEMM matrices (N>=1024), floating-point rounding errors accumulate over K additions, producing max_relative_error=55+ when the benchmark expects error<1e-3. The kernel compiles and runs without errors, but outputs are numerically incorrect.


## Solution

Set compute type to CUBLAS_COMPUTE_32F (FP32 accumulation) regardless of input/output precision. For FP16 GEMM:

cublasLtMatmulDescCreate(&matmulDesc, CUBLAS_COMPUTE_32F, CUDA_R_32F);

Alternatively with cublasGemmEx:
cublasGemmEx(handle, ..., CUDA_R_16F, CUDA_R_16F, CUDA_R_16F, CUBLAS_COMPUTE_32F, CUBLAS_GEMM_DEFAULT_TENSOR_OP);

The compute_type parameter controls INTERMEDIATE accumulation precision, NOT input/output type. FP32 accumulation with FP16 I/O still uses Tensor Cores (via CUBLAS_GEMM_DEFAULT_TENSOR_OP).

## Key Lessons

- CUBLAS_COMPUTE_16F means FP16 INTERMEDIATE accumulation — it does NOT mean 'use FP16 inputs'. FP16 accumulation causes catastrophic precision loss for K>=256.
- CUBLAS_COMPUTE_32F with FP16 I/O still uses Tensor Cores on Ampere+ GPUs. There is NO performance penalty for choosing FP32 accumulation.
- If max_relative_error is large (>1) but the kernel otherwise works, check the compute_type first — it's the most common cause of correctness failures in cublasLt GEMM.
- cublasGemmEx with CUBLAS_GEMM_DEFAULT_TENSOR_OP automatically selects the fastest math mode including TF32 and FP16 Tensor Core paths with FP32 accumulation.
