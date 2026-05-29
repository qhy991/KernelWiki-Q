---
id: exp-o-20260529-0002-gqa-single-warp-antipattern
title: 'GQA paged decode: single-warp (32 threads) kernel is a fatal anti-pattern'
experience_type: optimization
source_category: agent-experiment
architectures:
- sm90
tags:
- attention
kernel_types:
- attention
languages:
- cuda-cpp
captured_at: '2026-05-29'
confidence: inferred
reproducibility: concept
---

GQA paged decode: single-warp (32 threads) kernel is a fatal anti-pattern

## Challenge

Agent wrote a GQA kernel with blockDim=32 (one warp) that sequentially iterates all KV tokens per query head. The kernel loops: for each page in [kv_indptr[b], kv_indptr[b+1]): load K, compute QK dot product, track online softmax max/sum, accumulate V. With 55K pages per batch and head_dim=128, a single thread performs ~7 million FMA operations — far exceeding the 600s sol-execbench timeout.

## Solution

This kernel design is fundamentally unscalable. The fix is not to optimize this single-warp kernel (e.g., with shared memory tiling) — the fix is to use split-KV parallelism that partitions the KV sequence across multiple blocks.

## Key Lessons

- blockDim=32 for GQA decode is a fatal anti-pattern — NEVER use 1 warp for the entire KV sequence
- If your GQA kernel grid is (heads, batches) without a third splits dimension, it WILL time out on large inputs
- Correctness on small inputs does NOT validate performance: batch=1/seq=256 takes milliseconds, batch=64/seq=55K takes forever
- The gap between 'compiles and runs' and 'meets performance target' is enormous for attention kernels
- Always estimate arithmetic intensity: 55K pages * 128 dim * 2 (QK+V) = 14M FLOPs/thread * 4 serial iters = 56M FLOPs per warp
- When the RAG recalls no split-KV experience, read the FlashInfer reference code in REFERENCES/ directory to learn the pattern
