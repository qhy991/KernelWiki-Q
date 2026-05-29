---
id: exp-o-20260430-001007-gemm-autotune
title: 'GEMM autotuning pipeline: per-model per-GPU tactic selection'
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

Automated benchmarking pipeline to find optimal CUTLASS GEMM tactic for each (model, GPU, shape, precision) combination

## Challenge

GEMM performance varies significantly across shapes, precisions, and GPU architectures. The optimal tactic (tile size, stage count, split-K) for one shape may be suboptimal for another. Manual tuning is infeasible for models with dozens of GEMM shapes.

## Solution

Automated per-model autotuning with M-bucket classification and JSON config output

Pipeline: 1) Extract all unique (M, N, K) shapes from model forward pass. 2) Classify M into buckets (decode_s, decode_b, small, medium_s, medium_l, large, huge, ultra). 3) For each shape, benchmark all available tactics (0-7 for BF16/FP16, 8-17 for INT8). 4) Select best tactic per shape. 5) Output JSON config for runtime dispatch. Config format: {(M,N,K): {best_tactic: int, time_us: float}}.

## Key Lessons

- No single CUTLASS tactic wins across all GEMM shapes. Per-shape autotuning is essential for production deployment
- M dimension is the most important variable for tactic selection; classify M into buckets and tune within each bucket
- cuBLAS is a strong baseline for BF16/FP16 large-M shapes; CUTLASS wins primarily for small-M and quantized (INT8/FP8) shapes
- Model-specific shapes should be extracted from actual forward pass, not assumed from architecture paper. Different models have very different shape distributions
- Store autotune results as JSON configs per (GPU, model) pair for fast runtime dispatch without re-benchmarking
- Autotune should include warmup iterations and multiple runs to get stable timing, especially for small shapes where variance is high
- Fallback to cuBLAS when no CUTLASS tactic is available (unsupported architecture, unusual shape). Always keep cuBLAS as safety net
