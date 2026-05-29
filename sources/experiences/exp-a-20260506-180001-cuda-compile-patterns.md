---
id: exp-a-20260506-180001-cuda-compile-patterns
title: CUDA compile error patterns from SOL-ExecBench experiments and their resolution
experience_type: analysis
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

## Challenge

What CUDA compile errors recur and how should they be resolved systematically?

## Key Lessons

- C++ PyTorch API uses positional args only: sum(-1, true) not sum(dim=-1, keepdim=True)
- PYBIND11_MODULE must be in .cpp file (compiled by g++), never in .cu file (compiled by nvcc)
- DPS=true requires void run(*inputs, *outputs); DPS=false requires result = run(*inputs)
- Use tensor.data_ptr<float>() to convert torch::Tensor to float* for raw CUDA kernels
- Keep __global__ and <<<>>> syntax only in .cu files; bridge to .cpp via wrapper functions
- The compile smoke output explicitly tells you which check failed - read it carefully before attempting fixes
