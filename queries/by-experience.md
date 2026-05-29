# Query: By Experience

> Auto-generated. Do not edit manually.

## attention

| ID | Title | Type | Architectures | Languages |
|----|-------|------|--------------|-----------|
| [exp-i-20260506-flash-attention-kernel-eval-contract](../sources/experiences/exp-i-20260506-flash-attention-kernel-eval-contract.md) | KernelEval flash_attention CUDA kernel implementation contract | implementation | sm90 | cuda-cpp |
| [exp-i-20260519-0001-gqa-paged-decode-architecture](../sources/experiences/exp-i-20260519-0001-gqa-paged-decode-architecture.md) | GQA paged decode attention: architecture, kernel design, and correct run() signature | implementation | sm90 | cuda-cpp |
| [exp-i-20260519-0002-gqa-compilation-checklist](../sources/experiences/exp-i-20260519-0002-gqa-compilation-checklist.md) | GQA paged decode: compilation checklist for CUDA kernels | implementation | sm90 | cuda-cpp |
| [exp-i-20260519-0003-gqa-minimal-skeleton](../sources/experiences/exp-i-20260519-0003-gqa-minimal-skeleton.md) | GQA paged decode: minimal compile-able skeleton for new implementations | implementation | sm90 | cuda-cpp |
| [exp-o-20260506-flash-attention-tensor-core](../sources/experiences/exp-o-20260506-flash-attention-tensor-core.md) | Flash attention must leverage Tensor Cores for meaningful speedup | optimization | sm90 | cuda-cpp |
| [exp-o-20260507-flash-attention-tensor-core-no-speedup](../sources/experiences/exp-o-20260507-flash-attention-tensor-core-no-speedup.md) | All flash_attention kernels pass correctness but achieve 0.0025x-0.0425x speedup due to scalar-only compute | optimization | sm90 | cuda-cpp |
| [exp-o-20260529-0001-gqa-split-kv-parallelism](../sources/experiences/exp-o-20260529-0001-gqa-split-kv-parallelism.md) | GQA paged decode: split-KV parallelism is mandatory for competitive performance | optimization | sm90 | cuda-cpp |
| [exp-o-20260529-0002-gqa-single-warp-antipattern](../sources/experiences/exp-o-20260529-0002-gqa-single-warp-antipattern.md) | GQA paged decode: single-warp (32 threads) kernel is a fatal anti-pattern | optimization | sm90 | cuda-cpp |
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
| [exp-i-20260508-120001-sol-execbench-file-template](../sources/experiences/exp-i-20260508-120001-sol-execbench-file-template.md) | exp-i-20260508-120001-sol-execbench-file-template | implementation | sm90 | cuda-cpp |
| [exp-i-20260517-200010-int8-gemm-template](../sources/experiences/exp-i-20260517-200010-int8-gemm-template.md) | INT8 GEMM kernel implementation template for SOL-ExecBench | implementation | sm90 | cuda-cpp |
| [exp-i-20260517-200011-bf16-gemm-template](../sources/experiences/exp-i-20260517-200011-bf16-gemm-template.md) | BF16 GEMM kernel implementation template for SOL-ExecBench | implementation | sm90 | cuda-cpp |
| [exp-i-20260517-200012-sol-execbench-cpp-template](../sources/experiences/exp-i-20260517-200012-sol-execbench-cpp-template.md) | SOL-ExecBench cuda_cpp solution.json and source file template | implementation | sm90 | cuda-cpp |
| [exp-i-20260527-080001-cublaslt-fp16-gemm-best-config](../sources/experiences/exp-i-20260527-080001-cublaslt-fp16-gemm-best-config.md) | SOL-ExecBench GEMM: cublasLt FP16 reference implementation achieving 0.9999x | implementation | sm90 | cuda-cpp |
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
| [exp-r-20260508-120004-bf16-intrinsic-undefined](../sources/experiences/exp-r-20260508-120004-bf16-intrinsic-undefined.md) | exp-r-20260508-120004-bf16-intrinsic-undefined | repair | sm90 | cuda-cpp |

## rmsnorm

| ID | Title | Type | Architectures | Languages |
|----|-------|------|--------------|-----------|
| [exp-o-20260513-100004-rmsnorm-warp-level-reduction](../sources/experiences/exp-o-20260513-100004-rmsnorm-warp-level-reduction.md) | FlashInfer-Bench RMSNorm: warp-level reduction achieves 4.7x-5.4x speedup | optimization | sm90 | cuda-cpp |

## topk

| ID | Title | Type | Architectures | Languages |
|----|-------|------|--------------|-----------|
| [exp-i-20260507-topk-speedup-156pct](../sources/experiences/exp-i-20260507-topk-speedup-156pct.md) | TK_05 (topk) is the only kernel to achieve >1x speedup: 1.5664x with 0.014ms latency vs 0.022ms baseline | implementation | sm90 | cuda-cpp |

