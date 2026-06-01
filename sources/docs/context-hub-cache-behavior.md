---
id: doc-context-hub-cache-behavior
title: "CUDA Cache Behavior and Access Policy"
url: https://github.com/anthropics/context-hub/tree/main/content/cuda/docs/cache-behavior-and-access-policy
source_category: official-doc
architectures: [sm100, sm90, sm80]
tags: [cache-policy, vectorized-loads]
retrieved_at: 2026-06-01
---

# CUDA Cache Behavior and Access Policy

## Overview

Cache behavior fundamentals for bandwidth-limited kernels. No cache hint compensates for fundamentally poor locality — always fix coalescing, reuse distance, and working set shape first.

## Read-Only and Locality-Aware Access

- Group neighboring accesses by neighboring threads
- Avoid random scatter in the hottest loops
- Keep reused regions compact when possible

## L2 Access Policy Window

CUDA exposes stream-level access-policy controls for L2 persistence behavior:
- Set stream attributes for persistence windows
- Use only for demonstrably reused regions
- Tune hit ratio assumptions carefully

Overusing persistence windows can hurt other traffic and reduce global efficiency.

## Practical Workflow

1. Identify hotspot kernels
2. Confirm memory-bound behavior with profiling
3. Improve layout/coalescing first
4. Test cache/access-policy changes incrementally
5. Keep only changes that improve end-to-end latency

## Common Pitfalls

- Setting cache policy globally without per-kernel evidence
- Treating cache hints as deterministic guarantees
- Ignoring multi-stream interference in shared cache resources

## Related KernelWiki Pages

- [technique-cache-policy](../../wiki/techniques/cache-policy.md)
- [technique-vectorized-loads](../../wiki/techniques/vectorized-loads.md)
- [pattern-memory-bound](../../wiki/patterns/memory-bound.md)
