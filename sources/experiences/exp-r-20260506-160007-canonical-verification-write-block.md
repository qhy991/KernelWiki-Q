---
id: exp-r-20260506-160007-canonical-verification-write-block
title: 'SOL-ExecBench: canonical verification requires attempt_dir binding'
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

SOL-ExecBench verification cannot proceed without an active attempt_dir binding. The agent must bind the assignment and attempt_dir before running or recording verification.

## Challenge

Agent tries to run verification or record benchmark artifacts, but gets: 'Canonical verification requires an active attempt_dir. Bind the current assignment before running or recording verification.' This is the most common error in SOL-ExecBench tasks.

### Symptoms

- `Canonical verification requires an active attempt_dir`
- `Bind the current assignment before running or recording verification`
- `Agent retries verification repeatedly without fixing the binding issue`

## Solution

Before running verification, ensure the assignment is bound and attempt_dir is set. Use get_task or the task binding mechanism to establish the attempt context.

### Implementation

```cuda
1. Call get_task() to bind the current assignment if not already bound
2. Ensure attempt_dir is set in the task binding
3. The attempt_dir must exist and contain the source files
4. Only after binding is established, run the verification command
5. If binding fails, check that the task_id is correct
6. Do NOT retry verification without fixing the binding first
```

## Key Lessons

- SOL-ExecBench verification requires an active attempt_dir binding.
- The binding is established by get_task() or the task binding mechanism.
- attempt_dir must exist and contain the source files before verification.
- Retrying verification without fixing binding wastes step budget.
- This is the #1 most common error in SOL-ExecBench experiments.
