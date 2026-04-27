# Query: By Repository

> Auto-generated. Do not edit manually.

<a id="nvidiacutlass"></a>
## NVIDIA/cutlass
32 PRs

| PR | Title | Date | Techniques | Tags |
|-----|-------|------|------------|------|
| [#3130](../sources/prs/cutlass/PR-3130.md) | Update blackwell tutorial to be compatible with 4.5-dev version | 2026-03-25 | persistent-kernel | gemm, persistent-kernel |
| [#3106](../sources/prs/cutlass/PR-3106.md) | [CLI] add cutedsl fp16 gemm tutorial from 2 to 6 | 2026-03-13 |  | gemm |
| [#3091](../sources/prs/cutlass/PR-3091.md) | [Hopper CuTeDSL] Add grouped GEMM kernel example | 2026-03-06 |  | gemm, grouped-gemm |
| [#3021](../sources/prs/cutlass/PR-3021.md) | [Cute-DSL] Add option for issue_clc_query without multicast | 2026-02-11 |  | clc |
| [#2995](../sources/prs/cutlass/PR-2995.md) | [CuTeDSL] Fix: SM100 block-scale gemm overlapping accumulator | 2026-02-03 | double-buffering, pipeline-stages, epilogue-fusion | block-scale, cute-dsl, double-buffering |
| [#2965](../sources/prs/cutlass/PR-2965.md) | [Bug Fix]Set NumSplitsM to 1 when TileShapeM < 128 in sm90 fp8 blockwise scaling CollectiveMma | 2026-01-19 |  | fp8, gemm, tma |
| [#2946](../sources/prs/cutlass/PR-2946.md) | [Cutlass gemm] Fix SM100 FP8 nosmem epilogue-fusion shape_div 'Divisibility Condition' for non-multiple-of-64 N tiles | 2026-01-10 | epilogue-fusion | gemm, fp8, epilogue-fusion |
| [#2921](../sources/prs/cutlass/PR-2921.md) | Fix incorrect tensor layout strides in Blackwell MMA tutorial comments | 2026-01-03 |  | gemm |
| [#2881](../sources/prs/cutlass/PR-2881.md) | new example with TMA prefetch feature targeting for DRAM latency boun… | 2025-12-16 | persistent-kernel | gemm, persistent-kernel, tma |
| [#2865](../sources/prs/cutlass/PR-2865.md) | [Bug Fix]Bypass launch grids for SM120 Kernel with SM90 Mainloop & SM100 TileScheduler | 2025-12-09 |  | gemm, tma |
| [#2750](../sources/prs/cutlass/PR-2750.md) | Add tutorial fp16_gemm_1 | 2025-11-05 |  | gemm |
| [#2746](../sources/prs/cutlass/PR-2746.md) | Support for GEMM-K=0 for Blackwell Grouped GEMMs | 2025-11-04 | warp-specialization, persistent-kernel, pipeline-stages | grouped-gemm, gemm, pipeline-stages |
| [#2719](../sources/prs/cutlass/PR-2719.md) | Support PDL for SM90 Array TMA GEMM | 2025-10-24 |  | gemm, tma |
| [#2713](../sources/prs/cutlass/PR-2713.md) | DistGEMM bug fixes | 2025-10-22 |  | gemm |
| [#2599](../sources/prs/cutlass/PR-2599.md) | fix gqa issue for blackwell fmha.py | 2025-08-28 |  | flash-attention |
| [#2492](../sources/prs/cutlass/PR-2492.md) | fix: examples/cute/tutorial/blackwell/04_mma_tma_2sm_sm100.cu GridDim miscalculated | 2025-07-23 |  | 2sm-cooperative, tma |
| [#2472](../sources/prs/cutlass/PR-2472.md) | Add Blackwell MLA forward (shape: d=192, dv=128) implementation | 2025-07-16 | warp-specialization, pipeline-stages, double-buffering | mla, attention, prefill |
| [#2466](../sources/prs/cutlass/PR-2466.md) | Example 77 add blackwell flash-attention bwd for MLA shape | 2025-07-14 | warp-specialization, double-buffering, pipeline-stages | mla, attention, flash-attention |
| [#2378](../sources/prs/cutlass/PR-2378.md) | support fp16 accmulator for sm89 fp8 mma | 2025-06-07 |  | fp8, gemm |
| [#2366](../sources/prs/cutlass/PR-2366.md) | [ex77] fix mla split; add fwd lse; add bwd varlen | 2025-06-04 | epilogue-fusion, kernel-fusion, tile-scheduling | epilogue-fusion, flash-attention, kernel-fusion |
| [#2333](../sources/prs/cutlass/PR-2333.md) | Fix epilogue::thread::Convert cannot be used with DefaultEpilogue | 2025-05-26 | epilogue-fusion | epilogue-fusion |
| [#2291](../sources/prs/cutlass/PR-2291.md) | Correct divmod order in example 77 (blackwell fmha) | 2025-05-13 | tile-scheduling | flash-attention, tile-scheduling |
| [#2292](../sources/prs/cutlass/PR-2292.md) | Handle get_masked_trip_count for small length in fmha example | 2025-05-13 | kernel-fusion | flash-attention, kernel-fusion |
| [#2267](../sources/prs/cutlass/PR-2267.md) | war to fix blackwell grouped groupwise hang | 2025-04-29 | tile-scheduling | gemm, tile-scheduling |
| [#2220](../sources/prs/cutlass/PR-2220.md) | Set EpiTile correctly when TileN is not divisible by 32 | 2025-04-04 | epilogue-fusion | epilogue-fusion |
| [#2167](../sources/prs/cutlass/PR-2167.md) | Fix sm100 gemm wrong static constexpr that breaks compilation on Windows | 2025-03-13 |  | gemm, tma |
| [#2161](../sources/prs/cutlass/PR-2161.md) | Blockwise Improvement and Programmatic Dependent Launch | 2025-03-10 | persistent-kernel, tile-scheduling | pdl, gdc, gemm |
| [#2134](../sources/prs/cutlass/PR-2134.md) | Flash MLA Support - Step 2 | 2025-02-26 |  | mla, tma |
| [#2139](../sources/prs/cutlass/PR-2139.md) | Blockwise and Groupwise GEMM for Blackwell and Improvements for Hopper | 2025-02-26 | warp-specialization, fine-grained-quantization | gemm, grouped-gemm, fp8 |
| [#2130](../sources/prs/cutlass/PR-2130.md) | Flash MLA support | 2025-02-24 |  | mla, tma |
| [#2037](../sources/prs/cutlass/PR-2037.md) | Groupwise scaling along M for FP8 gemm | 2025-01-13 | warp-specialization | fp8, gemm, tma |
| [#2033](../sources/prs/cutlass/PR-2033.md) | [EVT] Add support for Row/Col broadcast PtrArray | 2025-01-08 | epilogue-fusion, kernel-fusion | epilogue-fusion, kernel-fusion, tma |

<a id="deepseek-aideepgemm"></a>
## deepseek-ai/DeepGEMM
1 PRs

| PR | Title | Date | Techniques | Tags |
|-----|-------|------|------------|------|
| [#304](../sources/prs/DeepGEMM/PR-304.md) | [Public release 26/04] Introducing Mega MoE, FP4 Indexer and other features/fixes | 2026-04-17 | kernel-fusion, fine-grained-quantization, communication-overlap | gemm, moe, fused-kernel |

<a id="flashinfer-aiflashinfer"></a>
## flashinfer-ai/flashinfer
583 PRs

| PR | Title | Date | Techniques | Tags |
|-----|-------|------|------------|------|
| [#3058](../sources/prs/flashinfer/PR-3058.md) | Support lse in trtllm paged attn kernels | 2026-04-14 |  | attention, decode, flash-attention |
| [#3066](../sources/prs/flashinfer/PR-3066.md) | feat: Add b12x CuTe DSL fused MoE for SM120 | 2026-04-14 | kernel-fusion | fp4, kernel-fusion, moe |
| [#3051](../sources/prs/flashinfer/PR-3051.md) | feat: Add backend="b12x" for mm_fp4 on SM120 | 2026-04-13 |  | fp4, gemm |
| [#3032](../sources/prs/flashinfer/PR-3032.md) | fused_moe: pre-filter SM89 tactics with zero occupancy on SM120 Blackwell (fix review feedback on #2764) | 2026-04-10 | kernel-fusion | gemm, kernel-fusion, moe |
| [#3021](../sources/prs/flashinfer/PR-3021.md) | fix: extend moe alltoall top-k specializations | 2026-04-09 |  | moe |
| [#3024](../sources/prs/flashinfer/PR-3024.md) | [feat] Add routing_replay_out support to MoE kernels and Python API | 2026-04-09 | kernel-fusion | kernel-fusion, moe |
| [#3025](../sources/prs/flashinfer/PR-3025.md) | Prevent MoE autotuner buffer overflow on large token buckets | 2026-04-09 | kernel-fusion | kernel-fusion, moe |
| [#3026](../sources/prs/flashinfer/PR-3026.md) | perf: Port TRT-LLM SM120/SM121 FP4 CUTLASS GEMM optimizations. Add PDL | 2026-04-09 |  | fp4, gemm |
| [#3014](../sources/prs/flashinfer/PR-3014.md) | perf: Optimize CUTLASS MoE helper kernels for small-batch decode workloads | 2026-04-08 | kernel-fusion | decode, kernel-fusion, moe |
| [#3017](../sources/prs/flashinfer/PR-3017.md) | [chore] Install nvidia-cutlass-dsl[cu13] for cu130+ | 2026-04-08 |  | gemm |
| [#3001](../sources/prs/flashinfer/PR-3001.md) | [feat] Add blackwell GDN prefill kernel | 2026-04-07 | tile-scheduling | gated-delta-net, prefill, tile-scheduling |
| [#3007](../sources/prs/flashinfer/PR-3007.md) | fix: use sym_int64 for strides in rmsnorm CuTe DSL kernels to prevent int32 overflow | 2026-04-07 | kernel-fusion | kernel-fusion |
| [#3008](../sources/prs/flashinfer/PR-3008.md) | feat: add PDL support to rmsnorm_fp4quant and add_rmsnorm_fp4quant CuTe DSL kernels | 2026-04-07 |  | fp4 |
| [#2988](../sources/prs/flashinfer/PR-2988.md) | [Fmha] support nvfp4 output keepsMmaAb generation kernels | 2026-04-06 |  | attention, flash-attention, fp4 |
| [#2994](../sources/prs/flashinfer/PR-2994.md) |   Fix MXFP4/MXFP8 failures in SM120 FAST_BUILD and expand all_tiles[]                                                   | 2026-04-06 |  | fp4, fp8 |
| [#2996](../sources/prs/flashinfer/PR-2996.md) | fix: tinygemm2 hang issue due to barrier sync | 2026-04-06 |  | gemm |
| [#2982](../sources/prs/flashinfer/PR-2982.md) | feat(comm): add MOE Finalize/Reduction patterns to unified allreduce_fusion API | 2026-04-05 | kernel-fusion | kernel-fusion, moe |
| [#2984](../sources/prs/flashinfer/PR-2984.md) | fix: restore SM120 CUTLASS MoE tile candidate removed by #2927 (test_trtllm_cutlass_fused_moe.py) | 2026-04-05 | kernel-fusion | kernel-fusion, moe |
| [#2966](../sources/prs/flashinfer/PR-2966.md) | Fused moe all-reduce routed scaling factor + quant support | 2026-04-03 | kernel-fusion | kernel-fusion, moe |
| [#2974](../sources/prs/flashinfer/PR-2974.md) | test: skip unsupported mm_mxfp8 configurations on SM12x | 2026-04-03 |  | fp8, gemm |
| [#2954](../sources/prs/flashinfer/PR-2954.md) | Only swizzle on v block scale; rename kv_block_scales to kv_cache_sf | 2026-04-02 | swizzling | attention, block-scale, decode |
| [#2960](../sources/prs/flashinfer/PR-2960.md) | Update NVSHMEM interface to use NVSHMEM4Py instead of custom bindings | 2026-04-02 |  | gemm |
| [#2963](../sources/prs/flashinfer/PR-2963.md) | test: xfail cuDNN FP8 prefill on Blackwell with CUDA <= 12.9 | 2026-04-02 |  | attention, fp8, prefill |
| [#2965](../sources/prs/flashinfer/PR-2965.md) | Add flashinfer.fused_rmsnorm_silu() with native kernel backend | 2026-04-02 | kernel-fusion | kernel-fusion |
| [#2940](../sources/prs/flashinfer/PR-2940.md) | CuTe DSL FP4 GEMM Heuristic | 2026-04-01 |  | fp4, gemm |
| [#2942](../sources/prs/flashinfer/PR-2942.md) | [Perf] Refactor MoE autotuning to set valid topk ids in routed MoE tuning | 2026-04-01 | kernel-fusion | kernel-fusion, moe |
| [#2945](../sources/prs/flashinfer/PR-2945.md) | fix: use float instead of double in sampling binary search to avoid FP64 bottleneck on SM103 | 2026-04-01 |  | gemm |
| [#2926](../sources/prs/flashinfer/PR-2926.md) | feat: add Relu2 (squared ReLU) activation support in CUTLASS MoE backend | 2026-03-31 | epilogue-fusion | epilogue-fusion, gemm, moe |
| [#2927](../sources/prs/flashinfer/PR-2927.md) | feat: SM121 (GB10) tile filtering and autotuner robustness | 2026-03-31 |  | gemm |
| [#2916](../sources/prs/flashinfer/PR-2916.md) | fix: Fix autotuner crash on meta-device tensor in trtllm_fp4_block_scale_routed_moe | 2026-03-30 | kernel-fusion | block-scale, fp4, kernel-fusion |
| [#2913](../sources/prs/flashinfer/PR-2913.md) | [NVIDIA] fix(jit): enable GDC for CUTLASS fused MoE PDL — prevent random crashes on SM12x | 2026-03-29 | kernel-fusion | fp8, gemm, kernel-fusion |
| [#2908](../sources/prs/flashinfer/PR-2908.md) | feat(gdn): state checkpointing in chunk_gated_delta_rule | 2026-03-28 |  | gated-delta-net, prefill, tma |
| [#2901](../sources/prs/flashinfer/PR-2901.md) | feat: add pdl support for cute dsl mla decode kernel support | 2026-03-27 |  | attention, decode, fp8 |
| [#2902](../sources/prs/flashinfer/PR-2902.md) | feat: add MXFP8 GEMM support for SM120 | 2026-03-27 |  | fp8, gemm |
| [#2904](../sources/prs/flashinfer/PR-2904.md) | perf: Optimize CuTe-DSL fp4 and fp8 quantization kernels | 2026-03-27 |  | fp4, fp8, nvfp4 |
| [#2898](../sources/prs/flashinfer/PR-2898.md) | fix: snap weight_scale_vec_size to handle block_scale_interleave padding for SM120 | 2026-03-26 | kernel-fusion | block-scale, fp4, kernel-fusion |
| [#2872](../sources/prs/flashinfer/PR-2872.md) | fix: add cute dsl moe utils to AOT | 2026-03-24 |  | moe |
| [#2876](../sources/prs/flashinfer/PR-2876.md) | [fix] bugfix 2856: Fix pre-allocated out shape check in trtllm_batch_decode_with_kv_cache_mla for q_len_per_req > 1 | 2026-03-24 |  | attention, decode, mla |
| [#2882](../sources/prs/flashinfer/PR-2882.md) | Fix silent bug with FP8 per tensor non-gated MoE | 2026-03-24 | kernel-fusion | fp8, kernel-fusion, moe |
| [#2864](../sources/prs/flashinfer/PR-2864.md) | Add support for Relu2 in BF16 fused MoE | 2026-03-23 | kernel-fusion | gemm, kernel-fusion, moe |
| [#2865](../sources/prs/flashinfer/PR-2865.md) | Mamba SSU: horizontal MTP kernel (+ DSTATE=96 support) | 2026-03-23 |  | gemm |
| [#2853](../sources/prs/flashinfer/PR-2853.md) | fix: int32 overflow in `trtllm_fp4_block_scale_moe` causing "Unsupported hidden state scale shape" for EP32+ configs | 2026-03-22 | kernel-fusion | block-scale, fp4, kernel-fusion |
| [#2836](../sources/prs/flashinfer/PR-2836.md) | [Fmha] Sparse MLA decode kernel selection heuristics | 2026-03-20 |  | decode, flash-attention, mla |
| [#2838](../sources/prs/flashinfer/PR-2838.md) | feat: Add CuTe-DSL backend for NVFP4 quantization | 2026-03-20 |  | fp4, nvfp4, quantization |
| [#2842](../sources/prs/flashinfer/PR-2842.md) | perf: Optimize GDN MTP decode kernel (v15) — eliminate ilp=1 fallback… | 2026-03-20 |  | decode |
| [#2844](../sources/prs/flashinfer/PR-2844.md) | read real strides for kv and block scale | 2026-03-20 |  | decode, flash-attention, prefill |
| [#2821](../sources/prs/flashinfer/PR-2821.md) | fix: Autotuner _find_nearest_profile non-power-of-2 num_tokens, create launchers for all supported tileN in trtllm fused MoE | 2026-03-19 | kernel-fusion | kernel-fusion, moe |
| [#2828](../sources/prs/flashinfer/PR-2828.md) | [Spark unit test] Adjust tolerance for test_xqa, test_logits_processor | 2026-03-19 |  | attention |
| [#2811](../sources/prs/flashinfer/PR-2811.md) | CuteDSL MoE fix redundant output buffer zeroing | 2026-03-18 | kernel-fusion | gemm, grouped-gemm, kernel-fusion |
| [#2802](../sources/prs/flashinfer/PR-2802.md) | [fix] Bugfix 1367: fix VariableBlockSparseAttention buffer overflow by dynamically resizing kv_lens_buffer | 2026-03-17 |  | attention, decode, prefill |
| [#2805](../sources/prs/flashinfer/PR-2805.md) | [CuTe DSL] Add modular FMHA prefill and MLA decode attention kernels | 2026-03-17 | epilogue-fusion, kernel-fusion, persistent-kernel | attention, decode, epilogue-fusion |
| [#2810](../sources/prs/flashinfer/PR-2810.md) | feat(gdn): add padding index guard for bf16 decode kernel | 2026-03-17 |  | decode |
| [#2792](../sources/prs/flashinfer/PR-2792.md) | feat: Support padding tokens with seqlen=0 for rope+quant+kv cache update fusion kernel | 2026-03-16 | kernel-fusion | attention, kernel-fusion |
| [#2798](../sources/prs/flashinfer/PR-2798.md) | Upgrade cutlass 4.2.1 -> 4.4.2 | 2026-03-16 |  | gemm, moe, tma |
| [#2777](../sources/prs/flashinfer/PR-2777.md) | perf: Performance tune cute dsl RMSNorm variants | 2026-03-13 | kernel-fusion | kernel-fusion |
| [#2780](../sources/prs/flashinfer/PR-2780.md) | fix(jit): enable GDC for CUTLASS GEMM PDL — SM100 flag only | 2026-03-13 |  | gemm |
| [#2781](../sources/prs/flashinfer/PR-2781.md) | tests: skip sliding window + fp8 to prevent hang in fmha_v2 unit tests | 2026-03-13 |  | attention, flash-attention, fp8 |
| [#2770](../sources/prs/flashinfer/PR-2770.md) | feat: Expose TRT-LLM FMHA style paged KV Cache and page table layout | 2026-03-12 |  | attention, decode, flash-attention |
| [#2750](../sources/prs/flashinfer/PR-2750.md) | [Spark unit test debugging] Fix for tests/attention/test_trtllm_gen_mla.py | 2026-03-11 |  | attention, mla |
| [#2751](../sources/prs/flashinfer/PR-2751.md) | [Spark unit test debugging] Fix for tests/gemm/test_groupwise_scaled_gemm_fp8.py | 2026-03-11 |  | fp8, gemm |
| [#2752](../sources/prs/flashinfer/PR-2752.md) | [feat] Add air top-p algorithm | 2026-03-11 |  | gemm |
| [#2757](../sources/prs/flashinfer/PR-2757.md) | feat: Add FP4 KV cache quant/dequant kernels  | 2026-03-11 |  | fp4, quantization |
| [#2738](../sources/prs/flashinfer/PR-2738.md) | Support for MXFP4 and NVFP4 group GEMMs on GeForce and Spark | 2026-03-10 |  | fp4, fp8, gemm |
| [#2739](../sources/prs/flashinfer/PR-2739.md) | Support in-place update for `trtllm_fp8_block_scale_moe` | 2026-03-10 | kernel-fusion | block-scale, fp8, kernel-fusion |
| [#2740](../sources/prs/flashinfer/PR-2740.md) | misc: Update gemm/batched gemm cubins from trtllm-gen, gemm header refactor | 2026-03-10 | kernel-fusion | gemm, kernel-fusion, moe |
| [#2743](../sources/prs/flashinfer/PR-2743.md) | Add cute dsl mla decode op | 2026-03-10 |  | attention, decode, fp8 |
| [#2744](../sources/prs/flashinfer/PR-2744.md) | [feat] Add 2048 experts and 32 Top K  | 2026-03-10 | kernel-fusion | kernel-fusion, moe |
| [#2725](../sources/prs/flashinfer/PR-2725.md) | fix: Add SM120 (RTX Blackwell desktop) support for NVFP4 MoE kernels | 2026-03-09 | kernel-fusion | fp4, kernel-fusion, moe |
| [#2727](../sources/prs/flashinfer/PR-2727.md) | [gdn] support non-contiguous state for decoding | 2026-03-09 |  | decode |
| [#2716](../sources/prs/flashinfer/PR-2716.md) | fix(jit): GEMM kernels produce NaN under concurrency — missing GDC flags cause PDL synchronization barriers to compile as no-ops | 2026-03-07 |  | gemm |
| [#2702](../sources/prs/flashinfer/PR-2702.md) | Add NVFP4 KV cache quantization support for SM100 | 2026-03-06 |  | attention, decode, flash-attention |
| [#2707](../sources/prs/flashinfer/PR-2707.md) | feat: Add support for TRTLLM MXFP8 non-gated MoE with ReLU2 | 2026-03-06 | kernel-fusion | fp8, kernel-fusion, moe |
| [#2709](../sources/prs/flashinfer/PR-2709.md) | Mamba2 SSD Combined Forward Pass (Blackwell CuTe DSL Kernel) | 2026-03-06 | tile-scheduling | tile-scheduling |
| [#2700](../sources/prs/flashinfer/PR-2700.md) | Add varlen and speculative decoding support to selective state update | 2026-03-05 |  | gemm |
| [#2670](../sources/prs/flashinfer/PR-2670.md) | fix: reduce smem allocation for tinygemm2 kernel in SM120 | 2026-03-03 |  | gemm |
| [#2677](../sources/prs/flashinfer/PR-2677.md) | feat: add support for more MLA head dimensions | 2026-03-03 |  | attention, flash-attention, mla |
| [#2679](../sources/prs/flashinfer/PR-2679.md) | feat(gdn): add BF16 state kernel with MTP support beyond T>4 with intermediate caching. | 2026-03-03 |  | decode |
| [#2666](../sources/prs/flashinfer/PR-2666.md) | benchmarks: Add FP8 input / BF16 output in ragged prefill benchmark | 2026-03-02 |  | attention, fp8, prefill |
| [#2667](../sources/prs/flashinfer/PR-2667.md) | perf: Update trtllm-gen batched GEMM kernels - faster, more NVFP4 tile dims, MXFP8 with relu2 act | 2026-03-02 |  | fp4, fp8, gemm |
| [#2661](../sources/prs/flashinfer/PR-2661.md) | feat: implement deterministic topk | 2026-03-01 |  | gemm |
| [#2653](../sources/prs/flashinfer/PR-2653.md) | [feat] trtllm-gen mxfp8 gemm | 2026-02-28 | kernel-fusion | attention, decode, fp4 |
| [#2654](../sources/prs/flashinfer/PR-2654.md) | fix: Add fused MOE and GEMM AOT modules for SM121 | 2026-02-28 | kernel-fusion | gemm, kernel-fusion, moe |
| [#2660](../sources/prs/flashinfer/PR-2660.md) | feat: support mxfp4 & mxfp8 entrypoint for blackwell cutedsl dense gemm | 2026-02-28 |  | fp4, fp8, gemm |
| [#2650](../sources/prs/flashinfer/PR-2650.md) | Enable sm120f compilation | 2026-02-27 |  | fp4, quantization |
| [#2642](../sources/prs/flashinfer/PR-2642.md) | [fp8_blockwise]Fix int32 overflow in TRTLLM fused MoE activation kernel | 2026-02-26 | kernel-fusion | fp8, kernel-fusion, moe |
| [#2644](../sources/prs/flashinfer/PR-2644.md) | feat: FP32 dtype output for BF16 matmuls (CUTLASS & cuDNN) | 2026-02-26 |  | gemm |
| [#2645](../sources/prs/flashinfer/PR-2645.md) | int16 Block-Scaled State and Stochastic Rounding for SSU (mamba) | 2026-02-26 |  | block-scale |
| [#2635](../sources/prs/flashinfer/PR-2635.md) | benchmark: Add MXFP4/MXFP8 quantization mode support to FP4 MoE benchmark | 2026-02-25 |  | fp4, fp8, moe |
| [#2627](../sources/prs/flashinfer/PR-2627.md) | fix: trtllm_mxint4_block_scale_moe unit test to index output list | 2026-02-24 | kernel-fusion | block-scale, kernel-fusion, moe |
| [#2628](../sources/prs/flashinfer/PR-2628.md) | benchmark: Enable speculative decode microbenchmarking for paged decode | 2026-02-24 |  | attention, decode |
| [#2629](../sources/prs/flashinfer/PR-2629.md) | fix: cute dsl nvfp4 moe routing index error | 2026-02-24 | kernel-fusion | fp4, kernel-fusion, moe |
| [#2631](../sources/prs/flashinfer/PR-2631.md) | fix: add SM121 support to SM120 version guards | 2026-02-24 | kernel-fusion | attention, decode, flash-attention |
| [#2618](../sources/prs/flashinfer/PR-2618.md) | perf(gdn): optimize MTP kernel with ILP rows and SMEM v caching | 2026-02-22 |  | decode |
| [#2619](../sources/prs/flashinfer/PR-2619.md) | feat: add pool+indices support to gated_delta_rule_decode_pretranspose (bf16 path)  | 2026-02-22 |  | decode, gated-delta-net |
| [#2607](../sources/prs/flashinfer/PR-2607.md) | support qk_nope_head_dim for 192 check for GLM-5 | 2026-02-21 |  | attention, mla |
| [#2610](../sources/prs/flashinfer/PR-2610.md) | Ameyn/gdn bf16 tolerance parallel reduction | 2026-02-21 |  | decode |
| [#2605](../sources/prs/flashinfer/PR-2605.md) | [bugfix] Fix FilteredTopK overflow correctness | 2026-02-20 |  | gemm |
| [#2587](../sources/prs/flashinfer/PR-2587.md) | feat: trtllm tinygemm2 in flashinfer as bf16 routergemm | 2026-02-19 |  | gemm |
| [#2588](../sources/prs/flashinfer/PR-2588.md) | Perf: Optimize GDN decode pretranspose kernel for all batch sizes | 2026-02-19 |  | decode |
| [#2591](../sources/prs/flashinfer/PR-2591.md) | Mamba SSU: better automatic kernel selection + algorithm selection optionally exposed to the user. | 2026-02-19 |  | gemm |
| [#2581](../sources/prs/flashinfer/PR-2581.md) | Implement `cutlass_fused_moe` mxfp8 | 2026-02-18 | kernel-fusion | fp8, gemm, kernel-fusion |
| [#2585](../sources/prs/flashinfer/PR-2585.md) | tests: add bias testing to nvfp4 moe | 2026-02-18 | kernel-fusion | fp4, kernel-fusion, moe |
| [#2573](../sources/prs/flashinfer/PR-2573.md) | [Bug] Fix spark unit test failures for test_add_rmsnorm_fp4_quant_cute_dsl | 2026-02-17 |  | fp4 |
| [#2574](../sources/prs/flashinfer/PR-2574.md) | feat: add is_sm12x_supported() helper for SM12x family detection | 2026-02-17 |  | attention, flash-attention, gemm |
| [#2564](../sources/prs/flashinfer/PR-2564.md) | fix: W4A8 autotune crash in cutlass_fused_moe profiler workspace | 2026-02-14 | kernel-fusion | kernel-fusion, moe |
| [#2559](../sources/prs/flashinfer/PR-2559.md) | fix: allow fmha_v2_prefill_deepseek on SM121 (DGX Spark) | 2026-02-13 |  | attention, flash-attention, prefill |
| [#2560](../sources/prs/flashinfer/PR-2560.md) | fix: guard CUTLASS FMHA against SM12x and fix fmha_v2 SM121a check | 2026-02-13 |  | attention, flash-attention, prefill |
| [#2543](../sources/prs/flashinfer/PR-2543.md) | misc: point triton blackwell-ptxas to local cuda ptxas | 2026-02-12 |  | gemm |
| [#2547](../sources/prs/flashinfer/PR-2547.md) | feat: Enable TRTLLM-Gen Skip-Softmax attention for MLA | 2026-02-12 |  | attention, flash-attention, mla |
| [#2549](../sources/prs/flashinfer/PR-2549.md) | Add gen_gemm_sm100_module_cutlass_mxfp8 to jit-cache | 2026-02-12 |  | fp8, gemm |
| [#2538](../sources/prs/flashinfer/PR-2538.md) | tests: bmm_fp8 for SM110 | 2026-02-11 |  | fp8, gemm |
| [#2540](../sources/prs/flashinfer/PR-2540.md) | feat: cute dsl mmfp4 for blackwell | 2026-02-11 |  | fp4, gemm |
| [#2533](../sources/prs/flashinfer/PR-2533.md) | fix: include fp8_blockscale_gemm_90 in AOT jit-cache | 2026-02-10 |  | fp8, gemm |
| [#2536](../sources/prs/flashinfer/PR-2536.md) | fallback to fa2 (instead of fa3) for unsupported configuration (bf16 Q, Fp8 KV) | 2026-02-10 |  | fp8 |
| [#2525](../sources/prs/flashinfer/PR-2525.md) | feat: BF16 GEMM benchmarking support | 2026-02-09 |  | gemm |
| [#2530](../sources/prs/flashinfer/PR-2530.md) | pick fa2 for BatchDecodeWithPagedKVCacheWrapper auto backend | 2026-02-09 |  | attention, decode |
| [#2520](../sources/prs/flashinfer/PR-2520.md) | Support NVFP4 KV cache decode on SM120 | 2026-02-08 |  | attention, decode, fp4 |
| [#2521](../sources/prs/flashinfer/PR-2521.md) | Feat/gdn decode pooled | 2026-02-08 |  | decode |
| [#2505](../sources/prs/flashinfer/PR-2505.md) | Feat: Trtllm-gen MxFP8 MoE integration | 2026-02-06 | kernel-fusion | fp8, gemm, kernel-fusion |
| [#2509](../sources/prs/flashinfer/PR-2509.md) | perf: cache cudaGetDeviceProperties in gdn_prefill to avoid per-call overhead | 2026-02-06 |  | prefill |
| [#2498](../sources/prs/flashinfer/PR-2498.md) | Ameyn/gdn decode cutedsl kernel | 2026-02-05 |  | decode, prefill |
| [#2503](../sources/prs/flashinfer/PR-2503.md) | refactor: Port upstream CUTLASS fixes and refactor grouped_gemm_nt_masked GEMM module location | 2026-02-05 |  | gemm, grouped-gemm |
| [#2495](../sources/prs/flashinfer/PR-2495.md) | fix: add support check for gemm config for cutlass moe | 2026-02-04 |  | gemm, moe |
| [#2476](../sources/prs/flashinfer/PR-2476.md) | fix: blockscale moe routine supports non-DS routing | 2026-02-03 |  | moe |
| [#2477](../sources/prs/flashinfer/PR-2477.md) | feat: Add TRTLLM-Gen Skip-Softmax kernels for prefill and decode | 2026-02-03 |  | attention, decode, flash-attention |
| [#2479](../sources/prs/flashinfer/PR-2479.md) | fix: Fix memory bandwidth calculation in MLA benchmarks | 2026-02-03 |  | attention, mla |
| [#2460](../sources/prs/flashinfer/PR-2460.md) | perf: add fp4 GEMM tile configs and streamK scheduler for SM120 | 2026-02-02 |  | fp4, gemm |
| [#2462](../sources/prs/flashinfer/PR-2462.md) | feat: Support Fused MoE non gated Relu2 NVFP4 & FP8 and support Nemotron, fixed | 2026-02-02 | kernel-fusion | fp4, fp8, gemm |
| [#2464](../sources/prs/flashinfer/PR-2464.md) | feat: Add MXFP8 GEMM mm_mxfp8 (cutlass) | 2026-02-02 |  | fp8, gemm |
| [#2456](../sources/prs/flashinfer/PR-2456.md) | fix: fix illegal memory access for NaN input in sampling kernels | 2026-01-31 |  | gemm |
| [#2443](../sources/prs/flashinfer/PR-2443.md) | Add cute-dsl backends to mxfp[8,4]_quantization for future refactor | 2026-01-30 |  | fp4, fp8, quantization |
| [#2444](../sources/prs/flashinfer/PR-2444.md) | MTP for mamba  | 2026-01-30 |  | gemm |
| [#2445](../sources/prs/flashinfer/PR-2445.md) | bugfix: fix stub generation directory in fused_moe module | 2026-01-30 | kernel-fusion | kernel-fusion, moe |
| [#2446](../sources/prs/flashinfer/PR-2446.md) | feat: Add TRTLLM fmha_v2 library for SM90 attention with Skip-Softmax  | 2026-01-30 | epilogue-fusion, kernel-fusion | attention, epilogue-fusion, flash-attention |
| [#2432](../sources/prs/flashinfer/PR-2432.md) | fix: Sampling: CUDA Graph fix | 2026-01-29 |  | gemm |
| [#2441](../sources/prs/flashinfer/PR-2441.md) | fix: Fix NaN output in mxfp8_quantize for very small input values | 2026-01-29 |  | fp8, quantization |
| [#2428](../sources/prs/flashinfer/PR-2428.md) | refactor: refactoring cuda code to cute-dsl (part 1) | 2026-01-28 | kernel-fusion | fp4, kernel-fusion |
| [#2421](../sources/prs/flashinfer/PR-2421.md) | refactor: simplify fp4 rmsnorm | 2026-01-27 |  | fp4 |
| [#2422](../sources/prs/flashinfer/PR-2422.md) | refactor: reduce hopper's gdn prefill compilation time and fix docstring. | 2026-01-27 | tile-scheduling | prefill, tile-scheduling, tma |
| [#2416](../sources/prs/flashinfer/PR-2416.md) | feat: update trtllm-gen MoE cubins | 2026-01-26 |  | gemm, moe, tma |
| [#2415](../sources/prs/flashinfer/PR-2415.md) | Remove cudaMalloc/Free in GDN prefill kernel | 2026-01-25 |  | prefill |
| [#2405](../sources/prs/flashinfer/PR-2405.md) | perf: improve gdn decode cute-dsl kernels | 2026-01-23 |  | decode |
| [#2387](../sources/prs/flashinfer/PR-2387.md) | A Blackwell-optimized version of selective_state_update (decode) | 2026-01-22 | warp-specialization, pipeline-stages, double-buffering | tcgen05, decode |
| [#2398](../sources/prs/flashinfer/PR-2398.md) | feat: cuteDSL fp4 moe for better DSR1 performance. | 2026-01-22 | kernel-fusion, pipeline-stages | fp4, gemm, grouped-gemm |
| [#2404](../sources/prs/flashinfer/PR-2404.md) | perf: mm_fp4 heuristic prioritizes CUTLASS over cuDNN on SM103 | 2026-01-22 |  | fp4, gemm |
| [#2395](../sources/prs/flashinfer/PR-2395.md) | feat: Add output_both_sf_layouts option to add_rmsnorm_fp4quant API | 2026-01-21 |  | fp4 |
| [#2376](../sources/prs/flashinfer/PR-2376.md) | feat: BF16 GEMM using cuDNN backend | 2026-01-20 |  | gemm |
| [#2378](../sources/prs/flashinfer/PR-2378.md) | bugfix: hotfix of PR 2366 (mamba kernel) | 2026-01-20 |  | gemm |
| [#2380](../sources/prs/flashinfer/PR-2380.md) | fix: ensure each CTA processes full numHeadsQPerKv for trtllm decode kernel | 2026-01-20 |  | decode, flash-attention |
| [#2385](../sources/prs/flashinfer/PR-2385.md) | fix: In-place Residual Update for add_rmsnorm_fp4quant | 2026-01-20 |  | fp4 |
| [#2370](../sources/prs/flashinfer/PR-2370.md) | feat: [Qwen3-Next] Add Cute DSL GDN decode kernel and  tests | 2026-01-18 |  | decode, prefill |
| [#2366](../sources/prs/flashinfer/PR-2366.md) | Enable fp16/bf16/f32 support for selective_state_update (mamba) | 2026-01-16 |  | gemm |
| [#2362](../sources/prs/flashinfer/PR-2362.md) | benchmarks: Add norm and quantization routines to microbenchmark harness. | 2026-01-15 |  | quantization |
| [#2352](../sources/prs/flashinfer/PR-2352.md) | Added the cudnn backend Ragged KV Cache wrapper | 2026-01-14 |  | attention, prefill |
| [#2343](../sources/prs/flashinfer/PR-2343.md) | Optimize quantization function in large problem size | 2026-01-13 | kernel-fusion | fp4, kernel-fusion, moe |
| [#2334](../sources/prs/flashinfer/PR-2334.md) | Support both 3D and 4D kv_cache shapes in MLA APIs | 2026-01-12 |  | mla |
| [#2327](../sources/prs/flashinfer/PR-2327.md) | [perf] Improve gemm_fp8_nt_groupwise (cutlass backend) by 10-40% for batch sizes <= 32 | 2026-01-11 |  | fp8, gemm |
| [#2328](../sources/prs/flashinfer/PR-2328.md) | fix: guard batchWarpReduceSum with ENABLE_FP8 to fix compilation without FP8 | 2026-01-11 |  | fp8 |
| [#2330](../sources/prs/flashinfer/PR-2330.md) | feat: expose swizzled_input_sf parameter for CUTLASS fused MOE | 2026-01-11 | kernel-fusion, swizzling | kernel-fusion, moe, swizzling |
| [#2325](../sources/prs/flashinfer/PR-2325.md) | bugfix: fix multi-cta top-k implementation when k value is different for different row | 2026-01-10 |  | gemm |
| [#2323](../sources/prs/flashinfer/PR-2323.md) | [ML3] Optimized Router Gemm | 2026-01-09 |  | gemm |
| [#2308](../sources/prs/flashinfer/PR-2308.md) | Fix: FilteredTopKUnifiedKernel read value out of length | 2026-01-08 |  | gemm |
| [#2302](../sources/prs/flashinfer/PR-2302.md) | fix: Decode benchmark's fa2_tc uses backend=fa2 in wrapper | 2026-01-07 |  | attention, decode |
| [#2303](../sources/prs/flashinfer/PR-2303.md) | [Perf][Feature] Add SM103-specific schedulers for NVFP4 CUTLASS kernels | 2026-01-07 |  | fp4, gemm, nvfp4 |
| [#2304](../sources/prs/flashinfer/PR-2304.md) | feat: Support Fused MoE non gated Relu2 NVFP4 & FP8 and support Nemotron | 2026-01-07 | kernel-fusion | fp4, fp8, gemm |
| [#2301](../sources/prs/flashinfer/PR-2301.md) | Selective State Update kernel (mamba) | 2026-01-06 |  | gemm |
| [#2281](../sources/prs/flashinfer/PR-2281.md) | feat: IdType indices in sampling kernels | 2026-01-02 |  | gemm |
| [#2279](../sources/prs/flashinfer/PR-2279.md) | [WIP] Refactor: simplify torch -> cute-dsl boilerplate and enable tvm-ffi for cute-dsl kernels | 2026-01-01 |  | fp4 |
| [#2276](../sources/prs/flashinfer/PR-2276.md) | feat: add GDN Attention | 2025-12-31 | tile-scheduling | attention, prefill, tile-scheduling |
| [#2277](../sources/prs/flashinfer/PR-2277.md) | Tiny fix bench tgv gemm | 2025-12-31 |  | gemm |
| [#2268](../sources/prs/flashinfer/PR-2268.md) | [performance]optimize for nvfp4 | 2025-12-25 | kernel-fusion | fp4, kernel-fusion, nvfp4 |
| [#2265](../sources/prs/flashinfer/PR-2265.md) | [TRTLLM-Gen Fmha] add optimized trtllm-gen decode kernels for high throughput + speculative decoding | 2025-12-24 |  | attention, decode, flash-attention |
| [#2266](../sources/prs/flashinfer/PR-2266.md) | test: use .float() in in F.cosine_similarity() in bmm_fp8 test | 2025-12-24 |  | fp8, gemm |
| [#2260](../sources/prs/flashinfer/PR-2260.md) | fix: Add global scale support and optional output allocation for RMSNorm+FP4Quant fusion kernels | 2025-12-23 | kernel-fusion | fp4, kernel-fusion |
| [#2261](../sources/prs/flashinfer/PR-2261.md) | Fix CUTLASS FP8 gemm correctness issue on SM120/SM121 for shapes where N is not divisible by ScaleGranularityN. | 2025-12-23 |  | fp8, gemm |
| [#2255](../sources/prs/flashinfer/PR-2255.md) | fix: support int64 IdType for RoPE part argument in `rope_quantize_fp8_append_paged_kv_cache` | 2025-12-22 |  | attention, fp8, quantization |
| [#2256](../sources/prs/flashinfer/PR-2256.md) | feat: Add support for bmm mxfp8 | 2025-12-22 |  | fp8, gemm |
| [#2254](../sources/prs/flashinfer/PR-2254.md) | feat: support non-contiguous query for trtllm-gen attention backend | 2025-12-21 |  | attention, flash-attention |
| [#2243](../sources/prs/flashinfer/PR-2243.md) | feat: RMSNorm/Fused RMSNorm + FP8 Quantization kernels | 2025-12-19 | kernel-fusion | fp8, kernel-fusion, quantization |
| [#2244](../sources/prs/flashinfer/PR-2244.md) | Remove cudaStreamSynchronize from gemm_groupwise_sm120.cuh for CUDA graph compatibility | 2025-12-19 |  | gemm |
| [#2245](../sources/prs/flashinfer/PR-2245.md) | test: Fix MNNVL tests to skip when container lacks SYS_PTRACE capability | 2025-12-19 |  | moe |
| [#2247](../sources/prs/flashinfer/PR-2247.md) | feat: Support numLocalTokens=0 for moe All-to-all | 2025-12-19 |  | moe |
| [#2237](../sources/prs/flashinfer/PR-2237.md) | [feat] Integrate SGLang concat_mla_k kernel into flashinfer | 2025-12-18 |  | mla |
| [#2241](../sources/prs/flashinfer/PR-2241.md) | Fp8 attention are now part of cuDNN 9.17.1 | 2025-12-18 |  | attention, fp8, prefill |
| [#2233](../sources/prs/flashinfer/PR-2233.md) | feat: Fused RMSNorm + FP4 Quantization Kernels in CuTe-DSL | 2025-12-17 | kernel-fusion | fp4, kernel-fusion, quantization |
| [#2234](../sources/prs/flashinfer/PR-2234.md) | fix: add DeepSeek routing for Bf16xBf16 and MxIntxBf16 TRT-LLM Gen MoE | 2025-12-17 | kernel-fusion | kernel-fusion, moe |
| [#2235](../sources/prs/flashinfer/PR-2235.md) | refactor: pull trtllm-gen batch-gemm/gemm headers from artifactory; update tma descriptor shape init | 2025-12-17 | kernel-fusion | gemm, kernel-fusion, moe |
| [#2217](../sources/prs/flashinfer/PR-2217.md) | feat: Support unpadded output hidden size for trtllm_fp4_block_scale_moe | 2025-12-14 | kernel-fusion | block-scale, fp4, kernel-fusion |
| [#2214](../sources/prs/flashinfer/PR-2214.md) | misc: support checks for gemm | 2025-12-13 |  | gemm |
| [#2215](../sources/prs/flashinfer/PR-2215.md) | feat: further optimize top-k and add fused top-k page construction kernels for DSA | 2025-12-13 | kernel-fusion | kernel-fusion |
| [#2211](../sources/prs/flashinfer/PR-2211.md) | Move the run function definition out of BatchedGemmInterface | 2025-12-12 |  | gemm |
| [#2193](../sources/prs/flashinfer/PR-2193.md) | feat: unit-test and api change, w4a8 grouped-gemm fused MoE for SM90 | 2025-12-10 | kernel-fusion | gemm, grouped-gemm, kernel-fusion |
| [#2194](../sources/prs/flashinfer/PR-2194.md) | Permute page table in benchmarking | 2025-12-10 |  | attention |
| [#2190](../sources/prs/flashinfer/PR-2190.md) | Fix for moe on sm110 | 2025-12-09 |  | gemm, moe |
| [#2181](../sources/prs/flashinfer/PR-2181.md) | Rename noauxtc to fused_topk_deepseek | 2025-12-05 | kernel-fusion | kernel-fusion, moe |
| [#2175](../sources/prs/flashinfer/PR-2175.md) | fix: compile flags for trtllm fmha_v2  | 2025-12-04 |  | attention, flash-attention, prefill |
| [#2163](../sources/prs/flashinfer/PR-2163.md) | refactor: Move mla code from decode.py to mla.py and add to documentation | 2025-12-03 |  | attention, decode, mla |
| [#2165](../sources/prs/flashinfer/PR-2165.md) | Add data type check for deepseek fp4 moe | 2025-12-03 | kernel-fusion | fp4, kernel-fusion, moe |
| [#2171](../sources/prs/flashinfer/PR-2171.md) | Fix gemm allreduce two shot | 2025-12-03 |  | gemm |
| [#2157](../sources/prs/flashinfer/PR-2157.md) | fix xqa mha_sm90.cu | 2025-12-02 |  | gemm |
| [#2159](../sources/prs/flashinfer/PR-2159.md) | feat: MxInt4 x Bf16 TRT-LLM Gen MoE support | 2025-12-02 | kernel-fusion | fp4, gemm, kernel-fusion |
| [#2148](../sources/prs/flashinfer/PR-2148.md) | Enable Hopper FA3 FP8 attention in decode.py | 2025-11-28 |  | attention, decode, fp8 |
| [#2149](../sources/prs/flashinfer/PR-2149.md) | enable sm103 moe dsl backend | 2025-11-28 |  | gemm, moe |
| [#2142](../sources/prs/flashinfer/PR-2142.md) | feat: TRTLLM FMHAv2 backend for ctx attention | 2025-11-25 | epilogue-fusion, kernel-fusion | attention, epilogue-fusion, flash-attention |
| [#2137](../sources/prs/flashinfer/PR-2137.md) | fix: some bugs of headDim 256 trtllm-gen fmha kernels.  | 2025-11-24 |  | attention, flash-attention |
| [#2138](../sources/prs/flashinfer/PR-2138.md) | feat: add trtllm-gen per-tensor sparseMla kernels. | 2025-11-24 |  | attention, decode, flash-attention |
| [#2134](../sources/prs/flashinfer/PR-2134.md) | fix(trtllm): reset negative strideBatch to 0 for ragged KV layout to … | 2025-11-23 |  | attention, flash-attention |
| [#2131](../sources/prs/flashinfer/PR-2131.md) | make DeepGEMM swapAB available for linear gemm SM90 | 2025-11-22 |  | fp8, gemm |
| [#2126](../sources/prs/flashinfer/PR-2126.md) | fix flaky xqa test | 2025-11-21 |  | attention, mla |
| [#2129](../sources/prs/flashinfer/PR-2129.md) | fix: Fix bench_mm_fp8.py | 2025-11-21 |  | fp8 |
| [#2130](../sources/prs/flashinfer/PR-2130.md) | A unified API for the MNNVL and single-node/multi-GPU AllReduce kernels. | 2025-11-21 | kernel-fusion | kernel-fusion |
| [#2117](../sources/prs/flashinfer/PR-2117.md) | update xqa license | 2025-11-20 |  | mla, tma |
| [#2118](../sources/prs/flashinfer/PR-2118.md) | Refactor trtllm_mnnvl_allreduce | 2025-11-20 |  | gemm |
| [#2119](../sources/prs/flashinfer/PR-2119.md) | perf: bunch of features and optimizations for top-k (sampling + sparse attention) | 2025-11-20 |  | attention |
| [#2125](../sources/prs/flashinfer/PR-2125.md) | feat: support variable sequence length in decode kernel of trtllm-gen attention | 2025-11-20 |  | attention, decode, flash-attention |
| [#2109](../sources/prs/flashinfer/PR-2109.md) | feat: support more head dim in RoPE kernel | 2025-11-19 |  | attention |
| [#2110](../sources/prs/flashinfer/PR-2110.md) | add tensor scale input for xqa | 2025-11-19 |  | attention, decode, mla |
| [#2111](../sources/prs/flashinfer/PR-2111.md) | refactor: update fa3 codebase and fix hopper unittest [part 1] | 2025-11-19 | epilogue-fusion | attention, epilogue-fusion, fp8 |
| [#2114](../sources/prs/flashinfer/PR-2114.md) | feature: make the LSE returned by MLA support base 2 or e  #2113 | 2025-11-19 |  | attention, mla |
| [#2102](../sources/prs/flashinfer/PR-2102.md) | Port TRT-LLM communication kernels to flashinfer | 2025-11-18 |  | moe |
| [#2105](../sources/prs/flashinfer/PR-2105.md) | enable xqa speculative decoding | 2025-11-18 |  | attention, decode |
| [#2100](../sources/prs/flashinfer/PR-2100.md) | [DSR1] Added MLA test | 2025-11-17 |  | attention, mla |
| [#2097](../sources/prs/flashinfer/PR-2097.md) | refactor: update dpsk fused_moe test [2] | 2025-11-16 | kernel-fusion | fp8, kernel-fusion, moe |
| [#2095](../sources/prs/flashinfer/PR-2095.md) | perf: enable pdl for cutlass fp4 gemm | 2025-11-15 |  | fp4, gemm |
| [#2090](../sources/prs/flashinfer/PR-2090.md) | refactor: pass hopper deepgemm include directory through python | 2025-11-14 | kernel-fusion | gemm, kernel-fusion, moe |
| [#2092](../sources/prs/flashinfer/PR-2092.md) | perf: TRT-LLM Gen finalize kernel optimization | 2025-11-14 | kernel-fusion | kernel-fusion, moe |
| [#2084](../sources/prs/flashinfer/PR-2084.md) | [API change] Allow using torch.Tensor for scales for trtllm-gen attention | 2025-11-13 |  | attention, decode, flash-attention |
| [#2088](../sources/prs/flashinfer/PR-2088.md) | refactor: update dpsk fused_moe test [1] | 2025-11-13 | kernel-fusion | fp8, kernel-fusion, moe |
| [#2079](../sources/prs/flashinfer/PR-2079.md) | [Feature] Support batch prefill for POD Attention | 2025-11-12 |  | attention, decode, prefill |
| [#2081](../sources/prs/flashinfer/PR-2081.md) | enable xqa fp8 output | 2025-11-12 |  | attention, decode, fp8 |
| [#2082](../sources/prs/flashinfer/PR-2082.md) | Patch sm103 for 3xfp4 moe generation | 2025-11-12 | kernel-fusion | fp4, kernel-fusion, moe |
| [#2075](../sources/prs/flashinfer/PR-2075.md) | unittest: improve the efficiency of xqa unittests | 2025-11-11 |  | attention, decode |
| [#2076](../sources/prs/flashinfer/PR-2076.md) | fix: fix test_trtllm_gen_attention when max_seq_len < page_size | 2025-11-11 |  | attention |
| [#2070](../sources/prs/flashinfer/PR-2070.md) | feat: BF16 GEMM using CUTLASS backend for SM100 | 2025-11-10 |  | gemm |
| [#2072](../sources/prs/flashinfer/PR-2072.md) | [Test] Optimize test_trtllm_gen_fused_moe.py | 2025-11-10 | kernel-fusion | kernel-fusion, moe |
| [#2058](../sources/prs/flashinfer/PR-2058.md) | perf: Optimize helper max/minmax function in sampling.cuh | 2025-11-07 |  | gemm |
| [#2061](../sources/prs/flashinfer/PR-2061.md) | Fix moe fp8 failure for sm121 | 2025-11-07 |  | fp8, moe |
| [#2062](../sources/prs/flashinfer/PR-2062.md) | Fix: several bugs/issues with trtllm-gen attention kernels.  | 2025-11-07 |  | attention, flash-attention |
| [#2063](../sources/prs/flashinfer/PR-2063.md) | perf: TRT-LLM MoE Block-FP8 activation optimization | 2025-11-07 | kernel-fusion | fp8, kernel-fusion, moe |
| [#2051](../sources/prs/flashinfer/PR-2051.md) | Add support for topkPacked input in block-level renormalize | 2025-11-06 | kernel-fusion | kernel-fusion, moe |
| [#2052](../sources/prs/flashinfer/PR-2052.md) | test: Skip test_fp8_quantize.py on Hopper | 2025-11-06 |  | fp8, quantization |
| [#2053](../sources/prs/flashinfer/PR-2053.md) | feat: add xqa mla backend | 2025-11-06 |  | attention, decode, mla |
| [#2055](../sources/prs/flashinfer/PR-2055.md) | misc: Add XQA decode to microbenchmark for sm90 and sm120 | 2025-11-06 |  | attention, decode |
| [#2044](../sources/prs/flashinfer/PR-2044.md) | perf: improve sampling/mask/softmax performance (part 1/2) | 2025-11-05 |  | tma |
| [#2047](../sources/prs/flashinfer/PR-2047.md) | Rebase FP8 SM100 Cutlass FMHA Attention to main (original PR#1238) | 2025-11-05 |  | attention, flash-attention, fp8 |
| [#2048](../sources/prs/flashinfer/PR-2048.md) | Fix dtype of output scales from mnnvl_moe_alltoallv_prepare_without_allgather | 2025-11-05 |  | moe |
| [#2049](../sources/prs/flashinfer/PR-2049.md) | [BUG] Fix trtllm-gen fp4 moe renormalize routing | 2025-11-05 | kernel-fusion | fp4, kernel-fusion, moe |
| [#2033](../sources/prs/flashinfer/PR-2033.md) | use scalar for kv_scale in xqa | 2025-11-04 |  | attention, decode, mla |
| [#2035](../sources/prs/flashinfer/PR-2035.md) | Added an initial implementation of Q and KV Cache in fp8 and to use t… | 2025-11-04 |  | attention, fp8, prefill |
| [#2037](../sources/prs/flashinfer/PR-2037.md) | feat: Add flashinfer.rope.rope_quantize_fp8_append_paged_kv_cache (fused RoPE + Q + KV cache, supports MLA/GQA/MHA)  | 2025-11-04 | kernel-fusion | attention, fp8, kernel-fusion |
| [#2025](../sources/prs/flashinfer/PR-2025.md) | perf: Speed up fp4 quantization for small batch with swizzling for cutlass MoE | 2025-11-03 | swizzling | fp4, moe, quantization |
| [#2028](../sources/prs/flashinfer/PR-2028.md) | [NVIDIA] Thor & Spark Support | 2025-11-03 |  | gemm |
| [#2029](../sources/prs/flashinfer/PR-2029.md) | feat: suitable_auto_backends to prune auto backends, bmm_fp8 refactor, heuristic_func intake | 2025-11-03 |  | fp8, gemm |
| [#2030](../sources/prs/flashinfer/PR-2030.md) | Enable renormalize(naive) routing for fp8 per-tensor | 2025-11-03 | kernel-fusion | fp8, kernel-fusion, moe |
| [#2019](../sources/prs/flashinfer/PR-2019.md) | [DSV3] Optimized Router Gemm | 2025-10-31 |  | fp4, gemm |
| [#2020](../sources/prs/flashinfer/PR-2020.md) | update trtllm cutlass moe  | 2025-10-31 | epilogue-fusion, kernel-fusion, warp-specialization | epilogue-fusion, fp4, fp8 |
| [#2011](../sources/prs/flashinfer/PR-2011.md) | Feature: Support non-gated activation in cutlass fused MoE nvfp4 | 2025-10-30 | kernel-fusion | fp4, kernel-fusion, moe |
| [#2012](../sources/prs/flashinfer/PR-2012.md) | fix: Enable SM121 for mm_fp4 | 2025-10-30 |  | fp4, gemm |
| [#2014](../sources/prs/flashinfer/PR-2014.md) | [feat] Refactor trtllmgen MOE and add Bf16 trtllmgen moe | 2025-10-30 | kernel-fusion | gemm, kernel-fusion, moe |
| [#2001](../sources/prs/flashinfer/PR-2001.md) | feat: add xqa backend and completes NHD/HND coverage for trtllm-gen/xqa backend | 2025-10-29 |  | attention, decode, flash-attention |
| [#2002](../sources/prs/flashinfer/PR-2002.md) | Fix trtllm-gen attention illegal memory access | 2025-10-29 |  | attention, decode |
| [#1994](../sources/prs/flashinfer/PR-1994.md) | minor fix for xqa | 2025-10-28 |  | attention, mla |
| [#1995](../sources/prs/flashinfer/PR-1995.md) | Bugfix: Change get() -> GetDLTensorPtr() in cutlass FusedMoE validations | 2025-10-28 | kernel-fusion | kernel-fusion, moe |
| [#1999](../sources/prs/flashinfer/PR-1999.md) | unittest: Add head dim 256 test cases and mark as xfail | 2025-10-28 |  | attention |
| [#1982](../sources/prs/flashinfer/PR-1982.md) | fix: correct PDL parameter handling in RopeQuantize kernel | 2025-10-26 |  | attention, fp8, quantization |
| [#1979](../sources/prs/flashinfer/PR-1979.md) | feat: Add backend='auto' to mm_fp4 and enable autotune for backend='cudnn' | 2025-10-25 |  | fp4, gemm |
| [#1980](../sources/prs/flashinfer/PR-1980.md) | feat: autotune tile_tokens_dim in trtllm-gen MOE | 2025-10-25 | kernel-fusion | kernel-fusion, moe |
| [#1976](../sources/prs/flashinfer/PR-1976.md) | fix: Make attention microbenchmark correctly use page table | 2025-10-24 |  | attention |
| [#1978](../sources/prs/flashinfer/PR-1978.md) | fix: Skipping attention sink Blackwell test outside of Blackwell | 2025-10-24 |  | attention |
| [#1969](../sources/prs/flashinfer/PR-1969.md) | feat: enable deepgemm jit for fp8 block-scale on SM90 | 2025-10-23 |  | block-scale, fp8, gemm |
| [#1973](../sources/prs/flashinfer/PR-1973.md) | Feature: Add support for L40 FusedMoE in cutlass path | 2025-10-23 | kernel-fusion, warp-specialization | gemm, kernel-fusion, moe |
| [#1959](../sources/prs/flashinfer/PR-1959.md) | fix: Add cutlass as an mm_fp4 backend in compute capability 12.0 in benchmark code | 2025-10-21 |  | fp4 |
| [#1961](../sources/prs/flashinfer/PR-1961.md) | Fix: Verify scales are not None for Cutlass FP8 FusedMoE | 2025-10-21 | kernel-fusion | fp8, kernel-fusion, moe |
| [#1963](../sources/prs/flashinfer/PR-1963.md) | fix: ensure SM120/121 SFA/SFB contiguity | 2025-10-21 |  | gemm |
| [#1954](../sources/prs/flashinfer/PR-1954.md) | Feature: Support Relu2 activation in fused MoE | 2025-10-20 | epilogue-fusion, kernel-fusion | epilogue-fusion, gemm, kernel-fusion |
| [#1955](../sources/prs/flashinfer/PR-1955.md) | Update trtllm-gen fused moe routing kernel and add more kernels | 2025-10-20 | kernel-fusion | gemm, kernel-fusion, moe |
| [#1942](../sources/prs/flashinfer/PR-1942.md) | Add realistic bench for persistent kernel  | 2025-10-17 | persistent-kernel | attention, persistent-kernel |
| [#1926](../sources/prs/flashinfer/PR-1926.md) | Add layernorm op for inputs of mixed dtype | 2025-10-14 |  | gemm |
| [#1927](../sources/prs/flashinfer/PR-1927.md) | silu_and_mul nvfp4 quanization fusion rework | 2025-10-14 | kernel-fusion | fp4, kernel-fusion, nvfp4 |
| [#1924](../sources/prs/flashinfer/PR-1924.md) | MLA RoPE + quantization fused kernel: shape generalization for MHA / GQA | 2025-10-13 | kernel-fusion | attention, fp8, kernel-fusion |
| [#1912](../sources/prs/flashinfer/PR-1912.md) | fix: Fix trtllm-gen prefill IMA when batch_size==1 | 2025-10-10 |  | attention, flash-attention, prefill |
| [#1882](../sources/prs/flashinfer/PR-1882.md) | feat: Add FP4 TRTLLM-Gen throughput MOE batched gemms | 2025-10-07 | kernel-fusion | fp4, gemm, kernel-fusion |
| [#1883](../sources/prs/flashinfer/PR-1883.md) | misc: fix some B200 GEMM bench | 2025-10-07 |  | fp8, gemm |
| [#1878](../sources/prs/flashinfer/PR-1878.md) | Tune kernel compilation parameters for https://github.com/flashinfer-ai/flashinfer/pull/1850  | 2025-10-06 |  | attention, flash-attention, tma |
| [#1862](../sources/prs/flashinfer/PR-1862.md) | raise error for group_gemm_fp8_nt_groupwise then num_groups > 1 on sm120/121 | 2025-10-04 |  | fp4, fp8, gemm |
| [#1865](../sources/prs/flashinfer/PR-1865.md) | Bugfix: fix o_strides in persistent kernel  | 2025-10-04 | persistent-kernel | attention, persistent-kernel |
| [#1850](../sources/prs/flashinfer/PR-1850.md) | Add head_dim=64 for tcgen05 tcgen05 flash-attention implementation | 2025-10-03 | warp-specialization, persistent-kernel, pipeline-stages | tcgen05, flash-attention, attention |
| [#1826](../sources/prs/flashinfer/PR-1826.md) | Bugfix: Fix data hazard in persistent reduce | 2025-10-01 | persistent-kernel | attention, persistent-kernel |
| [#1829](../sources/prs/flashinfer/PR-1829.md) | feat: trtrllm-gen global scaled FP8 GEMMs | 2025-10-01 | kernel-fusion | fp8, gemm, kernel-fusion |
| [#1831](../sources/prs/flashinfer/PR-1831.md) | Update the routing for TRTLLMGEN to support kimi k2 and qwen | 2025-10-01 | kernel-fusion | kernel-fusion, moe |
| [#1835](../sources/prs/flashinfer/PR-1835.md) | [Quantization] Add per-expert global scaling factor for fp4 batched quantize | 2025-10-01 |  | fp4, quantization |
| [#1810](../sources/prs/flashinfer/PR-1810.md) | tests: Update support for tgv_gemm to SM100 only and add to ut | 2025-09-30 |  | gemm |
| [#1812](../sources/prs/flashinfer/PR-1812.md) | tests: upgrade cutlass, fix import and skip non-SM100 cutedsl two shot allreduce | 2025-09-30 |  | gemm |
| [#1817](../sources/prs/flashinfer/PR-1817.md) | fix: fp4 moe on sm120 | 2025-09-30 | kernel-fusion | fp4, kernel-fusion, moe |
| [#1819](../sources/prs/flashinfer/PR-1819.md) | feat:enable fp8 blockscale moe for fused cultass for sm90 | 2025-09-30 | kernel-fusion | fp8, gemm, kernel-fusion |
| [#1809](../sources/prs/flashinfer/PR-1809.md) | Support checks PoC | 2025-09-29 |  | fp4, gemm |
| [#1769](../sources/prs/flashinfer/PR-1769.md) | feat: add xqa fp8 mha and fp8 kv cache | 2025-09-25 |  | attention, fp8, mla |
| [#1771](../sources/prs/flashinfer/PR-1771.md) | Waive / disable test_mla_decode_kernel.py::test_mla_decode_kernel for not sm80  | 2025-09-25 |  | decode, mla |
| [#1774](../sources/prs/flashinfer/PR-1774.md) | Masked batch nvfp4 quantization | 2025-09-25 |  | fp4, nvfp4, quantization |
| [#1764](../sources/prs/flashinfer/PR-1764.md) | fix: fix cannot import name 'cuda' from 'cuda' in CUDA13 | 2025-09-24 |  | gemm |
| [#1766](../sources/prs/flashinfer/PR-1766.md) | Added xfail for mx_fp4 matmul on SM120 | 2025-09-24 |  | fp4, gemm |
| [#1767](../sources/prs/flashinfer/PR-1767.md) | tests: skip non SM100/103 for grouped deepgemm | 2025-09-24 |  | fp8, gemm |
| [#1768](../sources/prs/flashinfer/PR-1768.md) | add test case for trtllm gen fused moe with kimi k2 problem sizes | 2025-09-24 | kernel-fusion | kernel-fusion, moe |
| [#1757](../sources/prs/flashinfer/PR-1757.md) | fix: should pass global_override_indptr_cpu in fast_decode_plan param list | 2025-09-23 |  | decode |
| [#1752](../sources/prs/flashinfer/PR-1752.md) | tests: xfail attention sink UT for sliding window + non causal case | 2025-09-22 |  | attention |
| [#1754](../sources/prs/flashinfer/PR-1754.md) | tests: xfail moe quantization classes mxfp8_bf16 UTs on sm103  | 2025-09-22 | kernel-fusion | fp8, kernel-fusion, moe |
| [#1755](../sources/prs/flashinfer/PR-1755.md) | Fix tests/test_trtllm_gen_attention.py::test_trtllm_batch_prefill, ::test_trtllm_batch_decode mismatch error | 2025-09-22 |  | attention, decode, prefill |
| [#1745](../sources/prs/flashinfer/PR-1745.md) | feat: port fast_decode_plan from sgl | 2025-09-21 |  | decode |
| [#1723](../sources/prs/flashinfer/PR-1723.md) | Fix DeepSeek quality for TRTLLM fused MoE routing | 2025-09-19 | kernel-fusion | kernel-fusion, moe |
| [#1724](../sources/prs/flashinfer/PR-1724.md) | bugfix: partially fix tests/test_trtllm_gen_fused_moe.py unit test failure | 2025-09-19 | kernel-fusion | kernel-fusion, moe |
| [#1725](../sources/prs/flashinfer/PR-1725.md) | TVM: support TVM binding for GroupedGemm | 2025-09-19 |  | fp8, gemm, grouped-gemm |
| [#1727](../sources/prs/flashinfer/PR-1727.md) | fix: put sampling kernel launch into macro | 2025-09-19 |  | gemm |
| [#1695](../sources/prs/flashinfer/PR-1695.md) | [cute_dsl] add gemm + all reduce (two_shot) | 2025-09-18 | kernel-fusion, tma-multicast | cute-dsl, gemm, kernel-fusion |
| [#1716](../sources/prs/flashinfer/PR-1716.md) | perf: Add tuning config for cutlass moe for a hardware | 2025-09-18 | kernel-fusion | kernel-fusion, moe |
| [#1698](../sources/prs/flashinfer/PR-1698.md) | hotfix: Hotfix for `test_pod_kernels.py` on B300 | 2025-09-17 |  | gemm |
| [#1706](../sources/prs/flashinfer/PR-1706.md) | feat: Benchmark mm_fp4 mxfp4 support and gemm autotune support.  Restore mm_fp4 API behavior | 2025-09-17 |  | fp4, gemm |
| [#1707](../sources/prs/flashinfer/PR-1707.md) | bugfix: increase workspace to make trtllm gen attention unit test pass | 2025-09-17 |  | attention |
| [#1710](../sources/prs/flashinfer/PR-1710.md) | test: skip the unsupported test cases for sm120/121 | 2025-09-17 | kernel-fusion | attention, fp4, fp8 |
| [#1681](../sources/prs/flashinfer/PR-1681.md) | perf: improve attention of tcgen05 flash-attention | 2025-09-16 | warp-specialization, persistent-kernel | tcgen05, flash-attention, attention |
| [#1685](../sources/prs/flashinfer/PR-1685.md) | perf: Port the separate reduce kernel mode from trtllm. | 2025-09-16 |  | attention, flash-attention |
| [#1694](../sources/prs/flashinfer/PR-1694.md) | Update deepgemm backend for 103a | 2025-09-16 |  | fp8, gemm |
| [#1696](../sources/prs/flashinfer/PR-1696.md) | Support Kimi-K2 for TRT: templatize number of experts | 2025-09-16 | kernel-fusion | kernel-fusion, moe |
| [#1679](../sources/prs/flashinfer/PR-1679.md) | [misc] add a wrapper class for attention sink jit args | 2025-09-15 |  | attention |
| [#1682](../sources/prs/flashinfer/PR-1682.md) | Update TGV GEMM default kernel and TGV code cleanup. | 2025-09-15 |  | gemm |
| [#1668](../sources/prs/flashinfer/PR-1668.md) | TGV GEMM as a BF16 backend alternative to cuBLAS | 2025-09-14 | persistent-kernel, tile-scheduling | gemm, fp8, tcgen05 |
| [#1677](../sources/prs/flashinfer/PR-1677.md) | Support output signals for overlapping for cutedsl gemm | 2025-09-14 |  | gemm |
| [#1670](../sources/prs/flashinfer/PR-1670.md) | feat: Add `variant.OutputTransform()` to decode kernels | 2025-09-11 |  | attention, decode |
| [#1674](../sources/prs/flashinfer/PR-1674.md) | test: better fp8 quantization init for fused_moe test | 2025-09-11 | kernel-fusion | fp8, kernel-fusion, moe |
| [#1675](../sources/prs/flashinfer/PR-1675.md) | feat: Batch-size invariant FA2 Prefill & Decode | 2025-09-11 |  | attention, decode, prefill |
| [#1665](../sources/prs/flashinfer/PR-1665.md) | test: update fused_moe test to random scale factor | 2025-09-10 | kernel-fusion | kernel-fusion, moe |
| [#1666](../sources/prs/flashinfer/PR-1666.md) | [Hotfix] `test_fp4_quantize.py` failure on sm103 | 2025-09-10 |  | fp4, quantization |
| [#1667](../sources/prs/flashinfer/PR-1667.md) | Refactor Blackwell unit test scripts | 2025-09-10 |  | attention, gemm, moe |
| [#1656](../sources/prs/flashinfer/PR-1656.md) | Add benchmark for MLARopeQuantize | 2025-09-09 |  | fp8, mla, quantization |
| [#1661](../sources/prs/flashinfer/PR-1661.md) | perf&bugfix: skip kv-tile computation out of sliding window in FA2; fix __syncthreads in mergestate | 2025-09-09 |  | attention, decode, fp8 |
| [#1548](../sources/prs/flashinfer/PR-1548.md) | perf: Enable SplitK and fix tile-scheduling for moe fp4 fused moe | 2025-09-05 | tile-scheduling, fine-grained-quantization | moe, fp4, gemm |
| [#1636](../sources/prs/flashinfer/PR-1636.md) | test: pytest.mark.xfail on deepgemm | 2025-09-05 |  | fp8, gemm |
| [#1640](../sources/prs/flashinfer/PR-1640.md) | bugfix: Fix FLOPS calculation for bench_trtllm_gen_mla.py | 2025-09-05 |  | mla |
| [#1643](../sources/prs/flashinfer/PR-1643.md) | fix: zero-init workspace buffer for trtllm-gen fmha | 2025-09-05 |  | attention, flash-attention, mla |
| [#1644](../sources/prs/flashinfer/PR-1644.md) | Added mx_fp4 support using the cudnn backend | 2025-09-05 |  | fp4, gemm |
| [#1633](../sources/prs/flashinfer/PR-1633.md) | feat: add support of fp4_batched_quantize | 2025-09-04 |  | fp4, quantization |
| [#1635](../sources/prs/flashinfer/PR-1635.md) | fix: pass workspace for trtllm-gen attention | 2025-09-04 |  | attention, decode, prefill |
| [#1631](../sources/prs/flashinfer/PR-1631.md) | bugfix: trtllm-gen fmha sm101 and sm100 compatibility | 2025-09-03 |  | flash-attention |
| [#1622](../sources/prs/flashinfer/PR-1622.md) | bugfix: collect all modules to aot | 2025-09-02 | kernel-fusion | attention, decode, gemm |
| [#1614](../sources/prs/flashinfer/PR-1614.md) | bugfix: fix merge_attention_state in BatchAttention w/ gqa-group-size in Qwen family | 2025-09-01 | persistent-kernel | attention, persistent-kernel |
| [#1615](../sources/prs/flashinfer/PR-1615.md) | perf: Fix the tactic sorting in TrtllmGenBatchedGemmRunner::getValidConfigIndices | 2025-09-01 |  | gemm |
| [#1608](../sources/prs/flashinfer/PR-1608.md) | feat: initial support for SM103, SM110, SM120, SM121 | 2025-08-30 | kernel-fusion | attention, flash-attention, fp4 |
| [#1609](../sources/prs/flashinfer/PR-1609.md) | feat: cutlass fp4 gemm bringup for SM120 & SM121 | 2025-08-30 |  | fp4, gemm, quantization |
| [#1610](../sources/prs/flashinfer/PR-1610.md) | feat: cutlass fp8 gemm bringup for SM120 & SM121 | 2025-08-30 |  | fp8, gemm |
| [#1611](../sources/prs/flashinfer/PR-1611.md) | bugfix: fix fp4 quantization with 8x4 scale factor layout | 2025-08-30 |  | fp4, quantization |
| [#1596](../sources/prs/flashinfer/PR-1596.md) | bugfix: fix fused-temperature softmax IMA issue | 2025-08-28 | kernel-fusion | kernel-fusion, tma |
| [#1597](../sources/prs/flashinfer/PR-1597.md) | bugfix: fix the register overflow issue for topk renorm kernels on blackwell | 2025-08-28 |  | gemm |
| [#1599](../sources/prs/flashinfer/PR-1599.md) | bugfix: fix unittest test_fp8_quantize | 2025-08-28 |  | fp8, quantization |
| [#1601](../sources/prs/flashinfer/PR-1601.md) | feat: Enable MnnvlMemory (for alltoallv) on B200 | 2025-08-28 |  | gemm |
| [#1589](../sources/prs/flashinfer/PR-1589.md) | fix: limit the number of nvcc threads for each kernel | 2025-08-27 |  | gemm |
| [#1590](../sources/prs/flashinfer/PR-1590.md) | fix: Improve TRTLLM attention kernel out_dtype unit test | 2025-08-27 |  | attention, decode, prefill |
| [#1577](../sources/prs/flashinfer/PR-1577.md) | bugfix: update trtllm-gen gemm kernel names | 2025-08-26 |  | gemm |
| [#1578](../sources/prs/flashinfer/PR-1578.md) | feat: Support for inferring out_dtype from out.dtype for TRTLLM attention kernel | 2025-08-26 |  | attention, decode, prefill |
| [#1581](../sources/prs/flashinfer/PR-1581.md) | refactor: Expose calculate_tile_tokens_dim function | 2025-08-26 | kernel-fusion | kernel-fusion, moe |
| [#1582](../sources/prs/flashinfer/PR-1582.md) | bugfix: Fix arg passing to TORCH_CHECK and TORCH_WARN macros | 2025-08-26 | kernel-fusion | gemm, kernel-fusion, moe |
| [#1584](../sources/prs/flashinfer/PR-1584.md) | fix: semaphoress must be at the fixed range in workspace buffer on trtllm_gen attention | 2025-08-26 |  | attention, flash-attention |
| [#1585](../sources/prs/flashinfer/PR-1585.md) | bugfix: Fix test_fp4_quantize test bug | 2025-08-26 |  | fp4, quantization |
| [#1567](../sources/prs/flashinfer/PR-1567.md) | Backend: downgrade trtllm-gen kernel to cuda-12 | 2025-08-25 |  | attention, decode, flash-attention |
| [#1571](../sources/prs/flashinfer/PR-1571.md) | bugfix: fix cuda version guard macros | 2025-08-25 | kernel-fusion | kernel-fusion, moe |
| [#1573](../sources/prs/flashinfer/PR-1573.md) | update trtllm-gen fp4 autotuner and routing | 2025-08-25 | kernel-fusion | fp4, kernel-fusion, moe |
| [#1559](../sources/prs/flashinfer/PR-1559.md) | bugfix: fix persistent attention kernel correctness on blackwell | 2025-08-24 | persistent-kernel | attention, persistent-kernel |
| [#1565](../sources/prs/flashinfer/PR-1565.md) | fix: separate out fp4 lib into sm90 and sm100 versions, add oob checking in fused moe | 2025-08-24 | kernel-fusion | fp4, kernel-fusion, moe |
| [#1540](../sources/prs/flashinfer/PR-1540.md) | feat: Add fp8-qkv, fp16/bf16 output MHA | 2025-08-22 | kernel-fusion | attention, decode, fp8 |
| [#1545](../sources/prs/flashinfer/PR-1545.md) | fix trtllm_allreduce_fusion twoshot register problem. | 2025-08-22 | kernel-fusion | kernel-fusion |
| [#1547](../sources/prs/flashinfer/PR-1547.md) | perf: replace cudaGetDeviceProperties with cudaDeviceGetAttribute | 2025-08-22 | kernel-fusion | kernel-fusion, moe |
| [#1550](../sources/prs/flashinfer/PR-1550.md) | Add mnnvl_moe_alltoallv_prepare_without_allgather | 2025-08-22 |  | moe |
| [#1530](../sources/prs/flashinfer/PR-1530.md) | bugfix: Fix compile error for undefined swizzle enum. | 2025-08-21 | kernel-fusion, swizzling | fp8, kernel-fusion, moe |
| [#1533](../sources/prs/flashinfer/PR-1533.md) | bugfix: Fix Persistent kernel precision for masked output  | 2025-08-21 | persistent-kernel | attention, persistent-kernel, prefill |
| [#1534](../sources/prs/flashinfer/PR-1534.md) | Remove cuda-python from dependency and check at runtime | 2025-08-21 |  | gemm |
| [#1535](../sources/prs/flashinfer/PR-1535.md) | Add sm check for sm100 only cutlass/trtllm kernel | 2025-08-21 |  | gemm |
| [#1537](../sources/prs/flashinfer/PR-1537.md) | feat: Integrate TRTLLM varlen kernel for deepseek R1 prefill  | 2025-08-21 |  | attention, flash-attention, prefill |
| [#1518](../sources/prs/flashinfer/PR-1518.md) | backend: Refactor trtllm-gen fmha metainfo loading | 2025-08-20 |  | attention, decode, flash-attention |
| [#1521](../sources/prs/flashinfer/PR-1521.md) | refactor fp4 masked gemm cute-dsl implementation and add manual cache | 2025-08-20 |  | fp4, gemm |
| [#1523](../sources/prs/flashinfer/PR-1523.md) | Fix linking errors with CUDA 13 | 2025-08-20 |  | gemm |
| [#1525](../sources/prs/flashinfer/PR-1525.md) | Add GeGLU support to trtllm-gen NVFP4 Fused MoE Kernel | 2025-08-20 | kernel-fusion | fp4, gemm, kernel-fusion |
| [#1502](../sources/prs/flashinfer/PR-1502.md) | Add benchmark for cutedsl gemm | 2025-08-18 |  | gemm |
| [#1503](../sources/prs/flashinfer/PR-1503.md) | feat: integrate xqa attention backend | 2025-08-18 |  | attention |
| [#1507](../sources/prs/flashinfer/PR-1507.md) | update allreduce to match trtllm | 2025-08-18 | kernel-fusion | kernel-fusion |
| [#1508](../sources/prs/flashinfer/PR-1508.md) | Support cuda<12.8 built for trtllm_allreduce_fusion. | 2025-08-18 | kernel-fusion | kernel-fusion, moe |
| [#1509](../sources/prs/flashinfer/PR-1509.md) | bugfix: Fix stream handling in cutedsl gemm | 2025-08-18 |  | gemm |
| [#1512](../sources/prs/flashinfer/PR-1512.md) | flashinfer_benchmark QoL Improvements and Attention FP8 Support | 2025-08-18 |  | attention, fp8, gemm |
| [#1500](../sources/prs/flashinfer/PR-1500.md) | fix: Replace cub Max/Min with cuda::maximum/minimum for cuda 13 compatibility | 2025-08-16 |  | gemm |
| [#1495](../sources/prs/flashinfer/PR-1495.md) | fix: update masked moe gemm fp4 tensor reshape | 2025-08-15 |  | fp4, gemm, moe |
| [#1498](../sources/prs/flashinfer/PR-1498.md) | feat: scaling at fp4 gemm epilogue | 2025-08-15 | epilogue-fusion | epilogue-fusion, fp4, gemm |
| [#1483](../sources/prs/flashinfer/PR-1483.md) | perf: add fast path to TopPRenormProbKernel for top_p >= 1.0, significantly boosting SGLang workloads | 2025-08-14 |  | gemm |
| [#1484](../sources/prs/flashinfer/PR-1484.md) | feat: add pdl for trtllm-gen attn | 2025-08-14 |  | attention, decode, flash-attention |
| [#1488](../sources/prs/flashinfer/PR-1488.md) | fix: update cutedsl masked moe gemm | 2025-08-14 |  | gemm, moe |
| [#1490](../sources/prs/flashinfer/PR-1490.md) | feat: Support fp8 qkv, fp16/bf16 out MHA for trtllm-gen. | 2025-08-14 | kernel-fusion | attention, decode, flash-attention |
| [#1491](../sources/prs/flashinfer/PR-1491.md) | Perf: support scale_a/scale_b instead of combined scale in cutlass bmm_fp8 | 2025-08-14 |  | fp8, gemm |
| [#1479](../sources/prs/flashinfer/PR-1479.md) | refactor: unify autotuner for bmm_fp8 | 2025-08-13 |  | fp8, gemm |
| [#1480](../sources/prs/flashinfer/PR-1480.md) | fix missing enable_pdl argument in trtllm-gen fp4 moe | 2025-08-13 | kernel-fusion | fp4, kernel-fusion, moe |
| [#1481](../sources/prs/flashinfer/PR-1481.md) | Add python API for masked grouped gemm | 2025-08-13 |  | fp4, gemm |
| [#1469](../sources/prs/flashinfer/PR-1469.md) | bugfix: Verify num_experts greater or equal to local_experts + offset | 2025-08-12 | kernel-fusion | kernel-fusion, moe |
| [#1472](../sources/prs/flashinfer/PR-1472.md) | feat: Enable multiple fused-moe backends | 2025-08-12 | kernel-fusion | kernel-fusion, moe |
| [#1473](../sources/prs/flashinfer/PR-1473.md) | perf: add 1x4x1 cluster shape for fp8 bmm M<16 cases | 2025-08-12 |  | fp8, gemm |
| [#1475](../sources/prs/flashinfer/PR-1475.md) | tuner: Trtllm-gen Fp4 MoE Autotunner | 2025-08-12 | kernel-fusion | fp4, gemm, kernel-fusion |
| [#1453](../sources/prs/flashinfer/PR-1453.md) | feat: enable trtllm-gen attn speculative decoding verify by decode | 2025-08-11 |  | attention, decode, mla |
| [#1460](../sources/prs/flashinfer/PR-1460.md) | Fix TRTLLM NVFP4-out attention kernel scale factor dim issue | 2025-08-11 |  | attention, decode, fp4 |
| [#1444](../sources/prs/flashinfer/PR-1444.md) | fix: remote redundant zero_init from trtllm-gen attn | 2025-08-10 |  | decode, flash-attention |
| [#1445](../sources/prs/flashinfer/PR-1445.md) | Add alignment in MxFP8Quantization | 2025-08-10 |  | fp8, quantization |
| [#1446](../sources/prs/flashinfer/PR-1446.md) | Remove getEnvEnablePDL in favor of enable_pdl parameter | 2025-08-10 | kernel-fusion | flash-attention, fp4, fp8 |
| [#1415](../sources/prs/flashinfer/PR-1415.md) | benchmark: trtllm-gen mha with sink, add benchmark args | 2025-08-08 |  | attention, decode, flash-attention |
| [#1427](../sources/prs/flashinfer/PR-1427.md) | refactor: Sink attention AoT | 2025-08-08 |  | attention |
| [#1428](../sources/prs/flashinfer/PR-1428.md) | Fix redundant kernels in moe | 2025-08-08 | kernel-fusion | kernel-fusion, moe |
| [#1434](../sources/prs/flashinfer/PR-1434.md) | Fixes for Blackwell Tests | 2025-08-08 |  | gemm |
| [#1435](../sources/prs/flashinfer/PR-1435.md) | bugfix: fix perf issue by using fp8 graph that can use cublaslt | 2025-08-08 |  | fp8, gemm |
| [#1405](../sources/prs/flashinfer/PR-1405.md) | feature: enable cublas for fp4 gemm when cudnn == 9.11.1 or >= 9.13 | 2025-08-07 |  | fp4, gemm |
| [#1410](../sources/prs/flashinfer/PR-1410.md) | [bugfix] Fix compilation failure when compiling csrc/trtllm_moe_allreduce_fusion.cu | 2025-08-07 | kernel-fusion | kernel-fusion, moe |
| [#1412](../sources/prs/flashinfer/PR-1412.md) | Faster weight processing (moe nvfp4) | 2025-08-07 | kernel-fusion | fp4, kernel-fusion, moe |
| [#1396](../sources/prs/flashinfer/PR-1396.md) | gpt-oss: Add MXFP8 x MXFP4 CUTLASS MOE for SM100 and BF16 x MXFP4 CUTLASS for SM90 + SwigluBias Activation | 2025-08-06 | kernel-fusion, warp-specialization | fp4, fp8, gemm |
| [#1397](../sources/prs/flashinfer/PR-1397.md) | feature: add cutlass as bmm_fp8 backend. | 2025-08-06 |  | fp8, gemm |
| [#1398](../sources/prs/flashinfer/PR-1398.md) | Fix trtllm moe launcher local_num_experts | 2025-08-06 | kernel-fusion | kernel-fusion, moe |
| [#1399](../sources/prs/flashinfer/PR-1399.md) | Add Mxfp4 trtllm-gen moe unit tests | 2025-08-06 | kernel-fusion | decode, fp4, kernel-fusion |
| [#1402](../sources/prs/flashinfer/PR-1402.md) | fix shared memory alignment conflict in sampling.cuh | 2025-08-06 |  | gemm |
| [#1384](../sources/prs/flashinfer/PR-1384.md) | Allow BatchPrefillPagedWrapper to call cudnn API | 2025-08-05 |  | attention, prefill |
| [#1389](../sources/prs/flashinfer/PR-1389.md) | GPT-OSS Support: Add Blackwell MoE mxfp4 implementation from TRTLLM and Attention Sink | 2025-08-05 | kernel-fusion | attention, decode, flash-attention |
| [#1390](../sources/prs/flashinfer/PR-1390.md) | Adding FP8 benchmark on attention and matmul testing | 2025-08-05 |  | attention, fp8, gemm |
| [#1376](../sources/prs/flashinfer/PR-1376.md) | bugfix: Add guard for fp4/fp8 related include headers | 2025-08-04 |  | fp4, fp8 |
| [#1378](../sources/prs/flashinfer/PR-1378.md) | refactor: download trtllm gemm metadata from server | 2025-08-04 |  | gemm |
| [#1371](../sources/prs/flashinfer/PR-1371.md) | bugfix: fixed cutlass fused moe usage of FP4QuantizationSFLayout::SWIZZLED | 2025-08-03 | kernel-fusion, swizzling | fp4, kernel-fusion, moe |
| [#1363](../sources/prs/flashinfer/PR-1363.md) | Support scale factor start index for fp4 mha prefill/decode | 2025-08-01 |  | decode, flash-attention, fp4 |
| [#1358](../sources/prs/flashinfer/PR-1358.md) | [fix] remove (view) transpose to keep consistent with majorness MN requirement. | 2025-07-31 |  | fp8, gemm |
| [#1359](../sources/prs/flashinfer/PR-1359.md) | hotfix: update mxfp4 groupwise-scaled gemm unittests | 2025-07-31 |  | fp4, gemm |
| [#1360](../sources/prs/flashinfer/PR-1360.md) | support trtllm-gen prefill fp4 output | 2025-07-31 |  | decode, flash-attention, fp4 |
| [#1361](../sources/prs/flashinfer/PR-1361.md) | Update autotune results for the nvfp4 cutlass moe backends for v0.2.9 | 2025-07-31 | kernel-fusion | fp4, kernel-fusion, moe |
| [#1355](../sources/prs/flashinfer/PR-1355.md) | feature: add fp4 mm using trtllm backend | 2025-07-30 | kernel-fusion | fp4, gemm, kernel-fusion |
| [#1344](../sources/prs/flashinfer/PR-1344.md) | Fix bench deepgemm setting | 2025-07-29 |  | gemm |
| [#1348](../sources/prs/flashinfer/PR-1348.md) | fix: fix trtllm-gen mla error on new interface | 2025-07-29 |  | decode, flash-attention, mla |
| [#1350](../sources/prs/flashinfer/PR-1350.md) | Support passing kv_data_type to MultiLevelCascadeAttentionWrapper.plan() | 2025-07-29 |  | attention |
| [#1339](../sources/prs/flashinfer/PR-1339.md) | feat: Fused rope fp8 quantize kernel for MLA | 2025-07-28 | kernel-fusion | fp8, kernel-fusion, mla |
| [#1324](../sources/prs/flashinfer/PR-1324.md) | feat: Support logits_soft_cap for Persistent attn; fix kv split limit | 2025-07-25 | persistent-kernel | attention, persistent-kernel, prefill |
| [#1328](../sources/prs/flashinfer/PR-1328.md) | refactor: Improved metainfo for trtllm-gen kernels | 2025-07-25 | kernel-fusion | gemm, kernel-fusion, moe |
| [#1331](../sources/prs/flashinfer/PR-1331.md) | feat: masked layout fp4 gemm using cute-dsl | 2025-07-25 |  | fp4, gemm |
| [#1333](../sources/prs/flashinfer/PR-1333.md) | add torch float4_e2m1fn_x2 check for cudnn fp4 backend | 2025-07-25 |  | fp4, gemm |
| [#1334](../sources/prs/flashinfer/PR-1334.md) | [Fix] remove torch 2.8 requirement for FP4 GEMM | 2025-07-25 |  | fp4, gemm |
| [#1314](../sources/prs/flashinfer/PR-1314.md) | test qkvo quantization not equal to 1. | 2025-07-24 |  | decode, quantization |
| [#1316](../sources/prs/flashinfer/PR-1316.md) | minor: add trtllm_gen_mla benchmark | 2025-07-24 |  | mla |
| [#1317](../sources/prs/flashinfer/PR-1317.md) | Allow cudnn prefill kernels to be called natively | 2025-07-24 |  | prefill |
| [#1318](../sources/prs/flashinfer/PR-1318.md) | feat: support output nvfp4 in trtllm-gen function call. | 2025-07-24 |  | decode, flash-attention, fp4 |
| [#1319](../sources/prs/flashinfer/PR-1319.md) | Make Fp8 MoE routing_bias optional | 2025-07-24 | kernel-fusion | fp8, kernel-fusion, moe |
| [#1320](../sources/prs/flashinfer/PR-1320.md) | Add blockwise-scaled FP8 GEMM via TRTLLM-Gen. | 2025-07-24 |  | fp8, gemm, tma |
| [#1321](../sources/prs/flashinfer/PR-1321.md) | Optimizations for TRTLLM MNNVL Allreduce | 2025-07-24 |  | gemm |
| [#1322](../sources/prs/flashinfer/PR-1322.md) | feat: Add k_scale and v_scale to persistent attention  | 2025-07-24 | persistent-kernel | attention, persistent-kernel |
| [#1307](../sources/prs/flashinfer/PR-1307.md) | Fix the bug of the kernel-selection heuristic in trtllm-gen | 2025-07-23 |  | flash-attention |
| [#1309](../sources/prs/flashinfer/PR-1309.md) | Refactor Fused Moe Module | 2025-07-23 | kernel-fusion | fp4, gemm, kernel-fusion |
| [#1310](../sources/prs/flashinfer/PR-1310.md) | Support loading autotuned results from json for cutlass fp4 moe backends | 2025-07-23 | kernel-fusion | fp4, kernel-fusion, moe |
| [#1298](../sources/prs/flashinfer/PR-1298.md) | perfix: use lightweight API to query device property | 2025-07-22 | kernel-fusion | kernel-fusion, moe |
| [#1305](../sources/prs/flashinfer/PR-1305.md) | [Feature] SM level profiler  | 2025-07-22 |  | gemm |
| [#1294](../sources/prs/flashinfer/PR-1294.md) | Update cutlass fp4 moe kernels | 2025-07-21 | kernel-fusion, warp-specialization | fp4, fp8, gemm |
| [#1296](../sources/prs/flashinfer/PR-1296.md) | add cutlass backend for mm_fp4 | 2025-07-21 |  | fp4, gemm |
| [#1297](../sources/prs/flashinfer/PR-1297.md) | feat: Add weight layout option for trtllm-gen fused moe | 2025-07-21 | kernel-fusion | gemm, kernel-fusion, moe |
| [#1290](../sources/prs/flashinfer/PR-1290.md) | [fix] fix integer overflow in FA2 customized_mask & add buffer overflow warning. | 2025-07-19 |  | attention, quantization |
| [#1291](../sources/prs/flashinfer/PR-1291.md) | Remove FAST_BUILD FLAG for MOE | 2025-07-19 | kernel-fusion | gemm, kernel-fusion, moe |
| [#1292](../sources/prs/flashinfer/PR-1292.md) | refactor: Improved metainfo for trtllm-gen fmha | 2025-07-19 |  | decode, flash-attention |
| [#1281](../sources/prs/flashinfer/PR-1281.md) | Unify groupwise fp8 GEMM test | 2025-07-18 |  | fp8, gemm |
| [#1284](../sources/prs/flashinfer/PR-1284.md) | Convert scale_factor from scalar to Tensor in trt_allreduce_fusion | 2025-07-18 | kernel-fusion | kernel-fusion |
| [#1286](../sources/prs/flashinfer/PR-1286.md) | fix multiCtasKvScratchPtr misalignment issue (new one) | 2025-07-18 |  | flash-attention |
| [#1287](../sources/prs/flashinfer/PR-1287.md) | Bug fix: guard fp8 e8m0 and e2m1 compile  | 2025-07-18 | kernel-fusion | fp8, kernel-fusion, moe |
| [#1288](../sources/prs/flashinfer/PR-1288.md) | add mm_fp4 use cudnn backend | 2025-07-18 |  | fp4, gemm, quantization |
| [#1289](../sources/prs/flashinfer/PR-1289.md) | refactor: refactor trtllm-gen attention kernel integration code | 2025-07-18 |  | attention, decode, flash-attention |
| [#1278](../sources/prs/flashinfer/PR-1278.md) | hotfix: fix deepgemm artifactory hash | 2025-07-17 |  | gemm |
| [#1280](../sources/prs/flashinfer/PR-1280.md) | fix: update trtllm-gen fmha benchmark | 2025-07-17 |  | flash-attention |
| [#1266](../sources/prs/flashinfer/PR-1266.md) | feat: add masked deepgemm support and benchmarking | 2025-07-16 |  | fp8, gemm |
| [#1267](../sources/prs/flashinfer/PR-1267.md) | Bug fix: fix duplicate launch in POD | 2025-07-16 |  | attention |
| [#1272](../sources/prs/flashinfer/PR-1272.md) | Add shuffle matrix flag | 2025-07-16 | kernel-fusion | gemm, kernel-fusion, moe |
| [#1255](../sources/prs/flashinfer/PR-1255.md) | TRT-LLM's Multi-Node NVLink AR + fused RMSNorm kernel | 2025-07-15 | kernel-fusion | kernel-fusion |
| [#1258](../sources/prs/flashinfer/PR-1258.md) | feat: enable trtllm-gen mla MTP | 2025-07-15 |  | decode, flash-attention, mla |
| [#1264](../sources/prs/flashinfer/PR-1264.md) | init add gemm fp8 using cudnn backend | 2025-07-15 |  | fp8, gemm |
| [#1265](../sources/prs/flashinfer/PR-1265.md) | Made AR output optional + esthetic changes | 2025-07-15 |  | gemm |
| [#1249](../sources/prs/flashinfer/PR-1249.md) | Remove sm100+ requirment for trtllm allreduce kernels | 2025-07-14 | kernel-fusion | kernel-fusion, moe |
| [#1251](../sources/prs/flashinfer/PR-1251.md) | Reduce the JIT compilation time of gen_gemm_sm100_module | 2025-07-14 |  | fp4, fp8, gemm |
| [#1240](../sources/prs/flashinfer/PR-1240.md) | Patch fp8 cubin availability | 2025-07-11 | kernel-fusion | fp8, gemm, kernel-fusion |
| [#1241](../sources/prs/flashinfer/PR-1241.md) | feat: Support MXFP8 x MXFP4 CUTLASS grouped GEMM | 2025-07-11 |  | fp4, fp8, gemm |
| [#1242](../sources/prs/flashinfer/PR-1242.md) | Add trtllm-gen attention mha kernel with FP8 Q/K/V and FP8 output | 2025-07-11 |  | attention, decode, flash-attention |
| [#1239](../sources/prs/flashinfer/PR-1239.md) | add trtllm-gen context attention | 2025-07-10 |  | attention, decode, flash-attention |
| [#1230](../sources/prs/flashinfer/PR-1230.md) | feat: Add non-causal cudnn prefill kernels | 2025-07-08 |  | prefill |
| [#1234](../sources/prs/flashinfer/PR-1234.md) | bugfix: support uint8_t for vec_t class template | 2025-07-08 |  | gemm |
| [#1221](../sources/prs/flashinfer/PR-1221.md) | Enable cudnn decode and add tests for the cudnn decode kernel | 2025-07-07 |  | decode |
| [#1222](../sources/prs/flashinfer/PR-1222.md) | feat: add trtllm-gen mla cubin | 2025-07-07 |  | attention, decode, flash-attention |
| [#1227](../sources/prs/flashinfer/PR-1227.md) | Fix missing hash in the cudnn cubin path | 2025-07-07 |  | gemm |
| [#1213](../sources/prs/flashinfer/PR-1213.md) | [comm] TRT-LLM's Multi-Node NVLink All-Reduce Kernel | 2025-07-04 |  | gemm |
| [#1214](../sources/prs/flashinfer/PR-1214.md) | Feature/sm100 low latency nvfp4 kernels | 2025-07-04 | kernel-fusion | fp4, gemm, kernel-fusion |
| [#1211](../sources/prs/flashinfer/PR-1211.md) | Fix test_groupwise_scaled_gemm_fp8.py | 2025-07-03 |  | fp8, gemm |
| [#1212](../sources/prs/flashinfer/PR-1212.md) | feat: trtllm-gen fp8 moe kernels | 2025-07-03 | kernel-fusion | fp8, gemm, kernel-fusion |
| [#1208](../sources/prs/flashinfer/PR-1208.md) | Fix the issue with auxillary kernel launch and grid dim calculation | 2025-07-02 |  | prefill |
| [#1209](../sources/prs/flashinfer/PR-1209.md) | Add DeepGEMM kernels | 2025-07-02 |  | fp8, gemm |
| [#1206](../sources/prs/flashinfer/PR-1206.md) | [fix] fix BatchAttention CTA_TILE_KV mask issue | 2025-07-01 |  | attention |
| [#1198](../sources/prs/flashinfer/PR-1198.md) | bugfix: fix blackwell fmha hanging issue for empty kv_len | 2025-06-30 | epilogue-fusion | attention, epilogue-fusion, flash-attention |
| [#1200](../sources/prs/flashinfer/PR-1200.md) | [feat] optimize persistent batch attention perf. | 2025-06-30 | persistent-kernel | attention, persistent-kernel |
| [#1189](../sources/prs/flashinfer/PR-1189.md) | update trtllm-gen decode attention kernel launcher | 2025-06-28 |  | attention, decode, flash-attention |
| [#1181](../sources/prs/flashinfer/PR-1181.md) | bugfix: fix invalid blackwell fmha unittests | 2025-06-26 |  | flash-attention |
| [#1176](../sources/prs/flashinfer/PR-1176.md) | Expose fp4 blockscale swizzling kernel | 2025-06-25 | swizzling | fp4, quantization, swizzling |
| [#1177](../sources/prs/flashinfer/PR-1177.md) | [feat] support block sparse attention w/ variable block sizes and head-wise sparse patterns | 2025-06-25 |  | attention, sparse-attention |
| [#1178](../sources/prs/flashinfer/PR-1178.md) | bugfix: softmax NaN results caused by large -inf masks | 2025-06-25 |  | tma |
| [#1170](../sources/prs/flashinfer/PR-1170.md) | feat: logits processor fustion rule for temperature softmax | 2025-06-24 | kernel-fusion | kernel-fusion, tma |
| [#1164](../sources/prs/flashinfer/PR-1164.md) | feat: enable and update all-reduce fused quantization | 2025-06-22 | kernel-fusion | kernel-fusion, moe, quantization |
| [#1157](../sources/prs/flashinfer/PR-1157.md) | Add fp4 quantization swizzling tests | 2025-06-19 | swizzling | fp4, quantization, swizzling |
| [#1158](../sources/prs/flashinfer/PR-1158.md) | Add more logging to TRTLLM-GEN debug trace (NFC) | 2025-06-19 |  | flash-attention |
| [#1159](../sources/prs/flashinfer/PR-1159.md) | feat: add finalize_moe_allreduce from trtllm | 2025-06-19 | kernel-fusion | kernel-fusion, moe |
| [#1160](../sources/prs/flashinfer/PR-1160.md) | feat: nvshmem python bindings | 2025-06-19 |  | gemm |
| [#1161](../sources/prs/flashinfer/PR-1161.md) | feat: update non-fused moe | 2025-06-19 | kernel-fusion | kernel-fusion, moe |
| [#1153](../sources/prs/flashinfer/PR-1153.md) | feat: Fused temperature online softmax kernel | 2025-06-18 | kernel-fusion | kernel-fusion, tma |
| [#1140](../sources/prs/flashinfer/PR-1140.md) | Fix FA2 and FA3 multi-item scoring and cuda illegal memory access error | 2025-06-12 |  | attention, prefill |
| [#1136](../sources/prs/flashinfer/PR-1136.md) | fix: negative zero by type trait --> binary value | 2025-06-11 |  | gemm |
| [#1137](../sources/prs/flashinfer/PR-1137.md) | [feat] add unified batch attention w/ correctness tests. | 2025-06-11 | persistent-kernel | attention, persistent-kernel, prefill |
| [#1134](../sources/prs/flashinfer/PR-1134.md) | MNNVL MoE All-to-All Support | 2025-06-10 |  | moe |
| [#1131](../sources/prs/flashinfer/PR-1131.md) | feat: add trtllm all-reduce fusion | 2025-06-09 | kernel-fusion | kernel-fusion, moe |
| [#1129](../sources/prs/flashinfer/PR-1129.md) | Fix pointer dtype bug in rope | 2025-06-08 |  | gemm |
| [#1116](../sources/prs/flashinfer/PR-1116.md) | hotfix: fix the blackwell fmha stream | 2025-06-06 |  | attention, flash-attention |
| [#1117](../sources/prs/flashinfer/PR-1117.md) | [Feature] Support PDL for batch Prefill and Decode | 2025-06-06 |  | attention, decode, fp8 |
| [#1114](../sources/prs/flashinfer/PR-1114.md) | bugfix: Fix test and output shape of fp4 quantize | 2025-06-05 | epilogue-fusion, kernel-fusion | epilogue-fusion, fp4, gemm |
| [#1113](../sources/prs/flashinfer/PR-1113.md) | Add CUTLASS fused moe kernels from TensorRT-LLM. | 2025-06-04 | epilogue-fusion, kernel-fusion, pipeline-stages | epilogue-fusion, fp8, gemm |
| [#1108](../sources/prs/flashinfer/PR-1108.md) | feat: add trtllm moe_allreduce_fusion | 2025-06-02 | kernel-fusion | kernel-fusion, moe |
| [#1106](../sources/prs/flashinfer/PR-1106.md) | bugfix: host-precomuted plan function for blackwell fmha | 2025-05-31 | epilogue-fusion, kernel-fusion, tile-scheduling | attention, epilogue-fusion, flash-attention |
| [#1096](../sources/prs/flashinfer/PR-1096.md) | feat: add trtllm all-reduce (non-MoE) | 2025-05-28 |  | moe |
| [#1086](../sources/prs/flashinfer/PR-1086.md) | perf: accelerate blackwell grouped gemm | 2025-05-23 |  | fp8, gemm, grouped-gemm |
| [#1087](../sources/prs/flashinfer/PR-1087.md) | bugfix: fix fp8 attention kernels aot compilation issue | 2025-05-23 |  | attention, fp8, prefill |
| [#1089](../sources/prs/flashinfer/PR-1089.md) | comm: refactor and initialize `flashinfer.comm` module | 2025-05-23 |  | gemm |
| [#1071](../sources/prs/flashinfer/PR-1071.md) | bugfix: adding lse output to blackwell fmha kernels | 2025-05-20 | epilogue-fusion | attention, epilogue-fusion, flash-attention |
| [#1072](../sources/prs/flashinfer/PR-1072.md) | bugfix: follow user-specified sm_scale for blackwell cutlass fmha | 2025-05-20 |  | attention, flash-attention, prefill |
| [#1059](../sources/prs/flashinfer/PR-1059.md) | Parameterize prefix mask call (needed by POD-Attention) | 2025-05-14 |  | attention, prefill |
| [#1054](../sources/prs/flashinfer/PR-1054.md) | Fix KV chunking for POD.  | 2025-05-13 |  | attention |
| [#1055](../sources/prs/flashinfer/PR-1055.md) | bugfix: temporally disable split-kv in blackwell mla | 2025-05-13 |  | attention, mla |
| [#1050](../sources/prs/flashinfer/PR-1050.md) | fix: top_k_mask_logits hangs on -inf inputs | 2025-05-09 |  | gemm |
| [#1051](../sources/prs/flashinfer/PR-1051.md) | [nvidia] Add Blackwell FMHA decode kernel from TRT-LLM | 2025-05-09 |  | attention, decode, flash-attention |
| [#1039](../sources/prs/flashinfer/PR-1039.md) | [nvidia] initial support for blackwell kernels | 2025-04-24 | epilogue-fusion, kernel-fusion, tile-scheduling | attention, epilogue-fusion, flash-attention |
| [#1033](../sources/prs/flashinfer/PR-1033.md) | feat: add functional per-head FP8 quantization for FA3 | 2025-04-23 | epilogue-fusion | attention, decode, epilogue-fusion |
| [#1035](../sources/prs/flashinfer/PR-1035.md) | feat: Softmax free sampling | 2025-04-23 |  | tma |
| [#1029](../sources/prs/flashinfer/PR-1029.md) | fix: add zero init for KV tiled copy | 2025-04-21 |  | attention |
| [#1025](../sources/prs/flashinfer/PR-1025.md) | feat: ragged tensor padding kernel for blackwell kernel alignment | 2025-04-20 |  | gemm |
| [#1015](../sources/prs/flashinfer/PR-1015.md) | add multi-item scoring | 2025-04-11 | epilogue-fusion, tile-scheduling | attention, decode, epilogue-fusion |
| [#1013](../sources/prs/flashinfer/PR-1013.md) | bugfix: import wrapper of mla decode | 2025-04-10 |  | decode, mla |
| [#1014](../sources/prs/flashinfer/PR-1014.md) | misc: fix instrument code for mla profiler | 2025-04-10 |  | attention, mla |
| [#1007](../sources/prs/flashinfer/PR-1007.md) | feat: update decode attention APIs | 2025-04-07 |  | attention, decode, prefill |
| [#997](../sources/prs/flashinfer/PR-997.md) | 3rdparty: upgrade cutlass to 3.9 | 2025-04-03 |  | attention, mla |
| [#994](../sources/prs/flashinfer/PR-994.md) | feat: SM-constraint Communication Kernels | 2025-04-01 |  | gemm |
| [#991](../sources/prs/flashinfer/PR-991.md) | perf: prefetch page indices for mla kernel | 2025-03-31 |  | attention, mla |
| [#982](../sources/prs/flashinfer/PR-982.md) | SM-constraint-GEMM by triton persistent kernel | 2025-03-29 | persistent-kernel | gemm, persistent-kernel |
| [#983](../sources/prs/flashinfer/PR-983.md) | Triton `rms_norm` kernels | 2025-03-29 |  | gemm |
| [#974](../sources/prs/flashinfer/PR-974.md) | perf: dual pivot top-p/top-k renorm | 2025-03-26 |  | gemm |
| [#969](../sources/prs/flashinfer/PR-969.md) | perf: Fix python API overhead when CUDAGraph is not enabled | 2025-03-23 |  | decode, fp8, gemm |
| [#968](../sources/prs/flashinfer/PR-968.md) | perf: reduce torch.library dispatch overhead | 2025-03-22 |  | decode, gemm, mla |
| [#958](../sources/prs/flashinfer/PR-958.md) | [TVM] Added tvm binding for sampling kernel | 2025-03-18 |  | attention |
| [#952](../sources/prs/flashinfer/PR-952.md) | perf: Use 2WG pipeline design for MLA implementation on Hopper | 2025-03-17 | pipeline-stages | attention, mla, pipeline-stages |
| [#945](../sources/prs/flashinfer/PR-945.md) | bugfix: fix potential issues of FA3 template loading nans for PageAttention | 2025-03-14 |  | attention, mla |
| [#930](../sources/prs/flashinfer/PR-930.md) | feat: experimenta support of PDL | 2025-03-11 |  | gemm |
| [#913](../sources/prs/flashinfer/PR-913.md) | feat: flashinfer intra-kernel profiler | 2025-03-05 |  | attention, mla |
| [#901](../sources/prs/flashinfer/PR-901.md) | perf: tweak the pipeline design of mla kernel | 2025-02-27 | pipeline-stages | attention, mla, pipeline-stages |
| [#898](../sources/prs/flashinfer/PR-898.md) | perf: fix MLA split-k performance bug | 2025-02-25 |  | attention, mla |
| [#887](../sources/prs/flashinfer/PR-887.md) | perf: FlashAttention-3 style MLA PageAttention | 2025-02-23 | epilogue-fusion | attention, epilogue-fusion, mla |
| [#888](../sources/prs/flashinfer/PR-888.md) | feat - support mla kvcache store | 2025-02-23 |  | mla |
| [#869](../sources/prs/flashinfer/PR-869.md) | Naive Support for Hopper FP8 Prefill Kernel with Per-Head Quantization | 2025-02-18 | epilogue-fusion | attention, epilogue-fusion, fp8 |
| [#858](../sources/prs/flashinfer/PR-858.md) | Add POD-Attention to FlashInfer | 2025-02-17 |  | attention, decode, prefill |
| [#861](../sources/prs/flashinfer/PR-861.md) | unittest: add MLA test cases where kv_len is evenly divided by page_size. | 2025-02-17 |  | mla |
| [#863](../sources/prs/flashinfer/PR-863.md) | perf: dynamic split-k for MLA | 2025-02-17 |  | attention, mla |
| [#868](../sources/prs/flashinfer/PR-868.md) | bugfix: fix the behavior of MLA kernel when kv-length is 0 | 2025-02-17 |  | attention, mla |
| [#850](../sources/prs/flashinfer/PR-850.md) | misc: Remove duplicate param set in MLA kernel | 2025-02-16 |  | mla |
| [#844](../sources/prs/flashinfer/PR-844.md) | perf: MLA decode kernel implemented by CuTe targeted to SM80 | 2025-02-14 |  | attention, decode, mla |
| [#816](../sources/prs/flashinfer/PR-816.md) | bugfix: fix the behavior of mla plan function when provided with host tensors | 2025-02-13 |  | mla |
| [#821](../sources/prs/flashinfer/PR-821.md) | bugfix: bugfix on sm89 MLA | 2025-02-13 |  | attention, mla |
| [#827](../sources/prs/flashinfer/PR-827.md) | bugfix: fix the signature of `CutlassSegmentGEMMSM90` | 2025-02-13 |  | gemm |
| [#810](../sources/prs/flashinfer/PR-810.md) | bugfix: mla page-attention kernel for different page sizes | 2025-02-12 |  | attention, mla |
| [#812](../sources/prs/flashinfer/PR-812.md) | feat: unlocking MLA for A100 | 2025-02-12 |  | attention, mla |
| [#814](../sources/prs/flashinfer/PR-814.md) | feat: unlock MLA attention for sm89 (L40/L40s/4090) | 2025-02-12 |  | attention, mla |
| [#804](../sources/prs/flashinfer/PR-804.md) | perf: memory efficient deepseek mla fused page-attention kernel | 2025-02-10 | kernel-fusion | attention, kernel-fusion, mla |
| [#801](../sources/prs/flashinfer/PR-801.md) | feat: apply sm_scale at logits instead of q in FA2 template | 2025-02-09 |  | attention, decode, prefill |
| [#799](../sources/prs/flashinfer/PR-799.md) | feat: support f32 attention output in FA2 template | 2025-02-08 |  | attention, prefill |
| [#793](../sources/prs/flashinfer/PR-793.md) | fix rope logic in mla decoding | 2025-02-07 |  | attention, decode, mla |
| [#787](../sources/prs/flashinfer/PR-787.md) | bugfix: MLA decode should multiply sm_scale by math::log2e | 2025-02-05 |  | attention, decode, mla |
| [#781](../sources/prs/flashinfer/PR-781.md) | bugfix: fix batch prefill attention kernel unittests | 2025-02-04 |  | attention, prefill |
| [#785](../sources/prs/flashinfer/PR-785.md) | bugfix: drop CTA_TILE_Q=32 | 2025-02-04 |  | prefill |
| [#776](../sources/prs/flashinfer/PR-776.md) | perf: refactor fa2 prefill template | 2025-02-03 |  | attention, prefill |
| [#778](../sources/prs/flashinfer/PR-778.md) | feat: Separate QK/VO head dim dispatch for sm90 AOT | 2025-02-03 |  | prefill |
| [#774](../sources/prs/flashinfer/PR-774.md) | bugfix: Ensure Loop Termination by Enforcing IEEE-754 Compliance in Sampling Kernels | 2025-02-01 |  | gemm |
| [#765](../sources/prs/flashinfer/PR-765.md) | feat: support deepseek prefill attention shape | 2025-01-30 | epilogue-fusion | attention, decode, epilogue-fusion |
| [#754](../sources/prs/flashinfer/PR-754.md) | Change `apply_rope_with_cos_sin_cache` to accept `cos_sin_cache` | 2025-01-27 |  | gemm |
| [#728](../sources/prs/flashinfer/PR-728.md) | Align KV chunk size binary search with actual KV chunk splitting. | 2025-01-09 |  | attention |
| [#718](../sources/prs/flashinfer/PR-718.md) | bugfix: FusedAddRMSNorm kernels might require more than 48KB shared memory when d is large. | 2025-01-06 | kernel-fusion | kernel-fusion |
| [#714](../sources/prs/flashinfer/PR-714.md) | perf: fix the iteration bound of SWA in FA2 prefill template | 2025-01-03 |  | attention, prefill |

<a id="pytorchpytorch"></a>
## pytorch/pytorch
85 PRs

| PR | Title | Date | Techniques | Tags |
|-----|-------|------|------------|------|
| [#180470](../sources/prs/pytorch/PR-180470.md) | [release 2.12] Apply Release only changes to 2.12 branch | 2026-04-15 |  | attention, flash-attention, quantization |
| [#178009](../sources/prs/pytorch/PR-178009.md) | [MPS] fix compiling of SDPA producing nan results | 2026-03-20 |  | gemm |
| [#177144](../sources/prs/pytorch/PR-177144.md) | [Inductor] Don't unfuse addmm for bf16/fp16 to avoid precision loss | 2026-03-11 |  | gemm |
| [#177193](../sources/prs/pytorch/PR-177193.md) | [Inductor][MPS] Fix half-precision type mismatches in Metal shader codegen (#176436) | 2026-03-11 |  | gemm |
| [#176783](../sources/prs/pytorch/PR-176783.md) | [inductor] Fix Identity comparability and evalf recursion | 2026-03-07 |  | gemm |
| [#176410](../sources/prs/pytorch/PR-176410.md) | [Inductor] Reject non-contiguous subnode fusion in mix-order reduction. | 2026-03-04 | kernel-fusion | kernel-fusion |
| [#176495](../sources/prs/pytorch/PR-176495.md) | [inductor] avoid multi-stage for mix-order-red by default (#176228) | 2026-03-04 |  | gemm |
| [#175826](../sources/prs/pytorch/PR-175826.md) | [CI] Update inductor CI jobs to CUDA 13.0 | 2026-02-26 |  | python |
| [#175567](../sources/prs/pytorch/PR-175567.md) | [release-only] Remove +ptx from cuda 13.0 builds | 2026-02-23 |  | gemm |
| [#175580](../sources/prs/pytorch/PR-175580.md) | [MPS] Fix 2-pass SDPA memory corruption by forcing float accumulators | 2026-02-23 |  | attention |
| [#175299](../sources/prs/pytorch/PR-175299.md) | [benchmark] Skip pytorch_CycleGAN_and_pix2pix from inductor benchmarks | 2026-02-19 |  | gemm |
| [#175091](../sources/prs/pytorch/PR-175091.md) | [RELEASE 2.11] Release only changes | 2026-02-16 |  | attention, flash-attention, quantization |
| [#175096](../sources/prs/pytorch/PR-175096.md) | Update inductor expected accuracy files | 2026-02-16 |  | gemm |
| [#172577](../sources/prs/pytorch/PR-172577.md) | [Graph Partition] Improve support for mutation ops | 2026-01-15 |  | gemm |
| [#172141](../sources/prs/pytorch/PR-172141.md) | Skip modded_nanogpt model in TorchInductor benchmark | 2026-01-09 |  | gemm |
| [#171895](../sources/prs/pytorch/PR-171895.md) | [cherry-pick][cuDNN][SDPA] cuDNN SDPA off-by-default for cuDNN versions < 12.9 (#171627) | 2026-01-07 |  | gemm |
| [#171247](../sources/prs/pytorch/PR-171247.md) | [xpu][fix][inductor] fallback bfloat16 atomics to eager | 2025-12-24 |  | gemm |
| [#171150](../sources/prs/pytorch/PR-171150.md) | Avoid closing random file handles in Inductor | 2025-12-23 |  | gemm |
| [#171189](../sources/prs/pytorch/PR-171189.md) | [cherry-pick][CUDA] Upgrade cuDNN to 9.15.1 for CUDA 13 builds  | 2025-12-23 |  | gemm |
| [#171129](../sources/prs/pytorch/PR-171129.md) | [Inductor] Fix constants handling for Triton constexpr (triton#8248) | 2025-12-22 |  | gemm |
| [#171140](../sources/prs/pytorch/PR-171140.md) | [ROCm] Make grouped GEMM CK opt‑in via env and default to fallback path | 2025-12-22 |  | gemm |
| [#170884](../sources/prs/pytorch/PR-170884.md) | [inductor] Fix cudagraph skip for index_put_ with boolean indices, gr… | 2025-12-19 |  | gemm |
| [#170486](../sources/prs/pytorch/PR-170486.md) | [flex_attention] adds support for low precision K/V inputs in compiled mode with GPU | 2025-12-16 |  | attention, flash-attention |
| [#170555](../sources/prs/pytorch/PR-170555.md) | [cherry-pick] Fix vllm issue for flex (#170499) | 2025-12-16 |  | attention |
| [#170190](../sources/prs/pytorch/PR-170190.md) | [ROCm] Enable shared memory based pruning for Triton configs | 2025-12-11 |  | gemm |
| [#170246](../sources/prs/pytorch/PR-170246.md) | [Inductor] ExternKernelBenchmarkRequest best attempt | 2025-12-11 |  | gemm |
| [#170112](../sources/prs/pytorch/PR-170112.md) | [RELEASE 2.10] Release only changes | 2025-12-10 |  | quantization |
| [#167327](../sources/prs/pytorch/PR-167327.md) | [cuDNN][SDPA][Convolution] Expose cuDNN runtime version in CUDA hooks | 2025-11-07 |  | gemm |
| [#167121](../sources/prs/pytorch/PR-167121.md) | [cuDNN][SDPA] Check-in test for #166211 | 2025-11-05 |  | gemm |
| [#166910](../sources/prs/pytorch/PR-166910.md) | [inductor] don't try to reorder loops for template | 2025-11-04 |  | gemm |
| [#166913](../sources/prs/pytorch/PR-166913.md) | [Dynamo] Don't guard data ptrs by default with mark_static_address | 2025-11-04 |  | gemm |
| [#166922](../sources/prs/pytorch/PR-166922.md) | [Inductor] No longer throw error in bmm out_dtype lowering due to tem… | 2025-11-04 |  | gemm |
| [#166967](../sources/prs/pytorch/PR-166967.md) | [Graph Partition] move custom rules to inductor config (#166458) | 2025-11-04 |  | gemm |
| [#166985](../sources/prs/pytorch/PR-166985.md) | [Graph Partition] fix graph partition input signature for fallback kernels | 2025-11-04 |  | gemm |
| [#166994](../sources/prs/pytorch/PR-166994.md) | [GraphPartition] cache get_free_symbol_uses (#166338) | 2025-11-04 |  | gemm |
| [#167020](../sources/prs/pytorch/PR-167020.md) | [Minor][Inductor] move some combo kernel log from warning to debug | 2025-11-04 |  | gemm |
| [#164893](../sources/prs/pytorch/PR-164893.md) | CUDA 13.0 builds fix on Amazon Linux 2023 | 2025-10-07 |  | gemm |
| [#164364](../sources/prs/pytorch/PR-164364.md) | [SDPA] [MPS] Fixes regression in 2.8.0 for scaled_dot_product_attention using mps | 2025-10-01 |  | attention |
| [#164368](../sources/prs/pytorch/PR-164368.md) | [Flex attention] Fix flex attention head broadcast | 2025-10-01 |  | attention |
| [#164236](../sources/prs/pytorch/PR-164236.md) | [AARCH64][CD][CUDA13][Triton][PTXAS] Turn on BUILD_BUNDLE_PTXAS=1   | 2025-09-30 |  | gemm |
| [#164026](../sources/prs/pytorch/PR-164026.md) | [cuDNN][SDPA] Disable dropout for cuDNN SDPA on 9.11 - 9.13 | 2025-09-27 |  | gemm |
| [#163954](../sources/prs/pytorch/PR-163954.md) | Move inductor jobs 3.9->3.10 | 2025-09-26 |  | gemm |
| [#163861](../sources/prs/pytorch/PR-163861.md) | fix pickling for BitwiseFn | 2025-09-25 |  | gemm |
| [#163764](../sources/prs/pytorch/PR-163764.md) | [Cherry-Pick] [CD] CUDA 13 specific followup changes. Remove sm50-70 From CUDA 12.6 and CUDA 12.8 builds (#162455) | 2025-09-24 |  | gemm |
| [#163766](../sources/prs/pytorch/PR-163766.md) | [CD] CUDA 13.0 fix preload logic to include nvidia/cu13/lib/ | 2025-09-24 |  | gemm |
| [#163633](../sources/prs/pytorch/PR-163633.md) | CUDA 13.0 Warning update for supported architectures | 2025-09-23 |  | gemm |
| [#163583](../sources/prs/pytorch/PR-163583.md) | [2.9 cherry pick][triton] update 3.5 pin to bbb06c0334a6772b92d24bde54956e675c8c6604 (#163382) | 2025-09-22 |  | gemm |
| [#163585](../sources/prs/pytorch/PR-163585.md) | CUDA 13.0 Warning update for supported architectures | 2025-09-22 |  | python |
| [#163388](../sources/prs/pytorch/PR-163388.md) | [Inductor][Intel GPU] Save `threads_per_warp` from tirton compiled kernel for launching kernel correctly in cpp wrapper. | 2025-09-20 |  | gemm |
| [#163395](../sources/prs/pytorch/PR-163395.md) | [graph partition] Add way to register custom rule (#163310) | 2025-09-20 |  | gemm |
| [#163380](../sources/prs/pytorch/PR-163380.md) | [Graph Partition] improve custom op output alias | 2025-09-19 |  | gemm |
| [#163265](../sources/prs/pytorch/PR-163265.md) | [Release 2.9] [cuDNN][SDPA][submodule] Roll-back cuDNN frontend upgrade, update Met… | 2025-09-18 |  | gemm |
| [#163097](../sources/prs/pytorch/PR-163097.md) | [Cherry Pick][Graph Partition] allow sharing default device context | 2025-09-16 |  | gemm |
| [#162764](../sources/prs/pytorch/PR-162764.md) | fix cpp extension distributed warning spew | 2025-09-11 |  | python, cuda-cpp |
| [#162455](../sources/prs/pytorch/PR-162455.md) | [CD] CUDA 13 specific followup changes. Remove sm50-70 From CUDA 12.6 and CUDA 12.8 builds | 2025-09-09 |  | python |
| [#162501](../sources/prs/pytorch/PR-162501.md) | CUDA 13.0 Windows Nvidia Driver Update to 580.88 | 2025-09-09 |  | gemm |
| [#158646](../sources/prs/pytorch/PR-158646.md) | [cherry-pick][inductor][triton] Update HAS_WARP_SPEC to check triton.Config params. Update Triton Hash to top of release/3.4.x stack | 2025-07-18 |  | gemm |
| [#158301](../sources/prs/pytorch/PR-158301.md) | Add warning about removed sm50 and sm60 arches | 2025-07-15 |  | python |
| [#158237](../sources/prs/pytorch/PR-158237.md) | [MPS] Switch Cholesky  decomp to column wise | 2025-07-14 |  | gemm |
| [#157752](../sources/prs/pytorch/PR-157752.md) | [release] Triton pin update to 3.4 | 2025-07-08 |  | gemm |
| [#157422](../sources/prs/pytorch/PR-157422.md) | [PowerPC] Fixed build issue for vsx vec256 complexfloat and scaled_mm_out_cpu  | 2025-07-02 |  | gemm |
| [#157241](../sources/prs/pytorch/PR-157241.md) | [user triton] AOT inductor support for device-side TMA | 2025-06-29 |  | tma |
| [#156932](../sources/prs/pytorch/PR-156932.md) | Fix macOS build with `USE_MPS=OFF` | 2025-06-26 |  | gemm |
| [#154121](../sources/prs/pytorch/PR-154121.md) | Fix uint view copy (#151598) | 2025-05-22 |  | gemm |
| [#153641](../sources/prs/pytorch/PR-153641.md) | [FlexAttention] explicilty create grad_q w/ strides | 2025-05-15 |  | attention |
| [#153304](../sources/prs/pytorch/PR-153304.md) | Mark auto_functionalized HOPs as cacheable (#151194) | 2025-05-10 |  | gemm |
| [#153104](../sources/prs/pytorch/PR-153104.md) | [FlexAttention] Remove Old Constraint on lastdim strides | 2025-05-07 |  | attention |
| [#152967](../sources/prs/pytorch/PR-152967.md) | [ATen][CUDA] Optimize 128 bit vectorization | 2025-05-06 |  | gemm |
| [#152774](../sources/prs/pytorch/PR-152774.md) | [dynamo][super variable] Fix bug to use correct source | 2025-05-04 |  | gemm |
| [#150676](../sources/prs/pytorch/PR-150676.md) | [CUDA][avgpool2d] Fix backward launch bounds again for `sm100`, `sm120` | 2025-04-04 |  | gemm |
| [#150705](../sources/prs/pytorch/PR-150705.md) | [CUDA] Only use vec128 if CUDA version is newer than 12.8 | 2025-04-04 | vectorized-loads | cuda-cpp |
| [#150640](../sources/prs/pytorch/PR-150640.md) | [CUDA][avgpool2d] Fix backward launch bounds again for sm100, sm120 | 2025-04-03 |  | cuda-cpp |
| [#150447](../sources/prs/pytorch/PR-150447.md) | [inductor] Fix inductor windows linker error | 2025-04-01 |  | gemm |
| [#150448](../sources/prs/pytorch/PR-150448.md) | [Windows][inductor] fix blank space break windows file path | 2025-04-01 |  | gemm |
| [#150145](../sources/prs/pytorch/PR-150145.md) | Dont exclude constant_pad_nd in prologue fusion | 2025-03-27 | kernel-fusion | kernel-fusion |
| [#149993](../sources/prs/pytorch/PR-149993.md) | [inductor][triton 3.3] Fix cpp_wrapper w/ TMA in triton 3.3 | 2025-03-26 |  | tma |
| [#149871](../sources/prs/pytorch/PR-149871.md) | Add release branch push triggers to inductor-rocm-mi300.yml | 2025-03-24 |  | gemm |
| [#149644](../sources/prs/pytorch/PR-149644.md) | op should NOT be static in aoti_torch_call_dispatcher | 2025-03-20 |  | gemm |
| [#149386](../sources/prs/pytorch/PR-149386.md) | Add AOTI shim for _weight_int4pack_mm_cpu_tensor (#149031) | 2025-03-18 |  | quantization |
| [#149125](../sources/prs/pytorch/PR-149125.md) | Remove runtime dependency on packaging | 2025-03-13 |  | gemm |
| [#149059](../sources/prs/pytorch/PR-149059.md) | [inductor] Fix profiler tests with latest Triton | 2025-03-12 |  | gemm |
| [#144398](../sources/prs/pytorch/PR-144398.md) | ROCm SDPA: Ensure attn_mask has the same dtype with q | 2025-01-08 |  | gemm |
| [#144335](../sources/prs/pytorch/PR-144335.md) | Fix PythonMod printing | 2025-01-07 |  | gemm |
| [#144248](../sources/prs/pytorch/PR-144248.md) | [inductor][cpu] Fix bmm b_index for dynamic expressions in inductor autotuner | 2025-01-06 |  | gemm |
| [#144209](../sources/prs/pytorch/PR-144209.md) | Update torch-xpu-ops commit pin | 2025-01-05 |  | gemm |

<a id="sgl-projectsglang"></a>
## sgl-project/sglang
105 PRs

| PR | Title | Date | Techniques | Tags |
|-----|-------|------|------------|------|
| [#22773](../sources/prs/sglang/PR-22773.md) | [Step3p5] Optimize allreduce in MoE layers  | 2026-04-14 |  | moe |
| [#22653](../sources/prs/sglang/PR-22653.md) | [Docker] Remove flashinfer cache copy | 2026-04-13 |  | gemm |
| [#22672](../sources/prs/sglang/PR-22672.md) | reland [Diffusion] Add FLUX.1-dev ModelOpt NVFP4 support | 2026-04-13 | kernel-fusion, pipeline-stages | fp4, fp8, kernel-fusion |
| [#22681](../sources/prs/sglang/PR-22681.md) | [Diffusion] Add Wan2.2 ModelOpt NVFP4 support | 2026-04-13 | kernel-fusion | fp4, kernel-fusion, nvfp4 |
| [#22723](../sources/prs/sglang/PR-22723.md) | [Fix] Fix accuracy bug in Flashmla sparse MLA kernel | 2026-04-13 |  | mla |
| [#22574](../sources/prs/sglang/PR-22574.md) | [Diffusion] Add FLUX.1-dev ModelOpt NVFP4 support | 2026-04-11 | kernel-fusion, pipeline-stages | fp4, fp8, kernel-fusion |
| [#22484](../sources/prs/sglang/PR-22484.md) | [RL] Fix weight update for mxfp8 flashinfer_cutlass gemm backend | 2026-04-10 |  | fp8, gemm, quantization |
| [#22491](../sources/prs/sglang/PR-22491.md) | [CI/Docker] Clean up redundant flashinfer cubin downloads | 2026-04-10 |  | gemm |
| [#22424](../sources/prs/sglang/PR-22424.md) | [AMD] Use aiter CK layernorm2d for LayerNorm to reduce NSA indexer kernel launches | 2026-04-09 |  | attention |
| [#22430](../sources/prs/sglang/PR-22430.md) | [Fix] Fix several bugs on DSA models | 2026-04-09 |  | attention |
| [#22440](../sources/prs/sglang/PR-22440.md) | Upgrade sglang-torch-profiler-analysis SKILLS | 2026-04-09 |  | gemm |
| [#22306](../sources/prs/sglang/PR-22306.md) | Lazy import flash_attention_v4 to avoid loading flash_attn.cute at startup | 2026-04-08 |  | attention, flash-attention |
| [#22314](../sources/prs/sglang/PR-22314.md) | [AMD] Fix GLM-5 fp8 KV quant path dispatch on MI300 | 2026-04-08 |  | fp8 |
| [#22316](../sources/prs/sglang/PR-22316.md) | [Reland] DeepSeek-R1-0528-w4a8: DeepEP Low Latency Dispatch Adopts FP8 Communication | 2026-04-08 |  | fp8, moe, quantization |
| [#22322](../sources/prs/sglang/PR-22322.md) | [Docker] Fix Trivy CVEs, cubin download 403s, and kernels command order | 2026-04-08 |  | gemm |
| [#22323](../sources/prs/sglang/PR-22323.md) | [Lora] Lora quat info re-factor and support deepseekv3 mla lora | 2026-04-08 |  | fp8, mla, moe |
| [#22336](../sources/prs/sglang/PR-22336.md) | [AMD] Add GLM-5.1-FP8 nightly accuracy and performance benchmarks for MI30x and MI35x | 2026-04-08 |  | fp8 |
| [#22365](../sources/prs/sglang/PR-22365.md) | [Diffusion] modelopt diffusion fp8 support for flux1/flux2 and wan2.2 | 2026-04-08 | kernel-fusion | fp8, kernel-fusion, quantization |
| [#22372](../sources/prs/sglang/PR-22372.md) | [DSA] Hopper FP8 FlashMLA KV padding | 2026-04-08 |  | attention, fp8, mla |
| [#22381](../sources/prs/sglang/PR-22381.md) | [Lora] Lora kimi support | 2026-04-08 |  | moe, quantization |
| [#22232](../sources/prs/sglang/PR-22232.md) | Reduce unnecessary kernels and copies in the NSA indexer | 2026-04-07 |  | attention |
| [#22258](../sources/prs/sglang/PR-22258.md) | [AMD][HIP] NSA: bf16 passthrough from RMSNorm to eliminate FP8 dequantization | 2026-04-07 |  | attention, fp8, quantization |
| [#22187](../sources/prs/sglang/PR-22187.md) | [HiSparse]: Add benchmark for hisparse kernel | 2026-04-06 |  | gemm |
| [#22204](../sources/prs/sglang/PR-22204.md) | [RL] Refactor NVFP4 shuffling/swizzling to in-place replacement | 2026-04-06 | swizzling | fp4, moe, nvfp4 |
| [#22127](../sources/prs/sglang/PR-22127.md) | [Diffusion] Add diffusion NVFP4 scaled-mm correctness test | 2026-04-05 | kernel-fusion | fp4, kernel-fusion, nvfp4 |
| [#22134](../sources/prs/sglang/PR-22134.md) | [Hotfix] Fix router gemm on sm103 | 2026-04-05 |  | gemm |
| [#22145](../sources/prs/sglang/PR-22145.md) | [Disagg][NIXL] Fix heterogeneous TP KV transfer for non-MLA models (same logic with mooncake, Step 1/2 for Qwen3.5 support) | 2026-04-05 |  | mla |
| [#22155](../sources/prs/sglang/PR-22155.md) | [hisparse]: Adding ci for hisparse kvcache-swap-in jit-kernel | 2026-04-05 |  | gemm |
| [#22091](../sources/prs/sglang/PR-22091.md) | [diffusion] Default NVFP4 to CUTLASS and add all-model shape benchmarks | 2026-04-04 | kernel-fusion | fp4, kernel-fusion, nvfp4 |
| [#21987](../sources/prs/sglang/PR-21987.md) | [Bugfix] Fix CUDA graph replay issues in trtllm_mla draft_extend | 2026-04-03 |  | attention, mla |
| [#22006](../sources/prs/sglang/PR-22006.md) | Tiny fix trtllm_fp8_per_tensor_scale_moe_wrapper router_logits dtype | 2026-04-03 |  | fp8, moe |
| [#22024](../sources/prs/sglang/PR-22024.md) | [NPU] enable mla prepare fused kernel only when being mla attn | 2026-04-03 | kernel-fusion | attention, kernel-fusion, mla |
| [#22051](../sources/prs/sglang/PR-22051.md) | [MUSA][9/N] Add FA3 attention backend support through MATE (MUSA AI Tensor Engine) | 2026-04-03 |  | attention |
| [#22064](../sources/prs/sglang/PR-22064.md) | [Diffusion] Fix weight scale swizzle and add large-M kernel config for FLUX.2-dev-NVFP4 | 2026-04-03 | kernel-fusion, swizzling | fp4, gemm, kernel-fusion |
| [#22079](../sources/prs/sglang/PR-22079.md) | [nvidia] Gemma4 nvfp4 fix | 2026-04-03 |  | attention, fp4, gemm |
| [#21888](../sources/prs/sglang/PR-21888.md) | fix pcg torch dynamo recompile in mxfp8 Triton path | 2026-04-02 |  | fp8, quantization |
| [#21906](../sources/prs/sglang/PR-21906.md) | [Bugfix] Temporarily skip TRTLLM attention on (G)B300 (SM103) to avoid high-concurrency hang | 2026-04-02 |  | attention |
| [#21914](../sources/prs/sglang/PR-21914.md) | [DSA] Set trtllm kernels as default for Blackwell | 2026-04-02 |  | gemm |
| [#21834](../sources/prs/sglang/PR-21834.md) | [Feature] JIT rmsnorm update (with claude) | 2026-04-01 | kernel-fusion | kernel-fusion |
| [#21861](../sources/prs/sglang/PR-21861.md) |   [GDN] Remove FlashInfer GDN decode + no_buffer guard and default to FlashInfer on SM100+   | 2026-04-01 |  | decode |
| [#21881](../sources/prs/sglang/PR-21881.md) | [Misc] [MXFP8] Drop sm100 mxfp8 warning | 2026-04-01 |  | fp8 |
| [#21776](../sources/prs/sglang/PR-21776.md) | Harden FlashInfer FP4 imports in standard dispatcher | 2026-03-31 |  | fp4, moe |
| [#21780](../sources/prs/sglang/PR-21780.md) | [Fix] Fall back to triton MOE for GPT-OSS on Blackwell with driver >= 595 | 2026-03-31 |  | moe |
| [#21783](../sources/prs/sglang/PR-21783.md) | [DSA] Support trtllm sparse mla kernel for prefill batches  | 2026-03-31 |  | attention, mla, prefill |
| [#21787](../sources/prs/sglang/PR-21787.md) | Remove redundant test_moe_eval_accuracy_large | 2026-03-31 |  | moe |
| [#21649](../sources/prs/sglang/PR-21649.md) | fix: TRT-LLM MHA CUDA illegal address with EAGLE v2 + DP attention | 2026-03-30 |  | attention |
| [#21657](../sources/prs/sglang/PR-21657.md) | [AMD] Use tgemm.mm for MoEGate router gemm in deepseek_v2.py | 2026-03-30 |  | gemm, moe |
| [#21710](../sources/prs/sglang/PR-21710.md) | [AMD] Add GLM-5-FP8 nightly performance benchmarks for MI30x and MI35x | 2026-03-30 |  | fp8 |
| [#21711](../sources/prs/sglang/PR-21711.md) | Remove flashinfer wheel cache cleanup that deletes other versions | 2026-03-30 |  | gemm |
| [#21576](../sources/prs/sglang/PR-21576.md) | [FlashInver v0.6.7] Integrate flashinfer_trtllm mxfp8 gemm | 2026-03-28 |  | fp8, gemm, quantization |
| [#21595](../sources/prs/sglang/PR-21595.md) | Change default mm-attention backend from triton_attn to fa4 | 2026-03-28 |  | attention |
| [#21511](../sources/prs/sglang/PR-21511.md) | [AMD] Enable FP8 KV cache and FP8 attention kernel for NSA on MI300/MI355 with TileLang backend | 2026-03-27 |  | attention, fp8, mla |
| [#21561](../sources/prs/sglang/PR-21561.md) | test: point DSV3 int8 MLA CI models to lmsys Hugging Face org | 2026-03-27 |  | mla |
| [#21436](../sources/prs/sglang/PR-21436.md) | fix nemotron capture for non attention layers | 2026-03-26 |  | attention |
| [#21446](../sources/prs/sglang/PR-21446.md) | Add explicit disable flag for FlashInfer allreduce fusion | 2026-03-26 | kernel-fusion | kernel-fusion |
| [#21452](../sources/prs/sglang/PR-21452.md) | fix: piecewise_cuda_graph get correct qo_indptr | 2026-03-26 |  | attention |
| [#21463](../sources/prs/sglang/PR-21463.md) | Migrate all callers from /get_server_info to /server_info | 2026-03-26 |  | attention, fp4, fp8 |
| [#21411](../sources/prs/sglang/PR-21411.md) | [GDN] Fuse GDN kkt + solve_tril into one kernel | 2026-03-25 | kernel-fusion | attention, kernel-fusion |
| [#21428](../sources/prs/sglang/PR-21428.md) | [Bugfix] Lazy-import CuteDSL KDA kernel to fix AMD/ROCm startup crash | 2026-03-25 |  | attention |
| [#21278](../sources/prs/sglang/PR-21278.md) | P2P Weight Update features for miles  | 2026-03-24 |  | moe |
| [#21280](../sources/prs/sglang/PR-21280.md) | [RL] Support mxfp8 DeepSeek V3 | 2026-03-24 | kernel-fusion | fp8, kernel-fusion, moe |
| [#21314](../sources/prs/sglang/PR-21314.md) | CUTLASS NVFP4 GEMM improvement of SM120 | 2026-03-24 |  | fp4, gemm, nvfp4 |
| [#21325](../sources/prs/sglang/PR-21325.md) | [misc] clean up kernel API | 2026-03-24 | kernel-fusion | attention, flash-attention, fp4 |
| [#21339](../sources/prs/sglang/PR-21339.md) | Add dedicated FlashInferCuteDslMoE layer for standard-path FP4 MoE | 2026-03-24 |  | fp4, moe, quantization |
| [#21166](../sources/prs/sglang/PR-21166.md) | [Not-Merge][AMD] GLM-5 performance optimization | 2026-03-23 |  | attention |
| [#21190](../sources/prs/sglang/PR-21190.md) | [Whisper] Enable CUDA graph support and timestamp for whisper model | 2026-03-23 |  | attention |
| [#21200](../sources/prs/sglang/PR-21200.md) | [NPU] bugfix for import sgl-kernel error | 2026-03-23 |  | gemm |
| [#21203](../sources/prs/sglang/PR-21203.md) | [KDA] Support CuTeDSL KDA decode kernel | 2026-03-23 |  | attention, decode |
| [#21213](../sources/prs/sglang/PR-21213.md) | [AMD]: Support MLA with nhead<16 and FP8 KV cache for TP=8 (Kimi K2.5… | 2026-03-23 |  | attention, fp4, fp8 |
| [#21219](../sources/prs/sglang/PR-21219.md) | Split pr-test.yml: extract sgl-kernel, jit-kernel, and multimodal-gen tests into separate workflow files | 2026-03-23 |  | gemm |
| [#21233](../sources/prs/sglang/PR-21233.md) | [refactor] Clean up duplicate flashinfer trtllm moe code | 2026-03-23 | kernel-fusion | kernel-fusion, moe, quantization |
| [#21239](../sources/prs/sglang/PR-21239.md) | Refactor JIT kernel CI to use run_suite.py registration system | 2026-03-23 | kernel-fusion | attention, flash-attention, fp4 |
| [#21240](../sources/prs/sglang/PR-21240.md) | [NVIDIA] Enable FP4 flashinfer trtllm routed moe | 2026-03-23 |  | fp4, moe, quantization |
| [#21118](../sources/prs/sglang/PR-21118.md) | ci: remove IS_BLACKWELL env var; auto-detect Blackwell | 2026-03-22 |  | gemm |
| [#20957](../sources/prs/sglang/PR-20957.md) | [Tiny Fix] Fix IS_BLACKWELL env var empty string warning in rerun-ut workflow | 2026-03-20 |  | gemm |
| [#20988](../sources/prs/sglang/PR-20988.md) | ci: run Stage A CUDA tests as stage-a-test-small-1-gpu on 5090 | 2026-03-20 | kernel-fusion | attention, fp8, kernel-fusion |
| [#21019](../sources/prs/sglang/PR-21019.md) | [Qwen3.5] Fuse split/reshape/cat ops in GDN projection with Triton kernel | 2026-03-20 | kernel-fusion | kernel-fusion |
| [#21022](../sources/prs/sglang/PR-21022.md) | [Chore] Clean up JIT compilation flags | 2026-03-20 |  | fp4, nvfp4 |
| [#21035](../sources/prs/sglang/PR-21035.md) | fix: wrap _import_static_state in inference_mode to fix resume on Blackwell | 2026-03-20 |  | gemm |
| [#20910](../sources/prs/sglang/PR-20910.md) | Add SGLang CUDA crash API logging inspired by FlashInfer | 2026-03-19 | kernel-fusion | attention, flash-attention, fp4 |
| [#20868](../sources/prs/sglang/PR-20868.md) | fix: guard configure_deep_gemm_num_sms when JIT disabled | 2026-03-18 |  | gemm |
| [#20874](../sources/prs/sglang/PR-20874.md) | [JIT Kernel] Fix NVFP4 multi-arch compilation failure | 2026-03-18 |  | fp4, nvfp4 |
| [#20887](../sources/prs/sglang/PR-20887.md) | CUTLASS FP8 Blockwise GEMM improvement of SM120 | 2026-03-18 |  | fp8, gemm |
| [#20755](../sources/prs/sglang/PR-20755.md) | Use FlashInfer tinygemm for GPT-OSS MoE router on SM90+ | 2026-03-17 |  | gemm, moe |
| [#20699](../sources/prs/sglang/PR-20699.md) | [Diffusion] Fix compile graph broken by flashinfer rope | 2026-03-16 | kernel-fusion | kernel-fusion |
| [#20708](../sources/prs/sglang/PR-20708.md) | Add Mistral Small 4 (Pixtral) support | 2026-03-16 |  | moe |
| [#20606](../sources/prs/sglang/PR-20606.md) | FIX: (NSA) Compute topk_indices_offset when NSA prefill flashmla_sparse is used with FP8 KV cache | 2026-03-15 |  | attention, fp8, mla |
| [#20632](../sources/prs/sglang/PR-20632.md) | [Diffusion] Add a benchmark for rmsnorm/fuse_add_rmsnorm | 2026-03-15 | kernel-fusion | kernel-fusion |
| [#20604](../sources/prs/sglang/PR-20604.md) | Use Flashinfer for target_verify in GDN model for SM120 | 2026-03-14 |  | attention |
| [#20501](../sources/prs/sglang/PR-20501.md) | [Kernel] Fuse temperature + softmax in sampling for decode speedup | 2026-03-13 | kernel-fusion | decode, kernel-fusion, tma |
| [#20394](../sources/prs/sglang/PR-20394.md) | [NVIDIA] Enable fp8 flashinfer_trtllm_routed MoE for MiniMax-M2.5 | 2026-03-12 |  | fp8, moe, quantization |
| [#20399](../sources/prs/sglang/PR-20399.md) | [AMD][Bug-fix] Fix gpu fault when run the test with dp-attention-enabled and max-concurrency is over 256 | 2026-03-12 |  | attention |
| [#20407](../sources/prs/sglang/PR-20407.md) | [Model] Support Nemotron 3 Super NVFP4 | 2026-03-12 |  | fp4, nvfp4, quantization |
| [#20409](../sources/prs/sglang/PR-20409.md) | [AMD][AITER] Guard _use_mla_ps_kernel with self.use_mla in draft_extend_v2 paths | 2026-03-12 |  | attention, mla |
| [#20428](../sources/prs/sglang/PR-20428.md) | [GDN] Add benchmark for sglang gdn prefill | 2026-03-12 |  | attention, prefill |
| [#20380](../sources/prs/sglang/PR-20380.md) | fix ci by removing nvidia-cutlass-dsl-libs-base and force reinstall n… | 2026-03-11 |  | gemm |
| [#20384](../sources/prs/sglang/PR-20384.md) | [Fix] Add fallback for flashinfer allreduce fusion | 2026-03-11 | kernel-fusion | kernel-fusion |
| [#20268](../sources/prs/sglang/PR-20268.md) | [4/n jit_kernel restruct] speed up CI tests and add benchmark workflow | 2026-03-10 | kernel-fusion | fp4, kernel-fusion, moe |
| [#20294](../sources/prs/sglang/PR-20294.md) | [AMD] Add 4-GPU test suite for MI325 runners | 2026-03-10 |  | attention |
| [#20305](../sources/prs/sglang/PR-20305.md) | [Benchmark] use flashinfer bench_gpu_time instead of triton do_bench | 2026-03-10 | kernel-fusion | attention, fp4, fp8 |
| [#5390](../sources/prs/sglang/PR-5390.md) | Add Cutlass MLA attention backend | 2025-04-28 | warp-specialization, persistent-kernel, tile-scheduling | tcgen05, mla, moe |
| [#5432](../sources/prs/sglang/PR-5432.md) | [perf] introduce deep gemm group_gemm_masked as gemm | 2025-04-20 | fine-grained-quantization, kernel-fusion | gemm, moe, decode |
| [#4165](../sources/prs/sglang/PR-4165.md) | DeepGemm integrate to gemm | 2025-03-10 | jit-compilation, fine-grained-quantization | gemm, jit-compilation |
| [#3529](../sources/prs/sglang/PR-3529.md) | integrate blockwise fp8 kernel | 2025-02-12 | fine-grained-quantization | fp8, fine-grained-quantization, moe |
| [#3056](../sources/prs/sglang/PR-3056.md) | feat: integrate gemm_fp8 kernel into gemm | 2025-01-22 | fine-grained-quantization | fp8, gemm, moe |

<a id="vllm-projectvllm"></a>
## vllm-project/vllm
126 PRs

| PR | Title | Date | Techniques | Tags |
|-----|-------|------|------------|------|
| [#40057](../sources/prs/vllm/PR-40057.md) | [Bugfix] Temporarily disable B200 fp4 MoE layer tests | 2026-04-16 |  | fp4, moe |
| [#39752](../sources/prs/vllm/PR-39752.md) | add warning when FP8 KV cache misses prefill query quantization | 2026-04-14 |  | attention, fp8, mla |
| [#39796](../sources/prs/vllm/PR-39796.md) | [Bugfix] add support for 'num_attention_groups' in ModelArchConfigConvertorBase for Step3p5 | 2026-04-14 |  | attention |
| [#39820](../sources/prs/vllm/PR-39820.md) | [Bug] Fix batch invariance nvfp4 support | 2026-04-14 |  | fp4, nvfp4 |
| [#39825](../sources/prs/vllm/PR-39825.md) | [Bugfix] Disable FlashInfer CUTLASS MoE on SM121 (DGX Spark) | 2026-04-14 | kernel-fusion | kernel-fusion, moe |
| [#39676](../sources/prs/vllm/PR-39676.md) | [XPU] properly handle q_descale on XPU as quant query input not supported | 2026-04-13 |  | attention |
| [#39707](../sources/prs/vllm/PR-39707.md) | [Bugfix] Fix mismatch between global and local attention heads in tensor-parallel mode for param2moe model | 2026-04-13 |  | attention, moe |
| [#39717](../sources/prs/vllm/PR-39717.md) | [Bugfix] Reject non-nvfp4 dtypes when using the flashinfer_nvlink_one_sided all2all backend | 2026-04-13 | kernel-fusion | fp4, kernel-fusion, moe |
| [#39724](../sources/prs/vllm/PR-39724.md) | [Bugfix][NIXL] Fix `_logical_to_kernel_block_ids` conversion for non-mamba models | 2026-04-13 |  | gemm |
| [#39596](../sources/prs/vllm/PR-39596.md) | [Mooncake] Fix mixed MLA+Eagle block-size validation | 2026-04-12 |  | mla |
| [#39644](../sources/prs/vllm/PR-39644.md) | [Bugfix] [Tests] Enforce `out` tensor device in `kernel/moe/test_cutedsl_moe.py` | 2026-04-12 |  | moe |
| [#39510](../sources/prs/vllm/PR-39510.md) | [Kernel] Support TRTLLM GEN NVFP4 MoE for non-512-aligned hidden dims via weight padding | 2026-04-10 | kernel-fusion | fp4, kernel-fusion, moe |
| [#39542](../sources/prs/vllm/PR-39542.md) | [Bugfix] Fix tensor shape mismatch in sparse attention with speculative decoding | 2026-04-10 |  | attention |
| [#39458](../sources/prs/vllm/PR-39458.md) | [MLA] Optimize mla indexer prepare uniform decode for MTP > 1 | 2026-04-09 |  | attention, decode, mla |
| [#39315](../sources/prs/vllm/PR-39315.md) | [Bugfix] FlashInfer MXINT4 MoE crashes, missing do_finalize | 2026-04-08 |  | moe, quantization |
| [#39322](../sources/prs/vllm/PR-39322.md) | [Feature] Batch invariant nvfp4 linear support | 2026-04-08 |  | fp4, nvfp4, quantization |
| [#39353](../sources/prs/vllm/PR-39353.md) | [Model Runner V2] Fix flex attention kv blocks calculation issue | 2026-04-08 |  | attention |
| [#39361](../sources/prs/vllm/PR-39361.md) | Fix NUMA binding on non-CDMM Grace-Blackwell systems | 2026-04-08 |  | gemm |
| [#39183](../sources/prs/vllm/PR-39183.md) | perf(moe): add tuned fused_moe config for RTX PRO 6000 Blackwell Server Edition | 2026-04-07 | kernel-fusion | fp8, kernel-fusion, moe |
| [#39205](../sources/prs/vllm/PR-39205.md) | [Refactor] Move MXFP8 GEMM management into MxFp8LinearKernel | 2026-04-07 |  | fp8, gemm, quantization |
| [#39225](../sources/prs/vllm/PR-39225.md) | [Bug] Fix rocm sparse attn indexer issue | 2026-04-07 |  | attention, mla |
| [#39054](../sources/prs/vllm/PR-39054.md) | [Bug] Fix Trtllm Fp8 MoE Weight Shuffle Memory Fragamentation | 2026-04-06 |  | fp8, moe, quantization |
| [#39064](../sources/prs/vllm/PR-39064.md) | [Bugfix] Fix GDN FLA kernel crashes with NULL_BLOCK_ID=0 CUDA graph padding | 2026-04-06 | kernel-fusion | kernel-fusion |
| [#39088](../sources/prs/vllm/PR-39088.md) | [XPU] Quick fix for TritonMLA to remove cuda hardcode | 2026-04-06 | kernel-fusion | attention, kernel-fusion, mla |
| [#39119](../sources/prs/vllm/PR-39119.md) | [ROCm] Align AiterFlashAttentionImpl attn_type check with backend | 2026-04-06 |  | attention |
| [#39129](../sources/prs/vllm/PR-39129.md) | [Refactor] Move NVFP4 GEMM management into NvFp4LinearKernel | 2026-04-06 |  | fp4, gemm, nvfp4 |
| [#39007](../sources/prs/vllm/PR-39007.md) | [MoE] Move GPT OSS Triton kernel experts into fused_moe/experts/ | 2026-04-05 | kernel-fusion | fp4, kernel-fusion, moe |
| [#39045](../sources/prs/vllm/PR-39045.md) | [Gemma4] Support quantized MoE  | 2026-04-05 |  | gemm, moe, quantization |
| [#38960](../sources/prs/vllm/PR-38960.md) | [MoE Refactor] Split up compressed_tensors_moe.py | 2026-04-04 |  | fp4, fp8, moe |
| [#38989](../sources/prs/vllm/PR-38989.md) | [Bug] Fix routing bias dtype for trtllm per-block fp8 moe | 2026-04-04 | kernel-fusion | fp8, kernel-fusion, moe |
| [#38990](../sources/prs/vllm/PR-38990.md) | [Bugfix][MoE] Fix 6-8% decode regression: prefer multi-stream shared expert overlap | 2026-04-04 | kernel-fusion | decode, kernel-fusion, moe |
| [#38993](../sources/prs/vllm/PR-38993.md) | [Perf] Change Trtllm fp8 MoE to use Shuffled Weights and BlockMajorK Layout | 2026-04-04 | kernel-fusion | fp8, gemm, kernel-fusion |
| [#38995](../sources/prs/vllm/PR-38995.md) | [Quantization] - Layerwise reloading of Attention/KV quantized models | 2026-04-04 |  | attention, quantization |
| [#39002](../sources/prs/vllm/PR-39002.md) | [Bugfix] Fix FlashInfer crash with kv_cache_dtype_skip_layers | 2026-04-04 | kernel-fusion | attention, kernel-fusion |
| [#38859](../sources/prs/vllm/PR-38859.md) | [Bugfix] Re-enable Renormalize routing for TRT-LLM MoE experts | 2026-04-03 | kernel-fusion | fp8, kernel-fusion, moe |
| [#38865](../sources/prs/vllm/PR-38865.md) | [Refactor] Improve indexer decode path metadata preparation | 2026-04-03 |  | attention, decode, mla |
| [#38879](../sources/prs/vllm/PR-38879.md) | [Gemma4] Enable Fast Prefill Optimization | 2026-04-03 |  | gemm, prefill |
| [#38922](../sources/prs/vllm/PR-38922.md) | [Bugfix] Fix broken explicit unquantized kv cache dtype support | 2026-04-03 |  | attention, fp8, quantization |
| [#38791](../sources/prs/vllm/PR-38791.md) | [Bugfix] Fix test mocks after SM100 restriction in #38730 | 2026-04-02 |  | attention |
| [#38794](../sources/prs/vllm/PR-38794.md) | [Perf] Reduce H2D pageable memory copies | 2026-04-02 |  | attention |
| [#38810](../sources/prs/vllm/PR-38810.md) | [LMCache][MP] optimize save when mla enabled | 2026-04-02 |  | mla |
| [#38814](../sources/prs/vllm/PR-38814.md) | [FlashAttention] Symlink FA4 instead of copying when using `VLLM_FLASH_ATTN_SRC_DIR` | 2026-04-02 |  | attention |
| [#38815](../sources/prs/vllm/PR-38815.md) | [Quant] add CompressedTensorsW8A8Mxfp8 for linear and MoE layers | 2026-04-02 |  | fp8, moe, quantization |
| [#38819](../sources/prs/vllm/PR-38819.md) | [Attention][MLA] Re-enable FA4 as default MLA prefill backend | 2026-04-02 |  | attention, mla, prefill |
| [#38832](../sources/prs/vllm/PR-38832.md) | [Bugfix] Fix NVFP4+MTP crash: force unquantized mtp.fc for Qwen3.5 | 2026-04-02 |  | fp4, nvfp4, quantization |
| [#38835](../sources/prs/vllm/PR-38835.md) | [Attention] relax the head dim 512 and paged kv for sm90+FA4 | 2026-04-02 |  | attention |
| [#38682](../sources/prs/vllm/PR-38682.md) | [XPU] add  xpu backend implementation of mxfp8 quant | 2026-04-01 |  | fp8, quantization |
| [#38690](../sources/prs/vllm/PR-38690.md) | [FA4] Update flash-attention to latest upstream FA4 | 2026-04-01 |  | attention, flash-attention |
| [#38730](../sources/prs/vllm/PR-38730.md) | [Bugfix] Restrict TRTLLM attention to SM100, fixing GB300 (SM103) hang | 2026-04-01 |  | attention |
| [#38615](../sources/prs/vllm/PR-38615.md) | [ROCm] Fix aiter persistent mode mla with q/o nhead<16 for kimi-k2.5 tp8 | 2026-03-31 | persistent-kernel | attention, mla, persistent-kernel |
| [#38631](../sources/prs/vllm/PR-38631.md) | Fix MLA runs when use_inductor_graph_partition=True | 2026-03-31 |  | attention, mla |
| [#38491](../sources/prs/vllm/PR-38491.md) | [XPU] Fix spec-decode UTs under tests/v1/spec_decode | 2026-03-30 |  | decode |
| [#38562](../sources/prs/vllm/PR-38562.md) | [Bugfix][MLA] Change default SM100 MLA prefill backend back to TRT-LLM | 2026-03-30 |  | attention, mla, prefill |
| [#38573](../sources/prs/vllm/PR-38573.md) | [Compile] Fix nvfp4 compile warning | 2026-03-30 |  | fp4, nvfp4, quantization |
| [#38460](../sources/prs/vllm/PR-38460.md) | [Perf] Batch KV cache swap copies via cuMemcpyBatchAsync | 2026-03-29 |  | gemm |
| [#38479](../sources/prs/vllm/PR-38479.md) | [Attention Backend] TurboQuant: 2-bit KV cache compression with 4x capacity | 2026-03-29 |  | attention, decode, quantization |
| [#38423](../sources/prs/vllm/PR-38423.md) | [NVIDIA] Bugfix NVFP4 DGX Spark and RTX50 | 2026-03-28 | kernel-fusion | fp4, fp8, kernel-fusion |
| [#38427](../sources/prs/vllm/PR-38427.md) | [Bugfix] Enable batch-invariant Triton matmul on all Ampere GPUs (SM 8x)  | 2026-03-28 |  | gemm |
| [#38311](../sources/prs/vllm/PR-38311.md) | [Model Runner V2] Rebuild attention metadata before eagle decode full… | 2026-03-27 |  | attention, decode |
| [#38325](../sources/prs/vllm/PR-38325.md) | [Kernel] Add swapAB support for SM120 CUTLASS blockwise FP8 GEMM  | 2026-03-27 |  | fp8, gemm, quantization |
| [#38329](../sources/prs/vllm/PR-38329.md) | [MoE] Add RoutingMethodType.Simulated to TRT-LLM FP8/NVFP4 kernel allowlists | 2026-03-27 | kernel-fusion | fp4, fp8, kernel-fusion |
| [#38361](../sources/prs/vllm/PR-38361.md) | [GDN] Eliminate GPU->CPU sync in prepare_chunk_indices during prefill | 2026-03-27 |  | attention, prefill |
| [#38391](../sources/prs/vllm/PR-38391.md) | [CI Bugfix] Pre-download missing FlashInfer headers in Docker build | 2026-03-27 |  | gemm |
| [#38251](../sources/prs/vllm/PR-38251.md) | [Quantization] Add FlashInfer CuteDSL batched experts backend for NVFP4 MoE | 2026-03-26 | kernel-fusion | fp4, kernel-fusion, moe |
| [#38050](../sources/prs/vllm/PR-38050.md) | [MoE Kernel] Flashinfer nvfp4 cutedsl moe kernel integration | 2026-03-25 | kernel-fusion | fp4, kernel-fusion, moe |
| [#38083](../sources/prs/vllm/PR-38083.md) | [Bugfix] Fix DeepGemm E8M0 accuracy degradation for Qwen3.5 FP8 on Blackwell | 2026-03-25 |  | fp4, fp8, gemm |
| [#37940](../sources/prs/vllm/PR-37940.md) | [NIXL][BUG] Fix Triton heterogeneous TP | 2026-03-24 |  | attention |
| [#37948](../sources/prs/vllm/PR-37948.md) | [Perf] triton bilinear_pos_embed kernel for ViT | 2026-03-24 |  | gemm |
| [#37880](../sources/prs/vllm/PR-37880.md) | [Feature] Support per-draft-model MoE backend via `--speculative-config` | 2026-03-23 |  | decode, moe |
| [#37887](../sources/prs/vllm/PR-37887.md) | [ROCm][perf] fix Aiter sparse MLA with MTP>1 | 2026-03-23 |  | decode, mla |
| [#37759](../sources/prs/vllm/PR-37759.md) | [MoE] Move FlashInfer CuteDSL experts into fused_moe/experts/ | 2026-03-21 | kernel-fusion | fp4, kernel-fusion, moe |
| [#37695](../sources/prs/vllm/PR-37695.md) | [Perf] Use torch compile to fuse pack topk in trtllm moe | 2026-03-20 | kernel-fusion | fp4, fp8, kernel-fusion |
| [#37718](../sources/prs/vllm/PR-37718.md) | [Bug] Fix fp8 deepgemm batch invariant | 2026-03-20 |  | fp8, gemm, quantization |
| [#37719](../sources/prs/vllm/PR-37719.md) | [Test] Only Run MLA model when user explicitly set for batch invariance | 2026-03-20 |  | mla |
| [#37725](../sources/prs/vllm/PR-37725.md) | [Bugfix] Preserve CUDA arch suffix (a/f) for SM12x — fixes NVFP4 NaN on desktop Blackwell | 2026-03-20 |  | fp4, nvfp4 |
| [#37502](../sources/prs/vllm/PR-37502.md) | [Bugfix] Fix marlin nvfp4 rescaling | 2026-03-19 |  | fp4, nvfp4, quantization |
| [#37503](../sources/prs/vllm/PR-37503.md) | [4/n] Migrate FP4/W4A8 CUTLASS kernels to torch stable ABI | 2026-03-19 | epilogue-fusion, kernel-fusion | epilogue-fusion, fp4, kernel-fusion |
| [#37519](../sources/prs/vllm/PR-37519.md) | refactor: abstract deepgemm support into platform | 2026-03-19 |  | gemm |
| [#37536](../sources/prs/vllm/PR-37536.md) | Fix KV Offloading + MLA AssertionError by using num_kv_heads=1 in cpu… | 2026-03-19 |  | mla |
| [#37539](../sources/prs/vllm/PR-37539.md) | [Performance] Remove unnecessary zero-fill of MLA decode output tensor in Aiter backend | 2026-03-19 |  | attention, decode, mla |
| [#37547](../sources/prs/vllm/PR-37547.md) | [Bugfix][ROCm] Fix lru_cache on paged_mqa_logits_module | 2026-03-19 |  | attention, mla |
| [#37565](../sources/prs/vllm/PR-37565.md) | [Bugfix] Disable --calculate-kv-scales for hybrid GDN/Mamba+Attention… | 2026-03-19 |  | attention |
| [#37605](../sources/prs/vllm/PR-37605.md) | [Bugfix] Disable monolithic TRTLLM MoE for Renormalize routing (#37591) | 2026-03-19 | kernel-fusion | fp8, kernel-fusion, moe |
| [#37606](../sources/prs/vllm/PR-37606.md) | [ROCm][Bugfix] fix cache block size mismatch for aiter unified attention | 2026-03-19 |  | attention |
| [#37364](../sources/prs/vllm/PR-37364.md) | [Model Runner V2] fix draft attention metadata generation | 2026-03-18 |  | attention, decode |
| [#37373](../sources/prs/vllm/PR-37373.md) | [torch.compile] Refactor Attention Quant Fusion Pass and Remove Boilerplate | 2026-03-18 | kernel-fusion | attention, kernel-fusion |
| [#37421](../sources/prs/vllm/PR-37421.md) | [Perf][Kernel] Persistent TopK scheduler: unified CUDAGraph-safe kernel with dynamic per-row dispatch - DeepSeek-V3.2 DSA decode | 2026-03-18 | persistent-kernel | attention, decode, mla |
| [#37465](../sources/prs/vllm/PR-37465.md) | [Bugfix] Remove assertion for NVFP4 scale dynamic range | 2026-03-18 |  | fp4, nvfp4, quantization |
| [#37475](../sources/prs/vllm/PR-37475.md) | [BugFix] Allow qk_nope_head_dim=192 in FlashInfer MLA backend checks | 2026-03-18 |  | attention, mla |
| [#37252](../sources/prs/vllm/PR-37252.md) | [Perf] Set Flashinfer sparse MLA as default backend for FP8 kv cache | 2026-03-17 |  | attention, fp8, mla |
| [#37303](../sources/prs/vllm/PR-37303.md) | [Attention] Support distinguishing between short extends and decodes | 2026-03-17 |  | attention, decode, prefill |
| [#37320](../sources/prs/vllm/PR-37320.md) | [Kernel] Add non-gated support for NVFP4 CUTLASS MoE | 2026-03-17 | kernel-fusion | fp4, kernel-fusion, moe |
| [#37322](../sources/prs/vllm/PR-37322.md) | [Bugfix] Fix EP weight filter breaking EPLB and NVFP4 accuracy | 2026-03-17 |  | fp4, nvfp4 |
| [#37143](../sources/prs/vllm/PR-37143.md) | [XPU] support MLA model on Intel GPU | 2026-03-16 |  | attention, fp8, mla |
| [#37199](../sources/prs/vllm/PR-37199.md) | [Misc] Add `float16` to `CacheDType` | 2026-03-16 |  | attention, mla |
| [#37205](../sources/prs/vllm/PR-37205.md) | [Kernel] Add gpt-oss Router GEMM kernel | 2026-03-16 | kernel-fusion | gemm, kernel-fusion, moe |
| [#37214](../sources/prs/vllm/PR-37214.md) | Fix minimax m2.5 nvfp4 kv scales weight loading | 2026-03-16 |  | fp4, nvfp4 |
| [#37217](../sources/prs/vllm/PR-37217.md) | [MoE/EPLB] Fix FlashInfer nvfp4 experts + EPLB correctness | 2026-03-16 | kernel-fusion | fp4, kernel-fusion, moe |
| [#37228](../sources/prs/vllm/PR-37228.md) | [ROCM][Bugfix] Use correct stride in cp_mha_gather_cache_kernel for hybrid model (#37228) | 2026-03-16 |  | attention |
| [#37233](../sources/prs/vllm/PR-37233.md) | [UX] Add flashinfer-cubin as CUDA default dep | 2026-03-16 |  | gemm |
| [#37090](../sources/prs/vllm/PR-37090.md) | [Bugfix] Disable cross-layer KV cache for MLA attention backends | 2026-03-15 |  | attention, mla |
| [#37115](../sources/prs/vllm/PR-37115.md) | [Benchmark] Improvements to attention benchmark script | 2026-03-15 |  | attention, decode, mla |
| [#37128](../sources/prs/vllm/PR-37128.md) | [MoE Refactor] Mxfp4 oracle rebased | 2026-03-15 | kernel-fusion | fp4, kernel-fusion, moe |
| [#37054](../sources/prs/vllm/PR-37054.md) | [Bugfix] Fix KV scales inconsistency in fp8 MLA & FlashInfer kv_cache_dtype "auto" leading to gibberish | 2026-03-14 |  | attention, fp8, mla |
| [#36982](../sources/prs/vllm/PR-36982.md) | [MTP][Sparse MLA] Take advantage of native MTP support in indexer when possible | 2026-03-13 |  | attention, mla |
| [#36845](../sources/prs/vllm/PR-36845.md) | [ROCm] Fix KV copy methods and auto-select attention backend for ROCm | 2026-03-12 |  | attention, decode |
| [#36846](../sources/prs/vllm/PR-36846.md) | [ROCm] Validate block_size for explicitly selected attention backends | 2026-03-12 |  | attention |
| [#36847](../sources/prs/vllm/PR-36847.md) | [Feat][Spec Decode] DFlash | 2026-03-12 |  | attention, decode |
| [#36876](../sources/prs/vllm/PR-36876.md) | [Bugfix] Fix FlashInfer GDN warmup ValueError on SM90 GPUs | 2026-03-12 |  | gemm |
| [#36931](../sources/prs/vllm/PR-36931.md) | [Feat][Bugfix] Enable additional dimension for Flashinfer MLA and fix routing dtype | 2026-03-12 |  | attention, mla |
| [#36725](../sources/prs/vllm/PR-36725.md) | [Bug][MoE] Fix TRTLLM NVFP4 Routing Kernel Precision | 2026-03-11 | kernel-fusion | fp4, kernel-fusion, moe |
| [#36728](../sources/prs/vllm/PR-36728.md) | [Bug][MoE] Strengthen _supports_current_device() checks in the TRTLLM FP8, NVFP4, and FlashInfer CuteDSL MoE experts | 2026-03-11 | kernel-fusion | fp4, fp8, kernel-fusion |
| [#36768](../sources/prs/vllm/PR-36768.md) | Update Flashinfer to 0.6.6 | 2026-03-11 |  | gemm |
| [#36574](../sources/prs/vllm/PR-36574.md) | [ROCm] Utilize persistent MLA kernel from AITER | 2026-03-10 | persistent-kernel | attention, mla, persistent-kernel |
| [#36599](../sources/prs/vllm/PR-36599.md) | [Bugfix] Warm up Triton autotuner for GDN layers during V1 profiling | 2026-03-10 |  | gemm |
| [#36647](../sources/prs/vllm/PR-36647.md) | [GDN] add a config for gdn kernel selection | 2026-03-10 |  | gemm |
| [#36674](../sources/prs/vllm/PR-36674.md) | [Bug] Fix FlashInfer MNNVL socket collisions under concurrent vLLM jobs | 2026-03-10 |  | gemm |
| [#36681](../sources/prs/vllm/PR-36681.md) | [ROCm][Perf] Allow MTP lens > 1 in Sparse MLA | 2026-03-10 |  | decode, mla |
| [#36702](../sources/prs/vllm/PR-36702.md) | [ROCm] Attention selector reordering | 2026-03-10 |  | attention, decode, prefill |
| [#36723](../sources/prs/vllm/PR-36723.md) | [DSV3.2][MTP] Optimize Indexer MTP handling | 2026-03-10 |  | attention, mla |
| [#23696](../sources/prs/vllm/PR-23696.md) | [Kernel][tcgen05] nvfp4 fused tcgen05 moe | 2025-09-11 | kernel-fusion, fine-grained-quantization | tcgen05, nvfp4, moe |
| [#22738](../sources/prs/vllm/PR-22738.md) | [Bugfix] Fix default enable for CUTLASS MLA on SM100 | 2025-08-13 |  | tcgen05, mla, gemm |
| [#19566](../sources/prs/vllm/PR-19566.md) | [Perf] Further tunings for SM100 FP8 CUTLASS kernel | 2025-06-15 | tile-scheduling | tcgen05, fp8, gemm |
| [#16032](../sources/prs/vllm/PR-16032.md) | [NVIDIA] Support Cutlass MLA for Blackwell GPUs | 2025-04-27 | warp-specialization, persistent-kernel | tcgen05, mla, moe |
| [#13798](../sources/prs/vllm/PR-13798.md) | add tcgen05 support for tcgen05 fp8 gemm | 2025-03-04 | tile-scheduling | tcgen05, fp8, gemm |
| [#13571](../sources/prs/vllm/PR-13571.md) | [NVIDIA] Support nvfp4 tcgen05 gemm | 2025-02-22 | fine-grained-quantization | tcgen05, nvfp4, fp4 |

