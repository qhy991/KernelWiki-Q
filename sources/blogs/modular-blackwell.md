---
id: blog-modular-blackwell
title: "Matrix Multiplication on Blackwell"
author: Modular
url: https://www.modular.com/blog/matrix-multiplication-on-nvidias-blackwell-part-1-introduction
source_category: community-note
architectures: [sm100]
tags: [tcgen05, tmem, tma, 2sm-cooperative, pipeline-stages, tma-multicast]
retrieved_at: 2026-04-16
---

## Summary

Modular's blog series on writing Blackwell GEMM kernels from scratch, reaching 85% of SOTA.

## Key Techniques
- TMA multicasting: SMs collaborate on loading tiles into shared memory
- 2-SM MMA: two SMs' tensor cores collaborate on one large MMA
- 5-stage circular buffer pipelining: TMA and MMA iterate in parallel
- Clear optimization progression with benchmarks at each stage
