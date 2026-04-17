---
id: blog-flash-attention-4
title: "FlashAttention-4 Blog"
author: Tri Dao
url: https://tridao.me/blog/2026/flash4/
source_category: benchmark-blog
architectures: [sm100]
tags: [attention, flash-attention, tcgen05, tmem, 2sm-cooperative, software-exp, ping-pong-scheduling, conditional-rescaling, cute-dsl]
retrieved_at: 2026-04-16
---

## Summary

Tri Dao's blog post on FlashAttention-4 design for Blackwell's asymmetric hardware scaling.

## Key Techniques
- Asymmetric problem: tensor core throughput doubles but SFU count and SMEM bandwidth unchanged
- Ping-pong scheduling: two 128-token query tiles per CTA
- Software 2^x: Cody-Waite range reduction + Horner polynomial (Sollya-optimized coefficients)
- Multiplies exponential throughput without additional SFU hardware
- Conditional softmax rescaling: only when max jump is large
- 2-CTA backward: paired CTAs share TMEM, halves SMEM traffic
- CuTe-DSL implementation: 20-30x faster compilation than C++ templates

## Performance
- 1605 TFLOPS on B200 BF16 (71% utilization)
- 1.1-1.3x over cuDNN 9.13, 2.1-2.7x over Triton
