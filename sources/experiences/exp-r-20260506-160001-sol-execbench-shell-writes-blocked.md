---
id: exp-r-20260506-160001-sol-execbench-shell-writes-blocked
title: 'SOL-ExecBench: direct shell writes to solution.json blocked'
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
captured_at: '2026-05-06'
confidence: inferred
reproducibility: snippet
impl_family: custom_cuda
---

SOL-ExecBench blocks direct filesystem writes to solution.json and other manifest-backed sources. Agents must use sol_execbench_update_sources() API instead.

## Challenge

Agent tries to write solution.json directly via mcp_filesystem_write_file or sandbox_execute (echo/cat), but SOL-ExecBench's manifest protection blocks these writes with an error: 'Direct shell writes to SOL-ExecBench manifest-backed sources are blocked. solution.json is the source of truth; use sol_execbench_update_sources.'

### Symptoms

- `Direct shell writes to SOL-ExecBench manifest-backed sources are blocked`
- `solution.json is the source of truth; use sol_execbench_update_sources`
- `Agent repeatedly retries the same blocked write operation, wasting steps`

## Solution

Use the sol_execbench_update_sources() API to update solution.json and other manifest-backed source files. Never use mcp_filesystem_write_file, echo, cat, or other direct file write methods for these files.

### Implementation

```cuda
1. Identify the source files that need updating (solution.json, main.cpp, kernel.cu, etc.)
2. Prepare the full content for each file
3. Call sol_execbench_update_sources(sources={relative_path: full_content})
4. Do NOT use mcp_filesystem_write_file for SOL-ExecBench source files
5. Do NOT use sandbox_execute with echo/cat/cp to write to these files
6. The only exception is if the file is in the attempt_dir and not manifest-backed
```

## Key Lessons

- SOL-ExecBench manifest-backed sources can only be updated via sol_execbench_update_sources() API.
- Direct filesystem writes (mcp_filesystem_write_file, echo, cat) are blocked for solution.json and other declared sources.
- The error message explicitly tells you to use sol_execbench_update_sources - follow it immediately.
- Repeated retries of blocked writes waste step budget - switch to the correct API on the first error.
- Files in attempt_dir that are NOT in the manifest (e.g. test scripts) can still be written directly.
