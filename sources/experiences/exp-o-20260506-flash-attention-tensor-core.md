---
id: exp-o-20260506-flash-attention-tensor-core
title: Flash attention must leverage Tensor Cores for meaningful speedup
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
captured_at: '2026-05-06'
confidence: inferred
reproducibility: concept
---

Performance analysis shows flash_attention kernels achieve only 0.1-0.12x baseline speedup without Tensor Core utilization. Tensor Core path is essential for any speedup over baseline.

## Challenge

In 14 experiments (FA_01-FA_18, May 1 2026), only 2 passed compilation+correctness, but both achieved speedup far below 1.0x (FA_16: 0.116x, FA_17: 0.0043x). Performance analysis reports consistently identified: vector_bound as primary bottleneck, tensor_core_path_not_detected, bandwidth_utilization at 0.0-0.1%, and headroom of 0.68x-7.39x. The kernels were doing naive scalar operations instead of utilizing GPU Tensor Cores.

## Solution

Use WMMA/MMA instructions or CUTLASS-based tiled computation for Q*K^T and softmax*V

1. Flash Attention performance depends critically on the QK^T and PV matrix multiplications
2. These must use Tensor Cores via: (a) wmma::load_matrix_sync + wmma::mma_sync for direct WMMA, or (b) CUTLASS Gemm transpose+reshape utilities, or (c) cuBLAS Lt matmul for small batch sizes
3. For head_dim=128 and seq_len=512-8192, the QK^T tile should be 16x16 or 32x32
4. Use shared memory tiling: load Q tile and K tile into shared memory, compute partial dot products
5. Online softmax: compute running max and sum to avoid materializing full attention matrix
6. SRAM target: keep per-thread Q, K, V chunks in registers (~20KB per thread block for seq_len=512)
7. Key insight from analysis: bandwidth_utilization=0.1% means the kernel is entirely compute-bound on scalar units, NOT memory-bound as a proper flash attention should be

## Key Lessons

- Flash attention kernels MUST use Tensor Cores (WMMA/MMA or CUTLASS) for the QK^T and PV matmul steps. Scalar CUDA cores are ~10x too slow for these dimensions.
- bandwidth_utilization near 0% indicates the kernel is compute-bound on scalar units. Proper flash attention should be IO-bound (memory bandwidth limited), not compute-bound.
- For head_dim=128, use 16x16x16 or 32x32x16 WMMA fragments for the attention computation.
- Online softmax (flash attention algorithm) avoids materializing the full NxN attention matrix. Compute running max and sum per row during the K-dimension loop.
- Shared memory tiling is essential: load Q tile (Br x d) and K tile (Bc x d) into shared memory, compute partial attention scores, accumulate in registers.
- For small cache sizes (512), kernel launch overhead dominates. Consider batched processing or persistent kernel approach.
- The performance_analysis_report.txt with vector_bound + tensor_core_path_not_detected is a clear signal that the kernel needs to be rewritten with Tensor Core operations.
