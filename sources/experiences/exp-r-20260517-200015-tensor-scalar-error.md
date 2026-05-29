---
id: exp-r-20260517-200015-tensor-scalar-error
title: Tensor with N elements cannot be converted to Scalar
experience_type: repair
source_category: agent-experiment
architectures:
- sm90
tags:
- gemm
- fine-grained-quantization
kernel_types:
- gemm
languages:
- cuda-cpp
captured_at: '2026-05-17'
confidence: inferred
reproducibility: concept
techniques:
- fine-grained-quantization
impl_family: custom_cuda
---

## Key Lessons

- Use tensor.size(0), tensor.size(1) etc. to get tensor dimensions in C++/CUDA code.
- Use tensor.numel() to check total element count, not .item().
- In main.cpp: int m = a.size(0) works; int m = a.item<int>() does NOT for multi-element tensors.
- Output tensors must match exactly the shapes declared in definition.json.
- If the error stack trace points to test.py, focus debugging on the kernel's output tensor shapes, not the test code.
- Add TORCH_CHECK assertions in run() to validate input and output tensor shapes early.
