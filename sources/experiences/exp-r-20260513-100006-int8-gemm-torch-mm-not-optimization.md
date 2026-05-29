---
id: exp-r-20260513-100006-int8-gemm-torch-mm-not-optimization
title: 'SOL-ExecBench INT8 GEMM: torch.mm() wrapper is not a kernel optimization'
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
- python
captured_at: '2026-05-13'
confidence: inferred
reproducibility: snippet
techniques:
- fine-grained-quantization
impl_family: pytorch
---

Submitting a solution where kernel.cu is a dummy and main.cpp calls torch.mm(A.float(), B.float()) is NOT a valid optimization. This is just PyTorch eager mode which the benchmark already uses as baseline. The speedup is ~1.0x (no improvement) and the solution should use a custom CUDA kernel, cuBLAS, or CUTLASS.

## Challenge

Agent generates a solution where kernel.cu is empty or a dummy placeholder, and main.cpp uses torch.mm(A.float(), B.float()) * scale to compute the result. This bypasses the intent of the benchmark — to write an optimized INT8 GEMM kernel.

### Symptoms

- `kernel.cu is empty or contains only a dummy function`
- `main.cpp calls torch.mm() or torch.matmul() directly`
- `Speedup is ~1.0x-1.4x (PyTorch eager vs PyTorch eager variance)`
- `The reference baseline is also PyTorch eager, so this gives no real improvement`

## Solution

Do NOT use torch.mm() as the GEMM implementation. Write a real CUDA kernel using cuBLAS or CUTLASS. The solution must contain actual GPU kernel code in kernel.cu that is launched from main.cpp.

### Implementation

```cuda
The solution structure should be:
1. kernel.cu: Contains the actual GEMM kernel using cuBLAS cublasGemmEx or CUTLASS templates
2. kernel.h: Declares the launch function
3. main.cpp: Calls the kernel launch function, passing raw device pointers

Do NOT:
- Leave kernel.cu empty
- Use torch.mm(), torch.matmul(), or torch.nn.functional.linear
- Convert int8 to float32 and use PyTorch eager (same as baseline)

DO:
- Use cublasGemmEx with CUDA_R_8I and CUBLAS_COMPUTE_32I for INT8 Tensor Core
- Or use CUTLASS int8_gemm kernel with fused epilogue dequantize
- Handle per-token scale_a[M] and per-channel scale_b[N] in a separate kernel or fused epilogue
```

## Key Lessons

- torch.mm() is NOT an optimization. The SOL-ExecBench reference is PyTorch eager, so using torch.mm() gives ~1.0x speedup — no improvement.
- The kernel.cu file must contain actual GPU kernel code. Leaving it as a dummy defeats the purpose of the benchmark.
- Valid INT8 GEMM approaches: (1) cuBLAS cublasGemmEx with CUBLAS_COMPUTE_32I, (2) CUTLASS int8_gemm with EpilogueVisitorPerRowPerCol for fused dequant, (3) cuBLASLt with custom dequant kernel.
- Speedup of 1.0x-1.4x for an INT8 GEMM usually means the solution is not using Tensor Cores. Real INT8 IMMA should give 2x-6x over float32 baseline.
- When the agent sees ~1x speedup, it should immediately recognize this means no real optimization happened, not that the kernel is 'working'.
