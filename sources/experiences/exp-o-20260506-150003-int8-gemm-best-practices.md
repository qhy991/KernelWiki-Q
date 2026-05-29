---
id: exp-o-20260506-150003-int8-gemm-best-practices
title: 'SOL-ExecBench INT8 GEMM: comprehensive best practices'
experience_type: optimization
source_category: agent-experiment
architectures:
- sm90
tags:
- gemm
- fine-grained-quantization
- vectorized-loads
kernel_types:
- gemm
languages:
- cuda-cpp
captured_at: '2026-05-06'
confidence: inferred
reproducibility: concept
techniques:
- fine-grained-quantization
- vectorized-loads
impl_family: cublas
---

Comprehensive best practices for SOL-ExecBench INT8 GEMM tasks based on multiple successful experiments.

## Challenge

INT8 GEMM implementation requires careful consideration of multiple factors: library choice, memory layout, accumulation type, and batch size optimization. Different approaches have different trade-offs.

### Symptoms

- `CUTLASS INT8 template instantiation failures`
- `cuBLAS handle overhead for small batches`
- `Row-major to col-major mapping confusion`
- `INT8 accumulation overflow issues`

## Solution

Follow a tiered implementation strategy based on batch size and requirements:

Tier 1 (Recommended): cuBLAS cublasGemmEx
- Best for: M > 16, production use
- Pros: Reliable, well-tested, Tensor Core utilization
- Cons: High overhead for small M

Tier 2 (Small M): DP4A Vectorized
- Best for: M <= 16, performance-critical
- Pros: Low overhead, good for small batches
- Cons: More complex implementation

Tier 3 (Advanced): CUTLASS INT8
- Best for: Custom epilogues, complex layouts
- Pros: Flexible, can fuse operations
- Cons: Template instantiation issues, debugging complexity

INT8 GEMM implementation checklist:

1. Problem Definition:
   - C[M,N] = A[M,K]_int8 @ B[N,K]_int8^T -> C[M,N]_int32
   - Reference: torch._int_mm(A, B.T)
   - B.T is critical - LLMs often miss this transpose

2. cuBLAS Implementation:
   - Handle: Create once, reuse across calls
   - Parameters: m=N, n=M, k=K, a=B, b=A
   - Types: CUDA_R_8I input, CUDA_R_32I compute
   - Algorithm: CUBLAS_GEMM_DEFAULT_TENSOR_OP

3. DP4A Implementation:
   - Grid: (ceil(N/32), M) - one warp per row
   - Use __dp4a() for INT8 dot product
   - Vectorize with int4 loads (128-bit)
   - No shared memory for small K

4. CUTLASS Implementation:
   - Use GemmIdentityTensorLayout<RowMajor>
   - Match SM architecture (Sm80/Sm89)
   - Use correct MMA instruction shape
   - Test with CUTLASS profiler first

5. Verification:
   - Run compile smoke first
   - Check for scaffold placeholders
   - Verify correctness across all workloads
   - Measure speedup against reference

## Key Lessons

- INT8 GEMM has multiple viable approaches - choose based on batch size and requirements.
- cuBLAS cublasGemmEx is the safest choice for most cases - start here.
- DP4A vectorized is optimal for small M (M<=16) - use when cuBLAS overhead is too high.
- CUTLASS INT8 is powerful but fragile - only use after working baseline exists.
- Always handle row-major to col-major mapping correctly: m=N, n=M, k=K for C=A@B^T.
- INT8 accumulation must use CUDA_R_32I - never CUDA_R_8I (will overflow).
- Handle reuse is critical for small GEMM - create cuBLAS handle once.
- Run compile smoke before full verification to catch build issues early.
- Check for scaffold placeholders before verification - static gate will block.
- Partial results can be used as starting point for next round.
