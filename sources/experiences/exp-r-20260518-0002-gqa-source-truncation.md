---
id: exp-r-20260518-0002-gqa-source-truncation
title: 'GQA paged decode: source code truncation causes syntax errors after sol_execbench_update_sources'
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
captured_at: '2026-05-18'
confidence: inferred
reproducibility: concept
---

GQA paged decode: source code truncation causes syntax errors after sol_execbench_update_sources

## Key Lessons

- Always verify source content integrity after sol_execbench_update_sources — read back function signatures and kernel launch calls
- For kernels longer than ~150 lines, consider writing sources via sandbox_execute with a Python json.dump script instead of sol_execbench_update_sources
- Truncation manifests as: missing commas between parameters, cut-off variable names, missing closing brackets
- Compilation errors with 'expected a )' or undefined short identifiers (like 'threa') are strong signals of truncation — not logic errors
- If truncation is detected, don't iterate on the code logic — fix the file writing method first
