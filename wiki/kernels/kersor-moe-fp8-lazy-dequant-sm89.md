---
id: kernel-kersor-moe-fp8-lazy-dequant-sm89
title: "FP8 MoE with Lazy Expert Dequantization (SM89)"
type: kernel
architectures: [sm89]
tags: [moe, fp8, block-scale, kernel-fusion]
confidence: source-reported
reproducibility: benchmarked
kernel_types: [moe, fused-kernel]
languages: [python-cpp-extension]
related: [kernel-fused-moe, kernel-fp8-block-scale-gemm]
sources: [exp-kersor-rtx4090-sm89]
performance_claims:
  - gpu: RTX 4090
    dtype: fp8
    shape: "topk=8, experts=32, hidden=7168, intermediate=2048, T=variable"
    metric: speedup
    value: 1.91
    utilization: "compute-bound for active experts"
    source_id: exp-kersor-rtx4090-sm89
blackwell_relevance: "Lazy dequantization pattern applies to any architecture with large expert count and small batch. On SM100, tcgen05 with UE8M0 block scaling would replace the manual dequant; the skip-empty-expert optimization remains valid."
---

# FP8 MoE with Lazy Expert Dequantization (SM89)

## Overview

DeepSeek-V3 style Mixture-of-Experts kernel with FP8 block-scale quantized weights (128×128 weight blocks, 1×128 activation blocks). Implements no-aux routing with grouped expert selection (8 groups × 4 top-k groups × top-8 total) and SwiGLU activation.

The key optimization: **lazy per-expert dequantization** — only dequantize weights for experts that actually receive tokens in the current batch. With small batch sizes (typical in decode), most of the 32 experts are empty, saving ~50% of memory bandwidth.

## Routing: No-Aux DeepSeek-V3 Style

```
Input: routing_logits [T, 256], routing_bias [256]
       (256 global experts, 32 local)

Step 1: Sigmoid scoring with additive bias
  s = sigmoid(routing_logits) + routing_bias

Step 2: Group selection (8 groups × 32 experts/group)
  Per group: sum of top-2 scores → group_score
  Select top-4 groups (TOPK_GROUP=4)

Step 3: Expert selection within kept groups
  Global top-8 (TOP_K=8) from 4×32=128 candidate experts

Step 4: Weight normalization (no aux loss)
  w = s_without_bias * mask / sum(s_without_bias * mask) * routed_scaling_factor
```

## Lazy Dequantization Pattern

```cpp
// CRITICAL OPTIMIZATION: only dequantize weights for non-empty experts
for (int64_t le = 0; le < E_LOCAL; ++le) {
    int64_t ge = local_start + le;

    // Check if ANY token selected this expert
    Tensor sel_mask = (topk_idx == ge).any(1);  // [T] bool
    if (!sel_mask.any().item<bool>()) {
        // SKIP: no dequantization, no GEMM, no accumulation
        // For T=64 with topk=8 and 32 experts: ~75% of experts are empty
        continue;
    }

    // Only now dequantize this expert's weights
    // W13: [2*I, H] = [4096, 7168] FP8 → FP32 with block scales
    Tensor W13_fp32 = gemm1_weights[le].to(kFloat);
    Tensor S13 = gemm1_weights_scale[le];  // [32, 56] = [2I/128, H/128]
    Tensor S13_expanded = repeat_interleave(S13, 128, dim=0);
    S13_expanded = repeat_interleave(S13_expanded, 128, dim=1);
    Tensor W13 = W13_fp32 * S13_expanded;

    // Gather tokens for this expert
    Tensor token_idx = nonzero(sel_mask).squeeze(1);
    Tensor A_e = A.index_select(0, token_idx);  // [Tk, H]

    // GEMM1 → SwiGLU → GEMM2
    Tensor G1 = A_e.matmul(W13.t());           // [Tk, 2I]
    Tensor X1 = G1.narrow(1, 0, I);
    Tensor X2 = G1.narrow(1, I, I);
    Tensor C = at::silu(X2) * X1;              // SwiGLU activation
    Tensor O = C.matmul(W2.t());               // [Tk, H]

    // Weighted accumulation
    Tensor w_tok = weights.index_select(0, token_idx).narrow(1, ge, 1);
    output.index_add_(0, token_idx, O * w_tok);
}
```

## FP8 Block-Scale Dequantization

```
Weight layout: [experts, 2*I, H] FP8 E4M3 (gemm1_weights)
               [experts, H, I]   FP8 E4M3 (gemm2_weights)

Scale layout:  [experts, 2*I/128, H/128] FP32 (per 128×128 block)

Dequant:
  W_fp32 = W_fp8.to(float32) * expand(scale, factor=128, both_dims)

Activation layout: [T, H] FP8 E4M3
                   [H/128, T] FP32 scales (note: transposed!)

Activation dequant:
  A_fp32 = A_fp8.to(float32) * expand(scale.permute(1,0), factor=128, dim=1)
```

## TF32 Tensor Core Acceleration

```cpp
// Enable TF32 for the internal fp32 matmuls
// FP32 accumulation with TF32 inputs: ~1.66x faster than pure FP32
// Mantissa precision: 10 bits (TF32) vs 23 bits (FP32) — sufficient for inference
at::globalContext().setAllowTF32CuBLAS(true);
```

## Performance Model

```
Without lazy dequant (all 32 experts pre-dequantized):
  Memory: 32 × (2*2048*7168 + 7168*2048) × 4 bytes = ~5.5 GB
  Time dominated by dequantization bandwidth

With lazy dequant (avg 8 active experts for topk=8):
  Memory: 8 × same = ~1.4 GB (75% reduction)
  + routing overhead (small: topk/scatter on [T, 256])

Breakeven: lazy wins when active_experts/total_experts < ~0.5
  With topk=8 and T≤128: typically 6-10 active experts out of 32
```

## When to Use

- FP8 MoE inference on SM89 with small-to-medium batch sizes
- DeepSeek-V3 style routing (no-aux, grouped selection)
- When most experts are idle per batch (small T relative to expert count)
- As a baseline for comparison with fused MoE kernels

## Caveats

- **Not a fused kernel**: uses ATen matmul calls (cuBLAS underneath), not a single custom CUDA kernel. The optimization is algorithmic (lazy dequant) not low-level.
- The `repeat_interleave` for scale expansion is memory-inefficient — a fused kernel would apply scales inline during the GEMM.
- `index_select` + `index_add_` create intermediate tensors — a scatter-gather MoE kernel avoids this.
- TF32 introduces ~0.01% numerical noise vs pure FP32 accumulation; acceptable for inference but potentially problematic for training.
- The `.any().item<bool>()` host sync per expert adds latency — batching the check would be faster for large expert counts.
