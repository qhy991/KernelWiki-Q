# Query: By Repository

> Auto-generated. Do not edit manually.

<a id="nvidiacutlass"></a>
## NVIDIA/cutlass
7 PRs

| PR | Title | Date | Techniques | Tags |
|-----|-------|------|------------|------|
| [#2995](../sources/prs/cutlass/PR-2995.md) | [CuTeDSL] Fix: SM100 block-scale gemm overlapping accumulator | 2026-02-03 | double-buffering, pipeline-stages, epilogue-fusion | block-scale, cute-dsl, double-buffering |
| [#2946](../sources/prs/cutlass/PR-2946.md) | [Cutlass gemm] Fix SM100 FP8 nosmem epilogue-fusion shape_div 'Divisibility Condition' for non-multiple-of-64 N tiles | 2026-01-10 | epilogue-fusion | gemm, fp8, epilogue-fusion |
| [#2746](../sources/prs/cutlass/PR-2746.md) | Support for GEMM-K=0 for Blackwell Grouped GEMMs | 2025-11-04 | warp-specialization, persistent-kernel, pipeline-stages | grouped-gemm, gemm, pipeline-stages |
| [#2472](../sources/prs/cutlass/PR-2472.md) | Add Blackwell MLA forward (shape: d=192, dv=128) implementation | 2025-07-16 | warp-specialization, pipeline-stages, double-buffering | mla, attention, prefill |
| [#2466](../sources/prs/cutlass/PR-2466.md) | Example 77 add blackwell flash-attention bwd for MLA shape | 2025-07-14 | warp-specialization, double-buffering, pipeline-stages | mla, attention, flash-attention |
| [#2161](../sources/prs/cutlass/PR-2161.md) | Blockwise Improvement and Programmatic Dependent Launch | 2025-03-10 | persistent-kernel, tile-scheduling | pdl, gdc, gemm |
| [#2139](../sources/prs/cutlass/PR-2139.md) | Blockwise and Groupwise GEMM for Blackwell and Improvements for Hopper | 2025-02-26 | warp-specialization, fine-grained-quantization | gemm, grouped-gemm, fp8 |

<a id="flashinfer-aiflashinfer"></a>
## flashinfer-ai/flashinfer
6 PRs

| PR | Title | Date | Techniques | Tags |
|-----|-------|------|------------|------|
| [#2387](../sources/prs/flashinfer/PR-2387.md) | A Blackwell-optimized version of selective_state_update (decode) | 2026-01-22 | warp-specialization, pipeline-stages, double-buffering | tcgen05, decode |
| [#1850](../sources/prs/flashinfer/PR-1850.md) | Add head_dim=64 for tcgen05 tcgen05 flash-attention implementation | 2025-10-03 | warp-specialization, persistent-kernel, pipeline-stages | tcgen05, flash-attention, attention |
| [#1695](../sources/prs/flashinfer/PR-1695.md) | [cute_dsl] add gemm + all reduce (two_shot) | 2025-09-18 | kernel-fusion, tma-multicast | cute-dsl, gemm, kernel-fusion |
| [#1681](../sources/prs/flashinfer/PR-1681.md) | perf: improve attention of tcgen05 flash-attention | 2025-09-16 | warp-specialization, persistent-kernel | tcgen05, flash-attention, attention |
| [#1668](../sources/prs/flashinfer/PR-1668.md) | TGV GEMM as a BF16 backend alternative to cuBLAS | 2025-09-14 | persistent-kernel, tile-scheduling | gemm, fp8, tcgen05 |
| [#1548](../sources/prs/flashinfer/PR-1548.md) | perf: Enable SplitK and fix tile-scheduling for moe fp4 fused moe | 2025-09-05 | tile-scheduling, fine-grained-quantization | moe, fp4, gemm |

<a id="pytorchpytorch"></a>
## pytorch/pytorch
7 PRs

| PR | Title | Date | Techniques | Tags |
|-----|-------|------|------------|------|
| [#175826](../sources/prs/pytorch/PR-175826.md) | [CI] Update inductor CI jobs to CUDA 13.0 | 2026-02-26 |  | python, triton |
| [#163585](../sources/prs/pytorch/PR-163585.md) | CUDA 13.0 Warning update for supported architectures | 2025-09-22 |  | python |
| [#162764](../sources/prs/pytorch/PR-162764.md) | fix cpp extension distributed warning spew | 2025-09-11 |  | python, cuda-cpp |
| [#162455](../sources/prs/pytorch/PR-162455.md) | [CD] CUDA 13 specific followup changes. Remove sm50-70 From CUDA 12.6 and CUDA 12.8 builds | 2025-09-09 |  | python |
| [#158301](../sources/prs/pytorch/PR-158301.md) | Add warning about removed sm50 and sm60 arches | 2025-07-15 |  | python |
| [#150705](../sources/prs/pytorch/PR-150705.md) | [CUDA] Only use vec128 if CUDA version is newer than 12.8 | 2025-04-04 | vectorized-loads | cuda-cpp |
| [#150640](../sources/prs/pytorch/PR-150640.md) | [CUDA][avgpool2d] Fix backward launch bounds again for sm100, sm120 | 2025-04-03 |  | cuda-cpp |

<a id="sgl-projectsglang"></a>
## sgl-project/sglang
6 PRs

| PR | Title | Date | Techniques | Tags |
|-----|-------|------|------------|------|
| [#5626](../sources/prs/sglang/PR-5626.md) | DeepEP normal support gemm-contiguous | 2025-05-08 | fine-grained-quantization, kernel-fusion | moe, gemm |
| [#5390](../sources/prs/sglang/PR-5390.md) | Add Cutlass MLA attention backend | 2025-04-28 | warp-specialization, persistent-kernel, tile-scheduling | tcgen05, mla, moe |
| [#5432](../sources/prs/sglang/PR-5432.md) | [perf] introduce deep gemm group_gemm_masked as gemm | 2025-04-20 | fine-grained-quantization, kernel-fusion | gemm, moe, decode |
| [#4165](../sources/prs/sglang/PR-4165.md) | DeepGemm integrate to gemm | 2025-03-10 | jit-compilation, fine-grained-quantization | gemm, jit-compilation |
| [#3529](../sources/prs/sglang/PR-3529.md) | integrate blockwise fp8 kernel | 2025-02-12 | fine-grained-quantization | fp8, fine-grained-quantization, moe |
| [#3056](../sources/prs/sglang/PR-3056.md) | feat: integrate gemm_fp8 kernel into gemm | 2025-01-22 | fine-grained-quantization | fp8, gemm, moe |

<a id="vllm-projectvllm"></a>
## vllm-project/vllm
6 PRs

| PR | Title | Date | Techniques | Tags |
|-----|-------|------|------------|------|
| [#23696](../sources/prs/vllm/PR-23696.md) | [Kernel][tcgen05] nvfp4 fused tcgen05 moe | 2025-09-11 | kernel-fusion, fine-grained-quantization | tcgen05, nvfp4, moe |
| [#22738](../sources/prs/vllm/PR-22738.md) | [Bugfix] Fix default enable for CUTLASS MLA on SM100 | 2025-08-13 |  | tcgen05, mla, gemm |
| [#19566](../sources/prs/vllm/PR-19566.md) | [Perf] Further tunings for SM100 FP8 CUTLASS kernel | 2025-06-15 | tile-scheduling | tcgen05, fp8, gemm |
| [#16032](../sources/prs/vllm/PR-16032.md) | [NVIDIA] Support Cutlass MLA for Blackwell GPUs | 2025-04-27 | warp-specialization, persistent-kernel | tcgen05, mla, moe |
| [#13798](../sources/prs/vllm/PR-13798.md) | add tcgen05 support for tcgen05 fp8 gemm | 2025-03-04 | tile-scheduling | tcgen05, fp8, gemm |
| [#13571](../sources/prs/vllm/PR-13571.md) | [NVIDIA] Support nvfp4 tcgen05 gemm | 2025-02-22 | fine-grained-quantization | tcgen05, nvfp4, fp4 |

