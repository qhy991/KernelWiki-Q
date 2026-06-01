---
id: doc-context-hub-thread-block-clusters
title: "CUDA Thread Block Clusters"
url: https://github.com/anthropics/context-hub/tree/main/content/cuda/docs/thread-block-clusters
source_category: official-doc
architectures: [sm100, sm90]
tags: [clc, cluster, shared-memory-optimization]
retrieved_at: 2026-06-01
---

# CUDA Thread Block Clusters

## Overview

Thread Block Clusters add an optional hierarchy level above blocks. Multiple blocks form one cluster, co-scheduled on the same GPC, enabling direct synchronization and communication. Available on compute capability 9.0+.

## Launch Mechanisms

- Compile time: `__cluster_dims__(x, y, z)`
- Launch time: `cudaLaunchKernelEx` with cluster-dimension attribute

`gridDim` still counts blocks, not clusters. The grid should be compatible with cluster dimensions.

## Cluster Synchronization

```cpp
auto cluster = cooperative_groups::this_cluster();
cluster.sync();
```

Cluster-scope analogue of block synchronization for blocks in the same cluster.

## Distributed Shared Memory

Blocks in a cluster can read/write shared memory owned by another block in the same cluster. Atomics can also target distributed shared memory addresses. Useful when one block's shared memory is too small but full global-memory communication is too expensive.

## Portable Cluster Size Rule

8 blocks is the portable maximum cluster size. Query support via `cudaOccupancyMaxPotentialClusterSize` instead of hard-coding.

## When To Use Clusters

Good fit when:
- Communication across neighboring blocks is frequent
- Distributed shared memory removes expensive global-memory round trips
- Algorithm naturally decomposes into tightly coupled blocks

Avoid when:
- Kernel is simple enough for ordinary per-block decomposition
- Portability matters more than architecture-specific optimization

## Related KernelWiki Pages

- [hw-clc](../../wiki/hardware/clc.md)
- [technique-persistent-kernels](../../wiki/techniques/persistent-kernels.md)
- [technique-tile-scheduling](../../wiki/techniques/tile-scheduling.md)
