---
id: doc-cutlass-blackwell
title: "CUTLASS Blackwell SM100 Functionality"
url: https://docs.nvidia.com/cutlass/latest/media/docs/cpp/blackwell_functionality.html
source_category: official-doc
architectures: [sm100, sm100a]
tags: [tcgen05, tmem, clc, cute-dsl, warp-specialization, 2sm-cooperative]
retrieved_at: 2026-04-16
---

## Summary

Official CUTLASS documentation for Blackwell SM100 GEMM kernels and CuTe abstractions.

## Key Content

### CUTLASS 4.x SM100 Support
- TCGen05 MMA atoms via CuTe (SM100_MMA_*)
- TMEM as first-class data locale
- Copy atoms for tmem↔rmem, rmem↔tmem, smem↔tmem
- Warp-specialized dispatch policies: KernelTmaWarpSpecialized1SmSm100, KernelTmaWarpSpecialized2SmSm100

### Dispatch Policies
- 1-SM: KernelTmaWarpSpecialized1SmSm100
- 2-SM: KernelTmaWarpSpecialized2SmSm100
- NVF4/MXF variants for sub-byte types

### Tile Scheduling
- PersistentTileSchedulerSm100 with CLC
- PipelineCLCFetchAsync for async tile fetch

### 16-Warp Kernel Structure
- Warp 0: TMA issuance
- Warp 1: MMA issuance (single thread)
- Warps 2+: Epilogue (minimum 4 warps for TMEM Layout D access)

### SM100 Attention
- Fused reduction for MLA
- FlashMLA-like weight-absorbed decoding
- K-dimension splitting across SMs
