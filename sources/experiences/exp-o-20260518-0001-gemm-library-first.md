---
id: exp-o-20260518-0001-gemm-library-first
title: 'GEMM/MatMul tasks: always prefer library path (cuBLAS/CUTLASS) over handwritten
  CUDA kernels'
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
captured_at: '2026-05-18'
confidence: inferred
reproducibility: concept
---

GEMM/MatMul tasks: always prefer library path (cuBLAS/CUTLASS) over handwritten CUDA kernels

## Key Lessons

- GEMM = always use cuBLAS/CUTLASS path first. Never hand-write a matmul kernel from scratch.
- If torch.matmul delegation is accepted, just use it — the reference already does this.
- If custom kernel is required, start from CUTLASS templates, not from scratch.
- Recognize GEMM tasks by: task name contains 'gemm'/'matmul', reference is torch.matmul, inputs are 2D A(M,K)×B(N,K).T→C(M,N).
- A shared-memory tiled kernel without vectorization, warp tiling, and double buffering is still 100x too slow.
- cuBLAS auto-tunes across all GPU architectures — no single handwritten kernel can match this generality.
- 16×16 tiles are textbook examples, not production-grade — real implementations use 128×128 or larger with register blocking.
