---
id: exp-r-20260513-100010-verification-contract-policy-violation
title: 'AutoResearch verification contract policy: sandbox command not declared in
  execution contract'
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
captured_at: '2026-05-13'
confidence: inferred
reproducibility: snippet
---

When the agent runs verification commands via sandbox_execute that are not the declared canonical verification command, the policy engine blocks them with: 'this sandbox command looks like a verification or benchmark action, but it is not declared by the current attempt execution contract'. Always use the canonical verification command provided in the task assignment.

## Challenge

Agent attempts to run ad-hoc verification commands (e.g., custom compile scripts, manual benchmark runs) instead of using the canonical verification command provided in the task assignment. The policy engine detects these as undeclared verification actions and blocks them.

### Symptoms

- `Verification contract policy: this sandbox command looks like a verification or benchmark action`
- `but it is not declared by the current attempt execution contract`
- `Use one of the declared commands, or add a domain contract`
- `sandbox_execute failed`

## Solution

Always use the exact canonical verification command provided in the task assignment's 'Canonical verification command' field. Never create ad-hoc verification scripts. If the canonical command is missing, recover it from task binding/runtime preflight first.

### Implementation

```cuda
// The task assignment contains:
// 'Canonical verification command (reuse verbatim when verifying):'
//   cd /home/qinhaiyan/SOL-ExecBench && uv run sol-execbench <problem_dir> --solution <solution.json> --json
//
// Use this EXACT command. Do not:
// - Create custom verification scripts
// - Modify the command (except solution.json path)
// - Run alternative verification methods
// - Add extra flags not in the canonical command
//
// If you need compile-smoke first, use the declared compile-smoke command,
// not a custom one.
```

## Key Lessons

- The verification contract policy blocks undeclared sandbox commands that look like verification/benchmark actions. Always use the canonical verification command from the task assignment.
- If the canonical command is missing from the task assignment, recover it from 'task binding/runtime preflight' before attempting verification.
- Do not create ad-hoc verification scripts or modify the canonical command. The policy engine pattern-matches sandbox commands against declared verification actions.
- For compile-smoke checks, use the declared compile-smoke command from the task assignment, not a custom compile script.
- When stuck in repeated verification failures, re-read the task assignment to find the exact canonical command rather than trying different command variations.
