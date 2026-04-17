---
id: blog-tcgen05-tutorial
title: "tcgen05 for dummies"
author: Gau Nernst
url: https://gau-nernst.github.io/tcgen05/
source_category: community-note
architectures: [sm100]
tags: [tcgen05, tmem, swizzling, pipeline-stages, persistent-kernel, warp-specialization, mbarrier]
retrieved_at: 2026-04-16
---

## Summary

Step-by-step tutorial building a Blackwell GEMM kernel from scratch in plain CUDA C++ with PTX, achieving 98% of cuBLAS performance.

## Performance Progression
- Basic kernel: 255 TFLOPS (17%)
- 128B swizzling: 695 TFLOPS (46%)
- Pipelining: 940 TFLOPS (62%)
- Warp specialization: ~1200 TFLOPS (80%)
- Persistent kernel: 1476 TFLOPS (98%) vs 1507 cuBLAS

## Key Findings
- tcgen05.mma operates directly on shared memory — no ldmatrix needed
- TMEM: 128×512 capacity, 32-bit elements, must alloc/dealloc
- mbarrier synchronization with phases and parity bits
- "Tensor Core programming on Blackwell is easier than previous generations"
- 128B swizzling alone gives 2.7× speedup
