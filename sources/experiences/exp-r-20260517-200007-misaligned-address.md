---
id: exp-r-20260517-200007-misaligned-address
title: CUDA misaligned address runtime error in BF16/INT8 kernels
experience_type: repair
source_category: agent-experiment
architectures:
- sm90
tags:
- gemm
- shared-memory-optimization
- vectorized-loads
kernel_types:
- gemm
languages:
- cuda-cpp
captured_at: '2026-05-17'
confidence: inferred
reproducibility: concept
techniques:
- shared-memory-optimization
- vectorized-loads
impl_family: custom_cuda
---

## Key Lessons

- Vectorized loads (uint2/uint4/float4) require alignment: sizeof(type) bytes. Check with reinterpret_cast<uintptr_t>(ptr) % sizeof(type) == 0.
- torch::Tensor data_ptr() does not guarantee 8-byte or 16-byte alignment — always check before vectorized access.
- Use scalar loads as fallback when alignment check fails.
- Declare shared memory with __align__(16) when used for vectorized access.
- Enable CUDA_LAUNCH_BLOCKING=1 during debugging to get synchronous error reporting.
- Use cuda-memcheck (compute-sanitizer) to find exact misaligned access locations.
- On newer GPUs (sm_80+), misaligned access may silently produce wrong results instead of crashing — correctness testing is essential.
