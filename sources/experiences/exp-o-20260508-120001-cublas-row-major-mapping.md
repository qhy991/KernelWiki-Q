---
id: exp-o-20260508-120001-cublas-row-major-mapping
title: exp-o-20260508-120001-cublas-row-major-mapping
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
captured_at: '2026-05-08'
confidence: inferred
reproducibility: concept
techniques:
- fine-grained-quantization
impl_family: cublas
---

## Key Lessons

- UNIVERSAL rule: Always swap A and B pointers — B_ptr first, A_ptr second.
- UNIVERSAL rule: Always swap m and n — m=N, n=M.
- Leading dimensions: always lda=K, ldb=K, ldc=N regardless of dtype.
- BF16: float alpha/beta, CUBLAS_COMPUTE_32F, CUDA_R_16BF data, CUDA_R_16BF output.
- INT8: int32_t alpha/beta, CUDA_R_32I compute, CUDA_R_8I data, CUDA_R_32I output.
- Always use CUBLAS_GEMM_DEFAULT_TENSOR_OP for both dtypes.
