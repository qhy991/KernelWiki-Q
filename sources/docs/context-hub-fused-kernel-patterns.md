---
id: doc-context-hub-fused-kernel-patterns
title: "CUDA Fused-Kernel Design Patterns"
url: https://github.com/anthropics/context-hub/tree/main/content/cuda/docs/fused-kernel-design-patterns
source_category: official-doc
architectures: [sm100, sm90, sm80]
tags: [epilogue-fusion, kernel-fusion]
retrieved_at: 2026-06-01
---

# CUDA Fused-Kernel Design Patterns

## Overview

Decision framework for when to combine multiple operations into one kernel. Fusion reduces global-memory round trips and launch overhead but can increase register pressure and lower occupancy.

## Why Fusion Helps

- Reducing global-memory round trips
- Reducing kernel-launch overhead
- Keeping intermediate values in registers/shared memory

## Why Fusion Can Hurt

- Register pressure and spills
- Lower occupancy
- Larger instruction footprint
- Harder scheduling and poorer maintainability

## Common Fusion Patterns

- Elementwise chain fusion (A→B→C)
- Reduction + lightweight post-processing
- GEMM epilogue fusion (bias/add/activation)
- Load-transform-store pipelines with shared-memory staging

## Practical Decision Rule

**Fuse when**: intermediate tensors are large, extra kernel boundaries dominate runtime, fused kernel remains resource-balanced.

**Do not fuse when**: each op is already compute-heavy, fusion introduces high register pressure or complex control divergence.

## Validation Workflow

1. Benchmark unfused baseline
2. Fuse one boundary at a time
3. Profile register usage, spills, occupancy, and bandwidth
4. Keep fusion only where end-to-end latency improves

## Related KernelWiki Pages

- [technique-epilogue-fusion](../../wiki/techniques/epilogue-fusion.md)
- [technique-kernel-fusion](../../wiki/techniques/kernel-fusion.md)
- [pattern-register-pressure](../../wiki/patterns/register-pressure.md)
