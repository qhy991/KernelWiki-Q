---
id: lang-triton
title: "Triton on Blackwell"
type: language
tags: [triton, attention, moe, gated-delta-net]
related: [kernel-nsa, kernel-gated-delta-net, kernel-fused-moe, lang-cute-dsl]
sources: [blog-nsa, blog-gated-delta-net, blog-flash-attention-4]
reproducibility: snippet
architectures: [sm100, sm90]
confidence: source-reported
blackwell_relevance: "Documents Triton limitations on SM100 (no tcgen05/TMEM access) and when to use Triton vs CuTe-DSL on Blackwell."
---

## Overview

Triton is used for many attention and linear-attention kernels (NSA, GatedDeltaNet, FLA). On Blackwell, Triton-generated kernels typically achieve 30-50% of hand-optimized CuTe-DSL performance for compute-bound workloads, but are excellent for rapid prototyping and memory-bound kernels.

## FlashInfer-Bench: AI-Generated Triton Performance

| Model | Avg Speedup vs FlashInfer | Resolved % |
|---|---|---|
| Gemini 2.5 Pro | 0.628x | 73.1% |
| GPT-5 | 0.467x | 92.3% |
| Claude Opus 4.1 | 0.456x | 73.1% |

AI-generated Triton kernels still lag behind hand-optimized production kernels.

## GatedDeltaNet Decode in Triton

```python
@triton.jit
def gated_delta_net_decode(
    Q, K, V, Gate, State, Output,
    qk_dim: tl.constexpr, v_dim: tl.constexpr, d: tl.constexpr,
):
    """Single-token decode: O(d^2) per token."""
    head_id = tl.program_id(0)
    # Load recurrent state S: [qk_dim*d, v_dim*d]
    s = tl.load(State + head_id * qk_dim * d * v_dim * d + offsets)
    q = tl.load(Q + offsets)
    k = tl.load(K + offsets)
    v = tl.load(V + offsets)
    g = tl.load(Gate + head_id)

    # Delta rule: S = g*S + k @ (v - S^T @ k)^T
    sk = tl.dot(tl.trans(s), k)
    delta_v = v - sk
    s = g * s + tl.dot(k[:, None], delta_v[None, :])
    o = tl.dot(tl.trans(s), q)

    tl.store(State + offsets, s)
    tl.store(Output + offsets, o)
```

## NSA Sparse Attention in Triton

```python
@triton.jit
def sparse_attention_fwd(Q, K, V, Output, TopK_Indices,
                         block_size: tl.constexpr, topk: tl.constexpr):
    """Attend to top-k sparse token blocks only."""
    qid = tl.program_id(0)
    q = tl.load(Q + qid * d + tl.arange(0, d))
    acc = tl.zeros([d], dtype=tl.float32)
    for i in range(topk):
        bidx = tl.load(TopK_Indices + qid * topk + i)
        k_block = tl.load(K + bidx * block_size * d + offsets)
        v_block = tl.load(V + bidx * block_size * d + offsets)
        scores = tl.dot(q[None, :], tl.trans(k_block))
        # softmax + accumulate...
```

## Limitations on Blackwell

1. **No direct tcgen05 access**: Triton compiler generates wgmma, not tcgen05
2. **No TMEM**: accumulators stay in registers
3. **CPU launch overhead**: impacts small-batch decode latency
4. **Workaround**: CUDA graphs (vLLM default for GatedDeltaNet)

## When to Use Triton on Blackwell
- Rapid prototyping
- Memory-bound kernels (bandwidth is bottleneck, not compute)
- Linear attention (GatedDeltaNet, FLA)
- Sparse attention (NSA) with irregular access
- **NOT** for peak-FLOPS compute-bound kernels (use CuTe-DSL instead)
