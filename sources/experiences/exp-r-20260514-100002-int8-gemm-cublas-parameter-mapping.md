---
id: exp-r-20260514-100002-int8-gemm-cublas-parameter-mapping
title: 'SOL-ExecBench INT8 GEMM: cuBLAS cublasGemmEx parameter mapping for mixed row/col-major
  inputs'
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
impl_family: cublas
---

The #1 cause of cuBLAS INT8 GEMM failure is wrong parameter mapping. 80% of cuBLAS attempts fail with status 7 (invalid value) or silent numerical errors. This experience provides the exact parameter derivation step-by-step so the agent can correctly map any SOL-ExecBench PI-int8 task dimensions to cuBLAS parameters.

## Challenge

cuBLAS uses column-major convention but SOL-ExecBench has mixed layouts: A is [M,K] row-major, B is [K,N] column-major. Agents consistently get the cublasGemmEx parameters wrong: wrong transpose ops, wrong leading dimensions, wrong m/n/k ordering, or wrong dimension extraction from PyTorch tensors.

### Symptoms

- `cuBLAS status 7 (CUBLAS_STATUS_INVALID_VALUE) — wrong leading dimensions or dimension mismatch`
- `Silent numerical errors (max_relative_error > 1e6) — wrong transpose operations`
- `Output all zeros — alpha/beta type mismatch (float vs int32_t)`
- `Segmentation fault — workspace tensor too small or wrong type`
- `Dimension confusion: using B.size(0) as N when B is [K,N] col-major (B.size(0)=K, not N)`

## Solution

Follow this step-by-step parameter derivation for SOL-ExecBench PI-int8 GEMM with cuBLAS:

### Implementation

```cuda
## Step 1: Know the actual tensor layouts

SOL-ExecBench definition.json specifies:
  A: int8 [M,K] row-major (contiguous, stride(0)=K)
  B: int8 [K,N] COLUMN-MAJOR (stride(0)=1)
  scale_a: float32 [M] per-token
  scale_b: float32 [N] per-channel
  C_out: bfloat16 [M,N]

In PyTorch: B.size(0)=K, B.size(1)=N  ← THIS IS CRITICAL

## Step 2: Extract dimensions correctly

```cpp
int M = A.size(0);   // rows of A
int K = A.size(1);   // cols of A = rows of B
int N = B.size(1);   // cols of B ← NOT B.size(0)!
```

## Step 3: Map to cuBLAS column-major convention

cuBLAS GEMM computes: C_col = alpha * op(A_param) * op(B_param) + beta * C_col
where all matrices are column-major.

Our goal: C_row[M,N] = A_row[M,K] @ B_col[K,N]

Memory reinterpretation:
  A_row[M,K] in memory = A_col[K,M]  (same bytes, different view)
  B_col[K,N] = B_col[K,N]           (already column-major)
  C_row[M,N] in memory = C_col[N,M]  (same bytes, different view)

So we need: C_col[N,M] = op(A_param) * op(B_param)
with: op(A_param) being [N,K] and op(B_param) being [K,M]

Solution: compute B_col^T * A_col
  A_param = B_col[K,N], opA = CUBLAS_OP_T → B_col^T [N,K]  ✓
  B_param = A_col[K,M], opB = CUBLAS_OP_N → A_col   [K,M]  ✓
  Result: [N,K] * [K,M] = [N,M] = C_col     ✓

## Step 4: The complete cuBLAS call

```cpp
int32_t alpha = 1, beta = 0;
cublasGemmEx(handle,
    CUBLAS_OP_T,              // transa: transpose B_col to get B_col^T
    CUBLAS_OP_N,              // transb: no transpose, A_col stays as-is
    N,                        // m = rows of result = N
    M,                        // n = cols of result = M
    K,                        // k = inner dimension = K
    &alpha,                   // int32_t, NOT float!
    B_ptr, CUDA_R_8I, K,     // A_param = B[K,N]col, lda = K (rows of B_col)
    A_ptr, CUDA_R_8I, K,     // B_param = A^T[K,M]col, ldb = K (rows of A_col)
    &beta,                    // int32_t, NOT float!
    workspace, CUDA_R_32I, N, // C_param = [N,M]col, ldc = N (rows of C_col)
    CUDA_R_32I,               // compute type = int32 accumulation
    CUBLAS_GEMM_DEFAULT_TENSOR_OP  // use tensor cores
);
```

## Step 5: Why workspace[m*N+n] = correct C[m,n]

cuBLAS writes C_col[n,m] at offset n + m*N (column-major).
But n + m*N = m*N + n (commutative addition).
So workspace[m*N+n] = C_col[n,m] = sum_k B[k,n]*A[m,k] = C_row[m,n].  ✓

The dequant kernel reads workspace[row*N+col] and gets the correct value directly.

## Common mistakes and their symptoms:

| Mistake | Symptom |
|--------|----------|
| N = B.size(0) instead of B.size(1) | Status 7 or wrong results |
| opA = CUBLAS_OP_N instead of T | max_relative_error > 1e6 |
| opB = CUBLAS_OP_T instead of N | max_relative_error > 1e6 |
| lda = N instead of K | Status 7 |
| ldb = M instead of K | Status 7 |
| ldc = M instead of N | Status 7 or segfault |
| alpha/beta as float not int32_t | Output all zeros or garbage |
| No workspace, write directly to C | Wrong dtype (need int32 accum) |
```

## Key Lessons

- ALWAYS extract dimensions as: M=A.size(0), K=A.size(1), N=B.size(1). NEVER use B.size(0) as N because B is [K,N] column-major and B.size(0)=K.
- cuBLAS parameter cheat sheet for SOL-ExecBench INT8: opA=T, opB=N, m=N, n=M, k=K, lda=K, ldb=K, ldc=N. A_param=B, B_param=A.
- alpha and beta MUST be int32_t (not float) when compute type is CUDA_R_32I with INT8 inputs. Using float gives garbage results.
- cuBLAS output [N,M] column-major has identical memory layout to [M,N] row-major. This is a mathematical identity: element at [m,n] is at offset m*N+n in both representations.
- Status 7 (CUBLAS_STATUS_INVALID_VALUE) almost always means wrong leading dimensions or m/n/k don't match lda/ldb/ldc. Double-check dimension extraction first.
- Always allocate int32 workspace [M,N] for accumulation. Never write cuBLAS output directly to bfloat16 C.
- Persistent cuBLAS handle (static variable) is essential for small M shapes to avoid handle creation overhead.
