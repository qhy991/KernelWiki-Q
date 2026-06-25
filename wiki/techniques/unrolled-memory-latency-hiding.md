---
id: technique-unrolled-memory-latency-hiding
title: "Unrolled Load Batching for Memory Latency Hiding"
type: technique
architectures: [sm89, sm90, sm100]
tags: [vectorized-loads, cache-policy, paged-kv-cache]
confidence: source-reported
reproducibility: benchmarked
prerequisites: []
related: [kernel-kersor-mla-decode-sm89, kernel-kersor-gqa-decode-sm89, pattern-memory-bound, technique-vectorized-loads]
sources: [exp-kersor-rtx4090-sm89]
blackwell_relevance: "Latency hiding via outstanding loads is universal. On SM100, TMA descriptors and cp.async.bulk replace manual ld.global.cs, but the principle of maximizing in-flight memory requests remains identical."
---

# Unrolled Load Batching for Memory Latency Hiding

## Overview

For kernels with scattered memory access patterns (e.g., paged KV cache with page_size=1), each token's data resides at a random DRAM location. DRAM access latency is 200-300 cycles, but the memory subsystem can service multiple outstanding requests concurrently. By issuing N independent loads before any synchronization or computation that depends on the results, we allow up to N DRAM requests to overlap — effectively hiding N× the latency.

KerSor experiments on RTX 4090 (SM89) demonstrated that going from 4-token to 8-token unrolling reduced latency by ~15% for MLA decode, with the dominant contribution being reduced sync-per-token overhead (0.25 vs 0.5 syncs/token).

## Mechanism

```
Sequential (high latency):
  load token[0] → wait → compute → load token[1] → wait → compute → ...
  Effective throughput: 1 / (latency + compute_time)

Unrolled N=8 (hidden latency):
  load token[0..7] → wait_all → compute[0..7] → sync
  Effective throughput: 8 / (latency + 8*compute_time)
  ≈ 1/compute_time for latency << 8*compute_time

The more loads in flight, the closer to peak bandwidth.
```

## Implementation Pattern

```cuda
// 8-token unrolled loop (from MLA decode V11)
const int chunk_len8 = (chunk_len >> 3) << 3;  // round to multiple of 8

for (int tok = 0; tok < chunk_len8; tok += 8) {
    // Phase 1: Issue ALL 8 loads (independent, no data dependency)
    const int pi0 = kv_indices[start + tok + 0];
    const int pi1 = kv_indices[start + tok + 1];
    // ... pi2 through pi7 ...

    float k0[4], k1[4], k2[4], k3[4], k4[4], k5[4], k6[4], k7[4];
    LOAD_CS(pi0, k0);  // ld.global.cs.v2.u32 — non-blocking
    LOAD_CS(pi1, k1);  // issues immediately, doesn't wait for pi0
    LOAD_CS(pi2, k2);
    LOAD_CS(pi3, k3);
    LOAD_CS(pi4, k4);
    LOAD_CS(pi5, k5);
    LOAD_CS(pi6, k6);
    LOAD_CS(pi7, k7);  // 8 loads in-flight simultaneously

    // Phase 2: All loads have completed by here (latency amortized)
    // Compute 8 partial results using the loaded data
    float d0 = dot(q, k0); float d1 = dot(q, k1); ...

    // Phase 3: Cross-thread reduction (requires sync)
    warp_reduce_sum(d0); ... warp_reduce_sum(d7);
    __syncthreads();  // sync #1

    // Phase 4: Use reduced values (softmax update)
    SOFTMAX_UPDATE(d0, k0); ... SOFTMAX_UPDATE(d7, k7);
    __syncthreads();  // sync #2
}
// Total: 2 syncs per 8 tokens = 0.25 syncs/token
```

## Tail Handling

```cuda
// After the unrolled main loop, handle remainder via power-of-2 decomposition
// 4-token, 2-token, 1-token fallbacks cover all possible remainders

if (tok + 4 <= chunk_len) {
    // 4-token block (same pattern, fewer registers)
    LOAD_CS(pi0, k0); LOAD_CS(pi1, k1); LOAD_CS(pi2, k2); LOAD_CS(pi3, k3);
    // ... compute ...
    tok += 4;
}
if (tok + 2 <= chunk_len) {
    LOAD_CS(pi0, k0); LOAD_CS(pi1, k1);
    // ...
    tok += 2;
}
if (tok < chunk_len) {
    LOAD_CS(pi0, k0);
    // ...
}
```

## Register Pressure Trade-off

```
Unroll factor:  Live registers per token:  Total additional regs:  Blocks/SM (SM89):
    4-token         4 floats                    16                    10 blocks
    8-token         4 floats                    32 (+16)               8 blocks
   16-token         4 floats                    48 (+32)               6 blocks

8-token is the sweet spot on SM89:
  - 20% occupancy reduction vs 4-token
  - 50% sync reduction (0.25 vs 0.5 per token)
  - 2× more outstanding loads saturating DRAM
  - Net: 15% latency improvement (memory-bound dominates occupancy)
```

## Cache Hints for Scattered Loads

```cuda
// When loading scattered pages that won't be reused, use streaming hints:

// ld.global.cs — "cache streaming" (L1 bypass, L2 streaming sector)
// Best for: paged KV cache where each page is visited once per sequence
asm volatile("ld.global.cs.v2.u32 {%0,%1},[%2];"
             :"=r"(v.x),"=r"(v.y):"l"(ptr));

// ld.global.cg — "cache global" (L1 bypass, L2 global)
// Best for: data that may be reused across CTAs but not within
asm volatile("ld.global.cg.v2.u32 {%0,%1},[%2];"
             :"=r"(v.x),"=r"(v.y):"l"(ptr));

// Key insight from KerSor experiments:
// .cs for V cache (V reads often use DIFFERENT pages than K reads)
// .cg for K cache (K pages may be revisited by later split-K chunks)
```

## When to Use

- **Scattered access patterns**: paged KV cache (page_size=1), hash-indexed lookups, indirect indexed access
- **Memory-bound kernels**: where DRAM latency (not compute or SMEM BW) is the bottleneck
- **Split-K attention decode**: each CTA processes random subset of KV pages
- **Large working sets**: where L1/L2 cache hit rates are low (KV cache >> cache capacity)

## Caveats

- Unrolling increases register pressure: may reduce occupancy to the point where latency hiding regresses. Profile to find the optimal unroll factor.
- On SM90/SM100 with TMA, the hardware handles batched loads more efficiently than manual ld.global.cs — use cp.async.bulk or TMA multicast instead.
- The technique is most effective when loads are truly independent and to different DRAM rows/banks. If loads alias to the same bank, parallelism is limited by bank conflicts.
- Sync reduction matters most at high L (long KV sequences); for L < 32, the small-L SMEM path avoids syncs entirely.
