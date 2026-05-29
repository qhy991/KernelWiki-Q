---
id: exp-o-20260508-160201-benchmark-timing-hygiene
title: Speedup values are unstable or suspiciously high due to inconsistent benchmark
  t
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

Speedup values are unstable or suspiciously high due to inconsistent benchmark timing protocol.

## Key Lessons

- A stable measurement protocol is required before claiming optimization wins.
- When gain is small, robustness metrics matter more than peak value.
