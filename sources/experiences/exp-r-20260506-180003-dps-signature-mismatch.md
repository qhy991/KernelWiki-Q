---
id: exp-r-20260506-180003-dps-signature-mismatch
title: DPS signature mismatch - non-void run() vs void run() with trailing output
  parameters
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
captured_at: '2026-05-06'
confidence: inferred
reproducibility: concept
---

## Key Lessons

- DPS=true requires void run(*inputs, *outputs) with output tensors as trailing parameters mutated in-place
- DPS=false requires result = run(*inputs) with output returned by value
- Always check definition.json for spec.destination_passing_style before choosing the run() signature
- The SOL-ExecBench static gate explicitly validates DPS compliance before compilation
- Output tensors in DPS mode are pre-allocated by the harness; the kernel must write in-place, not allocate new tensors
