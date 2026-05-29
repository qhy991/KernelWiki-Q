---
id: exp-r-20260513-100012-cutlass-include-path-missing
title: 'SOL-ExecBench CUTLASS kernel: include path not in compile_options'
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
- cute-dsl
captured_at: '2026-05-13'
confidence: inferred
reproducibility: snippet
impl_family: cutlass
---

When using CUTLASS headers (#include cutlass/...) in kernel.cu, the CUTLASS include path must be added to spec.compile_options.cuda_cflags as '-I/usr/local/cutlass/include' and '-I/usr/local/cutlass/tools/util/include'. Without these, compilation fails with 'cutlass/...: No such file or directory'.

## Challenge

Agent writes kernel.cu with CUTLASS #include directives but doesn't add the CUTLASS include paths to solution.json spec.compile_options. The compiler cannot find the CUTLASS headers.

### Symptoms

- `fatal error: cutlass/...: No such file or directory`
- `compilation terminated`
- `Affects any CUTLASS-based kernel implementation`

## Solution

Add CUTLASS include paths to solution.json spec.compile_options.cuda_cflags and cflags.

### Implementation

```cuda
// In solution.json spec.compile_options:
{
  "cuda_cflags": [
    "-O3",
    "--use_fast_math",
    "-std=c++17",
    "-I/usr/local/cutlass/include",
    "-I/usr/local/cutlass/tools/util/include"
  ],
  "cflags": [
    "-O3",
    "-std=c++17",
    "-I/usr/local/cutlass/include"
  ],
  "ld_flags": ["-lcublas"]
}

// The CUTLASS paths on this system:
// /usr/local/cutlass/include         — main CUTLASS headers
// /usr/local/cutlass/tools/util/include — utility headers
```

## Key Lessons

- CUTLASS headers require explicit include paths. Add -I/usr/local/cutlass/include and -I/usr/local/cutlass/tools/util/include to cuda_cflags in solution.json.
- CUTLASS installation on this system is at /usr/local/cutlass/. The include and tools/util/include directories are both needed.
- Also add -std=c++17 when using CUTLASS — it requires C++17 features.
- For CUTLASS kernels that also use cuBLAS, add -lcublas to ld_flags.
- The compile_options must be set in solution.json BEFORE submitting for verification. They are part of the solution spec, not runtime configuration.
