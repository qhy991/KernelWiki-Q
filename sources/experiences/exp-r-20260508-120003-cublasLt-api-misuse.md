---
id: exp-r-20260508-120003-cublasLt-api-misuse
title: exp-r-20260508-120003-cublasLt-api-misuse
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
captured_at: '2026-05-08'
confidence: inferred
reproducibility: snippet
techniques:
- fine-grained-quantization
impl_family: cublaslt
---

## Challenge

Calling cublasLtMatmulSearch() results in 'identifier is undefined' errors. cuBLASLt API requires complex descriptor setup and is error-prone.

## Key Lessons

- Never use cublasLt for SOL-ExecBench GEMM — use cublasGemmEx instead.
- cublasGemmEx with CUBLAS_GEMM_DEFAULT_TENSOR_OP automatically uses Tensor Cores.
