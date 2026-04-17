---
id: doc-ptx-isa-sm100
title: "PTX ISA — SM100 Instructions"
url: https://docs.nvidia.com/cuda/parallel-thread-execution/
source_category: official-doc
architectures: [sm100, sm100a]
tags: [ptx, tcgen05, tmem, clc, tma, mbarrier]
retrieved_at: 2026-04-16
---

## Summary

PTX ISA reference for SM100-specific instructions.

## Key SM100 PTX Instructions

### Tensor Core (tcgen05)
- `tcgen05.mma` — MMA operation, single-thread issue, SMEM inputs, TMEM output
- `tcgen05.alloc` — Allocate TMEM columns
- `tcgen05.dealloc` — Free TMEM columns
- `tcgen05.ld` — Load from TMEM to registers
- `tcgen05.st` — Store from registers to TMEM
- `tcgen05.cp` — Copy from SMEM to TMEM
- `tcgen05.fence::after_thread_sync` — Fence between TMA and MMA

### Cluster Launch Control
- `clusterlaunchcontrol.try_cancel` — Query next available tile
- Returns valid ClcID or decline signal

### TMA (shared with SM90)
- `cp.async.bulk.tensor` — Bulk tensor copy
- Enhanced for Blackwell with mandatory 128B swizzling

### mbarrier
- Two sync pairs: TMA↔MMA, Mainloop↔Epilogue
- Phase-based with parity bits
