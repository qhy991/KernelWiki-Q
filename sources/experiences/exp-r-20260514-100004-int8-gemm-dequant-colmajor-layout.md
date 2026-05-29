---
id: exp-r-20260514-100004-int8-gemm-dequant-colmajor-layout
title: 'SOL-ExecBench INT8 GEMM: dequant kernel layout — cuBLAS output is [N,M] column-major,
  not [M,N] row-major'
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

After cuBLAS cublasGemmEx computes INT8 GEMM, the int32 output is in [N,M] column-major layout (cuBLAS convention). Many agents incorrectly assume it is [M,N] row-major and dequant with wrong indexing, causing INCORRECT_NUMERICAL. However, [N,M] column-major and [M,N] row-major have identical memory layout (offset m*N+n), so the dequant kernel can use row-major indexing directly. The trap is when agents try to 'fix' the column-major by transposing or using col-major indexing.

## Challenge

After cuBLAS cublasGemmEx with opA=T and opB=N, the output workspace is [N,M] in column-major convention. Agents get confused by this and either: (1) try to transpose the output with wrong indexing, (2) use column-major indexing that double-transposes, (3) allocate wrong-sized workspace. The dequant kernel then produces garbage.

### Symptoms

- `INCORRECT_NUMERICAL with moderate max_relative_error (10-10000x) after cuBLAS step succeeds`
- `Dequant kernel reads workspace[n*M+m] but writes C_out[m*N+n], mixing conventions`
- `Output has correct structure (not NaN/inf) but values are scrambled/transposed`
- `Works correctly for M=N (symmetric) but fails when M!=N`
- `cuBLAS step passes (no status errors) but overall correctness fails`

## Solution

cuBLAS output [N,M] column-major has identical memory layout to [M,N] row-major. Use row-major indexing in the dequant kernel directly. Do NOT try to transpose or use column-major indexing.

### Implementation

```cuda
## The Key Mathematical Identity

cuBLAS writes D_col[n][m] at memory offset: n + m*N  (column-major)

Row-major C[m][n] at memory offset: m*N + n  (row-major)

Since n + m*N = m*N + n (commutative addition), both access the SAME element.

## Correct dequant kernel:

```cuda
__global__ void dequant_kernel(
    const int32_t* workspace,   // int32 [M,N] in memory (cuBLAS wrote [N,M] col)
    const float* scale_a,       // float [M] per-token
    const float* scale_b,       // float [N] per-channel
    uint16_t* C_bf16,           // bfloat16 [M,N] output
    int M, int N)
{
    int row = blockIdx.y * blockDim.y + threadIdx.y;  // 0..M-1
    int col = blockIdx.x * blockDim.x + threadIdx.x;  // 0..N-1
    if (row >= M || col >= N) return;

    // Row-major indexing: workspace[m*N+n] = D_col[n,m] = correct C[m,n]
    int32_t val = workspace[row * N + col];
    float scaled = static_cast<float>(val) * scale_a[row] * scale_b[col];
    C_bf16[row * N + col] = __bfloat16_as_ushort(__float2bfloat16(scaled));
}
```

## WRONG patterns that cause failures:

```cuda
// WRONG 1: Trying to 'fix' column-major by transposing
int32_t val = workspace[col * M + row];  // Double transpose! Wrong!

// WRONG 2: Using column-major indexing on both read and write
int32_t val = workspace[col * M + row];  // Wrong!
C_bf16[col * M + row] = ...;  // Also wrong!

// WRONG 3: Allocating workspace as [N,M] instead of [M,N]
auto workspace = torch::empty({N, M}, ...);  // Wrong size!
```

## Correct workspace allocation in main.cpp:

```cpp
auto workspace = torch::empty({M, N},
    torch::dtype(torch::kInt32).device(A.device()));
```

## The block/grid dimensions:

```cpp
dim3 blk(32, 8);  // 32 threads in x (N direction), 8 in y (M direction)
dim3 grd((N + 31) / 32, (M + 7) / 8);
```

## Why this works:

cuBLAS computes: D_col = B_col^T * A_col
  B_col^T is [N,K], A_col is [K,M]
  D_col is [N,M]

Element D_col[n][m] = sum_k B[k][n] * A[m][k] = C[m][n]

Memory: D_col[n][m] at offset n + m*N = m*N + n = C_row[m][n]

So workspace[m*N + n] IS the correct C[m][n]. No transpose needed.
```

## Key Lessons

- cuBLAS output [N,M] column-major and [M,N] row-major have identical memory layout: element [m,n] at offset m*N+n in both. Use row-major indexing directly in dequant kernel.
- NEVER use workspace[col*M+row] or workspace[col*M+row] in the dequant kernel. This double-transposes and produces wrong output.
- Allocate workspace as torch::empty({M, N}, torch::kInt32) — exactly [M,N] elements. Not [N,M].
- If dequant passes for M=N but fails for M!=N, the indexing convention is wrong.
- The dequant block dimensions should be (32, 8) with grid ((N+31)/32, (M+7)/8). x-dimension covers N (columns), y-dimension covers M (rows).
- scale_a is indexed by row (0..M-1), scale_b is indexed by col (0..N-1). Never swap these.
- Output must be bfloat16 (use __float2bfloat16 and __bfloat16_as_ushort for uint16_t storage), not float32.
- cuBLAS computes D = B^T * A^T in column-major. Each element D[n][m] = sum_k B[k][n]*A[m][k] which is exactly C[m][n].
