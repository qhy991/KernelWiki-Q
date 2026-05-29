---
id: exp-r-20260506-180000-cpp-pytorch-named-params
title: C++ PyTorch API named parameter error in CUDA kernels
experience_type: repair
source_category: agent-experiment
architectures:
- sm90
tags:
- attention
kernel_types:
- attention
languages:
- cuda-cpp
captured_at: '2026-05-06'
confidence: inferred
reproducibility: concept
---

## Key Lessons

- C++ PyTorch API uses positional arguments only; Python-style named parameters like dim= are not valid C++
- Common affected methods: sum(), max(), min(), argmax(), softmax(), log_softmax(), norm(), mean(), var(), std()
- Always use C++ API signatures: tensor.sum(dim_value, keepdim_value) not tensor.sum(dim=X, keepdim=Y)
- The keepdim parameter in C++ is a bool, not keyword argument: use .sum(-1, true) not .sum(dim=-1, keepdim=True)
