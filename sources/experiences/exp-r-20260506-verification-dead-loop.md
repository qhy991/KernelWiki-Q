---
id: exp-r-20260506-verification-dead-loop
title: 'Verification pipeline dead loop: repeated identical blocked state until step
  exhaustion'
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
captured_at: '2026-05-06'
confidence: inferred
reproducibility: snippet
---

Experiments FA_10, FA_18, FA_01 encountered verification dead loops where the same blocked state repeated 3+ times until step budget was exhausted without any progress

### Symptoms

- `Verification step shows same blocked status 3+ consecutive times`
- `Step budget exhausted with only 1 attempt generated`
- `Session status: completed_with_gaps`
- `experience_pipeline: all zeros (captured=0, triaged=0, published=0)`

## Solution

Implement detection and recovery for verification dead loops

### Implementation

```cuda
1. Track consecutive identical verification states in the pipeline
2. After 2 consecutive identical blocked states, force a strategy change:
   a. Switch from verification to code modification
   b. Use a different compilation approach
   c. Fall back to a simpler kernel implementation
3. Ensure the experience pipeline captures the failure pattern for future avoidance
4. When step budget is low (< 3 remaining), prioritize recording findings over re-verification
5. Log the exact error that causes blocking so RAG can recall it for future tasks
```

## Key Lessons

- If verification returns the same error 2+ times, the current code cannot pass verification. Must modify the kernel code before re-attempting.
- Dead loops waste step budget. After 2 identical failures, immediately switch strategy: modify code, try different approach, or record findings and move on.
- The experience pipeline must capture these dead loop patterns so RAG can warn future runs. Currently pipeline captures 0 experiences from failed tasks.
- Single-attempt experiments (like FA_10, FA_18, FA_01) are a strong signal of dead loop: the agent got stuck on the first attempt and never recovered.
- When kernel compilation fails, the error message from nvcc is critical for diagnosis. Ensure it's captured in the experience, not lost in truncation.
