---
id: blog-flashmla
title: "FlashMLA — Multi-head Latent Attention"
author: DeepSeek AI
url: https://github.com/deepseek-ai/FlashMLA
source_category: benchmark-blog
architectures: [sm100, sm90]
tags: [mla, attention, decode, prefill, fp8, sparse-attention, tcgen05, tmem]
retrieved_at: 2026-04-16
---

## Summary

DeepSeek's efficient MLA kernels for V3/V3.2 with massive KV cache compression (70KB/token).

## Variants
- Dense MLA decoding (SM90): BF16, paged KV (block 64), 3000 GB/s, 660 TFLOPS on H800
- Sparse MLA decoding (SM90/SM100): FP8 KV, token-level sparsity, 410 TFLOPS H800, 350 TFLOPS B200
- Dense prefill (SM100): 1460 TFLOPS fwd, 1000 TFLOPS bwd on B200
- Sparse prefill (SM90/SM100): 640 TFLOPS H800, 1450 TFLOPS B200

## Token Format
656 bytes/token: 512B FP8 data + 16B FP32 scales + 128B BF16 RoPE embeddings
