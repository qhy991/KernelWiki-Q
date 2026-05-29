---
id: exp-o-20260430-200003-gemm-handle-reuse-measure
title: 'SOL-ExecBench BF16 GEMM: handle reuse is not guaranteed to improve performance'
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
captured_at: '2026-04-30'
confidence: inferred
reproducibility: concept
impl_family: cublas
---

For medium-size BF16 GEMM, switching from a simple persistent handle to getCurrentCUDABlasHandle-based reuse passed correctness but did not improve speedup.

## Challenge

Once a correctness-passing cuBLAS BF16 GEMM baseline exists, the next temptation is to optimize away handle creation overhead. The question is whether handle reuse is a meaningful optimization for the actual problem shape.

## Solution

Compare the simplest passing cuBLAS baseline against a handle-reuse variant instead of assuming reuse is always better.

On the same SOL-ExecBench BF16 dense GEMM task, a round-1 cuBLAS baseline with a persistent handle achieved about 1.82x speedup. A round-2 variant using at::cuda::getCurrentCUDABlasHandle() still passed correctness, but measured around 1.69x speedup. The change was technically correct but not performance-positive for this shape.

## Key Lessons

- Handle reuse is not a universally positive optimization for BF16 GEMM; measure it against the simpler passing baseline.
- For these SOL-ExecBench dense GEMM shapes, correctness-passing cuBLAS baseline quality matters more than shaving handle-management overhead.
- If a handle-reuse change does not beat the prior kept baseline, keep the simpler implementation.
- Post-baseline optimizations should be judged by measured speedup, not by intuition about reduced overhead.
