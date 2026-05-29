---
id: exp-r-20260517-200006-sol-execbench-round-lock
title: SOL-ExecBench round lock and skill contract mismatch errors
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

- Round lock error = orchestrator has moved on. Call finish(success=false). Do NOT retry, inspect, or recover.
- Skill contract mismatch = the task uses a different verification mechanism. Don't load the skill; use the task's declared verification commands.
- Don't chase /tmp/sol_execbench_* directories — they are temporary build artifacts cleaned up after verification.
- If compilation fails, read compilation_failure_report.json in the attempt directory, not the /tmp build logs.
- After any code change, always call sol_execbench_update_sources before running verification.
- The task contract's verified commands are listed in the task metadata — use those, not commands from skill documentation.
