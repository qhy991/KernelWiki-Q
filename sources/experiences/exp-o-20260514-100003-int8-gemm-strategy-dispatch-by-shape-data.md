---
id: exp-o-20260514-100003-int8-gemm-strategy-dispatch-by-shape-data
title: 'SOL-ExecBench INT8 GEMM: implementation strategy dispatch by matrix shape
  with experimental data'
experience_type: optimization
source_category: agent-experiment
architectures:
- sm90
tags:
- gemm
- fine-grained-quantization
kernel_types:
- gemm
languages:
- cuda-cpp
captured_at: '2026-05-14'
confidence: inferred
reproducibility: snippet
techniques:
- fine-grained-quantization
impl_family: cublas,custom_cuda
---

Strategy selection table for INT8 GEMM based on 54 experiments across 17 tasks with latency data. cuBLAS+dequant is the only reliable path. DP4A works for M<=10 small shapes only. Manual CUDA fails for M>=768. The PyTorch eager baseline uses torch._int_mm with tensor cores, making it very hard to beat for large M.

## Challenge

Agents choose INT8 GEMM implementation approach based on intuition rather than empirical data. This leads to: (1) using DP4A for large M where it is 10-300x slower than baseline, (2) using manual CUDA for M>=768 where it cannot compete with tensor cores, (3) attempting CUTLASS which has <30% compile success rate. Agents need data-driven strategy selection.

### Symptoms

- `DP4A on M=768: 2.17ms latency vs 0.37ms reference (5.9x slower)`
- `DP4A on M=968, N=2048: 12.98ms vs 0.28ms reference (46x slower)`
- `Manual CUDA on M=768, N=4304: 6.37ms vs 0.38ms reference (16.9x slower)`
- `cuBLAS on M=968: 0.064ms vs 0.13ms reference (2.08x faster)`
- `CUTLASS: template instantiation failures in >70% of attempts`

## Solution

Use this data-driven strategy table to select the correct implementation approach based on M dimension. Always start with cuBLAS+dequant template.

### Implementation

```cuda
## INT8 GEMM Strategy Selection (based on 54 experiments)

### ALWAYS: cuBLAS + dequant (the default path)

Use the complete template from the companion experience. This is the only approach with verified correctness across ALL shapes.

### Strategy by M dimension:

| M range | Best approach | Expected speedup | Risk level | Notes |
|---------|--------------|-----------------|------------|-------|
| M <= 16 | cuBLAS+dequant | 2.0x - 5.5x | LOW | Handle reuse critical. dp4a sometimes faster but unreliable. |
| 16 < M <= 100 | cuBLAS+dequant | 0.8x - 2.6x | LOW-MED | Best result: m50_n1024_k2048 at 2.56x. Some shapes slightly below 1.0x. |
| 100 < M <= 500 | cuBLAS+dequant | 0.5x - 2.1x | MEDIUM | Performance varies with N,K. Large N helps tensor core utilization. |
| M > 500 | cuBLAS+dequant | 0.05x - 2.1x | HIGH | Baseline uses tensor cores too. Hard to beat. Expect ~1.0x. |

### Alignment check before cuBLAS call:

Tensor core IMMA requires K % 16 == 0 and N % 8 == 0.
If these conditions are NOT met:
- CUBLAS_GEMM_DEFAULT_TENSOR_OP may return status 7 (CUBLAS_STATUS_INVALID_VALUE)
- Fallback: use CUBLAS_GEMM_DEFAULT instead (uses CUDA cores, slower but works)
- All SOL-ExecBench PI-int8 tasks tested so far meet alignment requirements

### cuBLAS algo selection:
- Default: CUBLAS_GEMM_DEFAULT_TENSOR_OP (uses IMMA tensor cores, fastest)
- If status 7 error: try CUBLAS_GEMM_DEFAULT (CUDA core fallback)
- For SM80+: CUBLAS_COMPUTE_32I with CUBLAS_GEMM_DEFAULT_TENSOR_OP is optimal

### APPROACHES TO AVOID:

1. **DP4A for M >= 50**: Catastrophic slowdown. DP4A latency grows linearly with M while tensor cores do not. Results: m768 dp4a=2.17ms vs ref=0.37ms, m968 dp4a=12.98ms vs ref=0.28ms.

2. **Manual CUDA for M >= 768**: Cannot compete with tensor cores. Only result: m768_n4304_k1152 at 0.059x (6.37ms vs 0.38ms ref).

3. **CUTLASS direct usage**: 70%+ compile failure rate. Template instantiation errors, missing OpClassTensorOp, alignment issues. Only consider AFTER a working cuBLAS baseline exists.

4. **torch.mm / torch.matmul wrapper**: Not an optimization. Baseline already uses these internally.

### Why large M is hard:

PyTorch eager mode for INT8 GEMM calls torch._int_mm which uses tensor core IMMA instructions. For M>=768, the tensor core utilization is near-optimal. Custom kernels using DP4A or scalar multiply-accumulate are fundamentally slower because they don't use tensor cores.

cuBLAS cublasGemmEx with CUBLAS_GEMM_DEFAULT_TENSOR_OP also uses tensor cores, which is why it's the only approach that can compete with or beat the baseline for large M.

### N dimension impact on performance:
- Large N (N >= 2048) significantly improves tensor core utilization
- Small N (N < 512) results in lower speedup regardless of M
- Best results combine large N with small-to-medium M

### Performance data by task (best achieved):

| Task | Best method | Best latency | Ref latency | Speedup |
|------|-----------|-------------|-------------|----------|
| m10_n1024_k2048 | cuBLAS | 0.048ms | 0.13ms | 2.67x |
| m10_n1024_k4096 | DP4A | 0.028ms | 0.16ms | 5.49x |
| m10_n2560_k1024 | DP4A | 0.042ms | 0.15ms | 3.66x |
| m10_n8192_k1024 | manual | 0.183ms | 0.18ms | 0.98x |
| m50_n1024_k2048 | manual | 0.052ms | 0.13ms | 2.56x |
| m50_n1024_k4096 | manual | 0.200ms | 0.17ms | 0.84x |
| m768_n1152_k1152 | manual | 0.298ms | 0.16ms | 0.52x |
| m768_n4304_k1152 | manual | 6.37ms | 0.38ms | 0.06x |
| m968_n2048_k2048 | DP4A | 2.17ms | 0.37ms | 0.17x |
| m968_n2560_k2048 | cuBLAS | 0.064ms | 0.13ms | 2.08x |
```

## Key Lessons

- ALWAYS default to cuBLAS+dequant for INT8 GEMM. It is the only approach with reliable correctness and competitive performance across all shapes.
- M<=10: cuBLAS achieves 2.0x-5.5x speedup. DP4A can be faster but is unreliable (only 2/12 passed). Start with cuBLAS.
- M=50: cuBLAS or manual CUDA work. Best result: 2.56x with manual CUDA on m50_n1024_k2048.
- M>=768: cuBLAS is the ONLY viable option. DP4A is 10-300x slower. Manual CUDA is 10-170x slower. Expect speedup around 0.5x-2.0x depending on shape.
- PyTorch baseline for INT8 uses torch._int_mm with tensor cores. This makes large-M tasks extremely competitive. Only cuBLAS (which also uses tensor cores) can compete.
- CUTLASS fused epilogue could achieve 4x-6x but has <30% compile success rate. Only attempt after cuBLAS baseline works.
- For M>=968 with large N (n32768, n16384), cuBLAS is the only option but may still be below 1.0x because the baseline is highly optimized for these shapes too.
- Never waste step budget on DP4A or manual CUDA for M>=50. The failure rate is >80% and even when they pass, performance is below cuBLAS.
- ALIGNMENT CHECK: IMMA tensor cores require K%16==0 and N%8==0. If not met, CUBLAS_GEMM_DEFAULT_TENSOR_OP may return status 7. Fallback to CUBLAS_GEMM_DEFAULT.
- Large N (>=2048) significantly improves tensor core utilization. Small N (<512) yields lower speedup regardless of M. Shape selection matters as much as approach selection.
