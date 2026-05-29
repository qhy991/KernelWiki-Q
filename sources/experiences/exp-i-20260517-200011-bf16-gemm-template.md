---
id: exp-i-20260517-200011-bf16-gemm-template
title: BF16 GEMM kernel implementation template for SOL-ExecBench
experience_type: implementation
source_category: agent-experiment
architectures:
- sm90
tags:
- gemm
- shared-memory-optimization
- vectorized-loads
kernel_types:
- gemm
languages:
- cuda-cpp
captured_at: '2026-05-17'
confidence: inferred
reproducibility: concept
techniques:
- shared-memory-optimization
- vectorized-loads
impl_family: custom_cuda
---

BF16 GEMM kernel implementation template for SOL-ExecBench

## Solution

Three-tier strategy: M=1 uses simple per-row dot product with uint2 vectorized loads (2 BF16 elements per load). M<=32 uses shared memory tiling with warp shuffle reduction. M>32 uses full block tiling. All accumulation in FP32 to preserve precision. BF16 conversion at load and store only. Use __float2bfloat16() and __bfloat162float() intrinsics.

## Key Lessons

- BF16 computation uses float for accumulation to preserve precision. Convert to BF16 only at store time.
- uint2 loads 2 BF16 elements (4 bytes) — check 4-byte alignment. uint4 loads 4 BF16 elements (8 bytes) — check 8-byte alignment.
- __shfl_down_sync is always faster than shared memory for warp-level reduction. Use shared memory only for cross-warp reduction.
- TILE_K=16 or 32 works well for BF16; larger K tiles increase shared memory usage without proportional benefit.
- BF16 has limited range (same exponent as FP32 but 8-bit mantissa). Be careful with very large intermediate values.
- Avoid the atomicAdd pattern for warp reduction — use shuffle + shared memory for deterministic results.
- For M=1 scalar kernels: 1 thread per row, vectorized loads along K, simple FP32 accumulation, no synchronization needed.
- On RTX 4090 (sm_89), BF16 tensor core operations use the sm_80 path — ensure architecture flags include sm_80 and sm_89.
