---
id: exp-r-20260507-verification-dead-loop-r2
title: Verification dead loop in R1 blocks unverified, then R2 inherits failure
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

FA_05, FA_13, FA_14 failed R1 with blocked_unverified (compilation succeeded but verification couldn't confirm correctness). R2 then inherited the failed state and also failed. These experiments show a compounding failure pattern.

### Symptoms

- `R1 verdict: blocked_unverified`
- `R1 verification_status: failed`
- `R1 nmse: NaN or not recorded`
- `R2 verdict: dirty or blocked_unverified`
- `R2 verification_status: unknown or failed`
- `R2 last_step_error: 'verification_target_mismatch' or 'dead loop'`
- `Steps consumed: 18-58 before failure`
- `Result text: 'SUMMARY: Step budget exhausted after N steps'`

## Solution

blocked_unverified in R1 is a critical signal: the kernel compiles but correctness cannot be confirmed. This means the verification command returned something unparseable or a non-terminal state. R2 should NOT inherit a blocked_unverified R1 state - it should start fresh.

### Implementation

```cuda
1. When R1 verification_status=blocked_unverified, R2 should NOT use R1's verification evidence. 2. R2 must run its own verification from scratch. 3. If R1's kernel compiles but verification is blocked, R2 should try a different kernel approach, not reuse the same code. 4. The session memory's 'verification_target_mismatch' blocker indicates the verification evidence is stale - R2 should clear it.
```

## Key Lessons

- blocked_unverified is worse than verified_fail - it means the verification pipeline couldn't even determine pass/fail
- NMSE=NaN in test_results indicates the kernel either crashed, returned inf/nan, or the test harness failed to execute properly
- R2 inherits 'Existing verification evidence is stale' from R1 - the stale evidence poisons R2's verification attempt
- When R1 is blocked_unverified, the session_memory blocker says 'verification_target_mismatch' - this is a direct signal to NOT reuse R1's artifact
- FA_05, FA_13, FA_14 are distinct from the 12 other experiments in that they failed R1 correctness, not just performance
- The experience pipeline captured 0 experiences from these failed R2 tasks - blocked_unverified cascades to R2 experience capture failure
- A different verification command or fallback runner might have resolved blocked_unverified in R1
