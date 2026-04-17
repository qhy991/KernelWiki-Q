# Blackwell Kernel Wiki — 大规模扩展计划 (Phase 2)

## 现状

Phase 1 建立了知识库骨架（91 files），但PR覆盖严重不足：
- CUTLASS: 7/~41+ Blackwell PRs
- SGLang: 5/~194+ sm100 PRs (466 提到blackwell)
- vLLM: 6/~254+ sm100 PRs (574 提到blackwell, 555 nvfp4)
- FlashInfer: 6/~300+ sm100 PRs (247 提到blackwell)
- PyTorch: 7/~141+ sm100 PRs (159 提到blackwell)
- 比赛: 仅7个概述页，无具体提交方案

注意：上述数字包含大量仅mention关键词的PR（如CI/doc/依赖更新），实际kernel相关PR需要过滤。

## 目标

从2025-01-01至今，完整覆盖每个仓库中**与Blackwell/Hopper kernel编程直接相关**的PR。同时收录比赛的具体提交方案和排名。

## 过滤标准

PR必须满足以下至少一条才收录：
1. **新增/修改kernel代码**（CUDA C++, CuTe DSL, Triton, PTX, TileLang）
2. **kernel性能优化**（tile size tuning, schedule改进, 新的pipeline策略）
3. **新增硬件特性支持**（tcgen05, TMEM, CLC, 2-SM, NVFP4, FP8 block scale）
4. **kernel算法创新**（新的attention variant, MoE routing, sparse pattern）
5. **重要bug fix影响kernel正确性**（sync issues, precision bugs, launch bounds）

不收录的PR类型：
- 纯CI/CD改动
- 文档/README更新（除非包含kernel技术细节）
- 依赖版本bump
- 代码格式化/lint
- 纯Python binding（无kernel逻辑改动）

## 搜索策略

### NVIDIA/cutlass（预计收录 30-50 PRs）

GitHub API显示 ~41 PRs提到"blackwell"。CUTLASS是Blackwell kernel的核心实现。

**搜索关键词**（每个单独搜索，去重合并）：
```
blackwell, sm100, sm_100, sm_100a, tcgen05, tmem, tensor_memory,
nvfp4, fp4, mxfp4, block_scale, 2sm, cta_group, clc,
cluster_launch, umma, persistent, warp_special, fmha, mla,
epilogue, tile_scheduler, grouped_gemm, sub_byte
```

**按时间段分批搜索**（避免API限制）：
- 2025-01 ~ 2025-03（早期Blackwell支持）
- 2025-04 ~ 2025-06（CUTLASS 4.0发布期）
- 2025-07 ~ 2025-09（SM100 attention kernel）
- 2025-10 ~ 2025-12（sub-byte GEMM, NVFP4）
- 2026-01 ~ 2026-04（CuTe-DSL, bugfix）

**重点关注**：
- examples/cute/tutorial/blackwell/ 相关PR
- SM100 FMHA forward/backward
- Grouped GEMM / MoE support
- CuTe-DSL SM100 atoms
- Block-scale GEMM (NVFP4, MXFP4)
- PersistentTileSchedulerSm100
- 2-CTA cooperative MMA

### sgl-project/sglang（预计收录 20-30 PRs）

SGLang有大量Blackwell集成工作。~194 PRs提到sm100。

**搜索关键词**：
```
blackwell, sm100, cutlass, deepgemm, flashmla, fp8, nvfp4,
mla, flashinfer, triton, attention, moe, sparse, gated_delta,
sgl-kernel, trtllm, decode, prefill, quantiz
```

**重点关注**：
- DeepGEMM集成（FP8 GEMM, grouped GEMM）
- FlashMLA集成（dense/sparse MLA decode）
- CUTLASS MLA backend
- FP8 blockwise quantization
- NSA (Native Sparse Attention) 支持
- GatedDeltaNet 支持
- Blackwell-specific kernel选择逻辑

### vllm-project/vllm（预计收录 25-40 PRs）

vLLM有最多的Blackwell适配PR。~254 PRs提到sm100。

**搜索关键词**：
```
blackwell, sm100, cutlass, fp8, nvfp4, mxfp4, B200,
mla, deepseek, flashmla, attention, moe, fused_moe,
sparse_attention, gated_delta, quantiz, block_scale,
triton, flashinfer, grouped_gemm, decode, prefill
```

**重点关注**：
- CUTLASS FP8 GEMM on SM100
- NVFP4/MXFP4 GEMM和fused MoE
- CUTLASS MLA for Blackwell
- DeepSeek V3.2 sparse attention支持
- GatedDeltaNet/Qwen3-Next支持
- FP8 block-scale quantization kernels
- Attention backend selection for SM100

### flashinfer-ai/flashinfer（预计收录 25-35 PRs）

FlashInfer是Blackwell attention kernel的核心库。~300 PRs提到sm100。

**搜索关键词**：
```
blackwell, sm100, sm_100, tcgen05, tmem, cutlass, cute_dsl,
fmha, mla, attention, moe, fp8, fp4, nvfp4, block_scale,
trtllm, decode, prefill, sparse, gated_delta, splitk,
allreduce, head_dim, gemm, gemv
```

**重点关注**：
- CuTe-DSL FMHA kernels for SM100
- SM100 MLA kernels (forward/backward)
- FP4/FP8 fused MoE on Blackwell
- FlashInfer-Bench kernel definitions
- TGV GEMM和alternative backends
- head_dim variants for SM100
- GEMM+allreduce fusion

### pytorch/pytorch（预计收录 15-25 PRs）

PyTorch的Blackwell支持更侧重build/runtime层面，但也有kernel相关改动。

**搜索关键词**：
```
blackwell, sm100, sm_100, sm_100a, cuda_13, nvfp4,
B200, inductor, triton, cutlass, flash_attention,
vec128, launch_bounds, sm120, compute_10
```

**重点关注**：
- TorchInductor SM100 code generation
- Triton kernel templates for Blackwell
- CUTLASS integration for SM100
- NVFP4 support in torch
- Flash attention Blackwell path
- Launch bounds fixes for SM100/SM120
- 新的vectorized ops (vec128)

## 比赛数据扩展

### GPU Mode NVFP4 Blackwell Hackathon

**当前**：4个problem概述页
**需要新增**：
1. **排名数据**：每个problem的完整leaderboard（top 10+排名、用户名、成绩）
2. **获奖方案分析**：
   - Problem 1 (GEMV): Top 3方案的具体实现策略和代码模式
   - Problem 2 (GEMM): Simon/yue/currybab的kernel设计
   - Problem 3 (Gated Dual GEMM): 前几名的fusion策略
   - Problem 4 (Grouped GEMM): 前几名的CLC/tile策略
3. **参赛者博客和代码**：
   - 搜索GitHub repos: `nvfp4 hackathon`, `gpu-mode blackwell`
   - 搜索博客: GPU Mode Discord讨论摘要
4. **Reward hack分析**：已有概述，扩展技术细节

**搜索方法**：
```
# GitHub repos
curl "https://api.github.com/search/repositories?q=nvfp4+hackathon"
curl "https://api.github.com/search/repositories?q=gpu-mode+blackwell+kernel"

# GPU Mode leaderboard API (if available)
# https://www.gpumode.com/leaderboard/595 (GEMV)
# https://www.gpumode.com/leaderboard/597 (GEMM)

# Participant blogs
WebSearch: "blackwell nvfp4 hackathon solution"
WebSearch: "gpu mode hackathon blackwell winner"
WebSearch: "nvfp4 kernel optimization blog"
```

### FlashInfer AI Kernel Generation Contest (MLSys 2026)

**当前**：3个track概述页
**需要新增**：
1. **提交方案仓库**：搜索所有flashinfer-bench-starter-kit的forks（17个fork）
2. **每个fork的solution分析**：
   - Track A (Fused MoE): 参赛者的kernel实现
   - Track B (Sparse Attention): 参赛者的indexer+attention kernel
   - Track C (GatedDeltaNet): 参赛者的prefill/decode kernel
3. **Agent baseline分析**：
   - flashinfer-ai/mlsys26-agent-baseline 的evolve/iterative agent策略
   - K-Search论文的co-evolving world model方法
4. **FlashInfer-Bench leaderboard数据**：
   - bench.flashinfer.ai 的AI-generated kernel排名
   - 每个model (Gemini, GPT-5, Claude) 的per-kernel性能

**搜索方法**：
```
# Contest forks
curl "https://api.github.com/repos/flashinfer-ai/flashinfer-bench-starter-kit/forks?per_page=100"

# Contest submissions tagged on GitHub
curl "https://api.github.com/search/repositories?q=flashinfer+mlsys+2026"
curl "https://api.github.com/search/repositories?q=flashinfer-bench"

# Leaderboard
WebFetch: https://bench.flashinfer.ai/
WebSearch: "flashinfer mlsys 2026 contest results"
WebSearch: "flashinfer bench leaderboard kernel"
```

## 执行策略

### 并行度

每个仓库拆成 2-3 个time-range sub-agent：
- Agent 1: 2025-01 ~ 2025-06（每个repo）
- Agent 2: 2025-07 ~ 2025-12（每个repo）
- Agent 3: 2026-01 ~ 2026-04（每个repo）

总共：5 repos × 3 periods = 15 个 PR收集 sub-agents
加上：2 个比赛数据 sub-agents
= **17 个并行 sub-agents**

### 每个sub-agent的工作流

```
1. 用多个关键词搜索GitHub API，收集所有匹配PR的number和title
2. 去重合并
3. 对每个PR：
   a. 获取PR描述（gh api repos/{repo}/pulls/{number}）
   b. 根据过滤标准判断是否收录
   c. 如果收录：提取metadata，创建sources/prs/{repo}/PR-{N}.md
4. 使用严格的controlled vocabulary（从data/tags.yaml）
5. 确保frontmatter完整且validate.py通过
```

### 质量保证

1. 每个sub-agent完成后立即运行 `python3 scripts/validate.py`
2. 不合格的文件立即修复
3. 最终运行 `python3 scripts/generate-indices.py` 重建所有索引
4. 运行link integrity check

### 预期结果

| 来源 | 当前 | 目标 | 新增 |
|------|------|------|------|
| CUTLASS PRs | 7 | 30-50 | 23-43 |
| SGLang PRs | 5 | 20-30 | 15-25 |
| vLLM PRs | 6 | 25-40 | 19-34 |
| FlashInfer PRs | 6 | 25-35 | 19-29 |
| PyTorch PRs | 7 | 15-25 | 8-18 |
| GPU Mode 比赛 | 4 | 15-20 | 11-16 |
| FlashInfer 比赛 | 3 | 10-15 | 7-12 |
| Blogs | 10 | 20-25 | 10-15 |
| Docs | 6 | 10-12 | 4-6 |
| **Total sources** | **54** | **180-260** | **~120-200 new** |

加上现有37 wiki pages + 新增wiki pages → **总计 250-350 files**

## 额外博客和文档待收录

### 博客（新增 10-15 篇）
- Simon's NVFP4 GEMV Blog (Part 1 + Part 2)
- TFLOPS Gap: FP4 MoE Kernel Engineering on Blackwell (HuggingFace)
- NVFP4 Format Details (Harold Benoit)
- JAX Pallas Blackwell Matmul tutorial
- Tilus ASPLOS paper summary
- Blackwell Microbenchmarking papers (arxiv 2512.02189, 2507.10789)
- vLLM DeepSeek V3.2 Sparse Attention blog
- Qwen3-Next architecture blog (NVIDIA, Alibaba)
- K-Search automated kernel generation (arxiv 2602.19128)
- GPU Mode "Anatomy of a Reward Hack" full analysis

### 文档（新增 4-6 篇）
- CUTLASS Changelog (SM100 entries)
- CUTLASS CLC documentation
- Blackwell Compatibility Guide
- NVIDIA cuTile Python DSL reference
- Tilus documentation
