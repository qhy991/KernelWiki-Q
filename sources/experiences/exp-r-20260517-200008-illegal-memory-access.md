---
id: exp-r-20260517-200008-illegal-memory-access
title: CUDA illegal memory access in GEMM/attention kernels
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

- Every CUDA kernel must start with a bounds check: if (tid >= N) return; for 1D, check both dims for 2D.
- Grid dimension formula: int grid = (N + blockDim - 1) / blockDim; guard against grid == 0.
- For 2D tensors: check if (row >= rows || col >= cols) return; after computing row and col from thread indices.
- Shared memory indexing: verify threadIdx.x < TILE_SIZE before accessing __shared__ arrays.
- Grid-stride loops need bounds check inside the loop, not just at entry: for (int i = tid; i < N && i >= 0; i += stride).
- Use CUDA_LAUNCH_BLOCKING=1 env var for debugging; compile with -lineinfo for accurate stack traces.
- cuda-memcheck --tool memcheck (or compute-sanitizer --tool memcheck) pinpoints the exact illegal access.
