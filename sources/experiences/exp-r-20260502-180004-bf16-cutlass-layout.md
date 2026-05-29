---
id: exp-r-20260502-180004-bf16-cutlass-layout
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
reproducibility: concept
impl_family: cutlass
---

CUTLASS GEMM layout mismatch: definition B shape is [N,K] row-major (B.T stored), but code declares ColumnMajor causing wrong computation

### Symptoms

- `编译通过但 correctness 检查失败`
- `NMSE 远超容差阈值`
- `CUTLASS Gemm 使用 LayoutInputB = ColumnMajor 但 B 实际存储为 RowMajor [N,K]`

## Challenge

SOL-ExecBench 的 BF16 GEMM 定义为 C = A @ B.T，其中 A=[M,K] row-major, B=[N,K] row-major（已经是 B.T 的物理存储）。LLM 生成的 CUTLASS 代码将 B 声明为 ColumnMajor layout，导致 CUTLASS 按列优先解读 B 的内存，实际计算变成了 A @ B（而非 A @ B.T），结果完全错误。


## Solution

SOL-ExecBench GEMM 定义中 B shape 为 [N,K] row-major，物理存储就是 row-major。要计算 C = A @ B.T，CUTLASS 的 layout 应该都设为 RowMajor，因为 A[M,K] row-major 和 B[N,K] row-major 在 CUTLASS RowMajor 下自动处理 A * B^T（B 的 leading dim 为 K，CUTLASS 会自动转置）。

## Key Lessons

- SOL-ExecBench GEMM 的 B shape [N,K] 表示 B 按 [N,K] row-major 存储，即 B^T 的物理布局。C = A @ B.T 等价于 CUTLASS 的 RowMajor A * RowMajor B with ldb=K。
- CUTLASS device::Gemm 的 LayoutInputB 描述的是 B 矩阵在内存中的实际 layout，不是数学意义上的转置关系。如果 B 数据在内存中是 row-major 存储，LayoutInputB 就应该是 RowMajor。
- 常见错误：看到 B^T 就想当然将 LayoutInputB 设为 ColumnMajor。实际上 ColumnMajor 会让 CUTLASS 按列优先解读同一块内存，导致完全不同的索引计算。
- leading dimension 的计算：RowMajor 矩阵的 ld = 列数（K 对 B[N,K]），ColumnMajor 矩阵的 ld = 行数。
