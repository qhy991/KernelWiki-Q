---
id: exp-r-20260502-180007-attempt-dir-not-bound
title: sol_execbench_gemm
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
reproducibility: concept
---

SOL-ExecBench sandbox_execute always fails with 'attempt_dir not bound' even after static_gate passes, causing verification to never execute

### Symptoms

- `sol_execbench_update_sources 返回 success=true, static_gate_passed=true`
- `sandbox_execute 返回 exit_code=-1，无 stdout/stderr`
- `错误信息: 'Canonical verification requires an active attempt_dir. Bind the current assignment before running or recording verification.'`
- `反复重试同一命令均失败，步数耗尽`

## Challenge

LLM 生成的代码通过了 sol_execbench_update_sources 的 static_gate 检查，但运行 sandbox_execute 执行 sol-execbench 验证时，始终报 'Canonical verification requires an active attempt_dir. Bind the current assignment before running or recording verification.'。这不是代码问题，而是框架编排层面的 bug：task binding 没有在验证前正确传递到 sandbox_execute 环境。


## Solution

这是框架编排层的 bug，不是 LLM 可以通过修改代码解决的问题。需要在调度层修复 attempt_dir 的绑定传递。

LLM 端的临时规避策略：
1. 不要反复重试同一个失败的 sandbox_execute 命令（会在 3 次后触发 dead loop 保护）。
2. 尝试使用 delegate_coding 让 coder 子任务直接在子 workspace 中运行验证（coder 子任务有自己的 task binding 上下文，可以绕过主任务 binding 问题）。
3. 如果 delegate_coding 也不可用，使用 finish() 报告框架错误，而不是继续浪费步数。

## Key Lessons

- attempt_dir not bound 是框架编排层的 bug，不是生成代码的问题。代码可能完全正确但无法验证。
- 遇到此错误时不要反复重试（3 次后触发 dead loop），应尽早使用 delegate_coding 或 finish() 切换策略。
- 使用 delegate_coding 委托给 coder 子任务是可行的规避方案——coder 子任务有独立的 task binding context。
- 在 64 个实验中，此错误出现了 54 次（约 87% 的实验），是最频繁的失败原因。
- 此问题的根因是主任务的 task_binding 没有在 sandbox_execute 调用前正确传递 attempt_dir 变量。
