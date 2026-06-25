---
id: exp-kersor-rtx4090-sm89
title: "KerSor Automated Kernel Optimization — RTX 4090 (SM89) Campaign"
experience_type: campaign
source_category: agent-experiment
architectures:
- sm89
tags:
- attention
- mla
- gqa
- rmsnorm
- gemm
- moe
- fp8
- block-scale
- split-k
- paged-kv-cache
- kernel-fusion
- vectorized-loads
- cache-policy
kernel_types:
- mla
- gqa
- attention
- decode
- prefill
- rmsnorm
- gemm
- moe
languages:
- cuda-cpp
- triton
- python-cpp-extension
captured_at: '2026-06-17'
confidence: source-reported
reproducibility: benchmarked
impl_family: custom_cuda
---

## Overview

KerSor is an automated kernel optimization system that iteratively generates, benchmarks, and refines CUDA/Triton kernels through closed-loop optimization rounds. This campaign ran on NVIDIA RTX 4090 (SM89, Ada Lovelace) targeting 8 sol-execbench tasks from the FlashInfer-Bench suite, with real measured performance using `benchmark_reference:true` under torch 2.9.0+cu128.

## Campaign Results

| Task | Kernel Type | Real Speedup | Latency (ms) | Key Technique |
|---|---|---|---|---|
| 001_fused_add_rmsnorm_h2048 | Fused Norm | 9.38x | 0.0585 | Triton multi-row CTA, occupancy tuning |
| 008_gemm_n4096_k14336 | GEMM | 1.04x | 0.3996 | cuBLAS heuristic dispatch |
| 010_gemm_n6144_k4096 | GEMM | 1.04x | 0.1797 | Hybrid ATen + cublasGemmEx, B_T cache |
| 013_gqa_paged_decode | GQA Decode | 15066x* | 0.1109 | Split-K, cp.async, L1 .cg bypass |
| 018_mla_paged_decode | MLA Decode | 116.7x* | 0.1105 | 8-token unroll, ld.global.cs, split-K |
| 019_mla_paged_prefill | MLA Prefill | 40.2x* | 189.9 | FlashAttention-2 tiling, fused dual GEMM |
| 020_moe_fp8_block_scale | MoE FP8 | 1.91x | 21.08 | Lazy per-expert dequant, TF32 tensor cores |
| 021_rmsnorm_h128 | RMSNorm | 9.31x | 0.0432 | Warp-per-row, bfloat162 vectorization |

*Note: Tasks 013/018/019 measure against naive Python reference (not FlashInfer), so absolute latency is the meaningful metric. FlashInfer MLA kernels are SM80-only; no optimized baseline exists on SM89.

## Key Lessons

1. **Memory latency hiding via unrolled loads**: For paged KV cache with page_size=1 (scattered access), issuing 8 outstanding ld.global.cs loads per iteration amortizes DRAM latency far better than 4. Sync count drops from 0.5 to 0.25 per token.

2. **Split-K is essential for decode attention**: At batch_size=64 on SM89, per-head CTAs and non-split-KV approaches always regress. The KV sequence length is too large for a single CTA to process efficiently.

3. **L1 cache policy differentiation on SM89**: Using ld.global.cg (L1-bypass, L2-only) for streaming K-cache reads + cp.async for V-cache reads yields measurable gains by avoiding L1 pollution from the large KV working set.

4. **Triton occupancy tuning for normalization**: num_warps=8 (256 threads) gives 6 CTAs/SM vs 3 with num_warps=16. For memory-bound RMSNorm on SM89, more CTAs provide better memory latency hiding.

5. **Lazy expert dequantization for MoE**: With small batch sizes, most experts receive zero tokens per forward pass. Dequantizing weights on-demand per active expert (instead of upfront for all 32) saves ~50% memory bandwidth.

6. **cuBLAS dispatch strategy on SM89**: CUBLAS_COMPUTE_16F is broken on SM89 for fp16; must use COMPUTE_32F. For large M (≥2048), direct cublasGemmEx with NT layout beats ATen's mm(). For small M, pre-transposed B_T + ATen gives best results.

## Sources

- KerSor sessions: 20260610-144709, 20260611-184128, 20260612-020626, 20260613-202945, 20260614-000305, 20260614-200847, 20260617-130038, 20260617-232324
- Benchmark harness: sol-execbench (FlashInfer-Bench), torch 2.9.0+cu128
- Hardware: NVIDIA RTX 4090 24GB (sm_89, Ada Lovelace), 1008 GB/s memory bandwidth
