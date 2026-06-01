---
id: doc-context-hub-data-layout
title: "CUDA Data Layout and Alignment"
url: https://github.com/anthropics/context-hub/tree/main/content/cuda/docs/data-layout-and-alignment
source_category: official-doc
architectures: [sm100, sm90, sm80]
tags: [vectorized-loads, shared-memory-optimization]
retrieved_at: 2026-06-01
---

# CUDA Data Layout and Alignment

## Overview

Layout affects coalescing behavior, transaction count, shared-memory bank behavior, and feasibility of vectorized loads/stores. Poor layout can dominate runtime even when arithmetic is optimized.

## Alignment Basics

- Align pointers and base addresses to vector width
- Keep struct fields ordered to reduce padding
- Avoid accidental misalignment from custom allocators or byte offsets

## AoS vs SoA

- **SoA** (structure of arrays): often better for coalesced parallel access
- **AoS** (array of structs): easier semantically but may scatter accessed fields

Choose based on the access pattern of active threads, not code convenience.

## Vectorized Access

`float2`/`float4` loads/stores are useful when data is aligned to vector width and adjacent threads follow contiguous access. Always verify achieved bandwidth after vectorization.

## 2D Layouts

- Row-major contiguous row access is usually easiest to coalesce
- Use pitched allocation when row width alignment is problematic
- Treat logical shape and physical stride as separate concepts

## Common Pitfalls

- Hidden misalignment from packed/byte-offset structs
- Mixing row-major assumptions with column-oriented access
- Forcing vectorized access on unaligned data

## Related KernelWiki Pages

- [technique-vectorized-loads](../../wiki/techniques/vectorized-loads.md)
- [technique-swizzling](../../wiki/techniques/swizzling.md)
