---
id: exp-i-20260519-0001-gqa-paged-decode-architecture
title: 'GQA paged decode attention: architecture, kernel design, and correct run()
  signature'
experience_type: implementation
source_category: agent-experiment
architectures:
- sm90
tags:
- attention
kernel_types:
- attention
languages:
- cuda-cpp
captured_at: '2026-05-19'
confidence: inferred
reproducibility: concept
---

## Challenge

Implement a GQA paged decode attention kernel for FlashInfer-Bench from the TODO template. The kernel must compile with nvcc/g++, pass correctness validation, and produce correct output tensors.

## Solution

One CUDA block per (batch, qo_head) pair. Each block uses head_dim threads (128). The kernel iterates over pages assigned to the batch via kv_indptr/kv_indices, loads one k/v token per page, computes dot product with tree reduction, and runs online softmax with exponential rescaling.

## Key Lessons

- run() must return std::vector<torch::Tensor> when there are multiple outputs with DPS=false, not void or a single tensor
- Include <ATen/cuda/CUDAContext.h> in main.cpp for at::cuda::getCurrentCUDAStream()
- Use at::cuda::getCurrentCUDAStream() not c10::cuda::getCurrentCUDAStream()
- kernel.h launcher must use void* parameters (not __nv_bfloat16*) because the .h is included by main.cpp which is compiled by g++
- Cast void* to bf16* inside kernel.cu with static_cast<const bf16*>(ptr)
- kv_indptr and kv_indices are torch::Tensor of type int32 — use .data_ptr<int32_t>() to get the pointer
- Page_size=1 for decode means each KV cache page has exactly 1 token
- Initialize m = -INFINITY, d = 0.0f before page loop, return 0 output and -INFINITY lse if num_pages == 0
- Include <cuda_bf16.h> in kernel.cu for __nv_bfloat16 and __float2bfloat16 / __bfloat162float conversions
