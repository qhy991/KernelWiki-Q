---
id: doc-context-hub-memory-bound-playbook
title: "Memory-Bound Kernel Optimization Playbook"
url: https://github.com/anthropics/context-hub/tree/main/content/cuda/docs/memory-bound-kernel-optimization-playbook
source_category: official-doc
architectures: [sm100, sm90, sm80]
tags: [shared-memory-optimization, vectorized-loads, cache-policy]
retrieved_at: 2026-06-01
---

# Memory-Bound Kernel Optimization Playbook

## Overview

Playbook for optimizing kernels limited by memory movement rather than arithmetic throughput. Covers coalescing, cache locality, shared-memory staging, and bandwidth-focused validation.

## Primary Objectives

- Increase effective bandwidth
- Reduce wasted traffic
- Improve locality and access regularity

## High-Impact Levers

- Coalesced global-memory access
- Reuse through registers/shared memory
- Shared-memory layouts that avoid severe bank conflicts
- Data-layout changes that reduce strided/scattered loads

## Triage Sequence

1. Validate coalescing quality for major tensors
2. Check L1/L2 reuse opportunity and cache-policy behavior
3. Add or improve shared-memory staging for high-reuse tiles
4. Recheck occupancy/register pressure after staging changes

## Common Failure Modes

- Correct staging logic but poor layout (bank conflicts dominate)
- More shared memory with no reuse gain (occupancy drops, throughput worsens)
- Overly complex index math adds latency and defeats memory gains

## Verification Checklist

- Achieved bandwidth increases in profiler metrics
- Memory-related warp stalls decrease in hot sections
- Total runtime improves on representative production shapes

## Related KernelWiki Pages

- [pattern-memory-bound](../../wiki/patterns/memory-bound.md)
- [technique-vectorized-loads](../../wiki/techniques/vectorized-loads.md)
- [technique-swizzling](../../wiki/techniques/swizzling.md)
- [technique-cache-policy](../../wiki/techniques/cache-policy.md)
