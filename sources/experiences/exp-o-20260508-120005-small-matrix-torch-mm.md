---
id: exp-o-20260508-120005-small-matrix-torch-mm
title: exp-o-20260508-120005-small-matrix-torch-mm
experience_type: optimization
source_category: agent-experiment
architectures:
- sm90
tags:
- gemm
- fine-grained-quantization
kernel_types:
- gemm
languages:
- python
captured_at: '2026-05-08'
confidence: inferred
reproducibility: concept
techniques:
- fine-grained-quantization
impl_family: pytorch
---

## Key Lessons

- For small matrices (m<=50, n<=256), at::mm_out is simpler and equally fast.
- at::mm_out avoids all row/column-major parameter mapping risks.
- For large matrices, direct cublasGemmEx remains preferred for maximum performance.
