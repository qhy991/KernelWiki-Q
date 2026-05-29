---
id: exp-r-20260508-180001-cublas-lda-ldb-correctness
title: cuBLAS GEMM correctness fails silently when lda/ldb use row-major leading dimens
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
reproducibility: concept
techniques:
- fine-grained-quantization
impl_family: cublas
---

## Challenge

cuBLAS GEMM correctness fails silently when lda/ldb use row-major leading dimensions (M, N) instead of column-major leading dimensions (K). No compilation error — the result is simply wrong.

## Key Lessons

- lda, ldb, ldc in cuBLAS are column-major leading dimensions, NOT row-major.
- For row-major A:[M,K], the column-major view is A_cm:[K,M], so lda=K.
- For row-major B:[N,K], the column-major view is B_cm:[K,N], so ldb=K.
- For row-major C:[M,N], the column-major view is C_cm:[N,M], so ldc=N.
- Wrong lda/ldb causes silent correctness failure — no compile error.
