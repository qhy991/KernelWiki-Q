# Query: By Experience

> Auto-generated. Do not edit manually.

## attention

| ID | Title | Type | Architectures | Languages |
|----|-------|------|--------------|-----------|
| [exp-a-20260323-152446-0af59b22](../sources/experiences/exp-a-20260323-152446-0af59b22.md) | ## Task
Apply optimization to flash_attention kernel FA_01 in Round 2. Read kernel.cu from /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260323_150539_d9b92470/attempts/FA_01/r1/v1/ker | analysis | sm90 | cuda-cpp |
| [exp-a-20260324-115144-17bb4520](../sources/experiences/exp-a-20260324-115144-17bb4520.md) | ## Task
Write an optimized pure CUDA flash attention kernel for Qwen2.5-7B with Q4_0 KV cache. Write the complete kernel.cu file to /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260324 | analysis | sm90 | cuda-cpp |
| [exp-a-20260324-140805-8ad7dea8](../sources/experiences/exp-a-20260324-140805-8ad7dea8.md) | ## Task
Write an optimized pure CUDA flash attention kernel for task FA_12 and run the test to verify correctness and performance.

## Goal
Kernel compiles, passes correctness check, and achieves perf | analysis | sm90 | cuda-cpp |
| [exp-a-20260324-143036-fbe3d628](../sources/experiences/exp-a-20260324-143036-fbe3d628.md) | ## Task
Write an optimized CUDA flash attention kernel for task FA_12 (fp32_flash_attention_qwen2_5_7b_f16_cache8192) and test it. Then log results to results.tsv and update best_kernels.json if it im | analysis | sm90 | cuda-cpp |
| [exp-a-20260324-145123-aca9ca55](../sources/experiences/exp-a-20260324-145123-aca9ca55.md) | ## Task
Create optimized CUDA flash attention kernel at /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260324_140048_205d9eb5/attempts/FA_12/r2/v5/kernel.cu. Use shared memory for BOTH  | analysis | sm90 | cuda-cpp |
| [exp-a-20260324-185538-6422a673](../sources/experiences/exp-a-20260324-185538-6422a673.md) | Optimize flash_attention kernel for FA_12 task while maintaining correctness | analysis | sm90 | cuda-cpp |
| [exp-a-20260324-192707-89268cbf](../sources/experiences/exp-a-20260324-192707-89268cbf.md) | ## Task
Optimize the flash_attention kernel for FA_12 task. The current best kernel is at /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260324_182309_e639ccc9/attempts/FA_12/r1/v3/kern | analysis | sm90 | cuda-cpp |
| [exp-a-20260324-193709-1043172f](../sources/experiences/exp-a-20260324-193709-1043172f.md) | ## Task
Create an optimized flash attention CUDA kernel for FA_12 task. The current best kernel is at /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260324_182309_e639ccc9/attempts/FA_1 | analysis | sm90 | cuda-cpp |
| [exp-a-20260324-193752-39489fc9](../sources/experiences/exp-a-20260324-193752-39489fc9.md) | Optimize flash_attention kernel for FA_12 task while maintaining correctness | analysis | sm90 | cuda-cpp |
| [exp-a-20260324-201052-39489fc9](../sources/experiences/exp-a-20260324-201052-39489fc9.md) | Optimize flash_attention kernel for FA_12 task while maintaining correctness | analysis | sm90 | cuda-cpp |
| [exp-a-20260325-135700-4b5c6f98](../sources/experiences/exp-a-20260325-135700-4b5c6f98.md) | ## Task
Create FA_11 flash_attention kernel from baseline and run initial test

## Goal
Copy baseline kernel to attempt directory and run test to establish baseline performance

## Constraints
- kernel.cu must be pure CUDA: no torch/ATen/c10 includes
- Entry function must be named flash_attn_kernel
- Attempt dir: /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_134525_136de496/attempts/FA_11/r2/v1

## Verification
After writing the code, run this command to verify:
```
cd /home/qinhaiyan/Research/kernelevalplus && python3 llm_kernel_test/unified_test_runner.py --test --attempt-path /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_134525_136de496/attempts/FA_11/r2/v1 --definition /home/qinhaiyan/Research/kernelevalplus/definitions/flash_attention/qwen/fp32_flash_attention_qwen2_5_7b_f16_cache4096.json
```

## Seeded Files
The following files have been placed in your workspace (`/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_134525_136de496/task_002_20260325_134858/coder_workspace/coder_1774417858_1216`):
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_134525_136de496/task_002_20260325_134858/coder_workspace/coder_1774417858_1216/baseline_path`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_134525_136de496/task_002_20260325_134858/coder_workspace/coder_1774417858_1216/definition_path`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_134525_136de496/task_002_20260325_134858/coder_workspace/coder_1774417858_1216/task_context.json`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_134525_136de496/task_002_20260325_134858/coder_workspace/coder_1774417858_1216/iterations.json`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_134525_136de496/task_002_20260325_134858/coder_workspace/coder_1774417858_1216/llm_calls.json`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_134525_136de496/task_002_20260325_134858/coder_workspace/coder_1774417858_1216/round_state.json`
Read them first using their **absolute paths** shown above.

## Workspace & Output Placement
- Your workspace root is: `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_134525_136de496/task_002_20260325_134858/coder_workspace/coder_1774417858_1216`
- **IMPORTANT**: Seeded files are at `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_134525_136de496/task_002_20260325_134858/coder_workspace/coder_1774417858_1216/<filename>`, NOT in any subdirectory.
- Use `sandbox_execute(command="ls /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_134525_136de496/task_002_20260325_134858/coder_workspace/coder_1774417858_1216")` if you need to verify what files exist.
- Prefer writing final outputs in the workspace root.
- If a file like `program.md` is not present, do NOT attempt to read it; rely on the provided context instead.

## Workflow
1. Load relevant skills if specified above
2. Read seeded files to understand existing code
3. Write/modify code to achieve the goal. If the code is long, split it across multiple writes/edits and keep files consistent after each chunk.
4. Run verification command (if provided) to check correctness
5. If verification fails, diagnose and fix
6. Call `finish(result="<see format below>", success=True/False)`

**finish result format** (use these exact section headers):
```
SUMMARY: <one-line description of what you did>
DECISIONS:
- <key decision 1>
- <key decision 2>
ISSUES:
- <known issue or remaining problem>
```
If no decisions or issues, omit that section. | analysis | sm90 | cuda-cpp |
| [exp-a-20260325-141129-6a0518a8](../sources/experiences/exp-a-20260325-141129-6a0518a8.md) | task_002_20260325_134858 | analysis | sm90 | cuda-cpp |
| [exp-a-20260325-164413-39849730](../sources/experiences/exp-a-20260325-164413-39849730.md) | ## Task
Write an optimized v2 kernel.cu file for W4A32C8 Q4_0 quantized GEMM (LLaMA-3-8B attention output, N=4096, K=4096). The baseline has speedup=0.0113 on batch_512. Key optimization: improve large batch kernel (M>32) with weight-stationary GEMM - each block processes TILE_N=128 weight columns for all M rows, loading weights once into shared memory and reusing them. Keep M=1 and small batch kernels similar to baseline.

## Goal
Write complete kernel.cu to /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_162528_3bdf3b56/attempts/QG_55/r1/v2/kernel.cu that compiles and runs correctly

## Constraints
- Pure CUDA - no torch/ATen/c10 headers
- extern C entry point: quant_gemm_kernel
- Follow Q4_0 formula: output = activation @ (scale_w * (q_w - 8))^T
- Use vectorized float4 loads for activation
- block_q4_0 struct with uint16_t d (FP16 scale) and uint8_t qs[16] (packed 4-bit)

## Verification
After writing the code, run this command to verify:
```
Compile with nvcc -O3 -arch=sm_80 and test correctness
```

## Critical Context
Task QG_55, quant_gemm, N=4096, K=4096, block_size=32. Baseline speedup=0.0113 on batch_512 (M=512). Need to improve large batch performance.

## Seeded Files
The following files have been placed in your workspace (`/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_162528_3bdf3b56/task_001_20260325_162531/coder_workspace/coder_1774427712_1168`):
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_162528_3bdf3b56/task_001_20260325_162531/coder_workspace/coder_1774427712_1168//home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_162528_3bdf3b56/attempts/QG_55/r1/v1/kernel.cu`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_162528_3bdf3b56/task_001_20260325_162531/coder_workspace/coder_1774427712_1168/task_context.json`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_162528_3bdf3b56/task_001_20260325_162531/coder_workspace/coder_1774427712_1168/iterations.json`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_162528_3bdf3b56/task_001_20260325_162531/coder_workspace/coder_1774427712_1168/round_state.json`
Read them first using their **absolute paths** shown above.

## Workspace & Output Placement
- Your workspace root is: `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_162528_3bdf3b56/task_001_20260325_162531/coder_workspace/coder_1774427712_1168`
- **IMPORTANT**: Seeded files are at `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_162528_3bdf3b56/task_001_20260325_162531/coder_workspace/coder_1774427712_1168/<filename>`, NOT in any subdirectory.
- Use `sandbox_execute(command="ls /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_162528_3bdf3b56/task_001_20260325_162531/coder_workspace/coder_1774427712_1168")` if you need to verify what files exist.
- Prefer writing final outputs in the workspace root.
- If a file like `program.md` is not present, do NOT attempt to read it; rely on the provided context instead.

## Workflow
1. Load relevant skills if specified above
2. Read seeded files to understand existing code
3. Write/modify code to achieve the goal. If the code is long, split it across multiple writes/edits and keep files consistent after each chunk.
4. Run verification command (if provided) to check correctness
5. If verification fails, diagnose and fix
6. Call `finish(result="<see format below>", success=True/False)`

**finish result format** (use these exact section headers):
```
SUMMARY: <one-line description of what you did>
DECISIONS:
- <key decision 1>
- <key decision 2>
ISSUES:
- <known issue or remaining problem>
```
If no decisions or issues, omit that section. | analysis | sm90 | cuda-cpp |
| [exp-a-20260325-185043-1f06c3f2](../sources/experiences/exp-a-20260325-185043-1f06c3f2.md) | ## Task
Write and test an optimized flash attention kernel for Q4_0 KV cache

## Goal
Create a working kernel.cu in /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_182611_214fd041/attempts/FA_14/r2/v1/ that compiles and passes correctness tests. Target speedup over naive baseline (>1.0x).

## Constraints
- kernel.cu must be pure CUDA - no torch/ATen/c10/PYBIND11
- extern "C" void flash_attn_kernel(...) entry point
- Uses Q4_0 block_q4_0 struct (half d + uint8_t qs[16])
- Must handle: batch_size, seq_len=4096, num_heads=28, head_dim=128
- Query is float*, Key/Value cache are block_q4_0*
- Output is float*

## Verification
After writing the code, run this command to verify:
```
cd /home/qinhaiyan/Research/kernelevalplus && python3 llm_kernel_eval.py --attempt /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_182611_214fd041/attempts/FA_14/r2/v1 --definition /home/qinhaiyan/Research/kernelevalplus/definitions/flash_attention/FA_14.yaml --variant default 2>&1 | tail -50
```

## Skills
Load the following skills for domain knowledge: `kernelevalplus-baseline-loop`
Use `skill(name=...)` to load each skill before writing code.

## Critical Context
R1 kernel was 177x slower (0.0056x speedup). Issues: 1) Sequential KV processing, 2) Poor parallelism, 3) No shared memory buffering. Need warp-level parallelism for KV tiles and better memory access patterns.

## Seeded Files
The following files have been placed in your workspace (`/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_182611_214fd041/task_002_20260325_184436/coder_workspace/coder_1774435642_8976`):
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_182611_214fd041/task_002_20260325_184436/coder_workspace/coder_1774435642_8976/r1_kernel.cu`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_182611_214fd041/task_002_20260325_184436/coder_workspace/coder_1774435642_8976/task_context.json`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_182611_214fd041/task_002_20260325_184436/coder_workspace/coder_1774435642_8976/iterations.json`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_182611_214fd041/task_002_20260325_184436/coder_workspace/coder_1774435642_8976/round_state.json`
Read them first using their **absolute paths** shown above.

## Workspace & Output Placement
- Your workspace root is: `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_182611_214fd041/task_002_20260325_184436/coder_workspace/coder_1774435642_8976`
- **IMPORTANT**: Seeded files are at `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_182611_214fd041/task_002_20260325_184436/coder_workspace/coder_1774435642_8976/<filename>`, NOT in any subdirectory.
- Use `sandbox_execute(command="ls /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_182611_214fd041/task_002_20260325_184436/coder_workspace/coder_1774435642_8976")` if you need to verify what files exist.
- Prefer writing final outputs in the workspace root.
- If a file like `program.md` is not present, do NOT attempt to read it; rely on the provided context instead.

## Workflow
1. Load relevant skills if specified above
2. Read seeded files to understand existing code
3. Write/modify code to achieve the goal. If the code is long, split it across multiple writes/edits and keep files consistent after each chunk.
4. Run verification command (if provided) to check correctness
5. If verification fails, diagnose and fix
6. Call `finish(result="<see format below>", success=True/False)`

**finish result format** (use these exact section headers):
```
SUMMARY: <one-line description of what you did>
DECISIONS:
- <key decision 1>
- <key decision 2>
ISSUES:
- <known issue or remaining problem>
```
If no decisions or issues, omit that section. | analysis | sm90 | cuda-cpp |
| [exp-a-20260326-093418-2491cf4d](../sources/experiences/exp-a-20260326-093418-2491cf4d.md) | ## Task
Convert baseline flash_attention kernel to pure CUDA for task FA_15. Remove #include <torch/extension.h>, torch::, at::, c10::. Add extern "C" void flash_attn_kernel(...) entry function with raw pointers. The kernel does flash attention with Q4_0 KV cache dequantization for Qwen2.5-7B.

## Goal
Compile and pass correctness test with unified_test_runner.py. Pure CUDA only, no torch/ATen/c10/PYBIND11.

## Verification
After writing the code, run this command to verify:
```
python llm_kernel_test/unified_test_runner.py --test --attempt-path /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/attempts/FA_15/r1/v1 --definition /home/qinhaiyan/Research/kernelevalplus/definitions/flash_attention/qwen/fp32_flash_attention_qwen2_5_7b_q4_0_cache8192.json
```

## Critical Context
Baseline path: /home/qinhaiyan/Research/kernelevalplus/Baseline/flash_attention/fp32_flash_attention_qwen2_5_7b_q4_0_cache8192.cu. Entry point: flash_attn_kernel. Task FA_15: fp32_flash_attention_qwen2_5_7b_q4_0_cache8192. Use raw float* pointers for Q/K/V, uint8_t* for kv_cache. Must use cudaMalloc/cudaMemcpy for memory management in host code.

## Seeded Files
The following files have been placed in your workspace (`/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/task_001_20260326_092648/coder_workspace/coder_1774488517_9392`):
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/task_001_20260326_092648/coder_workspace/coder_1774488517_9392/task_context.json`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/task_001_20260326_092648/coder_workspace/coder_1774488517_9392/iterations.json`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/task_001_20260326_092648/coder_workspace/coder_1774488517_9392/llm_calls.json`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/task_001_20260326_092648/coder_workspace/coder_1774488517_9392/round_state.json`
Read them first using their **absolute paths** shown above.

## Workspace & Output Placement
- Your workspace root is: `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/task_001_20260326_092648/coder_workspace/coder_1774488517_9392`
- **IMPORTANT**: Seeded files are at `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/task_001_20260326_092648/coder_workspace/coder_1774488517_9392/<filename>`, NOT in any subdirectory.
- Use `sandbox_execute(command="ls /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/task_001_20260326_092648/coder_workspace/coder_1774488517_9392")` if you need to verify what files exist.
- Prefer writing final outputs in the workspace root.
- If a file like `program.md` is not present, do NOT attempt to read it; rely on the provided context instead.

## Workflow
1. Load relevant skills if specified above
2. Read seeded files to understand existing code
3. Write/modify code to achieve the goal. If the code is long, split it across multiple writes/edits and keep files consistent after each chunk.
4. Run verification command (if provided) to check correctness
5. If verification fails, diagnose and fix
6. Call `finish(result="<see format below>", success=True/False)`

**finish result format** (use these exact section headers):
```
SUMMARY: <one-line description of what you did>
DECISIONS:
- <key decision 1>
- <key decision 2>
ISSUES:
- <known issue or remaining problem>
```
If no decisions or issues, omit that section. | analysis | sm90 | cuda-cpp |
| [exp-a-20260326-100018-b14c6b4a](../sources/experiences/exp-a-20260326-100018-b14c6b4a.md) | ## Task
Diagnose and fix CUDA 'invalid argument' errors in the v2 flash attention kernel. The kernel is at /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/attempts/FA_15/r1/v2/kernel.cu. All 3 test batches (batch_1, batch_8, batch_512) fail with CUDA invalid argument. Common causes: shared memory too large, bad kernel launch config, invalid pointer. Check: (1) extern C function signature matches expected entry point 'flash_attn_kernel', (2) shared memory allocation size is within limits, (3) grid dimensions are valid. Fix the kernel and verify it compiles and runs without CUDA errors.

## Goal
Kernel compiles and passes correctness tests without CUDA errors

## Constraints
- Pure CUDA kernel - no torch/ATen/c10/PYBIND11
- extern C void flash_attn_kernel(...) entry point
- Use cudaMalloc/cudaMemcpy for memory management
- Shared memory must be within SM limits

## Verification
After writing the code, run this command to verify:
```
cd /home/qinhaiyan/Research/kernelevalplus && python llm_kernel_test/unified_test_runner.py --test --attempt-path /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/attempts/FA_15/r1/v2 --definition /home/qinhaiyan/Research/kernelevalplus/definitions/flash_attention/qwen/fp32_flash_attention_qwen2_5_7b_q4_0_cache8192.json 2>&1 | grep -E 'PASS|FAIL|correctness'
```

## Skills
Load the following skills for domain knowledge: `cuda-kernel-development`
Use `skill(name=...)` to load each skill before writing code.

## Critical Context
FA_15 flash_attention, v1 baseline passed correctness at 0.0046x speedup, v2 optimizations failed with invalid argument

## Seeded Files
The following files have been placed in your workspace (`/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/task_001_20260326_092648/coder_workspace/coder_1774490239_2800`):
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/task_001_20260326_092648/coder_workspace/coder_1774490239_2800/kernel.cu`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/task_001_20260326_092648/coder_workspace/coder_1774490239_2800/kernel_v1.cu`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/task_001_20260326_092648/coder_workspace/coder_1774490239_2800/task_context.json`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/task_001_20260326_092648/coder_workspace/coder_1774490239_2800/iterations.json`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/task_001_20260326_092648/coder_workspace/coder_1774490239_2800/terminal_output.json`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/task_001_20260326_092648/coder_workspace/coder_1774490239_2800/round_state.json`
Read them first using their **absolute paths** shown above.

## Workspace & Output Placement
- Your workspace root is: `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/task_001_20260326_092648/coder_workspace/coder_1774490239_2800`
- **IMPORTANT**: Seeded files are at `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/task_001_20260326_092648/coder_workspace/coder_1774490239_2800/<filename>`, NOT in any subdirectory.
- Use `sandbox_execute(command="ls /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/task_001_20260326_092648/coder_workspace/coder_1774490239_2800")` if you need to verify what files exist.
- Prefer writing final outputs in the workspace root.
- If a file like `program.md` is not present, do NOT attempt to read it; rely on the provided context instead.

## Workflow
1. Load relevant skills if specified above
2. Read seeded files to understand existing code
3. Write/modify code to achieve the goal. If the code is long, split it across multiple writes/edits and keep files consistent after each chunk.
4. Run verification command (if provided) to check correctness
5. If verification fails, diagnose and fix
6. Call `finish(result="<see format below>", success=True/False)`

**finish result format** (use these exact section headers):
```
SUMMARY: <one-line description of what you did>
DECISIONS:
- <key decision 1>
- <key decision 2>
ISSUES:
- <known issue or remaining problem>
```
If no decisions or issues, omit that section. | analysis | sm90 | cuda-cpp |
| [exp-a-20260328-164241-940e8e92](../sources/experiences/exp-a-20260328-164241-940e8e92.md) | ## Task
Implement tensor core optimization for flash attention Q@K computation. Use WMMA API (cuda_wmma) to accelerate the 128x128 Q@K^T matrix multiply using TensorCores.

## Goal
Achieve >1.0 speedup vs reference baseline. Correctness must pass.

## Constraints
- Pure CUDA kernel
- entry: flash_attn_kernel
- RTX 4090 compute 8.9
- BLOCK_SIZE=256
- head_dim=128, seq_len=512

## Verification
After writing the code, run this command to verify:
```
cd /home/qinhaiyan/kernelevalplus && python llm_kernel_test/unified_test_runner.py --test --attempt-path /home/qinhaiyan/kernelowl/experiments/autoresearch_20260328_162128_590af815/attempts/FA_01/r1/v1 --definition /home/qinhaiyan/kernelevalplus/definitions/cases_verified_rtx4090/flash_attention/llama/fp32_flash_attention_llama3_8b_f16_cache512.json
```

## Skills
Load the following skills for domain knowledge: `cuda-kernel-development`
Use `skill(name=...)` to load each skill before writing code.

## Critical Context
RTX 4090 supports wgmma. Use cuda_wmma API: wmma::load_matrix_sync, wmma::mma_sync, wmma::store_matrix_sync. Tile shapes: 16x16x16 for best performance. May need to convert Q to half or use fragment operations.

## Seeded Files
The following files have been placed in your workspace (`/home/qinhaiyan/kernelowl/experiments/autoresearch_20260328_162128_590af815/task_001_20260328_162129/coder_workspace/coder_1774687013_5680`):
- `/home/qinhaiyan/kernelowl/experiments/autoresearch_20260328_162128_590af815/task_001_20260328_162129/coder_workspace/coder_1774687013_5680/coder_context.json`
- `/home/qinhaiyan/kernelowl/experiments/autoresearch_20260328_162128_590af815/task_001_20260328_162129/coder_workspace/coder_1774687013_5680/kernel.cu`
- `/home/qinhaiyan/kernelowl/experiments/autoresearch_20260328_162128_590af815/task_001_20260328_162129/coder_workspace/coder_1774687013_5680/auto_wrapper.cu`
Read `coder_context.json` first. Read the other seeded files only as needed to inspect or modify the relevant code.

## Editable Targets
These files are already seeded into your workspace and should be treated as the primary implementation targets for this task:
- `/home/qinhaiyan/kernelowl/experiments/autoresearch_20260328_162128_590af815/task_001_20260328_162129/coder_workspace/coder_1774687013_5680/kernel.cu`
- `/home/qinhaiyan/kernelowl/experiments/autoresearch_20260328_162128_590af815/task_001_20260328_162129/coder_workspace/coder_1774687013_5680/auto_wrapper.cu`

## Reference Paths
These paths are references only. Their full contents were not preloaded into the workspace; read them on demand if they are needed for implementation or verification:
- `/home/qinhaiyan/kernelowl/experiments/autoresearch_20260328_162128_590af815/attempts/FA_01/r1/v1`
- `/home/qinhaiyan/kernelevalplus/definitions/cases_verified_rtx4090/flash_attention/llama/fp32_flash_attention_llama3_8b_f16_cache512.json`
- `/home/qinhaiyan/kernelevalplus/Baseline/flash_attention/fp32_flash_attention_llama3_8b_f16_cache512.cu`
- `/home/qinhaiyan/kernelowl/experiments/autoresearch_20260328_162128_590af815/attempts/FA_01/r1/v1/kernel.cu`
- `/home/qinhaiyan/kernelowl/experiments/autoresearch_20260328_162128_590af815/attempts/FA_01/r1/v1/test_results.json`
- `/home/qinhaiyan/kernelevalplus`
- `llm_kernel_test/unified_test_runner.py`
- `/home/qinhaiyan/kernelowl/experiments/autoresearch_20260328_162128_590af815/program.md`
- `/home/qinhaiyan/kernelowl/experiments/autoresearch_20260328_162128_590af815/attempts/FA_01/r1/v1/auto_wrapper.cu`

## Workspace & Output Placement
- Your workspace root is: `/home/qinhaiyan/kernelowl/experiments/autoresearch_20260328_162128_590af815/task_001_20260328_162129/coder_workspace/coder_1774687013_5680`
- **IMPORTANT**: Seeded files are at `/home/qinhaiyan/kernelowl/experiments/autoresearch_20260328_162128_590af815/task_001_20260328_162129/coder_workspace/coder_1774687013_5680/<filename>`, NOT in any subdirectory.
- Use `sandbox_execute(command="ls /home/qinhaiyan/kernelowl/experiments/autoresearch_20260328_162128_590af815/task_001_20260328_162129/coder_workspace/coder_1774687013_5680")` if you need to verify what files exist.
- Prefer writing final outputs in the workspace root.
- If a file like `program.md` is not present, do NOT attempt to read it; rely on the provided context instead.

## Workflow
1. Load relevant skills if specified above
2. Read seeded files to understand existing code
3. Write/modify code to achieve the goal. If the code is long, split it across multiple writes/edits and keep files consistent after each chunk.
4. Run verification command (if provided) to check correctness
5. If verification fails, diagnose and fix
6. Call `finish(result="<see format below>", success=True/False)`

**finish result format** (use these exact section headers):
```
SUMMARY: <one-line description of what you did>
DECISIONS:
- <key decision 1>
- <key decision 2>
ISSUES:
- <known issue or remaining problem>
```
If no decisions or issues, omit that section. | analysis | sm90 | cuda-cpp |
| [exp-a-20260328-165558-4757c191](../sources/experiences/exp-a-20260328-165558-4757c191.md) | ## Task
Add shared memory K/V caching to flash attention kernel. Cache K and V tiles in shared memory to reduce global memory accesses.

## Goal
Improve flash attention speedup from 0.034x. Correctness must pass.

## Constraints
- Pure CUDA kernel
- entry: flash_attn_kernel
- BLOCK_SIZE=256
- head_dim=128, seq_len=512

## Verification
After writing the code, run this command to verify:
```
cd /home/qinhaiyan/kernelevalplus && python llm_kernel_test/unified_test_runner.py --test --attempt-path /home/qinhaiyan/kernelowl/experiments/autoresearch_20260328_162128_590af815/attempts/FA_01/r1/v1 --definition /home/qinhaiyan/kernelevalplus/definitions/cases_verified_rtx4090/flash_attention/llama/fp32_flash_attention_llama3_8b_f16_cache512.json
```

## Skills
Load the following skills for domain knowledge: `cuda-kernel-development`
Use `skill(name=...)` to load each skill before writing code.

## Critical Context
Best so far: 0.0347x with __ldg cache loads. Reference baseline achieves 130 TFLOPS which suggests cuBLAS/TensorCores. Need shared memory tiling.

## Seeded Files
The following files have been placed in your workspace (`/home/qinhaiyan/kernelowl/experiments/autoresearch_20260328_162128_590af815/task_001_20260328_162129/coder_workspace/coder_1774687900_6496`):
- `/home/qinhaiyan/kernelowl/experiments/autoresearch_20260328_162128_590af815/task_001_20260328_162129/coder_workspace/coder_1774687900_6496/coder_context.json`
- `/home/qinhaiyan/kernelowl/experiments/autoresearch_20260328_162128_590af815/task_001_20260328_162129/coder_workspace/coder_1774687900_6496/kernel.cu`
- `/home/qinhaiyan/kernelowl/experiments/autoresearch_20260328_162128_590af815/task_001_20260328_162129/coder_workspace/coder_1774687900_6496/auto_wrapper.cu`
Read `coder_context.json` first. Read the other seeded files only as needed to inspect or modify the relevant code.

## Editable Targets
These files are already seeded into your workspace and should be treated as the primary implementation targets for this task:
- `/home/qinhaiyan/kernelowl/experiments/autoresearch_20260328_162128_590af815/task_001_20260328_162129/coder_workspace/coder_1774687900_6496/kernel.cu`
- `/home/qinhaiyan/kernelowl/experiments/autoresearch_20260328_162128_590af815/task_001_20260328_162129/coder_workspace/coder_1774687900_6496/auto_wrapper.cu`

## Reference Paths
These paths are references only. Their full contents were not preloaded into the workspace; read them on demand if they are needed for implementation or verification:
- `/home/qinhaiyan/kernelowl/experiments/autoresearch_20260328_162128_590af815/attempts/FA_01/r1/v1`
- `/home/qinhaiyan/kernelevalplus/definitions/cases_verified_rtx4090/flash_attention/llama/fp32_flash_attention_llama3_8b_f16_cache512.json`
- `/home/qinhaiyan/kernelevalplus/Baseline/flash_attention/fp32_flash_attention_llama3_8b_f16_cache512.cu`
- `/home/qinhaiyan/kernelevalplus`
- `llm_kernel_test/unified_test_runner.py`
- `/home/qinhaiyan/kernelowl/experiments/autoresearch_20260328_162128_590af815/attempts/FA_01/r1/v1/kernel.cu`
- `/home/qinhaiyan/kernelevalplus/llm_kernel_test/unified_test_runner.py`
- `s/__launch_bounds__`
- `s/__ldcs/__ldg/g`
- `/home/qinhaiyan/kernelowl/experiments/autoresearch_20260328_162128_590af815/attempts/FA_01/r1/v1/auto_wrapper.cu`

## Workspace & Output Placement
- Your workspace root is: `/home/qinhaiyan/kernelowl/experiments/autoresearch_20260328_162128_590af815/task_001_20260328_162129/coder_workspace/coder_1774687900_6496`
- **IMPORTANT**: Seeded files are at `/home/qinhaiyan/kernelowl/experiments/autoresearch_20260328_162128_590af815/task_001_20260328_162129/coder_workspace/coder_1774687900_6496/<filename>`, NOT in any subdirectory.
- Use `sandbox_execute(command="ls /home/qinhaiyan/kernelowl/experiments/autoresearch_20260328_162128_590af815/task_001_20260328_162129/coder_workspace/coder_1774687900_6496")` if you need to verify what files exist.
- Prefer writing final outputs in the workspace root.
- If a file like `program.md` is not present, do NOT attempt to read it; rely on the provided context instead.

## Workflow
1. Load relevant skills if specified above
2. Read seeded files to understand existing code
3. Write/modify code to achieve the goal. If the code is long, split it across multiple writes/edits and keep files consistent after each chunk.
4. Run verification command (if provided) to check correctness
5. If verification fails, diagnose and fix
6. Call `finish(result="<see format below>", success=True/False)`

**finish result format** (use these exact section headers):
```
SUMMARY: <one-line description of what you did>
DECISIONS:
- <key decision 1>
- <key decision 2>
ISSUES:
- <known issue or remaining problem>
```
If no decisions or issues, omit that section. | analysis | sm90 | cuda-cpp |
| [exp-a-20260506-180001-cuda-compile-patterns](../sources/experiences/exp-a-20260506-180001-cuda-compile-patterns.md) | CUDA compile error patterns from SOL-ExecBench experiments and their resolution | analysis | sm90 | cuda-cpp |
| [exp-i-20260312-180015-ac97b29c](../sources/experiences/exp-i-20260312-180015-ac97b29c.md) | fp32_flash_attention_llama3_8b_q8_0_cache8192 | implementation | sm90 | cuda-cpp |
| [exp-i-20260313-003922-cc397de3](../sources/experiences/exp-i-20260313-003922-cc397de3.md) | fp32_flash_attention_qwen2_5_7b_f16_cache512 | implementation | sm90 | cuda-cpp |
| [exp-i-20260316-173916-d15e5fbc](../sources/experiences/exp-i-20260316-173916-d15e5fbc.md) | fp32_flash_attention_llama3_8b_f16_cache4096 | implementation | sm90 | cuda-cpp |
| [exp-i-20260316-180236-cf8f502a](../sources/experiences/exp-i-20260316-180236-cf8f502a.md) | fp32_flash_attention_llama3_8b_f16_cache512 | implementation | sm90 | cuda-cpp |
| [exp-i-20260316-183421-cf8f502a](../sources/experiences/exp-i-20260316-183421-cf8f502a.md) | fp32_flash_attention_llama3_8b_f16_cache512 | implementation | sm90 | cuda-cpp |
| [exp-i-20260317-010854-2b9f12e5](../sources/experiences/exp-i-20260317-010854-2b9f12e5.md) | fp32_flash_attention_llama3_8b_q8_0_cache512 | implementation | sm90 | cuda-cpp |
| [exp-i-20260317-030058-ac97b29c](../sources/experiences/exp-i-20260317-030058-ac97b29c.md) | fp32_flash_attention_llama3_8b_q8_0_cache8192 | implementation | sm90 | cuda-cpp |
| [exp-i-20260506-flash-attention-kernel-eval-contract](../sources/experiences/exp-i-20260506-flash-attention-kernel-eval-contract.md) | KernelEval flash_attention CUDA kernel implementation contract | implementation | sm90 | cuda-cpp |
| [exp-i-20260519-0001-gqa-paged-decode-architecture](../sources/experiences/exp-i-20260519-0001-gqa-paged-decode-architecture.md) | GQA paged decode attention: architecture, kernel design, and correct run() signature | implementation | sm90 | cuda-cpp |
| [exp-i-20260519-0002-gqa-compilation-checklist](../sources/experiences/exp-i-20260519-0002-gqa-compilation-checklist.md) | GQA paged decode: compilation checklist for CUDA kernels | implementation | sm90 | cuda-cpp |
| [exp-i-20260519-0003-gqa-minimal-skeleton](../sources/experiences/exp-i-20260519-0003-gqa-minimal-skeleton.md) | GQA paged decode: minimal compile-able skeleton for new implementations | implementation | sm90 | cuda-cpp |
| [exp-o-20260323-154320-367ba2bf](../sources/experiences/exp-o-20260323-154320-367ba2bf.md) | flash_attention_FA_01 | optimization | sm90 | cuda-cpp |
| [exp-o-20260324-112630-a402097a](../sources/experiences/exp-o-20260324-112630-a402097a.md) | fp32_flash_attention_llama3_8b_q8_0_cache512 | optimization | sm90 | cuda-cpp |
| [exp-o-20260324-143500-0cfacb66](../sources/experiences/exp-o-20260324-143500-0cfacb66.md) | fp32_flash_attention_qwen2_5_7b_f16_cache8192 | optimization | sm90 | cuda-cpp |
| [exp-o-20260324-143929-1c0bed37](../sources/experiences/exp-o-20260324-143929-1c0bed37.md) | FA_12 flash attention optimization | optimization | sm90 | cuda-cpp |
| [exp-o-20260324-144336-5af081c5](../sources/experiences/exp-o-20260324-144336-5af081c5.md) | FA_12 r2 v4 | optimization | sm90 | cuda-cpp |
| [exp-o-20260324-145304-a090876f](../sources/experiences/exp-o-20260324-145304-a090876f.md) | fp32_flash_attention_qwen2_5_7b_f16_cache8192 | optimization | sm90 | cuda-cpp |
| [exp-o-20260324-151917-24a573ac](../sources/experiences/exp-o-20260324-151917-24a573ac.md) | fp32_flash_attention_qwen2_5_7b_f16_cache8192 | optimization | sm90 | cuda-cpp |
| [exp-o-20260328-074026-c0ff7e66](../sources/experiences/exp-o-20260328-074026-c0ff7e66.md) | fp32_flash_attention_llama3_8b_f16_cache8192 | optimization | sm90 | cuda-cpp |
| [exp-o-20260328-163155-7f76b595](../sources/experiences/exp-o-20260328-163155-7f76b595.md) | fp32_flash_attention_llama3_8b_f16_cache512 | optimization | sm90 | cuda-cpp |
| [exp-o-20260506-flash-attention-tensor-core](../sources/experiences/exp-o-20260506-flash-attention-tensor-core.md) | Flash attention must leverage Tensor Cores for meaningful speedup | optimization | sm90 | cuda-cpp |
| [exp-o-20260507-flash-attention-tensor-core-no-speedup](../sources/experiences/exp-o-20260507-flash-attention-tensor-core-no-speedup.md) | All flash_attention kernels pass correctness but achieve 0.0025x-0.0425x speedup due to scalar-only compute | optimization | sm90 | cuda-cpp |
| [exp-o-20260529-0001-gqa-split-kv-parallelism](../sources/experiences/exp-o-20260529-0001-gqa-split-kv-parallelism.md) | GQA paged decode: split-KV parallelism is mandatory for competitive performance | optimization | sm90 | cuda-cpp |
| [exp-o-20260529-0002-gqa-single-warp-antipattern](../sources/experiences/exp-o-20260529-0002-gqa-single-warp-antipattern.md) | GQA paged decode: single-warp (32 threads) kernel is a fatal anti-pattern | optimization | sm90 | cuda-cpp |
| [exp-r-20260317-145541-fecbc334](../sources/experiences/exp-r-20260317-145541-fecbc334.md) | Implement attention operator using Metal on macOS with kernel.metal and metal_test.mm | repair | sm90 | cuda-cpp |
| [exp-r-20260506-180000-cpp-pytorch-named-params](../sources/experiences/exp-r-20260506-180000-cpp-pytorch-named-params.md) | C++ PyTorch API named parameter error in CUDA kernels | repair | sm90 | cuda-cpp |
| [exp-r-20260506-180001-pybind-module-placement](../sources/experiences/exp-r-20260506-180001-pybind-module-placement.md) | PYBIND11_MODULE must be in .cpp file compiled by g++/clang++, not in .cu file compiled by nvcc | repair | sm90 | cuda-cpp |
| [exp-r-20260506-180003-dps-signature-mismatch](../sources/experiences/exp-r-20260506-180003-dps-signature-mismatch.md) | DPS signature mismatch - non-void run() vs void run() with trailing output parameters | repair | sm90 | cuda-cpp |
| [exp-r-20260506-180007-cuda-syntax-in-cpp](../sources/experiences/exp-r-20260506-180007-cuda-syntax-in-cpp.md) | CUDA syntax (__global__, <<<>>>) used in .cpp files compiled by g++/clang++ | repair | sm90 | cuda-cpp |
| [exp-r-20260506-flash-attention-compile-linker](../sources/experiences/exp-r-20260506-flash-attention-compile-linker.md) | Flash attention CUDA kernel linker error: undefined symbol flash_attn_kernel | repair | sm90 | cuda-cpp |
| [exp-r-20260506-verification-dead-loop](../sources/experiences/exp-r-20260506-verification-dead-loop.md) | Verification pipeline dead loop: repeated identical blocked state until step exhaustion | repair | sm90 | cuda-cpp |
| [exp-r-20260507-correctness-vs-performance-passing](../sources/experiences/exp-r-20260507-correctness-vs-performance-passing.md) | KernelEval verification_status=passed does not guarantee speedup > 1.0x - FA_12 passed with 0.7395x speedup | repair | sm90 | cuda-cpp |
| [exp-r-20260507-skill-suite-mismatch-blocked](../sources/experiences/exp-r-20260507-skill-suite-mismatch-blocked.md) | Skill suite mismatch blocks R2: sol_execbench skill used on kerneleval task | repair | sm90 | cuda-cpp |
| [exp-r-20260507-verification-dead-loop-r2](../sources/experiences/exp-r-20260507-verification-dead-loop-r2.md) | Verification dead loop in R1 blocks unverified, then R2 inherits failure | repair | sm90 | cuda-cpp |
| [exp-r-20260517-200017-flashinfer-cuda-syntax](../sources/experiences/exp-r-20260517-200017-flashinfer-cuda-syntax.md) | FlashInfer-Bench GQA paged decode kernel compilation errors | repair | sm90 | cuda-cpp |
| [exp-r-20260518-0001-gqa-cuda-syntax-in-cpp](../sources/experiences/exp-r-20260518-0001-gqa-cuda-syntax-in-cpp.md) | GQA paged decode: __nv_bfloat16 and CUDA types in .cpp files | repair | sm90 | cuda-cpp |
| [exp-r-20260518-0002-gqa-source-truncation](../sources/experiences/exp-r-20260518-0002-gqa-source-truncation.md) | GQA paged decode: source code truncation causes syntax errors after sol_execbench_update_sources | repair | sm90 | cuda-cpp |
| [exp-r-20260518-0003-gqa-stream-api](../sources/experiences/exp-r-20260518-0003-gqa-stream-api.md) | GQA paged decode: wrong CUDA stream API (c10 vs at) and missing cuda_runtime.h | repair | sm90 | cuda-cpp |
| [exp-r-20260529-0001-gqa-lse-formula-error](../sources/experiences/exp-r-20260529-0001-gqa-lse-formula-error.md) | GQA paged decode: incorrect base-2 LSE formula causes systematic ~20% numerical error | repair | sm90 | cuda-cpp |
| [exp-r-20260529-0002-verification-timeout-dead-loop](../sources/experiences/exp-r-20260529-0002-verification-timeout-dead-loop.md) | Agent retries sol-execbench verification 30+ times after timeout without modifying kernel | repair | sm90 | cuda-cpp |
| [exp-r-20260529-0004-mcp-allowed-dirs-bind-mount](../sources/experiences/exp-r-20260529-0004-mcp-allowed-dirs-bind-mount.md) | MCP filesystem server rejects /home/ paths when allowed_dirs only contains /data/ bind-mount spelling | repair | sm90 | cuda-cpp |

## conv2d

| ID | Title | Type | Architectures | Languages |
|----|-------|------|--------------|-----------|
| [exp-r-20260317-124730-314f1971](../sources/experiences/exp-r-20260317-124730-314f1971.md) | Metal convolution implementation on macOS | repair | sm90 | cuda-cpp |

## flash-attention

| ID | Title | Type | Architectures | Languages |
|----|-------|------|--------------|-----------|
| [exp-i-20260506-flash-attention-kernel-eval-contract](../sources/experiences/exp-i-20260506-flash-attention-kernel-eval-contract.md) | KernelEval flash_attention CUDA kernel implementation contract | implementation | sm90 | cuda-cpp |
| [exp-o-20260506-flash-attention-tensor-core](../sources/experiences/exp-o-20260506-flash-attention-tensor-core.md) | Flash attention must leverage Tensor Cores for meaningful speedup | optimization | sm90 | cuda-cpp |
| [exp-o-20260507-flash-attention-tensor-core-no-speedup](../sources/experiences/exp-o-20260507-flash-attention-tensor-core-no-speedup.md) | All flash_attention kernels pass correctness but achieve 0.0025x-0.0425x speedup due to scalar-only compute | optimization | sm90 | cuda-cpp |
| [exp-r-20260506-flash-attention-compile-linker](../sources/experiences/exp-r-20260506-flash-attention-compile-linker.md) | Flash attention CUDA kernel linker error: undefined symbol flash_attn_kernel | repair | sm90 | cuda-cpp |
| [exp-r-20260506-verification-dead-loop](../sources/experiences/exp-r-20260506-verification-dead-loop.md) | Verification pipeline dead loop: repeated identical blocked state until step exhaustion | repair | sm90 | cuda-cpp |
| [exp-r-20260507-correctness-vs-performance-passing](../sources/experiences/exp-r-20260507-correctness-vs-performance-passing.md) | KernelEval verification_status=passed does not guarantee speedup > 1.0x - FA_12 passed with 0.7395x speedup | repair | sm90 | cuda-cpp |
| [exp-r-20260507-skill-suite-mismatch-blocked](../sources/experiences/exp-r-20260507-skill-suite-mismatch-blocked.md) | Skill suite mismatch blocks R2: sol_execbench skill used on kerneleval task | repair | sm90 | cuda-cpp |
| [exp-r-20260507-verification-dead-loop-r2](../sources/experiences/exp-r-20260507-verification-dead-loop-r2.md) | Verification dead loop in R1 blocks unverified, then R2 inherits failure | repair | sm90 | cuda-cpp |

## gemm

| ID | Title | Type | Architectures | Languages |
|----|-------|------|--------------|-----------|
| [exp-a-20260325-170222-ee5351e3](../sources/experiences/exp-a-20260325-170222-ee5351e3.md) | ## Task
Write a CUDA kernel for Q4_0 quantized GEMM that achieves much better performance than the baseline (currently only 0.6% of baseline). The kernel computes C = A @ W^T where A(M,K) is FP32 activation, W(N,K/32) is Q4_0 quantized weights.

## Goal
Achieve >10x speedup over baseline performance of 1.18 TFLOPS. Must be correct (NMSE < 0.05).

## Constraints
- Pure CUDA kernel - no torch/ATen/c10/PYBIND11
- N=4096, K=4096, M=1 to 512, block_size=32
- Q4_0 format: struct with uint16_t d (scale) and uint8_t qs[16] (16 values each holding 2 4-bit quantized values with offset-8)
- extern "C" void quant_gemm_kernel(...) entry point

## Verification
After writing the code, run this command to verify:
```
Run unified_test_runner.py with --test --variant W4A32C8
```

## Skills
Load the following skills for domain knowledge: `cuda-kernel-development`
Use `skill(name=...)` to load each skill before writing code.

## Critical Context
Current v2 kernel only achieves 0.6% of baseline (0.007 TFLOPS). The key issue is insufficient parallelism: with M=1, the kernel underutilizes GPU resources. Need a fundamentally different approach that better utilizes all threads.

## Seeded Files
The following files have been placed in your workspace (`/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_162528_3bdf3b56/task_001_20260325_162531/coder_workspace/coder_1774428992_9600`):
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_162528_3bdf3b56/task_001_20260325_162531/coder_workspace/coder_1774428992_9600/task_context.json`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_162528_3bdf3b56/task_001_20260325_162531/coder_workspace/coder_1774428992_9600/iterations.json`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_162528_3bdf3b56/task_001_20260325_162531/coder_workspace/coder_1774428992_9600/terminal_output.json`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_162528_3bdf3b56/task_001_20260325_162531/coder_workspace/coder_1774428992_9600/round_state.json`
Read them first using their **absolute paths** shown above.

## Workspace & Output Placement
- Your workspace root is: `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_162528_3bdf3b56/task_001_20260325_162531/coder_workspace/coder_1774428992_9600`
- **IMPORTANT**: Seeded files are at `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_162528_3bdf3b56/task_001_20260325_162531/coder_workspace/coder_1774428992_9600/<filename>`, NOT in any subdirectory.
- Use `sandbox_execute(command="ls /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_162528_3bdf3b56/task_001_20260325_162531/coder_workspace/coder_1774428992_9600")` if you need to verify what files exist.
- Prefer writing final outputs in the workspace root.
- If a file like `program.md` is not present, do NOT attempt to read it; rely on the provided context instead.

## Workflow
1. Load relevant skills if specified above
2. Read seeded files to understand existing code
3. Write/modify code to achieve the goal. If the code is long, split it across multiple writes/edits and keep files consistent after each chunk.
4. Run verification command (if provided) to check correctness
5. If verification fails, diagnose and fix
6. Call `finish(result="<see format below>", success=True/False)`

**finish result format** (use these exact section headers):
```
SUMMARY: <one-line description of what you did>
DECISIONS:
- <key decision 1>
- <key decision 2>
ISSUES:
- <known issue or remaining problem>
```
If no decisions or issues, omit that section. | analysis | sm90 | cuda-cpp |
| [exp-a-20260325-172649-39d03bc4](../sources/experiences/exp-a-20260325-172649-39d03bc4.md) | ## Task
Run the KernelEvalPlus unified test runner on the existing QG_55 r1 v2 kernel to compile and benchmark it

## Goal
Get compile success status and speedup metrics for kernel at /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_162528_3bdf3b56/attempts/QG_55/r1/v2/kernel.cu

## Constraints
- Use the correct test runner command with --attempt-path or --attempt-id
- Capture all compile output and performance metrics
- Report back: compile_success=true/false, speedup ratio, baseline vs optimized tflops/gflops

## Verification
After writing the code, run this command to verify:
```
Extract speedup metrics from test output
```

## Critical Context
Task QG_55 is quant_gemm for W4A32C8 Q4_0 GEMM. N=4096, K=4096, block_size=32. The unified test runner needs --attempt-path pointing to the attempt directory.

## Seeded Files
The following files have been placed in your workspace (`/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_162528_3bdf3b56/task_002_20260325_170708/coder_workspace/coder_1774430716_2784`):
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_162528_3bdf3b56/task_002_20260325_170708/coder_workspace/coder_1774430716_2784/task_context.json`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_162528_3bdf3b56/task_002_20260325_170708/coder_workspace/coder_1774430716_2784/iterations.json`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_162528_3bdf3b56/task_002_20260325_170708/coder_workspace/coder_1774430716_2784/round_state.json`
Read them first using their **absolute paths** shown above.

## Workspace & Output Placement
- Your workspace root is: `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_162528_3bdf3b56/task_002_20260325_170708/coder_workspace/coder_1774430716_2784`
- **IMPORTANT**: Seeded files are at `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_162528_3bdf3b56/task_002_20260325_170708/coder_workspace/coder_1774430716_2784/<filename>`, NOT in any subdirectory.
- Use `sandbox_execute(command="ls /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_162528_3bdf3b56/task_002_20260325_170708/coder_workspace/coder_1774430716_2784")` if you need to verify what files exist.
- Prefer writing final outputs in the workspace root.
- If a file like `program.md` is not present, do NOT attempt to read it; rely on the provided context instead.

## Workflow
1. Load relevant skills if specified above
2. Read seeded files to understand existing code
3. Write/modify code to achieve the goal. If the code is long, split it across multiple writes/edits and keep files consistent after each chunk.
4. Run verification command (if provided) to check correctness
5. If verification fails, diagnose and fix
6. Call `finish(result="<see format below>", success=True/False)`

**finish result format** (use these exact section headers):
```
SUMMARY: <one-line description of what you did>
DECISIONS:
- <key decision 1>
- <key decision 2>
ISSUES:
- <known issue or remaining problem>
```
If no decisions or issues, omit that section. | analysis | sm90 | cuda-cpp |
| [exp-a-20260326-133610-3e7f549b](../sources/experiences/exp-a-20260326-133610-3e7f549b.md) | 实现一个量化的GEMM算子:
            - weight是Q4_0格式
            - activation是Q8_1格式
            - 输入activation是fp32需要量化
            - 输出需要反量化回fp32 | analysis | sm90 | cuda-cpp |
| [exp-a-20260328-071624-3e7f549b](../sources/experiences/exp-a-20260328-071624-3e7f549b.md) | 实现一个量化的GEMM算子:
            - weight是Q4_0格式
            - activation是Q8_1格式
            - 输入activation是fp32需要量化
            - 输出需要反量化回fp32 | analysis | sm90 | cuda-cpp |
| [exp-a-20260328-074031-3e7f549b](../sources/experiences/exp-a-20260328-074031-3e7f549b.md) | 实现一个量化的GEMM算子:
            - weight是Q4_0格式
            - activation是Q8_1格式
            - 输入activation是fp32需要量化
            - 输出需要反量化回fp32 | analysis | sm90 | cuda-cpp |
| [exp-a-20260328-074108-3e7f549b](../sources/experiences/exp-a-20260328-074108-3e7f549b.md) | 实现一个量化的GEMM算子:
            - weight是Q4_0格式
            - activation是Q8_1格式
            - 输入activation是fp32需要量化
            - 输出需要反量化回fp32 | analysis | sm90 | cuda-cpp |
| [exp-a-20260328-074205-3e7f549b](../sources/experiences/exp-a-20260328-074205-3e7f549b.md) | 实现一个量化的GEMM算子:
            - weight是Q4_0格式
            - activation是Q8_1格式
            - 输入activation是fp32需要量化
            - 输出需要反量化回fp32 | analysis | sm90 | cuda-cpp |
| [exp-a-20260526-200006-cublas-gemm-convergence](../sources/experiences/exp-a-20260526-200006-cublas-gemm-convergence.md) | SOL-ExecBench GEMM: optimization convergence — cuBLAS 0.99x+ means switch to cublasLt with proper config | analysis | sm90 | cuda-cpp |
| [exp-i-20260508-120001-sol-execbench-file-template](../sources/experiences/exp-i-20260508-120001-sol-execbench-file-template.md) | exp-i-20260508-120001-sol-execbench-file-template | implementation | sm90 | cuda-cpp |
| [exp-i-20260517-200010-int8-gemm-template](../sources/experiences/exp-i-20260517-200010-int8-gemm-template.md) | INT8 GEMM kernel implementation template for SOL-ExecBench | implementation | sm90 | cuda-cpp |
| [exp-i-20260517-200011-bf16-gemm-template](../sources/experiences/exp-i-20260517-200011-bf16-gemm-template.md) | BF16 GEMM kernel implementation template for SOL-ExecBench | implementation | sm90 | cuda-cpp |
| [exp-i-20260517-200012-sol-execbench-cpp-template](../sources/experiences/exp-i-20260517-200012-sol-execbench-cpp-template.md) | SOL-ExecBench cuda_cpp solution.json and source file template | implementation | sm90 | cuda-cpp |
| [exp-i-20260527-080001-cublaslt-fp16-gemm-best-config](../sources/experiences/exp-i-20260527-080001-cublaslt-fp16-gemm-best-config.md) | SOL-ExecBench GEMM: cublasLt FP16 reference implementation achieving 0.9999x | implementation | sm90 | cuda-cpp |
| [exp-o-20260324-234001-1ba7a113](../sources/experiences/exp-o-20260324-234001-1ba7a113.md) | w4a32c8_q4_0_fp32_int8_llama3_8b_att_out_n4096_k4096 | optimization | sm90 | cuda-cpp |
| [exp-o-20260430-001001-gemm-tile01](../sources/experiences/exp-o-20260430-001001-gemm-tile01.md) | CUTLASS GEMM tile size selection by problem shape | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-20260430-001002-gemm-splitk](../sources/experiences/exp-o-20260430-001002-gemm-splitk.md) | Split-K parallelization for large-K GEMM | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-20260430-001003-gemm-fp8evt](../sources/experiences/exp-o-20260430-001003-gemm-fp8evt.md) | Fused GEMM epilogue with scaling and bias via CUTLASS EVT | optimization | sm100 | cuda-cpp, cute-dsl |
| [exp-o-20260430-001004-gemm-smbudget](../sources/experiences/exp-o-20260430-001004-gemm-smbudget.md) | GEMM shared memory budget and stage count tuning across SM architectures | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-20260430-001005-gemm-layout](../sources/experiences/exp-o-20260430-001005-gemm-layout.md) | GEMM data layout handling: NN vs NT without runtime transpose | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-20260430-001006-gemm-precision](../sources/experiences/exp-o-20260430-001006-gemm-precision.md) | GEMM precision and accumulator selection: BF16 vs FP16 vs INT8 vs FP8 | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-20260430-001007-gemm-autotune](../sources/experiences/exp-o-20260430-001007-gemm-autotune.md) | GEMM autotuning pipeline: per-model per-GPU tactic selection | optimization | sm90 | cuda-cpp |
| [exp-o-20260430-200001-gemm-cutlass-fallback](../sources/experiences/exp-o-20260430-200001-gemm-cutlass-fallback.md) | SOL-ExecBench BF16 dense GEMM: fallback from CUTLASS to cuBLAS | optimization | sm90 | cuda-cpp |
| [exp-o-20260430-200002-gemm-cublaslt-risk](../sources/experiences/exp-o-20260430-200002-gemm-cublaslt-risk.md) | SOL-ExecBench BF16 GEMM: cuBLASLt is a risky first fallback | optimization | sm90 | cuda-cpp |
| [exp-o-20260430-200003-gemm-handle-reuse-measure](../sources/experiences/exp-o-20260430-200003-gemm-handle-reuse-measure.md) | SOL-ExecBench BF16 GEMM: handle reuse is not guaranteed to improve performance | optimization | sm90 | cuda-cpp |
| [exp-o-20260502-180013-int8-gemm-cublas-baseline](../sources/experiences/exp-o-20260502-180013-int8-gemm-cublas-baseline.md) | SOL-ExecBench INT8 GEMM: cuBLAS baseline strategy | optimization | sm90 | cuda-cpp |
| [exp-o-20260506-150001-int8-gemm-dp4a-vectorized](../sources/experiences/exp-o-20260506-150001-int8-gemm-dp4a-vectorized.md) | SOL-ExecBench INT8 GEMM: DP4A vectorized implementation | optimization | sm90 | cuda-cpp |
| [exp-o-20260506-150002-int8-gemm-cublas-persistent-handle](../sources/experiences/exp-o-20260506-150002-int8-gemm-cublas-persistent-handle.md) | SOL-ExecBench INT8 GEMM: cuBLAS with persistent handle | optimization | sm90 | cuda-cpp |
| [exp-o-20260506-150003-int8-gemm-best-practices](../sources/experiences/exp-o-20260506-150003-int8-gemm-best-practices.md) | SOL-ExecBench INT8 GEMM: comprehensive best practices | optimization | sm90 | cuda-cpp |
| [exp-o-20260506-150004-bf16-gemm-cublas-tensor-core](../sources/experiences/exp-o-20260506-150004-bf16-gemm-cublas-tensor-core.md) | SOL-ExecBench BF16 GEMM: cuBLAS Tensor Core optimization for small batch | optimization | sm90 | cuda-cpp |
| [exp-o-20260508-120001-cublas-row-major-mapping](../sources/experiences/exp-o-20260508-120001-cublas-row-major-mapping.md) | exp-o-20260508-120001-cublas-row-major-mapping | optimization | sm90 | cuda-cpp |
| [exp-o-20260508-120002-cublas-handle-persistence](../sources/experiences/exp-o-20260508-120002-cublas-handle-persistence.md) | exp-o-20260508-120002-cublas-handle-persistence | optimization | sm90 | cuda-cpp |
| [exp-o-20260508-120003-int8-gemm-prefer-cublas](../sources/experiences/exp-o-20260508-120003-int8-gemm-prefer-cublas.md) | exp-o-20260508-120003-int8-gemm-prefer-cublas | optimization | sm90 | cuda-cpp |
| [exp-o-20260508-120004-bf16-fp32-accumulation](../sources/experiences/exp-o-20260508-120004-bf16-fp32-accumulation.md) | exp-o-20260508-120004-bf16-fp32-accumulation | optimization | sm90 | cuda-cpp |
| [exp-o-20260508-120005-small-matrix-torch-mm](../sources/experiences/exp-o-20260508-120005-small-matrix-torch-mm.md) | exp-o-20260508-120005-small-matrix-torch-mm | optimization | sm90 | python |
| [exp-o-20260508-120006-problem-size-speedup](../sources/experiences/exp-o-20260508-120006-problem-size-speedup.md) | exp-o-20260508-120006-problem-size-speedup | optimization | sm90 | cuda-cpp |
| [exp-o-20260508-160201-benchmark-timing-hygiene](../sources/experiences/exp-o-20260508-160201-benchmark-timing-hygiene.md) | exp-o-20260508-160201-benchmark-timing-hygiene | optimization | sm90 | cuda-cpp |
| [exp-o-20260508-160202-gemm-strategy-dispatch-by-shape](../sources/experiences/exp-o-20260508-160202-gemm-strategy-dispatch-by-shape.md) | exp-o-20260508-160202-gemm-strategy-dispatch-by-shape | optimization | sm90 | cuda-cpp |
| [exp-o-20260508-180001-bf16-cublas-swap-mapping](../sources/experiences/exp-o-20260508-180001-bf16-cublas-swap-mapping.md) | exp-o-20260508-180001-bf16-cublas-swap-mapping | optimization | sm90 | cuda-cpp |
| [exp-o-20260513-100001-int8-gemm-cutlass-fused-epilogue](../sources/experiences/exp-o-20260513-100001-int8-gemm-cutlass-fused-epilogue.md) | SOL-ExecBench INT8 GEMM: CUTLASS EpilogueVisitorPerRowPerCol fused dequantize pattern | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-20260513-100002-int8-gemm-imma-tensor-core-tactics](../sources/experiences/exp-o-20260513-100002-int8-gemm-imma-tensor-core-tactics.md) | SOL-ExecBench INT8 GEMM: IMMA Tensor Core instructions and tactic autotuning | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-20260513-100003-int8-gemm-cublaslt-fallback-dequant](../sources/experiences/exp-o-20260513-100003-int8-gemm-cublaslt-fallback-dequant.md) | SOL-ExecBench INT8 GEMM: cuBLAS + dequant kernel fallback with correct parameter mapping | optimization | sm90 | cuda-cpp |
| [exp-o-20260513-100005-bf16-gemm-cublas-tensor-core](../sources/experiences/exp-o-20260513-100005-bf16-gemm-cublas-tensor-core.md) | SOL-ExecBench BF16 GEMM: cuBLAS cublasGemmEx with CUDA_R_16BF achieves 1.8x-4.5x speedup | optimization | sm90 | cuda-cpp |
| [exp-o-20260514-100001-int8-gemm-cublas-dequant-complete-template](../sources/experiences/exp-o-20260514-100001-int8-gemm-cublas-dequant-complete-template.md) | SOL-ExecBench INT8 GEMM: complete working cuBLAS + dequant template for all shapes | optimization | sm90 | cuda-cpp |
| [exp-o-20260514-100003-int8-gemm-strategy-dispatch-by-shape-data](../sources/experiences/exp-o-20260514-100003-int8-gemm-strategy-dispatch-by-shape-data.md) | SOL-ExecBench INT8 GEMM: implementation strategy dispatch by matrix shape with experimental data | optimization | sm90 | cuda-cpp |
| [exp-o-20260514-100004-int8-gemm-multiround-seed-solution](../sources/experiences/exp-o-20260514-100004-int8-gemm-multiround-seed-solution.md) | SOL-ExecBench INT8 GEMM: multi-round optimization must consume seed solution from prior round | optimization | sm90 | cuda-cpp |
| [exp-o-20260518-0001-gemm-library-first](../sources/experiences/exp-o-20260518-0001-gemm-library-first.md) | GEMM/MatMul tasks: always prefer library path (cuBLAS/CUTLASS) over handwritten CUDA kernels | optimization | sm90 | cuda-cpp |
| [exp-o-20260518-0002-gemm-naive-kernel-diagnosis](../sources/experiences/exp-o-20260518-0002-gemm-naive-kernel-diagnosis.md) | Diagnose naive CUDA kernel characteristics when speedup << 0.1x | optimization | sm90 | cuda-cpp |
| [exp-o-20260518-0003-gemm-structural-requirements](../sources/experiences/exp-o-20260518-0003-gemm-structural-requirements.md) | Minimum structural requirements for handwritten CUDA GEMM to achieve >0.5x speedup | optimization | sm90 | cuda-cpp |
| [exp-o-20260528-113602-flashinfer-gemm-baseline-rollback-policy](../sources/experiences/exp-o-20260528-113602-flashinfer-gemm-baseline-rollback-policy.md) | Use verified cuBLAS baseline as rollback anchor for unstable WMMA rounds | optimization | sm90 | cuda-cpp |
| [exp-r-20260317-121437-fb3f442e](../sources/experiences/exp-r-20260317-121437-fb3f442e.md) | Metal matrix multiplication implementation on macOS | repair | sm90 | cuda-cpp |
| [exp-r-20260318-111110-7d189321](../sources/experiences/exp-r-20260318-111110-7d189321.md) | Implement matrix multiplication in Metal (MSL) for macOS with test harness | repair | sm90 | cuda-cpp |
| [exp-r-20260318-115544-29d6f34e](../sources/experiences/exp-r-20260318-115544-29d6f34e.md) | kernelbench level_1 task_1: Square matrix multiplication C = A * B with N=2048 | repair | sm90 | cuda-cpp |
| [exp-r-20260318-132826-dddbe9aa](../sources/experiences/exp-r-20260318-132826-dddbe9aa.md) | Level 1 Task 1: Square matrix multiplication C = A * B with N=2048 | repair | sm90 | cuda-cpp |
| [exp-r-20260318-140038-e3e3e750](../sources/experiences/exp-r-20260318-140038-e3e3e750.md) | Task: level_1/task_2 - Matrix multiplication (GEMM) C = A * B. A shape (M,K), B shape (K,N), C shape (M,N). Default sizes: M=1024, K=4096, N=2048. | repair | sm90 | cuda-cpp |
| [exp-r-20260318-143055-d49a076f](../sources/experiences/exp-r-20260318-143055-d49a076f.md) | Task: level_1/task_3 - Batched Matrix Multiplication (BMM) with shapes (batch_size=128, m=128, k=256, n=512) | repair | sm90 | cuda-cpp |
| [exp-r-20260318-144822-95c6149c](../sources/experiences/exp-r-20260318-144822-95c6149c.md) | Task level_1/task_4: Matrix-vector multiplication (GEMV) with A(256, 131072) and B(131072, 1) | repair | sm90 | cuda-cpp |
| [exp-r-20260318-150408-f6b085d9](../sources/experiences/exp-r-20260318-150408-f6b085d9.md) | kernelbench level_1 task_5 - matrix-scalar multiplication (C = A * s) | repair | sm90 | cuda-cpp |
| [exp-r-20260318-160053-e59d7cd7](../sources/experiences/exp-r-20260318-160053-e59d7cd7.md) | Task 8: Square matrix multiplication with irregular shapes (M=8205, K=2949, N=5921) | repair | sm90 | cuda-cpp |
| [exp-r-20260318-160825-cda16943](../sources/experiences/exp-r-20260318-160825-cda16943.md) | Task 9: Tall skinny matrix multiplication C = A * B where A is (16384, 16) and B is (16, 16384) | repair | sm90 | cuda-cpp |
| [exp-r-20260318-170238-f91fc10a](../sources/experiences/exp-r-20260318-170238-f91fc10a.md) | Task 11 (level_1): 4D tensor-matrix multiplication C[b,i,j,k] = sum_l A[b,i,j,l] * B[l,k]. Input shapes: A(b,i,j,l), B(l,k), output C(b,i,j,k). Default config: b=i=j=l=k=16. | repair | sm90 | cuda-cpp |
| [exp-r-20260318-170938-95bbe496](../sources/experiences/exp-r-20260318-170938-95bbe496.md) | Metal fp16 matrix multiplication implementation on macOS | repair | sm90 | cuda-cpp |
| [exp-r-20260318-171326-e2047549](../sources/experiences/exp-r-20260318-171326-e2047549.md) | Task level_1/task_12: Implement CUDA kernel for diagonal matrix multiplication C = diag(A) @ B where A is (N,) and B is (N, M) | repair | sm90 | cuda-cpp |
| [exp-r-20260318-172925-fd1bb504](../sources/experiences/exp-r-20260318-172925-fd1bb504.md) | Metal FP16 GEMM optimization - Round 2: Implemented 32x32 tiling with 2x2 thread coarsening (each thread computes 4 output elements). | repair | sm90 | cuda-cpp |
| [exp-r-20260318-173417-8f9a0e3c](../sources/experiences/exp-r-20260318-173417-8f9a0e3c.md) | AutoResearch Round 3: Implement Metal matrix multiplication with fp16 precision on macOS | repair | sm90 | cuda-cpp |
| [exp-r-20260318-173724-d75e05d9](../sources/experiences/exp-r-20260318-173724-d75e05d9.md) | Task: level_1/task_13 - Matrix multiplication C = A * B with symmetric matrices (N=4096) | repair | sm90 | cuda-cpp |
| [exp-r-20260318-173851-5051966b](../sources/experiences/exp-r-20260318-173851-5051966b.md) | Round 4/10 AutoResearch: Implement Metal matrix multiplication using fp16 precision on macOS | repair | sm90 | cuda-cpp |
| [exp-r-20260318-174707-009e5fa8](../sources/experiences/exp-r-20260318-174707-009e5fa8.md) | Task 14 (level_1): Upper triangular matrix multiplication C = triu(A @ B) with N=4096 | repair | sm90 | cuda-cpp |
| [exp-r-20260318-174857-d36b944c](../sources/experiences/exp-r-20260318-174857-d36b944c.md) | Round 5/10 of AutoResearch: Implement Metal FP16 matrix multiplication with half4 vectorized loads optimization | repair | sm90 | cuda-cpp |
| [exp-r-20260318-175455-70c6a06a](../sources/experiences/exp-r-20260318-175455-70c6a06a.md) | Task 15 (level_1): Lower triangular matrix multiplication C = tril(A @ B) where A and B are (N, N) lower triangular matrices | repair | sm90 | cuda-cpp |
| [exp-r-20260318-180207-21635ea2](../sources/experiences/exp-r-20260318-180207-21635ea2.md) | Task 16: C = A.T * B matrix multiplication. A shape (K,M), B shape (K,N), output C shape (M,N). Default sizes: M=1024, K=4096, N=2048. | repair | sm90 | cuda-cpp |
| [exp-r-20260318-181032-2e07e16f](../sources/experiences/exp-r-20260318-181032-2e07e16f.md) | Task 17: Matrix multiplication C = A * B.T where A is (M,K), B is (N,K), output is (M,N). M=1024, K=4096, N=2048. | repair | sm90 | cuda-cpp |
| [exp-r-20260318-182008-dc2d8e17](../sources/experiences/exp-r-20260318-182008-dc2d8e17.md) | Task 18: Matmul with transposed both (C = A.T * B.T) where A is (K,M), B is (N,K), output is (M,N) | repair | sm90 | cuda-cpp |
| [exp-r-20260318-183046-e12ff58c](../sources/experiences/exp-r-20260318-183046-e12ff58c.md) | Metal FP16 MatMul baseline implementation - Round 1/3 of AutoResearch | repair | sm90 | cuda-cpp |
| [exp-r-20260318-183833-8ad468f8](../sources/experiences/exp-r-20260318-183833-8ad468f8.md) | AutoResearch Round 2: Metal FP16 MatMul optimization with tiled kernel | repair | sm90 | cuda-cpp |
| [exp-r-20260318-211801-39127dbf](../sources/experiences/exp-r-20260318-211801-39127dbf.md) | Metal FP16 matrix multiplication kernel on macOS with runtime compilation | repair | sm90 | cuda-cpp |
| [exp-r-20260319-150238-34e61a19](../sources/experiences/exp-r-20260319-150238-34e61a19.md) | KernelBench level_1 task_2: GEMM matrix multiplication C = A * B with shapes (M,K) * (K,N) -> (M,N) | repair | sm90 | cuda-cpp |
| [exp-r-20260319-160931-d0739854](../sources/experiences/exp-r-20260319-160931-d0739854.md) | KernelBench level_1 task_4: Matrix-vector multiplication (M=256, K=131072) | repair | sm90 | cuda-cpp |
| [exp-r-20260319-165311-63df6957](../sources/experiences/exp-r-20260319-165311-63df6957.md) | KernelBench level_1 task_7: Matrix multiplication C = A * B with small K dimension (M=N=16384, K=32) | repair | sm90 | cuda-cpp |
| [exp-r-20260319-170735-0a913493](../sources/experiences/exp-r-20260319-170735-0a913493.md) | KernelBench level_1 task_8: GEMM with irregular shapes (M=8205, K=2949, N=5921) | repair | sm90 | cuda-cpp |
| [exp-r-20260319-180915-18b02016](../sources/experiences/exp-r-20260319-180915-18b02016.md) | KernelBench level_1 task_10: Batched matrix multiplication (N=16, M=1024, K=2048, L=768) | repair | sm90 | cuda-cpp |
| [exp-r-20260319-184657-e8e3bec8](../sources/experiences/exp-r-20260319-184657-e8e3bec8.md) | KernelBench level_1 task_13: Matrix multiplication of symmetric matrices (C = A * B, N x N) | repair | sm90 | cuda-cpp |
| [exp-r-20260319-191757-27f2b389](../sources/experiences/exp-r-20260319-191757-27f2b389.md) | KernelBench level_1 task_14: Upper triangular matrix multiplication C = A * B where both A and B are upper triangular matrices of shape (N, N) | repair | sm90 | cuda-cpp |
| [exp-r-20260319-193531-a1bc6cd1](../sources/experiences/exp-r-20260319-193531-a1bc6cd1.md) | KernelBench level_1 task_15: Lower triangular matrix multiplication C = tril(A @ B) | repair | sm90 | cuda-cpp |
| [exp-r-20260319-195139-f62acb38](../sources/experiences/exp-r-20260319-195139-f62acb38.md) | KernelBench level_1 task_17: GEMM with B transposed (C = A * B.T). A shape (M,K), B shape (N,K), output shape (M,N). | repair | sm90 | cuda-cpp |
| [exp-r-20260319-212622-e37039ec](../sources/experiences/exp-r-20260319-212622-e37039ec.md) | KernelBench level_1 task_1: Square matrix multiplication (C = A * B, N=2048) | repair | sm90 | cuda-cpp |
| [exp-r-20260319-213757-2b3d4be4](../sources/experiences/exp-r-20260319-213757-2b3d4be4.md) | KernelBench level_1 task_1 - Square matrix multiplication (C = A * B, N=2048) | repair | sm90 | cuda-cpp |
| [exp-r-20260319-214847-2646e2e0](../sources/experiences/exp-r-20260319-214847-2646e2e0.md) | AutoResearch Round 3/4: Matrix multiplication optimization with float4 vectorized loads | repair | sm90 | cuda-cpp |
| [exp-r-20260319-223537-88ab7684](../sources/experiences/exp-r-20260319-223537-88ab7684.md) | KernelBench level_1 task_2: Matrix multiplication C = A * B with shapes A(M,K), B(K,N), C(M,N). Default sizes: M=1024, K=4096, N=2048. | repair | sm90 | cuda-cpp |
| [exp-r-20260319-232653-2bb73b86](../sources/experiences/exp-r-20260319-232653-2bb73b86.md) | KernelBench level_1 task_3: Batched Matrix Multiplication (BMM). Shapes: A(batch, m, k), B(batch, k, n), C(batch, m, n). Default: batch=128, m=128, k=256, n=512. | repair | sm90 | cuda-cpp |
| [exp-r-20260319-233345-ed30f558](../sources/experiences/exp-r-20260319-233345-ed30f558.md) | KernelBench level_1 task_3: Batched Matrix Multiplication (BMM) with shapes A(batch,m,k), B(batch,k,n), C(batch,m,n). Default sizes: batch=128, m=128, k=256, n=512. | repair | sm90 | cuda-cpp |
| [exp-r-20260320-001604-5961de1c](../sources/experiences/exp-r-20260320-001604-5961de1c.md) | KernelBench level_1 task_4: Matrix-vector multiplication (256, 131072) @ (131072, 1) = (256, 1) | repair | sm90 | cuda-cpp |
| [exp-r-20260320-004312-71fe80ed](../sources/experiences/exp-r-20260320-004312-71fe80ed.md) | KernelBench level_1 task_4: Matrix-vector multiplication C = A @ B where A(256,131072), B(131072,1), C(256,1). Challenge: accumulating 131072 float values causes precision drift. | repair | sm90 | cuda-cpp |
| [exp-r-20260320-004509-17613ae0](../sources/experiences/exp-r-20260320-004509-17613ae0.md) | KernelBench level_1 task_4: Matrix-vector multiplication C = A @ B where A=(256,131072), B=(131072,1) | repair | sm90 | cuda-cpp |
| [exp-r-20260320-010826-8a185c16](../sources/experiences/exp-r-20260320-010826-8a185c16.md) | KernelBench level_1 task_5: Matrix-scalar multiplication (C = A * s) with M=16384, N=4096 | repair | sm90 | cuda-cpp |
| [exp-r-20260320-015249-b7ea29ea](../sources/experiences/exp-r-20260320-015249-b7ea29ea.md) | KernelBench level_1 task_6: Matmul with large K dimension (M=256, N=256, K=131072) | repair | sm90 | cuda-cpp |
| [exp-r-20260320-020250-43602115](../sources/experiences/exp-r-20260320-020250-43602115.md) | KernelBench level_1 task_6 - GEMM with M=256, N=256, K=131072 | repair | sm90 | cuda-cpp |
| [exp-r-20260320-023100-cb1a9ab6](../sources/experiences/exp-r-20260320-023100-cb1a9ab6.md) | KernelBench level_1 task_7: Matrix multiplication C = A @ B with M=N=16384, K=32. Small K dimension makes this memory-bound operation. | repair | sm90 | cuda-cpp |
| [exp-r-20260320-033837-fef31f82](../sources/experiences/exp-r-20260320-033837-fef31f82.md) | KernelBench level_1 task_8: Matrix multiplication C = A * B with irregular shapes (M=8205, K=2949, N=5921) | repair | sm90 | cuda-cpp |
| [exp-r-20260320-044610-59227f0c](../sources/experiences/exp-r-20260320-044610-59227f0c.md) | KernelBench level_1 task_9: Tall-and-skinny GEMM C = A @ B where A(16384,16) @ B(16,16384) = C(16384,16384). Inner dimension K=16 is very small. | repair | sm90 | cuda-cpp |
| [exp-r-20260320-045051-2d4be381](../sources/experiences/exp-r-20260320-045051-2d4be381.md) | KernelBench level_1 task_9: Tall-and-skinny GEMM (16384x16 @ 16x16384) with K=16 | repair | sm90 | cuda-cpp |
| [exp-r-20260320-053129-e814b168](../sources/experiences/exp-r-20260320-053129-e814b168.md) | KernelBench level_1 task_9: Tall-and-skinny GEMM C = A @ B where A=(16384,16), B=(16,16384), C=(16384,16384). K=16 is very small. | repair | sm90 | cuda-cpp |
| [exp-r-20260320-053828-732b2c00](../sources/experiences/exp-r-20260320-053828-732b2c00.md) | KernelBench level_1 task_10: Batched matrix multiplication (N=16, M=1024, K=2048, L=768) x (K, L) -> (N, M, L) | repair | sm90 | cuda-cpp |
| [exp-r-20260320-060154-18b02016](../sources/experiences/exp-r-20260320-060154-18b02016.md) | KernelBench level_1 task_10: Batched matrix multiplication (N=16, M=1024, K=2048, L=768) | repair | sm90 | cuda-cpp |
| [exp-r-20260320-060518-f12819ca](../sources/experiences/exp-r-20260320-060518-f12819ca.md) | KernelBench level_1 task_10: Batched matrix multiplication (N, M, K) x (K, L) -> (N, M, L) with N=16, M=1024, K=2048, L=768 | repair | sm90 | cuda-cpp |
| [exp-r-20260320-061211-d8be03be](../sources/experiences/exp-r-20260320-061211-d8be03be.md) | KernelBench level_1 task_11: 4D tensor-matrix multiplication C[b,i,j,k] = sum_l A[b,i,j,l] * B[l,k] | repair | sm90 | cuda-cpp |
| [exp-r-20260320-071011-9605f4f9](../sources/experiences/exp-r-20260320-071011-9605f4f9.md) | KernelBench level_1 task_12: Diagonal matrix multiplication C = diag(A) @ B where A is (N,) and B is (N,M) | repair | sm90 | cuda-cpp |
| [exp-r-20260320-073051-761f6d76](../sources/experiences/exp-r-20260320-073051-761f6d76.md) | KernelBench level_1 task_12: Diagonal matrix multiplication C = diag(A) @ B. Round 2 optimization. | repair | sm90 | cuda-cpp |
| [exp-r-20260320-074134-bcdde970](../sources/experiences/exp-r-20260320-074134-bcdde970.md) | KernelBench level_1 task_12: Diagonal matrix multiplication C = diag(A) @ B | repair | sm90 | cuda-cpp |
| [exp-r-20260320-075858-1922570a](../sources/experiences/exp-r-20260320-075858-1922570a.md) | KernelBench level_1 task_13: Matrix multiplication C = A * B with symmetric N x N matrices | repair | sm90 | cuda-cpp |
| [exp-r-20260320-082832-af9dd831](../sources/experiences/exp-r-20260320-082832-af9dd831.md) | KernelBench level_1 task_14: Upper triangular matrix multiplication (C = triu(A * B)) | repair | sm90 | cuda-cpp |
| [exp-r-20260320-085548-af9dd831](../sources/experiences/exp-r-20260320-085548-af9dd831.md) | KernelBench level_1 task_14: Upper triangular matrix multiplication (C = triu(A * B)) | repair | sm90 | cuda-cpp |
| [exp-r-20260320-114803-404e4dd5](../sources/experiences/exp-r-20260320-114803-404e4dd5.md) | KernelBench level_1 task_17: C = A * B.T matrix multiplication with A(M,K) and B(N,K) | repair | sm90 | cuda-cpp |
| [exp-r-20260320-122905-f44966ee](../sources/experiences/exp-r-20260320-122905-f44966ee.md) | KernelBench level_1 task_18: C = A.T * B.T matrix multiplication. A(K,M), B(N,K), output C(M,N) | repair | sm90 | cuda-cpp |
| [exp-r-20260320-124443-4da8dda3](../sources/experiences/exp-r-20260320-124443-4da8dda3.md) | KernelBench level_1 task_18: C = A.T * B.T matrix multiplication optimization | repair | sm90 | cuda-cpp |
| [exp-r-20260320-160519-5aeec39e](../sources/experiences/exp-r-20260320-160519-5aeec39e.md) | KernelBench level_1 task_1: Square matrix multiplication C = A * B (N=2048) | repair | sm90 | cuda-cpp |
| [exp-r-20260320-163444-909019d4](../sources/experiences/exp-r-20260320-163444-909019d4.md) | KernelBench level_1 task_1: Square matrix multiplication C = A * B (N=2048). Tried multiple optimizations: tile size increase, float4 vectorization, register tiling. | repair | sm90 | cuda-cpp |
| [exp-r-20260320-165538-69fec7a7](../sources/experiences/exp-r-20260320-165538-69fec7a7.md) | KernelBench level_1 task_1: Square matrix multiplication C = A * B with N=2048 | repair | sm90 | cuda-cpp |
| [exp-r-20260320-170453-c04cb34c](../sources/experiences/exp-r-20260320-170453-c04cb34c.md) | KernelBench level_1 task_2: GEMM C = A * B with shapes M=1024, K=4096, N=2048 | repair | sm90 | cuda-cpp |
| [exp-r-20260320-172511-a58ca546](../sources/experiences/exp-r-20260320-172511-a58ca546.md) | KernelBench level_1 task_2 GEMM optimization Round 3 | repair | sm90 | cuda-cpp |
| [exp-r-20260320-173426-b3673a92](../sources/experiences/exp-r-20260320-173426-b3673a92.md) | KernelBench level_1 task_2 GEMM optimization - Round 4 attempted vectorized loads | repair | sm90 | cuda-cpp |
| [exp-r-20260328-095312-90041d73](../sources/experiences/exp-r-20260328-095312-90041d73.md) | w4a32c8_q4_0_fp32_int8_llama3_8b_att_out_n4096_k4096 | repair | sm90 | cuda-cpp |
| [exp-r-20260502-180001-static-gate-kernel-h-include](../sources/experiences/exp-r-20260502-180001-static-gate-kernel-h-include.md) | sol_execbench_bf16_int8_gemm | repair | sm90 | cuda-cpp |
| [exp-r-20260502-180002-cuda-type-in-cpp](../sources/experiences/exp-r-20260502-180002-cuda-type-in-cpp.md) | sol_execbench_bf16_int8_gemm | repair | sm90 | cuda-cpp |
| [exp-r-20260502-180003-dps-void-signature](../sources/experiences/exp-r-20260502-180003-dps-void-signature.md) | sol_execbench_bf16_int8_gemm | repair | sm90 | cuda-cpp |
| [exp-r-20260502-180004-bf16-cutlass-layout](../sources/experiences/exp-r-20260502-180004-bf16-cutlass-layout.md) | sol_execbench_bf16_gemm | repair | sm90 | cuda-cpp, cute-dsl |
| [exp-r-20260502-180005-cublaslt-transpose-logic](../sources/experiences/exp-r-20260502-180005-cublaslt-transpose-logic.md) | sol_execbench_bf16_gemm | repair | sm90 | cuda-cpp |
| [exp-r-20260502-180006-cublaslt-handle-overhead](../sources/experiences/exp-r-20260502-180006-cublaslt-handle-overhead.md) | sol_execbench_gemm | repair | sm90 | cuda-cpp |
| [exp-r-20260502-180007-attempt-dir-not-bound](../sources/experiences/exp-r-20260502-180007-attempt-dir-not-bound.md) | sol_execbench_gemm | repair | sm90 | cuda-cpp |
| [exp-r-20260502-180008-cutlass-minimal-header](../sources/experiences/exp-r-20260502-180008-cutlass-minimal-header.md) | sol_execbench_bf16_gemm | repair | sm90 | cuda-cpp, cute-dsl |
| [exp-r-20260502-180009-dps-contiguous-copyback](../sources/experiences/exp-r-20260502-180009-dps-contiguous-copyback.md) | sol_execbench_gemm | repair | sm90 | cuda-cpp |
| [exp-r-20260502-180010-autoresearch-premature-termination](../sources/experiences/exp-r-20260502-180010-autoresearch-premature-termination.md) | sol_execbench_int8_gemm | repair | sm90 | cuda-cpp |
| [exp-r-20260502-180011-int8-gemm-cutlass-template](../sources/experiences/exp-r-20260502-180011-int8-gemm-cutlass-template.md) | sol_execbench_int8_gemm | repair | sm90 | cuda-cpp |
| [exp-r-20260502-180012-int8-gemm-cublas-layout](../sources/experiences/exp-r-20260502-180012-int8-gemm-cublas-layout.md) | sol_execbench_int8_gemm | repair | sm90 | cuda-cpp |
| [exp-r-20260506-150001-int8-gemm-step-budget-exhaustion](../sources/experiences/exp-r-20260506-150001-int8-gemm-step-budget-exhaustion.md) | SOL-ExecBench INT8 GEMM: step budget exhaustion pattern | repair | sm90 | cuda-cpp |
| [exp-r-20260506-150002-int8-gemm-verification-blocked](../sources/experiences/exp-r-20260506-150002-int8-gemm-verification-blocked.md) | SOL-ExecBench BF16 GEMM: verification blocked by static gate | repair | sm90 | cuda-cpp |
| [exp-r-20260506-150003-gemm-cublaslt-api-misuse](../sources/experiences/exp-r-20260506-150003-gemm-cublaslt-api-misuse.md) | SOL-ExecBench GEMM: cuBLASLt API misuse causing compilation failure | repair | sm90 | cuda-cpp |
| [exp-r-20260506-150004-gemm-cutlass-step-budget](../sources/experiences/exp-r-20260506-150004-gemm-cutlass-step-budget.md) | SOL-ExecBench GEMM: CUTLASS template debugging exhausts step budget | repair | sm90 | cuda-cpp |
| [exp-r-20260506-150005-gemm-torch-mm-not-optimization](../sources/experiences/exp-r-20260506-150005-gemm-torch-mm-not-optimization.md) | SOL-ExecBench GEMM: torch.mm wrapper is not a valid optimization | repair | sm90 | cuda-cpp |
| [exp-r-20260506-150006-gemm-row-major-col-major](../sources/experiences/exp-r-20260506-150006-gemm-row-major-col-major.md) | SOL-ExecBench GEMM: row-major to column-major transpose pattern | repair | sm90 | cuda-cpp |
| [exp-r-20260506-150007-gemm-handle-creation-overhead](../sources/experiences/exp-r-20260506-150007-gemm-handle-creation-overhead.md) | SOL-ExecBench GEMM: cuBLAS handle creation overhead for small matrices | repair | sm90 | cuda-cpp |
| [exp-r-20260506-160001-sol-execbench-shell-writes-blocked](../sources/experiences/exp-r-20260506-160001-sol-execbench-shell-writes-blocked.md) | SOL-ExecBench: direct shell writes to solution.json blocked | repair | sm90 | cuda-cpp |
| [exp-r-20260506-160002-sol-execbench-evaluator-timeout](../sources/experiences/exp-r-20260506-160002-sol-execbench-evaluator-timeout.md) | SOL-ExecBench: evaluator times out after 180s | repair | sm90 | cuda-cpp |
| [exp-r-20260506-160003-results-tsv-state-core](../sources/experiences/exp-r-20260506-160003-results-tsv-state-core.md) | SOL-ExecBench: results.tsv missing because state_core projection not rebuilt | repair | sm90 | cuda-cpp |
| [exp-r-20260506-160004-projection-owned-artifact](../sources/experiences/exp-r-20260506-160004-projection-owned-artifact.md) | SOL-ExecBench: projection-owned artifacts cannot be edited directly | repair | sm90 | cuda-cpp |
| [exp-r-20260506-160005-entry-point-mismatch](../sources/experiences/exp-r-20260506-160005-entry-point-mismatch.md) | SOL-ExecBench: entry_point mismatch with actual code | repair | sm90 | cuda-cpp |
| [exp-r-20260506-160006-sol-execbench-compile-failure](../sources/experiences/exp-r-20260506-160006-sol-execbench-compile-failure.md) | SOL-ExecBench: common compilation failure patterns | repair | sm90 | cuda-cpp |
| [exp-r-20260506-160007-canonical-verification-write-block](../sources/experiences/exp-r-20260506-160007-canonical-verification-write-block.md) | SOL-ExecBench: canonical verification requires attempt_dir binding | repair | sm90 | cuda-cpp |
| [exp-r-20260508-120001-aten-getCurrentCUDAStream](../sources/experiences/exp-r-20260508-120001-aten-getCurrentCUDAStream.md) | exp-r-20260508-120001-aten-getCurrentCUDAStream | repair | sm90 | cuda-cpp |
| [exp-r-20260508-120002-cutlass-int8-opclass](../sources/experiences/exp-r-20260508-120002-cutlass-int8-opclass.md) | exp-r-20260508-120002-cutlass-int8-opclass | repair | sm90 | cuda-cpp, cute-dsl |
| [exp-r-20260508-120003-cublasLt-api-misuse](../sources/experiences/exp-r-20260508-120003-cublasLt-api-misuse.md) | exp-r-20260508-120003-cublasLt-api-misuse | repair | sm90 | cuda-cpp |
| [exp-r-20260508-120005-cutlass-int8-alignment](../sources/experiences/exp-r-20260508-120005-cutlass-int8-alignment.md) | exp-r-20260508-120005-cutlass-int8-alignment | repair | sm90 | cuda-cpp, cute-dsl |
| [exp-r-20260508-160101-dps-signature-contract](../sources/experiences/exp-r-20260508-160101-dps-signature-contract.md) | exp-r-20260508-160101-dps-signature-contract | repair | sm90 | cuda-cpp |
| [exp-r-20260508-160102-gemm-contiguous-stride-correctness](../sources/experiences/exp-r-20260508-160102-gemm-contiguous-stride-correctness.md) | exp-r-20260508-160102-gemm-contiguous-stride-correctness | repair | sm90 | cuda-cpp |
| [exp-r-20260508-160103-gemm-lda-ldb-ldc-selfcheck](../sources/experiences/exp-r-20260508-160103-gemm-lda-ldb-ldc-selfcheck.md) | exp-r-20260508-160103-gemm-lda-ldb-ldc-selfcheck | repair | sm90 | cuda-cpp |
| [exp-r-20260508-160104-cuda-linker-symbol-errors](../sources/experiences/exp-r-20260508-160104-cuda-linker-symbol-errors.md) | exp-r-20260508-160104-cuda-linker-symbol-errors | repair | sm90 | cuda-cpp |
| [exp-r-20260508-180001-cublas-lda-ldb-correctness](../sources/experiences/exp-r-20260508-180001-cublas-lda-ldb-correctness.md) | exp-r-20260508-180001-cublas-lda-ldb-correctness | repair | sm90 | cuda-cpp |
| [exp-r-20260508-180002-cutlass-extreme-aspect-ratio](../sources/experiences/exp-r-20260508-180002-cutlass-extreme-aspect-ratio.md) | exp-r-20260508-180002-cutlass-extreme-aspect-ratio | repair | sm90 | cuda-cpp, cute-dsl |
| [exp-r-20260508-180003-missing-cstdint-for-int-types](../sources/experiences/exp-r-20260508-180003-missing-cstdint-for-int-types.md) | exp-r-20260508-180003-missing-cstdint-for-int-types | repair | sm90 | cuda-cpp |
| [exp-r-20260513-100001-int8-gemm-b-layout-col-major](../sources/experiences/exp-r-20260513-100001-int8-gemm-b-layout-col-major.md) | SOL-ExecBench INT8 GEMM: B matrix is column-major, not row-major | repair | sm90 | cuda-cpp |
| [exp-r-20260513-100002-int8-gemm-cublas-lda-wrong](../sources/experiences/exp-r-20260513-100002-int8-gemm-cublas-lda-wrong.md) | SOL-ExecBench INT8 GEMM: cuBLAS leading dimension mismatch for col-major B | repair | sm90 | cuda-cpp |
| [exp-r-20260513-100003-int8-gemm-scale-tensor-to-scalar](../sources/experiences/exp-r-20260513-100003-int8-gemm-scale-tensor-to-scalar.md) | SOL-ExecBench INT8 GEMM: scale_a/scale_b are per-element tensors, not scalars | repair | sm90 | cuda-cpp |
| [exp-r-20260513-100004-int8-gemm-colmajor-index-overflow](../sources/experiences/exp-r-20260513-100004-int8-gemm-colmajor-index-overflow.md) | SOL-ExecBench INT8 GEMM: illegal memory access from wrong col-major index in dequant kernel | repair | sm90 | cuda-cpp |
| [exp-r-20260513-100005-int8-gemm-output-dtype-mismatch](../sources/experiences/exp-r-20260513-100005-int8-gemm-output-dtype-mismatch.md) | SOL-ExecBench INT8 GEMM: output tensor C dtype depends on task — always check C.scalar_type() at runtime | repair | sm90 | cuda-cpp |
| [exp-r-20260513-100006-int8-gemm-torch-mm-not-optimization](../sources/experiences/exp-r-20260513-100006-int8-gemm-torch-mm-not-optimization.md) | SOL-ExecBench INT8 GEMM: torch.mm() wrapper is not a kernel optimization | repair | sm90 | python |
| [exp-r-20260513-100007-fp16-half2float-type-conversion](../sources/experiences/exp-r-20260513-100007-fp16-half2float-type-conversion.md) | SOL-ExecBench FP16 GEMM: __half2float returns float, cannot assign to __half | repair | sm90 | cuda-cpp |
| [exp-r-20260513-100008-bf16-static-gate-cuda-type-in-cpp](../sources/experiences/exp-r-20260513-100008-bf16-static-gate-cuda-type-in-cpp.md) | SOL-ExecBench BF16 output: __nv_bfloat16 type in .cpp file triggers static gate error | repair | sm90 | cuda-cpp |
| [exp-r-20260513-100009-bf16-data-ptr-access](../sources/experiences/exp-r-20260513-100009-bf16-data-ptr-access.md) | SOL-ExecBench BF16 tensor: use data_ptr() or data_ptr<at::BFloat16>(), not data_ptr<__nv_bfloat16>() | repair | sm90 | cuda-cpp |
| [exp-r-20260513-100010-verification-contract-policy-violation](../sources/experiences/exp-r-20260513-100010-verification-contract-policy-violation.md) | AutoResearch verification contract policy: sandbox command not declared in execution contract | repair | sm90 | cuda-cpp |
| [exp-r-20260513-100012-cutlass-include-path-missing](../sources/experiences/exp-r-20260513-100012-cutlass-include-path-missing.md) | SOL-ExecBench CUTLASS kernel: include path not in compile_options | repair | sm90 | cuda-cpp, cute-dsl |
| [exp-r-20260514-100002-int8-gemm-cublas-parameter-mapping](../sources/experiences/exp-r-20260514-100002-int8-gemm-cublas-parameter-mapping.md) | SOL-ExecBench INT8 GEMM: cuBLAS cublasGemmEx parameter mapping for mixed row/col-major inputs | repair | sm90 | cuda-cpp |
| [exp-r-20260514-100004-int8-gemm-dequant-colmajor-layout](../sources/experiences/exp-r-20260514-100004-int8-gemm-dequant-colmajor-layout.md) | SOL-ExecBench INT8 GEMM: dequant kernel layout — cuBLAS output is [N,M] column-major, not [M,N] row-major | repair | sm90 | cuda-cpp |
| [exp-r-20260514-100005-int8-gemm-cuda-stream-api-include](../sources/experiences/exp-r-20260514-100005-int8-gemm-cuda-stream-api-include.md) | SOL-ExecBench INT8 GEMM: CUDA stream API and .cu/.cpp file responsibility | repair | sm90 | cuda-cpp |
| [exp-r-20260514-100006-int8-gemm-extern-c-linking](../sources/experiences/exp-r-20260514-100006-int8-gemm-extern-c-linking.md) | SOL-ExecBench INT8 GEMM: extern C linking for nvcc/g++ interop | repair | sm90 | cuda-cpp |
| [exp-r-20260514-100007-int8-gemm-cuda-bf16-include-type-boundary](../sources/experiences/exp-r-20260514-100007-int8-gemm-cuda-bf16-include-type-boundary.md) | SOL-ExecBench INT8 GEMM: cuda_bf16.h include and host/device type boundary | repair | sm90 | cuda-cpp |
| [exp-r-20260514-100008-int8-gemm-kernel-host-signature-mismatch](../sources/experiences/exp-r-20260514-100008-int8-gemm-kernel-host-signature-mismatch.md) | SOL-ExecBench INT8 GEMM: kernel-host function signature mismatch and missing declarations | repair | sm90 | cuda-cpp |
| [exp-r-20260514-100009-int8-gemm-dirty-state-locked-round](../sources/experiences/exp-r-20260514-100009-int8-gemm-dirty-state-locked-round.md) | SOL-ExecBench INT8 GEMM: dirty state cascade and locked_round dead loop in multi-round sessions | repair | sm90 | cuda-cpp |
| [exp-r-20260514-100010-int8-gemm-cstdio-include-debug-output](../sources/experiences/exp-r-20260514-100010-int8-gemm-cstdio-include-debug-output.md) | SOL-ExecBench INT8 GEMM: missing cstdio include for fprintf/stderr debug output in CUDA | repair | sm90 | cuda-cpp |
| [exp-r-20260517-200000-nv-bfloat16-in-cpp](../sources/experiences/exp-r-20260517-200000-nv-bfloat16-in-cpp.md) | CUDA BF16 type in .cpp wrapper causes host compiler error | repair | sm90 | cuda-cpp |
| [exp-r-20260517-200001-pybind-module-in-cu](../sources/experiences/exp-r-20260517-200001-pybind-module-in-cu.md) | PYBIND11_MODULE placed in .cu file instead of .cpp wrapper | repair | sm90 | cuda-cpp |
| [exp-r-20260517-200002-kernel-h-missing-cuda-runtime](../sources/experiences/exp-r-20260517-200002-kernel-h-missing-cuda-runtime.md) | kernel.h uses cudaStream_t but does not include cuda_runtime.h | repair | sm90 | cuda-cpp |
| [exp-r-20260517-200003-dps-signature-mismatch](../sources/experiences/exp-r-20260517-200003-dps-signature-mismatch.md) | DPS signature mismatch: run() must be void with output tensors at end | repair | sm90 | cuda-cpp |
| [exp-r-20260517-200004-get-current-cuda-stream](../sources/experiences/exp-r-20260517-200004-get-current-cuda-stream.md) | getCurrentCUDAStream is not a member of at::cuda | repair | sm90 | cuda-cpp |
| [exp-r-20260517-200005-sol-execbench-workflow](../sources/experiences/exp-r-20260517-200005-sol-execbench-workflow.md) | SOL-ExecBench workflow: solution.json is canonical, not loose files | repair | sm90 | cuda-cpp |
| [exp-r-20260517-200006-sol-execbench-round-lock](../sources/experiences/exp-r-20260517-200006-sol-execbench-round-lock.md) | SOL-ExecBench round lock and skill contract mismatch errors | repair | sm90 | cuda-cpp |
| [exp-r-20260517-200007-misaligned-address](../sources/experiences/exp-r-20260517-200007-misaligned-address.md) | CUDA misaligned address runtime error in BF16/INT8 kernels | repair | sm90 | cuda-cpp |
| [exp-r-20260517-200008-illegal-memory-access](../sources/experiences/exp-r-20260517-200008-illegal-memory-access.md) | CUDA illegal memory access in GEMM/attention kernels | repair | sm90 | cuda-cpp |
| [exp-r-20260517-200009-cuda-invalid-argument](../sources/experiences/exp-r-20260517-200009-cuda-invalid-argument.md) | CUDA invalid argument error in kernel launch | repair | sm90 | cuda-cpp |
| [exp-r-20260517-200013-wmma-api-misuse](../sources/experiences/exp-r-20260517-200013-wmma-api-misuse.md) | WMMA API misuse: tile size, fragment types, and memory layout | repair | sm90 | cuda-cpp |
| [exp-r-20260517-200014-q4-0-unpack-loop](../sources/experiences/exp-r-20260517-200014-q4-0-unpack-loop.md) | Q4_0 quantization: only unpacking first element instead of full 32-element block | repair | sm90 | cuda-cpp |
| [exp-r-20260517-200015-tensor-scalar-error](../sources/experiences/exp-r-20260517-200015-tensor-scalar-error.md) | Tensor with N elements cannot be converted to Scalar | repair | sm90 | cuda-cpp |
| [exp-r-20260517-200016-compilation-debug-workflow](../sources/experiences/exp-r-20260517-200016-compilation-debug-workflow.md) | SOL-ExecBench compilation failure debugging workflow | repair | sm90 | cuda-cpp |
| [exp-r-20260526-200001-cublaslt-compute-type-precision](../sources/experiences/exp-r-20260526-200001-cublaslt-compute-type-precision.md) | SOL-ExecBench GEMM: cublasLt COMPUTE_TYPE precision mismatch causing correctness failure | repair | sm90 | cuda-cpp |
| [exp-r-20260526-200002-cublaslt-matrix-layout-descriptor](../sources/experiences/exp-r-20260526-200002-cublaslt-matrix-layout-descriptor.md) | SOL-ExecBench GEMM: cublasLt matrix layout descriptor leading dimension error | repair | sm90 | cuda-cpp |
| [exp-r-20260526-200003-cpp-header-naming-nvcc](../sources/experiences/exp-r-20260526-200003-cpp-header-naming-nvcc.md) | SOL-ExecBench: C++ header naming confusion in nvcc-compiled .cu files | repair | sm90 | cuda-cpp |
| [exp-r-20260526-200004-sol-execbench-function-name-collision](../sources/experiences/exp-r-20260526-200004-sol-execbench-function-name-collision.md) | SOL-ExecBench: duplicate function name 'run' causing linker error | repair | sm90 | cuda-cpp |
| [exp-r-20260528-113600-fp16-wmma-store-matrix-sync-mismatch](../sources/experiences/exp-r-20260528-113600-fp16-wmma-store-matrix-sync-mismatch.md) | FP16 WMMA store_matrix_sync type/layout mismatch | repair | sm90 | cuda-cpp |
| [exp-r-20260528-113601-fp16-wmma-launch-failure-recovery](../sources/experiences/exp-r-20260528-113601-fp16-wmma-launch-failure-recovery.md) | FP16 WMMA runtime launch failure diagnosis and recovery | repair | sm90 | cuda-cpp |
| [exp-r-20260529-0003-update-sources-format-loop](../sources/experiences/exp-r-20260529-0003-update-sources-format-loop.md) | Agent wastes 40+ steps calling sol_execbench_update_sources with wrong sources format | repair | sm90 | cuda-cpp |

## layer-norm

| ID | Title | Type | Architectures | Languages |
|----|-------|------|--------------|-----------|
| [exp-i-20260311-231714-fab89c81](../sources/experiences/exp-i-20260311-231714-fab89c81.md) | fp32_rms_norm_llama2_7b_hs128 | implementation | sm90 | cuda-cpp |
| [exp-i-20260311-233239-f42aff56](../sources/experiences/exp-i-20260311-233239-f42aff56.md) | fp32_rms_norm_llama2_7b_hs512 | implementation | sm90 | cuda-cpp |
| [exp-i-20260322-210142-4252d6d8](../sources/experiences/exp-i-20260322-210142-4252d6d8.md) | fp32_rms_norm_llama2_7b_hs128 | implementation | sm90 | cuda-cpp |
| [exp-i-20260322-220040-23863070](../sources/experiences/exp-i-20260322-220040-23863070.md) | RN_02 | implementation | sm90 | cuda-cpp |
| [exp-i-20260323-144157-0869f7cc](../sources/experiences/exp-i-20260323-144157-0869f7cc.md) | fp32_rms_norm_deepseek_v3_hs7168 | implementation | sm90 | cuda-cpp |
| [exp-i-20260325-114539-de6d5998](../sources/experiences/exp-i-20260325-114539-de6d5998.md) | fp32_rms_norm_qwen3_4b_hs2560 | implementation | sm90 | cuda-cpp |
| [exp-i-20260327-152814-d1f87198](../sources/experiences/exp-i-20260327-152814-d1f87198.md) | fp32_rms_norm_qwen3_4b_hs1536 | implementation | sm90 | cuda-cpp |
| [exp-o-20260322-204022-2f58b68f](../sources/experiences/exp-o-20260322-204022-2f58b68f.md) | RN_04 | optimization | sm90 | cuda-cpp |
| [exp-o-20260322-210840-280630c4](../sources/experiences/exp-o-20260322-210840-280630c4.md) | fp32_rms_norm_llama2_7b_hs128 | optimization | sm90 | cuda-cpp |
| [exp-o-20260322-211546-c5fb30ce](../sources/experiences/exp-o-20260322-211546-c5fb30ce.md) | fp32_rms_norm_llama2_7b_hs128 | optimization | sm90 | cuda-cpp |
| [exp-o-20260322-220840-3e7acb0c](../sources/experiences/exp-o-20260322-220840-3e7acb0c.md) | RN_02_fp32_rms_norm_llama2_7b_hs128 | optimization | sm90 | cuda-cpp |
| [exp-o-20260322-221247-f8ecb799](../sources/experiences/exp-o-20260322-221247-f8ecb799.md) | RN_02_fp32_rms_norm_llama2_7b_hs128 | optimization | sm90 | cuda-cpp |
| [exp-o-20260323-144717-00bc5eef](../sources/experiences/exp-o-20260323-144717-00bc5eef.md) | fp32_rms_norm_deepseek_v3_hs7168 | optimization | sm90 | cuda-cpp |
| [exp-o-20260323-145813-95f2accb](../sources/experiences/exp-o-20260323-145813-95f2accb.md) | fp32_rms_norm_deepseek_v3_hs7168 | optimization | sm90 | cuda-cpp |
| [exp-o-20260323-175407-3ba488ff](../sources/experiences/exp-o-20260323-175407-3ba488ff.md) | fp32_rms_norm_llama3_8b_hs4096 | optimization | sm90 | cuda-cpp |
| [exp-o-20260323-175535-c29e0bf6](../sources/experiences/exp-o-20260323-175535-c29e0bf6.md) | fp32_rms_norm_llama3_8b_hs4096 | optimization | sm90 | cuda-cpp |
| [exp-o-20260323-180158-f7b97285](../sources/experiences/exp-o-20260323-180158-f7b97285.md) | fp32_rms_norm_llama3_8b_hs4096 | optimization | sm90 | cuda-cpp |
| [exp-o-20260323-181652-68b570c7](../sources/experiences/exp-o-20260323-181652-68b570c7.md) | fp32_rms_norm_llama3_8b_hs4096 | optimization | sm90 | cuda-cpp |
| [exp-o-20260323-185458-71f34a08](../sources/experiences/exp-o-20260323-185458-71f34a08.md) | fp32_rms_norm_llama3_8b_hs4096 | optimization | sm90 | cuda-cpp |
| [exp-o-20260323-190816-8c2d89ad](../sources/experiences/exp-o-20260323-190816-8c2d89ad.md) | fp32_rms_norm_llama3_8b_hs4096 | optimization | sm90 | cuda-cpp |
| [exp-o-20260323-191418-22a8d687](../sources/experiences/exp-o-20260323-191418-22a8d687.md) | fp32_rms_norm_llama3_8b_hs4096 | optimization | sm90 | cuda-cpp |
| [exp-o-20260323-194722-4272b7c0](../sources/experiences/exp-o-20260323-194722-4272b7c0.md) | RMS Norm LLaMA-3-8B hidden_size=4096 | optimization | sm90 | cuda-cpp |
| [exp-o-20260323-195729-0b88fb6e](../sources/experiences/exp-o-20260323-195729-0b88fb6e.md) | RMS Norm LLaMA-3-8B hidden_size=4096 | optimization | sm90 | cuda-cpp |
| [exp-o-20260323-200436-16cd76e8](../sources/experiences/exp-o-20260323-200436-16cd76e8.md) | RMS Norm LLaMA-3-8B hidden_size=4096 | optimization | sm90 | cuda-cpp |
| [exp-o-20260323-212039-a74d75e2](../sources/experiences/exp-o-20260323-212039-a74d75e2.md) | fp32_rms_norm_llama3_8b_hs4096 | optimization | sm90 | cuda-cpp |
| [exp-o-20260323-212535-b4ad4cd8](../sources/experiences/exp-o-20260323-212535-b4ad4cd8.md) | fp32_rms_norm_llama3_8b_hs4096 | optimization | sm90 | cuda-cpp |
| [exp-o-20260323-213317-3bd1c9c1](../sources/experiences/exp-o-20260323-213317-3bd1c9c1.md) | fp32_rms_norm_llama3_8b_hs4096 | optimization | sm90 | cuda-cpp |
| [exp-o-20260324-075625-a7f654c3](../sources/experiences/exp-o-20260324-075625-a7f654c3.md) | fp32_rms_norm_deepseek_v3_hs7168 | optimization | sm90 | cuda-cpp |
| [exp-o-20260324-080421-9a4ddbe2](../sources/experiences/exp-o-20260324-080421-9a4ddbe2.md) | fp32_rms_norm_deepseek_v3_hs7168 | optimization | sm90 | cuda-cpp |
| [exp-o-20260324-080807-fa41d2a5](../sources/experiences/exp-o-20260324-080807-fa41d2a5.md) | fp32_rms_norm_deepseek_v3_hs7168 | optimization | sm90 | cuda-cpp |
| [exp-o-20260324-092104-5c7202b0](../sources/experiences/exp-o-20260324-092104-5c7202b0.md) | fp32_rms_norm_llama3_8b_hs4096 | optimization | sm90 | cuda-cpp |
| [exp-o-20260324-092643-0aaab3f8](../sources/experiences/exp-o-20260324-092643-0aaab3f8.md) | fp32_rms_norm_llama3_8b_hs4096 | optimization | sm90 | cuda-cpp |
| [exp-o-20260324-093510-e372c040](../sources/experiences/exp-o-20260324-093510-e372c040.md) | fp32_rms_norm_llama3_8b_hs4096 | optimization | sm90 | cuda-cpp |
| [exp-o-20260324-111703-6a84e0ff](../sources/experiences/exp-o-20260324-111703-6a84e0ff.md) | fp32_rms_norm_qwen3_4b_hs1536 | optimization | sm90 | cuda-cpp |
| [exp-o-20260324-113124-85e25713](../sources/experiences/exp-o-20260324-113124-85e25713.md) | fp32_rms_norm_qwen2_5_7b_hs3584 | optimization | sm90 | cuda-cpp |
| [exp-o-20260325-122933-897dc088](../sources/experiences/exp-o-20260325-122933-897dc088.md) | fp32_rms_norm_qwen3_4b_hs2560 | optimization | sm90 | cuda-cpp |
| [exp-o-20260325-124446-4a3e87cb](../sources/experiences/exp-o-20260325-124446-4a3e87cb.md) | fp32_rms_norm_qwen3_4b_hs2560 | optimization | sm90 | cuda-cpp |
| [exp-o-20260328-172621-43b40b9c](../sources/experiences/exp-o-20260328-172621-43b40b9c.md) |  | optimization | sm90 | cuda-cpp |
| [exp-r-20260317-141520-6dcdaa12](../sources/experiences/exp-r-20260317-141520-6dcdaa12.md) | Implement RMS Norm operator using Metal on macOS with kernel.metal and metal_test.mm | repair | sm90 | cuda-cpp |
| [exp-r-20260321-232522-f11c425f](../sources/experiences/exp-r-20260321-232522-f11c425f.md) | RMS Norm kernel optimization for hidden_size=512, KernelEvalPlus RN_03 task | repair | sm90 | cuda-cpp |
| [exp-r-20260322-085339-8c1841e8](../sources/experiences/exp-r-20260322-085339-8c1841e8.md) | KernelEvalPlus AutoResearch Round 3: RN_01 rms_norm optimization (fp32, hidden_size=7168) | repair | sm90 | cuda-cpp |
| [exp-r-20260322-131009-09ff7fa1](../sources/experiences/exp-r-20260322-131009-09ff7fa1.md) | KernelEvalPlus AutoResearch Round 1 - RN_04 fp32_rms_norm_llama3_8b_hs4096 | repair | sm90 | cuda-cpp |
| [exp-r-20260322-131316-d7f07322](../sources/experiences/exp-r-20260322-131316-d7f07322.md) | KernelEvalPlus AutoResearch Round 2: RN_04 fp32_rms_norm_llama3_8b_hs4096 | repair | sm90 | cuda-cpp |
| [exp-r-20260322-131628-2e88bf69](../sources/experiences/exp-r-20260322-131628-2e88bf69.md) | KernelEvalPlus AutoResearch Round 3: RN_04 fp32_rms_norm_llama3_8b_hs4096 | repair | sm90 | cuda-cpp |
| [exp-r-20260322-141027-6b2e52e6](../sources/experiences/exp-r-20260322-141027-6b2e52e6.md) | KernelEvalPlus RMS Norm optimization (RN_04, fp32, LLaMA-3-8B, hidden_size=4096) | repair | sm90 | cuda-cpp |
| [exp-r-20260322-141853-10880a72](../sources/experiences/exp-r-20260322-141853-10880a72.md) | AutoResearch Round 2: RMS Norm kernel optimization for LLaMA-3-8B (hidden_size=4096) | repair | sm90 | cuda-cpp |
| [exp-r-20260322-142658-33768e6c](../sources/experiences/exp-r-20260322-142658-33768e6c.md) | AutoResearch Round 3: fp32 RMS Norm kernel optimization for LLaMA-3-8B (hidden_size=4096), task RN_04 | repair | sm90 | cuda-cpp |
| [exp-r-20260322-160442-fa91e764](../sources/experiences/exp-r-20260322-160442-fa91e764.md) | KernelEvalPlus AutoResearch Round 1 - RMS Norm optimization for LLaMA models | repair | sm90 | cuda-cpp |
| [exp-r-20260508-120004-bf16-intrinsic-undefined](../sources/experiences/exp-r-20260508-120004-bf16-intrinsic-undefined.md) | exp-r-20260508-120004-bf16-intrinsic-undefined | repair | sm90 | cuda-cpp |

## reduction

| ID | Title | Type | Architectures | Languages |
|----|-------|------|--------------|-----------|
| [exp-a-20260324-085331-7e045fdc](../sources/experiences/exp-a-20260324-085331-7e045fdc.md) | 请先调用 rag_search_experiences，查询与 'cuda shared memory bank conflict reduction' 相关的历史经验，总结找到的模式和建议，然后 finish。不要修改代码，不要使用
  web_search。 | analysis | sm90 | cuda-cpp |
| [exp-a-20260324-091458-7e045fdc](../sources/experiences/exp-a-20260324-091458-7e045fdc.md) | 请先调用 rag_search_experiences，查询与 'cuda shared memory bank conflict reduction' 相关的历史经验，总结找到的模式和建议，然后 finish。不要修改代码，不要使用
  web_search。 | analysis | sm90 | cuda-cpp |
| [exp-a-20260325-100250-12da447b](../sources/experiences/exp-a-20260325-100250-12da447b.md) | ## Task
Create v4 of the top-k sampling kernel for TK_09. The goal is to reduce kernel latency (currently ~4.7ms for all batch sizes) by eliminating the expensive curand_init overhead.

The interface is:
extern "C" void topk_kernel(const float* probs, int64_t* samples, int batch_size, int vocab_size, int k)

Task: Given probs[batch_size, vocab_size=256], find top-k (k=6) indices by probability, then sample one index from those top-k using the original probabilities as weights.

Optimization hypothesis for v4: Replace expensive curand_init with a fast inline random number generator (e.g., xorshift or LCG) seeded with batch_idx and a global seed passed via kernel argument. This avoids the ~4ms overhead from curand state initialization.

Algorithm:
1. One warp (32 threads) per batch item
2. Each thread loads 8 elements (vocab_size=256, 256/32=8)
3. Find top-k=6 using k rounds of warp-wide argmax with shuffle
4. Lane 0 generates random number using fast LCG: seed = batch_idx * 6364136223846793005ULL + 1442695040888963407ULL
5. Sample from top-k using cumulative probability

Fast LCG random in [0,1):
```
uint64_t state = (uint64_t)batch_idx * 6364136223846793005ULL + 1442695040888963407ULL;
state ^= (uint64_t)clock64();
state = state * 6364136223846793005ULL + 1442695040888963407ULL;
float r = (float)(state >> 11) * (1.0f / (float)(1ULL << 53));
```

Steps:
1. Create directory: /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_093822_1fb580bd/attempts/TK_09/r1/v4/
2. Write kernel.cu there (pure CUDA, no torch headers)
3. Run test: cd /home/qinhaiyan/Research/kernelevalplus && /home/qinhaiyan/anaconda3/envs/robust_kbench/bin/python llm_kernel_test/unified_test_runner.py --test --attempt-path /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_093822_1fb580bd/attempts/TK_09/r1/v4 --definition /home/qinhaiyan/Research/kernelevalplus/definitions/topk/qwen/fp32_top_k_sampling_qwen2_5_7b_k6_ne0256.json
4. Parse test_results.json and report latency_ms for each config and performance_ratio

## Goal
kernel.cu compiles, correctness passes, latency < 1ms for batch_1, performance_ratio > 0

## Constraints
- kernel.cu must be pure CUDA - no torch headers
- Entry function: extern "C" void topk_kernel(const float* probs, int64_t* samples, int batch_size, int vocab_size, int k)
- Must correctly sample from top-k distribution
- Use fast LCG instead of curand_init to reduce latency
- One warp per batch item

## Verification
After writing the code, run this command to verify:
```
cd /home/qinhaiyan/Research/kernelevalplus && /home/qinhaiyan/anaconda3/envs/robust_kbench/bin/python llm_kernel_test/unified_test_runner.py --test --attempt-path /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_093822_1fb580bd/attempts/TK_09/r1/v4 --definition /home/qinhaiyan/Research/kernelevalplus/definitions/topk/qwen/fp32_top_k_sampling_qwen2_5_7b_k6_ne0256.json
```

## Critical Context
The auto_wrapper.cu declares: extern "C" void topk_kernel(const float* probs, int64_t* samples, int batch_size, int vocab_size, int k). The correctness test verifies that each output sample is one of the top-k indices. The performance metric is gbps = data_size_MB / latency_ms. For batch_1, data is only 1KB so gbps will be tiny unless latency is very low. The baseline gbps is 0.06 for batch_1. Current v3 latency is 4.7ms for all batches - this is dominated by curand_init overhead. Removing curand_init should bring latency down to <0.1ms.

## Seeded Files
The following files have been placed in your workspace (`/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_093822_1fb580bd/task_001_20260325_093824/coder_workspace/coder_1774403923_2128`):
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_093822_1fb580bd/task_001_20260325_093824/coder_workspace/coder_1774403923_2128/iterations.json`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_093822_1fb580bd/task_001_20260325_093824/coder_workspace/coder_1774403923_2128/experiment_summary.json`
Read them first using their **absolute paths** shown above.

## Workspace & Output Placement
- Your workspace root is: `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_093822_1fb580bd/task_001_20260325_093824/coder_workspace/coder_1774403923_2128`
- **IMPORTANT**: Seeded files are at `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_093822_1fb580bd/task_001_20260325_093824/coder_workspace/coder_1774403923_2128/<filename>`, NOT in any subdirectory.
- Use `sandbox_execute(command="ls /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_093822_1fb580bd/task_001_20260325_093824/coder_workspace/coder_1774403923_2128")` if you need to verify what files exist.
- Prefer writing final outputs in the workspace root.
- If a file like `program.md` is not present, do NOT attempt to read it; rely on the provided context instead.

## Workflow
1. Load relevant skills if specified above
2. Read seeded files to understand existing code
3. Write/modify code to achieve the goal. If the code is long, split it across multiple writes/edits and keep files consistent after each chunk.
4. Run verification command (if provided) to check correctness
5. If verification fails, diagnose and fix
6. Call `finish(result="<see format below>", success=True/False)`

**finish result format** (use these exact section headers):
```
SUMMARY: <one-line description of what you did>
DECISIONS:
- <key decision 1>
- <key decision 2>
ISSUES:
- <known issue or remaining problem>
```
If no decisions or issues, omit that section. | analysis | sm90 | cuda-cpp |
| [exp-a-20260325-144943-f5b0965a](../sources/experiences/exp-a-20260325-144943-f5b0965a.md) | ## Task
Seed a pure CUDA kernel from baseline for RN_06 rms_norm task

## Goal
Create kernel.cu in attempt dir, strip all torch/c10/ATen bindings, run unified_test_runner to verify baseline correctness

## Constraints
- kernel.cu must have extern C void rms_norm_kernel(...) signature with raw pointers
- No torch/, at::, c10::, PYBIND11_MODULE
- Run test: python llm_kernel_test/unified_test_runner.py --test --attempt-path <dir> --definition <def_json>

## Verification
After writing the code, run this command to verify:
```
python llm_kernel_test/unified_test_runner.py --test --attempt-path /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_144346_d0734006/attempts/RN_06/r1/v1 --definition /home/qinhaiyan/Research/kernelevalplus/definitions/rms_norm/qwen/fp32_rms_norm_qwen2_5_7b_hs5120.json
```

## Skills
Load the following skills for domain knowledge: `kernelevalplus-baseline-loop`
Use `skill(name=...)` to load each skill before writing code.

## Critical Context
Baseline path: /home/qinhaiyan/Research/kernelevalplus/Baseline/rms_norm/fp32_rms_norm_qwen2_5_7b_hs5120.cu
Definition path: /home/qinhaiyan/Research/kernelevalplus/definitions/rms_norm/qwen/fp32_rms_norm_qwen2_5_7b_hs5120.json
Entry point: rms_norm_kernel
Op type: rms_norm
hidden_size=5120
Optimizations from baseline: vectorized float4 loads, warp-level reduction

## Seeded Files
The following files have been placed in your workspace (`/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_144346_d0734006/task_001_20260325_144348/coder_workspace/coder_1774421149_4864`):
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_144346_d0734006/task_001_20260325_144348/coder_workspace/coder_1774421149_4864/task_context.json`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_144346_d0734006/task_001_20260325_144348/coder_workspace/coder_1774421149_4864/iterations.json`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_144346_d0734006/task_001_20260325_144348/coder_workspace/coder_1774421149_4864/llm_calls.json`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_144346_d0734006/task_001_20260325_144348/coder_workspace/coder_1774421149_4864/round_state.json`
Read them first using their **absolute paths** shown above.

## Workspace & Output Placement
- Your workspace root is: `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_144346_d0734006/task_001_20260325_144348/coder_workspace/coder_1774421149_4864`
- **IMPORTANT**: Seeded files are at `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_144346_d0734006/task_001_20260325_144348/coder_workspace/coder_1774421149_4864/<filename>`, NOT in any subdirectory.
- Use `sandbox_execute(command="ls /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_144346_d0734006/task_001_20260325_144348/coder_workspace/coder_1774421149_4864")` if you need to verify what files exist.
- Prefer writing final outputs in the workspace root.
- If a file like `program.md` is not present, do NOT attempt to read it; rely on the provided context instead.

## Workflow
1. Load relevant skills if specified above
2. Read seeded files to understand existing code
3. Write/modify code to achieve the goal. If the code is long, split it across multiple writes/edits and keep files consistent after each chunk.
4. Run verification command (if provided) to check correctness
5. If verification fails, diagnose and fix
6. Call `finish(result="<see format below>", success=True/False)`

**finish result format** (use these exact section headers):
```
SUMMARY: <one-line description of what you did>
DECISIONS:
- <key decision 1>
- <key decision 2>
ISSUES:
- <known issue or remaining problem>
```
If no decisions or issues, omit that section. | analysis | sm90 | cuda-cpp |
| [exp-r-20260317-155302-fabb47a1](../sources/experiences/exp-r-20260317-155302-fabb47a1.md) | Metal reduce operator implementation on macOS | repair | sm90 | cuda-cpp |
| [exp-r-20260318-181359-241d741c](../sources/experiences/exp-r-20260318-181359-241d741c.md) | Implement Metal reduce operator using fp16 on macOS | repair | sm90 | cuda-cpp |

## relu

| ID | Title | Type | Architectures | Languages |
|----|-------|------|--------------|-----------|
| [exp-r-20260318-190221-5cf8738f](../sources/experiences/exp-r-20260318-190221-5cf8738f.md) | kernelbench level_1 task_20 - LeakyReLU activation | repair | sm90 | cuda-cpp |
| [exp-r-20260319-203829-bd43b197](../sources/experiences/exp-r-20260319-203829-bd43b197.md) | KernelBench level_1 task_20: LeakyReLU activation kernel | repair | sm90 | cuda-cpp |
| [exp-r-20260319-205516-69cca6ab](../sources/experiences/exp-r-20260319-205516-69cca6ab.md) | KernelBench level_1 task_20: LeakyReLU activation optimization | repair | sm90 | cuda-cpp |
| [exp-r-20260320-133920-1e02b61f](../sources/experiences/exp-r-20260320-133920-1e02b61f.md) | KernelBench level_1 task_19: ReLU activation element-wise operation | repair | sm90 | cuda-cpp |
| [exp-r-20260320-140144-9cae5ab1](../sources/experiences/exp-r-20260320-140144-9cae5ab1.md) | KernelBench level_1 task_19: ReLU activation element-wise operation with input shape (batch_size=16, dim=16384) | repair | sm90 | cuda-cpp |
| [exp-r-20260320-140623-1e02b61f](../sources/experiences/exp-r-20260320-140623-1e02b61f.md) | KernelBench level_1 task_19: ReLU activation element-wise operation | repair | sm90 | cuda-cpp |
| [exp-r-20260320-141730-2f00c745](../sources/experiences/exp-r-20260320-141730-2f00c745.md) | KernelBench level_1 task_20: LeakyReLU activation | repair | sm90 | cuda-cpp |

## rmsnorm

| ID | Title | Type | Architectures | Languages |
|----|-------|------|--------------|-----------|
| [exp-o-20260513-100004-rmsnorm-warp-level-reduction](../sources/experiences/exp-o-20260513-100004-rmsnorm-warp-level-reduction.md) | FlashInfer-Bench RMSNorm: warp-level reduction achieves 4.7x-5.4x speedup | optimization | sm90 | cuda-cpp |

## softmax

| ID | Title | Type | Architectures | Languages |
|----|-------|------|--------------|-----------|
| [exp-a-20260325-191646-f77b236f](../sources/experiences/exp-a-20260325-191646-f77b236f.md) | ## Task
Fix the flash attention kernel for FA_14 (fp32_flash_attention_qwen2_5_7b_q4_0_cache4096). The kernel must:
1. Load Q from [batch][head][head_dim] layout
2. Load K from Q4_0 KV cache with layout [seq_len][num_heads][head_dim] flattened. Each block_q4_0 stores 16 fp16 values (packed as 8 pairs of 4-bit). Total K blocks = seq_len * num_heads * head_dim / 16
3. Implement correct online softmax: acc = softmax(Q @ K^T / sqrt(d)) @ V
4. No CUDA errors (illegal memory access, etc)
5. Pure CUDA kernel - no torch/ATen headers

## Goal
Compile with nvcc -O3, pass correctness tests, and achieve measurable speedup over baseline

## Constraints
- No torch/*, at::, c10::, PYBIND11_MODULE
- extern "C" void flash_attn_kernel(...) signature
- Pure CUDA with cudaMalloc/cudaMemcpy if needed
- 128 threads per block for 28 heads

## Verification
After writing the code, run this command to verify:
```
python llm_kernel_test/unified_test_runner.py --test --attempt-path /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_182611_214fd041/attempts/FA_14/r3/v1 --definition /home/qinhaiyan/Research/kernelevalplus/definitions/flash_attention/FA_14.json
```

## Skills
Load the following skills for domain knowledge: `kernelevalplus-baseline-loop`
Use `skill(name=...)` to load each skill before writing code.

## Critical Context
FA_14: batch_size=var (tested 1/8/512), seq_len=4096, num_heads=28, head_dim=128. Q4_0 block = {half d; uint8_t qs[16]}. KV cache shapes: key_cache [4096,28,128] as int8 (flattened blocks), value_cache same. Query: [batch,28,128] as float32. Output: [batch,28,128] as float32. Test configs: batch_1, batch_8, batch_512. Previous attempt had 'illegal memory access' errors. The correct K flat index = s*num_heads*HEAD_DIM + h*HEAD_DIM + i, and block_idx = flat/16.

## Seeded Files
The following files have been placed in your workspace (`/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_182611_214fd041/task_003_20260325_190826/coder_workspace/coder_1774437175_7168`):
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_182611_214fd041/task_003_20260325_190826/coder_workspace/coder_1774437175_7168//home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_182611_214fd041/attempts/FA_14/r3/v1/kernel.cu`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_182611_214fd041/task_003_20260325_190826/coder_workspace/coder_1774437175_7168/task_context.json`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_182611_214fd041/task_003_20260325_190826/coder_workspace/coder_1774437175_7168/iterations.json`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_182611_214fd041/task_003_20260325_190826/coder_workspace/coder_1774437175_7168/round_state.json`
Read them first using their **absolute paths** shown above.

## Previous Errors (avoid repeating)
- CUDA error: an illegal memory access was encountered
- CUDA error: CUBLAS_STATUS_ALLOC_FAILED for batch_1

## Workspace & Output Placement
- Your workspace root is: `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_182611_214fd041/task_003_20260325_190826/coder_workspace/coder_1774437175_7168`
- **IMPORTANT**: Seeded files are at `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_182611_214fd041/task_003_20260325_190826/coder_workspace/coder_1774437175_7168/<filename>`, NOT in any subdirectory.
- Use `sandbox_execute(command="ls /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260325_182611_214fd041/task_003_20260325_190826/coder_workspace/coder_1774437175_7168")` if you need to verify what files exist.
- Prefer writing final outputs in the workspace root.
- If a file like `program.md` is not present, do NOT attempt to read it; rely on the provided context instead.

## Workflow
1. Load relevant skills if specified above
2. Read seeded files to understand existing code
3. Write/modify code to achieve the goal. If the code is long, split it across multiple writes/edits and keep files consistent after each chunk.
4. Run verification command (if provided) to check correctness
5. If verification fails, diagnose and fix
6. Call `finish(result="<see format below>", success=True/False)`

**finish result format** (use these exact section headers):
```
SUMMARY: <one-line description of what you did>
DECISIONS:
- <key decision 1>
- <key decision 2>
ISSUES:
- <known issue or remaining problem>
```
If no decisions or issues, omit that section. | analysis | sm90 | cuda-cpp |
| [exp-a-20260326-095034-2fac4e75](../sources/experiences/exp-a-20260326-095034-2fac4e75.md) | ## Task
Optimize the flash attention kernel for FA_15 (Qwen2.5-7B Q4_0 KV cache). The baseline (v1) achieves 0.0046x speedup vs baseline. Apply these optimizations: (1) Grid-stride loop over sequence length instead of one-thread-per-position, (2) Shared memory tiling for KV cache dequantization, (3) Load K/V tiles once into shared memory, reuse across Q iterations, (4) Better memory coalescing for Q loads, (5) Keep warp-level softmax reductions. Task definition: /home/qinhaiyan/Research/kernelevalplus/definitions/flash_attention/qwen/fp32_flash_attention_qwen2_5_7b_q4_0_cache8192.json. Write kernel.cu to /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/attempts/FA_15/r1/v2/kernel.cu. Keep extern "C" void flash_attn_kernel(...) entry. Pure CUDA only, no torch/ATen/c10. Use cuda_fp16.h for half precision.

## Goal
Achieve correctness (NMSE < 0.05) with improved performance over v1 baseline (0.0046x).

## Verification
After writing the code, run this command to verify:
```
cd /home/qinhaiyan/Research/kernelevalplus && python llm_kernel_test/unified_test_runner.py --test --attempt-path /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/attempts/FA_15/r1/v2 --definition /home/qinhaiyan/Research/kernelevalplus/definitions/flash_attention/qwen/fp32_flash_attention_qwen2_5_7b_q4_0_cache8192.json 2>&1 | tail -30
```

## Seeded Files
The following files have been placed in your workspace (`/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/task_001_20260326_092648/coder_workspace/coder_1774489370_2224`):
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/task_001_20260326_092648/coder_workspace/coder_1774489370_2224/kernel_v1.cu`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/task_001_20260326_092648/coder_workspace/coder_1774489370_2224/task_context.json`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/task_001_20260326_092648/coder_workspace/coder_1774489370_2224/iterations.json`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/task_001_20260326_092648/coder_workspace/coder_1774489370_2224/terminal_output.json`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/task_001_20260326_092648/coder_workspace/coder_1774489370_2224/round_state.json`
Read them first using their **absolute paths** shown above.

## Workspace & Output Placement
- Your workspace root is: `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/task_001_20260326_092648/coder_workspace/coder_1774489370_2224`
- **IMPORTANT**: Seeded files are at `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/task_001_20260326_092648/coder_workspace/coder_1774489370_2224/<filename>`, NOT in any subdirectory.
- Use `sandbox_execute(command="ls /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/task_001_20260326_092648/coder_workspace/coder_1774489370_2224")` if you need to verify what files exist.
- Prefer writing final outputs in the workspace root.
- If a file like `program.md` is not present, do NOT attempt to read it; rely on the provided context instead.

## Workflow
1. Load relevant skills if specified above
2. Read seeded files to understand existing code
3. Write/modify code to achieve the goal. If the code is long, split it across multiple writes/edits and keep files consistent after each chunk.
4. Run verification command (if provided) to check correctness
5. If verification fails, diagnose and fix
6. Call `finish(result="<see format below>", success=True/False)`

**finish result format** (use these exact section headers):
```
SUMMARY: <one-line description of what you did>
DECISIONS:
- <key decision 1>
- <key decision 2>
ISSUES:
- <known issue or remaining problem>
```
If no decisions or issues, omit that section. | analysis | sm90 | cuda-cpp |
| [exp-a-20260326-103616-7d4a9433](../sources/experiences/exp-a-20260326-103616-7d4a9433.md) | ## Task
Write a pure CUDA flash attention kernel for Q4_0 KV cache dequantization

## Goal
Create kernel.cu with extern C flash_attn_kernel entry point, implement flash attention with Q4_0 KV dequantization, compile with nvcc -O3 -arch=sm_80, verify compilation succeeds

## Constraints
- Must use raw CUDA/C++ only - no torch/ATen/c10 headers
- Must export extern C void flash_attn_kernel(...)
- Use float32 Q4_0 dequantization: 18 bytes per 32 values (2 bytes scale fp16 + 16 bytes packed 4-bit)
- Implement online softmax for flash attention
- Definition: query[B,28,128] float32, kv_cache[8192,28,128] int8 Q4_0, output[B,28,128] float32

## Verification
After writing the code, run this command to verify:
```
nvcc -O3 -arch=sm_80 /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/attempts/FA_15/r2/v1/kernel.cu -o /tmp/fa_test -lcudart 2>&1
```

## Seeded Files
The following files have been placed in your workspace (`/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/task_002_20260326_100853/coder_workspace/coder_1774492142_6928`):
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/task_002_20260326_100853/coder_workspace/coder_1774492142_6928/task_context.json`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/task_002_20260326_100853/coder_workspace/coder_1774492142_6928/iterations.json`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/task_002_20260326_100853/coder_workspace/coder_1774492142_6928/round_state.json`
Read them first using their **absolute paths** shown above.

## Workspace & Output Placement
- Your workspace root is: `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/task_002_20260326_100853/coder_workspace/coder_1774492142_6928`
- **IMPORTANT**: Seeded files are at `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/task_002_20260326_100853/coder_workspace/coder_1774492142_6928/<filename>`, NOT in any subdirectory.
- Use `sandbox_execute(command="ls /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_092646_368f2aea/task_002_20260326_100853/coder_workspace/coder_1774492142_6928")` if you need to verify what files exist.
- Prefer writing final outputs in the workspace root.
- If a file like `program.md` is not present, do NOT attempt to read it; rely on the provided context instead.

## Workflow
1. Load relevant skills if specified above
2. Read seeded files to understand existing code
3. Write/modify code to achieve the goal. If the code is long, split it across multiple writes/edits and keep files consistent after each chunk.
4. Run verification command (if provided) to check correctness
5. If verification fails, diagnose and fix
6. Call `finish(result="<see format below>", success=True/False)`

**finish result format** (use these exact section headers):
```
SUMMARY: <one-line description of what you did>
DECISIONS:
- <key decision 1>
- <key decision 2>
ISSUES:
- <known issue or remaining problem>
```
If no decisions or issues, omit that section. | analysis | sm90 | cuda-cpp |
| [exp-a-20260326-173130-2b19071b](../sources/experiences/exp-a-20260326-173130-2b19071b.md) | ## Task
Optimize flash attention kernel for FA_12 task

## Goal
Improve speedup from 0.005 to >0.5 with correct output

## Constraints
- Pure CUDA kernel - no torch/ATen/c10 includes
- Entry function: flash_attn_kernel
- Maintain correctness (pass reference comparison)

## Verification
After writing the code, run this command to verify:
```
cd /home/qinhaiyan/Research/kernelevalplus && python llm_kernel_test/unified_test_runner.py --test --attempt-path /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_172000_341513fc/attempts/FA_12/r1/v2 --definition /home/qinhaiyan/Research/kernelevalplus/definitions/flash_attention/qwen/fp32_flash_attention_qwen2_5_7b_f16_cache8192.json
```

## Critical Context
Task: fp32_flash_attention_qwen2_5_7b_f16_cache8192
- batch_size: variable, num_heads: 28, head_dim: 128, seq_len: 8192
- query: float32[B, 28, 128], key_cache: float16[8192, 28, 128], value_cache: float16[8192, 28, 128]
- GPU: compute_80 (Ampere)
- Scale factor: 1.0f / 11.3137085f
- Baseline kernel has BLOCK_SIZE=512, TILE_SIZE=2048, scalar KV loads (very slow), speedup=0.005

Optimize with: vectorized half2 loads for K/V, increased BLOCK_SIZE, shared memory tiling, online softmax.

## Seeded Files
The following files have been placed in your workspace (`/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_172000_341513fc/task_001_20260326_172008/coder_workspace/coder_1774517177_0096`):
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_172000_341513fc/task_001_20260326_172008/coder_workspace/coder_1774517177_0096/task_context.json`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_172000_341513fc/task_001_20260326_172008/coder_workspace/coder_1774517177_0096/iterations.json`
- `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_172000_341513fc/task_001_20260326_172008/coder_workspace/coder_1774517177_0096/round_state.json`
Read them first using their **absolute paths** shown above.

## Workspace & Output Placement
- Your workspace root is: `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_172000_341513fc/task_001_20260326_172008/coder_workspace/coder_1774517177_0096`
- **IMPORTANT**: Seeded files are at `/home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_172000_341513fc/task_001_20260326_172008/coder_workspace/coder_1774517177_0096/<filename>`, NOT in any subdirectory.
- Use `sandbox_execute(command="ls /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_20260326_172000_341513fc/task_001_20260326_172008/coder_workspace/coder_1774517177_0096")` if you need to verify what files exist.
- Prefer writing final outputs in the workspace root.
- If a file like `program.md` is not present, do NOT attempt to read it; rely on the provided context instead.

## Workflow
1. Load relevant skills if specified above
2. Read seeded files to understand existing code
3. Write/modify code to achieve the goal. If the code is long, split it across multiple writes/edits and keep files consistent after each chunk.
4. Run verification command (if provided) to check correctness
5. If verification fails, diagnose and fix
6. Call `finish(result="<see format below>", success=True/False)`

**finish result format** (use these exact section headers):
```
SUMMARY: <one-line description of what you did>
DECISIONS:
- <key decision 1>
- <key decision 2>
ISSUES:
- <known issue or remaining problem>
```
If no decisions or issues, omit that section. | analysis | sm90 | cuda-cpp |

## topk

| ID | Title | Type | Architectures | Languages |
|----|-------|------|--------------|-----------|
| [exp-i-20260312-105131-ba0592fe](../sources/experiences/exp-i-20260312-105131-ba0592fe.md) | fp32_top_k_sampling_qwen2.5-7b_k8_ne0256 | implementation | sm90 | cuda-cpp |
| [exp-i-20260314-152716-9a71808e](../sources/experiences/exp-i-20260314-152716-9a71808e.md) | fp32_top_k_sampling_llama3-8b_k6_ne0160 | implementation | sm90 | cuda-cpp |
| [exp-i-20260314-170313-9a71808e](../sources/experiences/exp-i-20260314-170313-9a71808e.md) | fp32_top_k_sampling_llama3-8b_k6_ne0160 | implementation | sm90 | cuda-cpp |
| [exp-i-20260314-172401-7b9a4136](../sources/experiences/exp-i-20260314-172401-7b9a4136.md) | fp32_top_k_sampling_llama3-8b_k6_ne0256 | implementation | sm90 | cuda-cpp |
| [exp-i-20260314-174053-992cc552](../sources/experiences/exp-i-20260314-174053-992cc552.md) | fp32_top_k_sampling_llama3-8b_k8_ne0160 | implementation | sm90 | cuda-cpp |
| [exp-i-20260314-183233-b5320f62](../sources/experiences/exp-i-20260314-183233-b5320f62.md) | fp32_top_k_sampling_llama3-8b_k8_ne0256 | implementation | sm90 | cuda-cpp |
| [exp-i-20260314-185636-4b87bb58](../sources/experiences/exp-i-20260314-185636-4b87bb58.md) | fp32_top_k_sampling_llama3_8b_k6 | implementation | sm90 | cuda-cpp |
| [exp-i-20260314-195604-33c38a5d](../sources/experiences/exp-i-20260314-195604-33c38a5d.md) | fp32_top_k_sampling_llama3_8b_k8 | implementation | sm90 | cuda-cpp |
| [exp-i-20260314-201753-e78afaee](../sources/experiences/exp-i-20260314-201753-e78afaee.md) | fp32_top_k_sampling_qwen2.5-7b_k6_ne0160 | implementation | sm90 | cuda-cpp |
| [exp-i-20260314-203435-3a499800](../sources/experiences/exp-i-20260314-203435-3a499800.md) | fp32_top_k_sampling_qwen2.5-7b_k6_ne0256 | implementation | sm90 | cuda-cpp |
| [exp-i-20260314-212316-ba0592fe](../sources/experiences/exp-i-20260314-212316-ba0592fe.md) | fp32_top_k_sampling_qwen2.5-7b_k8_ne0256 | implementation | sm90 | cuda-cpp |
| [exp-i-20260314-213658-5b6a321a](../sources/experiences/exp-i-20260314-213658-5b6a321a.md) | fp32_top_k_sampling_qwen2_5_7b_k8 | implementation | sm90 | cuda-cpp |
| [exp-i-20260507-topk-speedup-156pct](../sources/experiences/exp-i-20260507-topk-speedup-156pct.md) | TK_05 (topk) is the only kernel to achieve >1x speedup: 1.5664x with 0.014ms latency vs 0.022ms baseline | implementation | sm90 | cuda-cpp |
| [exp-o-20260324-175225-a14b261c](../sources/experiences/exp-o-20260324-175225-a14b261c.md) | fp32_top_k_sampling_llama3_8b_k8 | optimization | sm90 | cuda-cpp |
| [exp-o-20260324-180317-1365822b](../sources/experiences/exp-o-20260324-180317-1365822b.md) | fp32_top_k_sampling_llama3_8b_k8 | optimization | sm90 | cuda-cpp |
| [exp-o-20260325-073648-c4965aad](../sources/experiences/exp-o-20260325-073648-c4965aad.md) | fp32_top_k_sampling_qwen2_5_7b_k8_ne0160 | optimization | sm90 | cuda-cpp |
| [exp-o-20260325-074027-38b02cab](../sources/experiences/exp-o-20260325-074027-38b02cab.md) | fp32_top_k_sampling_qwen2_5_7b_k8_ne0160 | optimization | sm90 | cuda-cpp |
| [exp-o-20260325-082251-2f09a524](../sources/experiences/exp-o-20260325-082251-2f09a524.md) | fp32_top_k_sampling_qwen2_5_7b_k8_ne0160 | optimization | sm90 | cuda-cpp |
| [exp-o-20260325-100754-825e6ce7](../sources/experiences/exp-o-20260325-100754-825e6ce7.md) | fp32_top_k_sampling_qwen2_5_7b_k6_ne0256 | optimization | sm90 | cuda-cpp |
| [exp-o-20260325-101903-3a2ff77a](../sources/experiences/exp-o-20260325-101903-3a2ff77a.md) | fp32_top_k_sampling_qwen2_5_7b_k6_ne0256 | optimization | sm90 | cuda-cpp |
| [exp-r-20260327-182901-8a499e71](../sources/experiences/exp-r-20260327-182901-8a499e71.md) | fp32_top_k_sampling_qwen2_5_7b_k6_ne0256 | repair | sm90 | cuda-cpp |

