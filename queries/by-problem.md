# Query: By Problem / Symptom

> Auto-generated from `wiki/patterns/*.md` frontmatter. Do not edit manually.
> Regenerate: `python scripts/generate-indices.py`

| Symptom | Pattern Page | Candidate Techniques | Sources |
|---------|-------------|---------------------|---------|
| low-sm-utilization, tail-effect, load-imbalance | [Low SM Utilization](wiki/patterns/low-sm-utilization.md) | technique-persistent-kernels, technique-tile-scheduling, hw-clc | 2 sources |
| memory-bound, low-compute-utilization, high-memory-throughput | [Memory Bandwidth Bound](wiki/patterns/memory-bound.md) | technique-vectorized-loads, technique-swizzling, technique-tma-multicast | 3 sources |
| compute-bound, low-tensor-core-utilization, pipeline-stalls | [Not Reaching Peak FLOPS](wiki/patterns/compute-bound.md) | hw-2sm-cooperative, technique-pipeline-stages, technique-warp-specialization, technique-epilogue-fusion | 3 sources |
| register-pressure, low-occupancy, register-spilling | [Register Pressure — Low Occupancy](wiki/patterns/register-pressure.md) | hw-tmem, technique-warp-specialization, migration-register-to-tmem | 2 sources |
| tail-effect, low-sm-utilization, wave-quantization | [Tail Effect — Last Wave Underutilization](wiki/patterns/tail-effect.md) | technique-persistent-kernels, hw-clc, technique-tile-scheduling | 2 sources |
