---
id: exp-r-20260506-180007-cuda-syntax-in-cpp
title: CUDA syntax (__global__, <<<>>>) used in .cpp files compiled by g++/clang++
experience_type: repair
source_category: agent-experiment
architectures:
- sm90
tags:
- attention
kernel_types:
- attention
languages:
- cuda-cpp
captured_at: '2026-05-06'
confidence: inferred
reproducibility: concept
---

CUDA syntax (__global__, <<<>>>) used in .cpp files compiled by g++/clang++

## Key Lessons

- CUDA keywords (__global__, __device__, __shared__, blockIdx, threadIdx, <<<>>>) only work in .cu files compiled by nvcc
- .cpp files are compiled by g++/clang++ which does not understand CUDA syntax
- Keep CUDA kernels in .cu files and host code in .cpp files
- Use header files to bridge between .cu and .cpp files
- Kernel launch wrappers can be defined in .cu files and called from .cpp code
