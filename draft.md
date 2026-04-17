# Phase 3 Draft — Data Depth / 完整代码补全

> Status: **DRAFT**, not yet a RLCR plan. Discuss with Codex before promoting to `plan-phase3.md` via `/humanize:gen-plan`.

## 1. 问题陈述

Phase 2 结束后仓库有 545 files，但每个 file 都是**一张"索引卡片"**，不是真实代码：

| 页类型 | 平均行数 | 真实代码占比 | 典型缺陷 |
|---|---|---|---|
| `sources/prs/*/PR-*.md` | ~70 行 | 10–30 行 snippet | 只有 summary + "Key Code" 一小段，diff 全部外链到 GitHub |
| `sources/contests/*/problem-*.md` | ~200 行 | 0 行 | `submissions:` 只记录"排名 + 作者 + 一句话技术总结"，**完全没有**提交的 kernel 源码 |
| `sources/blogs/*.md` | ~100 行 | 20–40 行 | blog 里大段代码（FA4 blog 有完整 softmax+MMA 循环）只摘录关键几行 |
| `wiki/kernels/*.md` | ~200 行 | 40–80 行 | 用伪代码或片段讲解，没有一份端到端 compilable kernel |
| `wiki/techniques/*.md` | ~240 行 | 50–100 行 | 同上 |

**后果**：LLM agent 问"NVFP4 kernel 怎么写"，读 `kernel-nvfp4-gemm` 得到的是"它用 tcgen05 + UE8M0 block scale"，还是得跳到原 PR/blog 才看得到代码。**wiki 本身没有落下真正的知识。**

## 2. 目标（Definition of Done）

Phase 3 完成后，下列问题**不开外部链接**就能直接从本仓库解答，且能拿到**完整可编译/可读的 CUDA/PTX/CuTe 代码**：

1. "NVFP4 batched GEMV 怎么写（B200，PTX 风格）" → 能拿到 Simon / yue / Amandeep 三份 hackathon 冠军 kernel 完整源码 + 作者写的 approach 笔记
2. "warp specialization 怎么分工（producer/consumer/epilogue）" → 有一份 ~300 行、含 mbarrier phase、TMEM buffer 双缓冲、TMA load role 切分的端到端示例
3. "DeepGEMM FP8 block scale 怎么做 Nc=128 CUDA-core promotion" → 有对应 commit 的完整 .cu 文件
4. "CUTLASS SM100 怎么配 PersistentScheduler+CLC 的 tile 调度" → 有 PR-2161 的完整 diff（含改动到的头文件内容）
5. "FA4 软件 exp 近似公式和循环结构" → Tri Dao blog 里所有代码块都抓进 `sources/blogs/flash-attention-4/code/`

不是"把 GitHub 镜像过来"，是**精选 + 完整**：include 列表上的 PR/提交，其 kernel 相关文件全文落地到本仓库。

## 3. 数据来源盘点与量级估算

### 3.1 PR diffs（460 个 included PR）

- 工具：`gh pr diff <N> --repo <owner/repo>` 能拿完整 patch
- 粗估每个 PR 改动：中位数 ~30KB，长尾到 500KB+
- 清洗策略（把非 kernel 噪声砍掉）：
  - **保留**：`*.cu / *.cuh / *.cpp / *.h / *.hpp`，位于 `include/cutlass/`、`csrc/`、`python/vllm/_C/`、`csrc/kernels/` 等 kernel 目录
  - **保留**：PTX 内联、CuTe DSL 源、`.cutlass_configs.json`
  - **丢弃**：测试 (`tests/`、`*_test.cu`)、Python 胶水（非 DSL）、docs、CI、release notes
- 量级估算：460 × 平均 40KB（清洗后）≈ **18MB**
- 锁版本：每条记 `merge_sha`（已经有字段），diff 标注"基于 SHA=xxx"

### 3.2 Contest 提交 kernel 源码

- GPU Mode NVFP4 hackathon: 4 题 × 前 3 名 = **12 份 kernel**
  - 来源：GPU Mode Discord 公告 / 作者个人仓库 / 已经在 `sources/blogs/` 的参赛者博客
  - Simon 的 problem-1 解题博客里有完整 PTX kernel（已在 `blog-simon-nvfp4-gemv`，但只抓了片段）
- FlashInfer MLSys 2026: 3 track × 前 3 名 = **9 份**（若组委会公布提交，否则降级为"track spec + 预期实现思路"）
- 单份 kernel 100–800 行，总量 ~200KB

### 3.3 Blog 代码块

- 当前 20 篇 blog，有代码的估 12 篇
- 手抓每篇 blog 里的 code fences，按章节编号存成 `sources/blogs/{slug}/code/step-{n}-{topic}.{cu,ptx,py}`
- 每段代码附 2–3 行 caption（对应原 blog 的哪个小节）
- 量级 ~150KB

### 3.4 Wiki 页面深化

- 针对 **12 个重点页**：
  - kernels：`flash-attention-4, nvfp4-gemm, nvfp4-gemv, deepgemm, gated-dual-gemm, fused-moe, flashmla, gated-delta-net`
  - techniques：`warp-specialization, epilogue-fusion, persistent-kernels, ping-pong-scheduling`
- 每页挂钩一份 `wiki/kernels/<slug>/full/<kernel>.cu`（完整实现，不是 snippet）
- wiki md 主文件保留讲解 + 指向 `full/` 的链接 + 关键片段带行级注释
- 量级 ~300KB

### 3.5 总量级估算

| 来源 | 体积 | 备注 |
|---|---|---|
| PR diffs | ~18 MB | 清洗后 |
| Contest kernel | ~0.2 MB | 12–21 份 |
| Blog 代码 | ~0.15 MB | |
| Wiki 深化 | ~0.3 MB | |
| **总计** | **~19 MB** 增量 | 目前仓库 ~5MB，Phase 3 后 ~24MB，仍在 `~/.claude/skills/` 可接受范围；不需要 Git LFS |

## 4. 组织与 schema 变更

### 4.1 目录结构

```
sources/prs/{repo}/
  PR-2161.md                          # 既有摘要（不动）
  PR-2161/                            # 新增同名目录
    diff.patch                        # 清洗后 diff（或 diff.md 用代码块包裹）
    key-files/
      include/cutlass/detail/collective/mixed_input_utils.hpp
      include/cute/atom/copy_traits_sm100.hpp
    NOTES.md                          # 锁定 SHA、清洗规则、原始 diff 字节数

sources/contests/gpu-mode-nvfp4/
  problem-1-gemv.md                   # 既有描述（不动）
  problem-1-gemv/
    submissions/
      rank-1-simon/
        kernel.cu                     # 完整源码
        approach.md                   # 作者方法论（从 blog/Discord 抄录）
        bench.txt                     # 性能记录
      rank-2-yue/...
      rank-3-amandeep/...

sources/blogs/flash-attention-4.md    # 既有摘要
sources/blogs/flash-attention-4/
  code/
    01-mainloop.cu
    02-softmax-rescale.cu
    03-epilogue.cu
  README.md                           # 每段代码对应 blog 哪个小节

wiki/kernels/nvfp4-gemm.md            # 主讲解页（既有）
wiki/kernels/nvfp4-gemm/
  full/
    nvfp4_gemm_sm100.cu              # 完整 kernel
    nvfp4_gemm_sm100.cuh             # 公共头
  variants/
    naive.cu                          # 17% TFLOPS 基线
    with-swizzle.cu                   # 46%
    with-pipelining.cu                # 62%
    warp-spec.cu                      # 80%
    full-clc.cu                       # 98%
  BENCH.md                            # 各版本 B200 实测数字
```

### 4.2 Schema 扩展（`data/schemas.yaml`）

新增字段：

```yaml
source-pr:
  optional:
    diff_captured: bool                # 是否已落地 diff
    diff_path: string                  # 相对路径
    diff_size_bytes: int
    key_files: [list of paths]         # 清洗后保留的文件

source-contest.submissions[*]:
  optional:
    code_path: string                  # 指向 submissions/rank-N-author/kernel.cu
    code_unavailable: string           # 解释为什么没代码（Discord-only 等）

source-blog:
  optional:
    code_dir: string                   # blogs/<slug>/code/
    code_files: [list of paths]

wiki-kernel / wiki-technique:
  optional:
    full_code_dir: string              # wiki/kernels/<slug>/full/
    variants_dir: string               # wiki/kernels/<slug>/variants/
```

### 4.3 Validator 规则

- "**核心 PR**" 集合（TBD，约 60 个；从 wiki/*.md 的 `sources:` 反向推导）必须有 `diff_captured: true`
- 所有 contest 的前三名 submissions 必须有 `code_path` 或显式 `code_unavailable`
- 12 个 wiki 重点页必须有 `full_code_dir`
- 合成代码（`.cu` 非直接来自某个 PR/blog）必须在文件头有 `// provenance: derived from <sources>` 注释

### 4.4 Query 工具扩展

- `scripts/query.py`：新 filter `--has-code`（只返回有完整代码的页）
- `scripts/get_page.py`：新 flag `--include-code`（打印主 md + `full/` 或 `code/` 下所有文件）
- `scripts/grep_wiki.py`：scope 扩到 `.cu/.cuh/.ptx/.py`（目前只搜 markdown）

## 5. 执行 stage（4 个阶段，粗估 ~8–10 RLCR rounds）

### Stage A · 基础设施（1 round）
- schema 扩展，validator 规则，新目录规范
- `scripts/fetch_pr_diff.py`：给定 PR 编号批量 `gh pr diff`，按路径白名单清洗，落地
- `scripts/extract_blog_code.py`：从 blog .md 里的 code fence 拆分出独立源文件

### Stage B · PR diff 全量抓取（2 rounds）
- 先锁定 60 个"核心 PR"（techniques/kernels 页 `sources:` 里引用的 PR；NVFP4/tcgen05/TMEM/CLC 实现 PR；contest 相关 PR）
- 先抓这 60 个，validator 跑通
- 再扩到全部 460 个

### Stage C · Contest + Blog 代码落地（2 rounds）
- 12 份 hackathon kernel 源码：作者公开仓库 / blog 抓
- FlashInfer 9 份 track：若无公开提交则记 `code_unavailable` 并给出"如何近似重建"的 notes
- Blog 代码块拆成独立文件

### Stage D · Wiki 重点页深化（3 rounds）
- 每 round 聚焦 4 页
- 为每页写 full/ 完整 kernel（可基于 PR diff 或 blog 代码合成，附 provenance）
- 每页 README 里带 naive→optimized 的 variants 进度

### Stage E · 综合验证 + Codex 审核（1 round）
- `validate.py` 0 errors
- `query.py --has-code` 覆盖 Definition of Done 里的 5 个问题
- Codex 审核是否真的"不开外链能答 5 大问题"

## 6. 开放问题 / 需要用户 & Codex 定夺

1. **Scope**：要全抓 460 PR 还是先锁 60 个核心？全抓更完整，但维护成本高；60 个能覆盖 80% LLM agent 查询，风险小
2. **版权 / License**：
   - PR diff 属于 Apache 2.0 / MIT 派生——按照各仓库 license 保留 copyright header，在每个 PR-N/NOTES.md 注明来源
   - Contest 提交：是否需要作者授权？目前设想是作者**已公开**在 Discord/blog/个人仓库的才收录，私有提交不动
3. **仓库拆分**：要不要拆成 `KernelWiki`（索引 + wiki，5MB）和 `KernelWiki-Code`（代码归档，20MB）两个 repo？
   - 优点：skill 轻量
   - 缺点：双仓库 clone 麻烦；get_page.py 要支持跨 repo fetch
   - 我的倾向：**不拆**，20MB 还能接受
4. **Variants 的"重建"政策**：wiki/kernels/{slug}/variants/ 里的 naive→optimized 各版本，如果没有现成 PR 能完整覆盖所有版本，是否允许"基于 blog 讲解 + PR 片段"合成？
   - 合成代码必须标 `provenance: derived` 并列来源
5. **过期管理**：上游 PR 如果 reverted，本仓库 diff 怎么办？建议加 `scripts/verify_sha.py` 定期跑，标红失效条目但不删（保留历史价值）
6. **抓取方式**：GitHub 限流——gh CLI authenticated 5000 req/hour，460 PR = 460 API calls，一轮 ~5 分钟，没问题
7. **编译验证**：拉进来的 `.cu` 文件要不要 nvcc -arch=sm_100 过一遍语法检查？这需要 CUDA 12.8+ 工具链，用户本地有吗？
8. **Claude Code skill 加载行为**：`~/.claude/skills/KernelWiki/` 长到 20MB+ 后，Claude Code 启动时的 skill 发现机制会不会把所有 .md/.cu 扫进初始 context？需要确认是否需要 `.claude-skill-ignore` 或把大文件放在 Claude 不自动扫的目录

## 7. 风险

- **体积失控**：某些 PR diff 清洗后仍 >1MB（超大 refactor PR），可能要降级为"只存 key_files 的头文件片段"
- **Contest 提交抓不到**：FlashInfer MLSys 2026 leaderboard 可能还没公开；Stage C 可能得 degrade 成"仅 GPU Mode 那 12 份 + 记录 FlashInfer 的 track spec"
- **维护断代**：这些 kernel 代码不会跟随上游更新，半年后可能落伍；需在 README 明写"snapshot as of 2026-04-XX"
- **过度合成**：Stage D 为了"完整性"强行合成 variants 可能写出质量差的代码；必须和 Codex 确认每份合成 kernel 的正确性

## 8. 对 Codex 的请求

请从下列角度审核这份 draft：

1. Scope 取舍（60 核心 PR vs 460 全抓）哪个更匹配 LLM agent 的实际查询分布？
2. Stage 顺序和 round 数量估算是否合理？
3. schema 扩展是否过度？`key_files` / `full_code_dir` 会不会引入冗余？
4. 版权与 provenance 策略够不够严谨？
5. 有没有遗漏的数据来源？（如 NVIDIA GTC talk slides 代码、Tri Dao 开源的 FA4 仓库、DeepSeek 的 DeepGEMM 仓库）
6. "合成 variants" 这件事在质量和诚实性之间怎么平衡？
