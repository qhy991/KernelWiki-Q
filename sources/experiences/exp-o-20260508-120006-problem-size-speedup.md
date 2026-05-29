---
id: exp-o-20260508-120006-problem-size-speedup
title: What speedup can be expected for different GEMM problem sizes? Setting realistic
experience_type: optimization
source_category: agent-experiment
architectures:
- sm90
tags:
- gemm
kernel_types:
- gemm
languages:
- cuda-cpp
captured_at: '2026-05-08'
confidence: inferred
reproducibility: concept
impl_family: all
---

## Challenge

What speedup can be expected for different GEMM problem sizes? Setting realistic expectations helps avoid wasted optimization steps on problems already near-optimal.

## Key Lessons

- For n>=32768: accept minimal speedup, focus on getting code to compile and pass correctness.
- For m=968,n=256: expect 3-4.5x, worth investing optimization effort.
- INT8 offers ~37% higher speedup than BF16 when it works, but 2.2x lower pass rate.
