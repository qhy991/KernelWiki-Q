---
id: doc-context-hub-wmma-patterns
title: "WMMA Kernel Patterns"
url: https://github.com/anthropics/context-hub/tree/main/content/cuda/docs/wmma-kernel-patterns
source_category: official-doc
architectures: [sm100, sm90, sm80]
tags: [pipeline-stages, shared-memory-optimization]
retrieved_at: 2026-06-01
---

# WMMA Kernel Patterns

## Overview

Practical implementation patterns for `nvcuda::wmma` including warp-to-tile mapping, fragment loading rules, accumulator handling, and common failure modes.

## Warp-To-Tile Mapping

One warp per output tile: loads A/B tile fragments, keeps accumulator fragment, stores results. Scale by assigning multiple warps per block and iterating over K tiles.

## Minimal Pattern Skeleton

```cpp
using namespace nvcuda;
wmma::fragment<wmma::accumulator, 16, 16, 16, float> c_frag;
wmma::fill_fragment(c_frag, 0.0f);

for (int k0 = 0; k0 < K; k0 += 16) {
    wmma::fragment<wmma::matrix_a, 16, 16, 16, half, wmma::row_major> a_frag;
    wmma::fragment<wmma::matrix_b, 16, 16, 16, half, wmma::col_major> b_frag;
    wmma::load_matrix_sync(a_frag, a_ptr, lda);
    wmma::load_matrix_sync(b_frag, b_ptr, ldb);
    wmma::mma_sync(c_frag, a_frag, b_frag, c_frag);
}
wmma::store_matrix_sync(c_ptr, c_frag, ldc, wmma::mem_row_major);
```

## Critical Correctness Rules

- All lanes in the warp must execute WMMA calls with consistent arguments
- Layout and leading-dimension parameters must match fragment template expectations
- Pointer alignment and stride constraints must satisfy API requirements
- Fragment internal lane mapping is opaque; do not index with custom assumptions

## High-Value Performance Patterns

- Stage A/B tiles in shared memory to reduce uncoalesced global traffic
- Use double-buffered tile staging when K is large
- Keep one accumulator fragment alive across K-loop iterations
- Control register pressure before adding heavy unrolling

## Common Failure Modes

- Wrong `row_major`/`col_major` choice for multiplicands
- Incorrect `lda`/`ldb`/`ldc` in element units
- Partial-warp execution due to guard branches around WMMA calls
- Correct output with low speed because data movement dominates MMA throughput

## Related KernelWiki Pages

- [technique-pipeline-stages](../../wiki/techniques/pipeline-stages.md)
- [technique-double-buffering](../../wiki/techniques/double-buffering.md)
- [hw-tcgen05-mma](../../wiki/hardware/tcgen05-mma.md)
- [migration-wgmma-to-tcgen05](../../wiki/migration/wgmma-to-tcgen05.md)
