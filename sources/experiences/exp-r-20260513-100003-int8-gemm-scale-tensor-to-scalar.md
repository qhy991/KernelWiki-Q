---
id: exp-r-20260513-100003-int8-gemm-scale-tensor-to-scalar
title: 'SOL-ExecBench INT8 GEMM: scale_a/scale_b are per-element tensors, not scalars'
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

In SOL-ExecBench PI-int8 tasks, scale_a is [M] float32 (per-token) and scale_b is [N] float32 (per-channel). Calling scale_a.item<float>() on a multi-element tensor raises RuntimeError: 'a Tensor with 50 elements cannot be converted to Scalar'. Scale must be applied element-wise in a CUDA kernel or via broadcasting.

## Challenge

Agent writes main.cpp code that treats scale_a and scale_b as scalar values, calling .item<float>() on tensors with M or N elements. This crashes at runtime with 'a Tensor with X elements cannot be converted to Scalar'.

### Symptoms

- `RuntimeError: a Tensor with 50 elements cannot be converted to Scalar`
- `Error occurs in the run() function when accessing scale_a.item<float>()`
- `The kernel function signature takes float scale_a, float scale_b instead of tensor references`
- `Compilation succeeds but full verification fails immediately`

## Solution

Pass scale_a and scale_b as float* device pointers to the CUDA kernel, then apply per-element in the kernel. Never call .item<float>() on per-token/per-channel scale tensors.

### Implementation

```cuda
1. kernel.h: void gemm_launcher(..., const float* scale_a, const float* scale_b, ...)
2. main.cpp: launch_gemm(A, B, scale_a.data_ptr<float>(), scale_b.data_ptr<float>(), C)
3. kernel.cu: apply scale_a[row] and scale_b[col] inside the kernel
4. For cuBLAS path: do INT8 GEMM first to get int32 accumulator, then launch separate scale+dequant kernel that applies scale_a[row] * scale_b[col] per element
```

## Key Lessons

- scale_a is float32 [M] per-token, scale_b is float32 [N] per-channel. They are NEVER scalar floats. Always pass as float* device pointers.
- Never call .item<float>() on scale tensors — they have M or N elements. Use .data_ptr<float>() to get the device pointer.
- The DPS signature is: run(A:int8[M,K], B:int8[K,N], scale_a:float32[M], scale_b:float32[N], C:bfloat16[M,N]). All 5 tensors are passed in.
- In the dequantize kernel: output[row*N+col] = bf16(int32_acc[row*N+col] * scale_a[row] * scale_b[col]). Each element uses its own row and column scale.
- If your kernel function signature has 'float scale_a' (scalar), it is WRONG for PI-int8 tasks.
