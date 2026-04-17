---
id: blog-amandeep-nvfp4
title: "Twelve Attempts at an FP4 Kernel"
author: Amandeep Singh
url: https://amandeepsp.github.io/blog/nvfp4-blackwell-gemv/
source_category: benchmark-blog
architectures: [sm100, sm100a]
tags: [nvfp4, gemv, batched-gemv, vectorized-loads, register-budgeting]
retrieved_at: 2026-04-16
---

## Summary

12 approaches to NVFP4 Batched GEMV, final result ~26.7μs (3.1x off speed-of-light).

## Key Lesson
"The single most important thing could have been running Nsight Compute after attempt 7 to confirm memory-bound behavior."

## Findings
- Split-K ineffective for memory-bound kernels
- Wider loads without proper unpacking don't help
- ILP has diminishing returns for memory-bound workloads
- Profiling early saves wasted optimization effort
