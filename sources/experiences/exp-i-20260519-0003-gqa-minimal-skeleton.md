---
id: exp-i-20260519-0003-gqa-minimal-skeleton
title: 'GQA paged decode: minimal compile-able skeleton for new implementations'
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

When starting from a TODO template, the agent needs a minimal but complete skeleton that compiles and runs. This provides the correct file structure and function signatures for a GQA paged decode kernel.

## Solution

Provide a minimal but complete 3-file skeleton that compiles successfully. The kernel does naive GQA attention so the agent can verify the build pipeline works before iterating on performance.

## Key Lessons

- Start with the 3-file structure (main.cpp + kernel.h + kernel.cu) — never try to put CUDA code directly in main.cpp
- The run() function must extract num_qo_heads and head_dim from q.sizes(), num_kv_heads and page_size from k_cache.sizes()
- Allocate output as torch::empty({batch_size, num_qo_heads, head_dim}, torch::TensorOptions().dtype(torch::kBFloat16).device(q.device()))
- Allocate lse as torch::empty({batch_size, num_qo_heads}, torch::TensorOptions().dtype(torch::kFloat32).device(q.device()))
- Pass void* pointers to the launcher (via .data_ptr()), cast to __nv_bfloat16* inside kernel.cu with static_cast
- kv_indptr and kv_indices are int32 tensors — use .data_ptr<int32_t>()
- The launcher computes grid_size = batch_size * num_qo_heads and block_size = head_dim
- Shared memory: size_t shmem = head_dim * sizeof(float)
- LSE output: use logf(d) not log2f(d) when computing lse = m + logf(d)
