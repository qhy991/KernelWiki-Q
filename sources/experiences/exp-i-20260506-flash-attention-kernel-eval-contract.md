---
id: exp-i-20260506-flash-attention-kernel-eval-contract
title: KernelEval flash_attention CUDA kernel implementation contract
experience_type: implementation
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
captured_at: '2026-05-06'
confidence: inferred
reproducibility: concept
---

KernelEval flash_attention tasks require a specific function signature and compilation contract. The kernel must export a C-linkage wrapper with exact signature matching the test harness expectation.

## Challenge

14 consecutive experiments (FA_01-FA_18) showed systematic compilation failures because generated CUDA kernels did not match the KernelEval test harness contract. The harness expects a specific C-linkage function with typed parameters for Q, K, V tensors, dimensions, and output pointer. Generated kernels frequently use wrong signatures, miss extern C wrappers, or include incompatible headers.

## Solution

Follow the KernelEval definition JSON exactly for the function signature

1. Read the task definition JSON from the path provided in round_assignment_lease.definition_path
2. Extract the exact function signature, parameter types, and return type
3. Wrap the CUDA kernel in extern 'C' { ... } block
4. Ensure the kernel.cu file only contains the required function, no main(), no test harness
5. Use the keval validation command from the definition to test compilation
6. Common signature pattern: void flash_attention(float* out, const float* q, const float* k, const float* v, int batch, int heads, int seq_len, int head_dim, int cache_size)
7. Cache size variants (512/4096/8192) affect only the tensor dimensions, not the kernel logic

## Key Lessons

- Always read the KernelEval task definition JSON before writing any kernel code. It contains the exact expected function signature, parameter types, and compilation flags.
- The test harness expects a C-linkage host function, NOT a __global__ CUDA kernel directly. Wrap with extern 'C' and provide a host-callable entry point that internally launches the kernel.
- Do NOT include main() in kernel.cu. The KernelEval harness provides its own test driver.
- Quantization type (f16/q4_0/q8_0) determines the data type of Q/K/V tensors. f16 uses half, q4_0 and q8_0 may use float with dequantization or direct quantized operations.
- Cache size parameter (512/4096/8192) affects the KV cache tensor layout but not the flash attention algorithm itself. Adjust memory access patterns accordingly.
- Use the keval validation command (from canonical_verification in round_assignment_lease) to test compilation early and often, before attempting full optimization.
