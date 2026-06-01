---
id: doc-context-hub-launch-bounds
title: "CUDA Launch Bounds and Register Pressure"
url: https://github.com/anthropics/context-hub/tree/main/content/cuda/docs/launch-bounds-and-registers
source_category: official-doc
architectures: [sm100, sm90, sm80]
tags: [register-budgeting, register-reuse]
retrieved_at: 2026-06-01
---

# CUDA Launch Bounds and Register Pressure

## Overview

`__launch_bounds__(maxThreadsPerBlock, minBlocksPerMultiprocessor)` gives the compiler launch-time assumptions, affecting register allocation and instruction scheduling. Register pressure directly affects occupancy.

## Why It Matters

- Too many registers per thread → reduces active blocks/warps
- Too few registers → causes spills to local memory
- Tuning is a balance: occupancy gain vs spill cost

## Practical Tuning Pattern

1. Start from correctness and baseline performance
2. Inspect occupancy and local-memory traffic in Nsight Compute
3. Try `__launch_bounds__` with realistic block sizes
4. Re-measure runtime, spills, and achieved occupancy
5. Keep the setting only if end-to-end time improves

## `-maxrregcount` Caution

Compiler flag `-maxrregcount` caps registers globally but is blunt — may improve occupancy but also increase spills. Prefer targeted kernel-level `__launch_bounds__` before global caps.

## Common Mistakes

- Optimizing for occupancy percentage alone
- Forcing low register count without checking spill metrics
- Setting launch bounds that don't match actual launch configuration

## Related KernelWiki Pages

- [technique-register-budgeting](../../wiki/techniques/register-budgeting.md)
- [pattern-register-pressure](../../wiki/patterns/register-pressure.md)
- [technique-warp-specialization](../../wiki/techniques/warp-specialization.md)
