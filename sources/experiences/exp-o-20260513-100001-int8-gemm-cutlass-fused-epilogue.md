---
id: exp-o-20260513-100001-int8-gemm-cutlass-fused-epilogue
title: 'SOL-ExecBench INT8 GEMM: CUTLASS EpilogueVisitorPerRowPerCol fused dequantize
  pattern'
experience_type: optimization
source_category: agent-experiment
architectures:
- sm90
tags:
- gemm
- fine-grained-quantization
kernel_types:
- gemm
languages:
- cuda-cpp
- cute-dsl
captured_at: '2026-05-13'
confidence: inferred
reproducibility: snippet
techniques:
- fine-grained-quantization
impl_family: cutlass
---

The highest-performance INT8 GEMM uses CUTLASS 2.x EpilogueVisitorPerRowPerCol to fuse the dequantize (int32_acc * scale_a[row] * scale_b[col]) into the GEMM epilogue. This eliminates the extra kernel launch and int32 memory traffic that a separate dequant kernel requires. Compared to cuBLAS + separate dequant (2.5x speedup), fused epilogue achieves 4x-6x speedup.

## Challenge

The cuBLAS + separate dequant kernel pattern has two performance problems: (1) an extra kernel launch overhead (~5-10us), and (2) the int32 accumulator matrix [M,N] must be written to global memory and read back by the dequant kernel. For small M (e.g., M=10), the extra kernel launch dominates total latency.

### Symptoms

- `cuBLAS + dequant achieves only 2.0x-2.7x speedup over float32 baseline`
- `Extra kernel launch adds ~5-10us fixed overhead`
- `INT32 intermediate [M,N] memory traffic: read M*N*4 bytes + write M*N*4 bytes`
- `For M=10, N=1024: extra traffic is 80KB, comparable to total compute`

## Solution

Use CUTLASS 2.x EpilogueVisitorPerRowPerCol to fuse dequantize into the GEMM epilogue. The per-token scale_a[M] and per-channel scale_b[N] are applied during the epilogue write-out, eliminating the intermediate int32 buffer and extra kernel launch.

### Implementation

```cuda
// CUTLASS 2.x fused epilogue pattern:
//
// 1. Define the EpilogueVisitor:
using EpilogueVisitor = cutlass::epilogue::threadblock::EpilogueVisitorPerRowPerCol<
    ThreadblockShape,                    // e.g., GemmShape<128, 128, 64>
    GemmKernel::kThreadCount,            // threads per CTA
    AlphaColTileIterator,                // per-channel scale_b[N] iterator
    OutputTileIterator,                  // output tile iterator
    int32_t,                             // ElementAccumulator
    float,                               // ElementCompute
    EpilogueOutputOp>;                   // LinearCombination functor

// 2. The visitor applies in epilogue:
//    result = accumulator * scale_a[row] * scale_b[col]
//    No intermediate int32 buffer needed.
//    No separate dequant kernel needed.

// 3. Key CUTLASS template parameters for INT8 IMMA on SM80+:
using InstructionShape = cutlass::gemm::GemmShape<16, 8, 32>;  // IMMA instruction
using ElementA = int8_t;
using ElementB = int8_t;
using ElementC = cutlass::bfloat16_t;  // or half_t
using ElementAccumulator = int32_t;
using ElementCompute = float;

// 4. Layout mappings:
//    A is [M,K] row-major -> cutlass::layout::RowMajor
//    B is [K,N] col-major -> cutlass::layout::ColumnMajor
//    C is [M,N] row-major -> cutlass::layout::RowMajor
//    scale_a is [M] float -> RowMajor
//    scale_b is [N] float -> ColumnMajor (per-channel)
```

## Key Lessons

- CUTLASS EpilogueVisitorPerRowPerCol fuses int32->float dequantize with per-token scale_a[M] and per-channel scale_b[N] into the GEMM epilogue. This is the single most important optimization for INT8 GEMM: it removes the extra kernel launch and intermediate memory traffic.
- The formula in the fused epilogue is: output[row][col] = (bfloat16)(accumulator[row][col] * scale_a[row] * scale_b[col]). Accumulator is int32 from IMMA, scale_a and scale_b are float32.
- CUTLASS INT8 IMMA uses ElementA=int8_t, ElementB=int8_t, ElementAccumulator=int32_t. The instruction shape for SM80+ is GemmShape<16,8,32>. For SM75 it is GemmShape<8,8,16>.
- Layout mapping for SOL-ExecBench: A is [M,K] row-major, B is [K,N] column-major (stride(0)==1), C is [M,N] row-major. B being column-major means using cutlass::layout::ColumnMajor for B.
- For small M (M<=16), the cuBLAS + dequant overhead is dominated by the extra kernel launch. Fused epilogue avoids this entirely and is essential for good speedup at small batch sizes.
- If CUTLASS fused epilogue is not available, cuBLAS + dequant is an acceptable fallback but expect only 2.0x-2.7x speedup vs 4x-6x with fused epilogue.
