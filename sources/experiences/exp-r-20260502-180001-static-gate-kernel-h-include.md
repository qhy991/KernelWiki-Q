---
id: exp-r-20260502-180001-static-gate-kernel-h-include
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

SOL-ExecBench static gate rejects kernel.h that uses cudaStream_t without including <cuda_runtime.h>

### Symptoms

- `sol_execbench_update_sources 返回 static_gate_error`
- `错误信息: `kernel.h` uses `cudaStream_t` but does not include `<cuda_runtime.h>``

## Challenge

SOL-ExecBench static gate 拒绝了 kernel.h，因为它声明了 cudaStream_t 参数但未包含 <cuda_runtime.h>。main.cpp 由 g++ 编译，无法通过传递性从 .cu 文件获得 CUDA 类型定义，导致编译失败。


## Solution

在 kernel.h 中添加 `#include <cuda_runtime.h>`。头文件必须自包含（self-contained），不能依赖其他翻译单元的传递 include。

## Key Lessons

- SOL-ExecBench 的 .cpp 文件由 g++ 编译、.cu 文件由 nvcc 编译。kernel.h 被 main.cpp 包含，因此必须提供完整的类型定义，不能依赖 .cu 文件的传递 include。
- 头文件自包含原则：如果 header 声明使用了某个类型，该 header 必须自己 #include 对应的头文件。
- static_gate 检查会在 sol_execbench_update_sources 阶段拦截，不需要等编译才发现问题。
