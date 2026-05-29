---
id: exp-r-20260517-200003-dps-signature-mismatch
title: 'DPS signature mismatch: run() must be void with output tensors at end'
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
captured_at: '2026-05-17'
confidence: inferred
reproducibility: concept
impl_family: custom_cuda
---

## Key Lessons

- When destination_passing_style=true in definition.json, run() must be: void run(all_inputs..., all_outputs...).
- Read the definition.json to determine the exact parameter order: inputs array first, then outputs array.
- Both kernel.h declaration and main.cpp definition must have the same void run(...) signature.
- Output tensors are pre-allocated by the framework; run() must write results into them, not return new tensors.
- The number of output parameters matches the length of definition.json's outputs array.
- If there are multiple output tensors, all must appear after all inputs in the run() parameter list.
