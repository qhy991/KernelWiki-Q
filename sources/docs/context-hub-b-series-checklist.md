---
id: doc-context-hub-b-series-checklist
title: "B-Series Implementation Checklist (tcgen05)"
url: https://github.com/anthropics/context-hub/tree/main/content/cuda/docs/ptx/instructions/tcgen05/references/b-series-checklist.md
source_category: official-doc
architectures: [sm100, sm120]
tags: [tcgen05]
retrieved_at: 2026-06-01
---

# B-Series Implementation Checklist

## Checklist

- `.target` matches the actual deployment architecture (`sm_100`/`sm_120`)
- All tcgen05/WGMMA variants have passed capability gating
- Relevant async protocols (fence/commit/wait) are complete
- `sm_120a` restricted types have been checked and have fallbacks
- Linked scenarios with TMA paths have completed correctness regression testing

## Release Notes for Reviewers

- Record the capability matrix used during generation and testing
- Include sparse and alternate-FP coverage status explicitly in release notes
- Document fallback behavior when tcgen05 constraints fail on target hardware

## Minimum Evidence Package

- One correctness report per architecture family (`sm_100*`, `sm_120*`) with capability-gated variants
- One protocol trace confirming async fence/commit/wait ordering on representative kernels
- One numerical report covering dense, sparse, and alternate-FP routes

## Related KernelWiki Pages

- [migration-wgmma-to-tcgen05](../../wiki/migration/wgmma-to-tcgen05.md)
- [hw-tcgen05-mma](../../wiki/hardware/tcgen05-mma.md)
