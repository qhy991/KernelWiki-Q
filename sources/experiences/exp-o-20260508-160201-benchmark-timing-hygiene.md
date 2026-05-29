---
id: exp-o-20260508-160201-benchmark-timing-hygiene
title: exp-o-20260508-160201-benchmark-timing-hygiene
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

## Key Lessons

- A stable measurement protocol is required before claiming optimization wins.
- When gain is small, robustness metrics matter more than peak value.
