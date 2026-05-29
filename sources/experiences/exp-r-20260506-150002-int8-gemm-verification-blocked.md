---
id: exp-r-20260506-150002-int8-gemm-verification-blocked
title: 'SOL-ExecBench BF16 GEMM: verification blocked by static gate'
experience_type: repair
source_category: agent-experiment
architectures:
- sm90
tags:
- gemm
kernel_types:
- gemm
languages:
- cuda-cpp
captured_at: '2026-05-06'
confidence: inferred
reproducibility: snippet
---

BF16 GEMM verification can be blocked by SOL-ExecBench static gate when solution.json contains unimplemented scaffold placeholders.

## Challenge

SOL-ExecBench static gate blocks verification when solution.json contains unimplemented scaffold placeholders. The gate checks for patterns like '/* add problem-specific parameters */', 'TODO kernel-launch scaffold', and 'throw std::runtime_error("not implemented")'.

### Symptoms

- `Verification blocked: the SOL-ExecBench static gate detected unimplemented scaffold placeholders`
- `Source main.cpp still contains unimplemented scaffold placeholder(s)`
- `Replace the skeleton with real implementation code before verification`

## Solution

Before running verification, ensure solution.json contains complete implementation code without scaffold placeholders. Replace all TODO comments, throw statements, and placeholder patterns with actual implementation.

### Implementation

```cuda
1. Check solution.json for scaffold patterns before verification:
   - '/* add problem-specific parameters */'
   - 'TODO kernel-launch scaffold'
   - 'throw std::runtime_error("not implemented")'
   - 'not implemented'
2. Replace all placeholders with actual implementation code
3. For GEMM: implement actual kernel launch with correct parameters
4. Run compile smoke first to catch build issues
5. Only run full verification after compile smoke passes
6. If verification is blocked, check static gate error message for specific patterns to fix
```

## Key Lessons

- SOL-ExecBench static gate blocks verification for unimplemented scaffold placeholders.
- Common placeholder patterns: TODO comments, throw statements, 'not implemented' strings.
- Always replace scaffold placeholders with actual implementation before verification.
- Run compile smoke first to catch build issues before full verification.
- Check static gate error message for specific patterns to fix.
- GEMM implementation must have actual kernel launch code, not just function signatures.
