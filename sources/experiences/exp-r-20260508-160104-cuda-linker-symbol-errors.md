---
id: exp-r-20260508-160104-cuda-linker-symbol-errors
title: Build fails at link stage due to unresolved CUDA/cuBLAS/PyTorch symbols after
  so
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
captured_at: '2026-05-08'
confidence: inferred
reproducibility: snippet
impl_family: cublas,cutlass,torch
---

## Challenge

Build fails at link stage due to unresolved CUDA/cuBLAS/PyTorch symbols after source compiles successfully.

## Key Lessons

- Classify failures first: compile syntax/type errors vs linker symbol errors vs runtime verification.
- For linker errors, check symbol ownership and boundaries before tuning kernels.
