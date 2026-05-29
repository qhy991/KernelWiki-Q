---
id: exp-o-20260514-100004-int8-gemm-multiround-seed-solution
title: 'SOL-ExecBench INT8 GEMM: multi-round optimization must consume seed solution
  from prior round'
experience_type: optimization
source_category: agent-experiment
architectures:
- sm90
tags:
- gemm
- fine-grained-quantization
kernel_types:
- gemm
languages:
- cuda-cpp
captured_at: '2026-05-14'
confidence: inferred
reproducibility: snippet
techniques:
- fine-grained-quantization
impl_family: cublas
---

In multi-round autoresearch sessions, Round 2+ agents frequently ignore the best solution from Round 1 and start from scratch with a different approach (e.g., DP4A or manual CUDA instead of the working cuBLAS from Round 1). This wastes the entire round budget. The seed solution from the previous round's best attempt is available in the round assignment and must be consumed as the starting point for incremental optimization.

## Challenge

Round 2+ agents in autoresearch mode start coding from scratch instead of reading and improving the seed solution from the previous round. This causes: (1) repeating the same compilation failures already solved in Round 1, (2) switching to a worse approach (DP4A after working cuBLAS), (3) wasting 15-20 steps on boilerplate that Round 1 already produced correctly.

### Symptoms

- `Round 2 attempts a completely different implementation approach than Round 1's best`
- `Round 2 repeats the same B layout or parameter mapping errors Round 1 already fixed`
- `Round 2 starts with torch.mm wrapper instead of improving the cuBLAS solution from Round 1`
- `Performance regresses in Round 2 (e.g., 2.67x in Round 1, 0.04x in Round 2)`

## Solution

In Round 2+, the agent MUST: (1) read the seed solution files from the previous round's best attempt, (2) use the existing code as the starting point, (3) make targeted optimizations rather than rewriting from scratch. The seed solution path is provided in the round assignment.

### Implementation

```cuda
## Multi-round INT8 GEMM optimization protocol:

### Step 1: Read the seed solution
The seed solution from the previous round's best attempt is available at:
  <attempt_dir>/r<round-1>/v1/solution.json
Read this file FIRST. It contains the working kernel.h, kernel.cu, and main.cpp.

### Step 2: Identify the current approach
Check what implementation the seed uses:
- cuBLAS+dequant -> optimize dequant kernel, try fused epilogue, adjust block sizes
- DP4A -> optimize tile sizes, try cuBLAS for comparison
- Manual CUDA -> switch to cuBLAS if not already using it

### Step 3: Targeted improvement
Based on the seed's performance:
- If speedup < 1.5x and using cuBLAS: check handle reuse, stream sync, workspace allocation
- If speedup 1.5x-2.5x: try CUTLASS fused epilogue (only if cuBLAS baseline works)
- If speedup > 2.5x: tune dequant block sizes (try 32x8, 16x16, 64x4)

### Step 4: Preserve what works
- Keep the exact cuBLAS parameter mapping from the seed
- Keep the extern C declarations and file structure
- Only change the optimization target, not the core GEMM logic

### Anti-patterns to avoid:
- DO NOT start with torch.mm/torch.matmul wrapper
- DO NOT switch from cuBLAS to DP4A or manual CUDA
- DO NOT rewrite kernel.h declarations that already compile
- DO NOT change B layout handling that already produces correct results
```

## Key Lessons

- In Round 2+, ALWAYS read the seed solution.json from the previous round's best attempt before writing any code. It contains a working implementation that can be incrementally improved.
- NEVER switch implementation approach between rounds. If Round 1 works with cuBLAS, Round 2 should optimize the cuBLAS code, not try DP4A or manual CUDA.
- The seed solution preserves the correct B layout, cuBLAS parameter mapping, and extern C declarations. Reusing it avoids repeating the same compilation and correctness failures.
- Targeted improvements on a working baseline always outperform rewriting from scratch. Incremental changes: block size tuning, handle reuse optimization, fused epilogue.
- If Round 1 failed to produce a working solution, Round 2 should use the cuBLAS+dequant template directly (from the companion experience), not explore other approaches.
