---
id: doc-context-hub-tcgen05-migration
title: "tcgen05 Migration Playbook: From Works to Stable"
url: https://github.com/anthropics/context-hub/tree/main/content/cuda/docs/ptx/instructions/tcgen05/references/tcgen05-migration-playbook.md
source_category: official-doc
architectures: [sm100, sm120]
tags: [tcgen05, fine-grained-quantization]
retrieved_at: 2026-06-01
---

# tcgen05 Migration Playbook

## Overview

Minimal process for taking tcgen05 from "compiles" to "ready for stable production."

## Four-Step Process

1. **Architecture gate check**: determine whether `sm_100*`/`sm_120*` are available
2. **Combination validity check**: verify `kind + stype + scale_vec_size`
3. **Protocol correctness check**: ensure fences/commit/wait on the async path and full mbarrier participation
4. **Numerical and performance regression**: establish baselines separately for alternate FP and sparse paths

## Exit Criteria

- All generated kernels pass architecture-gated validation without manual overrides
- Async protocol traces show correct fence/commit/wait ordering under stress inputs
- Numerical tolerance and performance deltas are recorded for dense and sparse variants

## Common Failure Modes

- Migration stops at "compiles" without protocol or numerical regression coverage
- Sparse and alternate-FP paths share the same baseline, hiding path-specific drift
- Fallback policy is undocumented, leading to deployment-time behavior changes

## Rollback Readiness

- Keep a tested fallback path for unsupported architecture/type combinations
- Version migration decisions with reproducible benchmark and correctness artifacts

## Related KernelWiki Pages

- [migration-wgmma-to-tcgen05](../../wiki/migration/wgmma-to-tcgen05.md)
- [hw-tcgen05-mma](../../wiki/hardware/tcgen05-mma.md)
- [hw-nvfp4](../../wiki/hardware/nvfp4.md)
