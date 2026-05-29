---
id: exp-r-20260514-100010-int8-gemm-cstdio-include-debug-output
title: 'SOL-ExecBench INT8 GEMM: missing cstdio include for fprintf/stderr debug output
  in CUDA'
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
captured_at: '2026-05-14'
confidence: inferred
reproducibility: snippet
techniques:
- fine-grained-quantization
impl_family: custom_cuda
---

When adding debug output (fprintf(stderr, ...)) to CUDA kernel host code, the compilation fails with 'identifier stderr is undefined' if <cstdio> is not included. This happens because nvcc treats .cu files differently from standard C++ compilers. Always include <cstdio> explicitly when using fprintf, stderr, printf, or other C standard I/O in .cu files.

## Challenge

Agent adds fprintf(stderr, ...) debug statements to kernel.cu but omits #include <cstdio>. nvcc does not implicitly include C standard I/O headers, causing 'identifier stderr is undefined' and 'identifier fprintf is undefined' compilation errors.

### Symptoms

- `error: identifier "stderr" is undefined`
- `error: identifier "fprintf" is undefined`
- `error: identifier "printf" is undefined`

## Solution

Add #include <cstdio> to kernel.cu when using fprintf, stderr, printf, or any C standard I/O function. Alternatively, use CUDA's printf() inside __global__ kernels which doesn't require <cstdio>.

### Implementation

```cuda
## Option A: Host-side debug with fprintf (requires cstdio)
```cpp
// kernel.cu
#include <cuda_runtime.h>
#include <cstdio>   // REQUIRED for fprintf, stderr
#include "kernel.h"

extern "C" void launch_kernel(...) {
    // Host-side debug output
    fprintf(stderr, "Debug: M=%d N=%d K=%d\n", M, N, K);
    // ... kernel launch ...
}
```

## Option B: Device-side debug with CUDA printf (no extra include)
```cpp
__global__ void my_kernel(...) {
    // CUDA printf works inside kernels without cstdio
    if (threadIdx.x == 0 && blockIdx.x == 0) {
        printf("Block %d: val=%d\n", blockIdx.x, val);
    }
}
```

## Required includes by use case:
// fprintf(stderr, ...) → #include <cstdio>
// printf(...) in host code → #include <cstdio>
// printf(...) in device code → no extra include (CUDA built-in)
// std::cerr → #include <iostream> (not recommended in .cu files)
```

## Key Lessons

- nvcc does not implicitly include <cstdio>. When using fprintf, stderr, or printf in host-side .cu code, add #include <cstdio> explicitly.
- For device-side debug output, CUDA's built-in printf() inside __global__ kernels doesn't require any extra includes. Use it instead of fprintf for GPU-side debugging.
- Avoid using C++ streams (std::cerr, std::cout) in .cu files — they add compilation complexity. Prefer fprintf (with cstdio) or CUDA printf.
