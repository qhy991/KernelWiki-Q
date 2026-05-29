---
id: exp-r-20260502-180009-dps-contiguous-copyback
title: sol_execbench_gemm
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
---

DPS mode main.cpp creates contiguous copy of output C, writes to copy, but fails to write back to original C

### Symptoms

- `correctness 检查失败：C 全为零或未修改`
- `copy-back 条件判断不正确`

## Solution

DPS=true 模式下，SOL-ExecBench 框架保证传入的输出 C 已经是 contiguous 且预分配好的。直接对 C.data_ptr() 操作即可，不需要创建拷贝。不要对输出 tensor 调用 `.contiguous()`。

## Key Lessons

- DPS=true 模式下，输出 tensor C 由框架预分配，保证 contiguous。直接用 C.data_ptr() 写入，不要创建拷贝。
- 对输入 tensor 调用 .contiguous() 是安全的（只读），但对输出 tensor 调用 .contiguous() 会创建独立拷贝，写入不会反映到原始 tensor。
- 常见的错误 copy-back 模式: `if (!C.is_contiguous()) C.copy_(C_c)` —— 当 C 是 contiguous 时不会执行 copy-back，输出丢失。
- 正确的 DPS 模式：直接操作 C，不创建中间拷贝，不需要 copy-back 逻辑。
