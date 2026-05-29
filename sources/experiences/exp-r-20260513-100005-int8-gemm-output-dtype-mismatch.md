---
id: exp-r-20260513-100005-int8-gemm-output-dtype-mismatch
title: 'SOL-ExecBench INT8 GEMM: output tensor C dtype depends on task — always check
  C.scalar_type() at runtime'
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

In SOL-ExecBench PI-int8 tasks, the output tensor C dtype varies by task. Some tasks pass C as float32, others as bfloat16. The agent MUST check C.scalar_type() at runtime and write the matching dtype. Enforcing a hardcoded dtype causes RuntimeError. The complete cuBLAS+dequant template uses bfloat16 output and passes verification on m10_n1024_k2048, m10_n1024_k4096, m10_n2560_k1024, and m50_n1024_k2048.

## Challenge

Agent hardcodes a specific dtype assumption for C (either bfloat16 or float32) without checking the actual tensor passed by the framework. Different SOL-ExecBench PI-int8 tasks allocate C as different dtypes. Hardcoding the wrong dtype causes TORCH_CHECK failures or silent data corruption.

### Symptoms

- `RuntimeError: C must be float32 (output buffer)`
- `TORCH_CHECK failure on C.dtype()`
- `Kernel compiles and runs but output validation fails`

## Solution

Check C.scalar_type() at runtime in main.cpp. Branch the dequant kernel or output write based on the actual dtype. Never hardcode a dtype assumption. For the standard cuBLAS+dequant template that works on most PI-int8 tasks, writing bfloat16 output (via __float2bfloat16) is correct because those tasks allocate C as bfloat16. For tasks that allocate C as float32, write float32 directly.

### Implementation

```cuda
## Runtime dtype check in main.cpp
```cpp
void run(torch::Tensor A, torch::Tensor B,
         torch::Tensor scale_a, torch::Tensor scale_b,
         torch::Tensor C) {
    int M = A.size(0), K = A.size(1), N = B.size(1);
    auto workspace = torch::empty({M, N},
        torch::dtype(torch::kInt32).device(A.device()));

    // cuBLAS GEMM call (same regardless of output dtype)
    gemm_int8_dequant_cuda(
        A.data_ptr<int8_t>(), B.data_ptr<int8_t>(),
        scale_a.data_ptr<float>(), scale_b.data<float>(),
        C.data_ptr(), workspace.data_ptr<int32_t>(),
        M, N, K, at::cuda::getCurrentCUDAStream(),
        C.scalar_type() == at::kBFloat16);  // pass dtype flag to kernel
}
```

## In dequant kernel: branch on dtype
```cuda
__global__ void dequant_kernel(
    const int32_t* workspace,
    const float* scale_a, const float* scale_b,
    void* output, int M, int N, bool output_is_bf16) {
    int row = blockIdx.y * blockDim.y + threadIdx.y;
    int col = blockIdx.x * blockDim.x + threadIdx.x;
    if (row >= M || col >= N) return;
    float val = (float)workspace[row * N + col] * scale_a[row] * scale_b[col];
    if (output_is_bf16) {
        ((uint16_t*)output)[row * N + col] = __bfloat16_as_ushort(__float2bfloat16(val));
    } else {
        ((float*)output)[row * N + col] = val;
    }
}
```

## DO NOT:
// TORCH_CHECK(C.dtype() == torch::kFloat32)  // WRONG: some tasks use bf16
// TORCH_CHECK(C.dtype() == torch::kBFloat16)  // WRONG: some tasks use f32
// Always check at runtime instead.
```

## Key Lessons

- SOL-ExecBench PI-int8 output C dtype varies by task. Some tasks use bfloat16, others use float32. ALWAYS check C.scalar_type() at runtime. Never hardcode a dtype assumption.
- The verified cuBLAS+dequant template writes bfloat16 output and passes on m10_n1024_k2048, m10_n1024_k4096, m10_n2560_k1024, m50_n1024_k2048. If verification passes with bfloat16, keep it. If it fails, switch to float32.
- When seeing 'C must be float32 (output buffer)' error, the fix is to check C.scalar_type() and write the matching dtype. Do NOT blindly switch to float32 for all tasks.
- The dequant kernel should branch on output dtype: __float2bfloat16 for bfloat16, plain float cast for float32. Pass a bool flag from main.cpp based on C.scalar_type().
- The definition.json DPS signature is advisory — the actual runtime tensor dtype is authoritative. Always trust the runtime type over the declared type.
