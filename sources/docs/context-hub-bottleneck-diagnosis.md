---
id: doc-context-hub-bottleneck-diagnosis
title: "Kernel Bottleneck Diagnosis Workflow"
url: https://github.com/anthropics/context-hub/tree/main/content/cuda/docs/kernel-bottleneck-diagnosis-workflow
source_category: official-doc
architectures: [sm100, sm90, sm80]
tags: [register-budgeting, vectorized-loads]
retrieved_at: 2026-06-01
---

# Kernel Bottleneck Diagnosis Workflow

## Overview

Repeatable workflow for classifying kernels into memory-bound, compute-bound, or launch-bound categories, then routing to targeted optimization paths.

## Classification

Classify each hot kernel into one of three primary classes using profiling evidence:

- **Memory-bound**: high memory-pipeline utilization with low arithmetic utilization; strong sensitivity to coalescing/layout changes
- **Compute-bound**: arithmetic pipeline pressure dominates; throughput improves mainly with instruction-mix or scheduling improvements
- **Launch-bound**: many short kernels; significant CPU/launch overhead and weak overlap

## Optimization Routing

- Memory-bound: prioritize coalescing, reuse, layout, and staging fixes
- Compute-bound: optimize instruction mix, occupancy/ILP balance, and path selection
- Launch-bound: reduce launch count, fuse kernels where valid, evaluate CUDA Graphs

## Guardrails

- Reclassify after each major optimization; bottleneck class can change
- Keep correctness and numerical checks active during performance iteration
- Record profiler snapshots per step to avoid regression ambiguity

## Related KernelWiki Pages

- [pattern-memory-bound](../../wiki/patterns/memory-bound.md)
- [pattern-compute-bound](../../wiki/patterns/compute-bound.md)
- [pattern-low-sm-utilization](../../wiki/patterns/low-sm-utilization.md)
- [pattern-register-pressure](../../wiki/patterns/register-pressure.md)
