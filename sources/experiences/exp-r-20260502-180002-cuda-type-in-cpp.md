---
id: exp-r-20260502-180002-cuda-type-in-cpp
title: sol_execbench_bf16_int8_gemm
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
captured_at: '2026-05-02'
confidence: inferred
reproducibility: concept
impl_family: custom_cuda
---

SOL-ExecBench static gate rejects main.cpp containing CUDA-only constructs like __nv_bfloat16

### Symptoms

- `sol_execbench_update_sources 返回 static_gate_error`
- `错误信息: `main.cpp` contains CUDA-only construct `__nv_bfloat16`. `.cpp` wrapper files are compiled by the host compiler`

## Solution

将所有 CUDA-only 类型和计算移到 .cu 文件中。main.cpp 只使用 torch::Tensor、标准 C++ 类型和 void* 指针。bf16 数据通过 `torch::Tensor` 的 `data_ptr()` 以 `void*` 传递给 .cu 中的 launcher 函数。

## Key Lessons

- SOL-ExecBench 的 .cpp 文件由 g++ 编译，绝不能包含任何 CUDA 内建类型（__nv_bfloat16、__half、__nv_bfloat162 等）。
- CUDA-only 类型必须全部留在 .cu 文件中。.cpp 和 .cu 之间通过 void* 指针 + 普通 C 类型（int, float, cudaStream_t）交互。
- 如果需要 bf16 类型，在 .cu 中使用 `#include <cuda_bf16.h>` 或 `#include <cutlass/bfloat16.h>`，在 .cpp 中只用 `torch::Tensor`。
- static_gate 会扫描 .cpp 文件中的 `__nv_` 前缀标识符来检测 CUDA-only 构造。
