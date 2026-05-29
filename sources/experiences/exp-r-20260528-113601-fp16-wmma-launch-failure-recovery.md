---
id: exp-r-20260528-113601-fp16-wmma-launch-failure-recovery
title: FP16 WMMA runtime launch failure diagnosis and recovery
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
captured_at: '2026-05-28'
confidence: inferred
reproducibility: snippet
impl_family: custom_cuda_wmma
---

Round 3 compiled but failed correctness with unspecified launch failure; subsequent round recovered to verified pass after structural fixes.

## Challenge

Kernel passed compilation but failed at runtime with CUDA unspecified launch failure during verification.

### Symptoms

- `compile_success=true but correctness_passed=false`
- `root_cause_message includes 'CUDA error: unspecified launch failure'`
- `failure happens under full verification workload`

## Solution

Treat as runtime indexing/layout issue: enforce strict bounds in load/store paths, validate fragment layout assumptions, and use staged writeback checks before re-optimizing.

### Implementation

```cuda
Recovery checklist: (1) verify block/grid mapping against output tiles; (2) audit shared-memory strides and index ranges; (3) ensure WMMA fragment row/col layout matches memory layout; (4) guard final writeback; (5) rerun compile-smoke then full verification.
```

## Key Lessons

- WMMA code can compile yet still fail at runtime due to tile/index/layout mismatch.
- Launch failure should trigger safety-first structural debugging, not immediate micro-optimization.
- Recovered pass with low speedup should be marked as correctness milestone and seeded carefully.
