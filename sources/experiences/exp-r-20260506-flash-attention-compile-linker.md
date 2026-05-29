---
id: exp-r-20260506-flash-attention-compile-linker
title: 'Flash attention CUDA kernel linker error: undefined symbol flash_attn_kernel'
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
captured_at: '2026-05-06'
confidence: inferred
reproducibility: snippet
---

LLM generates kernel code with conflicting __global__ and extern C wrapper using same function name, causing linker errors

### Symptoms

- `Linker error: undefined symbol flash_attn_kernel`
- `Kernel source contains conflicting linkage: __global__ and extern C wrapper with same function name`
- `nvcc compilation succeeds but linking with the test harness fails`

## Solution

Use distinct names for the CUDA kernel and the C-linkage wrapper. The kernel should be __global__ with a descriptive name (e.g., flash_attn_cuda_kernel), and the exported function should be a host-callable wrapper in extern C that launches the kernel.

### Implementation

```cuda
1. Define __global__ void flash_attn_cuda_kernel(...) with the actual CUDA computation
2. Wrap with extern 'C' { void flash_attention(...) { flash_attn_cuda_kernel<<<grid, block, smem>>>(...); cudaDeviceSynchronize(); } }
3. The exported function name must match exactly what the KernelEval test harness expects
4. Use cudaMemcpy/cudaMalloc for device memory management inside the wrapper
5. Handle error checking with cudaGetLastError() after kernel launch
```

## Key Lessons

- Never use the same function name for both __global__ kernel and extern C wrapper. The linker will fail with undefined symbol.
- The exported function name must exactly match what the KernelEval harness expects. Check definition JSON for the expected name.
- Always call cudaDeviceSynchronize() after kernel launch in the host wrapper to ensure completion before returning.
- Allocate device memory (cudaMalloc) and copy input data (cudaMemcpy H2D) inside the wrapper, then copy result back (cudaMemcpy D2H).
- Check for CUDA errors after launch: cudaError_t err = cudaGetLastError(); if (err != cudaSuccess) handle error.
- KernelEval compiles the kernel.cu with specific nvcc flags from the definition. Do not assume specific CUDA architectures or include non-standard headers.
