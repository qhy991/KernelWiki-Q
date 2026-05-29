---
id: exp-r-20260502-180012-int8-gemm-cublas-layout
title: sol_execbench_int8_gemm
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
captured_at: '2026-05-02'
confidence: inferred
reproducibility: snippet
techniques:
- fine-grained-quantization
impl_family: cublas
---

INT8 GEMM cuBLAS cublasGemmEx correctness failure: row-major to column-major mapping for C = A @ B.T is wrong

### Symptoms

- `编译通过但 correctness 检查失败`
- `输出矩阵 C 的值与 reference 完全不匹配`
- `max_absolute_error 极大`
- `cuBLAS 返回 CUBLAS_STATUS_SUCCESS 但结果错误`

## Challenge

SOL-ExecBench PI-int8 GEMM 任务的 reference 实现是 C = A @ B.T，其中 A[M,K] int8, B[N,K] int8, C[M,N] int32。多个实验使用 cuBLAS cublasGemmEx 实现了 INT8 GEMM，编译通过但 correctness 检查失败。根本原因是 row-major (PyTorch) 到 column-major (cuBLAS) 的映射不正确。cuBLAS 按列主序计算 C_col = alpha * op(A_col) * op(B_col) + beta * C_col，而问题定义是 row-major 的 C_row = A_row @ B_row.T。LLM 经常直接传入 A、B 指针但混淆了 m/n/k 参数和 transa/transb 标志。


## Solution

SOL-ExecBench INT8 GEMM 定义为 C[M,N] = A[M,K] @ B.T[N,K]，其中所有 tensor 都是 row-major。正确映射到 cuBLAS column-major 的方法是利用等式 C_row^T = B_row * A_row^T，因此 cuBLAS 参数为：m=N, n=M, k=K, op(A)=CUBLAS_OP_N (B[N,K]), op(B)=CUBLAS_OP_N (A[M,K]), lda=K, ldb=K, ldc=N。但 C 是 row-major[M,N]，传给 cuBLAS 时当作 col-major[N,M]，所以 C 的内存布局实际匹配。

### Implementation

```cuda
```c
// problem: C_row[M,N] = A_row[M,K] @ B_row[N,K]^T
// equivalently: C_col[N,M] = B_col[N,K] @ A_col[K,M]
// cuBLAS call:
cublasGemmEx(handle,
    CUBLAS_OP_N,     // transa: B not transposed
    CUBLAS_OP_N,     // transb: A not transposed
    N, M, K,         // m=N, n=M, k=K
    &alpha,
    B_data, CUDA_R_8I, K,   // A_cublas = B, lda = K
    A_data, CUDA_R_8I, K,   // B_cublas = A, ldb = K
    &beta,
    C_data, CUDA_R_32I, N,  // C_cublas = C, ldc = N
    CUDA_R_32I,              // computeType = int32 accumulation
    CUBLAS_GEMM_DEFAULT_TENSOR_OP  // use Tensor Cores
);
```
```

## Key Lessons

- SOL-ExecBench INT8 GEMM 的 reference 是 torch._int_mm(A, B.T)，即 C=A@B^T。LLM 经常误解为 C=A@B。
- cuBLAS row-major → column-major 映射的正确策略：将原始问题 C_row=A_row@B_row^T 等价转换为 C_col=B_col@A_col^T，然后直接用 CUBLAS_OP_N + CUBLAS_OP_N。
- 不要用 CUBLAS_OP_T 来处理 transpose — 虽然看起来直观，但容易搞错 m/n/k 参数。用等价变换替代 transpose 更可靠。
- INT8 GEMM 的 computeType 必须是 CUDA_R_32I（int32 累加），不能用 CUDA_R_8I。
- DPS=true 模式下 C 是预分配的 int32 tensor，直接用 C.data_ptr<int32_t>() 作为输出指针。
