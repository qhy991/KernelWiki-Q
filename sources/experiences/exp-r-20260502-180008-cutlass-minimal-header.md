---
id: exp-r-20260502-180008-cutlass-minimal-header
title: sol_execbench_bf16_gemm
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
- cute-dsl
captured_at: '2026-05-02'
confidence: inferred
reproducibility: snippet
impl_family: cutlass
---

LLM generates minimal CUTLASS header stubs (arch.h, bfloat16.h, gemm.h) that compile fail with undefined types

### Symptoms

- `编译错误: identifier '__nv_bfloat16' is undefined`
- `编译错误: namespace 'cutlass::gemm' has no member 'GemmShape'`
- `编译错误: expected a '>' 或 expected a ';'`
- `solution.json sources 中包含 cutlass/ 子目录`

## Challenge

LLM 尝试在 solution.json 的 sources 中内联生成 CUTLASS 头文件的精简版本（如 cutlass/include/cutlass/arch.h, cutlass/bfloat16.h, cutlass/gemm/device/gemm.h），但这些精简版本缺少关键类型定义（GemmShape, GemmCoord, bfloat16_t 等），导致编译失败。SOL-ExecBench 的 compile_options 已经通过 -I/home/qinhaiyan/cutlass/include 指向本地 CUTLASS 安装，不需要自行生成头文件。


## Solution

不要在 solution.json 的 sources 中自行生成 CUTLASS 头文件。SOL-ExecBench 的 compile_options 已经设置了 -I 指向系统 CUTLASS 安装路径（如 -I/home/qinhaiyan/cutlass/include）。只需在 kernel.cu 中正常 #include <cutlass/...> 即可。

### Implementation

```cuda
1. kernel.cu 中使用 `#include <cutlass/cutlass.h>`, `#include <cutlass/gemm/device/gemm.h>` 等
2. solution.json 的 sources 只包含 kernel.h, kernel.cu, main.cpp
3. 不要在 sources 中创建 cutlass/ 子目录或任何 CUTLASS 头文件
4. compile_options 的 cuda_cflags 中已有 -I 指向 CUTLASS include 路径
```

## Key Lessons

- 不要在 solution.json 中自行生成 CUTLASS 头文件的精简版本。系统 CUTLASS 安装已通过 -I 路径可用。
- 自行生成的精简头文件必然缺少大量依赖（CUTLASS 头文件之间有复杂的相互依赖），会导致难以调试的编译错误。
- SOL-ExecBench compile_options 中的 -I 路径已经正确配置，只需正常 include 即可。
- 如果 CUTLASS include 路径不在 compile_options 中，说明该 benchmark 不支持 CUTLASS，应改用其他方案（cuBLAS、手写 kernel 等）。
