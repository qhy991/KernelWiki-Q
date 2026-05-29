---
id: exp-o-20260513-100002-int8-gemm-imma-tensor-core-tactics
title: 'SOL-ExecBench INT8 GEMM: IMMA Tensor Core instructions and tactic autotuning'
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

Hand-written CUDA tiled kernels for INT8 GEMM achieve 0.04x-0.99x speedup (slower than baseline). The correct approach is to use IMMA (Integer Matrix Multiply-Accumulate) Tensor Core instructions via CUTLASS or cuBLAS. IMMA processes 16x8x32 int8 elements per instruction on SM80+. Tactic autotuning selects optimal tile/warp/stage configurations based on matrix dimensions.

## Challenge

Agent writes custom CUDA tiled kernels with manual dot-product loops for INT8 GEMM. These achieve 0.04x-0.99x speedup because: (1) they use CUDA cores not Tensor Cores, (2) INT8 DP4A instructions are not exploited, (3) memory access patterns are suboptimal, and (4) no shared memory tiling optimization.

### Symptoms

- `Speedup 0.04x-0.99x — kernel is slower than PyTorch baseline`
- `Custom CUDA kernel uses per-element int8 multiply in a loop`
- `No Tensor Core (IMMA) usage — ncu shows no tensor instructions`
- `INCORRECT_NUMERICAL from B layout mistakes in hand-written kernels`

## Solution

Never hand-write CUDA kernels for INT8 GEMM. Use IMMA Tensor Core instructions through CUTLASS or cuBLAS. IMMA GemmShape<16,8,32> processes 16 rows, 8 columns, and 32 k-elements per instruction, giving 4096 int8 multiply-adds per Tensor Core clock cycle.

### Implementation

```cuda
// IMMA Tensor Core instruction shapes by SM version:
// SM75 (Turing):  GemmShape<8, 8, 16>  — limited INT8 support
// SM80 (Ampere): GemmShape<16, 8, 32>  — full IMMA
// SM86/SM89 (Ada): GemmShape<16, 8, 32>  — full IMMA, 100KB shared memory
// SM87 (Orin):   GemmShape<16, 8, 32>  — full IMMA, 100KB shared memory
// SM90 (Hopper): CUTLASS 3.x collective builder

// Alignment requirements for IMMA:
//   mat_a.size(1) % 16 == 0  (K must be multiple of 16)
//   mat_b.size(0) % 16 == 0  (K must be multiple of 16)
//   mat_b.size(1) % 8 == 0   (N must be multiple of 8)

// Tactic selection heuristic (SM89 example):
//   M <= 16: TileShape<16, 64, 128>, WarpShape<16, 64, 64>, 5 stages
//   M <= 32: TileShape<32, 64, 128>, WarpShape<16, 64, 64>, 6 stages
//   M <= 64: TileShape<64, 128, 64>, WarpShape<32, 64, 64>, 4-5 stages
//   M <= 128: TileShape<128, 128, 64>, WarpShape<64, 64, 64>, 4 stages
//   M > 128: TileShape<128, 128, 64>, WarpShape<64, 64, 64>, 3-4 stages
//
// Key constraint: TileK should be 64 or 128 for INT8 due to CUTLASS crosswise layout.
// WarpN should be 64 for INT8 IMMA operations.
// Stages limited by shared memory: SM80=164KB, SM86/SM89=100KB, SM87=100KB
```

## Key Lessons

- Never hand-write CUDA kernels for INT8 GEMM. The IMMA Tensor Core instruction processes 16x8x32 int8 elements per clock. Manual dot-product loops cannot compete — they achieve 0.04x-0.99x speedup vs 4x-6x with IMMA.
- IMMA instruction shape for SM80+: GemmShape<16, 8, 32>. This means one Tensor Core instruction multiplies a 16x32 int8 block by a 32x8 int8 block, accumulating into a 16x8 int32 result. Each instruction does 4096 multiply-adds.
- Alignment requirements: K must be multiple of 16, N must be multiple of 8. If inputs don't meet alignment, pad them.
- Tile/warp/stage autotuning is essential. Different matrix sizes need different configurations. Small M (M<=16) benefits from fewer warps and more stages. Large M (M>128) benefits from more warps and fewer stages.
- Shared memory limits constrain stages: SM80 has 164KB (allows 5-6 stages), SM86/SM89/SM87 have 100KB (allows 2-4 stages). TileShape and stages must be chosen together to fit in shared memory.
- TileK should be 64 or 128 for INT8 due to CUTLASS crosswise layout constraint. Do not use TileK=32 for INT8 — it wastes Tensor Core throughput.
- Custom tiled CUDA kernels for INT8 are a dead end. Even with shared memory tiling, a single SM's CUDA cores cannot match the throughput of Tensor Core IMMA instructions. Always use CUTLASS or cuBLAS for INT8 GEMM.
