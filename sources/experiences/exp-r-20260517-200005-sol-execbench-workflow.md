---
id: exp-r-20260517-200005-sol-execbench-workflow
title: 'SOL-ExecBench workflow: solution.json is canonical, not loose files'
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
captured_at: '2026-05-17'
confidence: inferred
reproducibility: concept
impl_family: custom_cuda
---

SOL-ExecBench workflow: solution.json is canonical, not loose files

## Key Lessons

- SOL-ExecBench sources live in solution.json['sources'] as [{"path": "...", "content": "..."}, ...], not as loose files on disk.
- Always use sol_execbench_update_sources(sources={...}) to modify source code.
- Never write source files directly in the attempt directory — the framework ignores them.
- Before verification, ensure solution.json is up-to-date with all source changes.
- The first bootstrap step: create solution.json with all initial sources before running any verification.
- When spec.languages is cuda_cpp, sources typically include: main.cpp, kernel.cu, kernel.h (all as embedded content in solution.json).
