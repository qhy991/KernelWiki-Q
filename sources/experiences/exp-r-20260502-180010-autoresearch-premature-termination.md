---
id: exp-r-20260502-180010-autoresearch-premature-termination
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
---

AutoResearch session terminates immediately after bootstrap skeleton is written, no implementation attempted

### Symptoms

- `session 创建与结束时间差 < 5 秒`
- `session_messages.jsonl 为空（0 行消息）`
- `rounds_completed=0，rounds=[]`
- `solution.json 中全是 TODO 占位符`
- `session_state_v2.status=running 但实际已停止`
- `experience_pipeline: captured=0, triaged=0`

## Challenge

AutoResearch 会话 autoresearch_20260430_210217_eeaf814d 在创建后仅存活 2 秒（21:02:17 → 21:02:19）就结束了。session_state_v2.json 显示 status=running 但 rounds_completed=0，session_messages.jsonl 为空（0 行），没有任何 LLM 交互发生。骨架 solution.json 被预写好但内容全是 TODO 占位符，没有实际 kernel 实现。experience_pipeline 显示 captured=0, triaged=0, reviewed=0。


## Solution

这是一个 AutoResearch 会话初始化/调度层面的问题，不是 kernel 实现问题。会话在调度阶段就被异常终止了，LLM agent 从未获得执行机会。

### Implementation

```cuda
1. 检查 AutoResearch 调度器（session manager）的日志，查看为何会话被立即关闭
2. 检查 bootstrap packet 中的 status 字段 — 如果创建时就显示 closed，说明是调度器逻辑问题
3. 检查 LLM provider 连接是否正常 — 如果 API key 过期或网络问题，agent 可能无法启动
4. 检查 resource limits — 是否有并发会话限制或 token budget 限制
5. 重新创建会话时，先验证 LLM provider 可达性
```

## Key Lessons

- AutoResearch 会话在 2 秒内终止且无任何消息，表明问题出在调度/初始化层而非 kernel 实现层。
- 当 session_messages.jsonl 为空且 rounds_completed=0 时，不要分析 kernel 代码问题，应检查系统调度和 LLM provider 状态。
- session_state_v2.json 中的 status=running 可能不准确，需结合 message_count 和 created_at/updated_at 时间差综合判断。
- 骨架 solution.json 被正确预写（包含正确的 spec、languages、entry_point），说明 bootstrap 流程本身正常，问题在后续 agent 调度。
