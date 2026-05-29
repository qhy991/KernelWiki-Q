---
id: exp-r-20260529-0003-update-sources-format-loop
title: Agent wastes 40+ steps calling sol_execbench_update_sources with wrong sources
  format
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
captured_at: '2026-05-29'
confidence: experimental
reproducibility: concept
---

## Key Lessons

- sol_execbench_update_sources(sources=...) expects flat dict {path: content}, NOT array [{path, content}]
- solution.json stores sources as array, but the tool parameter uses dict — these are different formats
- If sol_execbench_update_sources fails with format error more than 3 times, read the tool's expected_call hint in the error response
- Never pass problem=, solution=, path=, or content= as separate parameters — only sources={...} as a single dict
- After 3 failed format attempts, switch to sandbox_execute with a Python json.dump script to write solution.json directly
