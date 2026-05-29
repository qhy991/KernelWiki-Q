---
id: exp-i-20260519-0002-gqa-compilation-checklist
title: 'GQA paged decode: compilation checklist for CUDA kernels'
experience_type: implementation
source_category: agent-experiment
architectures:
- sm90
tags:
- attention
kernel_types:
- attention
languages:
- cuda-cpp
captured_at: '2026-05-19'
confidence: inferred
reproducibility: concept
---

## Challenge

Common compilation errors when writing GQA paged decode CUDA kernels for SOL-ExecBench. The build system compiles .cu with nvcc and .cpp with g++, with strict separation of CUDA and host code.

## Solution

Follow a strict file separation pattern: kernel.h declares the launcher with void* pointers and cudaStream_t, kernel.cu contains all CUDA kernel code and the launcher implementation, main.cpp contains host setup and calls the launcher via kernel.h.

## Key Lessons

- Check 1: main.cpp has NO __nv_bfloat16, cudaStream_t, <<<>>>, blockIdx, threadIdx — these are all in kernel.cu
- Check 2: kernel.h uses void* for bf16 pointers and includes <cuda_runtime.h>
- Check 3: kernel.cu includes <cuda_bf16.h> and uses static_cast<const bf16*>(void_ptr) to convert launcher args
- Check 4: at::cuda::getCurrentCUDAStream() is used (not c10::cuda)
- Check 5: run() returns std::vector<torch::Tensor> with {output, lse} when DPS=false with 2 outputs
- Check 6: kv_indptr.data_ptr<int32_t>() and kv_indices.data_ptr<int32_t>() are used (not just data_ptr())
- Check 7: After writing sources via sol_execbench_update_sources, read back key lines to verify no truncation
- Check 8: kernel launch in .cu uses <<<grid, block, shared_mem, stream>>> syntax, not in any .cpp or .h file
