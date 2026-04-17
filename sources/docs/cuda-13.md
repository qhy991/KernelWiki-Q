---
id: doc-cuda-13
title: "CUDA Toolkit 13.0/13.1 — Blackwell Support"
url: https://developer.nvidia.com/blog/whats-new-and-important-in-cuda-toolkit-13-0/
source_category: official-doc
architectures: [sm100, sm100a, sm120]
tags: [tcgen05, nvfp4, cutile]
retrieved_at: 2026-04-16
---

## Summary

CUDA 13.0 and 13.1 release notes covering Blackwell GPU support.

## CUDA 13.0
- Full Blackwell GPU support (B200, GB200, B300, RTX 5000)
- CCCL 3.0, requires C++17+
- 32-byte aligned types (double4_32a, long4_32a) for 256-bit loads
- cuBLAS: FP64 emulation on Tensor Cores, CUBLAS_GEMM_AUTOTUNE
- Zstandard fatbin compression by default

## CUDA 13.1
- CUDA Tile programming model (tile-based abstraction)
- cuTile Python DSL for authoring tile kernels
- CUDA Tile IR (new virtual ISA)
- Green Contexts for fine-grained GPU resource partitioning
- cuBLAS: Grouped GEMM API for FP8/BF16 on Blackwell (up to 4x MoE speedup)
- Compile-time memory sanitizer (-fdevice-sanitize=memcheck)
- CUB deterministic floating-point reductions
