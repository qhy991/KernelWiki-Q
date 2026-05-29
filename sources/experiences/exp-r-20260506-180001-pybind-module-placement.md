---
id: exp-r-20260506-180001-pybind-module-placement
title: PYBIND11_MODULE must be in .cpp file compiled by g++/clang++, not in .cu file
  compiled by nvcc
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

## Key Lessons

- PYBIND11_MODULE must always be in a .cpp file, never in a .cu file
- The host compiler (g++/clang++) handles pybind11; nvcc handles CUDA device code
- Separate CUDA kernels (.cu) from Python bindings (.cpp) into different source files
- SOL-ExecBench compile smoke explicitly checks: if PYBIND11_MODULE is only in .cu sources, it fails with a clear error message
- The .cpp wrapper should include <torch/extension.h> and define the Python-callable interface
