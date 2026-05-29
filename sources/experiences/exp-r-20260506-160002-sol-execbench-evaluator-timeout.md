---
id: exp-r-20260506-160002-sol-execbench-evaluator-timeout
title: 'SOL-ExecBench: evaluator times out after 180s'
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
impl_family: cublas
---

SOL-ExecBench evaluator can time out after 180 seconds for complex kernels. This prevents qa_report.json from being generated and blocks the finish tool.

## Challenge

The SOL-ExecBench evaluator times out after 180 seconds when running verification for kernels with long compilation or execution times. This causes 'Evaluator timed out after 180.0s' error and prevents qa_report.json from being generated.

### Symptoms

- `Evaluator timed out after 180.0s`
- `Evaluator did not produce a valid qa_report.json`
- `finish tool fails because no qa_report.json exists`
- `Task cannot complete even though the kernel may be correct`

## Solution

When the evaluator times out, the kernel is likely too slow or the compilation is too complex. Focus on making the kernel simpler and faster before re-running verification.

### Implementation

```cuda
1. If evaluator times out, the kernel likely has excessive compilation time or runtime
2. Simplify the kernel implementation to reduce compile time
3. Avoid deep template instantiation (e.g., CUTLASS) that increases compile time
4. Use simpler implementations (cuBLAS, DP4A) that compile faster
5. If the kernel is correct but slow, check if the timeout can be configured
6. Do NOT retry verification repeatedly - it will keep timing out
7. Consider switching to a different implementation strategy
```

## Key Lessons

- SOL-ExecBench evaluator has a 180-second timeout that cannot be changed by the agent.
- Evaluator timeout usually means the kernel takes too long to compile or execute.
- CUTLASS template-heavy kernels are more likely to time out due to long compilation.
- cuBLAS and DP4A implementations compile faster and are less likely to time out.
- Repeated retries of verification after timeout waste step budget.
- If evaluator times out, switch to a simpler implementation strategy.
