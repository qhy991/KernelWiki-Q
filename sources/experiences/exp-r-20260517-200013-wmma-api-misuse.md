---
id: exp-r-20260517-200013-wmma-api-misuse
title: 'WMMA API misuse: tile size, fragment types, and memory layout'
experience_type: repair
source_category: agent-experiment
architectures:
- sm90
tags:
- gemm
- tile-scheduling
- fine-grained-quantization
kernel_types:
- gemm
languages:
- cuda-cpp
captured_at: '2026-05-17'
confidence: inferred
reproducibility: concept
techniques:
- tile-scheduling
- fine-grained-quantization
impl_family: custom_cuda
---

## Key Lessons

- INT8 WMMA accumulator fragment must be int32_t, NOT float. The API enforces this at compile time.
- WMMA tile for INT8 is always 16x16x16 — M/N/K tile dimensions must be multiples of 16.
- load_matrix_sync(ptr, stride): stride is the leading dimension in ELEMENTS, not bytes.
- store_matrix_sync: use row_major layout with stride = leading dimension in elements.
- Fill the accumulator fragment with zeros before accumulation: wmma::fill_fragment(c_frag, 0).
- For large tiles (TILE_M > 16), iterate over 16-element sub-blocks with multiple warps.
- Consider whether standard tiled matmul with vectorized int4 loads might be simpler and faster than WMMA, especially for small M.
- On sm_89 (Ada Lovelace), WMMA is supported but the newer WGMMA (warp group MMA) instructions may offer better performance — check if available.
