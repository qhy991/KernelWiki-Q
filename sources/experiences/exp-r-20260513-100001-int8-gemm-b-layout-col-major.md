---
id: exp-r-20260513-100001-int8-gemm-b-layout-col-major
title: 'SOL-ExecBench INT8 GEMM: B matrix is column-major, not row-major'
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
captured_at: '2026-05-13'
confidence: inferred
reproducibility: snippet
techniques:
- fine-grained-quantization
impl_family: custom_cuda
---

In SOL-ExecBench PI-int8 tasks, B is [K,N] column-major (stride(0)==1). The definition says 'B: [K,N] col-major (per-channel quantized)'. Accessing B with row-major indexing B[n*K+k] causes INCORRECT_NUMERICAL with max_relative_error > 100000x. Must use B[k*N+n] or let cuBLAS handle the layout via leading dimension.

## Challenge

When writing custom CUDA kernels for SOL-ExecBench PI-int8 GEMM, the agent assumes B is row-major [N,K] and indexes it as B[n*K+k]. However, the definition.json specifies B as [K,N] column-major with stride(0)==1. This mismatch causes massive numerical errors.

### Symptoms

- `Evaluation status: INCORRECT_NUMERICAL`
- `max_relative_error: 195788800.0 or similar huge values`
- `max_absolute_error: 2899929.0 or similar`
- `has_nan: false, has_inf: false — wrong values, not NaN`
- `Kernel compiles and runs without crash, but output is completely wrong`

## Solution

In custom CUDA kernels, index B as column-major: B[k*N+n]. In cuBLAS calls, B is already [K,N] col-major, so pass it directly with lda=N (the leading dimension of a column-major [K,N] matrix).

### Implementation

```cuda
1. Read definition.json carefully: B shape is [K,N] col-major, meaning B[k][n] = B[k*N+n] in flat indexing
2. In custom CUDA: acc += A[m*K+k] * B[k*N+n]   (NOT B[n*K+k])
3. In cuBLAS: B is already col-major, use lda=N for B's leading dimension
4. Verify with the reference: reference does B.float() * scale_b where B is [K,N], then A_f @ B_f gives C[M,N] — this works because PyTorch treats B as row-major [K,N] but the underlying data is col-major
5. The generate_inputs function creates B as: (b_fp32 / scale_b.unsqueeze(1)).round().clamp(-128, 127).to(torch.int8).t() — the .t() makes it [K,N] col-major
```

## Key Lessons

- SOL-ExecBench PI-int8 B matrix is [K,N] column-major (stride(0)==1). The definition.json explicitly states this. Always read definition.json before writing kernel indexing.
- In custom CUDA: index B as B[k*N+n] for column-major. Using B[n*K+k] causes max_relative_error > 1e8.
- In cuBLAS cublasGemmEx: B is already column-major, pass directly. For A[M,K] row-major reinterpreted as col-major A^T[K,M], use opA=CUBLAS_OP_N with lda=K. For B[K,N] col-major, use opB=CUBLAS_OP_N with ldb=N.
- The generate_inputs function creates B via .t() — this transposes row-major [N,K] to col-major [K,N]. This is the source of the column-major layout.
- When debugging INCORRECT_NUMERICAL with huge relative errors (>1e6), first check matrix indexing — it is almost always a row-major vs column-major confusion.
- PI-int8 tasks m10_n2560_k1024, m50_n8192_k1024, and m50_n1024_k2048 all failed 100% of attempts because every kernel made this B layout mistake.
