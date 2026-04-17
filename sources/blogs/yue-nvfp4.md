---
id: blog-yue-nvfp4
title: "Blackwell NVFP4 Kernel Hackathon Journey"
author: Yue Zhang
url: https://yue-zhang-2025.github.io/2025/12/02/blackwell-nvfp4-kernel-hackathon-journey.html
source_category: benchmark-blog
architectures: [sm100, sm100a]
tags: [nvfp4, gemv, batched-gemv, vectorized-loads, cache-policy, register-budgeting]
retrieved_at: 2026-04-16
---

## Summary

Detailed optimization journey for GPU Mode NVFP4 Hackathon Problem 1 (Batched GEMV).

## Performance Progression
- CuTe DSL initial: 100μs
- Coalesced memory access: 443μs → 2000μs (wrong direction initially)
- Hardware intrinsics for FP4/FP8 decode: 443→39μs
- PTX assembly: 39→27μs
- Instruction-level parallelism: 27→22.9μs
- Final: 22.392μs

## Key Techniques
- `cvt.rn.f16x2.e2m1x2` PTX for FP4 conversion (vs C intrinsics)
- PTX byte unpacking `mov.b32 {tmp0,tmp1,tmp2,tmp3}`
- Per-K specialization with full loop unrolling
- Different cache policies per access pattern
