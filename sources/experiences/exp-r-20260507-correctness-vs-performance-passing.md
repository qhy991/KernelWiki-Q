---
id: exp-r-20260507-correctness-vs-performance-passing
title: KernelEval verification_status=passed does not guarantee speedup > 1.0x - FA_12
  passed with 0.7395x speedup
experience_type: repair
source_category: agent-experiment
architectures:
- sm90
tags:
- attention
- flash-attention
kernel_types:
- attention
- flash-attention
languages:
- cuda-cpp
captured_at: '2026-05-07'
confidence: experimental
reproducibility: concept
---

FA_12 (20260507_043742) passed verification (verification_status=verified_pass) but achieved only 0.7395x speedup (42% slower than baseline). All 9 'passed' tasks in the batch had speedup < 1.0x except TK_05 (1.5664x). The KernelEval verification confirms correctness, not performance.

## Challenge

All 9 'passed' tasks were marked as successful by KernelEval verification, but 8/9 had speedup < 1.0x (i.e., slower than baseline). FA_12 was particularly misleading because it had verification_status=verified_pass but performance_ratio=0.58 (meaning 42% slower than baseline). The difference between verification_pass and meaningful_speedup is not surfaced to the experiment runner.

## Solution

KernelEval verification only checks correctness (nmse < threshold). Performance benchmarking is separate. The experiment summary should distinguish: (1) verification_pass (correctness OK), (2) performance_pass (speedup > threshold, e.g., 0.8x).

## Key Lessons

- verification_status=passed in KernelEval means ONLY correctness (nmse < threshold), NOT that the kernel is competitive with baseline
- 8/9 'passed' tasks had speedup < 0.05x (essentially baseline performance not achieved)
- FA_12 is the most misleading case: verified_pass but 42% slower than baseline - should be flagged as 'passed_below_threshold'
- The experience pipeline captures 'passed' tasks indiscriminately, including those with terrible speedup - this pollutes future RAG retrieval
- When selecting 'successful' experiences for RAG, filter on speedup > 1.0x OR explicitly separate correctness-success from performance-success
- All flash_attention kernels pass correctness (scalar implementation works) but fail performance - the KernelEval contract only requires correctness
- For optimization-oriented tasks, the optimization target (speedup) should be checked before marking a task as 'successful'
