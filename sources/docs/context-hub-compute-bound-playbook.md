---
id: doc-context-hub-compute-bound-playbook
title: "Compute-Bound Kernel Optimization Playbook"
url: https://github.com/anthropics/context-hub/tree/main/content/cuda/docs/compute-bound-kernel-optimization-playbook
source_category: official-doc
architectures: [sm100, sm90, sm80]
tags: [register-budgeting, warp-specialization]
retrieved_at: 2026-06-01
---

# Compute-Bound Kernel Optimization Playbook

## Overview

Playbook for optimizing kernels where arithmetic throughput is the dominant limiter. Covers instruction mix tuning, occupancy/ILP balance, register pressure control, and CUDA Core vs Tensor Core path selection.

## Primary Objectives

- Improve useful instruction issue rate
- Reduce dependency and scheduling stalls
- Select the right arithmetic path (CUDA Core vs Tensor Core)

## High-Impact Levers

- Improve instruction mix in hot loops
- Balance occupancy and ILP
- Control register usage to avoid spill-driven regressions
- Evaluate Tensor Core migration only when workload shape supports it

## Triage Sequence

1. Confirm the kernel is truly compute-bound after memory cleanup
2. Inspect stall reasons related to dependencies and issue efficiency
3. Tune unroll depth and block geometry together
4. Re-evaluate path selection (`cuda-core` vs `wmma`/Tensor Core)

## Common Failure Modes

- Aggressive unrolling increases spills and slows kernel
- Occupancy chasing hurts per-warp progress
- Tensor Core migration applied to non-matrix-like workloads

## Verification Checklist

- Throughput metrics improve with stable correctness
- Register spills do not increase unexpectedly
- End-to-end runtime improves for production-representative shapes

## Related KernelWiki Pages

- [pattern-compute-bound](../../wiki/patterns/compute-bound.md)
- [pattern-register-pressure](../../wiki/patterns/register-pressure.md)
- [technique-register-budgeting](../../wiki/techniques/register-budgeting.md)
- [technique-warp-specialization](../../wiki/techniques/warp-specialization.md)
