---
id: exp-o-20260518-0002-gemm-naive-kernel-diagnosis
title: Diagnose naive CUDA kernel characteristics when speedup << 0.1x
experience_type: optimization
source_category: agent-experiment
architectures:
- sm90
tags:
- gemm
- shared-memory-optimization
- vectorized-loads
kernel_types:
- gemm
languages:
- cuda-cpp
captured_at: '2026-05-18'
confidence: inferred
reproducibility: concept
techniques:
- shared-memory-optimization
- vectorized-loads
---

Diagnose naive CUDA kernel characteristics when speedup << 0.1x

## Key Lessons

- No __shared__ in kernel body = the kernel is missing the entire memory hierarchy. Do not tune it, redesign it.
- Scalar dot product over K dimension = memory bandwidth wasted. Need warp-level dot product with shuffle instructions.
- No half2/float4 loads = 93% memory bandwidth wasted. Vectorized loads MUST be used.
- If after 3 rounds speedup < 0.1x, the approach is fundamentally wrong. Stop iterating and switch to library path.
- Adding __shared__ without vectorized loads and warp tiling yields negligible improvement — don't expect smem alone to fix 100x gaps.
- A tiled kernel without double buffering still leaves load latency exposed — compute is stalled waiting for memory.
- The loop should check: if speedup < 0.05x, check for red flags above and suggest library fallback, not another iteration.
