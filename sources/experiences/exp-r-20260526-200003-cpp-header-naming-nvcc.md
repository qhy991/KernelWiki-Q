---
id: exp-r-20260526-200003-cpp-header-naming-nvcc
title: 'SOL-ExecBench: C++ header naming confusion in nvcc-compiled .cu files'
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

Using C-style header names like <cstdint.h>, <cstdlib.h>, <cstring.h> in .cu files causes 'file not found' errors. C++ standard headers have no .h suffix: use <cstdint>, <cstdlib>, <cstring>.

### Symptoms

- `fatal error: cstdint.h: No such file or directory`
- `fatal error: cstdlib.h: No such file or directory`
- `Compilation fails immediately at the include statement`
- `Only .cu files affected (nvcc compiles as C++)`

## Challenge

nvcc reports 'fatal error: cstdint.h: No such file or directory' when a .cu file uses #include <cstdint.h>. This is a C/C++ naming confusion: C headers use .h suffix (stdlib.h, stdint.h, string.h) while C++ wrappers omit it (cstdlib, cstdint, cstring). The 'c' prefix + no suffix is the C++ convention.


## Solution

Replace C-style header includes with their C++ equivalents:

  #include <cstdint.h>  → #include <cstdint>
  #include <cstdlib.h>  → #include <cstdlib>
  #include <cstring.h>  → #include <cstring>
  #include <cstdio.h>   → #include <cstdio>
  #include <climits.h>  → #include <climits>
  #include <cmath.h>    → #include <cmath>

Alternatively, use the pure C headers (valid in C++ but types are in global namespace):
  #include <stdint.h>   (provides int8_t, int32_t, etc.)
  #include <stdlib.h>
  #include <string.h>

## Key Lessons

- C++ standard headers: <cstdint> (no .h), <cstdlib> (no .h), <cstring> (no .h). The 'c' prefix means 'C++ wrapper of C header'.
- C headers: <stdint.h> (with .h, no 'c' prefix), <stdlib.h>, <string.h>. These are also valid in C++.
- There is NO file called 'cstdint.h' on any system. The combination 'c' prefix + '.h' suffix does not exist.
- .cu files are compiled as C++ by nvcc. Use C++ includes (<cstdint>) or C includes (<stdint.h>), never the hybrid form.
