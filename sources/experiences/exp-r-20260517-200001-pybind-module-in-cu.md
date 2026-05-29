---
id: exp-r-20260517-200001-pybind-module-in-cu
title: PYBIND11_MODULE placed in .cu file instead of .cpp wrapper
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
captured_at: '2026-05-17'
confidence: inferred
reproducibility: concept
techniques:
- fine-grained-quantization
impl_family: custom_cuda
---

PYBIND11_MODULE placed in .cu file instead of .cpp wrapper

## Key Lessons

- PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) must be in a .cpp file, never in a .cu file.
- main.cpp structure: #include <torch/extension.h>, #include "kernel.h", void run(...) that calls kernel launch, PYBIND11_MODULE at the end.
- kernel.cu structure: #include "kernel.h", kernel implementations with __global__ and __device__, a host function that casts tensors and launches kernels.
- kernel.h structure: #pragma once, #include <cuda_runtime.h>, declarations of host functions called from main.cpp.
- Always use TORCH_EXTENSION_NAME macro literally, not a quoted string like "benchmark_kernel".
- The run() function signature must match the benchmark definition: void run(Type1 in1, Type2 in2, ..., TypeN out) with output tensors at the end for destination_passing_style=true.
