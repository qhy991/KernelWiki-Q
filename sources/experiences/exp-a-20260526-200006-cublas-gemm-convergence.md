---
id: exp-a-20260526-200006-cublas-gemm-convergence
title: 'SOL-ExecBench GEMM: optimization convergence — cuBLAS 0.99x+ means switch
  to cublasLt with proper config'
experience_type: analysis
source_category: agent-experiment
architectures:
- sm90
tags:
- gemm
kernel_types:
- gemm
languages:
- cuda-cpp
captured_at: '2026-05-26'
confidence: inferred
reproducibility: concept
impl_family: cublas
---

When cuBLAS cublasGemmEx achieves speedup > 0.99x, the cublasGemmEx path is exhausted. Further gains require switching to cublasLt with: (1) CUBLAS_COMPUTE_32F_FAST_16F, (2) per-M algo caching, (3) 8+ heuristic candidates. This has been shown to reach 0.9999x on the same task. Do NOT declare convergence — switch strategy instead.

### Symptoms

- `R1 speedup is 0.99x+ with cuBLAS cublasGemmEx`
- `R2+ attempts cublasLt with naive config (1 candidate, no cache) → no improvement`
- `But with proper config (8 candidates, per-M cache, FAST_16F) → 0.9999x achievable`
- `Wasted time comes from wrong cublasLt configuration, not from choosing cublasLt`

## Challenge

After achieving 0.995x speedup with cublasGemmEx, further rounds using cublasLt with 1 heuristic candidate and no per-M caching failed to improve. However, a parallel experiment showed that cublasLt with CUBLAS_COMPUTE_32F_FAST_16F + 8 heuristic candidates + per-M algo caching reached 0.9999x. The key is NOT to stop optimizing, but to use the right cublasLt configuration.


## Solution

Decision rule for GEMM optimization when cublasGemmEx speedup >= 0.99x:

1. Do NOT stop — 0.99x with cublasGemmEx means the GemmEx path is saturated, but cublasLt can still improve.

2. Switch to cublasLt with this PROVEN configuration (verified 0.9999x on FP16 4096x4096):
   - CUBLAS_COMPUTE_32F_FAST_16F (avoids FP16→TF32 conversion overhead)
   - Per-M algo caching: std::unordered_map<int, AlgoCacheEntry>
   - 8+ heuristic candidates: cublasLtMatmulAlgoGetHeuristic(..., 8, results, &count)
   - 64MB workspace: cudaMalloc(&workspace, 64*1024*1024)
   - Global cublasLt handle (cublasLtCreate once, reuse)

3. Common FAILURE patterns with cublasLt (avoid these):
   - Using only 1 heuristic candidate → misses better algos
   - No per-workload caching → repeated algo search overhead
   - CUBLAS_COMPUTE_32F instead of FAST_16F → unnecessary precision conversion
   - Recreating handle/descriptors per call → overhead

4. To exceed 1.0x, consider: persistent kernels, Stream-K, Triton custom tiling, epilogue fusion.

## Key Lessons

- cuBLAS cublasGemmEx at 0.99x means the GemmEx path is saturated, NOT that the hardware peak is reached. cublasLt with proper config can reach 0.9999x+.
- cublasLt CAN be faster than cublasGemmEx when configured correctly: CUBLAS_COMPUTE_32F_FAST_16F + per-M algo caching + 8+ heuristic candidates + 64MB workspace.
- If R1 achieves 0.99x with cublasGemmEx, R2 should switch to cublasLt with the proven configuration — not retry GemmEx with different flags.
- The WRONG approach: using cublasLt with only 1 heuristic candidate and no caching (produces same or worse results as GemmEx). The RIGHT approach: 8 candidates + per-M caching.
