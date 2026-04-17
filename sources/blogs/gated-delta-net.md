---
id: blog-gated-delta-net
title: "Gated Delta Networks"
author: NVlabs
url: https://github.com/NVlabs/GatedDeltaNet
source_category: benchmark-blog
architectures: [sm90, sm100]
tags: [gated-delta-net, linear-attention, attention, triton, chunk-parallelism]
retrieved_at: 2026-04-16
---

## Summary

Linear attention mechanism with delta rule for intelligent memory management (ICLR 2025). Used in Qwen3-Next (3:1 hybrid ratio).

## Architecture
- Delta rule: targeted state updates (keep/forget)
- Exponential gating: adaptive memory decay
- Causal Conv1D for local context
- Fixed-size 128×128 state matrix (independent of sequence length)
- O(n) complexity vs O(n²) for standard attention

## Implementations
- NVlabs reference: Triton kernels
- FLA optimized: recommended, significantly faster, varlen support
- Chunk-based parallelism for prefill, streaming for decode

## Adoption
- Qwen3-Next-80B (3:1 GDN:attention ratio, 512 experts)
- Qwen3.5 (262K context, 10x+ throughput over Qwen3-32B at 32K+)
