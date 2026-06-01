---
id: doc-context-hub-nsight-cheatsheet
title: "Nsight Metrics Interpretation Cheatsheet"
url: https://github.com/anthropics/context-hub/tree/main/content/cuda/docs/nsight-metrics-interpretation-cheatsheet
source_category: official-doc
architectures: [sm100, sm90, sm80]
tags: [register-budgeting, vectorized-loads]
retrieved_at: 2026-06-01
---

# Nsight Metrics Interpretation Cheatsheet

## Overview

Practical mapping from common Nsight profiler metric patterns to likely bottleneck classes and next optimization actions.

## Symptom To Action Map

- **High memory pressure + low arithmetic utilization**: likely memory-bound, prioritize coalescing/layout/reuse
- **Low issue efficiency + dependency-heavy stalls**: likely compute-bound scheduling/dependency bottleneck
- **Many short kernels + high CPU orchestration share**: likely launch-bound, evaluate fusion/graphs/overlap changes

## Warp Stall Reading Rules

- Treat stall reasons as supporting evidence, not standalone truth
- Interpret stall categories together with achieved throughput and occupancy
- Re-check after each optimization stage because dominant stalls can shift

## Minimal Workflow

1. Timeline classify (Nsight Systems)
2. Kernel-level metrics drilldown (Nsight Compute)
3. Route to memory/compute/launch playbook
4. Reprofile and confirm bottleneck shift

## Related KernelWiki Pages

- [pattern-memory-bound](../../wiki/patterns/memory-bound.md)
- [pattern-compute-bound](../../wiki/patterns/compute-bound.md)
- [pattern-low-sm-utilization](../../wiki/patterns/low-sm-utilization.md)
- [pattern-pipeline-stalls](../../wiki/patterns/pipeline-stalls.md)
