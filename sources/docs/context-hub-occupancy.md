---
id: doc-context-hub-occupancy
title: "CUDA Occupancy Essentials"
url: https://github.com/anthropics/context-hub/tree/main/content/cuda/docs/occupancy
source_category: official-doc
architectures: [sm100, sm90, sm80]
tags: [register-budgeting, shared-memory-optimization]
retrieved_at: 2026-06-01
---

# CUDA Occupancy Essentials

## Overview

Occupancy is the ratio of active warps on an SM to the maximum supported warps. It is constrained by threads per block, registers per thread, shared memory per block, and architectural limits.

## Important Caveat

Higher occupancy is not automatically better:
- Low occupancy can hurt latency hiding
- Very high occupancy can be unnecessary if the kernel is already bandwidth-limited
- Reducing registers just to raise occupancy can backfire if it causes spills to local memory

Treat occupancy as a constraint and diagnostic, not a standalone optimization target.

## Runtime APIs

```cpp
int minGridSize = 0;
int blockSize = 0;
cudaOccupancyMaxPotentialBlockSize(
    &minGridSize, &blockSize, my_kernel, 0, 0);
```

## What Usually Lowers Occupancy

- Large dynamic shared memory allocations
- High register pressure
- Overly large block sizes
- Cluster or architecture-specific launch constraints on newer GPUs

## Practical Tuning Rules

- Start in the 128 to 256 threads-per-block range unless you have a strong reason
- Prefer a multiple of warp size (32)
- If a kernel frequently calls `__syncthreads()`, several smaller blocks can outperform one very large block
- If reducing block size barely changes runtime, the kernel may not be occupancy-limited

## Common Misread

If performance is poor, ask these in order:
1. Is memory access coalesced?
2. Are there bank conflicts?
3. Is there divergence?
4. Is occupancy actually the limiting factor?

## Related KernelWiki Pages

- [pattern-register-pressure](../../wiki/patterns/register-pressure.md)
- [technique-register-budgeting](../../wiki/techniques/register-budgeting.md)
- [technique-warp-specialization](../../wiki/techniques/warp-specialization.md)
