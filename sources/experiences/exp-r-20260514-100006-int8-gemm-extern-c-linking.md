---
id: exp-r-20260514-100006-int8-gemm-extern-c-linking
title: 'SOL-ExecBench INT8 GEMM: extern C linking for nvcc/g++ interop'
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

When the SOL-ExecBench kernel launcher function in kernel.cu lacks extern C linkage, g++-compiled main.cpp cannot link to it due to C++ name mangling. The linker reports 'undefined symbol' with a mangled name like _Z22gemm_int8_dequant_cudaPKaS0_.... This affects all CUDA kernel types, not just INT8 GEMM.

## Challenge

nvcc compiles kernel.cu as C++ by default, mangling function names. g++ compiles main.cpp as C++. If the header doesn't wrap declarations in extern C, each compiler applies its own mangling, and the linker cannot resolve the symbol.

### Symptoms

- `undefined symbol: _Z22gemm_int8_dequant_cudaPKaS0_PKfS2_PvPiiiiP11CUstream_st`
- `undefined reference to `gemm_int8_dequant_cuda(...)'`
- `collect2: error: ld returned 1 exit status`
- `kernel.o: file not recognized: file format not recognized`

## Solution

Always wrap kernel launcher declarations in kernel.h with extern C guards. Both the declaration in kernel.h and the definition in kernel.cu must use extern C to prevent C++ name mangling.

### Implementation

```cuda
## kernel.h — Always use extern C guards
```cpp
#pragma once
#include <cuda_runtime.h>

#ifdef __cplusplus
extern "C" {
#endif

void gemm_int8_dequant_cuda(
    const int8_t* A, const int8_t* B,
    const float* scale_a, const float* scale_b,
    void* C, int32_t* workspace,
    int M, int N, int K, cudaStream_t stream);

#ifdef __cplusplus
}
#endif
```

## kernel.cu — Definition also uses extern C
```cpp
#include "kernel.h"
#include <cuda_runtime.h>
#include <cublas_v2.h>

// The extern C wrapping from kernel.h applies automatically.
// But if defining functions not declared in kernel.h, add:
extern "C" {
  // additional launcher functions
}

// The main launcher function matching the declaration:
void gemm_int8_dequant_cuda(
    const int8_t* A, const int8_t* B,
    const float* scale_a, const float* scale_b,
    void* C, int32_t* workspace,
    int M, int N, int K, cudaStream_t stream) {
    // implementation
}
```

## main.cpp — Calls the extern C function
```cpp
#include <torch/extension.h>
#include "kernel.h"

void run(torch::Tensor A, torch::Tensor B,
         torch::Tensor scale_a, torch::Tensor scale_b,
         torch::Tensor C) {
    // Direct call to the extern C function — no mangling issue
    gemm_int8_dequant_cuda(...);
}
```

## Diagnostic: If you see 'undefined symbol _Z...'
1. The _Z prefix means C++ name mangling is active
2. Check kernel.h: are extern C guards present?
3. Check kernel.cu: does the function signature EXACTLY match the declaration?
4. Parameter types must match exactly: cudaStream_t not CUstream_st, int8_t not signed char
```

## Key Lessons

- ALWAYS wrap kernel launcher declarations in extern C in kernel.h. nvcc compiles as C++ by default, causing name mangling that g++ cannot resolve.
- The #ifdef __cplusplus extern C guard ensures compatibility with both C and C++ compilation. Use it in every kernel.h.
- If the linker error shows a _Z prefix (e.g., _Z22gemm_int8_dequant_cuda...), it means C++ name mangling is active. The fix is extern C wrapping.
- The function signature in kernel.cu must EXACTLY match the declaration in kernel.h, including parameter types (cudaStream_t vs CUstream_st, int8_t vs signed char).
- This pattern is universal for SOL-ExecBench CUDA kernels, not INT8-specific. Apply it to all kernel types: BF16, FP16, INT8, FP32.
