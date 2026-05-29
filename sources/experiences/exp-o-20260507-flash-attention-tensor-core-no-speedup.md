---
id: exp-o-20260507-flash-attention-tensor-core-no-speedup
title: All flash_attention kernels pass correctness but achieve 0.0025x-0.0425x speedup
  due to scalar-only compute
experience_type: optimization
source_category: agent-experiment
architectures:
- sm90
tags:
- attention
- flash-attention
kernel_types:
- attention
- flash-attention
languages:
- cuda-cpp
captured_at: '2026-05-07'
confidence: experimental
reproducibility: concept
---

In the 20260506-07 batch, 8 flash_attention kernels passed KernelEval correctness verification (nmse < 1e-4) but achieved 0.0025x-0.0425x baseline speedup. All were diagnosed as vector-bound with 0.0-0.1% bandwidth utilization and no Tensor Core usage.

## Challenge

All flash_attention kernels (FA_02, FA_03, FA_04, FA_09, FA_10, FA_15, FA_17) passed correctness (nmse 5e-5) but were 23x-400x slower than baseline. Performance analysis consistently shows: (1) bandwidth_utilization 0.05-0.13%, (2) peak_utilization 0.03-3.5%, (3) tensor_core_path_not_detected, (4) vector-bound, (5) headroom 0.16x-28x. This is a 100% failure rate for performance, not correctness.

## Solution

Flash attention kernels MUST use Tensor Cores (WMMA/MMA) for the QK^T and PV matrix multiplications. The current kernels use only scalar CUDA cores, which are ~10x slower for these dimensions.

## Key Lessons

- Flash_attention correctness (nmse < 1e-4) is EASY - scalar implementation passes. Performance is HARD - requires Tensor Cores.
- bandwidth_utilization 0.0-0.13% is the clearest signal: the kernel is compute-bound on scalar units, not memory-bound as a properly optimized flash attention should be.
- tensor_core_path_not_detected in diagnosis = MUST rewrite the matmul portions with WMMA/MMA
- FA_10 (best flash_attention at 0.0425x) still uses only shared memory + warp intrinsics, no Tensor Cores. shared_memory alone is insufficient.
- The performance_analysis_report's 'evidence' field explicitly says '0.8% of baseline' and 'bandwidth_utilization=0.1%' - these are actionable诊断 signals
- For head_dim=128, the QK^T matmul needs WMMA fragments of shape 16x16x16 or 32x32x16 to be competitive
- topk (TK_05) achieved 1.57x because it's a sort/selection problem that doesn't need Tensor Cores - it can use warp-level sort primitives
- Even 65 steps of optimization on flash_attention cannot fix the fundamental architectural issue (no Tensor Cores) - the agent needs explicit guidance to use WMMA
