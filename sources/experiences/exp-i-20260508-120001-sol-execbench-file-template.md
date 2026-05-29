---
id: exp-i-20260508-120001-sol-execbench-file-template
title: How to structure CUDA C++ solution files for SOL-ExecBench GEMM problems to
  avoi
experience_type: implementation
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

How to structure CUDA C++ solution files for SOL-ExecBench GEMM problems to avoid compilation errors?

## Key Lessons

- Three-file split is mandatory: kernel.h (interface), kernel.cu (CUDA impl), main.cpp (PyTorch binding).
- ATen headers only in main.cpp. CUDA library headers only in kernel.cu.
- DPS void signature: void run(Tensor, Tensor, Tensor) — must not return Tensor.
- Always set destination_passing_style: true in solution.json spec.
