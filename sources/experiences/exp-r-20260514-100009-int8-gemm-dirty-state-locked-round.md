---
id: exp-r-20260514-100009-int8-gemm-dirty-state-locked-round
title: 'SOL-ExecBench INT8 GEMM: dirty state cascade and locked_round dead loop in
  multi-round sessions'
experience_type: repair
source_category: agent-experiment
architectures:
- sm90
tags:
- gemm
- fine-grained-quantization
kernel_types:
- gemm
languages:
- cuda-cpp
captured_at: '2026-05-14'
confidence: inferred
reproducibility: snippet
techniques:
- fine-grained-quantization
impl_family: cublas
---

In multi-round autoresearch sessions, Round 2+ frequently enters dirty state (no verification evidence) because the agent either (1) copies Round 1 files verbatim and gets blocked by the locked_round policy guard, or (2) generates a fresh TODO scaffold instead of improving Round 1's solution. The locked_round guard fires 5 consecutive times and terminates the round. This affects ~50% of multi-round INT8 sessions.

## Challenge

When Round 1 produces a verified_pass result, Round 2 agent reads the Round 1 solution but then gets blocked by the 'locked_round' action policy. The policy treats the round as locked because canonical state exists. The agent cannot write new code, run verification, or make progress. After 5 consecutive blocked responses, the system terminates the round as dirty.

### Symptoms

- `Stopping this round to avoid a action policy locked_round dead loop`
- `Round is locked by canonical state. Do not modify, verify, or open new attempts`
- `The same blocked state was returned 5 times in a row`
- `Round 2 status: dirty (missing_evidence)`
- `Round 2 canonical_verification.json does not exist`
- `Round 2 solution.json is identical to Round 1 or is a TODO scaffold`

## Solution

When starting Round 2+, the agent must NOT copy Round 1 files directly. Instead, it should: (1) get a new task assignment via get_sol_execbench_task, (2) read the seed solution that the task dispatcher provides, (3) write improved code into the NEW attempt directory, (4) run verification on the new code. The key is that each round gets a fresh attempt directory — do not copy files into it manually.

### Implementation

```cuda
## Correct Round 2+ protocol:

1. **Get new task assignment**: Call get_sol_execbench_task to receive a fresh attempt directory and seed solution path. The dispatcher handles round state transitions.

2. **Read the seed solution**: The task dispatcher provides the seed_solution path from Round 1's best attempt. Read kernel.h, kernel.cu, main.cpp from the seed.

3. **Write IMPROVED code to NEW attempt dir**: Write new files to the attempt_dir provided by the dispatcher. Do NOT copy Round 1 files — write fresh code that incorporates improvements.

4. **Run verification**: Execute the canonical verification command on the new attempt. This creates canonical_verification.json and exits dirty state.

5. **Do NOT**: Copy Round 1 files verbatim, try to modify Round 1's directory, or skip the task assignment step.

## Why locked_round fires:
- The policy guard detects that the round has canonical state (from Round 1)
- It blocks modifications to prevent accidental overwrites
- The agent interprets this as a permanent block instead of a signal to use the proper task assignment flow
- After 5 blocks, the system terminates the round

## Diagnosing dirty state:
- If results.tsv shows 'dirty' for a round, check canonical_verification.json
- If it doesn't exist, verification never ran
- If solution.json is identical to prior round, the agent copied instead of improving
- If step_summaries show 'locked_round' messages, the agent hit the policy guard
```

## Key Lessons

- Round 2+ must start by calling get_sol_execbench_task to get a fresh attempt directory. Do NOT copy Round 1 files directly into a new directory — this triggers the locked_round policy guard.
- The locked_round guard fires when canonical state exists and the agent tries to modify it. This is a safety feature, not a bug. Work WITH the task assignment flow, not around it.
- If you see 'locked_round dead loop' in step summaries, the agent is trying to modify a locked round. The fix is to use the proper task assignment flow (get_sol_execbench_task) instead.
- Each round gets its own attempt directory. The seed solution from the previous round is provided by the dispatcher as a reference — read it, improve it, write the improved version to the NEW attempt dir.
- Dirty status (missing_evidence) means verification never ran. Always ensure verification runs within the first 5 steps of a new round to create canonical_verification.json.
