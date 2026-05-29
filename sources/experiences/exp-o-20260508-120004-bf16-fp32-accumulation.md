---
id: exp-o-20260508-120004-bf16-fp32-accumulation
title: Which compute type should be used for BF16 GEMM — CUDA_R_16BF or CUDA_R_32F?
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
captured_at: '2026-05-08'
confidence: inferred
reproducibility: concept
impl_family: cublas
---

## Challenge

Which compute type should be used for BF16 GEMM — CUDA_R_16BF or CUDA_R_32F?

## Key Lessons

- BF16 data type (CUDA_R_16BF) with FP32 compute type (CUDA_R_32F) is the winning combination.
- alpha/beta must be float (1.0f/0.0f), not __nv_bfloat16.
- CUBLAS_GEMM_DEFAULT_TENSOR_OP enables Tensor Core for BF16.
