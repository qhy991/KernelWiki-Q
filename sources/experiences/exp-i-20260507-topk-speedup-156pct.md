---
id: exp-i-20260507-topk-speedup-156pct
title: 'TK_05 (topk) is the only kernel to achieve >1x speedup: 1.5664x with 0.014ms
  latency vs 0.022ms baseline'
experience_type: implementation
source_category: agent-experiment
architectures:
- sm90
tags:
- topk
kernel_types:
- topk
languages:
- cuda-cpp
captured_at: '2026-05-07'
confidence: experimental
reproducibility: concept
---

TK_05 (topk, fp32_top_k_sampling_llama3_8b_k8_ne0160) achieved 1.5664x speedup - the only kernel in the 20260506-07 batch to beat baseline. This was a 24.9 minute run with 65 steps, 101 LLM calls.

## Challenge

15 of 17 R1 tasks were flash_attention variants, all achieving <1x speedup. TK_05 was the sole non-flash_attention kernel and the only performance success.

## Solution

topk is a sort/selection problem - no matrix multiplications needed. The kernel likely used warp-level primitives (e.g., __shfl, warp reduce) or shared memory sorting networks, which are effective for small vocab sizes (160).

## Key Lessons

- topk/sorting kernels are good candidates for KernelEval because they don't require Tensor Cores and can achieve >1x with warp intrinsics + shared memory
- small vocab size (160) means the entire probability distribution fits in registers, enabling efficient in-register sort
- The problem is memory-bound (roofline: memory_bound), confirming the kernel is efficiently using memory bandwidth rather than stalling on compute
- bandwidth_utilization=1.2% for topk vs 0.05% for flash_attention shows the difference between an efficient and inefficient kernel
- topk with k=8 and vocab=160 is a fundamentally different problem from flash_attention - simpler computational structure enables success
- The KernelEval benchmark has a mix of kernel types - flash_attention is consistently the hardest due to Tensor Core requirement
