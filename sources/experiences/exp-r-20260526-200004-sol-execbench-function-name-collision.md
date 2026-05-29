---
id: exp-r-20260526-200004-sol-execbench-function-name-collision
title: 'SOL-ExecBench: duplicate function name ''run'' causing linker error'
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
captured_at: '2026-05-26'
confidence: inferred
reproducibility: concept
impl_family: custom_cuda
---

Defining a function named 'run()' in kernel.cu conflicts with main.cpp's framework-provided run() function, causing 'multiple definition' linker error. Use a unique name matching the kernel.h declaration.

### Symptoms

- `multiple definition of `run'`
- `Linker error (not compile error) — individual .o files compile fine`
- `Error appears when linking kernel.o and main.o together`
- `kernel.cu defines a function with same name as one in main.cpp`

## Challenge

SOL-ExecBench links kernel.cu and main.cpp into a single binary. If kernel.cu defines a function named 'run()' (a common generic name), it collides with main.cpp's framework-provided run() function at link time, producing 'multiple definition of `run(...)` errors.


## Solution

Use a unique, descriptive function name in kernel.cu that matches the declaration in kernel.h. Standard naming patterns for SOL-ExecBench:

  void gemm_launch(const void* A, const void* B, void* C, int M, int N, int K, cudaStream_t stream);
  void rmsnorm_launch(const void* input, void* output, const void* weight, int batch, int hidden, cudaStream_t stream);

Never use generic names like 'run', 'compute', 'execute', 'launch', 'kernel' as top-level function names — these may conflict with framework functions.

The function signature in kernel.h is what main.cpp calls. kernel.cu must implement that exact signature.

## Key Lessons

- SOL-ExecBench uses split compilation: kernel.cu (nvcc) + main.cpp (g++), linked together. Function names must be globally unique across both translation units.
- main.cpp is provided by the framework and may define common names like 'run()', 'main()', 'benchmark()', 'verify()'. Do not redefine these in kernel.cu.
- kernel.h serves as the interface contract between kernel.cu and main.cpp. Use a unique, descriptive name like 'gemm_launch' or 'rmsnorm_forward' — not generic names.
- If you get 'multiple definition' at link time, check if kernel.cu accidentally shadows a framework function from main.cpp.
