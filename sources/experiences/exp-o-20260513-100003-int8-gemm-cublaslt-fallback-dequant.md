---
id: exp-o-20260513-100003-int8-gemm-cublaslt-fallback-dequant
title: 'SOL-ExecBench INT8 GEMM: cuBLAS + dequant kernel fallback with correct parameter
  mapping'
experience_type: optimization
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
impl_family: cublas
---

When CUTLASS fused epilogue is not available, use cuBLAS cublasGemmEx for INT8 IMMA GEMM (int8*int8->int32) followed by a separate dequantize kernel. The correct cuBLAS parameter mapping for A:[M,K] row-major, B:[K,N] col-major is: opA=CUBLAS_OP_T, opB=CUBLAS_OP_N, m=N, n=M, k=K, A_param=B(lda=K), B_param=A(ldb=K), ldc=N. Expect 2.0x-2.7x speedup.

## Challenge

Agents using cuBLAS for INT8 GEMM consistently get the parameter mapping wrong. The key confusion: cuBLAS is column-major, but A is [M,K] row-major and B is [K,N] column-major. The correct mapping requires treating the operation as C_col = B_col * A_col^T, which swaps the parameter order.

### Symptoms

- `cuBLAS returns INCORRECT_NUMERICAL with wrong parameter mapping`
- `Agent passes A as first matrix parameter when it should be B`
- `Leading dimension lda/ldb set to wrong values`
- `Even when results are correct, agent uses separate scale computation incorrectly`

## Solution

The correct cuBLAS parameter mapping for C=A@B where A:[M,K] row-major, B:[K,N] col-major:

Step 1: cuBLAS INT8 GEMM (int8*int8 -> int32 accumulator):
cublasGemmEx(handle,
    CUBLAS_OP_T, CUBLAS_OP_N,    // opA=T for B^T, opB=N for A
    N, M, K,                      // m=N, n=M (swapped!)
    &alpha,
    B, CUDA_R_8I, K,              // A_param = B (col-major [K,N], lda=K)
    A, CUDA_R_8I, K,              // B_param = A (row-major [M,K] as col-major [K,M]^T, ldb=K)
    &beta,
    C_int32, CUDA_R_32I, N,       // C output (col-major [N,M], ldc=N)
    CUBLAS_COMPUTE_32I,            // INT8 Tensor Core computation
    CUBLAS_GEMM_DEFAULT_TENSOR_OP);

Step 2: Dequantize kernel (int32 -> float32 * scale_a * scale_b):
__global__ void dequant_kernel(
    const int32_t* C_int32,       // column-major [N, M] from cuBLAS
    const float* scale_a,         // [M] per-token
    const float* scale_b,         // [N] per-channel
    float* output,                // row-major [M, N] output
    int M, int N) {
  int row = blockIdx.y;
  int col = blockIdx.x * blockDim.x + threadIdx.x;
  if (row < M && col < N) {
    int idx_cm = row + col * M;              // col-major read
    float val = (float)C_int32[idx_cm] * scale_a[row] * scale_b[col];
    output[row * N + col] = val;             // row-major write
  }
}

Launch: dequant_kernel<<<dim3((N+255)/256, M), 256>>>(C_int32, scale_a, scale_b, output, M, N);

### Implementation

```cuda
Complete implementation pattern:

1. Allocate int32 temp buffer: torch::empty({N, M}, int32) for column-major cuBLAS output
2. Call cublasGemmEx with CUBLAS_COMPUTE_32I and CUBLAS_GEMM_DEFAULT_TENSOR_OP
3. Launch dequant kernel to convert int32 -> float32 with per-token and per-channel scaling
4. Reuse cuBLAS handle across calls (create once, use many times)

Key points:
- B is passed as the first matrix (A_param in cuBLAS) because we compute B^T * A^T^T = B * A^T
- opA=CUBLAS_OP_T transposes B from col-major [K,N] to appear as row-major [N,K]
- opB=CUBLAS_OP_N keeps A as-is (row-major [M,K] interpreted as col-major [K,M])
- The result C is column-major [N,M], so ldc=N and indexing is row + col*M
```

## Key Lessons

- cuBLAS parameter mapping for A:[M,K] row-major, B:[K,N] col-major: opA=T, opB=N, m=N, n=M, k=K. First matrix param is B (lda=K), second is A (ldb=K). ldc=N.
- cuBLAS outputs column-major. The temp buffer is [N,M] in column-major order. The dequant kernel must read it as column-major: idx = row + col*M.
- Use CUBLAS_COMPUTE_32I with CUBLAS_GEMM_DEFAULT_TENSOR_OP for INT8 IMMA. This enables Tensor Core int8 computation with int32 accumulation.
- The dequantize kernel applies: float_val = (float)int32_acc * scale_a[row] * scale_b[col]. Both scale_a and scale_b are float* device pointers, NOT scalar floats.
- Reuse the cuBLAS handle across calls. Creating a new handle each call adds ~200us overhead. Use a static handle or thread-local handle.
- cuBLAS+dequant is 2x-2.7x speedup. CUTLASS fused epilogue is 4x-6x. The difference comes from eliminating the extra kernel launch and int32 memory traffic.
- The complete flow: (1) cuBLAS int8*int8->int32 into temp, (2) dequant kernel: int32 * scale_a[M] * scale_b[N] -> float32 output. Two kernel launches total.
