---
id: exp-r-20260513-100007-fp16-half2float-type-conversion
title: 'SOL-ExecBench FP16 GEMM: __half2float returns float, cannot assign to __half'
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
captured_at: '2026-05-13'
confidence: inferred
reproducibility: snippet
impl_family: custom_cuda
---

When using CUDA __half vector types (half4, etc.), calling __half2float() returns a float, but assigning that float back to a __half variable causes compilation error: 'no suitable constructor exists to convert from float to __half'. Must use __float2half() or __float2half_rn() for the reverse conversion.

## Challenge

Agent writes FP16 GEMM kernel using half4 vector loads for performance. The dot-product loop converts half4.x/y/z/w to float via __half2float(), multiplies, and accumulates in a float 'sum'. But the compiler infers 'sum' as __half (due to initial assignment context) and the __half2float results cannot be assigned back to __half.

### Symptoms

- `Compilation error: no suitable constructor exists to convert from "float" to "__half"`
- `Error on lines using __half2float(a.x) * __half2float(b.x)`
- `8+ errors detected in the compilation of kernel.cu`
- `Build stopped: subcommand failed`

## Solution

Declare the accumulator as 'float' explicitly. Use __half2float() to read from __half inputs, accumulate in float, then convert final result back to __half with __float2half() or __float2half_rn().

### Implementation

```cuda
// CORRECT pattern for FP16 dot product with half4:
half4 a = reinterpret_cast<const half4*>(A)[idx];
half4 b = reinterpret_cast<const half4*>(B)[idx];
float sum = 0.0f;  // MUST be float, not __half
sum += __half2float(a.x) * __half2float(b.x);
sum += __half2float(a.y) * __half2float(b.y);
sum += __half2float(a.z) * __half2float(b.z);
sum += __half2float(a.w) * __half2float(b.w);
// Final conversion:
result[row * N + col] = __float2half(sum);

// For FP16 GEMM, prefer cuBLAS with CUDA_R_16F:
cublasGemmEx(handle, CUBLAS_OP_T, CUBLAS_OP_N,
    M, N, K, &alpha,
    A, CUDA_R_16F, K,
    B, CUDA_R_16F, K,
    &beta,
    C, CUDA_R_16F, N,
    CUBLAS_COMPUTE_32F, CUBLAS_GEMM_DEFAULT);
```

## Key Lessons

- __half2float() returns float. Never assign its result to __half without converting back via __float2half() or __float2half_rn().
- Always declare accumulators as 'float' (not __half) for FP16 computation. Accumulate in float precision, convert only the final result.
- For FP16 GEMM, prefer cuBLAS with CUDA_R_16F and CUBLAS_COMPUTE_32F over custom kernels. cuBLAS handles Tensor Core FP16 automatically.
- When using half4 vector loads for memory bandwidth, convert each component with __half2float(), compute in float, then store with __float2half().
- FP16 CUDA intrinsics cheat sheet: __half2float(h) -> float, __float2half(f) -> __half, __halves2half2(h1,h2) -> half2, __low2half(h2) -> __half, __high2half(h2) -> __half.
