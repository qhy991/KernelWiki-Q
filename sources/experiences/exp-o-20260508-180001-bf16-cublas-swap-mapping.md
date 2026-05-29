---
id: exp-o-20260508-180001-bf16-cublas-swap-mapping
title: 'Gemm optimization: BF16 and INT8 use the EXACT SAME swap mapping: m=N, n=M,
  A_p'
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
captured_at: '2026-05-09'
confidence: inferred
reproducibility: concept
impl_family: cublas
---

## Key Lessons

- BF16 and INT8 use the EXACT SAME swap mapping: m=N, n=M, A_ptr=B, B_ptr=A.
- Non-swap mapping (m=M, n=N) is ALWAYS wrong for both BF16 and INT8.
- Previous BF16 'verified_pass' with non-swap was a false positive in the verification system.
- Always verify parameter mappings by running the benchmark directly, not trusting historical verdicts.
