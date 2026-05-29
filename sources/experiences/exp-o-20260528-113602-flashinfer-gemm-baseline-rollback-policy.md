---
id: exp-o-20260528-113602-flashinfer-gemm-baseline-rollback-policy
title: Use verified cuBLAS baseline as rollback anchor for unstable WMMA rounds
experience_type: optimization
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
reproducibility: concept
---

Use verified cuBLAS baseline as rollback anchor for unstable WMMA rounds

## Key Lessons

- A high-quality verified baseline should be treated as production anchor in autoresearch loops.
- WMMA experimentation without strict rollback policy increases failure risk and can degrade final deliverable quality.
- For FlashInfer GEMM tasks, baseline-first then guarded custom branching is more stable than repeated full rewrites.
