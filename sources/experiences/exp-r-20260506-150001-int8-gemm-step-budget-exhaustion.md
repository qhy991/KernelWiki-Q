---
id: exp-r-20260506-150001-int8-gemm-step-budget-exhaustion
title: 'SOL-ExecBench INT8 GEMM: step budget exhaustion pattern'
experience_type: repair
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
captured_at: '2026-05-06'
confidence: inferred
reproducibility: snippet
techniques:
- fine-grained-quantization
impl_family: cublas
---

INT8 GEMM implementation tasks can exhaust step budget (52 steps) when agent spends too much time on CUTLASS template debugging, compilation failures, or exploring wrong approaches. The correct strategy is: Round 1 Step 1 must use the cuBLAS+dequant complete template directly. Do not explore DP4A, manual CUDA, or CUTLASS in Round 1.

## Challenge

Agent exhausts step budget (52 steps) before completing INT8 GEMM implementation. Common causes: (1) debugging CUTLASS INT8 template instantiation failures, (2) multiple compilation attempts with different configurations, (3) spending too many steps on environment issues.

### Symptoms

- `Step budget exhausted after 52 steps`
- `Task incomplete: did not finish within step budget`
- `Partial results available but not verified`
- `Agent stuck in CUTLASS INT8 template debugging loop`

## Solution

Use the cuBLAS+dequant complete template on Round 1 Step 1. Do not explore alternative approaches (DP4A, manual CUDA, CUTLASS) in the first round. The template is copy-paste-ready and verified across all shapes. Exploring alternatives wastes 15-20 steps on approaches with >80% failure rate.

### Implementation

```cuda
## Step-efficient INT8 GEMM protocol:

### Round 1 (MUST follow exactly):
1. Step 1: Write the complete cuBLAS+dequant template (kernel.h + kernel.cu + main.cpp)
2. Step 2: Run compilation smoke test
3. Step 3: Run canonical verification
4. Steps 4-10: If verification fails, fix based on error type:
   - compilation: check includes, extern C, stream API
   - INCORRECT_NUMERICAL: check B layout, scale types, cuBLAS params
   - wrong speedup: check handle reuse, workspace allocation
5. Do NOT attempt DP4A, manual CUDA, or CUTLASS in Round 1

### Round 2+ (only if Round 1 has a working baseline):
1. Read the seed solution from Round 1
2. If speedup >= 2.0x: tune dequant block sizes or try fused epilogue
3. If speedup < 2.0x: try CUBLAS_COMPUTE_32I_FAST_16FIMMA or adjust tensor core selection
4. Only attempt CUTLASS if: (a) cuBLAS baseline works, (b) >10 steps remain

### Step budget allocation:
- Round 1: 3 steps for template + compile + verify. Reserve 7 steps for fixes.
- Round 2: 5 steps for reading seed + incremental change + verify.
- NEVER spend >3 steps on CUTLASS debugging.
```

## Key Lessons

- Round 1 Step 1 MUST use the cuBLAS+dequant complete template. Do not explore DP4A, manual CUDA, or CUTLASS. The template is copy-paste-ready and verified on all shapes.
- Step budget exhaustion is a common failure mode for INT8 GEMM tasks. 52 steps means ~10 steps per round in a 5-round session. Each step is precious.
- CUTLASS INT8 template debugging can consume 20+ steps with <30% success rate. Only attempt AFTER a working cuBLAS baseline exists AND >10 steps remain.
- Round 1 should take exactly 3 steps if the template compiles: (1) write template, (2) compile smoke, (3) verify. Reserve remaining steps for fixes.
- Exploring DP4A or manual CUDA before cuBLAS wastes 15-20 steps on approaches with >80% failure rate for most shapes.
- Limit CUTLASS debugging to 3 compilation attempts. If it doesn't compile in 3 attempts, it won't compile in 30.
- Partial results (unverified solution.json) can be used as starting point for next round.
