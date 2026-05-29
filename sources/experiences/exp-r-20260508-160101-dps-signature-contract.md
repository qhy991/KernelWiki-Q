---
id: exp-r-20260508-160101-dps-signature-contract
title: 'DPS entrypoint contract mismatch causes compile-time or runtime binding failure '
experience_type: repair
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
reproducibility: snippet
impl_family: all
---

## Challenge

DPS entrypoint contract mismatch causes compile-time or runtime binding failure even when kernel logic is correct.

## Key Lessons

- Treat entrypoint contract as an executable gate before any performance tuning.
- Never optimize around a broken binding signature.
