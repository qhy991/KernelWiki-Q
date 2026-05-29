---
id: exp-r-20260507-skill-suite-mismatch-blocked
title: 'Skill suite mismatch blocks R2: sol_execbench skill used on kerneleval task'
experience_type: repair
source_category: agent-experiment
architectures:
- sm90
tags:
- attention
- flash-attention
kernel_types:
- attention
- flash-attention
languages:
- cuda-cpp
captured_at: '2026-05-07'
confidence: experimental
reproducibility: snippet
---

R2 tasks across the batch hit a skill/suite mismatch blocker: the action policy loaded a skill guide for sol_execbench when the task is kerneleval. This causes 'Skill is declared for suites ['sol_execbench'], but current task is bound to suite `kerneleval`' error and triggers locked_round dead loop.

### Symptoms

- `last_step_error contains 'Skill is declared for suites ['sol_execbench'], but current task is bound to suite `kerneleval`'`
- `last_root_cause: 'Repeated blocked state triggered automatic policy lock'`
- `R2 never progresses past the skill mismatch blocker`
- `The session_memory contains 'Loaded skill guide for kerneleval-baseline-loop' but the action policy uses sol-execbench-solution-loop`
- `This creates a contradiction in the skill layer`

## Solution

The skill loaded in session memory (kerneleval-baseline-loop) must match the skill used by the action policy. When R2 starts, if the action policy loads a sol_execbench skill instead of kerneleval skill, the task cannot proceed.

### Implementation

```cuda
1. R2 should use the same kerneleval skill as R1. 2. When transitioning R1->R2, the skill selection should be preserved or explicitly set to kerneleval-compatible skill. 3. Add a pre-flight check: if session_state.mode=autoresearch and backend=cuda and suite=kerneleval, ensure the active skill is kerneleval-compatible, not sol_execbench.
```

## Key Lessons

- The skill layer has a suite contract: sol_execbench skills cannot be used on kerneleval tasks
- R2 inherits session_memory from R1 which contains 'Loaded skill guide for kerneleval-baseline-loop', but the action policy in R2 loads 'sol-execbench-solution-loop'
- This mismatch causes the first action in R2 to be blocked immediately
- The 3x repeated blocked state triggers the automatic policy lock, which then causes the locked_round dead loop
- The root cause of the skill mismatch is in the action policy's skill selection logic for R2
- This affects ALL R2 tasks in the batch, not just FA_09 - it's a systemic autoresearch R1->R2 transition bug
