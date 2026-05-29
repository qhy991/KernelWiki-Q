---
id: exp-i-20260517-200012-sol-execbench-cpp-template
title: SOL-ExecBench cuda_cpp solution.json and source file template
experience_type: implementation
source_category: agent-experiment
architectures:
- sm90
tags:
- gemm
kernel_types:
- gemm
languages:
- cuda-cpp
captured_at: '2026-05-17'
confidence: inferred
reproducibility: concept
impl_family: custom_cuda
---

SOL-ExecBench cuda_cpp solution.json and source file template

## Solution

Follow the canonical three-file pattern for SOL-ExecBench CUDA C++ tasks. solution.json must have spec.languages=cuda_cpp, spec.destination_passing_style matching definition.json, and sources array with all three files. Never create stray files outside solution.json.

## Key Lessons

- solution.json is the canonical state. Loose files in the attempt directory are mirrors and will be ignored by the framework.
- spec.languages for CUDA C++ is "cuda_cpp" — exactly this string, not "cuda" or "cuda_c++".
- Every source file referenced in solution.json["sources"] must exist as an object with "path" and "content" keys.
- The content in solution.json is what's compiled — editing the loose file on disk has no effect.
- main.cpp's run() signature must match definition.json's inputs/outputs order. Use void for destination_passing_style=true.
- Add TORCH_CUDA_ARCH_LIST environment variable to avoid the 'all archs for visible cards' warning and speed up compilation.
- For the first bootstrap: create solution.json, then call sol_execbench_update_sources to sync, then verify.
- PYBIND11_MODULE must use TORCH_EXTENSION_NAME macro (not a string literal) and must be in main.cpp (not kernel.cu).
