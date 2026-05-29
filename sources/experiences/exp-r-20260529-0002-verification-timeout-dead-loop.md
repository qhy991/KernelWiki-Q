---
id: exp-r-20260529-0002-verification-timeout-dead-loop
title: Agent retries sol-execbench verification 30+ times after timeout without modifying
  kernel
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

Agent retries sol-execbench verification 30+ times after timeout without modifying kernel

## Key Lessons

- 2 consecutive sol-execbench timeouts = kernel hangs, not infrastructure issue. STOP retrying and FIX the kernel.
- Timeout on large workloads but success on small ones indicates O(n) or O(n^2) algorithmic issue, not a random failure.
- Always test with a small workload first (batch=1, few pages) with short timeout (30s) to verify the kernel can complete at all.
- Check kernel loop bounds: verify that the page table iteration (kv_indptr[kv_indptr[b+1]-1]) does not exceed kv_indices length.
- After modifying kernel source, run compile-smoke BEFORE full sol-execbench verification to catch compilation errors quickly.
