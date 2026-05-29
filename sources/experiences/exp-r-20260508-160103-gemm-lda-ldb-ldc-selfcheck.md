---
id: exp-r-20260508-160103-gemm-lda-ldb-ldc-selfcheck
title: Wrong lda/ldb/ldc or m/n/k assignment leads to incorrect output despite successf
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
impl_family: cublas
---

## Challenge

Wrong lda/ldb/ldc or m/n/k assignment leads to incorrect output despite successful compilation.

## Key Lessons

- For this benchmark, parameter mapping should be treated as immutable template code.
- If correctness fails first, inspect lda/ldb/ldc and m/n/k before changing kernels.
