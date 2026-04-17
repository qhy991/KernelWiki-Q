# Query: By Problem / Symptom

> Auto-generated. Do not edit manually.

| Symptom | Pattern Page | Candidate Techniques | Sources |
|---------|-------------|---------------------|---------|
| low-sm-utilization, tail-effect, load-imbalance | [Low SM Utilization](../wiki/patterns/low-sm-utilization.md) | [Persistent Kernels with CLC](../wiki/techniques/persistent-kernels.md), [Tile Scheduling Strategies](../wiki/techniques/tile-scheduling.md) | 2 sources |
| memory-bound, low-compute-utilization, high-memory-throughput | [Memory Bandwidth Bound](../wiki/patterns/memory-bound.md) | [Wide Vectorized Loads and Cache Policies](../wiki/techniques/vectorized-loads.md), [Shared Memory Swizzling](../wiki/techniques/swizzling.md), [Software Pipelining and Multi-Stage Buffering](../wiki/techniques/pipeline-stages.md) | 3 sources |
| compute-bound, low-tensor-core-utilization, pipeline-stalls | [Not Reaching Peak FLOPS](../wiki/patterns/compute-bound.md) | [Software Pipelining and Multi-Stage Buffering](../wiki/techniques/pipeline-stages.md), [Warp Specialization on Blackwell](../wiki/techniques/warp-specialization.md), [Epilogue Fusion](../wiki/techniques/epilogue-fusion.md) | 3 sources |
| register-pressure, low-occupancy, register-spilling | [Register Pressure — Low Occupancy](../wiki/patterns/register-pressure.md) | [Warp Specialization on Blackwell](../wiki/techniques/warp-specialization.md) | 2 sources |
| tail-effect, low-sm-utilization, wave-quantization | [Tail Effect — Last Wave Underutilization](../wiki/patterns/tail-effect.md) | [Persistent Kernels with CLC](../wiki/techniques/persistent-kernels.md), [Tile Scheduling Strategies](../wiki/techniques/tile-scheduling.md) | 2 sources |
