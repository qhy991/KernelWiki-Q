---
id: exp-r-20260502-180003-dps-void-signature
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
---

SOL-ExecBench DPS=true requires void run(*inputs, *outputs) signature, not non-void return

### Symptoms

- `sol_execbench_update_sources 返回 static_gate_error`
- `错误信息: `spec.destination_passing_style=true` requires a void entry point called as `run(*definition.inputs, *definition.outputs)` with output tensors mutated in-place; `main.cpp` appears to define a non-void `run(...)` signature.`

## Challenge

LLM 生成的 main.cpp 中 run() 函数返回了 torch::Tensor 而非 void。当 definition.json 中 destination_passing_style=true 时，SOL-ExecBench 要求 entry point 签名为 `void run(*inputs, *outputs)`，即输出 tensor 作为尾部参数传入并原地修改。


## Solution

将 run() 改为 void 返回类型，将输出 tensor C 作为最后一个参数传入（DPS=true 时 inputs + outputs 按顺序排列）。例如：`void run(torch::Tensor A, torch::Tensor B, torch::Tensor C)`，其中 C 是预分配的输出，kernel 写入 C 的内存。

## Key Lessons

- DPS (Destination Passing Style) 是 SOL-ExecBench 的关键约定。DPS=true 时，输出 tensor 作为 run() 的尾部参数传入，函数必须返回 void 并原地修改输出。
- DPS=false 时，run() 返回输出 tensor。
- 检查 definition.json 中的 destination_passing_style 字段来决定签名风格。
- DPS=true 的参数顺序是 (input1, input2, ..., output1, output2, ...)，由 definition.inputs 和 definition.outputs 的顺序决定。
