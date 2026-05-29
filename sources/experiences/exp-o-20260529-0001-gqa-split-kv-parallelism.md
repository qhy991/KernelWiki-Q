---
id: exp-o-20260529-0001-gqa-split-kv-parallelism
title: 'GQA paged decode: split-KV parallelism is mandatory for competitive performance'
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

## Challenge

A single-warp (32 threads) GQA kernel that sequentially iterates over all KV tokens hangs on large workloads (batch=64, 55K+ pages). The kernel compiles and produces correct results on tiny inputs, but the O(seq_len) per-thread work makes it 10-100x slower than the FlashInfer reference baseline.

## Solution

Use split-KV parallelism: partition the KV sequence across multiple thread blocks (or warps within a block), each computing partial softmax(Q*K)*V for its chunk, then merge the partial results using the log-sum-exp trick (online softmax reduction).

## Key Lessons

- NEVER write a single-warp sequential GQA kernel for sol-execbench — it WILL time out on large workloads
- Split-KV parallelism is the #1 optimization for GQA paged decode: it converts O(seq_len) per-block to O(seq_len/num_splits) per-block
- The online softmax merge (log-sum-exp trick) is not optional — it is the mathematical foundation for split-KV correctness
- Grid = (heads, batches, splits) with splits = ceil(num_pages / pages_per_split) — this is the parallelism that makes or breaks performance
- For page_size=1, each token is one page — the page table loop IS the sequence loop (no inner dimension)
- GQA ratio 8:1 means 8 query heads share 1 KV head — load K/V once and broadcast to all 8 query heads in the group
- A kernel that passes correctness on batch=1/seq=256 but hangs on batch=64/seq=55K is an algorithmic issue, not a bug
- Reference FlashInfer split-KV implementation in owl/skills/gqa-paged-attention/REFERENCES/ provides the correct pattern
