---
id: exp-o-20260430-001004-gemm-smbudget
title: GEMM shared memory budget and stage count tuning across SM architectures
experience_type: optimization
source_category: agent-experiment
architectures:
- sm90
tags:
- gemm
kernel_types:
- gemm
languages:
- cuda-cpp
- cute-dsl
captured_at: '2026-04-30'
confidence: inferred
reproducibility: concept
impl_family: cutlass
---

Different GPU architectures have different shared memory capacities, requiring tile and stage count adjustments

## Challenge

GEMM tile size and pipeline stage count must fit within shared memory budget. SM80 (A100) has 164KB, SM87 (Orin) has 100KB, SM89 (L20) has 100KB. Using SM80-optimized configs on SM87/89 causes shared memory overflow or reduced occupancy.

## Solution

Architecture-aware stage count and tile sizing based on shared memory budget formula

Formula: shared_mem_per_CTA = (TileM * TileK + TileN * TileK) * Stages * sizeof(Element) + epilogue_overhead. For BF16 on SM80: 128*64 + 32*128 = 12288 elements * 2B * 4 stages = ~96KB fits 164KB. For SM87/89 with 100KB: reduce to 3 stages or use smaller TileK. Each SM generation needs dedicated tactic table.

## Key Lessons

- Shared memory per CTA formula: (TileM*TileK + TileN*TileK) * Stages * sizeof(Element). Must fit within per-SM shared memory budget to avoid spilling to L1
- SM80 (A100) has 164KB shared memory allowing 4-5 stages with moderate tiles. SM87 (Orin) and SM89 (L20) have only 100KB, requiring 2-3 stages or smaller tiles
- Reducing stage count from 5 to 3 can save ~40% shared memory at cost of slightly more memory latency; worth it when budget is tight
- SM87 (Jetson Orin) has only 16 SMs, so using larger N-dimension tiles (128x256x64) with 8-warps-per-CTA reduces total CTA count and improves per-CTA work
- Occupancy is limited by shared memory when tiles are large; limited by register count when tiles are small with many stages
- Always validate shared memory usage at compile time; CUTLASS will fail to compile if tile+stage exceeds hardware limits
