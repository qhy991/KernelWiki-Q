---
id: doc-context-hub-warp-primitives
title: "CUDA Warp-Level Primitives"
url: https://github.com/anthropics/context-hub/tree/main/content/cuda/docs/warp-primitives
source_category: official-doc
architectures: [sm100, sm90, sm80]
tags: [reduction, warp-specialization, register-reuse]
retrieved_at: 2026-06-01
---

# CUDA Warp-Level Primitives

## Overview

Warp-scope communication patterns that avoid block-wide synchronization and often reduce shared-memory traffic. Core intrinsics: `__shfl_sync`, `__shfl_down_sync`, `__shfl_xor_sync`, `__ballot_sync`, `__all_sync`, `__any_sync`, `__activemask`, `__syncwarp`.

## When Warp Primitives Help

- Communication stays within one warp
- Want to avoid shared memory for small reductions or exchanges
- Block-wide barrier would be too expensive or unnecessary

## Shuffle vs Shared Memory

**Prefer shuffle when**: scope is one warp, data volume is small, want to avoid shared-memory round trip.

**Prefer shared memory when**: communication crosses warp boundaries, data footprint exceeds register comfort, access pattern spans whole block.

## Minimal Warp Reduction

```cpp
float x = value;
for (int offset = 16; offset > 0; offset >>= 1) {
    x += __shfl_down_sync(0xffffffff, x, offset);
}
```

Standard first step before reducing across warps with shared memory or atomics.

## Mask Discipline

For `_sync` intrinsics:
- Every participating lane must use the same mask
- Each calling lane must have its own bit set
- All named non-exited lanes must execute the same intrinsic with the same mask

Violating mask discipline leads to undefined behavior.

## Related KernelWiki Pages

- [technique-warp-specialization](../../wiki/techniques/warp-specialization.md)
- [technique-ping-pong-scheduling](../../wiki/techniques/ping-pong-scheduling.md)
