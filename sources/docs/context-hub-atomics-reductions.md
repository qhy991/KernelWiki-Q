---
id: doc-context-hub-atomics-reductions
title: "CUDA Atomics and Reduction Patterns"
url: https://github.com/anthropics/context-hub/tree/main/content/cuda/docs/atomics-and-reductions
source_category: official-doc
architectures: [sm100, sm90, sm80]
tags: [reduction, shared-memory-optimization, register-reuse]
retrieved_at: 2026-06-01
---

# CUDA Atomics and Reduction Patterns

## Overview

Decision framework for direct atomics vs shared-memory reductions vs warp-first patterns.

## Scope Choice

- Shared-memory atomics: contention within one block
- Global-memory atomics: visible across blocks, costlier under heavy contention

Common pattern: reduce within warp → reduce within block using shared memory → one global atomic per block.

## Preferred Reduction Structure

1. Warp shuffle reduction
2. Combine warp results in shared memory
3. Write one value per block or one atomic per block

Reduces contention and memory traffic vs one atomic per thread.

## When Direct Atomics Are Fine

- Output has low contention
- Kernel is not dominated by the atomic path
- Examples: histogram with many bins, sparse accumulation with low collision

## When Atomics Become A Problem

- Many threads update the same location
- Output space is very small
- Kernel becomes serialization-bound

Switch to hierarchical reduction or privatization.

## Strategy Guide

- One scalar result per block: block reduction in shared memory
- One scalar for whole grid: block reduction plus final stage
- Many bins with moderate collisions: shared-memory privatization, then flush
- Warp-local aggregation: use shuffle before shared/global memory

## Related KernelWiki Pages

- [technique-software-exp](../../wiki/techniques/software-exp.md)
- [technique-persistent-kernels](../../wiki/techniques/persistent-kernels.md)
