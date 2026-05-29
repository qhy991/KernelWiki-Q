---
id: exp-o-20260506-150001-int8-gemm-dp4a-vectorized
title: 'SOL-ExecBench INT8 GEMM: DP4A vectorized implementation'
experience_type: optimization
source_category: agent-experiment
architectures:
- sm90
tags:
- gemm
- fine-grained-quantization
- vectorized-loads
kernel_types:
- gemm
languages:
- cuda-cpp
captured_at: '2026-05-06'
confidence: inferred
reproducibility: concept
techniques:
- fine-grained-quantization
- vectorized-loads
impl_family: cublas
---

For SOL-ExecBench INT8 GEMM with small M (M<=16), DP4A vectorized implementation achieves 3.73x speedup using warp-level parallelism and vectorized int4 loads.

## Challenge

SOL-ExecBench PI-int8 GEMM tasks with small batch size (M=10) face challenges: (1) Tensor Core overhead dominates for small M, (2) cuBLAS has high launch overhead for tiny GEMM, (3) CUTLASS INT8 template instantiation fails frequently. Need a lightweight implementation that avoids these issues.

### Symptoms

- `cuBLAS cublasGemmEx achieves only 1-2x speedup for M=10`
- `CUTLASS INT8 template instantiation fails with incomplete type errors`
- `Standard GEMM libraries have high overhead for small batch sizes`

## Solution

Use DP4A (Dot Product 4 Accumulate) instruction with vectorized int4 loads and warp-level parallelism. One warp per row, each thread processes multiple K elements using DP4A for INT8 dot product.

Implementation pattern for SOL-ExecBench PI-int8 GEMM (M=10, N=1024, K=2048):
1. Grid: (ceil(N/32), M) - one warp per output row
2. Each thread computes multiple N elements using DP4A
3. Use __ldg() for vectorized int4 loads (128-bit)
4. DP4A instruction: __dp4a(int a, int b, int c) computes dot product of 4 int8 values
5. Accumulate in int32, write output as int32
6. No shared memory needed for this small problem size
7. Key optimization: vectorize memory access with int4 loads
8. Performance: 3.73x speedup, latency 0.021ms vs reference 0.077ms

## Key Lessons

- For small batch INT8 GEMM (M<=16), warp-level parallelism with DP4A is more efficient than Tensor Core libraries.
- DP4A instruction provides 4x throughput for INT8 dot products compared to scalar operations.
- Vectorized int4 loads (128-bit) significantly improve memory bandwidth utilization.
- One warp per row is optimal for M=10: provides enough parallelism without excessive overhead.
- No shared memory needed for small K (K<=2048) - register file is sufficient.
- cuBLAS/cuBLASLt have high launch overhead for tiny GEMM; custom kernels are better.
