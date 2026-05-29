---
id: exp-r-20260502-180006-cublaslt-handle-overhead
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
impl_family: cublaslt
---

cuBLASLt handle created/destroyed per kernel call causing extreme performance degradation (0.017x speedup)

### Symptoms

- `speedup_factor 远小于 1.0（如 0.017x ~ 0.03x）`
- `latency_ms 远大于 reference_latency_ms`
- `每次 kernel launch 延迟在 1.5ms ~ 3.5ms（基准仅 0.05ms）`

## Challenge

LLM 在每次 gemm_launch 调用中都执行 cublasLtCreate + cublasLtDestroy + cudaMalloc + cudaFree。对于 SOL-ExecBench 的小矩阵 GEMM（如 M=10），cuBLASLt handle 的创建/销毁开销远大于实际计算时间，导致 speedup 仅 0.017x（比基准慢约 60 倍）。


## Solution

方案1（推荐）：使用 cuBLASLt 的 batched API 或在 main.cpp 中用 static/thread_local 变量复用 handle。
方案2：改用 cuBLAS 的普通 cublasSgemmEx/cublasGemmEx 接口，开销更低。
方案3：如果 CUTLASS 可用，优先使用 CUTLASS（无 handle 创建开销）。

## Key Lessons

- cuBLASLt handle 创建/销毁开销约 0.5-1ms，对于小矩阵（M<=50）的 GEMM（计算仅 ~0.05ms），这会导致速度比基准慢几十倍。
- 绝对不要在 kernel launch 函数内创建/销毁 cuBLAS handle。应在初始化阶段创建，整个 session 复用。
- cuBLASLt workspace 也应复用而非每次 cudaMalloc/cudaFree。
- 对于极小矩阵（M=10），CUTLASS 可能比 cuBLAS 更合适，因为 CUTLASS 无 handle 开销且可以利用 tensor core。
- speedup 远小于 1.0 时，首先排查是否有 handle/workspace 的重复创建销毁。
