---
id: exp-i-20260517-200010-int8-gemm-template
title: INT8 GEMM kernel implementation template for SOL-ExecBench
experience_type: implementation
source_category: agent-experiment
architectures:
- sm90
tags:
- gemm
- shared-memory-optimization
- fine-grained-quantization
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
- fine-grained-quantization
- vectorized-loads
impl_family: custom_cuda
---

INT8 GEMM kernel implementation template for SOL-ExecBench

## Solution

Use a simplified INT8 GEMM approach: basic tiled matrix multiply with INT8 inputs and INT32 accumulation, then rescale to output type. Avoid WMMA API complexity unless necessary. For large K dimensions, use vectorized int4 loads. For small M, use per-thread accumulation. For medium/large M, use shared memory tiling.

## Key Lessons

- INT8 GEMM accumulates in INT32 to prevent overflow. Never use FP32 accumulator for INT8 matmul in WMMA — must be INT32.
- INT8 WMMA tile size is always 16x16x16. The outer tile (TILE_M, TILE_N, TILE_K) must be multiples of 16.
- For Q4_0 quantized weights: unpack the full 32-element block, not just the first element. Each Q4_0 group = 32 values packed into 18 bytes.
- Pad shared memory with +4 elements on the K dimension to avoid bank conflicts on the inner accumulation loop.
- Use int4 vectorized loads (16 bytes) for INT8 data — this doubles bandwidth vs int2 loads.
- Separate the dequantization step from the matmul: first load and dequantize into shared memory, then accumulate.
- For small M (M<=32), per-thread accumulation without shared memory often outperforms WMMA due to lower launch overhead.
- Always check that TILE_K is a multiple of the vector load width (4 for int4, 16 for WMMA).
