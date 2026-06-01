---
id: doc-context-hub-async-copy
title: "CUDA Async Copy Essentials"
url: https://github.com/anthropics/context-hub/tree/main/content/cuda/docs/async-copy
source_category: official-doc
architectures: [sm100, sm90, sm80]
tags: [double-buffering, pipeline-stages, shared-memory-optimization]
retrieved_at: 2026-06-01
---

# CUDA Async Copy Essentials

## Overview

Async copies from global memory to shared memory can avoid the register staging path on supported hardware (SM80+) and overlap data movement with computation.

## Conventional vs Async Copy

Conventional `shared[idx] = global[idx]` expands to load-into-register then store-to-shared. Async copy bypasses the register path.

## CUDA C++ Entry Points

- `cooperative_groups::memcpy_async(...)`
- `cuda::memcpy_async(...)` with `cuda::pipeline` or `cuda::barrier`

Both start an async transfer and require an explicit wait before consuming data in shared memory.

## Fundamental Safety Rule

After initiating async copy:
- Do not read destination shared memory until wait completes
- Do not modify source/destination while transfer is in flight

## Cooperative Groups Pattern

```cpp
namespace cg = cooperative_groups;
auto block = cg::this_thread_block();
extern __shared__ float smem[];
cg::memcpy_async(block, smem, gmem_ptr, bytes);
cg::wait(block);
block.sync();
```

## Pipeline Pattern

1. Acquire/start pipeline stage
2. Issue `cuda::memcpy_async`
3. Commit or advance the stage
4. Wait for the prior stage
5. Compute on the completed shared-memory tile

## When To Escalate To PTX / TMA

Stay in CUDA C++ when using `memcpy_async` or pipeline-level overlap. Drop to PTX/TMA for precise `cp.async` group semantics, bulk async copies, `mbarrier`, or cluster-scope completion.

## Related KernelWiki Pages

- [technique-double-buffering](../../wiki/techniques/double-buffering.md)
- [technique-pipeline-stages](../../wiki/techniques/pipeline-stages.md)
- [hw-tma](../../wiki/hardware/tma.md)
