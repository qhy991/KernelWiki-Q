---
id: exp-r-20260506-150007-gemm-handle-creation-overhead
title: 'SOL-ExecBench GEMM: cuBLAS handle creation overhead for small matrices'
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
captured_at: '2026-05-06'
confidence: inferred
reproducibility: snippet
impl_family: cublaslt
---

Creating and destroying cuBLAS/cuBLASLt handle per kernel call adds ~0.5-1ms overhead, making small GEMM 20-60x slower than baseline. Must use persistent or reused handle.

## Challenge

Agent creates cuBLAS handle inside the run() function with cublasCreate(&handle) / cublasDestroy(handle) per call. For small matrices (M<=50), handle creation overhead (~0.5-1ms) dominates actual compute (~0.02-0.05ms), causing speedup << 1.0.

### Symptoms

- `Speedup much less than 1.0 (e.g., 0.017x - 60x slower than baseline)`
- `cuBLAS handle created inside kernel launch function`
- `cublasCreate + cublasDestroy in every call`
- `cudaMalloc + cudaFree in every call for workspace`

## Solution

Create cuBLAS handle ONCE and reuse across calls. Use static variable, thread_local, or reuse PyTorch's existing handle.

### Implementation

```cuda
Three approaches for handle reuse:

1. Static handle (simplest):
   static cublasHandle_t handle = nullptr;
   if (!handle) { cublasCreate(&handle); }
   cublasSetStream(handle, stream);

2. Thread-local handle (thread-safe):
   thread_local cublasHandle_t handle = nullptr;
   if (!handle) { cublasCreate(&handle); }

3. Reuse PyTorch's handle (zero overhead):
   void* handle = reinterpret_cast<void*>(
       at::cuda::getCurrentCUDABlasHandle());

Do NOT:
- Call cublasCreate/cublasDestroy inside run()
- Allocate workspace with cudaMalloc per call
- Use cuBLASLt with per-call cublasLtCreate/cublasLtDestroy
```

## Key Lessons

- cuBLAS handle creation costs ~0.5-1ms - for small GEMM with ~0.02ms compute, this is 25-50x overhead.
- Never create cuBLAS handle inside the kernel launch function.
- Use static/thread_local handle or reuse PyTorch's handle via at::cuda::getCurrentCUDABlasHandle().
- speedup << 1.0 almost always means handle/workspace overhead, not compute issue.
- For SOL-ExecBench benchmark harness, handle is called multiple times - persistent handle amortizes creation cost.
- Also avoid cudaMalloc/cudaFree per call - pre-allocate workspace or use PyTorch allocator.
