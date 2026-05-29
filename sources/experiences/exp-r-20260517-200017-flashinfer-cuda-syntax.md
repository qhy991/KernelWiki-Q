---
id: exp-r-20260517-200017-flashinfer-cuda-syntax
title: FlashInfer-Bench GQA paged decode kernel compilation errors
experience_type: repair
source_category: agent-experiment
architectures:
- sm90
tags:
- attention
- fine-grained-quantization
kernel_types:
- attention
languages:
- cuda-cpp
captured_at: '2026-05-17'
confidence: inferred
reproducibility: concept
techniques:
- fine-grained-quantization
impl_family: custom_cuda
---

## Key Lessons

- For Float8 (FP8) types: include <cuda_fp8.h>, use __nv_fp8_e4m3fn type, compile with -arch=sm_89.
- Paged attention: page_table is int32_t* flat array. Access: page_id = page_table[page_idx]; ptr = k_cache + page_id * page_size * num_heads * head_dim + ...
- CUDAStream to cudaStream_t: use .stream() method on the CUDAStream object. Never cast.
- When a problem has 10+ input tensors, list them in definition.json order in run() signature. Triple-check.
- KV cache layout: [num_pages, page_size, num_kv_heads, head_dim] or [num_pages, num_kv_heads, page_size, head_dim] — check definition.json or baseline.
- len_indptr[batch+1] gives the range of kv_indices for batch element b: kv_indices[len_indptr[b]:len_indptr[b+1]].
