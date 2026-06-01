---
id: doc-context-hub-coalescing
title: "CUDA Memory Coalescing Essentials"
url: https://github.com/anthropics/context-hub/tree/main/content/cuda/docs/coalescing
source_category: official-doc
architectures: [sm100, sm90, sm80]
tags: [vectorized-loads, shared-memory-optimization]
retrieved_at: 2026-06-01
---

# CUDA Memory Coalescing Essentials

## Overview

Coalescing is the hardware combining a warp's global-memory accesses into as few memory transactions as possible. Adjacent threads should access adjacent addresses; strided or scattered access wastes bandwidth.

## Best Default Pattern

```cpp
int i = blockIdx.x * blockDim.x + threadIdx.x;
value = input[i];  // adjacent threads → adjacent addresses
```

## Common Bad Pattern

```cpp
value = input[i * stride];  // large stride → many transactions
```

## 2D Arrays and Pitch

For 2D row-major arrays, accesses are most efficient when threads move along the row dimension together. Use `cudaMallocPitch` when row width is awkward.

## Shared Memory As Reordering Tool

- Load from global memory in a coalesced pattern
- Reorder in shared memory
- Consume in the algorithm's preferred order

Common for: transpose, tiled GEMM, stencil halos, gather/scatter restructuring.

## Coalescing vs Bank Conflicts

These are different problems:
- Coalescing concerns global-memory transactions
- Bank conflicts concern shared-memory accesses

## When To Suspect Coalescing Problems

- Bandwidth is far below expectation
- Profiling shows many global-memory transactions per requested byte
- A transpose or gather/scatter kernel is unexpectedly slow
- Changing block shape changes performance dramatically

## Related KernelWiki Pages

- [pattern-memory-bound](../../wiki/patterns/memory-bound.md)
- [technique-vectorized-loads](../../wiki/techniques/vectorized-loads.md)
- [technique-swizzling](../../wiki/techniques/swizzling.md)
