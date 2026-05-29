---
id: exp-r-20260506-160005-entry-point-mismatch
title: 'SOL-ExecBench: entry_point mismatch with actual code'
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
---

SOL-ExecBench static gate checks that spec.entry_point matches the actual function defined in the source code. Mismatches cause static_gate_error.

## Challenge

SOL-ExecBench definition.json specifies an entry_point (e.g., 'main.cpp::run'), but the actual source code doesn't define that function, or defines it with a different signature. This triggers: 'spec.entry_point points to main.cpp::run, but main.cpp does not define run(...)'

### Symptoms

- `static_gate_error: spec.entry_point points to main.cpp::run, but main.cpp does not define run(...)`
- `entry_point_error: spec.entry_point must have format filename::function_name`
- `Verification cannot proceed because the entry point is invalid`

## Solution

Ensure the source code defines the exact function specified in spec.entry_point. Check both the filename and function name, and ensure the signature matches the DPS convention.

### Implementation

```cuda
1. Read definition.json to find spec.entry_point (e.g., 'main.cpp::run')
2. Check that the specified file exists and contains the function
3. For DPS=true: function must be void run(*inputs, *outputs)
4. For DPS=false: function must return the output tensor
5. The function name must match exactly (case-sensitive)
6. If using sol_execbench_update_sources, ensure the entry point file is included
7. After fixing, re-run verification
```

## Key Lessons

- spec.entry_point format is 'filename::function_name' - both must match exactly.
- The function signature must match the DPS convention (void for DPS=true).
- If the entry point file is not included in sol_execbench_update_sources, the function won't exist.
- Always check definition.json for the expected entry point before writing code.
- Case sensitivity matters - 'run' and 'Run' are different functions.
