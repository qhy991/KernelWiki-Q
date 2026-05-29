---
id: exp-r-20260517-200009-cuda-invalid-argument
title: CUDA invalid argument error in kernel launch
experience_type: repair
source_category: agent-experiment
architectures:
- sm90
tags:
- gemm
- shared-memory-optimization
kernel_types:
- gemm
languages:
- cuda-cpp
captured_at: '2026-05-17'
confidence: inferred
reproducibility: concept
techniques:
- shared-memory-optimization
impl_family: custom_cuda
---

CUDA invalid argument error in kernel launch

## Key Lessons

- Guard against zero grid dimensions: if (grid == 0) grid = 1; or if (N == 0) return; early exit.
- Check shared memory size: must be <= prop.sharedMemPerBlock (48KB default) or use cudaFuncSetAttribute for opt-in larger size.
- Max threads per block: 1024 on all current NVIDIA GPUs. Exceeding this gives invalid argument.
- Call cudaGetLastError() immediately after kernel launch (before any other CUDA calls) to catch the error at the source.
- For dynamic shared memory: the third argument to <<<>>> is in bytes, verify it doesn't exceed the limit.
- NULL tensor data pointers: torch::Tensor may have null data_ptr() for empty tensors — check tensor.numel() > 0 before accessing.
- Stream mismatch: ensure the stream belongs to the same device as the tensor data.
