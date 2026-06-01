---
id: doc-context-hub-tensor-core-pipeline
title: "Tensor Core Pipeline Patterns"
url: https://github.com/anthropics/context-hub/tree/main/content/cuda/docs/tensor-core-pipeline-patterns
source_category: official-doc
architectures: [sm100, sm90, sm80]
tags: [pipeline-stages, double-buffering, shared-memory-optimization, warp-specialization]
retrieved_at: 2026-06-01
---

# Tensor Core Pipeline Patterns

## Overview

End-to-end Tensor Core kernel structure covering global-to-shared staging, multi-stage K loops, async copy synchronization, and escalation from WMMA to WGMMA/TMA.

## Why Pipeline Design Dominates

In real GEMM-like kernels, arithmetic throughput is often high enough that data staging and synchronization decide final performance. A strong Tensor Core kernel needs:

- Global-memory tile fetch
- Shared-memory staging and layout control
- Fragment load and matrix instruction issue
- Overlapped staging for the next K tile

## Canonical Multi-Stage Loop

1. Stage N: copy tile data for current compute
2. Stage N+1: prefetch tile data for next compute step

With larger K, three-stage pipelines can smooth latency at the cost of more shared memory and register pressure.

## Synchronization Boundaries

Explicit boundaries needed between:
- Producer writes to shared memory
- Consumer fragment loads
- Matrix instruction issue
- Buffer reuse for next stage

## Shared-Memory Layout Rules

- Align tile rows/strides for load requirements
- Avoid severe bank conflicts in the staging pattern
- Keep layout choices consistent with fragment load layout expectations

## Stage-Depth Tradeoff

More stages can hide memory latency better, but also:
- Increase shared-memory footprint per block
- Reduce occupancy
- Increase control complexity

Tune stage count jointly with block-level warp count and tile shapes.

## WMMA vs WGMMA/TMA Escalation

Stay with WMMA-focused C++ pipeline when supported tile shapes and types fit. Escalate to lower-level PTX when you need architecture-specific warpgroup matrix instructions or advanced async tensor movement control.

## Related KernelWiki Pages

- [technique-pipeline-stages](../../wiki/techniques/pipeline-stages.md)
- [technique-double-buffering](../../wiki/techniques/double-buffering.md)
- [technique-swizzling](../../wiki/techniques/swizzling.md)
- [hw-tcgen05-mma](../../wiki/hardware/tcgen05-mma.md)
- [migration-wgmma-to-tcgen05](../../wiki/migration/wgmma-to-tcgen05.md)
