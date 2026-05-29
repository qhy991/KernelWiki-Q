---
id: exp-r-20260513-100009-bf16-data-ptr-access
title: 'SOL-ExecBench BF16 tensor: use data_ptr() or data_ptr<at::BFloat16>(), not
  data_ptr<__nv_bfloat16>()'
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

PyTorch does not instantiate the data_ptr<__nv_bfloat16>() template. To access BF16 tensor data in CUDA kernels, use tensor.data_ptr() (returns void*) or tensor.data_ptr<at::BFloat16>() with reinterpret_cast<__nv_bfloat16*>() inside .cu files.

## Challenge

Agent calls tensor.data_ptr<__nv_bfloat16>() to get a typed pointer for BF16 tensors. PyTorch only registers data_ptr specializations for standard types (float, int, at::BFloat16, etc.), not for CUDA-specific __nv_bfloat16.

### Symptoms

- `Compile error: no matching function for 'data_ptr<__nv_bfloat16>'`
- `Or: undefined reference to at::Tensor::data_ptr<__nv_bfloat16>()`
- `Happens when trying to pass BF16 tensor data to cuBLAS or custom kernels`

## Solution

Use tensor.data_ptr() to get void* and pass to kernel launcher. Inside .cu files, reinterpret_cast to __nv_bfloat16*. Or use data_ptr<at::BFloat16>() if you need a typed pointer in .cpp context.

### Implementation

```cuda
// In main.cpp (no CUDA types):
gemm_launcher(A.data_ptr(), B.data_ptr(), C.data_ptr(), M, N, K, stream);

// In kernel.cu:
void gemm_launcher(const void* A, const void* B, void* C, ...) {
    auto a_ptr = reinterpret_cast<const __nv_bfloat16*>(A);
    auto b_ptr = reinterpret_cast<const __nv_bfloat16*>(B);
    auto c_ptr = reinterpret_cast<__nv_bfloat16*>(C);
    // Use with cuBLAS:
    cublasGemmEx(handle, CUBLAS_OP_T, CUBLAS_OP_N,
        M, N, K, &alpha,
        a_ptr, CUDA_R_16BF, K,
        b_ptr, CUDA_R_16BF, K,
        &beta, c_ptr, CUDA_R_16BF, N,
        CUBLAS_COMPUTE_32F, CUBLAS_GEMM_DEFAULT);
}
```

## Key Lessons

- PyTorch at::Tensor does NOT support data_ptr<__nv_bfloat16>(). Use data_ptr() (void*) or data_ptr<at::BFloat16>().
- at::BFloat16 (PyTorch type) and __nv_bfloat16 (CUDA type) have the same binary layout (both are 16-bit BF16). reinterpret_cast between them is safe and free.
- For cuBLAS calls with BF16 data: pass void* from data_ptr() directly. cuBLAS accepts void* with CUDA_R_16BF type tag.
- If you need a typed pointer in .cpp: use data_ptr<at::BFloat16>(). If you need __nv_bfloat16* for CUDA operations: reinterpret_cast inside .cu.
- The type mapping: torch::kBFloat16 <-> at::BFloat16 (host) <-> __nv_bfloat16 (CUDA device). They are layout-compatible.
