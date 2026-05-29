---
id: exp-r-20260528-113600-fp16-wmma-store-matrix-sync-mismatch
title: FP16 WMMA store_matrix_sync type/layout mismatch
experience_type: repair
source_category: agent-experiment
architectures:
- sm90
tags:
- gemm
kernel_types:
- gemm
languages:
- cuda-cpp
captured_at: '2026-05-28'
confidence: inferred
reproducibility: snippet
impl_family: custom_cuda_wmma
---

WMMA accumulator<float> fragment was stored to half* destination directly, causing compilation failure in round 5.

## Challenge

Compilation failed with store_matrix_sync overload mismatch and layout symbol issues.

### Symptoms

- `error: type name is not allowed`
- `error: no instance of overloaded function "store_matrix_sync" matches the argument list`
- `accumulator fragment type is float but destination pointer is half*`
- `row_major symbol not fully qualified in strict compile context`

## Solution

For accumulator<float> fragments, store first to float staging buffer, then convert elementwise to half when writing final output. Use fully qualified enum names, e.g. nvcuda::wmma::mem_row_major.

### Implementation

```cuda
// Correct pattern
nvcuda::wmma::fragment<nvcuda::wmma::accumulator,16,16,16,float> acc;
float tmp[16 * 16];
nvcuda::wmma::store_matrix_sync(tmp, acc, 16, nvcuda::wmma::mem_row_major);
for (int i = 0; i < 16 * 16; ++i) {
    out_half[i] = __float2half_rn(tmp[i]);
}
```

## Key Lessons

- WMMA accumulator<float> cannot be directly stored to half* via store_matrix_sync.
- Always align fragment type, store destination type, and layout enum.
- In strict build environments, use fully qualified nvcuda::wmma layout symbols.
