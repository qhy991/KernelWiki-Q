---
id: exp-r-20260529-0001-gqa-lse-formula-error
title: 'GQA paged decode: incorrect base-2 LSE formula causes systematic ~20% numerical
  error'
experience_type: repair
source_category: agent-experiment
architectures:
- sm90
tags:
- attention
kernel_types:
- attention
languages:
- cuda-cpp
captured_at: '2026-05-29'
confidence: experimental
reproducibility: concept
---

GQA paged decode: incorrect base-2 LSE formula causes systematic ~20% numerical error

## Key Lessons

- For base-2 LSE in online softmax: lse = m_val / ln(2) + log2f(d_val), NOT (m_val + logf(d_val)) / ln(2) — the latter invites misinterpretation
- Always verify the LSE formula against the Python reference: torch.logsumexp(scores * sm_scale, dim=-1) / math.log(2)
- When all workloads show consistent ~20% relative error with no NaN/Inf, suspect a systematic formula error in the attention score normalization or LSE
- Use explicit constants: 1.4426950408889634f for 1/ln(2), avoid mixing logf and log2f in the same expression
