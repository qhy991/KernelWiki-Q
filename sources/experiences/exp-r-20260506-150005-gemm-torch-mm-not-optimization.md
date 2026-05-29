---
id: exp-r-20260506-150005-gemm-torch-mm-not-optimization
title: 'SOL-ExecBench GEMM: torch.mm wrapper is not a valid optimization'
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

Wrapping torch.mm or torch.matmul in the run() function is not a valid optimization - it IS the reference baseline. Achieves only ~1.17x because measurement noise, not real speedup.

## Challenge

Agent generates a Triton or Python solution that just calls torch.mm(A, B.T, out=C) or torch.matmul(A, B.T, out=C). This is functionally equivalent to the reference baseline and achieves only ~1.17x 'speedup' from measurement noise.

### Symptoms

- `Solution kernel.py contains only: torch.matmul(A, B.T, out=C)`
- `Speedup is around 1.0-1.2x - not a real optimization`
- `Spec declares 'triton' language but code is pure PyTorch`
- `Verification passes correctness but performance is meaningless`

## Solution

Do not submit torch.mm/torch.matmul as the kernel implementation. For GEMM optimization tasks, the solution must use a different implementation path (cuBLAS direct API, custom CUDA kernel, or Triton kernel) that can outperform the PyTorch reference.

### Implementation

```cuda
1. For CUDA C++ solutions: use cublasGemmEx directly with persistent handle
2. For Triton solutions: implement actual Triton kernel with tl.dot(), not torch.mm wrapper
3. The reference baseline already uses torch's internal cuBLAS/cuBLASLt
4. To beat the baseline, you must either:
   - Use a more efficient library call (direct cuBLAS API avoiding torch overhead)
   - Custom kernel optimized for the specific problem shape
   - Triton kernel with better memory access patterns
5. If agent can only generate torch.mm, switch to cuda_cpp language
```

## Key Lessons

- torch.mm/torch.matmul is the reference baseline, not an optimization - never submit it as the solution.
- Real speedup requires bypassing PyTorch's dispatch overhead with direct cuBLAS API or custom kernel.
- For GEMM tasks, cuda_cpp with cublasGemmEx typically outperforms Triton for small batch sizes.
- If the solution's run() function only calls torch operations, it will not achieve meaningful speedup.
- Triton solutions must use tl.dot() with proper block tiling, not delegate to PyTorch.
- Speedup ~1.17x with torch.mm is measurement noise, not real optimization.
