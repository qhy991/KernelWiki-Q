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
126 PRs

| PR | Title | Date | Techniques | Tags |
|-----|-------|------|------------|------|
| [#2387](../sources/prs/flashinfer/PR-2387.md) | A Blackwell-optimized version of selective_state_update (decode) | 2026-01-22 | warp-specialization, pipeline-stages, double-buffering | tcgen05, decode |
| [#1850](../sources/prs/flashinfer/PR-1850.md) | Add head_dim=64 for tcgen05 tcgen05 flash-attention implementation | 2025-10-03 | warp-specialization, persistent-kernel, pipeline-stages | tcgen05, flash-attention, attention |
| [#1695](../sources/prs/flashinfer/PR-1695.md) | [cute_dsl] add gemm + all reduce (two_shot) | 2025-09-18 | kernel-fusion, tma-multicast | cute-dsl, gemm, kernel-fusion |
| [#1681](../sources/prs/flashinfer/PR-1681.md) | perf: improve attention of tcgen05 flash-attention | 2025-09-16 | warp-specialization, persistent-kernel | tcgen05, flash-attention, attention |
| [#1668](../sources/prs/flashinfer/PR-1668.md) | TGV GEMM as a BF16 backend alternative to cuBLAS | 2025-09-14 | persistent-kernel, tile-scheduling | gemm, fp8, tcgen05 |
| [#1548](../sources/prs/flashinfer/PR-1548.md) | perf: Enable SplitK and fix tile-scheduling for moe fp4 fused moe | 2025-09-05 | tile-scheduling, fine-grained-quantization | moe, fp4, gemm |
| [#1281](../sources/prs/flashinfer/PR-1281.md) | Unify groupwise fp8 GEMM test | 2025-07-18 |  | fp8, gemm |
| [#1284](../sources/prs/flashinfer/PR-1284.md) | Convert scale_factor from scalar to Tensor in trt_allreduce_fusion | 2025-07-18 | kernel-fusion | kernel-fusion |
| [#1286](../sources/prs/flashinfer/PR-1286.md) | fix multiCtasKvScratchPtr misalignment issue (new one) | 2025-07-18 |  | flash-attention |
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
| [#1164](../sources/prs/flashinfer/PR-1164.md) | feat: enable and update all-reduce fused quantization | 2025-06-22 | kernel-fusion | kernel-fusion, moe, quantization |
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
71 PRs

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
| [#162764](../sources/prs/pytorch/PR-162764.md) | fix cpp extension distributed warning spew | 2025-09-11 |  | python, cuda-cpp |
| [#162455](../sources/prs/pytorch/PR-162455.md) | [CD] CUDA 13 specific followup changes. Remove sm50-70 From CUDA 12.6 and CUDA 12.8 builds | 2025-09-09 |  | python |
| [#158646](../sources/prs/pytorch/PR-158646.md) | [cherry-pick][inductor][triton] Update HAS_WARP_SPEC to check triton.Config params. Update Triton Hash to top of release/3.4.x stack | 2025-07-18 |  | gemm |
| [#158301](../sources/prs/pytorch/PR-158301.md) | Add warning about removed sm50 and sm60 arches | 2025-07-15 |  | python |
| [#158237](../sources/prs/pytorch/PR-158237.md) | [MPS] Switch Cholesky  decomp to column wise | 2025-07-14 |  | gemm |
| [#157752](../sources/prs/pytorch/PR-157752.md) | [release] Triton pin update to 3.4 | 2025-07-08 |  | gemm |
| [#157241](../sources/prs/pytorch/PR-157241.md) | [user triton] AOT inductor support for device-side TMA | 2025-06-29 |  | tma |
| [#156932](../sources/prs/pytorch/PR-156932.md) | Fix macOS build with `USE_MPS=OFF` | 2025-06-26 |  | gemm |
| [#153641](../sources/prs/pytorch/PR-153641.md) | [FlexAttention] explicilty create grad_q w/ strides | 2025-05-15 |  | attention |
| [#153104](../sources/prs/pytorch/PR-153104.md) | [FlexAttention] Remove Old Constraint on lastdim strides | 2025-05-07 |  | attention |
| [#152967](../sources/prs/pytorch/PR-152967.md) | [ATen][CUDA] Optimize 128 bit vectorization | 2025-05-06 |  | gemm |
| [#152774](../sources/prs/pytorch/PR-152774.md) | [dynamo][super variable] Fix bug to use correct source | 2025-05-04 |  | gemm |
| [#150676](../sources/prs/pytorch/PR-150676.md) | [CUDA][avgpool2d] Fix backward launch bounds again for `sm100`, `sm120` | 2025-04-04 |  | gemm |
| [#150705](../sources/prs/pytorch/PR-150705.md) | [CUDA] Only use vec128 if CUDA version is newer than 12.8 | 2025-04-04 | vectorized-loads | cuda-cpp |
| [#150640](../sources/prs/pytorch/PR-150640.md) | [CUDA][avgpool2d] Fix backward launch bounds again for sm100, sm120 | 2025-04-03 |  | cuda-cpp |
| [#149993](../sources/prs/pytorch/PR-149993.md) | [inductor][triton 3.3] Fix cpp_wrapper w/ TMA in triton 3.3 | 2025-03-26 |  | tma |
| [#149644](../sources/prs/pytorch/PR-149644.md) | op should NOT be static in aoti_torch_call_dispatcher | 2025-03-20 |  | gemm |
| [#149386](../sources/prs/pytorch/PR-149386.md) | Add AOTI shim for _weight_int4pack_mm_cpu_tensor (#149031) | 2025-03-18 |  | quantization |
| [#149125](../sources/prs/pytorch/PR-149125.md) | Remove runtime dependency on packaging | 2025-03-13 |  | gemm |
| [#149059](../sources/prs/pytorch/PR-149059.md) | [inductor] Fix profiler tests with latest Triton | 2025-03-12 |  | gemm |
| [#144248](../sources/prs/pytorch/PR-144248.md) | [inductor][cpu] Fix bmm b_index for dynamic expressions in inductor autotuner | 2025-01-06 |  | gemm |

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

