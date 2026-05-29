---
id: exp-r-20260506-160006-sol-execbench-compile-failure
title: 'SOL-ExecBench: common compilation failure patterns'
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
captured_at: '2026-05-06'
confidence: inferred
reproducibility: snippet
impl_family: cublaslt
---

SOL-ExecBench compilation failures often stem from missing CUDA includes, incorrect function signatures, or linker errors. Most are fixable by following the static_gate error messages.

## Challenge

SOL-ExecBench compilation fails with various errors: missing includes, undefined symbols, incorrect signatures, or linker failures. The agent often retries the same failing code without understanding the root cause.

### Symptoms

- `Compilation failed: subprocess.CalledProcessError: ninja returned non-zero exit status`
- `identifier 'cublasLtSetStream' is not declared`
- `undefined symbol: benchmark_kernel`
- `'getCurrentCUDAStream' is not a member of 'at::cuda'`
- `no instance of constructor 'cublasGemmEx' matches the argument list`

## Solution

Read the compilation error carefully and fix the specific issue. Common fixes: add missing includes, use correct API signatures, ensure linker flags are correct.

### Implementation

```cuda
1. Read the full compilation error output (not just the exit code)
2. For missing includes: add #include <cuda_runtime.h>, #include <cublas_v2.h>, etc.
3. For undefined symbols: check that all source files are included in sol_execbench_update_sources
4. For API errors: check the exact function signature in CUDA/cuBLAS documentation
5. For linker errors: ensure CUDA libraries are linked (cublas, cudart, etc.)
6. Run compile_smoke first before full verification
7. Fix one error at a time - don't rewrite everything
```

## Key Lessons

- Always read the full compilation error, not just the exit code.
- Missing #include <cuda_runtime.h> is the most common CUDA compilation error.
- cuBLAS functions require #include <cublas_v2.h> and -lcublas linker flag.
- All source files must be included in sol_execbench_update_sources for linking.
- Run compile_smoke before full verification to catch build issues early.
- Fix one error at a time - rewriting everything often introduces new errors.
