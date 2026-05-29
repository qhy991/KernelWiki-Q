---
id: exp-r-20260517-200016-compilation-debug-workflow
title: SOL-ExecBench compilation failure debugging workflow
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

## Key Lessons

- After ninja build failure, FIRST action: read compilation_failure_report.json in attempt_dir.
- If compilation_failure_report.json is missing: use grep_files(pattern='error:', path='<task_dir>') to find actual errors.
- NEVER read /tmp/sol_execbench_* — these directories are ephemeral and cleaned up.
- NEVER read tool_results/*_read_text_file_content.txt for build logs — PinCache truncation cuts off the interesting parts.
- TORCH_CUDA_ARCH_LIST warning is NOT an error — it just means all detected archs are included.
- Fix the actual source code compile error, then call sol_execbench_update_sources, then re-run sandbox_execute.
- Do NOT change nvcc flags, ninja build files, or build configuration — the framework handles these.
- If the same error persists after a fix, the fix didn't take effect — verify sol_execbench_update_sources was called.
