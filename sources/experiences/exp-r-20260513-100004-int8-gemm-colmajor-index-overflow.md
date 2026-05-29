---
id: exp-r-20260513-100004-int8-gemm-colmajor-index-overflow
title: 'SOL-ExecBench INT8 GEMM: illegal memory access from wrong col-major index
  in dequant kernel'
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
impl_family: cublas
---

When cuBLAS outputs int32 results to a temp buffer in column-major order, the subsequent dequantization kernel must index the temp buffer as col-major (row + col*M), NOT row-major (col*N + row). Using wrong indexing causes CUDA illegal memory access or reads past buffer bounds.

## Challenge

Agent performs INT8 GEMM via cuBLAS into a temp int32 buffer, then launches a dequant kernel to apply scale and convert to float. The temp buffer from cuBLAS is column-major, but the dequant kernel indexes it with row-major stride (col*N + row), causing out-of-bounds reads.

### Symptoms

- `CUDA error: an illegal memory access was encountered`
- `CUDA kernel errors might be asynchronously reported at some other API call`
- `Kernel sometimes works for small matrices but crashes for larger ones`
- `Crash occurs in the dequantize kernel, not in cuBLAS`

## Solution

For a column-major buffer of shape [M, N] output by cuBLAS, index element (row, col) as row + col * M. For a row-major buffer, index as row * N + col. Always match the indexing to the layout of the buffer.

### Implementation

```cuda
// cuBLAS outputs to temp buffer in column-major:
// temp[row][col] = temp[row + col * M] in column-major

__global__ void dequant_kernel(const int32_t* temp, ..., int M, int N) {
    int row = blockIdx.y;
    int col = blockIdx.x * blockDim.x + threadIdx.x;
    if (row < M && col < N) {
        int idx_temp = row + col * M;  // column-major indexing
        float val = (float)temp[idx_temp] * scale_a[row] * scale_b[col];
        output[row * N + col] = (bfloat16)val;  // output is row-major
    }
}
```

## Key Lessons

- cuBLAS always outputs in column-major format. If you write results to a temp buffer and read it in a custom kernel, you MUST use column-major indexing: row + col * M.
- Mixing layout conventions between cuBLAS output (col-major) and custom kernel indexing (row-major) causes silent data corruption or illegal memory access.
- When using cuBLAS + separate dequant kernel pattern, explicitly document which buffers are col-major and which are row-major. Never assume all buffers share the same layout.
- The crash may appear asynchronously — the illegal access happens in the dequant kernel but may be reported at the next CUDA API call.
- For large N (e.g., N=8192), the wrong index col*N+row can reach col*8192+row which easily exceeds M*N buffer size, causing the illegal memory access.
