---
id: exp-r-20260502-180011-int8-gemm-cutlass-template
title: sol_execbench_int8_gemm
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
reproducibility: snippet
impl_family: cublas
---

CUTLASS INT8 GEMM template instantiation fails with incomplete type errors in mma_tensor_op_policy.h

### Symptoms

- `编译错误: mma_tensor_op_policy.h(58): incomplete type is not allowed`
- `编译错误: mma_tensor_op.h: template instantiation depth exceeds maximum`
- `CUTLASS BF16/FP16 GEMM 编译正常，但 INT8 编译失败`
- `错误指向 CUTLASS 内部头文件而非用户代码`

## Challenge

使用 CUTLASS 库实现 INT8 GEMM 时，模板实例化阶段编译失败。典型错误：cutlass/gemm/warp/mma_tensor_op_policy.h(58): error: incomplete type is not allowed。此错误在多个 INT8 GEMM 实验中反复出现（m768_n4304_k1152、m768_n1152_k1152 等），但同样的 CUTLASS 模板在 BF16/FP16 GEMM 上工作正常。根本原因是 CUTLASS 的 INT8 Tensor Core 配置（OpMultiplyAdd + int32_t accumulator）对 SM architecture 和 instruction shape 的组合要求更严格，LLM 生成的配置参数经常不兼容。


## Solution

对于 SOL-ExecBench INT8 GEMM 任务，不要将 CUTLASS 作为首选方案。改用 cuBLAS cublasGemmEx 作为第一选择，它能可靠地处理 INT8 Tensor Core 操作。CUTLASS INT8 模板在当前版本（截至 CUTLASS 3.x）对 int8_t + int32_t accumulator 的支持不如 BF16/FP16 成熟。

### Implementation

```cuda
1. 首选方案：cuBLAS cublasGemmEx with CUDA_R_8I datatype and CUBLAS_GEMM_DEFAULT_TENSOR_OP algo
2. 正确的 row-major → col-major 映射：problem C=A@B^T with A[M,K] B[N,K] → cuBLAS 参数 m=N, n=M, k=K, a_ptr=B, b_ptr=A, c_ptr=C
3. 仅当 cuBLAS 无法满足性能要求时，才考虑 CUTLASS INT8，且需要仔细验证 SM arch / instruction shape 兼容性
4. CUTLASS INT8 需要使用 GemmIdentityTensorLayout<RowMajor> 和正确的 ArchTag (Sm80/Sm89)
```

## Key Lessons

- CUTLASS INT8 GEMM 模板实例化失败率高，不应作为 INT8 GEMM 的首选方案。cuBLAS cublasGemmEx 更可靠。
- CUTLASS incomplete type 错误通常是因为 LLM 生成的 SM architecture / instruction shape / layout 组合不兼容。CUTLASS 内部对 INT8 有更严格的约束。
- 同一份 CUTLASS 模板代码在 BF16/FP16 上能编译通过但 INT8 失败，说明 INT8 的 Tensor Core instruction shape 配置空间更窄。
- 对于 SOL-ExecBench PI-int8 类任务，推荐的优先级：cuBLAS cublasGemmEx > 手写 tiling kernel > CUTLASS INT8。
- 如果必须用 CUTLASS INT8，需先用 CUTLASS profiler 确认目标 SM arch 支持的 INT8 kernel 配置。
