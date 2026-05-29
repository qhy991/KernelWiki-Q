---
id: exp-r-20260514-100008-int8-gemm-kernel-host-signature-mismatch
title: 'SOL-ExecBench INT8 GEMM: kernel-host function signature mismatch and missing
  declarations'
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

When the function declaration in kernel.h does not exactly match the definition in kernel.cu, or when kernel.h is missing declarations that main.cpp calls, compilation or linking fails. Common mismatches: missing cudaStream_t parameter, wrong parameter types (void* vs int32_t*), extra or missing arguments. The declaration, definition, and call site must all agree exactly.

## Challenge

Agent writes kernel.h declaring a function with one signature, kernel.cu defining it with a different signature, and main.cpp calling with yet another set of arguments. This causes 'too many arguments', 'not declared in this scope', or 'undefined identifier' errors. The three-file compilation model requires exact signature consistency.

### Symptoms

- `error: too many arguments in function call`
- `error: 'launch_gemm_int8' was not declared in this scope`
- `error: identifier 'stream' is undefined`
- `error: identifier 'C' is undefined`
- `error: identifier 'K' is undefined`
- `error: no matching function for call to 'gemm_int8_dequant_cuda'`

## Solution

Ensure kernel.h declaration, kernel.cu definition, and main.cpp call site all use the EXACT same function signature including parameter types and count. Write kernel.h first, then copy the declaration to kernel.cu and main.cpp.

### Implementation

```cuda
## Step 1: Define the complete signature in kernel.h FIRST
```cpp
#pragma once
#include <cuda_runtime.h>
#include <cstdint>

#ifdef __cplusplus
extern "C" {
#endif

// Write this ONCE, then copy verbatim to kernel.cu and main.cpp call
void gemm_int8_dequant_cuda(
    const int8_t* A,        // NOT 'signed char*' or 'void*'
    const int8_t* B,
    const float* scale_a,
    const float* scale_b,
    void* C,                // void* for output (cast in kernel)
    int32_t* workspace,     // int32_t* for cuBLAS int32 accumulator
    int M, int N, int K,
    cudaStream_t stream     // ALWAYS include stream parameter
);

#ifdef __cplusplus
}
#endif
```

## Step 2: Copy EXACT signature to kernel.cu
```cpp
#include "kernel.h"
// Paste the EXACT same signature from kernel.h:
extern "C" void gemm_int8_dequant_cuda(
    const int8_t* A,
    const int8_t* B,
    const float* scale_a,
    const float* scale_b,
    void* C,
    int32_t* workspace,
    int M, int N, int K,
    cudaStream_t stream) {
    // implementation
}
```

## Step 3: Call with matching argument types in main.cpp
```cpp
#include "kernel.h"
void run(torch::Tensor A, torch::Tensor B,
         torch::Tensor scale_a, torch::Tensor scale_b,
         torch::Tensor C) {
    int M = A.size(0), K = A.size(1), N = B.size(1);
    auto workspace = torch::empty({M, N},
        torch::dtype(torch::kInt32).device(A.device()));
    gemm_int8_dequant_cuda(
        A.data_ptr<int8_t>(),       // matches const int8_t*
        B.data_ptr<int8_t>(),       // matches const int8_t*
        scale_a.data_ptr<float>(),  // matches const float*
        scale_b.data_ptr<float>(),  // matches const float*
        C.data_ptr(),               // matches void* (generic)
        workspace.data_ptr<int32_t>(), // matches int32_t*
        M, N, K,                    // matches int parameters
        at::cuda::getCurrentCUDAStream() // matches cudaStream_t
    );
}
```

## Common mismatches to avoid:
// Declaration says 'void* C' but definition says 'uint16_t* C' -> compile error
// Declaration has 8 params, definition has 9 (added stream) -> undefined identifier
// main.cpp passes float* where int32_t* expected -> silent data corruption
// Declaration missing cudaStream_t, definition has it -> too many arguments in call
```

## Key Lessons

- Write the function signature in kernel.h FIRST, then copy it verbatim to kernel.cu (definition) and main.cpp (call site). Never write each file independently.
- Parameter types must match exactly: const int8_t* vs int8_t* vs void* are different types. cuBLAS void* output must be void* in all three locations.
- ALWAYS include cudaStream_t as the last parameter in the launcher function. Omitting it causes 'too many arguments in function call' when main.cpp passes a stream.
- If kernel.h doesn't declare a function that main.cpp calls, you get 'was not declared in this scope'. Every function called from main.cpp must be declared in kernel.h.
- Parameter naming in the declaration is optional but helps readability. The types and order are what matter for compilation.
