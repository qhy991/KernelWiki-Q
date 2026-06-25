---
id: technique-split-k-attention-decode
title: "Split-K Decomposition for Paged Attention Decode"
type: technique
architectures: [sm89, sm90, sm100]
tags: [split-k, attention, decode, paged-kv-cache]
confidence: source-reported
reproducibility: benchmarked
prerequisites: []
related: [kernel-kersor-mla-decode-sm89, kernel-kersor-gqa-decode-sm89, kernel-flashmla, pattern-memory-bound]
sources: [exp-kersor-rtx4090-sm89]
blackwell_relevance: "Split-K attention is architecture-independent. The reduction kernel and workspace format transfer directly. SM100's larger register file and higher memory bandwidth shift the optimal K_CHUNKS higher."
---

# Split-K Decomposition for Paged Attention Decode

## Overview

For attention decode with long KV sequences, a single CTA per (batch, head) cannot fully utilize the GPU — the sequential KV processing creates a critical-path bottleneck. Split-K decomposes the KV sequence into K chunks processed by independent CTAs in parallel, followed by a lightweight reduction that merges partial results using log-sum-exp arithmetic.

KerSor experiments on RTX 4090 (SM89) consistently found that split-K is essential for decode attention once avg_L > 32-64 tokens. Per-head CTAs (without split-K) always regress regardless of other optimizations applied.

## Decomposition

```
KV sequence: L tokens → split into K chunks (K = 4, 16, or 32)
Each chunk: ceil(L/K) tokens, processed by independent CTA

Pass 1 (K CTAs per batch×head):
  Grid: (batch, heads, K)
  Each CTA computes: partial attention over its chunk
  Output: (m_k, d_k, acc_k[dim]) per chunk per (b, h)
    m_k = max logit in chunk (for numerical stability)
    d_k = sum of exp(logit - m_k) (softmax denominator)
    acc_k = sum of exp(logit - m_k) * V (unnormalized weighted sum)

Pass 2 (1 CTA per batch×head):
  Grid: (batch, heads)
  Merge K partial results using online softmax:
    global_max = max(m_0, m_1, ..., m_{K-1})
    For each chunk k:
      alpha = exp(m_k - global_max)
      output += alpha * acc_k
      sum    += alpha * d_k
    output /= sum
```

## Workspace Layout

```
Per (batch, head, chunk):
  workspace[slot_offset + 0]      = m   (float32, max logit)
  workspace[slot_offset + 1]      = d   (float32, softmax denominator)
  workspace[slot_offset + 2..dim+1] = acc (float32, unnormalized output)

Slot size = 2 + head_dim floats
Total workspace = batch × heads × K × (2 + head_dim) × 4 bytes

Example (MLA decode, batch=64, heads=16, K=16, dim=512):
  = 64 × 16 × 16 × 514 × 4 = 33.6 MB
```

## Adaptive K Selection

```
Dispatched at host side based on average sequence length:

avg_L ≤ 32:     no split-K (single CTA, SMEM-staged fast path)
avg_L = 33-63:  K = 4  (moderate parallelism, small workspace)
avg_L = 64-2047: K = 16 (main production path)
avg_L ≥ 2048:   K = 32 (full parallelism for long context)

Rationale: K should be chosen so each chunk has enough work (≥4 tokens)
to amortize CTA launch overhead, while providing sufficient parallelism
to saturate SMs.
```

## Strided vs Contiguous Chunking

```
Contiguous: chunk k gets tokens [k*chunk_size, (k+1)*chunk_size)
  Pro: better cache locality within chunk
  Con: load imbalance if last chunk is short

Strided: chunk k gets every K-th token starting at offset k
  Token i of chunk k = kv_indices[page_start + k + i * K]
  Pro: perfect load balance, better L2 cache distribution
  Con: no spatial locality within chunk

KerSor finding: strided wins for paged KV cache (page_size=1)
  → spatial locality is already destroyed by page indirection
  → load balance becomes the dominant factor
```

## Pass 2: Online Softmax Merge

```cuda
// Streaming merge: single pass, no sorting needed
// O(K × dim) work, no synchronization required

__global__ void splitk_reduce(
    const float* workspace,    // [B, H, K, 2+dim]
    __nv_bfloat16* output,     // [B, H, dim]
    float* lse_out,            // [B, H]
    int K)
{
    const int t = threadIdx.x;  // one thread per dim element

    float m_global = -FLT_MAX;
    float l_global = 0.0f;
    float out_val  = 0.0f;

    for (int k = 0; k < K; k++) {
        float mk = workspace[slot(k) + 0];
        float dk = workspace[slot(k) + 1];
        if (dk <= 0.0f) continue;  // empty chunk

        float new_m = fmaxf(m_global, mk);
        float alpha = exp2f(m_global - new_m);
        float beta  = exp2f(mk - new_m);

        out_val  = alpha * out_val + beta * workspace[slot(k) + 2 + t];
        l_global = alpha * l_global + beta * dk;
        m_global = new_m;
    }

    output[...] = __float2bfloat16(out_val / l_global);
    if (t == 0) lse_out[...] = m_global + log2f(l_global);
}
```

## GPU Utilization Analysis

```
Without split-K (single CTA per batch×head):
  Active CTAs = batch × heads = 64 × 16 = 1024
  SM89 has 128 SMs: 1024/128 = 8 CTAs/SM (good)
  BUT: each CTA processes L=2048 tokens sequentially
  Critical path = L × (load + compute) per token

With split-K=16:
  Active CTAs = batch × heads × K = 64 × 16 × 16 = 16,384
  16384/128 = 128 CTAs/SM → fully saturated, wave-limited
  Critical path = (L/K) × (load + compute) = 128 tokens/CTA

Speedup ≈ min(K, L/min_useful_chunk) × occupancy_efficiency
  For L=2048, K=16: theoretical 16× if perfectly balanced
  Actual: ~12× due to workspace write + pass2 overhead
```

## When to Use

- **Decode attention** with avg_L > 32 tokens (paged or contiguous KV cache)
- **Low-batch inference** where batch × heads alone doesn't saturate the GPU
- **Long-context inference** where L >> 1024 makes sequential processing too slow
- **GQA/MLA** where the head count is reduced (fewer CTAs without split-K)

## Caveats

- Workspace memory grows linearly with K × batch × heads × dim — can be significant for large models (33MB for MLA with K=16)
- Pass 2 adds latency: for very short sequences (L < 32), the overhead of workspace write + pass2 launch exceeds the benefit
- The `exp2f` / `log2f` 2-base arithmetic in pass1 and pass2 must be consistent — mixing bases produces incorrect results
- Strided chunking breaks if kv_indices has a repeating pattern aligned with the stride
- On SM90/SM100 with larger register files, higher unroll factors in pass1 shift the optimal K lower (each CTA can do more work internally)
