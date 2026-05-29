---
id: exp-o-20260430-001006-gemm-precision
title: 'GEMM precision and accumulator selection: BF16 vs FP16 vs INT8 vs FP8'
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

Different data types require different accumulator types and operator variants for optimal Tensor Core throughput

## Challenge

Tensor Core support different input/accumulator type combinations. Using wrong accumulator type (e.g. float32 for FP16 when FP16 accumulation is available) leaves performance on the table. CUDA 12.8+ adds native FP16 accumulation support.

## Solution

Precision-specific operator and accumulator selection via template specialization

BF16: use OpMultiplyAddFastF32 with float accumulator for high accuracy. FP16: use OpMultiplyAddFastF16 with half_t accumulator on CUDA 12.8+ for better throughput; fall back to float accumulator on older CUDA. INT8: use per-row/column scaling with EpilogueVisitor. FP8: use Sm90AccFetch with EVT for fused scaling in epilogue.

## Key Lessons

- BF16 GEMM should always use float32 accumulator via OpMultiplyAddFastF32 for numerical accuracy with minimal overhead
- FP16 GEMM on CUDA 12.8+ should use half_t accumulator via OpMultiplyAddFastF16 for better throughput; fallback to float on older CUDA
- INT8 GEMM achieves 180-210 TFLOPS on SM89, significantly outperforming BF16/FP16 (110+ TFLOPS). Use when quantization error is acceptable
- FP8 GEMM achieves 200+ TFLOPS on SM89 with CUTLASS 3.x EVT. Best throughput but requires SM89+ hardware support
- CUTLASS Tensor Core instruction shapes: 16x8x16 for BF16/FP16 (MMA.16816), varies for INT8/FP8 depending on SM architecture
- Precision selection is a trade-off between throughput and accuracy: FP8 > INT8 > FP16 > BF16 in throughput, reversed in accuracy
