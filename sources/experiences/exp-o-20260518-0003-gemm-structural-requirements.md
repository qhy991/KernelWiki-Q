---
id: exp-o-20260518-0003-gemm-structural-requirements
title: Minimum structural requirements for handwritten CUDA GEMM to achieve >0.5x
  speedup
experience_type: optimization
source_category: agent-experiment
architectures:
- sm90
tags:
- gemm
- shared-memory-optimization
- pipeline-stages
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
- pipeline-stages
- vectorized-loads
---

## Challenge

If a custom CUDA GEMM kernel must be written (library path unavailable), what are the minimum structural requirements to reach even 50% of cuBLAS performance?

## Key Lessons

- Minimum tile size 128×128 for GEMM — 16×16 is educational only, not practical
- float4/half2 loads are NOT optional — they are the difference between using 100% and 6% of memory bandwidth
- Double buffering is required — without it, global→shared load latency is fully exposed on every tile
- Warp shuffle reduction is 5-10x faster than shared memory reduction — use __shfl_xor_sync
- When N is small and fixed (N=128), consider warp-per-row specialization instead of a general tiled kernel
- 256 threads/block minimum — occupancy matters. 128 threads/block = at most 25% occupancy on modern GPUs.
- If you cannot implement all 7 requirements, fall back to library path — partial implementation won't reach 0.3x.
