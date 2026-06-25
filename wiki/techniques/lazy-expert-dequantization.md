---
id: technique-lazy-expert-dequantization
title: "Lazy Per-Expert Dequantization for MoE"
type: technique
architectures: [sm89, sm90, sm100]
tags: [moe, fp8, block-scale]
confidence: source-reported
reproducibility: benchmarked
prerequisites: []
related: [kernel-kersor-moe-fp8-lazy-dequant-sm89, kernel-fused-moe, technique-fine-grained-quantization]
sources: [exp-kersor-rtx4090-sm89]
blackwell_relevance: "The lazy-evaluation principle applies on any architecture. On SM100, tcgen05 with native block-scale handles dequant in hardware, but expert skipping (zero-token detection) remains a pure software optimization independent of the MMA unit."
---

# Lazy Per-Expert Dequantization for MoE

## Overview

In Mixture-of-Experts (MoE) models with FP8 quantized weights, the naive approach dequantizes all experts' weights upfront before routing. For small batch sizes (typical in decode), the routing selects only a fraction of experts — meaning most of the dequantization bandwidth is wasted on experts that receive zero tokens.

Lazy dequantization defers the expensive weight conversion until after routing confirms that an expert has at least one active token. On RTX 4090 with DeepSeek-V3's 32-expert layout and top-k=8, this typically saves 70-80% of dequantization bandwidth.

## Naive vs Lazy Approach

```
Naive (upfront dequant):
  1. Dequantize ALL 32 experts: W_fp8 → W_fp32 (32 × 2×2048×7168 × 4B = 3.7 GB writes)
  2. Route: determine which experts get tokens
  3. Compute: GEMM only for active experts (8 out of 32)
  Wasted: 24/32 = 75% of dequantization bandwidth

Lazy (on-demand dequant):
  1. Route: determine which experts get tokens
  2. For each expert with ≥1 token:
     a. Dequantize THIS expert only
     b. GEMM (this expert's tokens) × (dequantized weights)
     c. Accumulate weighted output
  Saved: only 8/32 experts dequantized = 75% bandwidth savings
```

## Implementation

```cpp
// FP8 block-scale dequantization (128×128 blocks)
// Only called for experts with active tokens

for (int64_t le = 0; le < E_LOCAL; ++le) {
    int64_t ge = local_start + le;

    // SKIP CHECK: does this expert receive any tokens?
    Tensor sel_mask = (topk_idx == ge).any(dim=1);  // [T] bool
    if (!sel_mask.any().item<bool>()) {
        continue;  // SKIP: no dequant, no GEMM, no accumulate
    }

    // LAZY DEQUANT: only this expert's weights
    Tensor W_fp32 = weights_fp8[le].to(kFloat);       // [rows, cols] fp8→fp32
    Tensor scale  = weights_scale[le];                 // [rows/128, cols/128]
    Tensor scale_expanded = repeat_interleave(scale, 128, dim=0);
    scale_expanded = repeat_interleave(scale_expanded, 128, dim=1);
    Tensor W = W_fp32 * scale_expanded;                // dequantized fp32

    // COMPUTE: only active tokens
    Tensor tokens = A.index_select(0, nonzero(sel_mask).squeeze());
    Tensor output = tokens.matmul(W.t());
    // ... accumulate ...
}
```

## When It Wins: Occupancy Analysis

```
Expected active experts per batch:
  P(expert active) = 1 - (1 - topk/total_experts)^T

  topk=8, experts=32:
    T=1:   P ≈ 0.25 → 8 active    (savings: 75%)
    T=16:  P ≈ 0.97 → 31 active   (savings: 3%)
    T=64:  P ≈ 1.00 → all active  (savings: 0%)

  topk=8, experts=256 (global routing):
    T=1:   P ≈ 0.03 → 8 active    (savings: 97%)
    T=64:  P ≈ 0.86 → 220 active  (savings: 14%)
    T=256: P ≈ 0.99 → all active  (savings: ~0%)

Breakeven: lazy wins when expected_active/total < cost_of_skip_check
  Skip check cost ≈ 1 topk comparison + 1 any() → negligible
  → lazy always wins (or ties) for decode workloads
```

## Limitations and Fused Alternatives

```
Lazy dequantization is an algorithmic optimization, not a kernel-level one:
  ✓ Saves memory bandwidth on expert weight loading
  ✗ Still creates intermediate fp32 tensors (memory allocation)
  ✗ Each expert's GEMM is a separate cuBLAS call (launch overhead)
  ✗ host-device sync per expert (.any().item<bool>())

For production: fused MoE kernels (vLLM/SGLang style) are superior:
  - Grouped-GEMM: all active experts in one launch
  - Inline dequant: apply block scales inside the MMA loop
  - No intermediate tensors: stream directly from FP8 → accumulator

Lazy dequant is most useful as:
  1. A correctness reference for fused kernel development
  2. A quick optimization when custom kernel development isn't possible
  3. The baseline ATen-level approach before investing in kernel fusion
```

## Combining with TF32

```cpp
// For fp32 matmuls on SM89: enable TF32 tensor cores
// 19-bit FP32 → 10-bit TF32 mantissa (acceptable for inference)
// ~1.66x throughput increase with negligible accuracy loss
at::globalContext().setAllowTF32CuBLAS(true);

// Combined effect: lazy dequant + TF32
// = (save 75% BW) × (1.66x compute throughput)
// = effective ~3x speedup over naive fp32 approach
```

## When to Use

- **Decode-phase MoE inference**: batch_size small relative to expert count
- **FP8 models with block-scale quantization**: where dequant is expensive
- **Rapid prototyping**: when custom MoE kernels aren't available for the architecture
- **SM89 specifically**: where no native FP8 block-scale MoE kernel exists (unlike SM90/SM100)

## Caveats

- Host-device synchronization (`.any().item<bool>()`) adds latency per expert — batch the check for large expert counts
- Memory allocation for dequantized weights (per expert) may trigger torch allocator overhead
- The `repeat_interleave` scale expansion is O(rows × cols) — a fused kernel applies scales with O(1) extra memory
- Not compatible with CUDA graphs (host-side branch per expert prevents graph capture)
- For training (backward pass), all experts need gradients regardless of activity — lazy dequant only helps forward
