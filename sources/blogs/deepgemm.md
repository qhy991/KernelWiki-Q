---
id: blog-deepgemm
title: "DeepGEMM — FP8 GEMM Library"
author: DeepSeek AI
url: https://github.com/deepseek-ai/DeepGEMM
source_category: benchmark-blog
architectures: [sm100, sm90]
tags: [gemm, fp8, fine-grained-quantization, block-scale, jit-compilation, tcgen05, wgmma]
retrieved_at: 2026-04-16
---

## Summary

DeepSeek's high-performance FP8 GEMM library with fine-grained scaling, supporting both Hopper and Blackwell.

## Key Techniques
- Fine-grained quantization: tile-wise 1×128 activations, block-wise 128×128 weights
- SM90: WGMMA with Nc=128 CUDA core promotion (FP22→FP32)
- SM100: tcgen05.mma with TMEM, packed UE8M0 scale format, all memory layouts
- MoE grouped GEMMs: M-axis grouping, contiguous/masked/K-grouped layouts
- JIT compilation via NVRTC
- ~300 lines core kernel code
- Up to 1550 TFLOPS on H800
