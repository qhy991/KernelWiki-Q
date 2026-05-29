# Query: By Experience

> Auto-generated. Do not edit manually.

## activation

| ID | Title | Type | Architectures | Languages |
|----|-------|------|--------------|-----------|
| [exp-a-kd-20260518-0013](../sources/experiences/exp-a-kd-20260518-0013.md) | float_sigmoid | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0014](../sources/experiences/exp-a-kd-20260518-0014.md) | float_N8 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0032](../sources/experiences/exp-a-kd-20260518-0032.md) | relu_float_constref | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0033](../sources/experiences/exp-a-kd-20260518-0033.md) | Change functor parameter from const reference to pass-by-value for __half, add a | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0034](../sources/experiences/exp-a-kd-20260518-0034.md) | gelu_array_size4 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0035](../sources/experiences/exp-a-kd-20260518-0035.md) | Replace int(rhs.size()) with the template parameter N directly in the loop bound | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0036](../sources/experiences/exp-a-kd-20260518-0036.md) | gelu_erff_float | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0052](../sources/experiences/exp-a-kd-20260518-0052.md) | conv3d_large_analytic | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0064](../sources/experiences/exp-a-kd-20260518-0064.md) | int_alpha_only_8 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0199](../sources/experiences/exp-a-kd-20260518-0199.md) | awq_medium_gated | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0201](../sources/experiences/exp-a-kd-20260518-0201.md) | shared_scale_large | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0286](../sources/experiences/exp-a-kd-20260518-0286.md) | f16_medium | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0307](../sources/experiences/exp-a-kd-20260518-0307.md) | Fuse the gated activation and per-expert scaling into a single kernel, combining | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0308](../sources/experiences/exp-a-kd-20260518-0308.md) | Fuse the gated activation and elementwise scale into a single kernel that keeps  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0468](../sources/experiences/exp-a-kd-20260518-0468.md) | Vectorize memory access using float4 (128-bit) loads/stores so each thread proce | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0474](../sources/experiences/exp-a-kd-20260518-0474.md) | The f16x8 variant unrolls per-thread processing from 1 half2 to 4 half2 loads/co | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0478](../sources/experiences/exp-a-kd-20260518-0478.md) | Consolidate four separate half2 loads/stores into a single 128-bit LDST128BITS ( | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0513](../sources/experiences/exp-a-kd-20260518-0513.md) | Expanded each thread to process 4 half2 registers (8 half elements) instead of 1 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0520](../sources/experiences/exp-a-kd-20260518-0520.md) | gelu_tanh_bf16_4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0521](../sources/experiences/exp-a-kd-20260518-0521.md) | silu_bf16_4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0522](../sources/experiences/exp-a-kd-20260518-0522.md) | silu_fp16_4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0552](../sources/experiences/exp-a-kd-20260518-0552.md) | Increase elements per thread from 2 to 8 (4 half2 loads) to reduce total thread  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0553](../sources/experiences/exp-a-kd-20260518-0553.md) | Replaces 4 separate half2 loads with a single LDST128BITS 128-bit load into a lo | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0571](../sources/experiences/exp-a-kd-20260518-0571.md) | mask_0pct | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0573](../sources/experiences/exp-a-kd-20260518-0573.md) | mask_75pct | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0691](../sources/experiences/exp-a-kd-20260518-0691.md) | float_64epg_cand | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0692](../sources/experiences/exp-a-kd-20260518-0692.md) | sigmoid_naive_vs_tanh | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0703](../sources/experiences/exp-a-kd-20260518-0703.md) | swigluoai_scalar | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0824](../sources/experiences/exp-a-kd-20260518-0824.md) | half_256K | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0961](../sources/experiences/exp-a-kd-20260518-0961.md) | gelu_erf_vs_tanh_fp16 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0962](../sources/experiences/exp-a-kd-20260518-0962.md) | gelu_erf_vs_tanh_fp32 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1210](../sources/experiences/exp-a-kd-20260518-1210.md) | half_silu_mul | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1500](../sources/experiences/exp-a-kd-20260518-1500.md) | float_d2048 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1501](../sources/experiences/exp-a-kd-20260518-1501.md) | half_d4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1502](../sources/experiences/exp-a-kd-20260518-1502.md) | float_d2048 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0013-1](../sources/experiences/exp-a-kd-20260519-0013-1.md) | Replace the monolithic standalone class with a type alias to LinearCombinationGe | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0014-1](../sources/experiences/exp-a-kd-20260519-0014-1.md) | Wrap the per-element expf computation inside templated SigmoidArray and Multipli | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0015-1](../sources/experiences/exp-a-kd-20260519-0015-1.md) | Replace scalar half load/store with half2 vectorized operations: load two half v | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0032-1](../sources/experiences/exp-a-kd-20260519-0032-1.md) | Replace the two-arg const-reference functor with a single-arg pass-by-value over | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0033-1](../sources/experiences/exp-a-kd-20260519-0033-1.md) | Switch the value parameter from const reference (T const &) to pass-by-value (T) | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0034-1](../sources/experiences/exp-a-kd-20260519-0034-1.md) | Replace the runtime rhs.size() call with the compile-time template parameter N a | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0035-1](../sources/experiences/exp-a-kd-20260519-0035-1.md) | Replace int(rhs.size()) with the template parameter N directly in the #pragma un | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0036-1](../sources/experiences/exp-a-kd-20260519-0036-1.md) | Replace erff-based exact GELU with a Taylor approximation using fast_tanh backed | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0037-1](../sources/experiences/exp-a-kd-20260519-0037-1.md) | Replace the expensive erff SFU call with a GELU Taylor approximation using the s | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0063-1](../sources/experiences/exp-a-kd-20260519-0063-1.md) | When is_source_needed() returns false at compile time (beta=0, OnlyAlphaScaling  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0142-1](../sources/experiences/exp-a-kd-20260519-0142-1.md) | Replace the division scalar / sqrt(2) with a multiplication scalar * (1/sqrt(2)) | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0143-1](../sources/experiences/exp-a-kd-20260519-0143-1.md) | Replace scalar / sqrt(2) with scalar * (1/sqrt(2)), precomputing the reciprocal  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0170-1](../sources/experiences/exp-a-kd-20260519-0170-1.md) | Pack pairs of half values into uint32_t and issue tanh.approx.f16x2 PTX instruct | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0171-1](../sources/experiences/exp-a-kd-20260519-0171-1.md) | Pack consecutive __half pairs into uint32_t and issue tanh.approx.f16x2 PTX inst | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0305-1](../sources/experiences/exp-a-kd-20260519-0305-1.md) | Fuse the activation and scale kernels into a single kernel that reads GEMM outpu | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0305-2](../sources/experiences/exp-a-kd-20260519-0305-2.md) | Restructure to a 2D grid where blockIdx.x maps to row groups and blockIdx.y maps | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0306-1](../sources/experiences/exp-a-kd-20260519-0306-1.md) | Fuse the activation and scaling into a single templated kernel where the gated-S | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0307-1](../sources/experiences/exp-a-kd-20260519-0307-1.md) | Fuse the gated activation and per-expert scale multiply into a single kernel tha | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0308-1](../sources/experiences/exp-a-kd-20260519-0308-1.md) | Fuse the two sequential kernels into a single fused_gated_activation_kernel that | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0324-1](../sources/experiences/exp-a-kd-20260519-0324-1.md) | Fuse all 5 SiLU backward kernels into a single silu_bw_fused_kernel that compute | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0325-1](../sources/experiences/exp-a-kd-20260519-0325-1.md) | Fuse all five elementwise kernels into a single silu_bw_fused_kernel that loads  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0467-1](../sources/experiences/exp-a-kd-20260519-0467-1.md) | Use float4 (128-bit) vectorized loads/stores via the FLOAT4 macro to process 4 f | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0468-1](../sources/experiences/exp-a-kd-20260519-0468-1.md) | Use float4 (128-bit) vectorized loads/stores via the FLOAT4 macro to process 4 f | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0469-1](../sources/experiences/exp-a-kd-20260519-0469-1.md) | Use float4 (128-bit) vectorized loads/stores via the FLOAT4 macro so each thread | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0470-1](../sources/experiences/exp-a-kd-20260519-0470-1.md) | Vectorize loads/stores to half2 (two elements per thread) using the HALF2 reinte | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0471-1](../sources/experiences/exp-a-kd-20260519-0471-1.md) | Vectorize to half2 loads/stores so each thread processes two elements via the HA | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0472-1](../sources/experiences/exp-a-kd-20260519-0472-1.md) | Use half2 (32-bit) vectorized loads/stores via the HALF2 macro to process two ha | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0473-1](../sources/experiences/exp-a-kd-20260519-0473-1.md) | Increase per-thread processing from 2 to 8 half-elements (4x half2 registers), l | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0474-1](../sources/experiences/exp-a-kd-20260519-0474-1.md) | Increasing per-thread vectorization from half2 (2 elements) to half2×4 (8 elemen | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0475-1](../sources/experiences/exp-a-kd-20260519-0475-1.md) | Widen per-thread vectorization from half2 (2 elements) to 4×half2 (8 elements) b | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0476-1](../sources/experiences/exp-a-kd-20260519-0476-1.md) | Consolidate four half2 loads/stores into a single 128-bit LDST128BITS (float4 re | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0477-1](../sources/experiences/exp-a-kd-20260519-0477-1.md) | Replace four separate half2 loads/stores with a single LDST128BITS (float4 reint | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0478-1](../sources/experiences/exp-a-kd-20260519-0478-1.md) | Consolidate four separate half2 loads/stores into a single 128-bit LDST128BITS ( | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0507-1](../sources/experiences/exp-a-kd-20260519-0507-1.md) | Replace per-thread scalar float load/store with float4 vectorized load/store via | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0508-1](../sources/experiences/exp-a-kd-20260519-0508-1.md) | Vectorize to half2 processing: each thread loads a full 32-bit half2 (two adjace | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0509-1](../sources/experiences/exp-a-kd-20260519-0509-1.md) | Increase per-thread work from 2 to 8 half values by unpacking into 4 separate ha | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0510-1](../sources/experiences/exp-a-kd-20260519-0510-1.md) | Replace 4 separate half2 loads/stores with a single LDST128BITS (float4) 128-bit | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0511-1](../sources/experiences/exp-a-kd-20260519-0511-1.md) | Vectorize memory access using float4 (128-bit loads/stores) so each thread proce | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0512-1](../sources/experiences/exp-a-kd-20260519-0512-1.md) | Vectorize the kernel to process 2 half elements per thread using half2 packed lo | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0513-1](../sources/experiences/exp-a-kd-20260519-0513-1.md) | Attempted f16x8 expansion: each thread loads 4 half2 registers and processes 8 e | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0514-1](../sources/experiences/exp-a-kd-20260519-0514-1.md) | Replace 4 separate half2 loads/stores with a single LDST128BITS (reinterpret_cas | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0515-1](../sources/experiences/exp-a-kd-20260519-0515-1.md) | Vectorize load/store using float4 (16-byte) transactions so each thread processe | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0516-1](../sources/experiences/exp-a-kd-20260519-0516-1.md) | Vectorize loads/stores using float4 so each thread processes 4 elements via a si | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0517-1](../sources/experiences/exp-a-kd-20260519-0517-1.md) | Vectorize memory access using half2 (via HALF2 macro reinterpret_cast) to load a | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0518-1](../sources/experiences/exp-a-kd-20260519-0518-1.md) | Pack two half elements into a half2 register per thread using reinterpret_cast-b | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0519-1](../sources/experiences/exp-a-kd-20260519-0519-1.md) | Increase per-thread workload from 2 to 8 half elements by using 4 independent ha | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0520-1](../sources/experiences/exp-a-kd-20260519-0520-1.md) | The attempted optimization widened per-thread vectorization from f16x2 to f16x8  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0521-1](../sources/experiences/exp-a-kd-20260519-0521-1.md) | Replace 4 half2 load/store pairs with a single LDST128BITS (float4) 128-bit pack | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0522-1](../sources/experiences/exp-a-kd-20260519-0522-1.md) | Replace four named half2 registers and individual HALF2 loads/stores with local  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0550-1](../sources/experiences/exp-a-kd-20260519-0550-1.md) | Replace scalar float load/store with float4 vectorized load/store so each thread | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0551-1](../sources/experiences/exp-a-kd-20260519-0551-1.md) | Vectorize to half2 (32-bit) load/store so each thread processes two elements, ha | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0552-1](../sources/experiences/exp-a-kd-20260519-0552-1.md) | The after kernel increases elements-per-thread from 2 to 8 (4 half2 pairs), redu | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0553-1](../sources/experiences/exp-a-kd-20260519-0553-1.md) | Consolidate 4 separate half2 loads into one 128-bit LDST128BITS transaction and  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0586-1](../sources/experiences/exp-a-kd-20260519-0586-1.md) | Vectorize loads/stores using float4 so each thread processes 4 elements, reducin | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0587-1](../sources/experiences/exp-a-kd-20260519-0587-1.md) | Vectorize load/store with float4 (16-byte) transactions: each thread loads 4 flo | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0588-1](../sources/experiences/exp-a-kd-20260519-0588-1.md) | Pack two half elements per thread via half2 vectorized loads/stores, halving the | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0589-1](../sources/experiences/exp-a-kd-20260519-0589-1.md) | Vectorize memory access by processing two half values per thread via half2 reint | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0590-1](../sources/experiences/exp-a-kd-20260519-0590-1.md) | Vectorize the kernel to process 4 float elements per thread using float4 loads a | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0591-1](../sources/experiences/exp-a-kd-20260519-0591-1.md) | Replace scalar per-thread load/store with float4 vectorized access, processing 4 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0592-1](../sources/experiences/exp-a-kd-20260519-0592-1.md) | Process two half elements per thread using half2 vectorized loads and stores via | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0593-1](../sources/experiences/exp-a-kd-20260519-0593-1.md) | Replace scalar half loads/stores with half2 vectorized access via reinterpret_ca | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0885-1](../sources/experiences/exp-a-kd-20260519-0885-1.md) | Replace global iteration with direct thread-to-expert partitioning: compute expe | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0885-2](../sources/experiences/exp-a-kd-20260519-0885-2.md) | Restructure the loop to iterate only within a single expert's contiguous row ran | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0930-1](../sources/experiences/exp-a-kd-20260519-0930-1.md) | The after code moves the entire activation and multiply to float32 domain by cas | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0931-1](../sources/experiences/exp-a-kd-20260519-0931-1.md) | Refactor the activation function to accept and return float32 directly, and move | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0932-1](../sources/experiences/exp-a-kd-20260519-0932-1.md) | Move the multiply into fp32 domain: cast both gate and up to float, compute SiLU | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0933-1](../sources/experiences/exp-a-kd-20260519-0933-1.md) | Move all arithmetic to float32 domain: cast both gate and up inputs to float32 e | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0982-1](../sources/experiences/exp-a-kd-20260519-0982-1.md) | Add a per-thread expert_ids lookup with early return when the token is assigned  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0983-1](../sources/experiences/exp-a-kd-20260519-0983-1.md) | Add expert filtering via an early-return check on expert_ids[token_id / expert_s | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0984-1](../sources/experiences/exp-a-kd-20260519-0984-1.md) | Add expert-based early-return filtering: each thread checks expert_ids[token_id  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1010-1](../sources/experiences/exp-a-kd-20260519-1010-1.md) | Cache input data in shared memory during Pass-1 with bank-conflict padding (32-b | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1012-1](../sources/experiences/exp-a-kd-20260519-1012-1.md) | Fuse silu_and_mul activation and quantization into a single kernel so that the a | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1059-1](../sources/experiences/exp-a-kd-20260519-1059-1.md) | Fuse sigmoid, shared-memory bias backup, bias addition, and index assignment int | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1129-1](../sources/experiences/exp-a-kd-20260519-1129-1.md) | Replace naive 1/(1+expf(-x)) with the mathematically equivalent tanhf-based form | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1139-1](../sources/experiences/exp-a-kd-20260519-1139-1.md) | Replace scalar __ldg loads and stores with int4 (128-bit) vectorized loads and s | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1140-1](../sources/experiences/exp-a-kd-20260519-1140-1.md) | Replace explicit ternary clamp chains with fminf/fmaxf intrinsics and fold the f | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1141-1](../sources/experiences/exp-a-kd-20260519-1141-1.md) | Replace stride-2 scalar __ldg loads with int4 (128-bit) vectorized loads that fe | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1160-1](../sources/experiences/exp-a-kd-20260519-1160-1.md) | Replace runtime branching on scoring_func with C++ template parameter and if con | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1176-1](../sources/experiences/exp-a-kd-20260519-1176-1.md) | Upgrade from 128-bit int4 loads/stores to 256-bit u32x8_t via PTX ld.global.nc.v | analysis | sm100 | cuda-cpp |
| [exp-a-kd-20260519-1177-1](../sources/experiences/exp-a-kd-20260519-1177-1.md) | Replace 128-bit int4 loads/stores with 256-bit ld256/st256 using inline PTX (ld. | analysis | sm100 | cuda-cpp |
| [exp-a-kd-20260519-1177-2](../sources/experiences/exp-a-kd-20260519-1177-2.md) | Process __half2 pairs using __half22float2 for dual-lane upconversion, float2 si | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1178-1](../sources/experiences/exp-a-kd-20260519-1178-1.md) | Reinterpret loaded int4 data as packed __nv_bfloat162 pairs and compute SiLU-and | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1179-1](../sources/experiences/exp-a-kd-20260519-1179-1.md) | Replace scalar __half processing with packed __half2 SIMD operations: use __half | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1258-1](../sources/experiences/exp-a-kd-20260519-1258-1.md) | Fuse SiLU+Mul and quantization into a single kernel that loads gate and up vecto | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1259-1](../sources/experiences/exp-a-kd-20260519-1259-1.md) | Fuse SiLU+Mul and FP4 quantization into a single kernel so compute_silu_mul resu | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1260-1](../sources/experiences/exp-a-kd-20260519-1260-1.md) | Fuse SiLU activation and elementwise multiply into a single kernel that reads ga | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1261-1](../sources/experiences/exp-a-kd-20260519-1261-1.md) | Fuse SiLU activation and element-wise multiplication into a single kernel that l | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1321-1](../sources/experiences/exp-a-kd-20260519-1321-1.md) | Fuse the SiLU+mul activation and scaled int8 quantization into a single kernel w | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1322-1](../sources/experiences/exp-a-kd-20260519-1322-1.md) | Fuse SiLU-and-mul and scaled int8 quantization into a single kernel so the float | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1326-1](../sources/experiences/exp-a-kd-20260519-1326-1.md) | Replace conditional vectorization with vectorize_with_alignment which unconditio | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1398-1](../sources/experiences/exp-a-kd-20260519-1398-1.md) | Replace erf-based GELU with tanh-approximation GELU (GELU(x) = 0.5x(1 + tanh(bet | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1399-1](../sources/experiences/exp-a-kd-20260519-1399-1.md) | Replace erf-based exact GELU with the tanh polynomial approximation: 0.5f * f *  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1515-1](../sources/experiences/exp-a-kd-20260519-1515-1.md) | Introduce silu2_v2 that directly produces __nv_bfloat162 via make_bfloat162(__fl | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1556-1](../sources/experiences/exp-a-kd-20260519-1556-1.md) | Wrap global loads with __ldg() to explicitly route reads through the read-only d | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1557-1](../sources/experiences/exp-a-kd-20260519-1557-1.md) | Wrap the two global loads with __ldg() to explicitly request read-only cache rou | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1558-1](../sources/experiences/exp-a-kd-20260519-1558-1.md) | Wrap both read-only input loads with __ldg() to explicitly route them through th | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1622-1](../sources/experiences/exp-a-kd-20260519-1622-1.md) | Introduce cp.async.cg.shared.global PTX instructions to initiate asynchronous 16 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1622-2](../sources/experiences/exp-a-kd-20260519-1622-2.md) | Replace scalar bf16 operations with vectorized __nv_bfloat162 intrinsics: proces | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1623-1](../sources/experiences/exp-a-kd-20260519-1623-1.md) | Introduce cp.async.cg.shared.global PTX instructions to initiate asynchronous 16 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1623-2](../sources/experiences/exp-a-kd-20260519-1623-2.md) | Replace scalar bf16 operations with bf16x2 packed intrinsics (__bfloat1622float2 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1624-1](../sources/experiences/exp-a-kd-20260519-1624-1.md) | Replace the single global scale with per-group dynamic scale computed via warp-l | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1625-1](../sources/experiences/exp-a-kd-20260519-1625-1.md) | Replace the precomputed global scale with per-token-group dynamic scale computat | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1626-1](../sources/experiences/exp-a-kd-20260519-1626-1.md) | Replace the scalar per-element loop with bfloat162 vectorized processing: load 2 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1626-2](../sources/experiences/exp-a-kd-20260519-1626-2.md) | Replace scalar scale+clamp+store loop with bfloat162 vectorized intrinsics: __hm | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1627-1](../sources/experiences/exp-a-kd-20260519-1627-1.md) | Vectorize the entire SiLU+mul+quant pipeline from scalar bfloat16 to bfloat162 ( | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1638-1](../sources/experiences/exp-a-kd-20260519-1638-1.md) | Replace raw int4 with a typed PackedVecHalf struct exposing named half2 elts[] m | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1639-1](../sources/experiences/exp-a-kd-20260519-1639-1.md) | Replace raw reinterpret_cast<int4> and __ldg with a typed PackedVec struct provi | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1640-1](../sources/experiences/exp-a-kd-20260519-1640-1.md) | Introduce typed ld128/st128 template wrappers (static_assert-enforced 16-byte si | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1641-1](../sources/experiences/exp-a-kd-20260519-1641-1.md) | Introduce typed ld128/st128 template wrappers around __ldg on int4* and a Packed | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1647-1](../sources/experiences/exp-a-kd-20260519-1647-1.md) | Refactor type-conditional branches into reusable `cast_to_float2`/`cast_to_packe | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1648-1](../sources/experiences/exp-a-kd-20260519-1648-1.md) | Extract type-dispatch conversions into reusable cast_to_float2/cast_to_packed he | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1750-1](../sources/experiences/exp-a-kd-20260519-1750-1.md) | Fuse SiLU+mul and per-block quantization into a single kernel that computes the  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1751-1](../sources/experiences/exp-a-kd-20260519-1751-1.md) | Fuse SiLU+mul and per-block quantization into a single kernel that computes the  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1752-1](../sources/experiences/exp-a-kd-20260519-1752-1.md) | Reuse the already-allocated shared_max[0] reduction buffer to broadcast the comp | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1753-1](../sources/experiences/exp-a-kd-20260519-1753-1.md) | Remove the shared_result array entirely and keep the SiLU*up result in a registe | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2375-1](../sources/experiences/exp-a-kd-20260519-2375-1.md) | Replace the hardcoded silu() call with a non-type template function-pointer para | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2376-1](../sources/experiences/exp-a-kd-20260519-2376-1.md) | Generalize the kernel by replacing the hardcoded silu() call with a compile-time | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2377-1](../sources/experiences/exp-a-kd-20260519-2377-1.md) | Replace tanh-approximation GELU with exact GELU using ::erf, which computes f *  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2378-1](../sources/experiences/exp-a-kd-20260519-2378-1.md) | Replace the tanh-approximation GELU with the exact GELU using ::erf, which requi | analysis | sm90 | cuda-cpp |
| [exp-i-kd-20260518-0057](../sources/experiences/exp-i-kd-20260518-0057.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2440-1](../sources/experiences/exp-i-kd-20260519-2440-1.md) | Cast raw T* pointers to cutlass::Array<T,N>* via reinterpret_cast for vectorized | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2441-1](../sources/experiences/exp-i-kd-20260519-2441-1.md) | Cast raw T* pointers to cutlass::Array<T, N>* via reinterpret_cast for vectorize | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260518-0075](../sources/experiences/exp-o-kd-20260518-0075.md) | awq_large_gated | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0085](../sources/experiences/exp-o-kd-20260518-0085.md) | float_medium | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0111](../sources/experiences/exp-o-kd-20260518-0111.md) | f16_large | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0217](../sources/experiences/exp-o-kd-20260518-0217.md) | Replace erff-based exact GELU with tanh-based Taylor approximation (GELU(x) ≈ 0. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0264](../sources/experiences/exp-o-kd-20260518-0264.md) | mask_50pct | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0310](../sources/experiences/exp-o-kd-20260518-0310.md) | Fuse the activation and scale stages into a single kernel so the activation resu | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0314](../sources/experiences/exp-o-kd-20260518-0314.md) | float_32epg_cand | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0363](../sources/experiences/exp-o-kd-20260518-0363.md) | half_m256_k1024 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0365](../sources/experiences/exp-o-kd-20260518-0365.md) | bfloat16_256K | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0384](../sources/experiences/exp-o-kd-20260518-0384.md) | Replace per-thread scalar half load/store with half2 (32-bit) vectorized access  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0445](../sources/experiences/exp-o-kd-20260518-0445.md) | Vectorize memory access using float4 (128-bit) loads/stores so each thread proce | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0446](../sources/experiences/exp-o-kd-20260518-0446.md) | Vectorize memory access using half2 reinterpret_cast to load and store two half  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0450](../sources/experiences/exp-o-kd-20260518-0450.md) | Replace scalar float load/store with float4 vectorized loads/stores so each thre | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0690](../sources/experiences/exp-o-kd-20260518-0690.md) | Because each memory transaction has fixed overhead, and the GPU cannot fully sat | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0691](../sources/experiences/exp-o-kd-20260518-0691.md) | Ize versus float32, the scalar access pattern still issues narrow memory transac | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0692](../sources/experiences/exp-o-kd-20260518-0692.md) | Nd increases latency. Additionally, the total thread count equals N, which incre | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0693](../sources/experiences/exp-o-kd-20260518-0693.md) | At least 32 bits, wasting half the bus width. Thread count equals N, causing hig | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0735](../sources/experiences/exp-o-kd-20260518-0735.md) | The optimization eliminates wasted computation on masked tokens and removes a se | optimization | sm90 | triton |
| [exp-o-kd-20260518-0802](../sources/experiences/exp-o-kd-20260518-0802.md) | Ecisions. This caused unnecessary shared-memory reads and register pressure for  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0217-1](../sources/experiences/exp-o-kd-20260519-0217-1.md) | Replace erff-based GELU with a Taylor approximation using the single-cycle PTX h | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0275-1](../sources/experiences/exp-o-kd-20260519-0275-1.md) | Replace erf(scalar / sqrt(2)) with erf(scalar * (1/sqrt(2))) by precomputing HAL | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0276-1](../sources/experiences/exp-o-kd-20260519-0276-1.md) | Replace scalar / ROOT_TWO_F with scalar * HALF_ROOT_TWO_F (precomputed 1/sqrt(2) | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0277-1](../sources/experiences/exp-o-kd-20260519-0277-1.md) | Replace scalar / root_two with scalar * half_root_two (where half_root_two = sqr | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0309-1](../sources/experiences/exp-o-kd-20260519-0309-1.md) | Fuse the activation gate and per-expert prequant scale into a single kernel so t | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0309-2](../sources/experiences/exp-o-kd-20260519-0309-2.md) | Replace the 1D strided loop with a 2D grid where blockIdx.x maps to row-groups a | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0310-1](../sources/experiences/exp-o-kd-20260519-0310-1.md) | Fuse gated-activation and per-expert scaling into a single kernel so the activat | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0311-1](../sources/experiences/exp-o-kd-20260519-0311-1.md) | Fuse the gated activation and prequant scale into a single kernel that computes  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0312-1](../sources/experiences/exp-o-kd-20260519-0312-1.md) | Rework doActivationKernel into a 2D row/column launch where blockIdx.x covers to | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0313-1](../sources/experiences/exp-o-kd-20260519-0313-1.md) | Reuse the expert-id lookup already needed for gated parameter selection to also  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0345-1](../sources/experiences/exp-o-kd-20260519-0345-1.md) | Fuse all five elementwise kernels into a single silu_bw_fused_kernel that comput | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0346-1](../sources/experiences/exp-o-kd-20260519-0346-1.md) | Fuse all five kernels into a single silu_bw_fused_kernel that loads x1, x2, dx4  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0357-1](../sources/experiences/exp-o-kd-20260519-0357-1.md) | Use float4 (128-bit) vectorized loads/stores via the FLOAT4 macro so each thread | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0358-1](../sources/experiences/exp-o-kd-20260519-0358-1.md) | Use float4 (128-bit) vectorized loads and stores via the FLOAT4 macro to process | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0359-1](../sources/experiences/exp-o-kd-20260519-0359-1.md) | Replace scalar float load/store with float4 (128-bit) vectorized memory transact | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0360-1](../sources/experiences/exp-o-kd-20260519-0360-1.md) | Replace scalar half loads/stores with half2 (32-bit) vectorized memory transacti | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0361-1](../sources/experiences/exp-o-kd-20260519-0361-1.md) | Replace scalar 32-bit loads/stores with float4 (128-bit) vectorized loads/stores | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0362-1](../sources/experiences/exp-o-kd-20260519-0362-1.md) | Replace scalar half loads/stores with half2 (32-bit) vector loads/stores so each | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0381-1](../sources/experiences/exp-o-kd-20260519-0381-1.md) | Use float4 vectorized load/store (reinterpret_cast<float4*> via FLOAT4 macro) to | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0382-1](../sources/experiences/exp-o-kd-20260519-0382-1.md) | Convert scalar half load/store to half2 vectorized load/store via the HALF2 rein | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0383-1](../sources/experiences/exp-o-kd-20260519-0383-1.md) | Vectorize the kernel to process 4 floats per thread using float4 (128-bit) load/ | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0384-1](../sources/experiences/exp-o-kd-20260519-0384-1.md) | Replace scalar half load/store with half2 (32-bit) vectorized access so each thr | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0385-1](../sources/experiences/exp-o-kd-20260519-0385-1.md) | Vectorize to half2 (4-byte) loads/stores so each thread processes two half eleme | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0386-1](../sources/experiences/exp-o-kd-20260519-0386-1.md) | Increase per-thread workload from 2 to 8 half elements by unrolling into 4 indep | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0387-1](../sources/experiences/exp-o-kd-20260519-0387-1.md) | Vectorize to half2 (4-byte) loads/stores so each thread processes two half eleme | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0388-1](../sources/experiences/exp-o-kd-20260519-0388-1.md) | Expand per-thread workload from 2 to 8 half elements using 4 separate half2 regi | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0445-1](../sources/experiences/exp-o-kd-20260519-0445-1.md) | Vectorize loads and stores using float4 (16-byte) transactions via reinterpret_c | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0446-1](../sources/experiences/exp-o-kd-20260519-0446-1.md) | Vectorize the kernel to use half2 loads and stores via reinterpret_cast, process | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0447-1](../sources/experiences/exp-o-kd-20260519-0447-1.md) | Replace scalar float load/store with vectorized float4 (128-bit) load/store via  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0448-1](../sources/experiences/exp-o-kd-20260519-0448-1.md) | Vectorize scalar half loads/stores into half2 (4-byte) transactions using HALF2  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0449-1](../sources/experiences/exp-o-kd-20260519-0449-1.md) | Vectorize global memory access using float4 so each thread loads/stores 4 contig | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0450-1](../sources/experiences/exp-o-kd-20260519-0450-1.md) | Vectorize the kernel with float4 loads/stores so each thread processes 4 element | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0451-1](../sources/experiences/exp-o-kd-20260519-0451-1.md) | Use half2 vectorized loads and stores via reinterpret_cast<half2*> to process tw | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0452-1](../sources/experiences/exp-o-kd-20260519-0452-1.md) | Vectorize to float4 processing: each thread loads 4 contiguous floats via a sing | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0453-1](../sources/experiences/exp-o-kd-20260519-0453-1.md) | Process 2 half elements per thread using half2 vector type: a single 32-bit load | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0714-1](../sources/experiences/exp-o-kd-20260519-0714-1.md) | Replace scalar stride loads with float4 vectorized loads via reinterpret_cast<fl | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0742-1](../sources/experiences/exp-o-kd-20260519-0742-1.md) | Add expert-based early-return filter after the bounds check: threads whose token | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0743-1](../sources/experiences/exp-o-kd-20260519-0743-1.md) | Add expert_ids and expert_step fields to Params and insert an early-return guard | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0744-1](../sources/experiences/exp-o-kd-20260519-0744-1.md) | Add a compile-time template parameter kFilterExpert to act_and_mul_kernel so tha | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0763-1](../sources/experiences/exp-o-kd-20260519-0763-1.md) | Cache input data in per-warp shared memory during Pass-1, then read from shared  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0764-1](../sources/experiences/exp-o-kd-20260519-0764-1.md) | Fuse the two kernels into a single fused_silu_mul_quant_kernel that performs SiL | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0765-1](../sources/experiences/exp-o-kd-20260519-0765-1.md) | Fuse silu_and_mul into the FP4 quantization kernel by conditionally reading both | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1876-1](../sources/experiences/exp-o-kd-20260519-1876-1.md) | Replace scalar __ldg loads and scalar stores with int4 (128-bit) vectorized load | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1877-1](../sources/experiences/exp-o-kd-20260519-1877-1.md) | Replace scalar __ldg loads with int4 (128-bit) vectorized loads that fetch adjac | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1878-1](../sources/experiences/exp-o-kd-20260519-1878-1.md) | Introduce a 128-bit int4 vectorized fast path that loads VEC_SIZE elements (4 fo | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1879-1](../sources/experiences/exp-o-kd-20260519-1879-1.md) | Vectorize the interleaved data access using int4 (128-bit) loads that fetch VEC_ | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1897-1](../sources/experiences/exp-o-kd-20260519-1897-1.md) | Replace scalar bf16 element-by-element processing with packed __nv_bfloat162 dua | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1898-1](../sources/experiences/exp-o-kd-20260519-1898-1.md) | Replace scalar __half inner loop with packed __half2 SIMD operations: __half22fl | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1899-1](../sources/experiences/exp-o-kd-20260519-1899-1.md) | Reinterpret input pointers as packed_t (e.g., __half2, __nv_bfloat162) instead o | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1944-1](../sources/experiences/exp-o-kd-20260519-1944-1.md) | Fuse SiLU(gate)*up activation and FP4-quantization proxy into a single kernel: l | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1945-1](../sources/experiences/exp-o-kd-20260519-1945-1.md) | Fuse SiLU+Mul and FP4 quantization into a single kernel where compute_silu_mul o | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1946-1](../sources/experiences/exp-o-kd-20260519-1946-1.md) | Added a FUSE_SILU_MUL compile-time template parameter to cvt_fp16_to_fp4; when e | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1947-1](../sources/experiences/exp-o-kd-20260519-1947-1.md) | Fuse SiLU and Mul into a single kernel (kernel_fused_silu_mul_bf16) that reads g | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1948-1](../sources/experiences/exp-o-kd-20260519-1948-1.md) | Fuse SiLU and element-wise multiplication into a single kernel that loads gate a | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1984-1](../sources/experiences/exp-o-kd-20260519-1984-1.md) | Fuse both kernels into a single fused_silu_mul_quant_kernel where the float-valu | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1985-1](../sources/experiences/exp-o-kd-20260519-1985-1.md) | Fuse silu_and_mul and scaled_quant into a single fused_silu_mul_quant_kernel whe | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2145-1](../sources/experiences/exp-o-kd-20260519-2145-1.md) | Replace synchronous global memory reads with cp.async.cg.shared.global PTX instr | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2146-1](../sources/experiences/exp-o-kd-20260519-2146-1.md) | Replace synchronous global memory reads with cp.async.cg.shared.global PTX instr | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2147-1](../sources/experiences/exp-o-kd-20260519-2147-1.md) | Vectorize using __nv_bfloat162 dual-half types to process two bf16 values per in | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2148-1](../sources/experiences/exp-o-kd-20260519-2148-1.md) | Vectorize the entire pipeline to bfloat162 (bf16x2): load gate/up pairs via rein | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2149-1](../sources/experiences/exp-o-kd-20260519-2149-1.md) | Replace synchronous VLLM_LDG global reads with a cp.async.cg.shared.global PTX i | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2150-1](../sources/experiences/exp-o-kd-20260519-2150-1.md) | Replace the scalar loop with bfloat162 dual-half vectorized operations: silu2 ap | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2208-1](../sources/experiences/exp-o-kd-20260519-2208-1.md) | Fuse SiLU+mul and per-block quantization into a single kernel where each thread  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2209-1](../sources/experiences/exp-o-kd-20260519-2209-1.md) | Fuse SiLU+mul and per-block quantization into a single kernel that computes the  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2210-1](../sources/experiences/exp-o-kd-20260519-2210-1.md) | Thread 0 writes the computed scale to shared_max[0] in addition to global memory | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2290-1](../sources/experiences/exp-o-kd-20260519-2290-1.md) | Replace tanh-approximation GELU with exact erf-based GELU: cast to float once, c | optimization | sm90 | cuda-cpp |

## allreduce

| ID | Title | Type | Architectures | Languages |
|----|-------|------|--------------|-----------|
| [exp-o-kd-20260519-0691-1](../sources/experiences/exp-o-kd-20260519-0691-1.md) | Add two new fields to AllReduceParams: tmp_result_buffers[MAX_RANKS_PER_NODE] pr | optimization | sm90 | cuda-cpp |

## attention

| ID | Title | Type | Architectures | Languages |
|----|-------|------|--------------|-----------|
| [exp-a-20260323-152446-0af59b22](../sources/experiences/exp-a-20260323-152446-0af59b22.md) | ## Task
Apply optimization to flash_attention kernel FA_01 in Round 2. Read kernel.cu from /home/qinhaiyan/Research/Kern | analysis | sm90 | cuda-cpp |
| [exp-a-20260324-115144-17bb4520](../sources/experiences/exp-a-20260324-115144-17bb4520.md) | ## Task
Write an optimized pure CUDA flash attention kernel for Qwen2.5-7B with Q4_0 KV cache. Write the complete kernel | analysis | sm90 | cuda-cpp |
| [exp-a-20260324-140805-8ad7dea8](../sources/experiences/exp-a-20260324-140805-8ad7dea8.md) | ## Task
Write an optimized pure CUDA flash attention kernel for task FA_12 and run the test to verify correctness and pe | analysis | sm90 | cuda-cpp |
| [exp-a-20260324-143036-fbe3d628](../sources/experiences/exp-a-20260324-143036-fbe3d628.md) | ## Task
Write an optimized CUDA flash attention kernel for task FA_12 (fp32_flash_attention_qwen2_5_7b_f16_cache8192) an | analysis | sm90 | cuda-cpp |
| [exp-a-20260324-145123-aca9ca55](../sources/experiences/exp-a-20260324-145123-aca9ca55.md) | ## Task
Create optimized CUDA flash attention kernel at /home/qinhaiyan/Research/KernelOwl/experiments/autoresearch_2026 | analysis | sm90 | cuda-cpp |
| [exp-a-20260324-185538-6422a673](../sources/experiences/exp-a-20260324-185538-6422a673.md) | Optimize flash_attention kernel for FA_12 task while maintaining correctness | analysis | sm90 | cuda-cpp |
| [exp-a-20260324-192707-89268cbf](../sources/experiences/exp-a-20260324-192707-89268cbf.md) | ## Task
Optimize the flash_attention kernel for FA_12 task. The current best kernel is at /home/qinhaiyan/Research/Kerne | analysis | sm90 | cuda-cpp |
| [exp-a-20260324-193709-1043172f](../sources/experiences/exp-a-20260324-193709-1043172f.md) | ## Task
Create an optimized flash attention CUDA kernel for FA_12 task. The current best kernel is at /home/qinhaiyan/Re | analysis | sm90 | cuda-cpp |
| [exp-a-20260324-193752-39489fc9](../sources/experiences/exp-a-20260324-193752-39489fc9.md) | Optimize flash_attention kernel for FA_12 task while maintaining correctness | analysis | sm90 | cuda-cpp |
| [exp-a-20260324-201052-39489fc9](../sources/experiences/exp-a-20260324-201052-39489fc9.md) | Optimize flash_attention kernel for FA_12 task while maintaining correctness | analysis | sm90 | cuda-cpp |
| [exp-a-20260325-135700-4b5c6f98](../sources/experiences/exp-a-20260325-135700-4b5c6f98.md) | ## Task
Create FA_11 flash_attention kernel from baseline and run initial test

## Goal
Copy baseline kernel to attempt  | analysis | sm90 | cuda-cpp |
| [exp-a-20260325-141129-6a0518a8](../sources/experiences/exp-a-20260325-141129-6a0518a8.md) | task_002_20260325_134858 | analysis | sm90 | cuda-cpp |
| [exp-a-20260325-164413-39849730](../sources/experiences/exp-a-20260325-164413-39849730.md) | ## Task
Write an optimized v2 kernel.cu file for W4A32C8 Q4_0 quantized GEMM (LLaMA-3-8B attention output, N=4096, K=409 | analysis | sm90 | cuda-cpp |
| [exp-a-20260325-185043-1f06c3f2](../sources/experiences/exp-a-20260325-185043-1f06c3f2.md) | ## Task
Write and test an optimized flash attention kernel for Q4_0 KV cache

## Goal
Create a working kernel.cu in /hom | analysis | sm90 | cuda-cpp |
| [exp-a-20260326-093418-2491cf4d](../sources/experiences/exp-a-20260326-093418-2491cf4d.md) | ## Task
Convert baseline flash_attention kernel to pure CUDA for task FA_15. Remove #include <torch/extension.h>, torch: | analysis | sm90 | cuda-cpp |
| [exp-a-20260326-100018-b14c6b4a](../sources/experiences/exp-a-20260326-100018-b14c6b4a.md) | ## Task
Diagnose and fix CUDA 'invalid argument' errors in the v2 flash attention kernel. The kernel is at /home/qinhaiy | analysis | sm90 | cuda-cpp |
| [exp-a-20260328-164241-940e8e92](../sources/experiences/exp-a-20260328-164241-940e8e92.md) | ## Task
Implement tensor core optimization for flash attention Q@K computation. Use WMMA API (cuda_wmma) to accelerate t | analysis | sm90 | cuda-cpp |
| [exp-a-20260328-165558-4757c191](../sources/experiences/exp-a-20260328-165558-4757c191.md) | ## Task
Add shared memory K/V caching to flash attention kernel. Cache K and V tiles in shared memory to reduce global m | analysis | sm90 | cuda-cpp |
| [exp-a-20260506-180001-cuda-compile-patterns](../sources/experiences/exp-a-20260506-180001-cuda-compile-patterns.md) | CUDA compile error patterns from SOL-ExecBench experiments and their resolution | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0018](../sources/experiences/exp-a-kd-20260518-0018.md) | Remove the offset_q offset term by dispatching with IsQBegin=true (CausalMask<tr | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0023](../sources/experiences/exp-a-kd-20260518-0023.md) | split4_H128_B1 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0024](../sources/experiences/exp-a-kd-20260518-0024.md) | split8_H128_B4 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0027](../sources/experiences/exp-a-kd-20260518-0027.md) | large_kv_uncapped | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0028](../sources/experiences/exp-a-kd-20260518-0028.md) | Cap split_kv at sm_count/2 when split_wave_aware exceeds 1, preventing excessive | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0029](../sources/experiences/exp-a-kd-20260518-0029.md) | Add a cap of sm_count/2 on the computed split_kv value so that the split count n | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0030](../sources/experiences/exp-a-kd-20260518-0030.md) | fused_reduction_no_memset | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0110](../sources/experiences/exp-a-kd-20260518-0110.md) | ldmatrix_vs_pointer_fp16 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0113](../sources/experiences/exp-a-kd-20260518-0113.md) | Distribute exp2f computations across all 4 warps via warp-partitioned indexing ( | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0114](../sources/experiences/exp-a-kd-20260518-0114.md) | large_32row | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0118](../sources/experiences/exp-a-kd-20260518-0118.md) | Reduce pipeline stages from 4 to 1 by communicating kMaxK=128 to MakeCustomMma s | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-0127](../sources/experiences/exp-a-kd-20260518-0127.md) | Fuse the per-element computation by loading attn and di values directly into the | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0130](../sources/experiences/exp-a-kd-20260518-0130.md) | Add a template parameter kMaxK and derive constexpr bool kSingleIteration = kMax | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0132](../sources/experiences/exp-a-kd-20260518-0132.md) | softmax_accum_atomic | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0133](../sources/experiences/exp-a-kd-20260518-0133.md) | warp_exp_allthreads | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0134](../sources/experiences/exp-a-kd-20260518-0134.md) | out_rescale_mprime | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0218](../sources/experiences/exp-a-kd-20260518-0218.md) | seq128_dim64 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0219](../sources/experiences/exp-a-kd-20260518-0219.md) | seq256_dim64 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0266](../sources/experiences/exp-a-kd-20260518-0266.md) | d64_s512 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0326](../sources/experiences/exp-a-kd-20260518-0326.md) | Fuse the two separate compute+update loops into a single loop body and add isfin | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0330](../sources/experiences/exp-a-kd-20260518-0330.md) | Fuse QK scoring, softmax, and value weighting into a single kernel using online  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0331](../sources/experiences/exp-a-kd-20260518-0331.md) | Fuse QK-scoring and softmax-value into a single kernel using online softmax with | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0367](../sources/experiences/exp-a-kd-20260518-0367.md) | tokens_2048 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0409](../sources/experiences/exp-a-kd-20260518-0409.md) | many_heads_no_pragma | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0483](../sources/experiences/exp-a-kd-20260518-0483.md) | float_4M | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0489](../sources/experiences/exp-a-kd-20260518-0489.md) | Introduce double-buffered async copy pipeline (kStage=2): V tile is prefetched t | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0575](../sources/experiences/exp-a-kd-20260518-0575.md) | bf16_m256_topk8 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0607](../sources/experiences/exp-a-kd-20260518-0607.md) | bf16_large | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0608](../sources/experiences/exp-a-kd-20260518-0608.md) | half_large | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0609](../sources/experiences/exp-a-kd-20260518-0609.md) | half_xl | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0630](../sources/experiences/exp-a-kd-20260518-0630.md) | half_1024t_32h | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0705](../sources/experiences/exp-a-kd-20260518-0705.md) | write_cache_h8_hs64_bs16 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0706](../sources/experiences/exp-a-kd-20260518-0706.md) | read_attention_h8_hs64_bs16 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0731](../sources/experiences/exp-a-kd-20260518-0731.md) | uint16_cast_to_float | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0755](../sources/experiences/exp-a-kd-20260518-0755.md) | kauto_bf16 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0895](../sources/experiences/exp-a-kd-20260518-0895.md) | pipeline_hd128 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0897](../sources/experiences/exp-a-kd-20260518-0897.md) | multihead_hd128_512t | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1096](../sources/experiences/exp-a-kd-20260518-1096.md) | half_mla_128heads_64rotdim_512rank | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1097](../sources/experiences/exp-a-kd-20260518-1097.md) | half_mla_64heads_128rotdim_1024rank | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1113](../sources/experiences/exp-a-kd-20260518-1113.md) | attention_workload | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1114](../sources/experiences/exp-a-kd-20260518-1114.md) | attention_workload | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1123](../sources/experiences/exp-a-kd-20260518-1123.md) | noncontiguous_access | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1167](../sources/experiences/exp-a-kd-20260518-1167.md) | mqa_8q_1kv | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1168](../sources/experiences/exp-a-kd-20260518-1168.md) | gqa_8q_2kv | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1169](../sources/experiences/exp-a-kd-20260518-1169.md) | mha_8q_8kv | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1170](../sources/experiences/exp-a-kd-20260518-1170.md) | mqa_8q_1kv | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1171](../sources/experiences/exp-a-kd-20260518-1171.md) | gqa_8q_2kv | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1172](../sources/experiences/exp-a-kd-20260518-1172.md) | mha_8q_8kv | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1195](../sources/experiences/exp-a-kd-20260518-1195.md) | nhd_32h_128d | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1196](../sources/experiences/exp-a-kd-20260518-1196.md) | nhd_8h_128d | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1213](../sources/experiences/exp-a-kd-20260518-1213.md) | fusion_medium_32q | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1282](../sources/experiences/exp-a-kd-20260518-1282.md) | small_stride_8q | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0016-1](../sources/experiences/exp-a-kd-20260519-0016-1.md) | Switch to CausalMask<true> (IsQBegin=true) which omits the offset_q term from th | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0017-1](../sources/experiences/exp-a-kd-20260519-0017-1.md) | Replace CausalMask<false> with CausalMask<true> by removing offset_q from the tr | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0018-1](../sources/experiences/exp-a-kd-20260519-0018-1.md) | Switch to CausalMask<true> (IsQBegin=true) dispatch by removing the offset_q ter | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0019-1](../sources/experiences/exp-a-kd-20260519-0019-1.md) | Move the local_split_kv computation before shared memory declaration and tensor  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0020-1](../sources/experiences/exp-a-kd-20260519-0020-1.md) | Compute local_split_kv before declaring shared memory, then add an early return  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0023-1](../sources/experiences/exp-a-kd-20260519-0023-1.md) | Fuse two kernels into a single fused_lse_reduction kernel using two-phase atomic | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0024-1](../sources/experiences/exp-a-kd-20260519-0024-1.md) | Fuse the two-kernel LSE reduction into a single kernel using atomicMax for globa | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0025-1](../sources/experiences/exp-a-kd-20260519-0025-1.md) | Fuse the two-kernel write-then-reduce sequence into a single kernel that uses at | analysis | sm100 | cuda-cpp |
| [exp-a-kd-20260519-0026-1](../sources/experiences/exp-a-kd-20260519-0026-1.md) | Fused kernel uses per-element atomicAdd on the global output tensor for accumula | analysis | sm100 | cuda-cpp |
| [exp-a-kd-20260519-0026-2](../sources/experiences/exp-a-kd-20260519-0026-2.md) | Software-managed cross-CTA barriers using atomicAdd on global memory counters co | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0027-1](../sources/experiences/exp-a-kd-20260519-0027-1.md) | Cap split_kv at sm_count/2 when split_wave_aware exceeds 1 and fused reduction i | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0028-1](../sources/experiences/exp-a-kd-20260519-0028-1.md) | Cap split_kv at sm_count/2 when split_wave_aware > 1, using min(split_wave_aware | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0029-1](../sources/experiences/exp-a-kd-20260519-0029-1.md) | Cap split_wave_aware at sm_count/2 to prevent over-splitting when K is large; in | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0030-1](../sources/experiences/exp-a-kd-20260519-0030-1.md) | Add cudaMemsetAsync to zero the output buffer before launching split accumulatio | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0113-1](../sources/experiences/exp-a-kd-20260519-0113-1.md) | Distribute exp2f across all 4 warps by mapping rows via id = warp_id * kLinesPer | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0113-2](../sources/experiences/exp-a-kd-20260519-0113-2.md) | Add a conditional changed = (m_prime_id < mi_id) guard that skips the exp2f comp | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0114-1](../sources/experiences/exp-a-kd-20260519-0114-1.md) | Distribute the 32 exp2f calls across 8 warps by mapping each warp's lanes 0–3 to | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0117-1](../sources/experiences/exp-a-kd-20260519-0117-1.md) | Split the key dimension across multiple CUDA blocks via blockIdx.x (num_splits_k | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0118-1](../sources/experiences/exp-a-kd-20260519-0118-1.md) | Reduce pipeline stages from 4 to 1 by computing kStages = min(max_stages, ceil(k | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0119-1](../sources/experiences/exp-a-kd-20260519-0119-1.md) | Reduce pipeline stages to min(4, ceil(kMaxK/kBlockK))=1 when kMaxK equals kBlock | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0120-1](../sources/experiences/exp-a-kd-20260519-0120-1.md) | Pass kMaxK=128 to MakeCustomMma for medium heads so that kStages is computed as  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0121-1](../sources/experiences/exp-a-kd-20260519-0121-1.md) | Reduce kStages from 4 to 1 for small head dimensions (k<=64) by passing kMaxK=64 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0127-1](../sources/experiences/exp-a-kd-20260519-0127-1.md) | Fuse the per-element computation into a single loop: load current_di once (broad | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0128-1](../sources/experiences/exp-a-kd-20260519-0128-1.md) | Fuse the attention and di fragment loads into the computation loop: replace frag | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0129-1](../sources/experiences/exp-a-kd-20260519-0129-1.md) | Capture the shared-memory dropout mask once before the hot loop into a single ui | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0130-1](../sources/experiences/exp-a-kd-20260519-0130-1.md) | Introduce a constexpr bool kSingleIteration = kMaxK <= TileN template parameter  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0131-1](../sources/experiences/exp-a-kd-20260519-0131-1.md) | Fix the sign error in the causal boundary formula from key_start - num_keys - nu | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0134-1](../sources/experiences/exp-a-kd-20260519-0134-1.md) | Introduce a dedicated out_rescale shared-memory array to hold the rescale factor | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0136-1](../sources/experiences/exp-a-kd-20260519-0136-1.md) | Use SmemLayoutA (Crosswise) layout for TensorRefA instead of Operator::LayoutA ( | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0319-1](../sources/experiences/exp-a-kd-20260519-0319-1.md) | Reduce kBlockSizeI from 128 to 64, cutting the thread count from 256 to 128 so t | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0326-1](../sources/experiences/exp-a-kd-20260519-0326-1.md) | Fuse the two separate compute and update passes into a single q-loop that comput | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0327-1](../sources/experiences/exp-a-kd-20260519-0327-1.md) | Fuse both kernels into one, reformulate tmp_sum using the chain-rule identity su | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0330-1](../sources/experiences/exp-a-kd-20260519-0330-1.md) | Fuse QK scoring, softmax, and value weighting into a single kernel using online  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0331-1](../sources/experiences/exp-a-kd-20260519-0331-1.md) | Fuse the two separate QK-score and softmax-value kernels into a single kernel us | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0483-1](../sources/experiences/exp-a-kd-20260519-0483-1.md) | Increase kStage from 1 to 2 to enable multi-stage async pipeline with double-buf | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0484-1](../sources/experiences/exp-a-kd-20260519-0484-1.md) | Enable double-buffered multi-stage pipeline (kStage=2) so cp.async.cg prefetches | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0485-1](../sources/experiences/exp-a-kd-20260519-0485-1.md) | Upgrade to multi-stage (kStage=2) async pipeline with double-buffered K shared m | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0486-1](../sources/experiences/exp-a-kd-20260519-0486-1.md) | Increase kStage from 1 to 2, enabling the async multi-stage pipeline to double-b | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0487-1](../sources/experiences/exp-a-kd-20260519-0487-1.md) | Replace sequential K/V loading with kStage=2 software pipeline: double-buffer K  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0488-1](../sources/experiences/exp-a-kd-20260519-0488-1.md) | Double-stage (kStage=2) double-buffering overlaps async gmem→smem copies with HM | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0489-1](../sources/experiences/exp-a-kd-20260519-0489-1.md) | Introduce double-buffered smem partitions (kStage=2) with cp.async software pipe | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0490-1](../sources/experiences/exp-a-kd-20260519-0490-1.md) | Store the output accumulator R_D as FP32 (4 registers per element instead of 2), | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0491-1](../sources/experiences/exp-a-kd-20260519-0491-1.md) | Switch R_D accumulator storage from FP16 (kOStorageAccFloat32=0) to FP32 (kOStor | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0492-1](../sources/experiences/exp-a-kd-20260519-0492-1.md) | Upgrade to kStage=2 double-buffered software pipelining: allocate separate smem  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0493-1](../sources/experiences/exp-a-kd-20260519-0493-1.md) | Upgrade to kStage=2 double-buffered async prefetch: K occupies smem slot 0 and V | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0494-1](../sources/experiences/exp-a-kd-20260519-0494-1.md) | Upgrade from kStage=1 to kStage=2 double-buffered software pipelining: add a pro | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0495-1](../sources/experiences/exp-a-kd-20260519-0495-1.md) | Upgrade from kStage=1 single-buffer to kStage=2 double-buffer pipeline: add a pr | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0496-1](../sources/experiences/exp-a-kd-20260519-0496-1.md) | Upgrade to kStage=2 multi-stage async prefetch by issuing V gmem-to-smem before  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0497-1](../sources/experiences/exp-a-kd-20260519-0497-1.md) | Promote the R_D accumulator register array from FP16 (2 uint32 per element) to F | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0498-1](../sources/experiences/exp-a-kd-20260519-0498-1.md) | Switch to kStage=2 double-buffered async prefetch using CP_ASYNC_CG into alterna | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0499-1](../sources/experiences/exp-a-kd-20260519-0499-1.md) | Switch from kStage=1 (synchronous) to kStage=2 (two-stage pipelined) loading usi | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0500-1](../sources/experiences/exp-a-kd-20260519-0500-1.md) | Switch to two-stage software pipelining (kStage=2) which activates the if conste | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0501-1](../sources/experiences/exp-a-kd-20260519-0501-1.md) | Set kOStorageAccFloat32=1 to store the output accumulator R_D as 4 float registe | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0502-1](../sources/experiences/exp-a-kd-20260519-0502-1.md) | Switch R_D accumulator storage from FP16 (2 uint32_t per element) to FP32 (4 uin | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0503-1](../sources/experiences/exp-a-kd-20260519-0503-1.md) | Switch to kStage=2 double-stage async copy pipelining where next Q/K/V tiles are | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0504-1](../sources/experiences/exp-a-kd-20260519-0504-1.md) | Switch O accumulator storage from FP16 to FP32 (kOStorageAccFloat32=1) by storin | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0505-1](../sources/experiences/exp-a-kd-20260519-0505-1.md) | Switch the template parameter kOStorageAccFloat32_ from 0 to 1, keeping accumula | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0506-1](../sources/experiences/exp-a-kd-20260519-0506-1.md) | Switch the output accumulator storage to FP32 (kOStorageAccFloat32=1) so that th | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0775-1](../sources/experiences/exp-a-kd-20260519-0775-1.md) | Reorganize memory access from per-element scalar bf16 to warp-cooperative vector | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0775-2](../sources/experiences/exp-a-kd-20260519-0775-2.md) | Load k_rope once per warp into a register buffer (k_rope_buf) and reuse it acros | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0778-1](../sources/experiences/exp-a-kd-20260519-0778-1.md) | Introduce a register buffer (k_rope_buf) loaded once before the unrolled loop, t | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0844-1](../sources/experiences/exp-a-kd-20260519-0844-1.md) | Replace scalar bfloat16 load/store with 128-bit uint4 packed operations, so each | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0845-1](../sources/experiences/exp-a-kd-20260519-0845-1.md) | Replace per-element scalar float loads/stores with uint4 (128-bit) packed transa | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0846-1](../sources/experiences/exp-a-kd-20260519-0846-1.md) | Replace scalar half-element load/store with uint4 (128-bit) packed memory transa | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0847-1](../sources/experiences/exp-a-kd-20260519-0847-1.md) | Reorganize LSE storage from transposed [num_heads, num_tokens] to row-major [num | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0848-1](../sources/experiences/exp-a-kd-20260519-0848-1.md) | Reorganize LSE storage from transposed [num_heads, num_tokens] to row-major [num | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1040-1](../sources/experiences/exp-a-kd-20260519-1040-1.md) | Transpose the LSE array layout from head-major [num_heads][num_tokens] to token- | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1041-1](../sources/experiences/exp-a-kd-20260519-1041-1.md) | Change LSE layout from head-major (head_idx * num_tokens + token_idx) to token-m | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1042-1](../sources/experiences/exp-a-kd-20260519-1042-1.md) | Override global NNZ_V/NNZ_S with per-head actual topk counts read from device ar | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1142-1](../sources/experiences/exp-a-kd-20260519-1142-1.md) | The layout transpose swaps block_size and head_size in the inner two dimensions, | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1143-1](../sources/experiences/exp-a-kd-20260519-1143-1.md) | Transpose the inner two dimensions to [num_blocks, num_heads, head_size, block_s | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1155-1](../sources/experiences/exp-a-kd-20260519-1155-1.md) | Quantize fp16 KV cache entries to fp8 e4m3 via __nv_cvt_float_to_fp8 with per-ke | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1168-1](../sources/experiences/exp-a-kd-20260519-1168-1.md) | Add a cast_to_float(uint16_t) overload that wraps a half_to_float(uint16_t) help | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1251-1](../sources/experiences/exp-a-kd-20260519-1251-1.md) | Fuse reduce_kernel_float and quantize_kernel_fp8 into a single reduce_kernel_fus | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1287-1](../sources/experiences/exp-a-kd-20260519-1287-1.md) | Fuse FP8 quantization into the merge kernel via a compile-time USE_FP8_OUTPUT te | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1288-1](../sources/experiences/exp-a-kd-20260519-1288-1.md) | Fuse FP8 quantization into the merge kernel by adding a compile-time USE_FP8_OUT | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1289-1](../sources/experiences/exp-a-kd-20260519-1289-1.md) | Pre-compute the reciprocal scale_inv = 1.0f / scale once at kernel entry, then r | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1290-1](../sources/experiences/exp-a-kd-20260519-1290-1.md) | Pre-compute the reciprocal of the scale once at kernel entry (1.0f / *output_sca | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1314-1](../sources/experiences/exp-a-kd-20260519-1314-1.md) | Split-KV factor of 2 distributes 256 KV tokens across two partial attention kern | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1315-1](../sources/experiences/exp-a-kd-20260519-1315-1.md) | Simplified to a single-pass kernel that iterates over the full KV sequence in on | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1316-1](../sources/experiences/exp-a-kd-20260519-1316-1.md) | Replace split-KV with a single-pass kernel that processes the entire KV sequence | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1317-1](../sources/experiences/exp-a-kd-20260519-1317-1.md) | Redesign the cache layout from packed interleaved [num_blocks, num_heads, head_s | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1318-1](../sources/experiences/exp-a-kd-20260519-1318-1.md) | Replace the packed interleaved cache layout [num_blocks, num_heads, head_size/x, | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1318-2](../sources/experiences/exp-a-kd-20260519-1318-2.md) | Replace fixed per-h_block thread assignment with a grid-stride loop where each t | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1329-1](../sources/experiences/exp-a-kd-20260519-1329-1.md) | Replace scalar per-thread bf16 loads and uint8 stores with int4 (128-bit) vector | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1329-2](../sources/experiences/exp-a-kd-20260519-1329-2.md) | Eliminate shared memory entirely by using half-warp shfl_xor reductions with wid | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1329-3](../sources/experiences/exp-a-kd-20260519-1329-3.md) | Replace scalar bf16 load/store with int32 vectorized load/store so each thread h | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1377-1](../sources/experiences/exp-a-kd-20260519-1377-1.md) | Add an early-exit branch for suffix-only tokens (token_idx >= prefix_num_tokens) | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1378-1](../sources/experiences/exp-a-kd-20260519-1378-1.md) | Add an early-exit fast path that checks token_idx >= prefix_num_tokens and copie | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1511-1](../sources/experiences/exp-a-kd-20260519-1511-1.md) | Cooperative shared memory loading replaces per-thread register arrays with __sha | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1512-1](../sources/experiences/exp-a-kd-20260519-1512-1.md) | Replace per-thread register query storage with cooperative shared-memory loading | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1550-1](../sources/experiences/exp-a-kd-20260519-1550-1.md) | Replace the scalar loop with 2 __halves2half2 packed calls followed by __low2hal | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1560-1](../sources/experiences/exp-a-kd-20260519-1560-1.md) | Replace the hardcoded contiguous offset (seq_idx * num_heads * HEAD_SIZE) with a | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1573-1](../sources/experiences/exp-a-kd-20260519-1573-1.md) | Store key cache in FP8-E5M2 format and dequantize to bf16 on load via __nv_cvt_f | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1574-1](../sources/experiences/exp-a-kd-20260519-1574-1.md) | Store key cache in FP8-E5M2 format (1 byte/element) and use __nv_cvt_fp8x2_to_ha | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1575-1](../sources/experiences/exp-a-kd-20260519-1575-1.md) | Compress K-cache storage from FP16 to FP8-E5M2 (1 byte/element), halving memory  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1576-1](../sources/experiences/exp-a-kd-20260519-1576-1.md) | Store K-cache in FP8-E5M2 format (1 byte/element) instead of fp16, halving K-cac | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1577-1](../sources/experiences/exp-a-kd-20260519-1577-1.md) | Store V-cache as FP8-E5M2 (1 byte/element) and dequantize to fp16 via software b | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1578-1](../sources/experiences/exp-a-kd-20260519-1578-1.md) | Replace fp16 V-cache storage with FP8-E5M2 (1 byte/element) to halve memory traf | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1604-1](../sources/experiences/exp-a-kd-20260519-1604-1.md) | Switch to MQA layout with NKV=1, making block_stride=NKV*HS*BS (1024 half-elemen | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1605-1](../sources/experiences/exp-a-kd-20260519-1605-1.md) | Replace MHA layout (NKV=8, identity mapping) with GQA layout (NKV=2, head_mappin | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1606-1](../sources/experiences/exp-a-kd-20260519-1606-1.md) | Replace hardcoded NH-based stride computation with NKV-based strides (block_stri | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1607-1](../sources/experiences/exp-a-kd-20260519-1607-1.md) | Switch to MQA layout by reducing NKV from 8 to 1 and setting head_mapping to all | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1608-1](../sources/experiences/exp-a-kd-20260519-1608-1.md) | Switch to GQA with NKV=2 KV heads by changing block_stride to NKV*HS*BS and usin | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1609-1](../sources/experiences/exp-a-kd-20260519-1609-1.md) | Replace NH with NKV in block_stride computation, v_cache allocation size, and ho | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1649-1](../sources/experiences/exp-a-kd-20260519-1649-1.md) | Fuse both kernels into a single advance_step_flashinfer_kernel where each thread | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1650-1](../sources/experiences/exp-a-kd-20260519-1650-1.md) | Fuse both kernels into a single advance_step_flashinfer_kernel that reads seq_le | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1718-1](../sources/experiences/exp-a-kd-20260519-1718-1.md) | Replace one-element-per-thread mapping with a grid-stride loop that iterates ove | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1719-1](../sources/experiences/exp-a-kd-20260519-1719-1.md) | Replace the one-element-per-thread idx/stride decomposition with a grid-stride l | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1739-1](../sources/experiences/exp-a-kd-20260519-1739-1.md) | Increase BLOCK_SIZE from 16 to 32, setting THREAD_GROUP_SIZE=1 so each thread in | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1740-1](../sources/experiences/exp-a-kd-20260519-1740-1.md) | Increase BLOCK_SIZE from 16 to 32 so THREAD_GROUP_SIZE becomes 1, allowing each  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1741-1](../sources/experiences/exp-a-kd-20260519-1741-1.md) | Increasing BLOCK_SIZE from 16 to 32 sets THREAD_GROUP_SIZE=1, eliminating the in | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1741-2](../sources/experiences/exp-a-kd-20260519-1741-2.md) | BLOCK_SIZE=32 raises NUM_V_VECS_PER_ROW from 2 to 4, spreading each warp's 32 th | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1742-1](../sources/experiences/exp-a-kd-20260519-1742-1.md) | Double BLOCK_SIZE from 16 to 32 so THREAD_GROUP_SIZE becomes 1, eliminating intr | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1743-1](../sources/experiences/exp-a-kd-20260519-1743-1.md) | Increase BLOCK_SIZE to 32 (matching WARP_SIZE) so THREAD_GROUP_SIZE=1, enabling  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1766-1](../sources/experiences/exp-a-kd-20260519-1766-1.md) | Replace the hard-coded stride expression with a runtime q_stride parameter, allo | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2312-1](../sources/experiences/exp-a-kd-20260519-2312-1.md) | Replace scalar half load/store with 128-bit uint4 packed loads (8 half elements  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2313-1](../sources/experiences/exp-a-kd-20260519-2313-1.md) | Replace scalar per-element load/store with 128-bit uint4 (8 half) packed load/st | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2314-1](../sources/experiences/exp-a-kd-20260519-2314-1.md) | Replace scalar half load/store with 128-bit uint4 packed load/store and restruct | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2317-1](../sources/experiences/exp-a-kd-20260519-2317-1.md) | Replace scalar-by-value k_scale/v_scale parameters with const float* pointers, d | analysis | sm90 | cuda-cpp |
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
| [exp-i-kd-20260519-2399-1](../sources/experiences/exp-i-kd-20260519-2399-1.md) | Implement warp-specialized kernel architecture with 6 warp roles (DMA_Q, DMA_KV, | implementation | sm100 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2399-2](../sources/experiences/exp-i-kd-20260519-2399-2.md) | Compute tile-aligned skip boundary by floor-dividing the skip offset to CTA_kvL  | implementation | sm100 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2399-3](../sources/experiences/exp-i-kd-20260519-2399-3.md) | Issue cp.async for seq_len loading immediately on thread 0 before barrier initia | implementation | sm100 | cuda-cpp, cute-dsl |
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
| [exp-o-kd-20260518-0047](../sources/experiences/exp-o-kd-20260518-0047.md) | small_head_64 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0052](../sources/experiences/exp-o-kd-20260518-0052.md) | causal_formula | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0103](../sources/experiences/exp-o-kd-20260518-0103.md) | flash_attn_d64_N1024 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0208](../sources/experiences/exp-o-kd-20260518-0208.md) | Remove the offset_q = N_K - N_Q term from causal_trip_count by switching from Ca | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0210](../sources/experiences/exp-o-kd-20260518-0210.md) | Add a causal_q_begin boolean flag (default true) to enable runtime dispatch to C | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260518-0268](../sources/experiences/exp-o-kd-20260518-0268.md) | Fix the sign in the causal-from-bottom-right diagonal formula: change key_start  | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260518-0271](../sources/experiences/exp-o-kd-20260518-0271.md) | Introduce InstructionShape_ as a template parameter replacing the hardcoded Matr | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260518-0338](../sources/experiences/exp-o-kd-20260518-0338.md) | unfused_vs_fused_mla_cache_write | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0341](../sources/experiences/exp-o-kd-20260518-0341.md) | Added a runtime maxK dispatch macro that buckets max(query_dim, value_dim) into  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0367](../sources/experiences/exp-o-kd-20260518-0367.md) | Upgrade from kStage=1 to kStage=2 to enable a multi-stage async pipeline: issue  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0368](../sources/experiences/exp-o-kd-20260518-0368.md) | Upgrade from single-stage synchronous K/V loading (kStage=1) to two-stage async  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0370](../sources/experiences/exp-o-kd-20260518-0370.md) | Switch accumulator storage from FP16 (2 regs/element) to FP32 (4 regs/element) b | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0371](../sources/experiences/exp-o-kd-20260518-0371.md) | Switch output accumulator R_D to FP32 storage (kOStorageAccFloat32=1) so online  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0518](../sources/experiences/exp-o-kd-20260518-0518.md) | fusion_large_128q | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0520](../sources/experiences/exp-o-kd-20260518-0520.md) | fusion_small_8q | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0597](../sources/experiences/exp-o-kd-20260518-0597.md) | scalar_scale_128heads | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0624](../sources/experiences/exp-o-kd-20260518-0624.md) | N training prefill case). | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0625](../sources/experiences/exp-o-kd-20260518-0625.md) | Rip count and masked trip count, potentially visiting more K-tiles than necessar | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0628](../sources/experiences/exp-o-kd-20260518-0628.md) | Separate reduction kernel, producing incorrect output. It also wasted GPU time o | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0635](../sources/experiences/exp-o-kd-20260518-0635.md) | Case (64 < head_size_v <= 128), the boolean was true but the actual kMaxK=128 wa | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0638](../sources/experiences/exp-o-kd-20260518-0638.md) | Een num_keys and num_queries, the subtraction produces an unnecessarily small (o | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0657](../sources/experiences/exp-o-kd-20260518-0657.md) | H` that makes `kBlockSizeI = 128`, which yields `kNumWarpsPerBlock = 8` even for | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0658](../sources/experiences/exp-o-kd-20260518-0658.md) | The fix switches the alignment predicate to stride(2), the per-head stride in th | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260518-0659](../sources/experiences/exp-o-kd-20260518-0659.md) | Ond. That forced extra global traffic, an extra launch, and synchronization thro | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260518-0661](../sources/experiences/exp-o-kd-20260518-0661.md) | O launch enough resident blocks or become unavailable when the kernel's shared-m | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0668](../sources/experiences/exp-o-kd-20260518-0668.md) | Errors can exceed 1e-3, degrading output quality. Additionally, the conversion o | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0703](../sources/experiences/exp-o-kd-20260518-0703.md) | 584 bytes (576-byte value + 8-byte scale). The generic stride computation produc | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0705](../sources/experiences/exp-o-kd-20260518-0705.md) | Irs via a flat global_idx that increments token_idx first, the LSE access patter | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0718](../sources/experiences/exp-o-kd-20260518-0718.md) | Tions per vector instead of a single coalesced 128-bit write. The smaller vec_si | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0731](../sources/experiences/exp-o-kd-20260518-0731.md) | Te write-back also re-reads K values from global memory that were already comput | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0736](../sources/experiences/exp-o-kd-20260518-0736.md) | In fp16/bf16 causes precision loss when summing across multiple topk experts bec | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0738](../sources/experiences/exp-o-kd-20260518-0738.md) | per_layer_kv | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0741](../sources/experiences/exp-o-kd-20260518-0741.md) | Der load instructions (16-byte vector loads) that fetch multiple elements in one | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0750](../sources/experiences/exp-o-kd-20260518-0750.md) | Ortunity for the compiler to batch memory accesses or unroll the accumulation ac | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0779](../sources/experiences/exp-o-kd-20260518-0779.md) | He intermediate results, adding latency and wasting memory bandwidth. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0785](../sources/experiences/exp-o-kd-20260518-0785.md) | Contiguous()` first, triggering an extra device-side memory copy of the entire i | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0786](../sources/experiences/exp-o-kd-20260518-0786.md) | Erpret-cast pointer to compute wrong offsets when reading or writing input vecto | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0787](../sources/experiences/exp-o-kd-20260518-0787.md) | Layernorm), the kernel cannot operate directly. A separate copy must first extra | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0822](../sources/experiences/exp-o-kd-20260518-0822.md) | Non-contiguous tensor or force an expensive host-side torch.contiguous() copy th | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0824](../sources/experiences/exp-o-kd-20260518-0824.md) | Applied change: The kernel now conditionally reads K-cache as FP8-E5M2 packed ve | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0825](../sources/experiences/exp-o-kd-20260518-0825.md) | Eck, and storing in full precision doubles the memory and bandwidth cost compare | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0832](../sources/experiences/exp-o-kd-20260518-0832.md) | GPU would incur an additional kernel launch overhead (~5-10 microseconds per lau | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0845](../sources/experiences/exp-o-kd-20260518-0845.md) | In a single kernel launch and has the same template-based BLOCK_SIZE dependency. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0852](../sources/experiences/exp-o-kd-20260518-0852.md) | Mory traffic and kernel launch overhead for KV-cache attention operations. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0862](../sources/experiences/exp-o-kd-20260518-0862.md) | Ntization scales vary across heads or layers. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0863](../sources/experiences/exp-o-kd-20260518-0863.md) | The optimization is in numerical accuracy of FP8 KV cache entries. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0864](../sources/experiences/exp-o-kd-20260518-0864.md) | E static scalar float approach for k_scale and v_scale, identical to the reshape | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0206-1](../sources/experiences/exp-o-kd-20260519-0206-1.md) | Switch to CausalMask<true> (IsQBegin=true) which computes max_blocks_q = ceil_di | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0207-1](../sources/experiences/exp-o-kd-20260519-0207-1.md) | Remove offset_q from the trip count formula to use CausalMask<true> semantics, c | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0208-1](../sources/experiences/exp-o-kd-20260519-0208-1.md) | Remove the offset_q term to implement CausalMask<true> (IsQBegin=true) dispatch: | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0209-1](../sources/experiences/exp-o-kd-20260519-0209-1.md) | Switch from CausalMask<false> to CausalMask<true> (IsQBegin=true) by removing th | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0210-1](../sources/experiences/exp-o-kd-20260519-0210-1.md) | Add a causal_q_begin boolean flag (default true) to the Options struct so that t | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0211-1](../sources/experiences/exp-o-kd-20260519-0211-1.md) | Dispatch between CausalMask<true> (IsQBegin=true) and CausalMask<false> (IsQBegi | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0213-1](../sources/experiences/exp-o-kd-20260519-0213-1.md) | Reorder the kernel prologue to compute local_split_kv from per-batch dim_k/split | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0214-1](../sources/experiences/exp-o-kd-20260519-0214-1.md) | Move per-sequence dim_k and local_split_kv computation before shared memory allo | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0216-1](../sources/experiences/exp-o-kd-20260519-0216-1.md) | Add !params.fmha_params.is_fused_reduction to the guard condition so the separat | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0256-1](../sources/experiences/exp-o-kd-20260519-0256-1.md) | Replace atomicAdd with warp-partitioned addition_storage where each warp writes  | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0257-1](../sources/experiences/exp-o-kd-20260519-0257-1.md) | Compute kStages = min(4, ceil(kMaxK/kKeysPerBlock)) = min(4, ceil(128/128)) = 1, | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0258-1](../sources/experiences/exp-o-kd-20260519-0258-1.md) | Reduce pipeline stages from 4 to 1 by computing kStages=min(default_stages, ceil | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0259-1](../sources/experiences/exp-o-kd-20260519-0259-1.md) | Reduce kStages from 4 to 1 (since ceil(128/128)=1 stage suffices when head_size_ | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0260-1](../sources/experiences/exp-o-kd-20260519-0260-1.md) | Reduce kStages from 4 to 1 for small head dimensions (K<=64) by passing the actu | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0261-1](../sources/experiences/exp-o-kd-20260519-0261-1.md) | Replace bool kSingleValueIteration with int kMaxK in run_grouped() and run_atten | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0262-1](../sources/experiences/exp-o-kd-20260519-0262-1.md) | Replace boolean kSingleValueIteration flags with concrete kMaxK upper bounds (12 | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0263-1](../sources/experiences/exp-o-kd-20260519-0263-1.md) | Read the shared-memory dropout mask once before the iteration loop and compress  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0264-1](../sources/experiences/exp-o-kd-20260519-0264-1.md) | Add a kMaxK template parameter and compute constexpr bool kSingleIteration = kMa | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0265-1](../sources/experiences/exp-o-kd-20260519-0265-1.md) | Fix the sign error by changing the formula from key_start - num_keys - num_queri | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0266-1](../sources/experiences/exp-o-kd-20260519-0266-1.md) | Capture the dropout mask into a compact 1-bit register array (cutlass::Array<cut | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0267-1](../sources/experiences/exp-o-kd-20260519-0267-1.md) | Introduce constexpr bool kSingleIterationGradV = kMaxK <= MatmulGradV::Threadblo | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0268-1](../sources/experiences/exp-o-kd-20260519-0268-1.md) | Change the sign from minus to plus in the formula (key_start - num_keys + num_qu | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0271-1](../sources/experiences/exp-o-kd-20260519-0271-1.md) | Introduce InstructionShape_ as a template parameter and delegate the alias to it | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0337-1](../sources/experiences/exp-o-kd-20260519-0337-1.md) | Replace at::zeros with at::empty to skip the eager zero-fill, relying on the ker | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0337-2](../sources/experiences/exp-o-kd-20260519-0337-2.md) | Conditionally allocate a dedicated fp32 accumulation buffer (output_accum) when  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0339-1](../sources/experiences/exp-o-kd-20260519-0339-1.md) | Add a num_splits_key argument and compute an adaptive split count from the numbe | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0341-1](../sources/experiences/exp-o-kd-20260519-0341-1.md) | Add a DISPATCH_MAXK macro that computes max(query_dim, value_dim) at runtime, bu | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0343-1](../sources/experiences/exp-o-kd-20260519-0343-1.md) | Switch the alignment predicate from stride(-1) to stride(2), the per-head stride | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0349-1](../sources/experiences/exp-o-kd-20260519-0349-1.md) | Fuse the entire backward pass into a single CUTLASS-based kernel that tiles over | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0350-1](../sources/experiences/exp-o-kd-20260519-0350-1.md) | Replace the two-pass atomic-accumulate-and-reload pattern with a fused computeDi | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0351-1](../sources/experiences/exp-o-kd-20260519-0351-1.md) | Fuse Q·K scoring, softmax, and value aggregation into a single kernel using the  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0352-1](../sources/experiences/exp-o-kd-20260519-0352-1.md) | Fuse the two-pass attention into a single kernel using the online softmax algori | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0354-1](../sources/experiences/exp-o-kd-20260519-0354-1.md) | Add a second entry point that instantiates AttentionBackwardKernel with a 64x64  | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0367-1](../sources/experiences/exp-o-kd-20260519-0367-1.md) | Upgrade to kStage=2 multi-stage async pipeline: issue current V tile and next K  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0368-1](../sources/experiences/exp-o-kd-20260519-0368-1.md) | Upgrade to kStage=2 multi-stage pipeline with double-buffered K tiles using asyn | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0369-1](../sources/experiences/exp-o-kd-20260519-0369-1.md) | Switch the output accumulator R_D from FP16 storage (2 uint32_t registers per el | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0370-1](../sources/experiences/exp-o-kd-20260519-0370-1.md) | Promote the output accumulator R_D from FP16 storage (2 regs) to FP32 storage (4 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0371-1](../sources/experiences/exp-o-kd-20260519-0371-1.md) | Store output accumulators in FP32 (kOStorageAccFloat32=1) so the online rescalin | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0372-1](../sources/experiences/exp-o-kd-20260519-0372-1.md) | Upgrade to kStage=2 double-buffered async prefetch: assign K to smem slot 0 and  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0373-1](../sources/experiences/exp-o-kd-20260519-0373-1.md) | Introduce kStage=2 double-buffering: a prologue pre-loads the first Q/K tile bef | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0373-2](../sources/experiences/exp-o-kd-20260519-0373-2.md) | Prefetch V tiles before P@V begins using a prologue loop, then issue async copie | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0374-1](../sources/experiences/exp-o-kd-20260519-0374-1.md) | Promote the R_D accumulator from FP16 (2 uint32 registers per element) to FP32 ( | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0375-1](../sources/experiences/exp-o-kd-20260519-0375-1.md) | Enable FP32 output accumulator storage (kOStorageAccFloat32=1) for head_dim<256  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0376-1](../sources/experiences/exp-o-kd-20260519-0376-1.md) | Change kStage from 1 to 2 to activate double-buffered software pipelining: the a | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0377-1](../sources/experiences/exp-o-kd-20260519-0377-1.md) | Change kOStorageAccFloat32 from 0 to 1 so the accumulator register R_D is stored | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0378-1](../sources/experiences/exp-o-kd-20260519-0378-1.md) | Switch to double-stage async copy pipeline (kStage=2): preload first Q/K/V tiles | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0379-1](../sources/experiences/exp-o-kd-20260519-0379-1.md) | Switch O accumulator storage to FP32 registers (4 uint32_t per element via float | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0380-1](../sources/experiences/exp-o-kd-20260519-0380-1.md) | Store the output accumulator R_D in native FP32 (4 uint32_t registers per elemen | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0639-1](../sources/experiences/exp-o-kd-20260519-0639-1.md) | Replace scalar per-element bfloat16 memory access with 128-bit uint4 packed load | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0640-1](../sources/experiences/exp-o-kd-20260519-0640-1.md) | Replace per-element scalar float loads/stores with uint4 (128-bit) packed loads/ | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0641-1](../sources/experiences/exp-o-kd-20260519-0641-1.md) | Replace scalar half-element load/store with uint4 (128-bit) packed access so eac | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0642-1](../sources/experiences/exp-o-kd-20260519-0642-1.md) | Change LSE memory layout from transposed [num_heads, num_tokens] to row-major [n | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0643-1](../sources/experiences/exp-o-kd-20260519-0643-1.md) | Change LSE storage from transposed [num_heads, num_tokens] to row-major [num_tok | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0644-1](../sources/experiences/exp-o-kd-20260519-0644-1.md) | Switch LSE layout to row-major [num_tokens, num_heads] with access token_idx * n | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0754-1](../sources/experiences/exp-o-kd-20260519-0754-1.md) | Add a bool kIsMLA template parameter and wrap all V-cache load/store operations  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1081-1](../sources/experiences/exp-o-kd-20260519-1081-1.md) | Override the global NNZ_V/NNZ_S loop bounds with per-head actual topk counts rea | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1102-1](../sources/experiences/exp-o-kd-20260519-1102-1.md) | Replace bool-per-element mask with bit-packed uint8_t representation (8x memory  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1103-1](../sources/experiences/exp-o-kd-20260519-1103-1.md) | Replace bool-per-element mask with bit-packed uint8_t mask (8 bits per byte), re | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1930-1](../sources/experiences/exp-o-kd-20260519-1930-1.md) | Replace the 2D batch-split grid with a 1D flat warp-per-token model where flat_w | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1940-1](../sources/experiences/exp-o-kd-20260519-1940-1.md) | Fuse the reduce and quantize kernels into a single kernel that computes softmax  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1941-1](../sources/experiences/exp-o-kd-20260519-1941-1.md) | Fuse reduce_kernel_float and quantize_kernel_fp8 into a single reduce_kernel_fus | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1942-1](../sources/experiences/exp-o-kd-20260519-1942-1.md) | Fuse the FP8 output scale into the reduce kernel by computing out_scale = 1.0f / | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1963-1](../sources/experiences/exp-o-kd-20260519-1963-1.md) | Fuse FP8 quantization directly into the merge kernel using a compile-time bool t | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1964-1](../sources/experiences/exp-o-kd-20260519-1964-1.md) | Fuse FP8 quantization into the merge kernel by adding a compile-time USE_FP8_OUT | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1965-1](../sources/experiences/exp-o-kd-20260519-1965-1.md) | Pre-compute the reciprocal scale_inv = 1.0f / scale once at kernel entry, then r | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1966-1](../sources/experiences/exp-o-kd-20260519-1966-1.md) | Pre-invert the scale once per thread (1.0f / scale) and replace the per-element  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1967-1](../sources/experiences/exp-o-kd-20260519-1967-1.md) | Fuse FP8 quantization inline by extending the kernel template with output_t and  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1982-1](../sources/experiences/exp-o-kd-20260519-1982-1.md) | Replace packed layout with NHD (Natural Head Dimension) layout [num_blocks, bloc | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1986-1](../sources/experiences/exp-o-kd-20260519-1986-1.md) | Replace scalar 1-element-per-thread processing with vectorized int4 loads (8 bf1 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1987-1](../sources/experiences/exp-o-kd-20260519-1987-1.md) | Restructured NoPE processing from 1-element-per-thread to int4 vectorized 8-elem | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1987-2](../sources/experiences/exp-o-kd-20260519-1987-2.md) | Vectorize RoPE copy from 1-element-per-thread to 2-element-per-thread by loading | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2024-1](../sources/experiences/exp-o-kd-20260519-2024-1.md) | Add an early-exit fast path that checks token_idx >= prefix_num_tokens at the to | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2025-1](../sources/experiences/exp-o-kd-20260519-2025-1.md) | Add a prefix_num_tokens kernel parameter and an early-exit branch: threads handl | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2026-1](../sources/experiences/exp-o-kd-20260519-2026-1.md) | Add an early-exit branch at the top of the kernel: when token_idx >= prefix_num_ | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2081-1](../sources/experiences/exp-o-kd-20260519-2081-1.md) | Add ENTRY_SIZE and CTA_SIZE as compile-time template parameters, replacing runti | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2120-1](../sources/experiences/exp-o-kd-20260519-2120-1.md) | Eliminate the cudaMemcpy2D intermediate copy by passing a runtime q_stride param | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2121-1](../sources/experiences/exp-o-kd-20260519-2121-1.md) | Add a q_stride kernel parameter set to query.stride(0) from the host launcher, r | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2125-1](../sources/experiences/exp-o-kd-20260519-2125-1.md) | Store K-cache as FP8-E5M2 (1 byte/element) and dequantize to fp16 via software b | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2126-1](../sources/experiences/exp-o-kd-20260519-2126-1.md) | Store K-cache in FP8-E5M2 (1 byte/element) instead of fp16, halving DRAM traffic | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2127-1](../sources/experiences/exp-o-kd-20260519-2127-1.md) | Conditionally read K-cache as FP8-E5M2 packed vectors (Quant_vec) and dequantize | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2128-1](../sources/experiences/exp-o-kd-20260519-2128-1.md) | Store KV cache in FP8-E5M2 (1 byte) instead of FP16 (2 bytes) by adding a separa | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2129-1](../sources/experiences/exp-o-kd-20260519-2129-1.md) | Extend the kernel with a separate cache_t type parameter and compile-time is_fp8 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2154-1](../sources/experiences/exp-o-kd-20260519-2154-1.md) | Fuse paged_kv_last_page_len (block_offset + 1) and block_table_bound (div_ceil(n | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2198-1](../sources/experiences/exp-o-kd-20260519-2198-1.md) | Increase BLOCK_SIZE from 16 to 32 so THREAD_GROUP_SIZE becomes 1, eliminating th | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2199-1](../sources/experiences/exp-o-kd-20260519-2199-1.md) | Increase BLOCK_SIZE from 16 to 32 so THREAD_GROUP_SIZE becomes 1, enabling each  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2200-1](../sources/experiences/exp-o-kd-20260519-2200-1.md) | Increase BLOCK_SIZE from 16 to 32 so that THREAD_GROUP_SIZE becomes 1, eliminati | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2201-1](../sources/experiences/exp-o-kd-20260519-2201-1.md) | Increase BLOCK_SIZE from 16 to 32 to set THREAD_GROUP_SIZE=1, eliminating intra- | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2203-1](../sources/experiences/exp-o-kd-20260519-2203-1.md) | Add an `else if (block_size == 32)` branch calling `single_query_cached_kv_atten | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2204-1](../sources/experiences/exp-o-kd-20260519-2204-1.md) | Add an `else if (block_size == 32)` dispatch branch calling `multi_query_cached_ | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2256-1](../sources/experiences/exp-o-kd-20260519-2256-1.md) | Consolidate all three kernels into a single templated advance_step_kernel that r | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2257-1](../sources/experiences/exp-o-kd-20260519-2257-1.md) | Fuse all three per-query metadata updates (token copy, seq_len/position incremen | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2261-1](../sources/experiences/exp-o-kd-20260519-2261-1.md) | Change k_scale and v_scale kernel parameters from scalar float (pass-by-value) t | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2262-1](../sources/experiences/exp-o-kd-20260519-2262-1.md) | Change k_scale/v_scale from scalar-by-value kernel parameters to device pointers | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2264-1](../sources/experiences/exp-o-kd-20260519-2264-1.md) | Change k_scale and v_scale from scalar float to float* pointer parameters so the | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2265-1](../sources/experiences/exp-o-kd-20260519-2265-1.md) | Change k_scale and v_scale from scalar float to pointer (float*) parameters and  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2280-1](../sources/experiences/exp-o-kd-20260519-2280-1.md) | Distribute heads across warps (one warp per head iteration) and use vectorize_wi | optimization | sm90 | cuda-cpp |
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

## convolution

| ID | Title | Type | Architectures | Languages |
|----|-------|------|--------------|-----------|
| [exp-a-kd-20260518-0048](../sources/experiences/exp-a-kd-20260518-0048.md) | Replace per-access coordinate recomputation with precomputed bitmask validity ma | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0053](../sources/experiences/exp-a-kd-20260518-0053.md) | Replace plain integer div/mod with FastDivmod using __umulhi (single-cycle on SM | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0084](../sources/experiences/exp-a-kd-20260518-0084.md) | conv_interleaved_store | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0047-1](../sources/experiences/exp-a-kd-20260519-0047-1.md) | Precompute the four increment values into a Params struct (inc_next[4]) on the h | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0048-1](../sources/experiences/exp-a-kd-20260519-0048-1.md) | Precompute per-dimension validity as bitmasks at host construction time (one bit | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0052-1](../sources/experiences/exp-a-kd-20260519-0052-1.md) | Replace plain integer div/mod with FastDivmod objects that use __umulhi (single  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0052-2](../sources/experiences/exp-a-kd-20260519-0052-2.md) | Precompute per-row byte-offset increments (inc_next_s/r/t) derived from stride,  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0053-1](../sources/experiences/exp-a-kd-20260519-0053-1.md) | Replace six plain div/mod operations with FastDivmod structs precomputed outside | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0053-2](../sources/experiences/exp-a-kd-20260519-0053-2.md) | Precompute byte-offset increments (inc_next_s/r/t) for filter dimension traversa | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0065-1](../sources/experiences/exp-a-kd-20260519-0065-1.md) | Switch to kOptimized iterator algorithm with kUnity stride support, which precom | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0066-1](../sources/experiences/exp-a-kd-20260519-0066-1.md) | Switch from kAnalytic/kStrided to kOptimized/kUnity iterator: the optimized iter | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0067-1](../sources/experiences/exp-a-kd-20260519-0067-1.md) | Switch from IteratorAlgorithm::kAnalytic to IteratorAlgorithm::kOptimized, which | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0084-1](../sources/experiences/exp-a-kd-20260519-0084-1.md) | Replace C++ if-guarded store with inline PTX @p st.global.v4.u32 predicated stor | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-2340-1](../sources/experiences/exp-a-kd-20260519-2340-1.md) | Remove the 'static' qualifier from the local constexpr bool variable, since 'con | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2341-1](../sources/experiences/exp-a-kd-20260519-2341-1.md) | Add a varlen guard to the VecLoad condition so that vectorized loads are only en | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2342-1](../sources/experiences/exp-a-kd-20260519-2342-1.md) | Replace multiple scattered 'if (channel_id < dim)' guard conditionals with a sin | analysis | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0221-1](../sources/experiences/exp-o-kd-20260519-0221-1.md) | Replace six plain integer div/mod operations with three FastDivmod objects that  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0221-2](../sources/experiences/exp-o-kd-20260519-0221-2.md) | Compute base_offset once at the (n,d0,h0,w0,fc) corner using ndhwc_offset, then  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0222-1](../sources/experiences/exp-o-kd-20260519-0222-1.md) | Replace six plain integer div/mod operations with FastDivmod::divmod() calls tha | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0222-2](../sources/experiences/exp-o-kd-20260519-0222-2.md) | Compute base_offset once at (n, d0, h0, w0, fc) and add precomputed byte increme | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0225-1](../sources/experiences/exp-o-kd-20260519-0225-1.md) | Switch to kOptimized iterator algorithm with kUnity stride support, which precom | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0226-1](../sources/experiences/exp-o-kd-20260519-0226-1.md) | Switch from kAnalytic iterator to kOptimized iterator with kUnity stride support | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0227-1](../sources/experiences/exp-o-kd-20260519-0227-1.md) | Replace IteratorAlgorithm::kAnalytic with IteratorAlgorithm::kOptimized, which p | optimization | sm90 | cuda-cpp, cute-dsl |

## copy

| ID | Title | Type | Architectures | Languages |
|----|-------|------|--------------|-----------|
| [exp-a-kd-20260518-0050](../sources/experiences/exp-a-kd-20260518-0050.md) | Replace ld.global.cg with ld.global.cs (cache streaming) hint to minimize L2 cac | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0051](../sources/experiences/exp-a-kd-20260518-0051.md) | Switch cache hint from .cs (streaming, bypass L2) to .cg (cache-all levels) for  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0090](../sources/experiences/exp-a-kd-20260518-0090.md) | Add the missing kRow multiplier into the row offset calculation so that byte_poi | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0100](../sources/experiences/exp-a-kd-20260518-0100.md) | Replace per-element scalar index decomposition with shared-memory tiling: 192 th | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0141](../sources/experiences/exp-a-kd-20260518-0141.md) | Wrap tile selection in a compile-time if-constexpr guard that checks compatible( | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-0174](../sources/experiences/exp-a-kd-20260518-0174.md) | Replace four scalar st.shared instructions with the SM90 stmatrix.sync.aligned.x | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0176](../sources/experiences/exp-a-kd-20260518-0176.md) | Replace synchronous smem[i]=g_in[i] with cp.async.ca.shared.global PTX instructi | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0177](../sources/experiences/exp-a-kd-20260518-0177.md) | Replace synchronous LDG+STS with cp.async.ca.shared.global inline PTX for asynch | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0003-1](../sources/experiences/exp-a-kd-20260519-0003-1.md) | Add a runtime bool guard (is_accumulator_needed = K > 0) that wraps the accumula | analysis | sm100 | cuda-cpp |
| [exp-a-kd-20260519-0011-1](../sources/experiences/exp-a-kd-20260519-0011-1.md) | Merge two separate elect_one_sync() guards into a single __ballot_sync + __syncw | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0050-1](../sources/experiences/exp-a-kd-20260519-0050-1.md) | Replace ld.global.cg with ld.global.cs (cache streaming) hint on 128-bit loads t | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0051-1](../sources/experiences/exp-a-kd-20260519-0051-1.md) | Switch from ld.global.cs.f32 (streaming, bypasses L2) to ld.global.cg.f32 (cache | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0054-1](../sources/experiences/exp-a-kd-20260519-0054-1.md) | Increase kFragmentsPerIteration from 1 to 2, halving sync barriers from 16 to 8  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0089-1](../sources/experiences/exp-a-kd-20260519-0089-1.md) | Add the missing kRow multiplier to the row offset term so that byte_pointer adva | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0100-1](../sources/experiences/exp-a-kd-20260519-0100-1.md) | Replace scalar per-element index decomposition with cooperative shared-memory ti | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0103-1](../sources/experiences/exp-a-kd-20260519-0103-1.md) | Reinterpret pointers as float2 and halve the channel dimensions (c_in/2, c_out/2 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0141-1](../sources/experiences/exp-a-kd-20260519-0141-1.md) | Wrap tile selection in a compile-time if-constexpr guard that checks compatible( | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0174-1](../sources/experiences/exp-a-kd-20260519-0174-1.md) | Replace four scalar uint32 shared-memory stores with the SM90 stmatrix.sync.alig | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0176-1](../sources/experiences/exp-a-kd-20260519-0176-1.md) | Replace synchronous LDG+STS loads with cp.async.ca.shared.global PTX instruction | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0177-1](../sources/experiences/exp-a-kd-20260519-0177-1.md) | Replace synchronous LDG+STS with cp.async.ca.shared.global inline PTX to issue a | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0320-1](../sources/experiences/exp-a-kd-20260519-0320-1.md) | Switch the alignment variable from stride_last (always 1) to stride_heads=kHeadD | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0321-1](../sources/experiences/exp-a-kd-20260519-0321-1.md) | Replace stride_last=1 with stride_heads=kHeadDim in the alignment check so the d | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0776-1](../sources/experiences/exp-a-kd-20260519-0776-1.md) | Replace per-thread scalar processing with warp-cooperative vectorized access: ea | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0777-1](../sources/experiences/exp-a-kd-20260519-0777-1.md) | Load k_rope once into a register variable (k_rope_buf) before the loop, then reu | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0779-1](../sources/experiences/exp-a-kd-20260519-0779-1.md) | Replace scalar bf16 loads/stores with vectorized int2 (8-byte) and int (4-byte)  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0780-1](../sources/experiences/exp-a-kd-20260519-0780-1.md) | Replace scalar bf16 element-wise reads/writes with vectorized int2 (128-bit, 8 b | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0821-1](../sources/experiences/exp-a-kd-20260519-0821-1.md) | Replace per-lane scalar 64-bit PTX load/store with paired 128-bit v2.b64 instruc | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0822-1](../sources/experiences/exp-a-kd-20260519-0822-1.md) | Replace scalar 64-bit PTX load/store with vectorized 128-bit .v2.b64 variants th | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0823-1](../sources/experiences/exp-a-kd-20260519-0823-1.md) | Replace 17 scalar 64-bit transfers with 8 vectorized 128-bit transfers (ld.globa | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0824-1](../sources/experiences/exp-a-kd-20260519-0824-1.md) | The after code uses PTX inline asm ld.volatile.global.v2.b32 to bypass L1 cache  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0831-1](../sources/experiences/exp-a-kd-20260519-0831-1.md) | Fuse all 5 metadata copy operations into a single kernel launch using a paramete | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0832-1](../sources/experiences/exp-a-kd-20260519-0832-1.md) | Fuse all 5 metadata copy operations into a single kernel using a parameter struc | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0833-1](../sources/experiences/exp-a-kd-20260519-0833-1.md) | Fuse all 5 metadata copy operations into a single templated kernel using a Fused | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0834-1](../sources/experiences/exp-a-kd-20260519-0834-1.md) | Bundle all kernel parameters (10 pointers + 3 scalars) into a single FusedMetada | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0835-1](../sources/experiences/exp-a-kd-20260519-0835-1.md) | Bundle all kernel parameters into a single FusedMetadataCopyParams struct and pa | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0836-1](../sources/experiences/exp-a-kd-20260519-0836-1.md) | Fuse 3 separate kernel launches into a single multi-destination kernel that read | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0837-1](../sources/experiences/exp-a-kd-20260519-0837-1.md) | Fuse 3 separate single-destination kernel launches into one multi-destination ke | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0840-1](../sources/experiences/exp-a-kd-20260519-0840-1.md) | Replace the generic loop-based PTX 8-byte transfer with a page-padded memory lay | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0841-1](../sources/experiences/exp-a-kd-20260519-0841-1.md) | Replace linear interleaved layout with DSv4 page-padded layout: group 64 items p | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0841-2](../sources/experiences/exp-a-kd-20260519-0841-2.md) | Replace variable-count qword loop with a fixed 3-operation pattern per lane: loa | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0861-1](../sources/experiences/exp-a-kd-20260519-0861-1.md) | Split the single evictable category into two sub-categories — misses (recently l | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0863-1](../sources/experiences/exp-a-kd-20260519-0863-1.md) | The after code attempts to accelerate the streaming copy by (1) using PTX-level  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0864-1](../sources/experiences/exp-a-kd-20260519-0864-1.md) | Replace two-phase buffered load-then-store with a software-pipelined loop that p | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0865-1](../sources/experiences/exp-a-kd-20260519-0865-1.md) | The after kernel wraps all loads and stores in inline PTX asm with L1::no_alloca | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0865-2](../sources/experiences/exp-a-kd-20260519-0865-2.md) | The after kernel replaces the two-phase load-all-then-store-all pattern with a s | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0877-1](../sources/experiences/exp-a-kd-20260519-0877-1.md) | Replace scalar float loads/stores with float4 (128-bit) vectorized access via ca | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0883-1](../sources/experiences/exp-a-kd-20260519-0883-1.md) | Scan the index arrays for consecutive runs where both src_diff==1 and dst_diff== | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0884-1](../sources/experiences/exp-a-kd-20260519-0884-1.md) | Detect runs of consecutive pages (where both src_idx and dst_idx advance by 1) a | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0994-1](../sources/experiences/exp-a-kd-20260519-0994-1.md) | Remove the alignas(64) constraint by replacing AlignedStorage with LocalStorage  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0995-1](../sources/experiences/exp-a-kd-20260519-0995-1.md) | Remove the alignas directive from the local storage struct (renamed AlignedStora | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0996-1](../sources/experiences/exp-a-kd-20260519-0996-1.md) | Guard the entire V-cache transfer block with if constexpr (!kIsMLA), a compile-t | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0997-1](../sources/experiences/exp-a-kd-20260519-0997-1.md) | Add a compile-time bool constant kIsMLA and guard the entire V-cache load/store  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1154-1](../sources/experiences/exp-a-kd-20260519-1154-1.md) | Generalize the kernel to a triple-template design (scalar_t, cache_t, kv_dt enum | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1164-1](../sources/experiences/exp-a-kd-20260519-1164-1.md) | Replace 16 separate cudaMemcpyAsync D2D calls with a single copy_blocks_kernel l | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1165-1](../sources/experiences/exp-a-kd-20260519-1165-1.md) | Replace 64 individual cudaMemcpyAsync dispatches with a single CUDA kernel launc | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1175-1](../sources/experiences/exp-a-kd-20260519-1175-1.md) | Replace coalesce() with a structured 2D layout that groups 256 consecutive 4-bit | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1191-1](../sources/experiences/exp-a-kd-20260519-1191-1.md) | Fuse the two index_select kernels and the cache_write kernel into a single kerne | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1192-1](../sources/experiences/exp-a-kd-20260519-1192-1.md) | Use C++17 if constexpr with template parameters and an enum class non-type param | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1269-1](../sources/experiences/exp-a-kd-20260519-1269-1.md) | Wrap 4 floats into a __align__(16) array_t<float,4> struct and operate on packed | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1270-1](../sources/experiences/exp-a-kd-20260519-1270-1.md) | Pack 8 half values into a 16-byte __align__(16) struct and cast pointers so each | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1297-1](../sources/experiences/exp-a-kd-20260519-1297-1.md) | Raise AlignmentCD to 8 for fp16 output and explicitly pack 8 fp16 values into a  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1308-1](../sources/experiences/exp-a-kd-20260519-1308-1.md) | Reinterpret float pointers as uint4 (128-bit) pointers so each load/store moves  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1309-1](../sources/experiences/exp-a-kd-20260519-1309-1.md) | Replace scalar half-element copy loop with 128-bit vectorized uint4 load/store,  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1319-1](../sources/experiences/exp-a-kd-20260519-1319-1.md) | Add kv_scale_stride parameter to generalize scale loading: extend the fast-path  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1320-1](../sources/experiences/exp-a-kd-20260519-1320-1.md) | Move scale loading inside the per-head warp loop using indexed access k_scale[he | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1366-1](../sources/experiences/exp-a-kd-20260519-1366-1.md) | Assign one warp to each (token, head) pair, computing source and destination bas | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1366-2](../sources/experiences/exp-a-kd-20260519-1366-2.md) | Use inline PTX vectorized 128-bit int4 load/store (ld.global.cs.v4.u32 / st.glob | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1367-1](../sources/experiences/exp-a-kd-20260519-1367-1.md) | Assign one warp to each (token, head) pair and compute the non-contiguous base p | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1367-2](../sources/experiences/exp-a-kd-20260519-1367-2.md) | Replace scalar bfloat16 accesses with inline PTX asm 128-bit (int4) vectorized l | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1368-1](../sources/experiences/exp-a-kd-20260519-1368-1.md) | Assign one warp per (token, head) pair so each of the 32 lanes maps to a dimensi | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1368-2](../sources/experiences/exp-a-kd-20260519-1368-2.md) | Replace scalar bf16 load/store with 128-bit vectorized int4 load/store via inlin | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1369-1](../sources/experiences/exp-a-kd-20260519-1369-1.md) | Replace scalar bf16 copy loops with 128-bit vectorized cache-streaming loads/sto | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1370-1](../sources/experiences/exp-a-kd-20260519-1370-1.md) | Replace scalar bf16 loads/stores with 128-bit vectorized int4 loads/stores via r | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1370-2](../sources/experiences/exp-a-kd-20260519-1370-2.md) | Use inline PTX cache-streaming hints (ld.global.cs / st.global.cs) on all loads  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1371-1](../sources/experiences/exp-a-kd-20260519-1371-1.md) | Replace __ldg/plain stores with ld.global.cs.b32/st.global.cs.b32 PTX instructio | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1372-1](../sources/experiences/exp-a-kd-20260519-1372-1.md) | Replace __ldg-based loads and plain stores with PTX inline assembly using .cs (c | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1404-1](../sources/experiences/exp-a-kd-20260519-1404-1.md) | Remove reverse_map and permuted_idx side-effect writes entirely and simplify the | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1405-1](../sources/experiences/exp-a-kd-20260519-1405-1.md) | Remove side-effect writes (reverse_map, permuted_idx) from the kernel entirely,  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1437-1](../sources/experiences/exp-a-kd-20260519-1437-1.md) | Replace the unconditional deep clone with a lazy shallow pointer assignment when | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1465-1](../sources/experiences/exp-a-kd-20260519-1465-1.md) | Replace the hardcoded (kv_lora_rank + pe_dim) stride with a runtime entry_stride | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1477-1](../sources/experiences/exp-a-kd-20260519-1477-1.md) | Replace scalar bf16 load/store loop with vectorized float4-width (8 bf16 element | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1478-1](../sources/experiences/exp-a-kd-20260519-1478-1.md) | Replace scalar bf16 load/store with float4-width vectorized transactions using a | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1479-1](../sources/experiences/exp-a-kd-20260519-1479-1.md) | Replace batch-split 2D grid (batch × num_splits, 1024 threads/CTA) with per-toke | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1480-1](../sources/experiences/exp-a-kd-20260519-1480-1.md) | Replace batch-split grid (1024-thread CTAs with nested block/token loops) with p | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1481-1](../sources/experiences/exp-a-kd-20260519-1481-1.md) | Convert entry_size and CTA_SIZE into compile-time template parameters (ENTRY_SIZ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1482-1](../sources/experiences/exp-a-kd-20260519-1482-1.md) | Convert entry_size and CTA_SIZE into C++ template parameters (ENTRY_SIZE_T, CTA_ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1483-1](../sources/experiences/exp-a-kd-20260519-1483-1.md) | Replace single-CTA sequential block-level loop with a per-token direct addressin | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1484-1](../sources/experiences/exp-a-kd-20260519-1484-1.md) | Replace single-CTA nested block/token loop with a per-token-direct kernel where  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1571-1](../sources/experiences/exp-a-kd-20260519-1571-1.md) | Replace the 4-type dispatch macro with a 3-type variant (DISPATCH_3_FLOATING_TYP | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1572-1](../sources/experiences/exp-a-kd-20260519-1572-1.md) | Replace AT_DISPATCH_FLOATING_TYPES_AND2 (4 types including double) with VLLM_DIS | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1579-1](../sources/experiences/exp-a-kd-20260519-1579-1.md) | Introduce a separate cache_t template parameter and an is_fp8_e5m2_kv_cache comp | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1610-1](../sources/experiences/exp-a-kd-20260519-1610-1.md) | The before kernel's 2D TiledCopy partition computes thread-to-row/col mapping on | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1613-1](../sources/experiences/exp-a-kd-20260519-1613-1.md) | Precompute a single thread_base (b * blockDim.x * values_per_thread + threadIdx. | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1632-1](../sources/experiences/exp-a-kd-20260519-1632-1.md) | Replace hardcoded dimension products with explicit int64_t stride parameters (pa | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1633-1](../sources/experiences/exp-a-kd-20260519-1633-1.md) | Replace hardcoded inline dimension products with pre-computed int64_t stride par | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1634-1](../sources/experiences/exp-a-kd-20260519-1634-1.md) | Replace scalar half-element loads with 128-bit vectorized loads via cutlass::Arr | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-1635-1](../sources/experiences/exp-a-kd-20260519-1635-1.md) | Replace individual float32 loads/stores with 128-bit vectorized loads via cutlas | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-1642-1](../sources/experiences/exp-a-kd-20260519-1642-1.md) | Replace template-parameterized PackedVec_Old with a concrete u32x8_t struct whos | analysis | sm100 | cuda-cpp |
| [exp-a-kd-20260519-1643-1](../sources/experiences/exp-a-kd-20260519-1643-1.md) | Remove the PackedVec16_Old template wrapper and reinterpret_cast overlay entirel | analysis | sm100 | cuda-cpp |
| [exp-a-kd-20260519-1732-1](../sources/experiences/exp-a-kd-20260519-1732-1.md) | The after code attempts to use an uncached allocation path (hipExtMallocWithFlag | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1738-1](../sources/experiences/exp-a-kd-20260519-1738-1.md) | Add cudaMemAdviseSetAccessedBy hint after cudaMalloc to advise the driver that t | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1761-1](../sources/experiences/exp-a-kd-20260519-1761-1.md) | Read the stride directly from the tensor's actual leading dimension (LDA) instea | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1762-1](../sources/experiences/exp-a-kd-20260519-1762-1.md) | Read the actual leading dimension from the input tensor (lda = a.stride(0)) and  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1805-1](../sources/experiences/exp-a-kd-20260519-1805-1.md) | Merge the two separate kernels into a single templated kernel (concat_and_cache_ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1806-1](../sources/experiences/exp-a-kd-20260519-1806-1.md) | Fuse the two kernels into a single launch using a templated kernel (concat_and_c | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2297-1](../sources/experiences/exp-a-kd-20260519-2297-1.md) | Apply 4x loop unrolling with separated read/write phases: batch all 4 cache read | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2298-1](../sources/experiences/exp-a-kd-20260519-2298-1.md) | Apply loop unrolling with factor=4 and separate the read phase (batch all __ldg  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2318-1](../sources/experiences/exp-a-kd-20260519-2318-1.md) | Change scale parameters from scalar float (by-value) to float pointers, allowing | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2319-1](../sources/experiences/exp-a-kd-20260519-2319-1.md) | The pointer-based parameter passing is purely an API change with no genuine opti | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2320-1](../sources/experiences/exp-a-kd-20260519-2320-1.md) | Switch k_scale/v_scale from scalar float pass-by-value to const float* pointers  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2329-1](../sources/experiences/exp-a-kd-20260519-2329-1.md) | The after kernel assigns one thread per head-block (num_heads*(head_size/x)=64 t | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2330-1](../sources/experiences/exp-a-kd-20260519-2330-1.md) | Restructure thread mapping from strided scalar loop (512 threads iterating all e | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2335-1](../sources/experiences/exp-a-kd-20260519-2335-1.md) | Pre-compute source and destination base pointers once outside the loop using tok | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2335-2](../sources/experiences/exp-a-kd-20260519-2335-2.md) | Use VEC_SIZE=8 (128-bit) vectorized loads and stores via vec_n_t<half,8> to tran | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2336-1](../sources/experiences/exp-a-kd-20260519-2336-1.md) | Pre-compute source and destination base pointers once outside the loop, then use | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2337-1](../sources/experiences/exp-a-kd-20260519-2337-1.md) | Distribute heads across warps (warp-per-head decomposition) so each warp owns a  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2338-1](../sources/experiences/exp-a-kd-20260519-2338-1.md) | Decompose work into warp-per-head assignments (8 warps for 32 heads, each warp h | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2356-1](../sources/experiences/exp-a-kd-20260519-2356-1.md) | The after code unifies both paths into a single loop over largest_part with a co | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2357-1](../sources/experiences/exp-a-kd-20260519-2357-1.md) | Merge the two separate loop sections into a single unified loop over largest_par | analysis | sm90 | cuda-cpp |
| [exp-i-kd-20260519-2388-1](../sources/experiences/exp-i-kd-20260519-2388-1.md) | Construct a PredicatedTileIterator with PitchLinearWarpRakedThreadMap to load a  | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2389-1](../sources/experiences/exp-i-kd-20260519-2389-1.md) | Implement a two-phase copy loop using PredicatedTileIterator: zero-initialize th | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2406-1](../sources/experiences/exp-i-kd-20260519-2406-1.md) | Use make_coord(_,_) to slice tiled tensors by blockIdx indices, local_partition  | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2407-1](../sources/experiences/exp-i-kd-20260519-2407-1.md) | Implement the canonical 6-step CUTE tensor copy pipeline: slice source/destinati | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2408-1](../sources/experiences/exp-i-kd-20260519-2408-1.md) | Build a CUTE tensor pipeline: make_identity_tensor generates coordinate tensor,  | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2409-1](../sources/experiences/exp-i-kd-20260519-2409-1.md) | Use the Cute library's make_identity_tensor + elem_less transform for coordinate | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2410-1](../sources/experiences/exp-i-kd-20260519-2410-1.md) | Use cute::block_id_in_cluster() to obtain the cluster-local block coordinates, t | implementation | sm90 | cuda-cpp |
| [exp-i-kd-20260519-2411-1](../sources/experiences/exp-i-kd-20260519-2411-1.md) | Implement scalar class with unique_ptr RAII wrapping cudaMalloc and custom scala | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2412-1](../sources/experiences/exp-i-kd-20260519-2412-1.md) | Implement cluster shape validation using check_cluster_shape template, parameter | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2413-1](../sources/experiences/exp-i-kd-20260519-2413-1.md) | Implement cluster shape validation via a templated check_cluster_shape function, | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2428-1](../sources/experiences/exp-i-kd-20260519-2428-1.md) | Use if-constexpr dispatch based on Mode to route to specialized __device__ funct | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2430-1](../sources/experiences/exp-i-kd-20260519-2430-1.md) | Use CUTE tensor abstractions (make_tensor + make_smem_ptr/make_gmem_ptr + Int<1> | implementation | sm90 | cuda-cpp |
| [exp-i-kd-20260519-2431-1](../sources/experiences/exp-i-kd-20260519-2431-1.md) | Declare a stride-indexed __shared__ uint32_t array sized 32*count, load global m | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2432-1](../sources/experiences/exp-i-kd-20260519-2432-1.md) | Implement the three-stage pipeline: (1) strided gmem→smem load with stride equal | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2433-1](../sources/experiences/exp-i-kd-20260519-2433-1.md) | Allocate aligned shared memory via SharedStorage, construct CuTe tensors for SME | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2434-1](../sources/experiences/exp-i-kd-20260519-2434-1.md) | Use a strided thread-indexed loop where each thread copies elements at stride bl | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2434-2](../sources/experiences/exp-i-kd-20260519-2434-2.md) | Construct an output GMEM tensor, instantiate Copy_Traits<SM90_BULK_COPY_AUTO> fo | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2435-1](../sources/experiences/exp-i-kd-20260519-2435-1.md) | Stage data through three tiers using uint32_t register arrays for gmem→rmem load | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2436-1](../sources/experiences/exp-i-kd-20260519-2436-1.md) | Implement the complete CUTE tensor pipeline: construct global and shared memory  | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2438-1](../sources/experiences/exp-i-kd-20260519-2438-1.md) | Use CUTE's tensor abstraction to create gmem tensors with uint32_t reinterpretat | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2439-1](../sources/experiences/exp-i-kd-20260519-2439-1.md) | Use CuTe's local_tile(gC, tiler, 0) to partition the global tensor into an 8x8 t | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2450-1](../sources/experiences/exp-i-kd-20260519-2450-1.md) | Compute packed NHWC strides (ldc=C, ldw=C*W, ldh=C*W*H), construct TensorNHWC la | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2452-1](../sources/experiences/exp-i-kd-20260519-2452-1.md) | Use CUTLASS PredicatedTileIterator to decompose the copy into threadblock-level  | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0198-1](../sources/experiences/exp-o-kd-20260519-0198-1.md) | Add a K>0 guard (is_accumulator_needed) that branches between copying valid accu | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0249-1](../sources/experiences/exp-o-kd-20260519-0249-1.md) | Replace per-element modular index decomposition with cooperative shared-memory t | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0249-2](../sources/experiences/exp-o-kd-20260519-0249-2.md) | Reformulate the kernel around float4 (128-bit) vectorized I/O: input is cast to  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0273-1](../sources/experiences/exp-o-kd-20260519-0273-1.md) | Wrap tile selection in a compile-time if-constexpr guard that checks compatible( | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0274-1](../sources/experiences/exp-o-kd-20260519-0274-1.md) | Add a compile-time compatibility guard using compatible(shape(CTA_Tile{}), shape | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0342-1](../sources/experiences/exp-o-kd-20260519-0342-1.md) | Replace the misaligned stride_last=1 with stride_heads=kHeadDim (=64) so the ali | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0596-1](../sources/experiences/exp-o-kd-20260519-0596-1.md) | Assign one warp per 16-head chunk per token; each lane uses int2 (8-byte) vector | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0596-2](../sources/experiences/exp-o-kd-20260519-0596-2.md) | Load k_rope once per warp into a register buffer (k_rope_buf as int, covering 2  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0597-1](../sources/experiences/exp-o-kd-20260519-0597-1.md) | Replace scalar grid-stride loop with warp-cooperative parallelism: each warp own | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0598-1](../sources/experiences/exp-o-kd-20260519-0598-1.md) | Replace scalar bf16 j-loops with reinterpret_cast<int2*> (8-byte) reads/writes f | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0598-2](../sources/experiences/exp-o-kd-20260519-0598-2.md) | Hoist k_rope read outside the head loop into a register buffer (KRopeBufType k_r | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0599-1](../sources/experiences/exp-o-kd-20260519-0599-1.md) | Replace scalar bf16 read/write loops with vectorized int2 (16-byte, covering 8 b | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0627-1](../sources/experiences/exp-o-kd-20260519-0627-1.md) | Fuse all five metadata copy operations into a single kernel launch using a param | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0628-1](../sources/experiences/exp-o-kd-20260519-0628-1.md) | Fuse all 5 metadata copy operations into a single kernel that uses a __grid_cons | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0629-1](../sources/experiences/exp-o-kd-20260519-0629-1.md) | Fuse all 5 metadata copy operations into a single kernel that iterates over each | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0630-1](../sources/experiences/exp-o-kd-20260519-0630-1.md) | Fuse three separate single-destination kernel launches into one multi-destinatio | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0631-1](../sources/experiences/exp-o-kd-20260519-0631-1.md) | Fuse 3 separate single-destination kernel launches into a single multi-destinati | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0635-1](../sources/experiences/exp-o-kd-20260519-0635-1.md) | Restructure device-side layout into page-padded format: group 64 items' value da | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0635-2](../sources/experiences/exp-o-kd-20260519-0635-2.md) | Replace the variable-count loop with a fixed 3-load/store pattern per lane: 2 va | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0636-1](../sources/experiences/exp-o-kd-20260519-0636-1.md) | Introduce a DSv4-specific transfer path via IsDsv4Layout template flag that call | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0673-1](../sources/experiences/exp-o-kd-20260519-0673-1.md) | Scan the index arrays for consecutive runs where both src_diff==1 and dst_diff== | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0674-1](../sources/experiences/exp-o-kd-20260519-0674-1.md) | Detect consecutive runs in both source and destination index arrays at runtime a | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0675-1](../sources/experiences/exp-o-kd-20260519-0675-1.md) | Scan all index pairs and detect consecutive runs where both src_diff==1 and dst_ | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0752-1](../sources/experiences/exp-o-kd-20260519-0752-1.md) | Add a compile-time constexpr bool kIsMLA template parameter and guard the entire | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0753-1](../sources/experiences/exp-o-kd-20260519-0753-1.md) | Introduce a compile-time constant kIsMLA and wrap the V-cache transfer code in i | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0755-1](../sources/experiences/exp-o-kd-20260519-0755-1.md) | Add a bool kIsMLA template parameter to the kernel and wrap all V-cache pointer  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1887-1](../sources/experiences/exp-o-kd-20260519-1887-1.md) | Replace the CPU-side loop of individual cudaMemcpyAsync calls with a single CUDA | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1888-1](../sources/experiences/exp-o-kd-20260519-1888-1.md) | Replace the 64 sequential cudaMemcpyAsync dispatches with a single CUDA kernel l | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1889-1](../sources/experiences/exp-o-kd-20260519-1889-1.md) | Replace the CPU-loop cudaMemcpyAsync approach with a single-launch CUDA kernel ( | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1905-1](../sources/experiences/exp-o-kd-20260519-1905-1.md) | Fuse all three kernels into a single kernel that reads source kv_c and k_pe tens | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1949-1](../sources/experiences/exp-o-kd-20260519-1949-1.md) | Wrap 4 floats into a __align__(16) array_t<float,4> struct so that each load/sto | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1950-1](../sources/experiences/exp-o-kd-20260519-1950-1.md) | Pack 8 half values into a __align__(16) struct (16 bytes) so the compiler emits  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1976-1](../sources/experiences/exp-o-kd-20260519-1976-1.md) | Reinterpret float pointers as uint4 (128-bit) pointers to issue 16-byte load/sto | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1977-1](../sources/experiences/exp-o-kd-20260519-1977-1.md) | Replace scalar half load/store with 128-bit uint4 vectorized accesses that pack  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1983-1](../sources/experiences/exp-o-kd-20260519-1983-1.md) | Replace packed interleaved layout with flat NHD (num_blocks, block_size, num_hea | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2015-1](../sources/experiences/exp-o-kd-20260519-2015-1.md) | Assign one warp to each (token, head) pair so the base pointer is computed once  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2015-2](../sources/experiences/exp-o-kd-20260519-2015-2.md) | Use inline PTX ld.global.cs.v4.u32 / st.global.cs.v4.u32 (128-bit vector loads/s | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2016-1](../sources/experiences/exp-o-kd-20260519-2016-1.md) | Map each warp to one (token, head) pair via flat_warp_id = tid >> 5, compute the | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2016-2](../sources/experiences/exp-o-kd-20260519-2016-2.md) | Use int4 (128-bit = 8 bfloat16) vector loads via inline PTX asm with cache-strea | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2017-1](../sources/experiences/exp-o-kd-20260519-2017-1.md) | Assign one warp per (token, head) pair to eliminate per-element index decomposit | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2018-1](../sources/experiences/exp-o-kd-20260519-2018-1.md) | Replace 18 scalar bf16 load/store pairs with 3 vectorized PTX inline-asm operati | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2038-1](../sources/experiences/exp-o-kd-20260519-2038-1.md) | Add an lda parameter and compute separate input_row_stride (lda-based) and outpu | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2074-1](../sources/experiences/exp-o-kd-20260519-2074-1.md) | Replace batch-split 2D grid (1024 threads/CTA) with a per-token 1D grid (64 thre | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2075-1](../sources/experiences/exp-o-kd-20260519-2075-1.md) | Replace batch-split grid (1024 threads/CTA) with per-token grid (64 threads/CTA) | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2076-1](../sources/experiences/exp-o-kd-20260519-2076-1.md) | Convert ENTRY_SIZE and CTA_SIZE from runtime function parameters to compile-time | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2077-1](../sources/experiences/exp-o-kd-20260519-2077-1.md) | Convert entry_size and CTA_SIZE into compile-time template parameters (ENTRY_SIZ | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2078-1](../sources/experiences/exp-o-kd-20260519-2078-1.md) | Replace the sequential single-CTA block-level loop with a parallel per-token dir | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2079-1](../sources/experiences/exp-o-kd-20260519-2079-1.md) | Replace the serial single-CTA block-level loop with a parallel per-token direct  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2080-1](../sources/experiences/exp-o-kd-20260519-2080-1.md) | Replace the batch-split grid launch with a per-token launch grid(num_tokens) and | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2082-1](../sources/experiences/exp-o-kd-20260519-2082-1.md) | Replace the nested block-then-token iteration with direct per-token address comp | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2217-1](../sources/experiences/exp-o-kd-20260519-2217-1.md) | Move getMIndices computation before expandInputRowsKernelLauncher and pass the p | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2232-1](../sources/experiences/exp-o-kd-20260519-2232-1.md) | Consolidate both kv_c and k_pe copy phases into a single kernel launch using a d | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2233-1](../sources/experiences/exp-o-kd-20260519-2233-1.md) | Merge both copy kernels into a single templated kernel using a device-side lambd | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2254-1](../sources/experiences/exp-o-kd-20260519-2254-1.md) | Apply loop unrolling with factor 4 to process four elements per iteration, separ | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2255-1](../sources/experiences/exp-o-kd-20260519-2255-1.md) | Unroll the loop by a factor of 4 and separate read/write into two phases: first  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2263-1](../sources/experiences/exp-o-kd-20260519-2263-1.md) | Change k_scale and v_scale from scalar pass-by-value parameters to const float*  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2275-1](../sources/experiences/exp-o-kd-20260519-2275-1.md) | Recognize that NHD layout (head_stride == head_size) causes the multi-dimensiona | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2276-1](../sources/experiences/exp-o-kd-20260519-2276-1.md) | Pre-compute source and destination base pointers once per token to eliminate per | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2277-1](../sources/experiences/exp-o-kd-20260519-2277-1.md) | Replace the flat scalar loop with warp-per-head decomposition: each warp (32 thr | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2277-2](../sources/experiences/exp-o-kd-20260519-2277-2.md) | Use vectorize_with_alignment<VEC_SIZE=8> to perform 128-bit wide (8×half) memory | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2278-1](../sources/experiences/exp-o-kd-20260519-2278-1.md) | Decompose work so each warp owns one head (warp_id selects head, lane indexes wi | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2279-1](../sources/experiences/exp-o-kd-20260519-2279-1.md) | For NHD contiguous-heads layout, pre-compute base source/destination pointers on | optimization | sm90 | cuda-cpp |

## dequantization

| ID | Title | Type | Architectures | Languages |
|----|-------|------|--------------|-----------|
| [exp-a-kd-20260518-0003](../sources/experiences/exp-a-kd-20260518-0003.md) | Bit-level half construction for 4-bit dequant zero-point constants | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0004](../sources/experiences/exp-a-kd-20260518-0004.md) | Bit-level half construction for 4-bit dequant zero-point constants (zero=8 variant) | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0005](../sources/experiences/exp-a-kd-20260518-0005.md) | half2 broadcast intrinsic: __halves2half2 vs __half2half2 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0010](../sources/experiences/exp-a-kd-20260518-0010.md) | LOP3 ternary logic instruction for 4-bit dequant nibble unpacking | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0089](../sources/experiences/exp-a-kd-20260518-0089.md) | tile_offset_row_small | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0145](../sources/experiences/exp-a-kd-20260518-0145.md) | sm80_fp16_vs_sm89_fp8_mma_raw | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0146](../sources/experiences/exp-a-kd-20260518-0146.md) | kfactor8_int8 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0313](../sources/experiences/exp-a-kd-20260518-0313.md) | hist_i32_N1M | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0372](../sources/experiences/exp-a-kd-20260518-0372.md) | large_batch_bf16 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0382](../sources/experiences/exp-a-kd-20260518-0382.md) | moe_align_256exp_8k_tokens | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0384](../sources/experiences/exp-a-kd-20260518-0384.md) | fragment_reduction_256exp | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0387](../sources/experiences/exp-a-kd-20260518-0387.md) | fp16_128grp_128gs | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0388](../sources/experiences/exp-a-kd-20260518-0388.md) | fp16_256grp_64gs | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0389](../sources/experiences/exp-a-kd-20260518-0389.md) | fp16_128grp_128gs_vec | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0392](../sources/experiences/exp-a-kd-20260518-0392.md) | fp16_17grp_128gs_dyn | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0401](../sources/experiences/exp-a-kd-20260518-0401.md) | varied_8tok_1024d | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0402](../sources/experiences/exp-a-kd-20260518-0402.md) | varied_256tok_4096d | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0405](../sources/experiences/exp-a-kd-20260518-0405.md) | row_major_fp16_int8 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0427](../sources/experiences/exp-a-kd-20260518-0427.md) | moe_block_16_valid_scan | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0433](../sources/experiences/exp-a-kd-20260518-0433.md) | bf16_128h_8hd_256t | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0435](../sources/experiences/exp-a-kd-20260518-0435.md) | half_128h_8hd_256t | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0475](../sources/experiences/exp-a-kd-20260518-0475.md) | moe_6ep_288r_2048c | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0482](../sources/experiences/exp-a-kd-20260518-0482.md) | float_1M | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0497](../sources/experiences/exp-a-kd-20260518-0497.md) | vec_32k_256ep | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0498](../sources/experiences/exp-a-kd-20260518-0498.md) | vec_8k_256ep | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0503](../sources/experiences/exp-a-kd-20260518-0503.md) | quant_float_8192 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0504](../sources/experiences/exp-a-kd-20260518-0504.md) | quant_float_131072 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0505](../sources/experiences/exp-a-kd-20260518-0505.md) | quant_float_4M | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0506](../sources/experiences/exp-a-kd-20260518-0506.md) | half_hdim1024 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0507](../sources/experiences/exp-a-kd-20260518-0507.md) | half_hdim4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0509](../sources/experiences/exp-a-kd-20260518-0509.md) | small_half_hdim4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0560](../sources/experiences/exp-a-kd-20260518-0560.md) | float_gs128_ng4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0561](../sources/experiences/exp-a-kd-20260518-0561.md) | float_gs64_ng8192 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0583](../sources/experiences/exp-a-kd-20260518-0583.md) | elem_512b | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0584](../sources/experiences/exp-a-kd-20260518-0584.md) | elem_1024b | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0595](../sources/experiences/exp-a-kd-20260518-0595.md) | bf16_clamp_fmax | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0596](../sources/experiences/exp-a-kd-20260518-0596.md) | bf16_aligned_remainder | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0600](../sources/experiences/exp-a-kd-20260518-0600.md) | half_hidden_2048 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0602](../sources/experiences/exp-a-kd-20260518-0602.md) | mask_50pct_padding | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0626](../sources/experiences/exp-a-kd-20260518-0626.md) | fill_16k | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0627](../sources/experiences/exp-a-kd-20260518-0627.md) | fill_64k | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0629](../sources/experiences/exp-a-kd-20260518-0629.md) | half_128t_32h | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0632](../sources/experiences/exp-a-kd-20260518-0632.md) | nibble_extract_16K | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0633](../sources/experiences/exp-a-kd-20260518-0633.md) | dequant_arith_16K | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0650](../sources/experiences/exp-a-kd-20260518-0650.md) | bf16_topk4_hidden4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0651](../sources/experiences/exp-a-kd-20260518-0651.md) | bf16_topk8_hidden8192 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0666](../sources/experiences/exp-a-kd-20260518-0666.md) | bs256_draft32 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0676](../sources/experiences/exp-a-kd-20260518-0676.md) | naive_u4_dequant | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0677](../sources/experiences/exp-a-kd-20260518-0677.md) | prmt_u8_dequant | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0680](../sources/experiences/exp-a-kd-20260518-0680.md) | small_m8_k512 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0686](../sources/experiences/exp-a-kd-20260518-0686.md) | div_to_bitwise_mixed | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0687](../sources/experiences/exp-a-kd-20260518-0687.md) | stride_offset_mixed | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0699](../sources/experiences/exp-a-kd-20260518-0699.md) | per_tensor_h2048 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0700](../sources/experiences/exp-a-kd-20260518-0700.md) | per_channel_g32_h2048 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0701](../sources/experiences/exp-a-kd-20260518-0701.md) | per_channel_g128_h2048 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0704](../sources/experiences/exp-a-kd-20260518-0704.md) | interleaved_d4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0718](../sources/experiences/exp-a-kd-20260518-0718.md) | fp8_e4m3 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0735](../sources/experiences/exp-a-kd-20260518-0735.md) | fp8_quant_4k | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0739](../sources/experiences/exp-a-kd-20260518-0739.md) | bf16_128_vs_256 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0740](../sources/experiences/exp-a-kd-20260518-0740.md) | fp16_128_vs_256 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0743](../sources/experiences/exp-a-kd-20260518-0743.md) | scale_dequant_16k | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0744](../sources/experiences/exp-a-kd-20260518-0744.md) | scale_dequant_256k | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0745](../sources/experiences/exp-a-kd-20260518-0745.md) | convert_half2_256k | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0746](../sources/experiences/exp-a-kd-20260518-0746.md) | convert_half2_64k | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0747](../sources/experiences/exp-a-kd-20260518-0747.md) | moe_read_32 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0749](../sources/experiences/exp-a-kd-20260518-0749.md) | shm_8bit_m16_k128 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0756](../sources/experiences/exp-a-kd-20260518-0756.md) | fp8_e4m3_to_bf16 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0757](../sources/experiences/exp-a-kd-20260518-0757.md) | fp8_quant_group128 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0758](../sources/experiences/exp-a-kd-20260518-0758.md) | fp8_quant_group256 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0763](../sources/experiences/exp-a-kd-20260518-0763.md) | bfloat162_kU4B8 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0768](../sources/experiences/exp-a-kd-20260518-0768.md) | scale_load_every_iter | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0769](../sources/experiences/exp-a-kd-20260518-0769.md) | xor_full_row_128r | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0771](../sources/experiences/exp-a-kd-20260518-0771.md) | scale_sub_half | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0790](../sources/experiences/exp-a-kd-20260518-0790.md) | fp8_dequant_64tokens | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0791](../sources/experiences/exp-a-kd-20260518-0791.md) | batch_split_8reqs | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0797](../sources/experiences/exp-a-kd-20260518-0797.md) | fp8_per_token_quant_h2048 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0798](../sources/experiences/exp-a-kd-20260518-0798.md) | fp8_per_token_quant_h8192 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0805](../sources/experiences/exp-a-kd-20260518-0805.md) | fp8_vec_medium_128t_4096h | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0806](../sources/experiences/exp-a-kd-20260518-0806.md) | fp8_vec_large_512t_8192h | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0817](../sources/experiences/exp-a-kd-20260518-0817.md) | smem_overlap_balanced | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0818](../sources/experiences/exp-a-kd-20260518-0818.md) | scale_idx_group2 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0820](../sources/experiences/exp-a-kd-20260518-0820.md) | bias_async_pipeline | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0822](../sources/experiences/exp-a-kd-20260518-0822.md) | half_m512_k2048 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0830](../sources/experiences/exp-a-kd-20260518-0830.md) | float_uniform | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0831](../sources/experiences/exp-a-kd-20260518-0831.md) | per_tensor_scales | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0847](../sources/experiences/exp-a-kd-20260518-0847.md) | repack_4bit | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0849](../sources/experiences/exp-a-kd-20260518-0849.md) | zp_scalar_fp16 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0850](../sources/experiences/exp-a-kd-20260518-0850.md) | fp8_fusion_large | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0854](../sources/experiences/exp-a-kd-20260518-0854.md) | large_36mb | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0856](../sources/experiences/exp-a-kd-20260518-0856.md) | large_36mb | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0859](../sources/experiences/exp-a-kd-20260518-0859.md) | float_output | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0861](../sources/experiences/exp-a-kd-20260518-0861.md) | fused_vs_twostep_large_batch | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0862](../sources/experiences/exp-a-kd-20260518-0862.md) | fused_vs_twostep_small_batch | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0871](../sources/experiences/exp-a-kd-20260518-0871.md) | float_2048rows | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0884](../sources/experiences/exp-a-kd-20260518-0884.md) | fp16_128_4tok | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0889](../sources/experiences/exp-a-kd-20260518-0889.md) | aligned_1024 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0890](../sources/experiences/exp-a-kd-20260518-0890.md) | aligned_4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0891](../sources/experiences/exp-a-kd-20260518-0891.md) | unaligned_1021 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0931](../sources/experiences/exp-a-kd-20260518-0931.md) | small_contiguous | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0935](../sources/experiences/exp-a-kd-20260518-0935.md) | stream_128bit | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0949](../sources/experiences/exp-a-kd-20260518-0949.md) | mn4_k7168_gs128 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0955](../sources/experiences/exp-a-kd-20260518-0955.md) | sm_overlap_128threads | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0977](../sources/experiences/exp-a-kd-20260518-0977.md) | lop3_dequant | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0980](../sources/experiences/exp-a-kd-20260518-0980.md) | prmt_dequant | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0982](../sources/experiences/exp-a-kd-20260518-0982.md) | contiguous | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0984](../sources/experiences/exp-a-kd-20260518-0984.md) | stride_access | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1006](../sources/experiences/exp-a-kd-20260518-1006.md) | pack_factor_4bit_4bit | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1025](../sources/experiences/exp-a-kd-20260518-1025.md) | bf16_gs128_ng4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1036](../sources/experiences/exp-a-kd-20260518-1036.md) | fp16_gs128_131kgrp | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1110](../sources/experiences/exp-a-kd-20260518-1110.md) | scalar_bf16_dsv3_256ep | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1111](../sources/experiences/exp-a-kd-20260518-1111.md) | scalar_bf16_dsv3_4tok | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1136](../sources/experiences/exp-a-kd-20260518-1136.md) | bf16_key_load | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1137](../sources/experiences/exp-a-kd-20260518-1137.md) | fp16_key_load | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1138](../sources/experiences/exp-a-kd-20260518-1138.md) | kcache_fp16_load | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1140](../sources/experiences/exp-a-kd-20260518-1140.md) | vcache_fp16_load | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1141](../sources/experiences/exp-a-kd-20260518-1141.md) | vcache_fp16_long | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1142](../sources/experiences/exp-a-kd-20260518-1142.md) | fp16_32h_128d | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1146](../sources/experiences/exp-a-kd-20260518-1146.md) | half_output | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1177](../sources/experiences/exp-a-kd-20260518-1177.md) | lut_uint4_to_int8 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1178](../sources/experiences/exp-a-kd-20260518-1178.md) | fast_fp16_to_int8 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1179](../sources/experiences/exp-a-kd-20260518-1179.md) | fp8_dequant_equal_scale | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1180](../sources/experiences/exp-a-kd-20260518-1180.md) | fp8_dequant_diff_scale | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1181](../sources/experiences/exp-a-kd-20260518-1181.md) | same_scale_8h128d | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1182](../sources/experiences/exp-a-kd-20260518-1182.md) | diff_scale_8h128d | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1190](../sources/experiences/exp-a-kd-20260518-1190.md) | vec_bf162_H128_T128 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1191](../sources/experiences/exp-a-kd-20260518-1191.md) | kcache_deferred_fp8_head128 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1193](../sources/experiences/exp-a-kd-20260518-1193.md) | vcache_inline_fp8_head128 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1199](../sources/experiences/exp-a-kd-20260518-1199.md) | bf16_4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1200](../sources/experiences/exp-a-kd-20260518-1200.md) | f16_8192 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1201](../sources/experiences/exp-a-kd-20260518-1201.md) | packed_vec_half_128b | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1202](../sources/experiences/exp-a-kd-20260518-1202.md) | packed_vec_bf16_128b | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1203](../sources/experiences/exp-a-kd-20260518-1203.md) | ld128_half | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1204](../sources/experiences/exp-a-kd-20260518-1204.md) | ld128_bf16 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1205](../sources/experiences/exp-a-kd-20260518-1205.md) | pred_256b_load | analysis | sm100 | cuda-cpp |
| [exp-a-kd-20260518-1206](../sources/experiences/exp-a-kd-20260518-1206.md) | pred_128b_load | analysis | sm100 | cuda-cpp |
| [exp-a-kd-20260518-1207](../sources/experiences/exp-a-kd-20260518-1207.md) | vec_ld_st_32byte | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1218](../sources/experiences/exp-a-kd-20260518-1218.md) | scaled_fp8_classwrap | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1220](../sources/experiences/exp-a-kd-20260518-1220.md) | fp8x2_to_float2_scalar | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1223](../sources/experiences/exp-a-kd-20260518-1223.md) | float2_to_fp8x2_scalar | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1225](../sources/experiences/exp-a-kd-20260518-1225.md) | fp8_to_half | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1226](../sources/experiences/exp-a-kd-20260518-1226.md) | fp8x2_to_half2 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1227](../sources/experiences/exp-a-kd-20260518-1227.md) | scaled_fp8_to_float | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1232](../sources/experiences/exp-a-kd-20260518-1232.md) | float_hs8192_gs256 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1245](../sources/experiences/exp-a-kd-20260518-1245.md) | seq8k | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1262](../sources/experiences/exp-a-kd-20260518-1262.md) | pertoken_16384 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1263](../sources/experiences/exp-a-kd-20260518-1263.md) | pertoken_4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1283](../sources/experiences/exp-a-kd-20260518-1283.md) | float_h16384 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1285](../sources/experiences/exp-a-kd-20260518-1285.md) | azp_h16384 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1286](../sources/experiences/exp-a-kd-20260518-1286.md) | azp_h4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1287](../sources/experiences/exp-a-kd-20260518-1287.md) | dyn_h16384 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1289](../sources/experiences/exp-a-kd-20260518-1289.md) | dynazp_h16384 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1290](../sources/experiences/exp-a-kd-20260518-1290.md) | dynazp_h4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1312](../sources/experiences/exp-a-kd-20260518-1312.md) | awq_dequant_large | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1321](../sources/experiences/exp-a-kd-20260518-1321.md) | int8_aligned_gemm | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1323](../sources/experiences/exp-a-kd-20260518-1323.md) | int8_alignment | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1352](../sources/experiences/exp-a-kd-20260518-1352.md) | fp8_e4m3_fp16_kcache | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1353](../sources/experiences/exp-a-kd-20260518-1353.md) | fp8_e4m3_fp16_vcache | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1354](../sources/experiences/exp-a-kd-20260518-1354.md) | fp8_to_float_scaled | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1355](../sources/experiences/exp-a-kd-20260518-1355.md) | fp8_to_half_scaled | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1357](../sources/experiences/exp-a-kd-20260518-1357.md) | vec4_fp8_to_half | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1358](../sources/experiences/exp-a-kd-20260518-1358.md) | fp8_to_float | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1359](../sources/experiences/exp-a-kd-20260518-1359.md) | half_to_fp8 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1360](../sources/experiences/exp-a-kd-20260518-1360.md) | large_hidden | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1362](../sources/experiences/exp-a-kd-20260518-1362.md) | small_hidden | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1379](../sources/experiences/exp-a-kd-20260518-1379.md) | a8bit_int8_turing | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1380](../sources/experiences/exp-a-kd-20260518-1380.md) | pipeline_4stage | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1396](../sources/experiences/exp-a-kd-20260518-1396.md) | bf16_u4b8_dequant | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1398](../sources/experiences/exp-a-kd-20260518-1398.md) | fp8_scales_fp16 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1399](../sources/experiences/exp-a-kd-20260518-1399.md) | u4_zp_int | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1402](../sources/experiences/exp-a-kd-20260518-1402.md) | skip_scale_fetch | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1403](../sources/experiences/exp-a-kd-20260518-1403.md) | scale_bandwidth | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1406](../sources/experiences/exp-a-kd-20260518-1406.md) | scale_stride | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1407](../sources/experiences/exp-a-kd-20260518-1407.md) | frag_s_load | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1408](../sources/experiences/exp-a-kd-20260518-1408.md) | dequant_dispatch | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1409](../sources/experiences/exp-a-kd-20260518-1409.md) | dequant_skip_flop | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1410](../sources/experiences/exp-a-kd-20260518-1410.md) | float_large_32M | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1411](../sources/experiences/exp-a-kd-20260518-1411.md) | float_moderate_4M | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1412](../sources/experiences/exp-a-kd-20260518-1412.md) | float_to_fp8_scalar | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1413](../sources/experiences/exp-a-kd-20260518-1413.md) | float_to_fp8_vec4 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1414](../sources/experiences/exp-a-kd-20260518-1414.md) | float_to_fp8_compute_bound | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1427](../sources/experiences/exp-a-kd-20260518-1427.md) | fp8_scale_hidden256 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1428](../sources/experiences/exp-a-kd-20260518-1428.md) | fp8_scale_hidden4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1429](../sources/experiences/exp-a-kd-20260518-1429.md) | int8_h1024 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1430](../sources/experiences/exp-a-kd-20260518-1430.md) | int8_h4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1431](../sources/experiences/exp-a-kd-20260518-1431.md) | fp8_adjusted_qmax | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1432](../sources/experiences/exp-a-kd-20260518-1432.md) | int8_qmax | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1433](../sources/experiences/exp-a-kd-20260518-1433.md) | fp8_sf_param | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1434](../sources/experiences/exp-a-kd-20260518-1434.md) | int8_sf_param | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1435](../sources/experiences/exp-a-kd-20260518-1435.md) | fp8_dynamic_quant_large | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1436](../sources/experiences/exp-a-kd-20260518-1436.md) | fp8_dynamic_quant_small | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1437](../sources/experiences/exp-a-kd-20260518-1437.md) | half_h64_t16 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1438](../sources/experiences/exp-a-kd-20260518-1438.md) | half_h128_t16 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1439](../sources/experiences/exp-a-kd-20260518-1439.md) | half_h256_t16 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1441](../sources/experiences/exp-a-kd-20260518-1441.md) | loop_deref_scale | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1444](../sources/experiences/exp-a-kd-20260518-1444.md) | batch_32tokens_flash | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1445](../sources/experiences/exp-a-kd-20260518-1445.md) | single_token_flash | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1475](../sources/experiences/exp-a-kd-20260518-1475.md) | encode_large_64k | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1476](../sources/experiences/exp-a-kd-20260518-1476.md) | encode_small_4k | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1477](../sources/experiences/exp-a-kd-20260518-1477.md) | nibble_lut_16mb | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1478](../sources/experiences/exp-a-kd-20260518-1478.md) | nibble_lut_1mb | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1479](../sources/experiences/exp-a-kd-20260518-1479.md) | nibble_vec_16mb | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1480](../sources/experiences/exp-a-kd-20260518-1480.md) | nibble_vec_1mb | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1494](../sources/experiences/exp-a-kd-20260518-1494.md) | xor_smem_layout | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1495](../sources/experiences/exp-a-kd-20260518-1495.md) | iq1s_vecdot_256cols | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1496](../sources/experiences/exp-a-kd-20260518-1496.md) | shuffle_elision_16elts | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0009-1](../sources/experiences/exp-a-kd-20260519-0009-1.md) | Reorder the INT4 weight layout offline so that all 16 INT4 values per thread bec | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0797-1](../sources/experiences/exp-a-kd-20260519-0797-1.md) | Replace the exp2f/ceilf/log2f transcendental function chain with integer-only IE | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0812-1](../sources/experiences/exp-a-kd-20260519-0812-1.md) | Replace __shared__ float scale with const float scale, moving the variable into  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0813-1](../sources/experiences/exp-a-kd-20260519-0813-1.md) | Replace __shared__ float scale with const float scale computed directly from eac | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0814-1](../sources/experiences/exp-a-kd-20260519-0814-1.md) | Add a bool IS_COLUMN_MAJOR template parameter and use if constexpr to dispatch b | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0814-2](../sources/experiences/exp-a-kd-20260519-0814-2.md) | Remove the dead half-precision quantization loop entirely, keeping only the int8 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0895-1](../sources/experiences/exp-a-kd-20260519-0895-1.md) | Increase VEC_SIZE from 8 to 16 so that 16 FP8 output bytes exactly fill a uint4  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0916-1](../sources/experiences/exp-a-kd-20260519-0916-1.md) | Replace custom FP8_TYPE_WRAPPER software emulation with CUDA native __nv_fp8_e4m | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0967-1](../sources/experiences/exp-a-kd-20260519-0967-1.md) | Pad shared memory stride from 16 to 17 (s_absmax[16][17]) to prevent potential b | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0970-1](../sources/experiences/exp-a-kd-20260519-0970-1.md) | Coarsen the kernel by mapping 16 independent groups into a single block with 256 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0971-1](../sources/experiences/exp-a-kd-20260519-0971-1.md) | Replace the loop-based reduction with a WarpReduce helper that uses volatile sha | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1006-1](../sources/experiences/exp-a-kd-20260519-1006-1.md) | Replace fmax/fmin with fmaxf/fminf to use single-precision float math directly,  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1008-1](../sources/experiences/exp-a-kd-20260519-1008-1.md) | Doubling block size to 256 threads reduces per-thread iteration count from 4 to  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1013-1](../sources/experiences/exp-a-kd-20260519-1013-1.md) | Add a mask array parameter that specifies the number of valid rows per expert, a | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1043-1](../sources/experiences/exp-a-kd-20260519-1043-1.md) | Reduce explicit shifts from 3 to 1 by introducing TOP_MASK (0x00f000f0) to extra | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1044-1](../sources/experiences/exp-a-kd-20260519-1044-1.md) | Replace 8 explicit asm volatile PTX statements with a #pragma unroll for-loop ov | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1045-1](../sources/experiences/exp-a-kd-20260519-1045-1.md) | Decompose each packed half2 __hfma2 into two scalar FP32 fma operations: extract | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1046-1](../sources/experiences/exp-a-kd-20260519-1046-1.md) | Decompose each half2 multiply-add into individual FP32 fma operations to widen a | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1051-1](../sources/experiences/exp-a-kd-20260519-1051-1.md) | Stage input data to per-warp shared memory during pass-1 so pass-2 reads from sm | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1105-1](../sources/experiences/exp-a-kd-20260519-1105-1.md) | Decompose each half2 weight pair into individual FP32 values via __low2float/__h | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1106-1](../sources/experiences/exp-a-kd-20260519-1106-1.md) | Replace float-arithmetic constant construction with IEEE 754 bit-level manipulat | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1107-1](../sources/experiences/exp-a-kd-20260519-1107-1.md) | Replace float-arithmetic constant construction with IEEE 754 bit-level manipulat | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1108-1](../sources/experiences/exp-a-kd-20260519-1108-1.md) | Replace __halves2half2(x, x) with the dedicated __half2half2(x) broadcast intrin | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1113-1](../sources/experiences/exp-a-kd-20260519-1113-1.md) | Fuse AND+OR into a single LOP3 (LOgic Predicate 3-input) PTX instruction via lop | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1114-1](../sources/experiences/exp-a-kd-20260519-1114-1.md) | Replace the multi-instruction shift/mask/OR byte rearrangement with a single PRM | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1115-1](../sources/experiences/exp-a-kd-20260519-1115-1.md) | Broadcast the scalar zero-point to half2 width with __half2half2, then apply __h | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1122-1](../sources/experiences/exp-a-kd-20260519-1122-1.md) | Replace all division/modulo with bitwise shift/AND equivalents (>>7 for /128, &3 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1124-1](../sources/experiences/exp-a-kd-20260519-1124-1.md) | Replace div/mod index decomposition with bitwise shift/AND for power-of-two-alig | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1180-1](../sources/experiences/exp-a-kd-20260519-1180-1.md) | Replace half2 scales with __nv_fp8x2_e4m3 to halve scale memory footprint, conve | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1181-1](../sources/experiences/exp-a-kd-20260519-1181-1.md) | The after kernel replaces half2 scales with __nv_fp8x2_e4m3, cutting scale memor | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1193-1](../sources/experiences/exp-a-kd-20260519-1193-1.md) | Store KV cache as FP8 E4M3 (1 byte/element) and dequantize on-the-fly via softwa | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1199-1](../sources/experiences/exp-a-kd-20260519-1199-1.md) | Change dequant_kU4B8 from return-by-value (FragB struct) to output-pointer (half | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1200-1](../sources/experiences/exp-a-kd-20260519-1200-1.md) | Replace the return-by-value FragB pattern with an output-pointer parameter (nv_b | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1205-1](../sources/experiences/exp-a-kd-20260519-1205-1.md) | Add a conditional branch inside the hot loop to load from shared memory only at  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1208-1](../sources/experiences/exp-a-kd-20260519-1208-1.md) | Fuse scale multiplication and zero-point subtraction into a single __hfma instru | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1227-1](../sources/experiences/exp-a-kd-20260519-1227-1.md) | Replace 512-thread scalar kernel with 256-thread vectorized kernel using int4 lo | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1228-1](../sources/experiences/exp-a-kd-20260519-1228-1.md) | Replace 2D batch-split grid with a 1D flat warp-per-token model using binary sea | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1228-2](../sources/experiences/exp-a-kd-20260519-1228-2.md) | Replace scalar per-byte dequant with vectorized int4 loads where each lane loads | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1241-1](../sources/experiences/exp-a-kd-20260519-1241-1.md) | Add a per-invocation kv_scale multiplication (input[i] * kv_scale) before quanti | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1242-1](../sources/experiences/exp-a-kd-20260519-1242-1.md) | Replace the hardcoded typedef with a local using alias to a templated q8x4_t<FP8 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1252-1](../sources/experiences/exp-a-kd-20260519-1252-1.md) | Exploit the fact that E8M0 value 2^(e-127) maps directly to a BF16 with zero man | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1253-1](../sources/experiences/exp-a-kd-20260519-1253-1.md) | Replace 8 FP operations per element with 3 pure bitwise integer ops: mask odd by | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1255-1](../sources/experiences/exp-a-kd-20260519-1255-1.md) | Replace warp_row % 2 with (warp_row / group_blocks) % 2 so that adjacent warp ro | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1256-1](../sources/experiences/exp-a-kd-20260519-1256-1.md) | Split the FE2M1f scale fragment index computation into two branches: when group_ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1282-1](../sources/experiences/exp-a-kd-20260519-1282-1.md) | Introduce an undo_pack constexpr lookup table {0,4,1,5,2,6,3,7} to remap AWQ's i | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1283-1](../sources/experiences/exp-a-kd-20260519-1283-1.md) | Apply AWQ undo_pack deinterleaving table {0,2,1,3} to remap the sequential bit p | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1285-1](../sources/experiences/exp-a-kd-20260519-1285-1.md) | Replace the two-step load-then-extract pattern with one-step direct shared memor | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1286-1](../sources/experiences/exp-a-kd-20260519-1286-1.md) | Pack quantized value pairs into half2 and use __hsub2 for vectorized zero-point  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1292-1](../sources/experiences/exp-a-kd-20260519-1292-1.md) | Replace CPU host-side round-trip with a GPU kernel that uses a 256-byte constant | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1298-1](../sources/experiences/exp-a-kd-20260519-1298-1.md) | Fuse gather and dequantize into a single kernel (cp_gather_and_upconvert_fp8_kv_ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1299-1](../sources/experiences/exp-a-kd-20260519-1299-1.md) | Fuse gather and dequantize into a single kernel that reads FP8 data directly fro | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1330-1](../sources/experiences/exp-a-kd-20260519-1330-1.md) | Replace the per-byte FP32 conversion pipeline with a bit-manipulation technique: | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1331-1](../sources/experiences/exp-a-kd-20260519-1331-1.md) | Replace per-element software FP8→FP32→BF16 conversion with integer bit-manipulat | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1348-1](../sources/experiences/exp-a-kd-20260519-1348-1.md) | Replace cutlass::bfloat16_t scalar operator* with native nv_bfloat16 type and ex | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-1385-1](../sources/experiences/exp-a-kd-20260519-1385-1.md) | Replace atomicOr with a direct byte-level write via reinterpret_cast<uint8_t*>,  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1387-1](../sources/experiences/exp-a-kd-20260519-1387-1.md) | Replace atomicOr-based 32-bit packing with direct byte-addressed writes using re | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1387-2](../sources/experiences/exp-a-kd-20260519-1387-2.md) | Expand the kernel grid to cover TMA-aligned padding groups (num_groups_padded) s | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1388-1](../sources/experiences/exp-a-kd-20260519-1388-1.md) | Fuse zero-initialization into the kernel by expanding the grid to cover all padd | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1393-1](../sources/experiences/exp-a-kd-20260519-1393-1.md) | Always load scales into shared memory on every pipeline iteration (guarded only  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1394-1](../sources/experiences/exp-a-kd-20260519-1394-1.md) | Replace the group-aligned offset formula with direct pipe indexing (S_SH_STAGE * | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1414-1](../sources/experiences/exp-a-kd-20260519-1414-1.md) | Replace the entire shift/mask/sign-extend/float-convert pipeline with lop3.b32 i | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1416-1](../sources/experiences/exp-a-kd-20260519-1416-1.md) | Replace separate (q & LO) | EX with an explicit inline PTX lop3.b32 instruction  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1417-1](../sources/experiences/exp-a-kd-20260519-1417-1.md) | Replace the multi-instruction shift-mask-or byte extraction and manual fp16 bias | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1440-1](../sources/experiences/exp-a-kd-20260519-1440-1.md) | Convert the runtime has_act_order flag into a compile-time template parameter HA | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1443-1](../sources/experiences/exp-a-kd-20260519-1443-1.md) | Replace hardcoded pack_factor_4bit=8 with a template parameter num_bits and deri | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1444-1](../sources/experiences/exp-a-kd-20260519-1444-1.md) | Generalize the kernel with a template parameter num_bits, deriving all bit-width | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1445-1](../sources/experiences/exp-a-kd-20260519-1445-1.md) | Replace hardcoded bit-width constants with a compile-time template parameter num | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1446-1](../sources/experiences/exp-a-kd-20260519-1446-1.md) | Replace hardcoded constants with a compile-time template parameter num_bits, der | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1447-1](../sources/experiences/exp-a-kd-20260519-1447-1.md) | Replace hardcoded loads and split loops with a templated approach using constexp | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1475-1](../sources/experiences/exp-a-kd-20260519-1475-1.md) | Replace shared memory ping-pong reduction with warp-level __shfl_xor_sync butter | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1516-1](../sources/experiences/exp-a-kd-20260519-1516-1.md) | Precompute fp8_inv = __hdiv(1.0, fp8_max) once outside the per-group loop, then  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1516-2](../sources/experiences/exp-a-kd-20260519-1516-2.md) | Use native bfloat16 __hdiv(one_bf16, y_s) to compute the inverse entirely within | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1523-1](../sources/experiences/exp-a-kd-20260519-1523-1.md) | Replace bare WARP_SIZE with a project-specific WARP_SIZE_GGUF constant hard-code | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1535-1](../sources/experiences/exp-a-kd-20260519-1535-1.md) | Replace the scalar loop with 4 lop3.b32 PTX instructions that extract two int4 p | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1536-1](../sources/experiences/exp-a-kd-20260519-1536-1.md) | Lower the preprocessor guard threshold from __CUDA_ARCH__ < 800 to __CUDA_ARCH__ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1563-1](../sources/experiences/exp-a-kd-20260519-1563-1.md) | Add a conjunction bounds check ib0 + ir * BPW / QR < bpr to the #pragma unroll l | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1580-1](../sources/experiences/exp-a-kd-20260519-1580-1.md) | Wrap each half-precision dequant result with convert_from_half<dst_t>() before s | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1581-1](../sources/experiences/exp-a-kd-20260519-1581-1.md) | The convert_from_half<half> specialization simply returns its input unchanged, a | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1582-1](../sources/experiences/exp-a-kd-20260519-1582-1.md) | Remove __float2half() so the float computation result is assigned directly to ds | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1583-1](../sources/experiences/exp-a-kd-20260519-1583-1.md) | Remove the explicit __float2half() call and rely on CUDA's implicit float-to-hal | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1584-1](../sources/experiences/exp-a-kd-20260519-1584-1.md) | Fuse the half-to-bf16 conversion directly into the dequantize kernel's store poi | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1585-1](../sources/experiences/exp-a-kd-20260519-1585-1.md) | Introduce a templatized convert_from_half<dst_t> helper with an identity special | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1586-1](../sources/experiences/exp-a-kd-20260519-1586-1.md) | Template the kernel on dst_t and introduce convert_from_half<dst_t> — an identit | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1611-1](../sources/experiences/exp-a-kd-20260519-1611-1.md) | Switch to sequential (non-interleaved) packing where each byte holds two consecu | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1612-1](../sources/experiences/exp-a-kd-20260519-1612-1.md) | Switch to sequential (non-interleaved) packing where nibbles are stored in natur | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1614-1](../sources/experiences/exp-a-kd-20260519-1614-1.md) | Replace the per-nibble shift/mask/subtract loop with a 16-entry compile-time LUT | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1616-1](../sources/experiences/exp-a-kd-20260519-1616-1.md) | Split the shared kv_scale parameter into separate k_scale and v_scale, allowing  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1617-1](../sources/experiences/exp-a-kd-20260519-1617-1.md) | Split the shared kv_scale parameter into separate k_scale and v_scale per-tensor | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1618-1](../sources/experiences/exp-a-kd-20260519-1618-1.md) | Split the shared kv_scale parameter into separate k_scale and v_scale arguments, | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1619-1](../sources/experiences/exp-a-kd-20260519-1619-1.md) | Replace the single shared kv_scale with separate k_scale and v_scale, each tuned | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1628-1](../sources/experiences/exp-a-kd-20260519-1628-1.md) | Split the single load+convert loop into two phases: Phase 1 loads all raw fp8 by | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1629-1](../sources/experiences/exp-a-kd-20260519-1629-1.md) | Split the fused load+convert loop into two separate phases: Phase 1 loads all ra | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1630-1](../sources/experiences/exp-a-kd-20260519-1630-1.md) | Replace the two-phase deferred pattern with inline conversion: load each fp8 chu | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1631-1](../sources/experiences/exp-a-kd-20260519-1631-1.md) | Fuse fp8 load and dequant into a single triple-nested loop using a stack-local f | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1637-1](../sources/experiences/exp-a-kd-20260519-1637-1.md) | Replace the hardcoded FP8_E4M3_MAX macro with a type-dependent fp8_e4m3_adjusted | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1657-1](../sources/experiences/exp-a-kd-20260519-1657-1.md) | Replace the entire manual scalar-decomposition pipeline (two calls to fp8_e4m3_t | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1661-1](../sources/experiences/exp-a-kd-20260519-1661-1.md) | Replace manual scalar float_to_fp8_manual conversion with the vendor __nv_fp8x2_ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1663-1](../sources/experiences/exp-a-kd-20260519-1663-1.md) | Replace the two-call scalar decomposition with __nv_cvt_fp8x2_to_halfraw2, a sin | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1667-1](../sources/experiences/exp-a-kd-20260519-1667-1.md) | Replace the single CUB BlockReduce with groupwise shared-memory partitioning: di | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1683-1](../sources/experiences/exp-a-kd-20260519-1683-1.md) | Replace num_ints_per_thread scalar 4-byte loads with a single 16-byte int4 vecto | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1684-1](../sources/experiences/exp-a-kd-20260519-1684-1.md) | Replace the integer zero-point path with a float16 zero-point path where ZP valu | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1699-1](../sources/experiences/exp-a-kd-20260519-1699-1.md) | Fuse absmax reduction and quantization into a single per-token kernel (one block | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1699-2](../sources/experiences/exp-a-kd-20260519-1699-2.md) | Use vec4_t_f (16-byte aligned struct of 4 floats) to load and process four eleme | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1699-3](../sources/experiences/exp-a-kd-20260519-1699-3.md) | Replace the shared-memory tree reduction with warp shuffle reduction (__shfl_xor | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1700-1](../sources/experiences/exp-a-kd-20260519-1700-1.md) | Fuse absmax reduction and quantization into a single per-token kernel where each | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1700-2](../sources/experiences/exp-a-kd-20260519-1700-2.md) | Use float4 (vec4_t_f) vectorized loads to process 4 elements per memory transact | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1724-1](../sources/experiences/exp-a-kd-20260519-1724-1.md) | Replace ternary-operator absmax with fabsf/fmaxf intrinsics which compile to sin | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1724-2](../sources/experiences/exp-a-kd-20260519-1724-2.md) | Reduce block size from 1024 to 256 threads (BlockReduce<256>) to lower shared me | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1724-3](../sources/experiences/exp-a-kd-20260519-1724-3.md) | Use vectorize_with_alignment<16> to process 16 float elements (64 bytes) per vec | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1727-1](../sources/experiences/exp-a-kd-20260519-1727-1.md) | Merge the two separate BlockReduce passes into a single pass using a custom MinM | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1727-2](../sources/experiences/exp-a-kd-20260519-1727-2.md) | Replace the scalar quantization loop with vectorize_with_alignment<16> which pro | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1748-1](../sources/experiences/exp-a-kd-20260519-1748-1.md) | Replace the scalar __hsub/__hmul loop with explicit inline PTX sub.f16x2 and fma | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1749-1](../sources/experiences/exp-a-kd-20260519-1749-1.md) | Replace the scalar __hsub/__hmul loop with explicit inline PTX sub.f16x2 and fma | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1789-1](../sources/experiences/exp-a-kd-20260519-1789-1.md) | Replace preprocessor-guarded fp8_e4m3::scaled_vec_conversion with a unified fp8  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1790-1](../sources/experiences/exp-a-kd-20260519-1790-1.md) | Replace format-specific namespace (fp8_e4m3) with a unified fp8 namespace using  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1791-1](../sources/experiences/exp-a-kd-20260519-1791-1.md) | Fuse the three-step conversion into a compact single-expression helper (scaled_v | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1792-1](../sources/experiences/exp-a-kd-20260519-1792-1.md) | Fuse the fp8→half dequantization and scale multiplication into a single scaled_v | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1793-1](../sources/experiences/exp-a-kd-20260519-1793-1.md) | Fuse the unscaled fp8→half conversion and the scale multiply into a single kerne | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1794-1](../sources/experiences/exp-a-kd-20260519-1794-1.md) | Fuse the unscaled fp8x4-to-half2x2 conversion and the element-wise scale into a  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1833-1](../sources/experiences/exp-a-kd-20260519-1833-1.md) | Split the single-step __hfma2 into a two-step pattern: skip_flop=true stores raw | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1834-1](../sources/experiences/exp-a-kd-20260519-1834-1.md) | Split the monolithic dequant into two functions: skip_flop_true performs only bi | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1835-1](../sources/experiences/exp-a-kd-20260519-1835-1.md) | Exploit the 1-bit exponent difference between FP8 E4M3 and FP16: a single combin | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1836-1](../sources/experiences/exp-a-kd-20260519-1836-1.md) | Algebraically fold the bias subtraction into the zero-point term: skip bias subt | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1838-1](../sources/experiences/exp-a-kd-20260519-1838-1.md) | Fix the comparison operator from < to > so the clamp correctly caps sh_num_group | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1839-1](../sources/experiences/exp-a-kd-20260519-1839-1.md) | Skip fetch_col_scale_to_shared at pipeline start when dequant_skip_flop is true, | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1840-1](../sources/experiences/exp-a-kd-20260519-1840-1.md) | Replace the 2-byte half scale load with a 1-byte ScaleFP8 load followed by a con | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1843-1](../sources/experiences/exp-a-kd-20260519-1843-1.md) | Replace hardcoded weight-type check (b_type == kFE2M1f) with a semantic property | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1844-1](../sources/experiences/exp-a-kd-20260519-1844-1.md) | Replace the weight-type-specific branch condition (is_fe2m1f) with a scale-prope | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1845-1](../sources/experiences/exp-a-kd-20260519-1845-1.md) | Change the compile-time dispatch guard from weight type (b_type == kFE2M1f) to s | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1846-1](../sources/experiences/exp-a-kd-20260519-1846-1.md) | Refine dequant_skip_flop to exclude MXFP8 by adding && !(s_type == kFE8M0fnu) to | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1850-1](../sources/experiences/exp-a-kd-20260519-1850-1.md) | Replace 25-line software float_to_fp8_e4m3_sw emulation with single-call __nv_cv | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2306-1](../sources/experiences/exp-a-kd-20260519-2306-1.md) | Replace the hardcoded 240.0f magic constant with a type-trait specialization (qu | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2310-1](../sources/experiences/exp-a-kd-20260519-2310-1.md) | Replace the runtime min_scaling_factor kernel parameter with a template struct ( | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2315-1](../sources/experiences/exp-a-kd-20260519-2315-1.md) | Pass k_scale and v_scale as const float* pointers instead of scalar-by-value, de | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2316-1](../sources/experiences/exp-a-kd-20260519-2316-1.md) | Change k_scale/v_scale from scalar by-value float parameters to const float* poi | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2360-1](../sources/experiences/exp-a-kd-20260519-2360-1.md) | Eliminate the separate transpose kernel by directly indexing the original scale  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2368-1](../sources/experiences/exp-a-kd-20260519-2368-1.md) | Replace the separate AND+OR pattern with PTX lop3.b32 inline assembly using a co | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2370-1](../sources/experiences/exp-a-kd-20260519-2370-1.md) | Consolidate four separate dp4a accumulators into a single accumulator to reduce  | analysis | sm90 | cuda-cpp |
| [exp-i-kd-20260518-0034](../sources/experiences/exp-i-kd-20260518-0034.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0039](../sources/experiences/exp-i-kd-20260518-0039.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0040](../sources/experiences/exp-i-kd-20260518-0040.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0044](../sources/experiences/exp-i-kd-20260518-0044.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0068](../sources/experiences/exp-i-kd-20260518-0068.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260518-0004](../sources/experiences/exp-o-kd-20260518-0004.md) | smem_scatter | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0188](../sources/experiences/exp-o-kd-20260518-0188.md) | moe_block_32_valid_scan | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0192](../sources/experiences/exp-o-kd-20260518-0192.md) | float_128h_8hd_256t | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0209](../sources/experiences/exp-o-kd-20260518-0209.md) | binary_search_shared_mem | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0224](../sources/experiences/exp-o-kd-20260518-0224.md) | fp16_hd4096 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0225](../sources/experiences/exp-o-kd-20260518-0225.md) | fp16_hd8192 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0260](../sources/experiences/exp-o-kd-20260518-0260.md) | float_gs64_ng4096 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0263](../sources/experiences/exp-o-kd-20260518-0263.md) | dtn8_bs32 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0274](../sources/experiences/exp-o-kd-20260518-0274.md) | bf16_h4096_t128 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0275](../sources/experiences/exp-o-kd-20260518-0275.md) | fp16_h4096_t128 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0278](../sources/experiences/exp-o-kd-20260518-0278.md) | half_8epg_1024r_256c | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0289](../sources/experiences/exp-o-kd-20260518-0289.md) | vec_fill_N8192 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0304](../sources/experiences/exp-o-kd-20260518-0304.md) | bs256_draft8 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0307](../sources/experiences/exp-o-kd-20260518-0307.md) | dequant_zero15 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0308](../sources/experiences/exp-o-kd-20260518-0308.md) | dequant_zero8 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0319](../sources/experiences/exp-o-kd-20260518-0319.md) | fp16_d4096 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0333](../sources/experiences/exp-o-kd-20260518-0333.md) | bf16_scalar_vs_packed | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0334](../sources/experiences/exp-o-kd-20260518-0334.md) | fp16_scalar_vs_packed | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0358](../sources/experiences/exp-o-kd-20260518-0358.md) | int8_loop_1M | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0359](../sources/experiences/exp-o-kd-20260518-0359.md) | int8_quant_runtime_if | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0361](../sources/experiences/exp-o-kd-20260518-0361.md) | fp8_fusion_256 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0380](../sources/experiences/exp-o-kd-20260518-0380.md) | repack_8bit | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0382](../sources/experiences/exp-o-kd-20260518-0382.md) | fp8_fusion_small | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0383](../sources/experiences/exp-o-kd-20260518-0383.md) | scale_div_large | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0387](../sources/experiences/exp-o-kd-20260518-0387.md) | medium_16kb | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0393](../sources/experiences/exp-o-kd-20260518-0393.md) | half_4096rows | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0394](../sources/experiences/exp-o-kd-20260518-0394.md) | float_topk8 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0395](../sources/experiences/exp-o-kd-20260518-0395.md) | half_topk8 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0401](../sources/experiences/exp-o-kd-20260518-0401.md) | fp16_4096_64tok | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0402](../sources/experiences/exp-o-kd-20260518-0402.md) | ds_mla_full | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0403](../sources/experiences/exp-o-kd-20260518-0403.md) | fp8_to_fp16_bulk | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0404](../sources/experiences/exp-o-kd-20260518-0404.md) | fp8_to_bf16_bulk | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0423](../sources/experiences/exp-o-kd-20260518-0423.md) | large_contiguous | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0433](../sources/experiences/exp-o-kd-20260518-0433.md) | mn128_k7168_gs128 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0442](../sources/experiences/exp-o-kd-20260518-0442.md) | noncontiguous | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0501](../sources/experiences/exp-o-kd-20260518-0501.md) | kcache_fp16_long | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0503](../sources/experiences/exp-o-kd-20260518-0503.md) | bf16_fused_write | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0516](../sources/experiences/exp-o-kd-20260518-0516.md) | vec_bf162_H128_T32 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0524](../sources/experiences/exp-o-kd-20260518-0524.md) | fp8_to_float_custom | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0526](../sources/experiences/exp-o-kd-20260518-0526.md) | fp8x2_to_half2_conditional | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0533](../sources/experiences/exp-o-kd-20260518-0533.md) | zp_scalar_vs_vec | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0534](../sources/experiences/exp-o-kd-20260518-0534.md) | zp_dequant_sub | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0562](../sources/experiences/exp-o-kd-20260518-0562.md) | sm_broadcast_gs128 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0570](../sources/experiences/exp-o-kd-20260518-0570.md) | scalar_fp8_to_half | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0575](../sources/experiences/exp-o-kd-20260518-0575.md) | medium_hidden | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0581](../sources/experiences/exp-o-kd-20260518-0581.md) | stages_int8_turing_4stages | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0582](../sources/experiences/exp-o-kd-20260518-0582.md) | a8bit_int8_ampere | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0598](../sources/experiences/exp-o-kd-20260518-0598.md) | batch_32tokens_static | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0646](../sources/experiences/exp-o-kd-20260518-0646.md) | Atom configurations). Under such configurations, the hardcoded check would rejec | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0653](../sources/experiences/exp-o-kd-20260518-0653.md) | Itten again by applyPrequantScale. | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260518-0654](../sources/experiences/exp-o-kd-20260518-0654.md) | Ed change: The patch extended doGatedActivationKernel and doGatedActivation with | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0698](../sources/experiences/exp-o-kd-20260518-0698.md) | Y_s, 1e-10f)))) requires computing log2, ceiling it, and then computing 2^result | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0702](../sources/experiences/exp-o-kd-20260518-0702.md) | And a sequential dependency chain that prevented parallel counting. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0708](../sources/experiences/exp-o-kd-20260518-0708.md) | Vision requires multiple instruction cycles. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0716](../sources/experiences/exp-o-kd-20260518-0716.md) | Offset arrays, search loop iterations, and potential shared memory bank conflict | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0717](../sources/experiences/exp-o-kd-20260518-0717.md) | Ized load + warp-shuffle reduction pattern from being reused for int8. | optimization | sm90 | triton |
| [exp-o-kd-20260518-0723](../sources/experiences/exp-o-kd-20260518-0723.md) | Memory traffic pressure since each load fetches only 4 bytes from potentially un | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0730](../sources/experiences/exp-o-kd-20260518-0730.md) | The optimization is most effective for small tensors where the overhead fraction | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0742](../sources/experiences/exp-o-kd-20260518-0742.md) | The optimization is most impactful when the per-token data footprint is large en | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0743](../sources/experiences/exp-o-kd-20260518-0743.md) | Zation kernel would read that intermediate tensor and convert it to FP4 format.  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0747](../sources/experiences/exp-o-kd-20260518-0747.md) | Erates more DRAM requests than necessary for a contiguous fill pattern. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0749](../sources/experiences/exp-o-kd-20260518-0749.md) | Rdware still fetches a full 128-bit cache line but only uses 16 bits of it. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0751](../sources/experiences/exp-o-kd-20260518-0751.md) | Er than integer bit manipulation and also prevented the kernel from supporting v | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0753](../sources/experiences/exp-o-kd-20260518-0753.md) | Small-batch quantization workloads. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0756](../sources/experiences/exp-o-kd-20260518-0756.md) | Ndent and the loop stride is blockDim.x, not 1. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0757](../sources/experiences/exp-o-kd-20260518-0757.md) | Only one useful element while the adjacent element in the same cache line is als | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0762](../sources/experiences/exp-o-kd-20260518-0762.md) | Launch overhead and data traversal cost for every quantization call. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0766](../sources/experiences/exp-o-kd-20260518-0766.md) | Division is executed for every row in every pipeline stage of every slice, creat | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0768](../sources/experiences/exp-o-kd-20260518-0768.md) | N share or reorganize their layout to use only tb_m*4 bytes. This over-counting  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0769](../sources/experiences/exp-o-kd-20260518-0769.md) | Rom fitting in shared memory for small-batch configurations and limiting SM occu | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0775](../sources/experiences/exp-o-kd-20260518-0775.md) | S tid < 576 for RoPE copy). Short requests generated inactive splits that return | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0780](../sources/experiences/exp-o-kd-20260518-0780.md) | By quantization), which is wasteful since the intermediate data is consumed imme | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0781](../sources/experiences/exp-o-kd-20260518-0781.md) | . This two-kernel approach incurs an extra kernel launch overhead and an extra r | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0782](../sources/experiences/exp-o-kd-20260518-0782.md) | CudaMemcpy HostToDevice). This host-side round-trip incurs two synchronous PCIe  | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260518-0783](../sources/experiences/exp-o-kd-20260518-0783.md) | The optimization reduces thread count from 576 to 96, which reduces scheduling o | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0793](../sources/experiences/exp-o-kd-20260518-0793.md) | Dditional DRAM write pass, and prevents overlap with computation. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0811](../sources/experiences/exp-o-kd-20260518-0811.md) | Ncluding within a warp where shuffle instructions would be faster. Additionally, | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0816](../sources/experiences/exp-o-kd-20260518-0816.md) | Optimization focus: Lower the CUDA arch guard in dequantize_s4_to_fp16x2 from __ | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0831](../sources/experiences/exp-o-kd-20260518-0831.md) | Capability for bfloat16 operations. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0834](../sources/experiences/exp-o-kd-20260518-0834.md) | Er and prevents instruction scheduling optimizations across the conversion bound | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0835](../sources/experiences/exp-o-kd-20260518-0835.md) | Ts to float then re-packed into half2. Without that flag, it decomposed fp8x2 in | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0837](../sources/experiences/exp-o-kd-20260518-0837.md) | B fragments before subtraction. This multi-step process involves N individual sh | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0842](../sources/experiences/exp-o-kd-20260518-0842.md) | Red two full reduction traversals over shared memory and an explicit barrier bet | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0848](../sources/experiences/exp-o-kd-20260518-0848.md) | Applied change: Removed the StreamK/Persistent heuristic and hardcoded a single  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0851](../sources/experiences/exp-o-kd-20260518-0851.md) | Rnel launch overhead. Without fused scaling, the intermediate half values could  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0853](../sources/experiences/exp-o-kd-20260518-0853.md) | Ing a separate pre-scaling pass that added memory traffic and kernel launch over | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0854](../sources/experiences/exp-o-kd-20260518-0854.md) | At value, then the kernel launch re-sends that scalar to the device via kernel a | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0855](../sources/experiences/exp-o-kd-20260518-0855.md) | Ge: Replace the compile-time pipe_stages=4 constant with a runtime stages parame | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0856](../sources/experiences/exp-o-kd-20260518-0856.md) | INT8 thread configs to fit within shared memory limits, especially on constraine | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0868](../sources/experiences/exp-o-kd-20260518-0868.md) | E num_heads*head_size region is contiguous in both source and destination memory | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0869](../sources/experiences/exp-o-kd-20260518-0869.md) | Loop treated this strided access pattern the same as the contiguous one, missing | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0613-1](../sources/experiences/exp-o-kd-20260519-0613-1.md) | Replace all four expensive FP math calls with IEEE 754 bit-level manipulation: f | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0614-1](../sources/experiences/exp-o-kd-20260519-0614-1.md) | Replace exp2f(x) with fast_pow2 that constructs IEEE 754 float via integer bit-s | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0677-1](../sources/experiences/exp-o-kd-20260519-0677-1.md) | Replace per-element expert search with upfront round-robin thread-to-expert assi | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0721-1](../sources/experiences/exp-o-kd-20260519-0721-1.md) | Move the reciprocal division to the host side and pass scale_val as a scalar ker | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0722-1](../sources/experiences/exp-o-kd-20260519-0722-1.md) | Pass scale_val as a scalar kernel argument by value instead of a global memory p | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1859-1](../sources/experiences/exp-o-kd-20260519-1859-1.md) | Replace float-arithmetic constant construction with IEEE 754 bit-level manipulat | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1860-1](../sources/experiences/exp-o-kd-20260519-1860-1.md) | Replace float-arithmetic constant construction with IEEE 754 bit-level manipulat | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1861-1](../sources/experiences/exp-o-kd-20260519-1861-1.md) | Replace hardcoded float-arithmetic zero-point construction with runtime-paramete | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1866-1](../sources/experiences/exp-o-kd-20260519-1866-1.md) | Round m up to the next multiple of 128 via computeEffectiveRows(m) before comput | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1896-1](../sources/experiences/exp-o-kd-20260519-1896-1.md) | Split into static_scaled_fp8_quant which skips segmented_max_reduction and direc | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1929-1](../sources/experiences/exp-o-kd-20260519-1929-1.md) | Replace 2D batch-split grid with 1D flat warp-per-token model where each warp pr | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1929-2](../sources/experiences/exp-o-kd-20260519-1929-2.md) | Replace scalar loads with vectorized int4 loads where each of 32 lanes loads 16  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1943-1](../sources/experiences/exp-o-kd-20260519-1943-1.md) | Replace all eight FP function calls per int32 element with three pure bitwise in | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1969-1](../sources/experiences/exp-o-kd-20260519-1969-1.md) | Replace the host-device round-trip with a single GPU kernel launch that processe | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1969-2](../sources/experiences/exp-o-kd-20260519-1969-2.md) | Replace per-byte conditional nibble remapping with a 256-entry constant-memory l | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1971-1](../sources/experiences/exp-o-kd-20260519-1971-1.md) | Replace the CPU round-trip with a GPU kernel (unified_encode_int4b_device) that  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1972-1](../sources/experiences/exp-o-kd-20260519-1972-1.md) | Fuse gather and FP8-to-BF16 dequantization into a single kernel where each threa | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1973-1](../sources/experiences/exp-o-kd-20260519-1973-1.md) | Fuse the paged gather and FP8→BF16 dequantize into a single kernel that reads FP | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1988-1](../sources/experiences/exp-o-kd-20260519-1988-1.md) | Replace the per-byte FP32 conversion pipeline with a unified bit-manipulation pa | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1989-1](../sources/experiences/exp-o-kd-20260519-1989-1.md) | Replace per-byte FP8→FP32→BF16 arithmetic conversion with integer bit manipulati | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2027-1](../sources/experiences/exp-o-kd-20260519-2027-1.md) | Replace atomicOr with direct byte-level writes via reinterpret_cast<uint8_t*> to | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2027-2](../sources/experiences/exp-o-kd-20260519-2027-2.md) | Expand the kernel grid to cover all TMA-aligned padding groups (num_groups_padde | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2029-1](../sources/experiences/exp-o-kd-20260519-2029-1.md) | Remove the host-side torch::stable::zero_() call entirely and expand the kernel  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2053-1](../sources/experiences/exp-o-kd-20260519-2053-1.md) | Convert has_act_order from a runtime flag to a compile-time template parameter H | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2054-1](../sources/experiences/exp-o-kd-20260519-2054-1.md) | Add a compile-time constexpr early return at the top of init_same_group that che | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2088-1](../sources/experiences/exp-o-kd-20260519-2088-1.md) | Replace the scalar byte-decomposition loop with the __dp4a intrinsic which perfo | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2101-1](../sources/experiences/exp-o-kd-20260519-2101-1.md) | Replace the scalar loop with lop3.b32 PTX instructions to extract two pairs of 4 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2102-1](../sources/experiences/exp-o-kd-20260519-2102-1.md) | Lower the preprocessor arch guard from __CUDA_ARCH__ < 800 to __CUDA_ARCH__ < 75 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2130-1](../sources/experiences/exp-o-kd-20260519-2130-1.md) | Fuse the half-to-bfloat16 conversion into the dequantize kernel by introducing a | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2159-1](../sources/experiences/exp-o-kd-20260519-2159-1.md) | Replace the manual bit-manipulation FP8 conversion with the vendor-provided __nv | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2161-1](../sources/experiences/exp-o-kd-20260519-2161-1.md) | Replace the manual scalar-decomposition path (two calls to fp8_e4m3_to_float_man | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2163-1](../sources/experiences/exp-o-kd-20260519-2163-1.md) | Replace the MI300-conditional dual-path code with a unified fp8x2_type cast that | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2171-1](../sources/experiences/exp-o-kd-20260519-2171-1.md) | Consolidate the inner loop's multiple scalar 4-byte loads into a single 16-byte  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2172-1](../sources/experiences/exp-o-kd-20260519-2172-1.md) | Replace the integer zero-point path with a direct fp16 zero-point path where ZP  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2182-1](../sources/experiences/exp-o-kd-20260519-2182-1.md) | Fuse absmax reduction and quantization into a single kernel with one block per t | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2182-2](../sources/experiences/exp-o-kd-20260519-2182-2.md) | Replace the shared-memory reduction tree with a two-phase blockReduceMax: first  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2182-3](../sources/experiences/exp-o-kd-20260519-2182-3.md) | Use vec4_t_f (4-wide aligned float struct) to load and process 4 input elements  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2222-1](../sources/experiences/exp-o-kd-20260519-2222-1.md) | Fuse the unscaled fp8→half conversion and the scale multiply into a single kerne | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2223-1](../sources/experiences/exp-o-kd-20260519-2223-1.md) | Fuse the fp8-to-half conversion and scale multiply into a single device function | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2226-1](../sources/experiences/exp-o-kd-20260519-2226-1.md) | Replace unscaled vec_conversion with scaled_vec_conversion that fuses scale mult | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2227-1](../sources/experiences/exp-o-kd-20260519-2227-1.md) | Fuse the per-element scale multiplication directly into the fp8-to-float convers | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2228-1](../sources/experiences/exp-o-kd-20260519-2228-1.md) | Fuses the quantization scale division into the half-to-fp8 conversion by dividin | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2260-1](../sources/experiences/exp-o-kd-20260519-2260-1.md) | Pass k_scale/v_scale as const float* pointers and dereference once into local re | optimization | sm90 | cuda-cpp |

## elementwise

| ID | Title | Type | Architectures | Languages |
|----|-------|------|--------------|-----------|
| [exp-a-kd-20260518-0006](../sources/experiences/exp-a-kd-20260518-0006.md) | Vector pack materialization before VecOp: vec16 case regression | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0007](../sources/experiences/exp-a-kd-20260518-0007.md) | Vector pack materialization before VecOp: vec4 case neutral | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0008](../sources/experiences/exp-a-kd-20260518-0008.md) | Vector pack materialization for read-only vec16: valid improvement | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0009](../sources/experiences/exp-a-kd-20260518-0009.md) | Vector pack materialization for read-only vec4: regression | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0045](../sources/experiences/exp-a-kd-20260518-0045.md) | Replace all six integer division/modulo operations with CUTLASS-style FastDivmod | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-0046](../sources/experiences/exp-a-kd-20260518-0046.md) | Replace if-else branch with PTX inline assembly using predicate registers (setp. | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0049](../sources/experiences/exp-a-kd-20260518-0049.md) | Replace conditional branch with inline PTX predicated mov (setp + @p mov) to eli | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0055](../sources/experiences/exp-a-kd-20260518-0055.md) | Increased kFragmentsPerIteration from 1 to 2 to halve the number of __syncthread | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-0060](../sources/experiences/exp-a-kd-20260518-0060.md) | Skip the beta multiply entirely by directly assigning source_frag to intermediat | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-0062](../sources/experiences/exp-a-kd-20260518-0062.md) | Eliminate the source tensor load entirely when OnlyAlphaScaling by using a compi | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0063](../sources/experiences/exp-a-kd-20260518-0063.md) | Eliminate source tensor load and beta multiply entirely when beta=0 (OnlyAlphaSc | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0076](../sources/experiences/exp-a-kd-20260518-0076.md) | Replace the 128-iteration sub-byte element loop with a 4-iteration word-level OR | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0078](../sources/experiences/exp-a-kd-20260518-0078.md) | Replace the element-by-element loop (128 iterations of sub-byte get/set) with a  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0081](../sources/experiences/exp-a-kd-20260518-0081.md) | Replace C++ if-branch with explicit PTX @p st.global.v4.u32 predicated store via | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0082](../sources/experiences/exp-a-kd-20260518-0082.md) | Replace the C++ if-branch with inline PTX predicated global store (setp.ne.b32 + | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0083](../sources/experiences/exp-a-kd-20260518-0083.md) | interleaved_store | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-0099](../sources/experiences/exp-a-kd-20260518-0099.md) | float_4x112x112_3to4 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0102](../sources/experiences/exp-a-kd-20260518-0102.md) | Vectorize I/O from scalar float to float2 when both c_in and c_out are even: hal | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0103](../sources/experiences/exp-a-kd-20260518-0103.md) | Vectorize scalar float I/O to float2 by casting pointers and halving channel dim | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0106](../sources/experiences/exp-a-kd-20260518-0106.md) | Pad each threadblock's workspace region to the next 128-byte cacheline boundary  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0123](../sources/experiences/exp-a-kd-20260518-0123.md) | Replace the int32_t-only overload plus manual punning wrapper with a single temp | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0138](../sources/experiences/exp-a-kd-20260518-0138.md) | shape_16x8x8 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0163](../sources/experiences/exp-a-kd-20260518-0163.md) | Insert an early work-done event recorded after the main kernel but before the ta | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0168](../sources/experiences/exp-a-kd-20260518-0168.md) | Replace FastDivmod with hardcoded integer div/mod by 2, and narrow remapping to  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0169](../sources/experiences/exp-a-kd-20260518-0169.md) | Add a (sm_occupancy > 1) guard before the remapping logic so that when only one  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0180](../sources/experiences/exp-a-kd-20260518-0180.md) | Annotate the kernel parameter with __grid_constant__ and const to explicitly req | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0181](../sources/experiences/exp-a-kd-20260518-0181.md) | small_params | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0182](../sources/experiences/exp-a-kd-20260518-0182.md) | Refactor to CUTLASS 3.0 device_kernel pattern: wrap kernel body in a TransformOp | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0224](../sources/experiences/exp-a-kd-20260518-0224.md) | manual_vs_cute_abstraction | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0231](../sources/experiences/exp-a-kd-20260518-0231.md) | f32_1M | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0240](../sources/experiences/exp-a-kd-20260518-0240.md) | f16_large | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0416](../sources/experiences/exp-a-kd-20260518-0416.md) | push_signal_rw | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0425](../sources/experiences/exp-a-kd-20260518-0425.md) | medium_batch_32 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0456](../sources/experiences/exp-a-kd-20260518-0456.md) | vec_copy_vpt32 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0464](../sources/experiences/exp-a-kd-20260518-0464.md) | Vectorize to half2 (two FP16 values per thread) via reinterpret_cast, halving th | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0530](../sources/experiences/exp-a-kd-20260518-0530.md) | fp32_64K | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0565](../sources/experiences/exp-a-kd-20260518-0565.md) | float_per_token_topk8_h4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0639](../sources/experiences/exp-a-kd-20260518-0639.md) | fp16_hdim1024_smem_vs_reload | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0642](../sources/experiences/exp-a-kd-20260518-0642.md) | float_32k_vocab | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0671](../sources/experiences/exp-a-kd-20260518-0671.md) | broadcast_half2halves | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0672](../sources/experiences/exp-a-kd-20260518-0672.md) | vec16_half2float | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0673](../sources/experiences/exp-a-kd-20260518-0673.md) | vec4_half2float | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0674](../sources/experiences/exp-a-kd-20260518-0674.md) | vec16_read | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0675](../sources/experiences/exp-a-kd-20260518-0675.md) | vec4_read | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0678](../sources/experiences/exp-a-kd-20260518-0678.md) | vector_zp_sub | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0778](../sources/experiences/exp-a-kd-20260518-0778.md) | float_aligned_4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0787](../sources/experiences/exp-a-kd-20260518-0787.md) | d2h_transfer_overhead | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0789](../sources/experiences/exp-a-kd-20260518-0789.md) | small_kernel_sync | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0886](../sources/experiences/exp-a-kd-20260518-0886.md) | aligned_1024 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0887](../sources/experiences/exp-a-kd-20260518-0887.md) | aligned_4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0888](../sources/experiences/exp-a-kd-20260518-0888.md) | unaligned_1021 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0906](../sources/experiences/exp-a-kd-20260518-0906.md) | strided_float | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0981](../sources/experiences/exp-a-kd-20260518-0981.md) | to_half4 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0991](../sources/experiences/exp-a-kd-20260518-0991.md) | fp16_hidden4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0992](../sources/experiences/exp-a-kd-20260518-0992.md) | fp16_hidden6144 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0993](../sources/experiences/exp-a-kd-20260518-0993.md) | fp16_h4096_constexpr | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1055](../sources/experiences/exp-a-kd-20260518-1055.md) | float_absmax_aligned_4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1112](../sources/experiences/exp-a-kd-20260518-1112.md) | typical_values | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1176](../sources/experiences/exp-a-kd-20260518-1176.md) | coalesced_offset_4M | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-1293](../sources/experiences/exp-a-kd-20260518-1293.md) | aligned_prefix_4k | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1370](../sources/experiences/exp-a-kd-20260518-1370.md) | float_dtype_hidden_1024 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1371](../sources/experiences/exp-a-kd-20260518-1371.md) | float_dtype_hidden_4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1372](../sources/experiences/exp-a-kd-20260518-1372.md) | scale_host_sync | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1443](../sources/experiences/exp-a-kd-20260518-1443.md) | single_token_static | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0006-1](../sources/experiences/exp-a-kd-20260519-0006-1.md) | Change fast_exp return type from float to half_t so the FP16 result of ::hexp st | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0045-1](../sources/experiences/exp-a-kd-20260519-0045-1.md) | Replace all six integer division/modulo operations with CUTLASS-style FastDivmod | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0046-1](../sources/experiences/exp-a-kd-20260519-0046-1.md) | Replace if-else branch with PTX predicated move instructions using inline assemb | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0049-1](../sources/experiences/exp-a-kd-20260519-0049-1.md) | Replace the conditional branch with inline PTX using predicated mov (@p mov.u32  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0058-1](../sources/experiences/exp-a-kd-20260519-0058-1.md) | Use compile-time ScaleType::OnlyAlphaScaling to make is_source_needed() return f | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0061-1](../sources/experiences/exp-a-kd-20260519-0061-1.md) | When beta is known to be 1.0 (NoBetaScaling path), eliminate the mul_source call | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0062-1](../sources/experiences/exp-a-kd-20260519-0062-1.md) | Make is_source_needed() a compile-time decision for the OnlyAlphaScaling epilogu | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0072-1](../sources/experiences/exp-a-kd-20260519-0072-1.md) | Coarsen the loop by processing FPP=2 fragments per iteration using partitioned s | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0073-1](../sources/experiences/exp-a-kd-20260519-0073-1.md) | Coarsen the loop stride by FPP=2 so each iteration stages multiple fragments int | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0075-1](../sources/experiences/exp-a-kd-20260519-0075-1.md) | Replace the 128-iteration element-by-element sub-byte extraction and insertion l | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0076-1](../sources/experiences/exp-a-kd-20260519-0076-1.md) | Replace the 128-iteration sub-byte element loop with a 4-iteration word-level lo | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0077-1](../sources/experiences/exp-a-kd-20260519-0077-1.md) | Replace the 128-iteration element-wise get/set loop with a 4-iteration loop that | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0078-1](../sources/experiences/exp-a-kd-20260519-0078-1.md) | Replace the 128-iteration element-by-element XOR loop with a 4-iteration word-le | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0081-1](../sources/experiences/exp-a-kd-20260519-0081-1.md) | Replace the C++ if-branch with an explicit PTX-level predicated store using inli | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0082-1](../sources/experiences/exp-a-kd-20260519-0082-1.md) | Replace the C++ if-guarded store with inline PTX using setp.ne.b32 to set a .pre | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0099-1](../sources/experiences/exp-a-kd-20260519-0099-1.md) | Replace scalar element-wise kernel with shared-memory-tiled float4 vectorized ke | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0101-1](../sources/experiences/exp-a-kd-20260519-0101-1.md) | Replace scalar per-element kernel with a specialized 3-to-8 channel kernel using | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0102-1](../sources/experiences/exp-a-kd-20260519-0102-1.md) | Replace scalar float pointers with float2 pointers and halve the channel dimensi | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0122-1](../sources/experiences/exp-a-kd-20260519-0122-1.md) | Replace the int32_t-only overload and manual memcpy wrapper with a single templa | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0123-1](../sources/experiences/exp-a-kd-20260519-0123-1.md) | Replace the int32_t-only API and manual punning wrapper with a templated warp_un | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0124-1](../sources/experiences/exp-a-kd-20260519-0124-1.md) | Replace the int32_t-only function with a templated warp_uniform<T> using a union | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0161-1](../sources/experiences/exp-a-kd-20260519-0161-1.md) | Insert cudaStreamWaitEvent between consecutive kernel launches using cudaEventDi | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0163-1](../sources/experiences/exp-a-kd-20260519-0163-1.md) | Record a work-done event (cudaEventRecord with cudaEventDisableTiming) immediate | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0168-1](../sources/experiences/exp-a-kd-20260519-0168-1.md) | Replace FastDivmod with hardcoded integer division/modulo by 2, limiting remappi | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0169-1](../sources/experiences/exp-a-kd-20260519-0169-1.md) | Add a (sm_occupancy > 1) guard to skip all remapping logic when sm_occupancy=1,  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0178-1](../sources/experiences/exp-a-kd-20260519-0178-1.md) | The after code wraps threadIdx.x / 32 in __shfl_sync(0xffffffff, ..., 0) to broa | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0179-1](../sources/experiences/exp-a-kd-20260519-0179-1.md) | Replace local threadIdx.x / 128 with __shfl_sync(0xffffffff, threadIdx.x / NumTh | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0180-1](../sources/experiences/exp-a-kd-20260519-0180-1.md) | Add __grid_constant__ qualifier to the kernel parameter declaration to explicitl | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0181-1](../sources/experiences/exp-a-kd-20260519-0181-1.md) | Annotate the by-value params argument with __grid_constant__ to request constant | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0182-1](../sources/experiences/exp-a-kd-20260519-0182-1.md) | Adopt the CUTLASS 3.0 device_kernel pattern: wrap computation in an Operator str | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0183-1](../sources/experiences/exp-a-kd-20260519-0183-1.md) | Refactor the kernel into a CUTLASS-style functor pattern with __launch_bounds__( | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0187-1](../sources/experiences/exp-a-kd-20260519-0187-1.md) | Replace __shfl_sync(threadIdx.x/32, 0) with a plain threadIdx.x/32 computation v | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0189-1](../sources/experiences/exp-a-kd-20260519-0189-1.md) | Replace __shfl_sync broadcast with a plain threadIdx.x / 32 integer division wra | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0190-1](../sources/experiences/exp-a-kd-20260519-0190-1.md) | Replace __shfl_sync warp shuffle with canonical_warp_idx() that computes threadI | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0191-1](../sources/experiences/exp-a-kd-20260519-0191-1.md) | Replace the __shfl_sync warp shuffle with a direct threadIdx.x / 32 integer divi | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0192-1](../sources/experiences/exp-a-kd-20260519-0192-1.md) | Replace __shfl_sync-based warp index broadcast with direct arithmetic (threadIdx | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0194-1](../sources/experiences/exp-a-kd-20260519-0194-1.md) | Replace __shfl_sync-based warp index broadcast with canonical_warp_idx() using p | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0196-1](../sources/experiences/exp-a-kd-20260519-0196-1.md) | Replace __shfl_sync warp shuffle with a __device__ helper canonical_warp_idx() t | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0197-1](../sources/experiences/exp-a-kd-20260519-0197-1.md) | Replace __shfl_sync with a direct threadIdx.x / 32 computation wrapped in canoni | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0314-1](../sources/experiences/exp-a-kd-20260519-0314-1.md) | Keep the running accumulator entirely in fp32 using a dedicated float buffer, pe | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0315-1](../sources/experiences/exp-a-kd-20260519-0315-1.md) | Remove the redundant cudaMemset calls from both warmup and timed loops since the | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0333-1](../sources/experiences/exp-a-kd-20260519-0333-1.md) | Reduce the shared-memory reservation from 49,152 bytes to 24,576 bytes by halvin | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0334-1](../sources/experiences/exp-a-kd-20260519-0334-1.md) | Reduce shared memory per block from 96 KB to 48 KB and block size from 128 to 64 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0455-1](../sources/experiences/exp-a-kd-20260519-0455-1.md) | Use CuTe local_tile to assign 8 half elements (16 bytes) per thread, then copy() | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0455-2](../sources/experiences/exp-a-kd-20260519-0455-2.md) | Use recast<half2>() to reinterpret 8-element register tensors as 4-element half2 | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0456-1](../sources/experiences/exp-a-kd-20260519-0456-1.md) | Replace manual LDST128BITS/HALF2 reinterpret_cast macros with CuTe tensor abstra | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0463-1](../sources/experiences/exp-a-kd-20260519-0463-1.md) | Apply float4 (128-bit) vectorized loads and stores so each thread processes 4 el | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0464-1](../sources/experiences/exp-a-kd-20260519-0464-1.md) | Vectorize to half2 processing (two FP16 elements per thread) via reinterpret_cas | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0465-1](../sources/experiences/exp-a-kd-20260519-0465-1.md) | Widen per-thread work from 2 to 8 elements by using 4 half2 register pairs, but  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0466-1](../sources/experiences/exp-a-kd-20260519-0466-1.md) | Consolidate 4 separate half2 loads into a single 128-bit LDST128BITS (float4) lo | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0546-1](../sources/experiences/exp-a-kd-20260519-0546-1.md) | Vectorize memory access using float4 (128-bit) loads and stores so each thread p | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0547-1](../sources/experiences/exp-a-kd-20260519-0547-1.md) | Process 2 FP16 elements per thread using half2 vectorized loads/stores via reint | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0548-1](../sources/experiences/exp-a-kd-20260519-0548-1.md) | The f16x8 unpack approach widens per-thread processing from 2 to 8 elements by l | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0549-1](../sources/experiences/exp-a-kd-20260519-0549-1.md) | Consolidate 4 half2 loads/stores into single 128-bit LDST128BITS (float4) transa | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0783-1](../sources/experiences/exp-a-kd-20260519-0783-1.md) | Reorganize from 1-token-per-CTA (256 threads, blockReduceMax + __syncthreads) to | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0784-1](../sources/experiences/exp-a-kd-20260519-0784-1.md) | Replace 1-token-per-CTA blockReduceMax (256 threads, __syncthreads) with 8-token | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0791-1](../sources/experiences/exp-a-kd-20260519-0791-1.md) | Fuse normalize and scale into a single fused_rescale_kernel that reads each elem | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0798-1](../sources/experiences/exp-a-kd-20260519-0798-1.md) | Replace shared-memory GroupReduceMax with __shfl_xor_sync warp shuffle reduction | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0800-1](../sources/experiences/exp-a-kd-20260519-0800-1.md) | Replace scalar stride-16 __half loads with 16-byte vectorized loads via a half8_ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0801-1](../sources/experiences/exp-a-kd-20260519-0801-1.md) | Replace scalar __half loads with vectorized 16-byte loads via a custom half8_vec | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0802-1](../sources/experiences/exp-a-kd-20260519-0802-1.md) | Replace magic-number 16 with named constants (threads_per_group, GROUPS_PER_BLOC | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0803-1](../sources/experiences/exp-a-kd-20260519-0803-1.md) | Change GROUPS_PER_BLOCK from 16 to 1, launching num_groups blocks of 16 threads  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0815-1](../sources/experiences/exp-a-kd-20260519-0815-1.md) | Add a bool IS_COLUMN_MAJOR template parameter with if constexpr dispatch: when f | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0825-1](../sources/experiences/exp-a-kd-20260519-0825-1.md) | Move the weight and input loads (float2 w, inp via regular ld.global.v2.f32 cach | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0826-1](../sources/experiences/exp-a-kd-20260519-0826-1.md) | The attempted simplification stripped the Semaphore struct's alignas(128) paddin | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0827-1](../sources/experiences/exp-a-kd-20260519-0827-1.md) | Pad each block's signal to 128-byte alignment using alignas(128) struct so each  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0856-1](../sources/experiences/exp-a-kd-20260519-0856-1.md) | Pre-compute all sorted_id / top_k divisions once during the shared-memory loadin | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0862-1](../sources/experiences/exp-a-kd-20260519-0862-1.md) | Split the two-category write-back into three categories — misses placed just bef | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0872-1](../sources/experiences/exp-a-kd-20260519-0872-1.md) | Replace the 2D nested loop with a flat 1D global thread index that strides acros | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0872-2](../sources/experiences/exp-a-kd-20260519-0872-2.md) | Size the grid by totalWorkSize (numRows*colsPerRow) instead of just numRows, and | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0874-1](../sources/experiences/exp-a-kd-20260519-0874-1.md) | Cache all expert offsets into shared memory via cooperative int4-vectorized load | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0875-1](../sources/experiences/exp-a-kd-20260519-0875-1.md) | Replace the pure stochastic acceptance `coin < acc` with a parameterized combine | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0876-1](../sources/experiences/exp-a-kd-20260519-0876-1.md) | Add a greedy shortcut clause that unconditionally accepts any draft token whose  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0878-1](../sources/experiences/exp-a-kd-20260519-0878-1.md) | Fuse the alignment and padding operations into a single fused_align_and_padding_ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0878-2](../sources/experiences/exp-a-kd-20260519-0878-2.md) | Replace scalar int32 stores with 4-wide AlignedArray<int32_t,4> vectorized store | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0879-1](../sources/experiences/exp-a-kd-20260519-0879-1.md) | Replace scalar int32_t stores with 4-wide AlignedArray<int32_t,4> vectorized sto | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0880-1](../sources/experiences/exp-a-kd-20260519-0880-1.md) | Replace scalar int32_t stores with 4-wide AlignedArray<int32_t,4> vectorized sto | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0881-1](../sources/experiences/exp-a-kd-20260519-0881-1.md) | Fuse the normalize and conditional scale operations into a single kernel (rescal | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0882-1](../sources/experiences/exp-a-kd-20260519-0882-1.md) | Fuse normalization and conditional scaling into a single kernel that reads each  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0886-1](../sources/experiences/exp-a-kd-20260519-0886-1.md) | Replace global loop with round-robin thread assignment that statically partition | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0888-1](../sources/experiences/exp-a-kd-20260519-0888-1.md) | Replace scalar half loads with vectorized 16-byte loads via vec_t<T,8>::cast_loa | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0888-2](../sources/experiences/exp-a-kd-20260519-0888-2.md) | Replace shared-memory reduction with warp-shuffle __shfl_xor_sync reduction (Gro | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0893-1](../sources/experiences/exp-a-kd-20260519-0893-1.md) | The after kernel attempts to improve output throughput by using a fixed VEC_SIZE | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0894-1](../sources/experiences/exp-a-kd-20260519-0894-1.md) | Widen the per-thread vector size to 16 fp8 elements (128 bits) and replace the s | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0896-1](../sources/experiences/exp-a-kd-20260519-0896-1.md) | Double the vector size to 16 elements (matching 128-bit = 16 uint8_t output byte | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0914-1](../sources/experiences/exp-a-kd-20260519-0914-1.md) | Replaced FP8_TYPE_WRAPPER with __nv_fp8_e4m3 native CUDA type expecting hardware | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0915-1](../sources/experiences/exp-a-kd-20260519-0915-1.md) | Replace FP8_TYPE_WRAPPER with __nv_fp8_e4m3 native CUDA type, expecting NVCC to  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0917-1](../sources/experiences/exp-a-kd-20260519-0917-1.md) | Replace custom FP8Wrapper and inline fp8e4m3fn_from_fp32_value with native __nv_ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0918-1](../sources/experiences/exp-a-kd-20260519-0918-1.md) | The analysis reveals that __nv_fp8_e4m3 with static_cast only benefits GPUs with | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0919-1](../sources/experiences/exp-a-kd-20260519-0919-1.md) | Replace custom FP8Wrapper bit-manipulation conversion with NVCC's native __nv_fp | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0920-1](../sources/experiences/exp-a-kd-20260519-0920-1.md) | Replace the custom FP8Wrapper type with NVCC's native __nv_fp8_e4m3 type as a te | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0940-1](../sources/experiences/exp-a-kd-20260519-0940-1.md) | Move the reciprocal scale computation (1.0f / scale) to the host side before ker | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0941-1](../sources/experiences/exp-a-kd-20260519-0941-1.md) | Replace the global memory pointer parameter (const float* scale_ptr) with a scal | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0951-1](../sources/experiences/exp-a-kd-20260519-0951-1.md) | Replace thread-per-expert with cooperative binary search across all threads: eve | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0952-1](../sources/experiences/exp-a-kd-20260519-0952-1.md) | Replace thread-per-expert sequential fill with cooperative binary search across  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0969-1](../sources/experiences/exp-a-kd-20260519-0969-1.md) | Coarsen the grid by assigning 16 groups per block with 256 threads (8 warps), ma | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0975-1](../sources/experiences/exp-a-kd-20260519-0975-1.md) | Hoist the loop-invariant scale computation (null-pointer check, global memory lo | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0976-1](../sources/experiences/exp-a-kd-20260519-0976-1.md) | Hoist the loop-invariant scale computation (null-pointer check and float divisio | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0977-1](../sources/experiences/exp-a-kd-20260519-0977-1.md) | Add a scalar tail loop that processes the remaining (hidden_size % vec_size) ele | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0980-1](../sources/experiences/exp-a-kd-20260519-0980-1.md) | Replace bool* tree_mask with uint8_t* bit-packed representation where each row u | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0981-1](../sources/experiences/exp-a-kd-20260519-0981-1.md) | Replace bool* tree_mask (1 byte per boolean) with uint8_t* bit-packed representa | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1000-1](../sources/experiences/exp-a-kd-20260519-1000-1.md) | Hoist all three redundant host-side operations (cudaStreamCreate/Destroy, cudaGe | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1007-1](../sources/experiences/exp-a-kd-20260519-1007-1.md) | Remove the scalar remainder loop entirely and enforce alignment (hidden_dim % ve | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1009-1](../sources/experiences/exp-a-kd-20260519-1009-1.md) | Cache input in shared memory during Pass-1 (with bank-conflict padding via 32-by | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1011-1](../sources/experiences/exp-a-kd-20260519-1011-1.md) | Cache Pass-1 input data into shared memory with 32-byte bank-conflict-padded str | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1018-1](../sources/experiences/exp-a-kd-20260519-1018-1.md) | Replace the hand-rolled vec4_t (4-element, 64-bit aligned) with flashinfer::vec_ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1019-1](../sources/experiences/exp-a-kd-20260519-1019-1.md) | Replace manual vec4_t (64-bit, 4-element) vectorization with flashinfer::vec_t ( | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1020-1](../sources/experiences/exp-a-kd-20260519-1020-1.md) | Replace custom vec4_t (64-bit) with flashinfer::vec_t using int4-backed 128-bit  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1037-1](../sources/experiences/exp-a-kd-20260519-1037-1.md) | Replace scalar int32 stores with int4 vectorized stores: pack the sentinel into  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1038-1](../sources/experiences/exp-a-kd-20260519-1038-1.md) | Replace scalar int32 stores with vectorized int4 stores, packing the fill value  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1047-1](../sources/experiences/exp-a-kd-20260519-1047-1.md) | Pack 8 tokens per CTA with one warp (32 threads) per token, replacing blockReduc | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1048-1](../sources/experiences/exp-a-kd-20260519-1048-1.md) | Pack 8 tokens per CTA with one warp per token, replacing blockReduceMax + __shar | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1049-1](../sources/experiences/exp-a-kd-20260519-1049-1.md) | Warp-level multi-token packing assigns each warp to one token using warpReduceMa | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1050-1](../sources/experiences/exp-a-kd-20260519-1050-1.md) | Stage input data to shared memory during pass-1 (alongside max computation), the | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1052-1](../sources/experiences/exp-a-kd-20260519-1052-1.md) | Vectorize to float4 (kAlignment=4) so each thread processes 4 logits per iterati | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1053-1](../sources/experiences/exp-a-kd-20260519-1053-1.md) | Replace scalar float reads/writes with vectorized float4 (128-bit) loads/stores, | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1054-1](../sources/experiences/exp-a-kd-20260519-1054-1.md) | Replace scalar int32 stores with vectorized int4 stores, packing 4 int32 values  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1058-1](../sources/experiences/exp-a-kd-20260519-1058-1.md) | Replace scalar load/store loops with single pointer-cast AlignedArray loads and  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1075-1](../sources/experiences/exp-a-kd-20260519-1075-1.md) | Replace bool-per-element mask with bit-packed uint8_t mask to achieve 8x memory  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1076-1](../sources/experiences/exp-a-kd-20260519-1076-1.md) | Replace bool-per-element mask with bit-packed uint8_t mask where each bit repres | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1077-1](../sources/experiences/exp-a-kd-20260519-1077-1.md) | Replace bool-per-element mask with bit-packed uint8_t mask (256*32*4 = 32768 byt | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1109-1](../sources/experiences/exp-a-kd-20260519-1109-1.md) | Materialize the global-memory vector pack into a local variable (vin_t src = v_i | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1110-1](../sources/experiences/exp-a-kd-20260519-1110-1.md) | Materialize v_in[i] into a local register variable (vin_t src = v_in[i]) before  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1111-1](../sources/experiences/exp-a-kd-20260519-1111-1.md) | Materialize the vector pack into a local vin_t variable before passing it to the | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1112-1](../sources/experiences/exp-a-kd-20260519-1112-1.md) | Pass the global-memory reference v_in[i] directly to the __forceinline__ operato | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1116-1](../sources/experiences/exp-a-kd-20260519-1116-1.md) | Replace division/modulo with bitwise shift/AND for power-of-2 decompositions (mI | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1116-2](../sources/experiences/exp-a-kd-20260519-1116-2.md) | Precompute int32_t const numKTiles = (numCols + 63) / 64 at kernel scope outside | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1117-1](../sources/experiences/exp-a-kd-20260519-1117-1.md) | Replace all division/modulo with bitwise shift/AND (valid for power-of-2 divisor | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1118-1](../sources/experiences/exp-a-kd-20260519-1118-1.md) | Replace raw m with effectiveRows = round_up_int(m, 128) in the grid size calcula | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1119-1](../sources/experiences/exp-a-kd-20260519-1119-1.md) | Replace raw m with effectiveRows=round_up(m,128) in the grid size calculation, d | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1120-1](../sources/experiences/exp-a-kd-20260519-1120-1.md) | Replace raw m with effectiveRows = round_up(m, 128) as the grid size upper bound | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1121-1](../sources/experiences/exp-a-kd-20260519-1121-1.md) | Precompute numKTiles once at kernel entry and pass it as parameter, replace all  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1123-1](../sources/experiences/exp-a-kd-20260519-1123-1.md) | Replace all div/mod operations on power-of-2 divisors with explicit right-shift  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1136-1](../sources/experiences/exp-a-kd-20260519-1136-1.md) | Generalize the kernel into a template <bool STRIDE_I_ZERO, bool STRIDE_J_ZERO> m | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1137-1](../sources/experiences/exp-a-kd-20260519-1137-1.md) | Replace the scalar strided loop with a per-group float4 vectorized path that pro | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1138-1](../sources/experiences/exp-a-kd-20260519-1138-1.md) | Replace scalar element-wise loop with float4 vectorized per-group dispatch using | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1144-1](../sources/experiences/exp-a-kd-20260519-1144-1.md) | Replace __hadd2 CUDA intrinsic with inline PTX asm 'add.f16x2' using explicit re | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1145-1](../sources/experiences/exp-a-kd-20260519-1145-1.md) | Replace __hmul2 intrinsic with explicit PTX inline asm mul.f16x2 using uint32_t  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1146-1](../sources/experiences/exp-a-kd-20260519-1146-1.md) | Replace __hfma2 intrinsic with PTX inline asm 'fma.rn.f16x2' using explicit uint | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1147-1](../sources/experiences/exp-a-kd-20260519-1147-1.md) | The batched cvt.rn.f16x2.f32 instruction replaces two scalar conversions with on | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1148-1](../sources/experiences/exp-a-kd-20260519-1148-1.md) | Replace two separate cvt.rn.f16.f32 instructions with a single cvt.rn.f16x2.f32  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1149-1](../sources/experiences/exp-a-kd-20260519-1149-1.md) | Replace the entire float-domain pipeline with native half2 PTX operations: use h | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1150-1](../sources/experiences/exp-a-kd-20260519-1150-1.md) | Replace the entire float-domain pipeline with native PTX f16x2 packed operations | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1159-1](../sources/experiences/exp-a-kd-20260519-1159-1.md) | Convert the runtime scoring_func parameter into a compile-time template paramete | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1172-1](../sources/experiences/exp-a-kd-20260519-1172-1.md) | Eliminate the GPU-side segmented_max_reduction kernel entirely by pre-computing  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1182-1](../sources/experiences/exp-a-kd-20260519-1182-1.md) | Replace 4 scalar __half2float(__low2half/__high2half) calls with 2 vector __half | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1183-1](../sources/experiences/exp-a-kd-20260519-1183-1.md) | Replace the four scalar __half2float(__low2half/__high2half) calls with two vect | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1194-1](../sources/experiences/exp-a-kd-20260519-1194-1.md) | Replace the software SoftFP8E4M3FN type with NVIDIA's native __nv_fp8_e4m3 hardw | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1195-1](../sources/experiences/exp-a-kd-20260519-1195-1.md) | Replace the 70-line software FP8 emulation struct with the native __nv_fp8_e4m3  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1203-1](../sources/experiences/exp-a-kd-20260519-1203-1.md) | Pre-compute sh_ids[i] / top_k into a second shared memory array (sh_precomputed) | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1224-1](../sources/experiences/exp-a-kd-20260519-1224-1.md) | Pass the scalar as a device pointer (const float* d_scale) so the kernel reads * | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1225-1](../sources/experiences/exp-a-kd-20260519-1225-1.md) | Keep the scalar on device and pass a device pointer (const float* d_scale_ptr) t | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1226-1](../sources/experiences/exp-a-kd-20260519-1226-1.md) | Eliminate the cudaMemcpy DeviceToHost by keeping the scalar on device and passin | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1234-1](../sources/experiences/exp-a-kd-20260519-1234-1.md) | Replace inverted-scale multiplication with direct per-element division and intro | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1235-1](../sources/experiences/exp-a-kd-20260519-1235-1.md) | The after version replaces inverted-scale multiplication (precompute FP8_E4M3_MA | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1243-1](../sources/experiences/exp-a-kd-20260519-1243-1.md) | Replace the hardcoded typedef with a templated q8x4_t<quant_type_t> struct plus  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1248-1](../sources/experiences/exp-a-kd-20260519-1248-1.md) | Replace the three-operation software path (rintf + fmaxf/fminf + cast) with a si | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1249-1](../sources/experiences/exp-a-kd-20260519-1249-1.md) | Replace the runtime bool argument with a template parameter bool is_scale_invert | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1249-2](../sources/experiences/exp-a-kd-20260519-1249-2.md) | Replace the multi-instruction software conversion with a single PTX inline asm c | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1257-1](../sources/experiences/exp-a-kd-20260519-1257-1.md) | Replace the synchronous int4 copy with cp.async.ca.shared.global PTX instruction | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1273-1](../sources/experiences/exp-a-kd-20260519-1273-1.md) | Cast float pointers to P32* (array_t<float,4> with __align__(16)) so each iterat | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1274-1](../sources/experiences/exp-a-kd-20260519-1274-1.md) | Replace scalar per-element loads with 128-bit packed loads using array_t<half,8> | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1291-1](../sources/experiences/exp-a-kd-20260519-1291-1.md) | Replace the CPU round-trip with an on-device GPU kernel that uses a 256-byte pre | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1293-1](../sources/experiences/exp-a-kd-20260519-1293-1.md) | Replace the per-nibble branching function with a 256-entry __constant__ memory l | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1293-2](../sources/experiences/exp-a-kd-20260519-1293-2.md) | Use uint4 (16-byte) vector loads/stores to process 16 bytes per thread per itera | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1294-1](../sources/experiences/exp-a-kd-20260519-1294-1.md) | Replace scalar byte loads/stores with uint4 (16-byte) vectorized loads/stores vi | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1294-2](../sources/experiences/exp-a-kd-20260519-1294-2.md) | Precompute all 256 byte-to-byte mappings into a constant-memory lookup table (kN | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1295-1](../sources/experiences/exp-a-kd-20260519-1295-1.md) | Pack 8 half elements into a __align__(16) half8_packed_t struct containing 4 x _ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1301-1](../sources/experiences/exp-a-kd-20260519-1301-1.md) | Cache the expert_map into shared memory via cooperative loading with __syncthrea | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1302-1](../sources/experiences/exp-a-kd-20260519-1302-1.md) | Cooperatively load the entire expert offset array into shared memory via __ldg b | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1303-1](../sources/experiences/exp-a-kd-20260519-1303-1.md) | Cache the entire expert_first_token_offset array into shared memory via cooperat | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1313-1](../sources/experiences/exp-a-kd-20260519-1313-1.md) | Load the entire expert_first_token_offset array into shared memory via __ldg (re | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1327-1](../sources/experiences/exp-a-kd-20260519-1327-1.md) | Replace the conditional vectorization branch with vectorize_with_alignment, whic | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1328-1](../sources/experiences/exp-a-kd-20260519-1328-1.md) | Replace conditional all-or-nothing vectorization with vectorize_with_alignment w | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1340-1](../sources/experiences/exp-a-kd-20260519-1340-1.md) | Pack adjacent BF16 pairs into __nv_bfloat162 structs and use the native __hadd2  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1341-1](../sources/experiences/exp-a-kd-20260519-1341-1.md) | Replace 8 scalar __hadd calls with 4 packed __hadd2 calls using __halves2half2 p | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1349-1](../sources/experiences/exp-a-kd-20260519-1349-1.md) | Replace cutlass::bfloat16_t with native nv_bfloat16 type and explicitly pack adj | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1379-1](../sources/experiences/exp-a-kd-20260519-1379-1.md) | Precompute the inverse scale (1.0f / *scale) once per thread at kernel entry and | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1380-1](../sources/experiences/exp-a-kd-20260519-1380-1.md) | Precompute the reciprocal scale (1.0f / *scale) once per thread outside the loop | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1381-1](../sources/experiences/exp-a-kd-20260519-1381-1.md) | Precompute the reciprocal of scale (1.0f / *scale) once per thread before the lo | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1382-1](../sources/experiences/exp-a-kd-20260519-1382-1.md) | Replace scalar element-wise access with vec4_t<__half> (8-byte) and float4_t (16 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1383-1](../sources/experiences/exp-a-kd-20260519-1383-1.md) | Replace the scalar while-loop with a vec4_t<__half> (8-byte) load and float4_t ( | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1384-1](../sources/experiences/exp-a-kd-20260519-1384-1.md) | Replace scalar element-by-element access with 4-element struct-based vectorized  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1386-1](../sources/experiences/exp-a-kd-20260519-1386-1.md) | Replace atomicOr word-level packing with direct byte-level write via reinterpret | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1409-1](../sources/experiences/exp-a-kd-20260519-1409-1.md) | Replace inline with __forceinline__ on all four convert method overloads to guar | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1410-1](../sources/experiences/exp-a-kd-20260519-1410-1.md) | Replace inline with __forceinline__ on all four convert methods to guarantee the | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1411-1](../sources/experiences/exp-a-kd-20260519-1411-1.md) | Specialize the operator+= with if constexpr (std::is_same_v<T2, float2>) to bypa | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1412-1](../sources/experiences/exp-a-kd-20260519-1412-1.md) | Add an if constexpr (std::is_same_v<T2, float2>) specialization that directly mu | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1418-1](../sources/experiences/exp-a-kd-20260519-1418-1.md) | Replace the naive __float2half + memcpy + shift-OR sequence with inline PTX usin | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1439-1](../sources/experiences/exp-a-kd-20260519-1439-1.md) | FP32 pre-reduction scaling via scale_float_device converts each fp16 scale compo | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1462-1](../sources/experiences/exp-a-kd-20260519-1462-1.md) | Cache input into shared memory during the absmax pass and quantize from shared m | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1463-1](../sources/experiences/exp-a-kd-20260519-1463-1.md) | Cache input in shared memory during the first pass (copy global→shared while com | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1464-1](../sources/experiences/exp-a-kd-20260519-1464-1.md) | Cache input data into shared memory during the absmax pass so the quantize pass  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1473-1](../sources/experiences/exp-a-kd-20260519-1473-1.md) | Fuse both passes into one: read global memory once into shared memory while comp | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1474-1](../sources/experiences/exp-a-kd-20260519-1474-1.md) | Add shared memory caching to read input from global memory once into shared memo | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1476-1](../sources/experiences/exp-a-kd-20260519-1476-1.md) | Replace scalar fp16 loads with __half2 packed loads via reinterpret_cast, readin | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1476-2](../sources/experiences/exp-a-kd-20260519-1476-2.md) | Replace scalar float output writes with float4 packed stores via reinterpret_cas | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1489-1](../sources/experiences/exp-a-kd-20260519-1489-1.md) | Add a can_vec guard that checks both address alignment (addr & WIDTH-1 == 0) and | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1490-1](../sources/experiences/exp-a-kd-20260519-1490-1.md) | Add a fast-path early return that checks both pointer alignment (addr & (WIDTH-1 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1500-1](../sources/experiences/exp-a-kd-20260519-1500-1.md) | Replacing the custom blockReduceMax with CUB's BlockReduce<float,1024> caused a  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1514-1](../sources/experiences/exp-a-kd-20260519-1514-1.md) | Wrap min() in a __device__ inline function (min__()) with explicit uint32_t para | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1522-1](../sources/experiences/exp-a-kd-20260519-1522-1.md) | Replace the scalar byte-by-byte decomposition and multiply-add loop with the __d | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1549-1](../sources/experiences/exp-a-kd-20260519-1549-1.md) | Replace scalar __float2half_rn loop with __halves2half2 calls that pack two half | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1551-1](../sources/experiences/exp-a-kd-20260519-1551-1.md) | Replace 4 scalar __half additions with 2 native __half2 vector additions via uni | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1615-1](../sources/experiences/exp-a-kd-20260519-1615-1.md) | Magic-bias technique (arxiv:2406.09904) adds 0x64806480 to FP16 pairs via __hadd | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1636-1](../sources/experiences/exp-a-kd-20260519-1636-1.md) | Replace the hardcoded FP8_E4M3_MAX macro with a type-dependent template trait fp | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1644-1](../sources/experiences/exp-a-kd-20260519-1644-1.md) | Replace named struct members (u0..u7) with a fixed-size array member (d[8]) to e | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1645-1](../sources/experiences/exp-a-kd-20260519-1645-1.md) | Extract the inline if constexpr branch into a standalone __device__ __forceinlin | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1646-1](../sources/experiences/exp-a-kd-20260519-1646-1.md) | Extract the inline if constexpr branch into a standalone __device__ __forceinlin | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1651-1](../sources/experiences/exp-a-kd-20260519-1651-1.md) | Fuse both kernels into a single advance_step_flashinfer_kernel so each thread re | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1655-1](../sources/experiences/exp-a-kd-20260519-1655-1.md) | Replace the class-wrapped Fp8Wrapper + __noinline__ trampoline with a direct __f | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1656-1](../sources/experiences/exp-a-kd-20260519-1656-1.md) | Replace the entire manual bit-unpacking routine with the vendor-provided __nv_fp | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1658-1](../sources/experiences/exp-a-kd-20260519-1658-1.md) | Replace the entire 25-line manual bit-manipulation routine with the vendor-provi | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1659-1](../sources/experiences/exp-a-kd-20260519-1659-1.md) | Replace the manual scalar-decomposition path with the unified __nv_fp8x2_e4m3 ve | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1660-1](../sources/experiences/exp-a-kd-20260519-1660-1.md) | Replace the manual scalar conversion and decomposition with the vectorized __nv_ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1662-1](../sources/experiences/exp-a-kd-20260519-1662-1.md) | Replace the two-step software conversion with __nv_cvt_fp8_to_halfraw intrinsic  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1664-1](../sources/experiences/exp-a-kd-20260519-1664-1.md) | Replace memcpy-based __nv_fp8_e4m3 construction with direct assignment to the __ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1689-1](../sources/experiences/exp-a-kd-20260519-1689-1.md) | Guard the entire allocation, memset, and kernel launch sequence behind a needs_a | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1690-1](../sources/experiences/exp-a-kd-20260519-1690-1.md) | Guard the cudaMalloc+cudaMemset allocation, getMIndicesKernel launch, and subseq | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1721-1](../sources/experiences/exp-a-kd-20260519-1721-1.md) | Replace the scalar strided loop with vectorize_with_alignment<16> (16-element ve | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1722-1](../sources/experiences/exp-a-kd-20260519-1722-1.md) | Replaced per-element division with precomputed reciprocal multiplication (inv_s  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1723-1](../sources/experiences/exp-a-kd-20260519-1723-1.md) | Replace scalar for-loop with vectorize_with_alignment<16> for coalesced 16-eleme | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1725-1](../sources/experiences/exp-a-kd-20260519-1725-1.md) | Replace branch-based ternary absmax with fabsf/fmaxf intrinsics for branch-free  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1725-2](../sources/experiences/exp-a-kd-20260519-1725-2.md) | Use vectorize_with_alignment<16> to load 16 floats (64 bytes) per vector operati | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1726-1](../sources/experiences/exp-a-kd-20260519-1726-1.md) | Merge max and min into a single BlockReduce<MinMax,256> pass using a custom MinM | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1726-2](../sources/experiences/exp-a-kd-20260519-1726-2.md) | Replace the scalar quantization loop with vectorize_with_alignment<16> to proces | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1728-1](../sources/experiences/exp-a-kd-20260519-1728-1.md) | Replace scalar float pointer accesses with vec_n_t<float,4> reinterpret_cast to  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1729-1](../sources/experiences/exp-a-kd-20260519-1729-1.md) | Replace scalar stride loop with DefaultVecOp<4> wrapper over vec_n_t<float,4>, u | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1730-1](../sources/experiences/exp-a-kd-20260519-1730-1.md) | Replace the naive reinterpret_cast with a generic vectorize_with_alignment templ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1731-1](../sources/experiences/exp-a-kd-20260519-1731-1.md) | Replace the scalar stride loop with an alignment-aware vectorized template (vect | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1745-1](../sources/experiences/exp-a-kd-20260519-1745-1.md) | Replace uniform kChunkSize chunks with variable-length chunks read from a pre-co | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1769-1](../sources/experiences/exp-a-kd-20260519-1769-1.md) | Pre-compute aligned_expert_first_token_offset array on the host (or a separate k | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1770-1](../sources/experiences/exp-a-kd-20260519-1770-1.md) | Pre-compute the aligned prefix-sum of expert token offsets on the host into alig | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1771-1](../sources/experiences/exp-a-kd-20260519-1771-1.md) | Pre-compute the aligned expert offset prefix-sum on the host side into a separat | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1795-1](../sources/experiences/exp-a-kd-20260519-1795-1.md) | Fuse the fp8-to-float conversion and scale multiplication into a single kernel w | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1796-1](../sources/experiences/exp-a-kd-20260519-1796-1.md) | Fuse the two-kernel pipeline into a single kernel that reads half, converts to f | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1797-1](../sources/experiences/exp-a-kd-20260519-1797-1.md) | Fuse the absmax computation and quantization into a single kernel: compute per-t | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1798-1](../sources/experiences/exp-a-kd-20260519-1798-1.md) | Fuse the absmax computation and quantization into a single kernel that computes  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1798-2](../sources/experiences/exp-a-kd-20260519-1798-2.md) | Precompute the reciprocal tmp_scale = 127.0f / block_absmax_val once after the b | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1799-1](../sources/experiences/exp-a-kd-20260519-1799-1.md) | Fuse absmax reduction and quantization into a single kernel launch, storing the  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1807-1](../sources/experiences/exp-a-kd-20260519-1807-1.md) | Pass scale as a device pointer (const scale_type* scale_ptr) and dereference it  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1808-1](../sources/experiences/exp-a-kd-20260519-1808-1.md) | Pass scale as a device pointer (const scale_type* scale_ptr) instead of a scalar | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1809-1](../sources/experiences/exp-a-kd-20260519-1809-1.md) | Pass the scale as a device pointer instead of a host scalar; the kernel derefere | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1847-1](../sources/experiences/exp-a-kd-20260519-1847-1.md) | Replacing the two-step half-intermediary path with the single-step __nv_cvt_floa | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1848-1](../sources/experiences/exp-a-kd-20260519-1848-1.md) | Replace the two-step software path with the direct __nv_cvt_float_to_fp8 hardwar | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1849-1](../sources/experiences/exp-a-kd-20260519-1849-1.md) | Replace the entire software emulation with the single-instruction __nv_cvt_float | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1851-1](../sources/experiences/exp-a-kd-20260519-1851-1.md) | Replace the entire software emulation function with the __nv_cvt_float_to_fp8 ha | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2299-1](../sources/experiences/exp-a-kd-20260519-2299-1.md) | Consolidate three separate kernels into one advance_step_kernel that performs al | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2300-1](../sources/experiences/exp-a-kd-20260519-2300-1.md) | Fuse all three per-query tensor updates (token copy, position/length increment,  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2301-1](../sources/experiences/exp-a-kd-20260519-2301-1.md) | Fuse all three kernels into a single advance_step_kernel where each thread compu | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2302-1](../sources/experiences/exp-a-kd-20260519-2302-1.md) | Generalize FP8-specific template names to type-agnostic quant_type_max_v (suppor | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2303-1](../sources/experiences/exp-a-kd-20260519-2303-1.md) | Refactor to SFINAE-constrained quant_type_max<T> and min_scaling_factor<T> templ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2311-1](../sources/experiences/exp-a-kd-20260519-2311-1.md) | Replace the runtime float kernel parameter with a constexpr template struct (min | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2327-1](../sources/experiences/exp-a-kd-20260519-2327-1.md) | Replace unconditional atomicAdd with a conditional branch (if masks[i]) that ski | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2344-1](../sources/experiences/exp-a-kd-20260519-2344-1.md) | Replace vectorized BlockLoad/BlockStore with scalar BLOCK_LOAD_DIRECT/BLOCK_STOR | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2346-1](../sources/experiences/exp-a-kd-20260519-2346-1.md) | Fuse the three separate stride fill kernels into the existing init_offsets_kerne | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2350-1](../sources/experiences/exp-a-kd-20260519-2350-1.md) | Embed cudaDeviceSynchronize inside the wrapper alongside cudaGetLastError, addin | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2351-1](../sources/experiences/exp-a-kd-20260519-2351-1.md) | Embed cudaDeviceSynchronize and printf-based error diagnostics inside the wrappe | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2352-1](../sources/experiences/exp-a-kd-20260519-2352-1.md) | The after code uses __constant__ memory for the LUT, but constant cache can only | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2353-1](../sources/experiences/exp-a-kd-20260519-2353-1.md) | Moving the LUT from __device__ global memory to __constant__ memory causes const | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2354-1](../sources/experiences/exp-a-kd-20260519-2354-1.md) | Replace byte-by-byte scalar load/store with uint4 (16-byte) vectorized load/stor | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2355-1](../sources/experiences/exp-a-kd-20260519-2355-1.md) | Replace byte-by-byte access with uint4 (16-byte) vectorized load/store: each thr | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2361-1](../sources/experiences/exp-a-kd-20260519-2361-1.md) | Eliminate the transpose kernel entirely by indexing the original scale tensor di | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2371-1](../sources/experiences/exp-a-kd-20260519-2371-1.md) | Templatize the kernel with THREADS_PER_SF and wrap __shfl_xor_sync in if constex | analysis | sm100 | cuda-cpp |
| [exp-a-kd-20260519-2372-1](../sources/experiences/exp-a-kd-20260519-2372-1.md) | Templatize the kernel on THREADS_PER_SF and guard the shuffle with if constexpr  | analysis | sm90 | cuda-cpp |
| [exp-i-kd-20260518-0023](../sources/experiences/exp-i-kd-20260518-0023.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0026](../sources/experiences/exp-i-kd-20260518-0026.md) | Implement kernel following the CUTLASS_kernel_template interface pattern with co | implementation | sm90 | cuda-cpp |
| [exp-i-kd-20260518-0028](../sources/experiences/exp-i-kd-20260518-0028.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0029](../sources/experiences/exp-i-kd-20260518-0029.md) | Implement kernel following the CUTLASS_kernel_template interface pattern with co | implementation | sm90 | cuda-cpp |
| [exp-i-kd-20260518-0032](../sources/experiences/exp-i-kd-20260518-0032.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0035](../sources/experiences/exp-i-kd-20260518-0035.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0036](../sources/experiences/exp-i-kd-20260518-0036.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0038](../sources/experiences/exp-i-kd-20260518-0038.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0043](../sources/experiences/exp-i-kd-20260518-0043.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2385-1](../sources/experiences/exp-i-kd-20260519-2385-1.md) | Implement the device function to return -1 directly and call it from the global  | implementation | sm90 | cuda-cpp |
| [exp-i-kd-20260519-2386-1](../sources/experiences/exp-i-kd-20260519-2386-1.md) | Map threads to matrix elements via standard 2D CUDA indexing (threadIdx + blockI | implementation | sm90 | cuda-cpp |
| [exp-i-kd-20260519-2392-1](../sources/experiences/exp-i-kd-20260519-2392-1.md) | Map threads 2D (threadIdx.x for rows, threadIdx.y for columns) with bounds check | implementation | sm90 | cuda-cpp |
| [exp-i-kd-20260519-2394-1](../sources/experiences/exp-i-kd-20260519-2394-1.md) | Map threads to matrix elements using standard 2D CUDA indexing (threadIdx + bloc | implementation | sm90 | cuda-cpp |
| [exp-i-kd-20260519-2414-1](../sources/experiences/exp-i-kd-20260519-2414-1.md) | Declare a local cutlass::Array<T, N> storage, call its built-in clear() member t | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2415-1](../sources/experiences/exp-i-kd-20260519-2415-1.md) | Implement unrolled loop using CUTLASS_PRAGMA_UNROLL with Array::at(i) accessor t | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2416-1](../sources/experiences/exp-i-kd-20260519-2416-1.md) | Initialize each array element via .at(i) with an explicit cast T(int(threadIdx.x | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2417-1](../sources/experiences/exp-i-kd-20260519-2417-1.md) | Use cutlass::NumericArrayConverter<bfloat16_t, float, 2> for packed FP32→BF16 co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2418-1](../sources/experiences/exp-i-kd-20260519-2418-1.md) | Use CUTLASS's FastNumericArrayConverter<Destination, Source, Count> which encaps | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2419-1](../sources/experiences/exp-i-kd-20260519-2419-1.md) | Instantiate the CUTLASS Operator functor, load source elements via pointer deref | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2420-1](../sources/experiences/exp-i-kd-20260519-2420-1.md) | Instantiate cutlass::maximum<half_t, propagate_NaN> as a callable functor with t | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2421-1](../sources/experiences/exp-i-kd-20260519-2421-1.md) | Use cutlass::Array<cutlass::half_t, kN> as the Element type for vectorized SIMD  | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2422-1](../sources/experiences/exp-i-kd-20260519-2422-1.md) | Leverage CUTLASS's template-based operator system: instantiate the Operator temp | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2423-1](../sources/experiences/exp-i-kd-20260519-2423-1.md) | Instantiate cutlass::NumericArrayConverter<Destination, Source, Count> as a loca | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2424-1](../sources/experiences/exp-i-kd-20260519-2424-1.md) | Instantiate cutlass::NumericArrayConverter<Destination, Source, Count> and call  | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2425-1](../sources/experiences/exp-i-kd-20260519-2425-1.md) | Implement two nested-loop phases: Phase 1 iterates over input words and extracts | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2426-1](../sources/experiences/exp-i-kd-20260519-2426-1.md) | Instantiate a stack-allocated cutlass::NumericConverter<tfloat32_t, float, round | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2427-1](../sources/experiences/exp-i-kd-20260519-2427-1.md) | Use standard 1D thread indexing (threadIdx.x + blockIdx.x * blockDim.x) with a b | implementation | sm90 | cuda-cpp |
| [exp-i-kd-20260519-2429-1](../sources/experiences/exp-i-kd-20260519-2429-1.md) | Implement the canonical shared memory staging pattern: coalesced global load int | implementation | sm90 | cuda-cpp |
| [exp-i-kd-20260519-2444-1](../sources/experiences/exp-i-kd-20260519-2444-1.md) | Instantiate the CUTLASS LinearCombinationPlanarComplex<float,4,float,float> func | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2454-1](../sources/experiences/exp-i-kd-20260519-2454-1.md) | Implement a spin-wait loop using cuda::atomic<bool>::load with memory_order_acqu | implementation | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0040](../sources/experiences/exp-o-kd-20260518-0040.md) | float_4x112x112_3to8 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0220](../sources/experiences/exp-o-kd-20260518-0220.md) | Replace all integer division/modulo pairs with CUTLASS-style FastDivmod that use | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0293](../sources/experiences/exp-o-kd-20260518-0293.md) | Replace __shfl_sync(threadIdx.x/32, 0) with a plain threadIdx.x/32 computation v | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0321](../sources/experiences/exp-o-kd-20260518-0321.md) | broadcast_mul | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0326](../sources/experiences/exp-o-kd-20260518-0326.md) | float_1layer_8pairs | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0386](../sources/experiences/exp-o-kd-20260518-0386.md) | medium_16kb | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0399](../sources/experiences/exp-o-kd-20260518-0399.md) | Vectorize memory access by processing 2 FP16 elements per thread using half2 rei | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0549](../sources/experiences/exp-o-kd-20260518-0549.md) | float_to_int8_unaligned | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0760](../sources/experiences/exp-o-kd-20260518-0760.md) | Ny block copies across multiple layers, this resulted in many small, sequential  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0220-1](../sources/experiences/exp-o-kd-20260519-0220-1.md) | Replace all three integer division/modulo pairs with CUTLASS-style FastDivmod us | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0223-1](../sources/experiences/exp-o-kd-20260519-0223-1.md) | Eliminate the source tensor load entirely by removing the source parameter, beta | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0231-1](../sources/experiences/exp-o-kd-20260519-0231-1.md) | Coarsen the outer loop to process FPP=2 fragments per iteration, staging all FPP | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0234-1](../sources/experiences/exp-o-kd-20260519-0234-1.md) | Replace the 128-iteration element-by-element loop with a 4-iteration loop over t | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0235-1](../sources/experiences/exp-o-kd-20260519-0235-1.md) | Replace the 128-iteration sub-byte element loop with a 4-iteration word-level lo | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0236-1](../sources/experiences/exp-o-kd-20260519-0236-1.md) | Replace the 128-iteration per-element get/NOT/set loop with a 4-iteration word-l | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0237-1](../sources/experiences/exp-o-kd-20260519-0237-1.md) | Replace the 128-iteration element-wise loop (get/set sub-byte access) with a 4-i | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0247-1](../sources/experiences/exp-o-kd-20260519-0247-1.md) | Replace scalar per-element index-decomposition loop with shared-memory tiling: 1 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0248-1](../sources/experiences/exp-o-kd-20260519-0248-1.md) | Replace scalar per-element processing with shared-memory tiling: 192 threads coo | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0250-1](../sources/experiences/exp-o-kd-20260519-0250-1.md) | Replace the generic scalar kernel with a specialized 3-to-8 channel kernel using | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0251-1](../sources/experiences/exp-o-kd-20260519-0251-1.md) | Replace scalar float loads/stores with float2 vectorized I/O by casting the inpu | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0252-1](../sources/experiences/exp-o-kd-20260519-0252-1.md) | Reinterpret the float pointer as float2 and halve the channel dimensions (c_in/2 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0293-1](../sources/experiences/exp-o-kd-20260519-0293-1.md) | Replace __shfl_sync(0xffffffff, threadIdx.x/32, 0) with a plain threadIdx.x/32 c | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0295-1](../sources/experiences/exp-o-kd-20260519-0295-1.md) | Replace __shfl_sync warp-index broadcast with plain integer division threadIdx.x | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0297-1](../sources/experiences/exp-o-kd-20260519-0297-1.md) | Replace __shfl_sync-based warp index broadcast with direct arithmetic (threadIdx | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0299-1](../sources/experiences/exp-o-kd-20260519-0299-1.md) | Replace __shfl_sync warp shuffle with direct threadIdx.x / 32 computation: since | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0300-1](../sources/experiences/exp-o-kd-20260519-0300-1.md) | Replace the __shfl_sync-based warp index broadcast with direct arithmetic (threa | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0302-1](../sources/experiences/exp-o-kd-20260519-0302-1.md) | Replace __shfl_sync with a __device__ helper canonical_warp_idx() that compiles  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0303-1](../sources/experiences/exp-o-kd-20260519-0303-1.md) | Replace __shfl_sync with a direct threadIdx.x / 32 computation via canonical_war | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0335-1](../sources/experiences/exp-o-kd-20260519-0335-1.md) | Decompose the monolithic fp16-accumulating kernel into three separate kernels: i | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0336-1](../sources/experiences/exp-o-kd-20260519-0336-1.md) | Remove all cudaMemset calls from the warmup and benchmark loops since the write_ | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0356-1](../sources/experiences/exp-o-kd-20260519-0356-1.md) | Consolidate 4 separate half2 loads/stores into single 128-bit LDST128BITS (float | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0399-1](../sources/experiences/exp-o-kd-20260519-0399-1.md) | Process 2 FP16 elements per thread using half2 vectorized loads/stores via reint | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0400-1](../sources/experiences/exp-o-kd-20260519-0400-1.md) | Consolidate four separate half2 loads/stores into single 128-bit LDST128BITS (fl | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0401-1](../sources/experiences/exp-o-kd-20260519-0401-1.md) | Replace scalar half loads/stores with half2 vectorized accesses: load two consec | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0402-1](../sources/experiences/exp-o-kd-20260519-0402-1.md) | Replace 4 separate half2 loads/stores with LDST128BITS (reinterpret_cast<float4> | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0603-1](../sources/experiences/exp-o-kd-20260519-0603-1.md) | Fuse the three separate kernels (compute_neg_indices → gather_from_map → conditi | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0605-1](../sources/experiences/exp-o-kd-20260519-0605-1.md) | Fuse all three operations into a single resolve_future_token_ids_kernel that rea | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0606-1](../sources/experiences/exp-o-kd-20260519-0606-1.md) | Fuse the normalize and scale operations into a single fused_rescale_kernel where | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0623-1](../sources/experiences/exp-o-kd-20260519-0623-1.md) | Issue weight and input global memory loads BEFORE the spin-wait using instructio | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0659-1](../sources/experiences/exp-o-kd-20260519-0659-1.md) | Replace the direct vector copy with a #pragma unroll loop that extracts elements | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0662-1](../sources/experiences/exp-o-kd-20260519-0662-1.md) | Flatten the 2D nested loop into a 1D global-index stride pattern where each thre | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0663-1](../sources/experiences/exp-o-kd-20260519-0663-1.md) | Cache the expert_offsets array into shared memory via cooperative int4-vectorize | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0663-2](../sources/experiences/exp-o-kd-20260519-0663-2.md) | Replace linear scan with binary search over the sorted expert_offsets array, red | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0664-1](../sources/experiences/exp-o-kd-20260519-0664-1.md) | Flatten the 2D row/col loop into a 1D global-index range over numRows * colsPerR | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0667-1](../sources/experiences/exp-o-kd-20260519-0667-1.md) | Replace scalar float loads/stores with float4 (128-bit) vectorized loads/stores  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0669-1](../sources/experiences/exp-o-kd-20260519-0669-1.md) | Fuse the sorted_token_ids padding logic directly into both moe_align_block_size_ | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0670-1](../sources/experiences/exp-o-kd-20260519-0670-1.md) | Fuse the normalize and scale operations into a single rescale_fused_kernel so ea | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0671-1](../sources/experiences/exp-o-kd-20260519-0671-1.md) | Fuse normalization and conditional routed_scaling_factor multiplication into a s | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0676-1](../sources/experiences/exp-o-kd-20260519-0676-1.md) | Replace global flat iteration with static per-expert thread assignment computed  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0678-1](../sources/experiences/exp-o-kd-20260519-0678-1.md) | Use a templated vec_t<T, 8> struct with memcpy-based cast_load to perform 16-byt | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0678-2](../sources/experiences/exp-o-kd-20260519-0678-2.md) | Replace the 128-thread shared-memory tree reduction with a 16-thread warp-shuffl | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0678-3](../sources/experiences/exp-o-kd-20260519-0678-3.md) | Process 16 groups per block using 256 threads (16 threads per group via warp-shu | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0679-1](../sources/experiences/exp-o-kd-20260519-0679-1.md) | Replace scalar half loads with 16-byte vectorized loads via a templated vec_t st | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0679-2](../sources/experiences/exp-o-kd-20260519-0679-2.md) | Replace shared-memory tree reduction with a hardcoded __shfl_xor_sync warp-shuff | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0680-1](../sources/experiences/exp-o-kd-20260519-0680-1.md) | Replace the hardcoded FP8_TYPE alias with a DST_DTYPE template parameter on the  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0685-1](../sources/experiences/exp-o-kd-20260519-0685-1.md) | Double the vector processing width to VEC_SIZE=16 and replace the 8-iteration sc | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0686-1](../sources/experiences/exp-o-kd-20260519-0686-1.md) | Double vector width to VEC_SIZE=16 (fixed for all types) and replace 8 scalar by | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0687-1](../sources/experiences/exp-o-kd-20260519-0687-1.md) | Fix VEC_SIZE to 16 (always 16 FP8 output elements regardless of input type) and  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0715-1](../sources/experiences/exp-o-kd-20260519-0715-1.md) | Track cumulative tile counts across groups with group_total_tiles and head_cta_i | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0741-1](../sources/experiences/exp-o-kd-20260519-0741-1.md) | Replace bool* tree_mask with uint8_t* bit-packed representation where each byte  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0760-1](../sources/experiences/exp-o-kd-20260519-0760-1.md) | Remove the scalar remainder loop entirely and enforce hidden_dim alignment (divi | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0761-1](../sources/experiences/exp-o-kd-20260519-0761-1.md) | Replace scalar loads with flashinfer::vec_t vectorized 16-byte loads (vec_size = | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1082-1](../sources/experiences/exp-o-kd-20260519-1082-1.md) | Replace scalar int32 stores with int4 (Vec) vectorized stores that pack 4 int32  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1084-1](../sources/experiences/exp-o-kd-20260519-1084-1.md) | Pack 4 int32 values into a single Vec (int4) struct and write 16 bytes per store | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1087-1](../sources/experiences/exp-o-kd-20260519-1087-1.md) | Replace scalar per-element load loops and scalar store loops with single pointer | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1089-1](../sources/experiences/exp-o-kd-20260519-1089-1.md) | Replace the scalar per-element loop with a compile-time AlignedArray<T, Vlen> ty | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1101-1](../sources/experiences/exp-o-kd-20260519-1101-1.md) | Replace the bool mask array with a uint8_t bit-packed mask (1 byte per token ins | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1862-1](../sources/experiences/exp-o-kd-20260519-1862-1.md) | Materialize the vector pack into a register-backed local vin_t variable before p | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1863-1](../sources/experiences/exp-o-kd-20260519-1863-1.md) | Materialize the vector pack into a local variable (vin_t tmp = v_in[i]) before p | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1864-1](../sources/experiences/exp-o-kd-20260519-1864-1.md) | Replace raw m with effectiveRows=round_up(m,128) in the grid-size calculation so | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1880-1](../sources/experiences/exp-o-kd-20260519-1880-1.md) | Replace the entire float-domain pipeline with native f16x2 PTX operations: use h | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1881-1](../sources/experiences/exp-o-kd-20260519-1881-1.md) | Eliminate all half↔float conversion round-trips by operating directly on packed  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1893-1](../sources/experiences/exp-o-kd-20260519-1893-1.md) | Eliminate the GPU-side segmented_max_reduction entirely by pre-computing the max | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1894-1](../sources/experiences/exp-o-kd-20260519-1894-1.md) | Pre-compute the FP8 scaling factor on the CPU using a simple loop over the host- | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1907-1](../sources/experiences/exp-o-kd-20260519-1907-1.md) | Pre-compute all division results (sh_ids[i] / top_k) into a second shared memory | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1924-1](../sources/experiences/exp-o-kd-20260519-1924-1.md) | Pass the scalar as a device pointer (const float* d_scale) and dereference it di | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1926-1](../sources/experiences/exp-o-kd-20260519-1926-1.md) | Keep the scale value on the GPU and pass its device pointer directly to the seco | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1927-1](../sources/experiences/exp-o-kd-20260519-1927-1.md) | Keep the scale value on device memory and pass a device pointer (const float* d_ | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1938-1](../sources/experiences/exp-o-kd-20260519-1938-1.md) | Replace the three-operation software path with a single inline PTX ASM instructi | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1939-1](../sources/experiences/exp-o-kd-20260519-1939-1.md) | Convert the runtime bool parameter to a template parameter bool is_scale_inverte | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1939-2](../sources/experiences/exp-o-kd-20260519-1939-2.md) | Replace the software conversion chain with a single PTX inline asm instruction c | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1953-1](../sources/experiences/exp-o-kd-20260519-1953-1.md) | Cast float pointers to P32* (array_t<float,4> with __align__(16)) so the compile | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1954-1](../sources/experiences/exp-o-kd-20260519-1954-1.md) | Replace scalar per-element half loads with 128-bit aligned packed loads using ar | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1968-1](../sources/experiences/exp-o-kd-20260519-1968-1.md) | Replace the host-side round-trip with an on-device GPU kernel that uses a 256-by | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1970-1](../sources/experiences/exp-o-kd-20260519-1970-1.md) | Replace scalar byte loads and stores with uint4 (16-byte) vectorized loads via r | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1970-2](../sources/experiences/exp-o-kd-20260519-1970-2.md) | Precompute a 256-entry byte-level lookup table in CUDA __constant__ memory that  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1980-1](../sources/experiences/exp-o-kd-20260519-1980-1.md) | Cooperatively load all 65 int64_t offsets (520 bytes) into shared memory via __l | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1981-1](../sources/experiences/exp-o-kd-20260519-1981-1.md) | Load the small expert offset array (9 int64_t = 72 bytes) into shared memory via | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1996-1](../sources/experiences/exp-o-kd-20260519-1996-1.md) | Pack adjacent __nv_bfloat16 pairs into __nv_bfloat162 via the {x,y} register-lev | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2047-1](../sources/experiences/exp-o-kd-20260519-2047-1.md) | Introduce adaptive block sizing: when num_tokens >= 256 cap max_block_size at 25 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2118-1](../sources/experiences/exp-o-kd-20260519-2118-1.md) | Move the write-only sorted_token_ids initialization into a separate threadblock  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2151-1](../sources/experiences/exp-o-kd-20260519-2151-1.md) | Fuse both kernels into a single advance_step_flashinfer_kernel where each thread | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2152-1](../sources/experiences/exp-o-kd-20260519-2152-1.md) | Fuse the two separate kernels into a single advance_step_flashinfer_kernel that  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2153-1](../sources/experiences/exp-o-kd-20260519-2153-1.md) | Fuse both kernels into a single advance_step_flashinfer_kernel where each thread | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2160-1](../sources/experiences/exp-o-kd-20260519-2160-1.md) | Replace manual bit-manipulation fp8x2→float2 conversion with the vendor SDK intr | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2162-1](../sources/experiences/exp-o-kd-20260519-2162-1.md) | Replace the entire custom hip_fp8 struct and its MI300-specific inline asm conve | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2177-1](../sources/experiences/exp-o-kd-20260519-2177-1.md) | Guard the entire allocation, memset, and kernel launch with a needs_alignment co | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2178-1](../sources/experiences/exp-o-kd-20260519-2178-1.md) | Guard the cudaMalloc+cudaMemset allocation and getMIndicesKernel launch behind a | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2179-1](../sources/experiences/exp-o-kd-20260519-2179-1.md) | Move both align_expert_first_token_offset allocation (torch::zeros_like) and get | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2183-1](../sources/experiences/exp-o-kd-20260519-2183-1.md) | Fuse absmax reduction and quantization into a single per-token kernel where each | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2190-1](../sources/experiences/exp-o-kd-20260519-2190-1.md) | Merge min and max tracking into a single MinMax struct and perform one BlockRedu | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2190-2](../sources/experiences/exp-o-kd-20260519-2190-2.md) | Use vectorize_with_alignment<16> to process 16 elements per vector iteration, co | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2192-1](../sources/experiences/exp-o-kd-20260519-2192-1.md) | Replace the scalar stride loop with a vectorized loop using vec_n_t<float,4> (16 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2193-1](../sources/experiences/exp-o-kd-20260519-2193-1.md) | Replace scalar stride loop with DefaultVecOp<4>-based vectorized loop using rein | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2194-1](../sources/experiences/exp-o-kd-20260519-2194-1.md) | Replace scalar stride loop with vectorize_with_alignment<4> that computes pointe | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2215-1](../sources/experiences/exp-o-kd-20260519-2215-1.md) | Pre-compute the aligned expert prefix offsets on the host into a dedicated array | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2216-1](../sources/experiences/exp-o-kd-20260519-2216-1.md) | Move the expert-aligned offset prefix-sum accumulation to host-side pre-computat | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2224-1](../sources/experiences/exp-o-kd-20260519-2224-1.md) | Fuse the fp8→half→float conversion and scale multiplication into a single kernel | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2225-1](../sources/experiences/exp-o-kd-20260519-2225-1.md) | Fuse the pre-scale division and half-to-fp8 conversion into a single kernel: rea | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2229-1](../sources/experiences/exp-o-kd-20260519-2229-1.md) | Fuse the absmax computation and quantization into a single kernel that computes  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2230-1](../sources/experiences/exp-o-kd-20260519-2230-1.md) | Fuse absmax computation and quantization into a single kernel that computes per- | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2230-2](../sources/experiences/exp-o-kd-20260519-2230-2.md) | Replace per-element FP division (/ scale) with multiplication by precomputed rec | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2231-1](../sources/experiences/exp-o-kd-20260519-2231-1.md) | Fuse the two-pass quantization into a single kernel that computes per-token absm | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2234-1](../sources/experiences/exp-o-kd-20260519-2234-1.md) | Change the kernel to accept a device pointer (const scale_type* scale_ptr) and d | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2235-1](../sources/experiences/exp-o-kd-20260519-2235-1.md) | Changed the scale parameter from float (host scalar) to torch::Tensor const& (de | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2285-1](../sources/experiences/exp-o-kd-20260519-2285-1.md) | Replace scalar byte-by-byte load/store with uint4 vectorized 16-byte load/store: | optimization | sm90 | cuda-cpp |

## embedding

| ID | Title | Type | Architectures | Languages |
|----|-------|------|--------------|-----------|
| [exp-a-kd-20260519-0479-1](../sources/experiences/exp-a-kd-20260519-0479-1.md) | Attempt to vectorize each thread to process 4 consecutive f32 elements (f32x4),  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0480-1](../sources/experiences/exp-a-kd-20260519-0480-1.md) | Replace 4 scalar float load/store pairs with a single 128-bit packed load/store  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0481-1](../sources/experiences/exp-a-kd-20260519-0481-1.md) | Thread coarsening attempts to reduce thread count by 8x and have each thread iss | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0482-1](../sources/experiences/exp-a-kd-20260519-0482-1.md) | Replace 8 individual scalar half load/store pairs with a single 128-bit packed l | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0787-1](../sources/experiences/exp-a-kd-20260519-0787-1.md) | Fuse the three sequential kernels into a single-pass kernel that reads input_ids | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0788-1](../sources/experiences/exp-a-kd-20260519-0788-1.md) | Fuse the three separate kernels into a single-pass kernel that reads input_ids o | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0789-1](../sources/experiences/exp-a-kd-20260519-0789-1.md) | Fuse three separate kernels into a single-pass resolve_future_token_ids_kernel t | analysis | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0363-1](../sources/experiences/exp-o-kd-20260519-0363-1.md) | Replace 4 scalar f32 load/store pairs with a single 128-bit packed load/store vi | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0364-1](../sources/experiences/exp-o-kd-20260519-0364-1.md) | Replace 8 scalar half load/store pairs with a single 128-bit packed transaction  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0365-1](../sources/experiences/exp-o-kd-20260519-0365-1.md) | Use the LDST128BITS macro (reinterpret_cast<float4*>) to perform a single 128-bi | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0366-1](../sources/experiences/exp-o-kd-20260519-0366-1.md) | Replace eight scalar half load/store assignments with two 128-bit packed transac | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0604-1](../sources/experiences/exp-o-kd-20260519-0604-1.md) | Fuse all three kernels into a single resolve_future_token_ids_kernel that reads  | optimization | sm90 | cuda-cpp |

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

## gather-scatter

| ID | Title | Type | Architectures | Languages |
|----|-------|------|--------------|-----------|
| [exp-i-kd-20260519-2396-1](../sources/experiences/exp-i-kd-20260519-2396-1.md) | Compute per-batch base pointers via blockIdx.z offset, then use a grid-stride lo | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2397-1](../sources/experiences/exp-i-kd-20260519-2397-1.md) | Use blockIdx.z for batch dimension offset with per-batch base pointers, grid-str | implementation | sm90 | cuda-cpp, cute-dsl |

## gemm

| ID | Title | Type | Architectures | Languages |
|----|-------|------|--------------|-----------|
| [exp-a-20260325-170222-ee5351e3](../sources/experiences/exp-a-20260325-170222-ee5351e3.md) | ## Task
Write a CUDA kernel for Q4_0 quantized GEMM that achieves much better performance than the baseline (currently o | analysis | sm90 | cuda-cpp |
| [exp-a-20260325-172649-39d03bc4](../sources/experiences/exp-a-20260325-172649-39d03bc4.md) | ## Task
Run the KernelEvalPlus unified test runner on the existing QG_55 r1 v2 kernel to compile and benchmark it

## Go | analysis | sm90 | cuda-cpp |
| [exp-a-20260328-074205-3e7f549b](../sources/experiences/exp-a-20260328-074205-3e7f549b.md) | 实现一个量化的GEMM算子:
            - weight是Q4_0格式
            - activation是Q8_1格式
            - 输入activation是fp32需要量化
            - 输出需要反量化回fp32 | analysis | sm90 | cuda-cpp |
| [exp-a-20260526-200006-cublas-gemm-convergence](../sources/experiences/exp-a-20260526-200006-cublas-gemm-convergence.md) | SOL-ExecBench GEMM: optimization convergence — cuBLAS 0.99x+ means switch to cublasLt with proper config | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0002](../sources/experiences/exp-a-kd-20260518-0002.md) | 8-bit weight dot product: half2 vs FP32 accumulation for quantized GEMM | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0012](../sources/experiences/exp-a-kd-20260518-0012.md) | gemm_reorder | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0039](../sources/experiences/exp-a-kd-20260518-0039.md) | b2b_gemm_f16_sm80_large | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0040](../sources/experiences/exp-a-kd-20260518-0040.md) | pipelining_blocking | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0043](../sources/experiences/exp-a-kd-20260518-0043.md) | pipeline_gemm_2048 | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-0044](../sources/experiences/exp-a-kd-20260518-0044.md) | b2b_gemm_unfused | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-0067](../sources/experiences/exp-a-kd-20260518-0067.md) | conv3d_fprop_small | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0080](../sources/experiences/exp-a-kd-20260518-0080.md) | Replace modulo/division index computation with direct linear offset (index = ite | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-0091](../sources/experiences/exp-a-kd-20260518-0091.md) | Replace pointers_ += offset (array decay) with pointers_[i] += offset inside the | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-0092](../sources/experiences/exp-a-kd-20260518-0092.md) | Scale tile offsets by tile dimensions: row offset multiplied by Shape::kRow, col | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-0094](../sources/experiences/exp-a-kd-20260518-0094.md) | smem_transfer | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0097](../sources/experiences/exp-a-kd-20260518-0097.md) | b2b_gemm_standard | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-0104](../sources/experiences/exp-a-kd-20260518-0104.md) | Add the missing tile_m * ldr row-stride term to the bias vector pointer offset,  | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-0107](../sources/experiences/exp-a-kd-20260518-0107.md) | streamk_broadcast_1024x1024x4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0108](../sources/experiences/exp-a-kd-20260518-0108.md) | Remove the redundant epilogue __syncthreads() (and in real CUTLASS: cp_async_fen | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0109](../sources/experiences/exp-a-kd-20260518-0109.md) | long_k | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-0117](../sources/experiences/exp-a-kd-20260518-0117.md) | split_keys | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0126](../sources/experiences/exp-a-kd-20260518-0126.md) | remat_heavy | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0128](../sources/experiences/exp-a-kd-20260518-0128.md) | fused_dsij_wide | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0129](../sources/experiences/exp-a-kd-20260518-0129.md) | dropout_smem | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0136](../sources/experiences/exp-a-kd-20260518-0136.md) | smem_layout_correctness | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0137](../sources/experiences/exp-a-kd-20260518-0137.md) | Parameterize InstructionShape as a template parameter (InstructionShape_) so the | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-0140](../sources/experiences/exp-a-kd-20260518-0140.md) | Parameterize InstructionShape as a template argument (instantiated at 16x16) and | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-0144](../sources/experiences/exp-a-kd-20260518-0144.md) | sm80_fp16_vs_sm89_fp8_coop_gemm | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0147](../sources/experiences/exp-a-kd-20260518-0147.md) | bf16_m16n8k8 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0148](../sources/experiences/exp-a-kd-20260518-0148.md) | bf16_m16n8k16 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0149](../sources/experiences/exp-a-kd-20260518-0149.md) | f16_m16n8k16 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0150](../sources/experiences/exp-a-kd-20260518-0150.md) | f64_m8n8k4 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0153](../sources/experiences/exp-a-kd-20260518-0153.md) | Add an explicit kClearLastStage step that zeroes the next-stage SMEM slot after  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0157](../sources/experiences/exp-a-kd-20260518-0157.md) | gemm_m256_n256_k4096_split8 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0160](../sources/experiences/exp-a-kd-20260518-0160.md) | pdl_chained_gemm | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0162](../sources/experiences/exp-a-kd-20260518-0162.md) | pdl_launch_at_exit | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0164](../sources/experiences/exp-a-kd-20260518-0164.md) | Add an sm_occupancy > 1 guard before the modulo-based SK wave formation check so | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-0165](../sources/experiences/exp-a-kd-20260518-0165.md) | Add sm_occupancy > 1 guard to the conditional branch so the SK wave formation pa | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-0167](../sources/experiences/exp-a-kd-20260518-0167.md) | Replace wave-based ceiling-division rounding with a simpler two-branch heuristic | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0170](../sources/experiences/exp-a-kd-20260518-0170.md) | half_t_even8 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0172](../sources/experiences/exp-a-kd-20260518-0172.md) | Replace the hardcoded % 4 divisibility check with a dynamically computed divisor | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-0186](../sources/experiences/exp-a-kd-20260518-0186.md) | gemm_like | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0188](../sources/experiences/exp-a-kd-20260518-0188.md) | gemm_like_warp_select | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0193](../sources/experiences/exp-a-kd-20260518-0193.md) | gemm_like_warp_idx | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0195](../sources/experiences/exp-a-kd-20260518-0195.md) | warp_idx_compute | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-0210](../sources/experiences/exp-a-kd-20260518-0210.md) | medium | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0225](../sources/experiences/exp-a-kd-20260518-0225.md) | f32_vs_f32x4 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0227](../sources/experiences/exp-a-kd-20260518-0227.md) | f16_vs_f16x2 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0230](../sources/experiences/exp-a-kd-20260518-0230.md) | f16x2_vs_f16x8_pack_batched | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0291](../sources/experiences/exp-a-kd-20260518-0291.md) | hgemm_cublas_small_256 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0292](../sources/experiences/exp-a-kd-20260518-0292.md) | hgemm_cublas_medium_512 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0293](../sources/experiences/exp-a-kd-20260518-0293.md) | hgemm_cublas_large_1024 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0299](../sources/experiences/exp-a-kd-20260518-0299.md) | hgemm_256 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0304](../sources/experiences/exp-a-kd-20260518-0304.md) | hgemm_1024 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0306](../sources/experiences/exp-a-kd-20260518-0306.md) | hgemm_512 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0332](../sources/experiences/exp-a-kd-20260518-0332.md) | Trim shared memory to the exact working-set dimensions (kRows*kK + kK*kCols), sp | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0344](../sources/experiences/exp-a-kd-20260518-0344.md) | sgemm_1024x1024x1024 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0345](../sources/experiences/exp-a-kd-20260518-0345.md) | sgemm_4096x4096x4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0353](../sources/experiences/exp-a-kd-20260518-0353.md) | M256_K16 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0374](../sources/experiences/exp-a-kd-20260518-0374.md) | large_m_256n8192k4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0375](../sources/experiences/exp-a-kd-20260518-0375.md) | large_m_512n4096k4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0446](../sources/experiences/exp-a-kd-20260518-0446.md) | shmem_overlap_tiled | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0524](../sources/experiences/exp-a-kd-20260518-0524.md) | Replace global singleton handle with an external handle parameter passed as func | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0529](../sources/experiences/exp-a-kd-20260518-0529.md) | Enabled BLOCK_SWIZZLE=true and introduced a 3D grid launch where blockIdx.z sele | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0542](../sources/experiences/exp-a-kd-20260518-0542.md) | Replace scalar half loads with half2 (f16x4) vectorized loads, processing 4 half | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0543](../sources/experiences/exp-a-kd-20260518-0543.md) | Replace scalar half loads with half2 vectorized (f16x4) loads: each thread loads | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0577](../sources/experiences/exp-a-kd-20260518-0577.md) | routing_64experts | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0578](../sources/experiences/exp-a-kd-20260518-0578.md) | routing_256experts | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0588](../sources/experiences/exp-a-kd-20260518-0588.md) | moe_dispatch_k64 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0590](../sources/experiences/exp-a-kd-20260518-0590.md) | stream_hoist_pipeline | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0592](../sources/experiences/exp-a-kd-20260518-0592.md) | small_m_32 | analysis | sm120 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-0634](../sources/experiences/exp-a-kd-20260518-0634.md) | dot22_normal_range | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0635](../sources/experiences/exp-a-kd-20260518-0635.md) | dot22_overflow_safe | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0668](../sources/experiences/exp-a-kd-20260518-0668.md) | dot8_half2acc_vs_fp32acc | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0715](../sources/experiences/exp-a-kd-20260518-0715.md) | dot_float4 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0716](../sources/experiences/exp-a-kd-20260518-0716.md) | dot_float8 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0762](../sources/experiences/exp-a-kd-20260518-0762.md) | half2_kU4B8 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0764](../sources/experiences/exp-a-kd-20260518-0764.md) | small_m_gemm | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0765](../sources/experiences/exp-a-kd-20260518-0765.md) | msplit_small_n | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0825](../sources/experiences/exp-a-kd-20260518-0825.md) | large_m_tile128k | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-0827](../sources/experiences/exp-a-kd-20260518-0827.md) | small_m_tile32 | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-0840](../sources/experiences/exp-a-kd-20260518-0840.md) | tokens_1_256ep | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0841](../sources/experiences/exp-a-kd-20260518-0841.md) | tokens_8_256ep | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0842](../sources/experiences/exp-a-kd-20260518-0842.md) | tokens_16_256ep | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0844](../sources/experiences/exp-a-kd-20260518-0844.md) | tokens_8_384ep | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0911](../sources/experiences/exp-a-kd-20260518-0911.md) | bf16_scale_4k | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-0912](../sources/experiences/exp-a-kd-20260518-0912.md) | bf16_scale_64k | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-0920](../sources/experiences/exp-a-kd-20260518-0920.md) | medium_m_32_n_512_k_256 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0923](../sources/experiences/exp-a-kd-20260518-0923.md) | small_m_swap | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-0924](../sources/experiences/exp-a-kd-20260518-0924.md) | edge_m_64 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0925](../sources/experiences/exp-a-kd-20260518-0925.md) | small_m_4 | analysis | sm120 | cuda-cpp |
| [exp-a-kd-20260518-0926](../sources/experiences/exp-a-kd-20260518-0926.md) | tiny_m_1 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0927](../sources/experiences/exp-a-kd-20260518-0927.md) | m3_non_aligned | analysis | sm120 | cuda-cpp |
| [exp-a-kd-20260518-0953](../sources/experiences/exp-a-kd-20260518-0953.md) | bf16_m512_n2048_k1024 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0958](../sources/experiences/exp-a-kd-20260518-0958.md) | m3_n4096_k4096_fp16 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0959](../sources/experiences/exp-a-kd-20260518-0959.md) | m7_n4096_k4096_fp16 | analysis | sm100 | cuda-cpp |
| [exp-a-kd-20260518-0963](../sources/experiences/exp-a-kd-20260518-0963.md) | pipeline_reorder | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0978](../sources/experiences/exp-a-kd-20260518-0978.md) | sparse_mma | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0996](../sources/experiences/exp-a-kd-20260518-0996.md) | sm64_large_tile | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0997](../sources/experiences/exp-a-kd-20260518-0997.md) | sm128_m128_large_tile | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1015](../sources/experiences/exp-a-kd-20260518-1015.md) | reduce_4slice | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1078](../sources/experiences/exp-a-kd-20260518-1078.md) | silu_fused_bf16 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1079](../sources/experiences/exp-a-kd-20260518-1079.md) | fp8_inv_scale | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1085](../sources/experiences/exp-a-kd-20260518-1085.md) | dp4a_guard | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1090](../sources/experiences/exp-a-kd-20260518-1090.md) | small_m_8exp | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-1100](../sources/experiences/exp-a-kd-20260518-1100.md) | small_n_64 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1101](../sources/experiences/exp-a-kd-20260518-1101.md) | small_n_128_large_k | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1104](../sources/experiences/exp-a-kd-20260518-1104.md) | streamk_balanced | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1106](../sources/experiences/exp-a-kd-20260518-1106.md) | dispatch_balanced | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1107](../sources/experiences/exp-a-kd-20260518-1107.md) | dispatch_tall_skinny | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1108](../sources/experiences/exp-a-kd-20260518-1108.md) | tokens_1 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1151](../sources/experiences/exp-a-kd-20260518-1151.md) | small_m_dispatch | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-1152](../sources/experiences/exp-a-kd-20260518-1152.md) | large_n_dispatch | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-1158](../sources/experiences/exp-a-kd-20260518-1158.md) | sm89_fp8_gate | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-1174](../sources/experiences/exp-a-kd-20260518-1174.md) | int4_half_1M | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1175](../sources/experiences/exp-a-kd-20260518-1175.md) | int4_int8_1M | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1183](../sources/experiences/exp-a-kd-20260518-1183.md) | small_m_nobias | analysis | sm100 | cuda-cpp |
| [exp-a-kd-20260518-1237](../sources/experiences/exp-a-kd-20260518-1237.md) | small_m_small_n | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1238](../sources/experiences/exp-a-kd-20260518-1238.md) | medium_m_medium_n | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1253](../sources/experiences/exp-a-kd-20260518-1253.md) | experts_8 | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-1303](../sources/experiences/exp-a-kd-20260518-1303.md) | block16_vs_block32_medium_seq | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1304](../sources/experiences/exp-a-kd-20260518-1304.md) | block16_vs_block32_long_seq | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1317](../sources/experiences/exp-a-kd-20260518-1317.md) | dispatch_m1 | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-1318](../sources/experiences/exp-a-kd-20260518-1318.md) | dispatch_m8 | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-1320](../sources/experiences/exp-a-kd-20260518-1320.md) | dispatch_m32 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1326](../sources/experiences/exp-a-kd-20260518-1326.md) | epilogue_int32_accum | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-1327](../sources/experiences/exp-a-kd-20260518-1327.md) | stride_permute | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-1328](../sources/experiences/exp-a-kd-20260518-1328.md) | schedule_pingpong | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-1330](../sources/experiences/exp-a-kd-20260518-1330.md) | square_balanced | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1336](../sources/experiences/exp-a-kd-20260518-1336.md) | m64_n4096_k4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1337](../sources/experiences/exp-a-kd-20260518-1337.md) | m16_n4096_k4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1338](../sources/experiences/exp-a-kd-20260518-1338.md) | m32_n1280_k4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1339](../sources/experiences/exp-a-kd-20260518-1339.md) | m16_n1280_k4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1340](../sources/experiences/exp-a-kd-20260518-1340.md) | m8_n4096_k4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1343](../sources/experiences/exp-a-kd-20260518-1343.md) | m8_n4096_k4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1345](../sources/experiences/exp-a-kd-20260518-1345.md) | m32_n1280_k4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1351](../sources/experiences/exp-a-kd-20260518-1351.md) | n_dispatch | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-1381](../sources/experiences/exp-a-kd-20260518-1381.md) | fp16_mma_single_vs_decomposed | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1382](../sources/experiences/exp-a-kd-20260518-1382.md) | fp16_mma_repeated_single_vs_decomposed | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1383](../sources/experiences/exp-a-kd-20260518-1383.md) | int8_mma_k32_single_vs_fourway | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1384](../sources/experiences/exp-a-kd-20260518-1384.md) | int8_mma_k32_repeated_single_vs_fourway | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1385](../sources/experiences/exp-a-kd-20260518-1385.md) | mma_4warp_8acc | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1400](../sources/experiences/exp-a-kd-20260518-1400.md) | fuse_global_scale | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1420](../sources/experiences/exp-a-kd-20260518-1420.md) | small_batch_m1 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1421](../sources/experiences/exp-a-kd-20260518-1421.md) | small_batch_m8 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1474](../sources/experiences/exp-a-kd-20260518-1474.md) | large_m_256 | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-1483](../sources/experiences/exp-a-kd-20260518-1483.md) | contiguous_gemm_1024x512x128 | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-1484](../sources/experiences/exp-a-kd-20260518-1484.md) | contiguous_gemm_256x128x64 | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-1493](../sources/experiences/exp-a-kd-20260518-1493.md) | lop3_dequant_int4 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0002-1](../sources/experiences/exp-a-kd-20260519-0002-1.md) | Add a conditional guard is_accumulator_needed = K > 0 that branches between the  | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0004-1](../sources/experiences/exp-a-kd-20260519-0004-1.md) | Guard both the MMA loop entry and the producer state advancement with if (k_tile | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0005-1](../sources/experiences/exp-a-kd-20260519-0005-1.md) | Guard both the MMA loop and the pipeline state increment with `if (k_tile_count  | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0010-1](../sources/experiences/exp-a-kd-20260519-0010-1.md) | Reorder the shared memory layout so that all 16 INT4 elements owned by one threa | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0012-1](../sources/experiences/exp-a-kd-20260519-0012-1.md) | Reorder the loop to issue mma_sync first with the current fragment, then prefetc | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0038-1](../sources/experiences/exp-a-kd-20260519-0038-1.md) | Fuse both GEMMs into a single B2bGemm kernel using CUTLASS's back-to-back GEMM A | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0039-1](../sources/experiences/exp-a-kd-20260519-0039-1.md) | Fuse both GEMMs into a single CUTLASS B2bGemm kernel where GEMM0's output stays  | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0040-1](../sources/experiences/exp-a-kd-20260519-0040-1.md) | Replace single-stage blocking copy with 3-stage cp.async pipeline: a prologue is | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0041-1](../sources/experiences/exp-a-kd-20260519-0041-1.md) | Introduce cp.async.cg (cache-global, bypass L1) for B operand async copies so th | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0042-1](../sources/experiences/exp-a-kd-20260519-0042-1.md) | Double-buffer shared memory (2x allocation) and attempt to overlap loading the n | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0043-1](../sources/experiences/exp-a-kd-20260519-0043-1.md) | Double-buffer shared memory into 2 stages (sA[2][BM][BK], sB[2][BK][BN]), load f | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0044-1](../sources/experiences/exp-a-kd-20260519-0044-1.md) | Fuse both GEMMs into a single kernel so accum0 (A*B0 result) stays in registers  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0055-1](../sources/experiences/exp-a-kd-20260519-0055-1.md) | Doubling kFragmentsPerIteration from 1 to 2 halves the __syncthreads() count fro | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0056-1](../sources/experiences/exp-a-kd-20260519-0056-1.md) | Add a float-specific template specialization setting kFragmentsPerIteration=2, w | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0057-1](../sources/experiences/exp-a-kd-20260519-0057-1.md) | Propagate DefaultIterators::kFragmentsPerIteration to the epilogue when kPartiti | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0059-1](../sources/experiences/exp-a-kd-20260519-0059-1.md) | Replace the runtime beta check with a compile-time bool template parameter (Sour | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0060-1](../sources/experiences/exp-a-kd-20260519-0060-1.md) | Skip the beta*source multiply entirely under NoBetaScaling by directly assigning | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0064-1](../sources/experiences/exp-a-kd-20260519-0064-1.md) | Specialize the epilogue for OnlyAlphaScaling by removing the source_in parameter | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0068-1](../sources/experiences/exp-a-kd-20260519-0068-1.md) | Batch all fragments into a single iteration (FragmentsPerIteration=2) to reduce  | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0069-1](../sources/experiences/exp-a-kd-20260519-0069-1.md) | Batch all 4 fragments into a single 34.8KB shared memory buffer (4x larger) to c | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0070-1](../sources/experiences/exp-a-kd-20260519-0070-1.md) | Batch multiple fragments per barrier pair (FragmentsPerPartition=2): outer loop  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0071-1](../sources/experiences/exp-a-kd-20260519-0071-1.md) | Double FragmentsPerPartition from 1 to 2, allocating 2x SMEM (1024 floats) and p | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0079-1](../sources/experiences/exp-a-kd-20260519-0079-1.md) | Use compute_source_not_needed_() path that skips all source-related global memor | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0080-1](../sources/experiences/exp-a-kd-20260519-0080-1.md) | Replace modulo/division index computation with direct multiplication (index = it | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0083-1](../sources/experiences/exp-a-kd-20260519-0083-1.md) | Replace the C++ if-guarded store with an explicit PTX inline asm predicated stor | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0090-1](../sources/experiences/exp-a-kd-20260519-0090-1.md) | Insert the missing kRow multiplier into the row offset computation so the pointe | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0091-1](../sources/experiences/exp-a-kd-20260519-0091-1.md) | Replace the array-decay offset application (pointers_ += offset, which only touc | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0092-1](../sources/experiences/exp-a-kd-20260519-0092-1.md) | Scale tile offsets by tile dimensions: multiply row offset by Shape::kRow and co | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0093-1](../sources/experiences/exp-a-kd-20260519-0093-1.md) | Replace the Coord2Int extent_ member with a single int extent_row_ (4 bytes), el | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0094-1](../sources/experiences/exp-a-kd-20260519-0094-1.md) | Centralize the scale/bias epilogue: write GEMM0 accumulator to shared memory wit | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0095-1](../sources/experiences/exp-a-kd-20260519-0095-1.md) | Apply scale/bias once in a centralized epilogue pass over the M*K1 accumulator e | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0096-1](../sources/experiences/exp-a-kd-20260519-0096-1.md) | Replace two separate CUTLASS Gemm kernels with a single B2bGemm using register-f | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0097-1](../sources/experiences/exp-a-kd-20260519-0097-1.md) | Fusing both GEMMs into a single cutlass::gemm::device::B2bGemm kernel that keeps | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0104-1](../sources/experiences/exp-a-kd-20260519-0104-1.md) | Add the missing tile_m * ldr row-stride offset to the vector pointer computation | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0107-1](../sources/experiences/exp-a-kd-20260519-0107-1.md) | Replace GemmIdentityThreadblockSwizzle with ThreadblockSwizzleStreamK to split K | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0108-1](../sources/experiences/exp-a-kd-20260519-0108-1.md) | Remove the epilogue synchronization barrier entirely: the last __syncthreads() i | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0109-1](../sources/experiences/exp-a-kd-20260519-0109-1.md) | Remove the epilogue __syncthreads() since the final mainloop iteration already c | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0110-1](../sources/experiences/exp-a-kd-20260519-0110-1.md) | Replace 4 individual uint32_t pointer dereferences with a single ldmatrix.x4.m8n | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0125-1](../sources/experiences/exp-a-kd-20260519-0125-1.md) | Replace simple threadIdx register reads with warp_uniform_func (shfl_sync broadc | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0126-1](../sources/experiences/exp-a-kd-20260519-0126-1.md) | Rematerialize thread IDs between pipeline stages via a lambda that recomputes wa | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0137-1](../sources/experiences/exp-a-kd-20260519-0137-1.md) | Parameterize InstructionShape as a template parameter, enabling MatrixShape<16,1 | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0138-1](../sources/experiences/exp-a-kd-20260519-0138-1.md) | Replace the triple-nested unrolled loop with conditional branch by direct O(1) i | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0139-1](../sources/experiences/exp-a-kd-20260519-0139-1.md) | Replace the triple-nested loop and conditional match with three direct integer d | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0140-1](../sources/experiences/exp-a-kd-20260519-0140-1.md) | Consolidate two separate ldmatrix.x4 calls (via repeated load()+operator++) into | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0144-1](../sources/experiences/exp-a-kd-20260519-0144-1.md) | Replace SM80 FP16 mma.sync m16n8k16 with SM89 FP8 mma.sync m16n8k32, which doubl | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0145-1](../sources/experiences/exp-a-kd-20260519-0145-1.md) | Replace SM80 FP16 m16n8k16 MMA with SM89 FP8 m16n8k32 MMA that doubles the K dim | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0146-1](../sources/experiences/exp-a-kd-20260519-0146-1.md) | Add a kFactor==8 branch that computes factor_in_partition from PartitionShape/Ti | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0147-1](../sources/experiences/exp-a-kd-20260519-0147-1.md) | Change the C/D operand pointers from uint32_t* to float* and the corresponding i | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0148-1](../sources/experiences/exp-a-kd-20260519-0148-1.md) | Change C/D operand pointers from uint32_t* to float* and asm constraints from "r | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0149-1](../sources/experiences/exp-a-kd-20260519-0149-1.md) | Change the C/D accumulator operands from uint32_t* with "r" (integer register) c | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0150-1](../sources/experiences/exp-a-kd-20260519-0150-1.md) | Replace uint64_t types and "l" register constraints with native double types and | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0153-1](../sources/experiences/exp-a-kd-20260519-0153-1.md) | Add kClearLastStage pattern: explicitly zero the next-stage SMEM slot (the stage | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0156-1](../sources/experiences/exp-a-kd-20260519-0156-1.md) | Split the K=2048 dimension into 4 slices of K=512 and launch 4 gemm_partial kern | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0157-1](../sources/experiences/exp-a-kd-20260519-0157-1.md) | Split the K=4096 dimension into 8 slices of K_len=512, launch 8 gemm_partial ker | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0160-1](../sources/experiences/exp-a-kd-20260519-0160-1.md) | Insert cudaStreamWaitEvent between consecutive chained kernels to simulate CUTLA | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0162-1](../sources/experiences/exp-a-kd-20260519-0162-1.md) | Introduce a CUDA event recorded at the work-exhaustion point (after the GEMM ker | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0164-1](../sources/experiences/exp-a-kd-20260519-0164-1.md) | Add an `sm_occupancy > 1` guard to the modulo-based SK wave formation branch so  | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0165-1](../sources/experiences/exp-a-kd-20260519-0165-1.md) | Add an sm_occupancy > 1 guard to the SK-wave branch condition so that it only fi | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0166-1](../sources/experiences/exp-a-kd-20260519-0166-1.md) | Replace occupancy-rounded waveset ceiling division with fast_max(work_blocks, av | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0167-1](../sources/experiences/exp-a-kd-20260519-0167-1.md) | Replace waveset-rounding heuristic with a two-branch approach: if work_blocks is | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0172-1](../sources/experiences/exp-a-kd-20260519-0172-1.md) | Replace the hardcoded % 4 divisibility check with a dynamically computed divisor | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0186-1](../sources/experiences/exp-a-kd-20260519-0186-1.md) | Replace __shfl_sync-based warp index computation with canonical_warp_idx() (plai | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0188-1](../sources/experiences/exp-a-kd-20260519-0188-1.md) | Replace __shfl_sync warp-index broadcast with a __forceinline__ device function  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0193-1](../sources/experiences/exp-a-kd-20260519-0193-1.md) | Replace __shfl_sync warp-index broadcast with a __forceinline__ device function  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0195-1](../sources/experiences/exp-a-kd-20260519-0195-1.md) | Replace __shfl_sync-based warp index broadcast with direct arithmetic (threadIdx | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0322-1](../sources/experiences/exp-a-kd-20260519-0322-1.md) | Fuse both GEMM accumulators and the SiLU-gated multiply into a single kernel tha | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0323-1](../sources/experiences/exp-a-kd-20260519-0323-1.md) | Fusing all three kernels into a single fused_dual_gemm_kernel that computes both | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0332-1](../sources/experiences/exp-a-kd-20260519-0332-1.md) | Right-size shared memory to the exact working set (kRows*kK + kK*kCols = 32 KB,  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0523-1](../sources/experiences/exp-a-kd-20260519-0523-1.md) | Pass the cuBLAS handle as an explicit function parameter created once at applica | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0524-1](../sources/experiences/exp-a-kd-20260519-0524-1.md) | Refactor to pass the cuBLAS handle as an explicit parameter, removing the global | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0525-1](../sources/experiences/exp-a-kd-20260519-0525-1.md) | Refactor to pass cublasHandle_t as an explicit parameter and use local alpha/bet | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0526-1](../sources/experiences/exp-a-kd-20260519-0526-1.md) | Block swizzle remaps thread-block IDs via a 3D grid (gridDim.z = N_SWIZZLE group | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0527-1](../sources/experiences/exp-a-kd-20260519-0527-1.md) | Enable BLOCK_SWIZZLE to launch a 3D grid where N_SWIZZLE z-slices remap adjacent | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0528-1](../sources/experiences/exp-a-kd-20260519-0528-1.md) | Enable BLOCK_SWIZZLE=true and restructure the launch grid from 2D to 3D, interle | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0529-1](../sources/experiences/exp-a-kd-20260519-0529-1.md) | Enable block-level swizzle (BLOCK_SWIZZLE=true) to interleave thread blocks acro | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0530-1](../sources/experiences/exp-a-kd-20260519-0530-1.md) | Change BLOCK_SWIZZLE from false to true and launch with a 3D grid (gridDim.z = N | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0531-1](../sources/experiences/exp-a-kd-20260519-0531-1.md) | Replace B matrix shared-memory padding (B_PAD=8) with XOR-based swizzle address  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0532-1](../sources/experiences/exp-a-kd-20260519-0532-1.md) | Replace B_PAD=8 padding with XOR permutation swizzle pattern (swizzle_permuted_B | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0533-1](../sources/experiences/exp-a-kd-20260519-0533-1.md) | Replace B smem padding (B_PAD=8) with XOR-permuted swizzle addressing (swizzle_p | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0534-1](../sources/experiences/exp-a-kd-20260519-0534-1.md) | Enable BLOCK_SWIZZLE=true to switch from a 2D grid to a 3D grid that reorders bl | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0535-1](../sources/experiences/exp-a-kd-20260519-0535-1.md) | Enable block-level grid swizzle by switching to a 3D grid with interleaving stri | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0536-1](../sources/experiences/exp-a-kd-20260519-0536-1.md) | Changing BLOCK_SWIZZLE from false to true with stride=2048 switches from a 2D gr | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0537-1](../sources/experiences/exp-a-kd-20260519-0537-1.md) | Enable WARP_SWIZZLE template parameter to alternate j iteration direction for od | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0538-1](../sources/experiences/exp-a-kd-20260519-0538-1.md) | Enable WARP_SWIZZLE template parameter to alternate MMA iteration direction for  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0539-1](../sources/experiences/exp-a-kd-20260519-0539-1.md) | Enable WARP_SWIZZLE (template param true) so that odd i-rows reverse their j ite | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0541-1](../sources/experiences/exp-a-kd-20260519-0541-1.md) | Replace 4 scalar half iterations with 1 vectorized iteration using half2 loads ( | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0543-1](../sources/experiences/exp-a-kd-20260519-0543-1.md) | Replace scalar half loads with half2 vectorized loads (f16x4 pattern), loading 4 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0564-1](../sources/experiences/exp-a-kd-20260519-0564-1.md) | Apply block tiling with K-dimension slicing: each 32x32 thread block cooperative | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0565-1](../sources/experiences/exp-a-kd-20260519-0565-1.md) | Thread tiling (8x8 per thread) with float4 vectorized loads and larger 128x128 b | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0566-1](../sources/experiences/exp-a-kd-20260519-0566-1.md) | Transpose shared memory A from s_a[BM][BK] to s_a[BK][BM+OFFSET] so consecutive  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0566-2](../sources/experiences/exp-a-kd-20260519-0566-2.md) | Stage shared memory values into register arrays (r_comp_a[TM], r_comp_b[TN]) via | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0567-1](../sources/experiences/exp-a-kd-20260519-0567-1.md) | Double buffering with a 2-stage software pipeline: allocate s_a[2][BK][BM] and s | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0568-1](../sources/experiences/exp-a-kd-20260519-0568-1.md) | Replace synchronous B-tile global-to-shared FLOAT4 copies with cp.async asynchro | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0569-1](../sources/experiences/exp-a-kd-20260519-0569-1.md) | Replace synchronous FLOAT4 B-matrix loads with cp.async (CP_ASYNC_CA) instructio | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0570-1](../sources/experiences/exp-a-kd-20260519-0570-1.md) | Replace synchronous FLOAT4 B-tile loads with cp.async.ca.shared.global (CP_ASYNC | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0571-1](../sources/experiences/exp-a-kd-20260519-0571-1.md) | Replace synchronous B-matrix global-to-shared FLOAT4 loads with cp.async.ca.shar | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0572-1](../sources/experiences/exp-a-kd-20260519-0572-1.md) | Replace synchronous FLOAT4 stores to s_b with cp.async.ca (copy asynchronous, ca | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0573-1](../sources/experiences/exp-a-kd-20260519-0573-1.md) | Replace synchronous B-tile global-to-shared FLOAT4 copies with cp.async.ca.share | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0574-1](../sources/experiences/exp-a-kd-20260519-0574-1.md) | Replace synchronous FLOAT4 B-tile loads with cp.async.ca.shared.global directive | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0575-1](../sources/experiences/exp-a-kd-20260519-0575-1.md) | Replace synchronous FLOAT4 B-tile global-to-shared copies with cp.async.ca (asyn | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0576-1](../sources/experiences/exp-a-kd-20260519-0576-1.md) | Set CUBLAS_TF32_TENSOR_OP_MATH math mode and CUBLAS_GEMM_DEFAULT_TENSOR_OP algor | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0577-1](../sources/experiences/exp-a-kd-20260519-0577-1.md) | Enable TF32 tensor core acceleration by setting CUBLAS_TF32_TENSOR_OP_MATH math  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0578-1](../sources/experiences/exp-a-kd-20260519-0578-1.md) | Replace static 3D shared memory with extern __shared__ dynamic allocation plus m | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0579-1](../sources/experiences/exp-a-kd-20260519-0579-1.md) | Replace static shared memory with dynamic shared memory (extern __shared__ float | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0580-1](../sources/experiences/exp-a-kd-20260519-0580-1.md) | Pre-compute __cvta_generic_to_shared once on the shared memory array base pointe | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0583-1](../sources/experiences/exp-a-kd-20260519-0583-1.md) | Replace scalar f32 loads with vectorized float4 loads via the FLOAT4 macro (rein | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0584-1](../sources/experiences/exp-a-kd-20260519-0584-1.md) | Pack multiple rows per warp via sub-warp tiling: each warp processes ROW_PER_WAR | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0785-1](../sources/experiences/exp-a-kd-20260519-0785-1.md) | Enlarge TileShape to <128,128,64> and WarpShape to <64,64,64>: each threadblock  | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0786-1](../sources/experiences/exp-a-kd-20260519-0786-1.md) | Enlarge the tile to ThreadblockShape<128,128,64> and WarpShape<64,64,64>, comput | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0855-1](../sources/experiences/exp-a-kd-20260519-0855-1.md) | Replace ^row with ^(row % 8) in the XOR remapping to constrain the XOR operand t | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0857-1](../sources/experiences/exp-a-kd-20260519-0857-1.md) | Overlap B-loading and reduction buffers in shared memory (they are never live si | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0899-1](../sources/experiences/exp-a-kd-20260519-0899-1.md) | Assign each independent GEMM to a dedicated CUDA stream (stream1, stream2) so th | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0900-1](../sources/experiences/exp-a-kd-20260519-0900-1.md) | Add explicit cudaSetDevice(0) for multi-GPU device context and create a dedicate | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0934-1](../sources/experiences/exp-a-kd-20260519-0934-1.md) | Replace fixed blockIdx.x starting offset with a rotation scheme: track cumulativ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0935-1](../sources/experiences/exp-a-kd-20260519-0935-1.md) | Rotate the starting CTA offset across groups by tracking the cumulative tile cou | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0988-1](../sources/experiences/exp-a-kd-20260519-0988-1.md) | Replace the single M-threshold with arithmetic intensity (AI = 2·M·N·K / (M·K +  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0989-1](../sources/experiences/exp-a-kd-20260519-0989-1.md) | Replace the single M-dimension threshold with an arithmetic-intensity-aware rout | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0998-1](../sources/experiences/exp-a-kd-20260519-0998-1.md) | Add hardware-aware guard (sm_count == 78 && K > 128) so that on GPUs with many S | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0999-1](../sources/experiences/exp-a-kd-20260519-0999-1.md) | Add SM count awareness to the dispatch condition by requiring both sm_count == 7 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1001-1](../sources/experiences/exp-a-kd-20260519-1001-1.md) | Hoist cudaStream_t creation, cudaGetDeviceProperties query, and cudaSetDevice gu | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1002-1](../sources/experiences/exp-a-kd-20260519-1002-1.md) | Introduce an adaptive dispatch that selects between a cooperative kernel (BM=16, | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1003-1](../sources/experiences/exp-a-kd-20260519-1003-1.md) | Conditional dispatch selects a smaller-tile pingpong kernel (BM=8, BK=8, BN=16)  | analysis | sm120 | cuda-cpp |
| [exp-a-kd-20260519-1153-1](../sources/experiences/exp-a-kd-20260519-1153-1.md) | Replace the mul-then-tree-add pattern with a serial FMA chain: multiply the firs | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1170-1](../sources/experiences/exp-a-kd-20260519-1170-1.md) | Reduce TILE_M from 128 to 64 to exactly match the problem dimension M=64, elimin | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1171-1](../sources/experiences/exp-a-kd-20260519-1171-1.md) | Reduce TILE_M from 128 to 32 to better match the actual M=16 problem dimension,  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1185-1](../sources/experiences/exp-a-kd-20260519-1185-1.md) | Replace the two m16n8k16 MMA calls with a single m16n8k32 MMA instruction that c | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1186-1](../sources/experiences/exp-a-kd-20260519-1186-1.md) | Add an is_a_8bit flag to conditionally compute sh_a_size as 1 byte per element f | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1186-2](../sources/experiences/exp-a-kd-20260519-1186-2.md) | Expand metadata allocation from tb_m * 4 to tb_m * 16 bytes (4 floats per row) t | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1201-1](../sources/experiences/exp-a-kd-20260519-1201-1.md) | Introduce m_block_size=8 specialization when prob_m <= 8 and thread_m_blocks ==  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1202-1](../sources/experiences/exp-a-kd-20260519-1202-1.md) | Refactor M-split dispatch from a for-loop over tot_m_blocks to a while(rest_m) l | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1206-1](../sources/experiences/exp-a-kd-20260519-1206-1.md) | Replace full row XOR (col ^ row) with truncated row XOR (col ^ (row % 8)) — sinc | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1207-1](../sources/experiences/exp-a-kd-20260519-1207-1.md) | Replace the hardcoded ldmatrix.x4 load with a templated ldsm_load<count> that se | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1211-1](../sources/experiences/exp-a-kd-20260519-1211-1.md) | Adapt TILE_M at compile time to match the actual valid row count (TILE_M=8 for s | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1232-1](../sources/experiences/exp-a-kd-20260519-1232-1.md) | Query the actual device SM count at runtime via cudaDeviceGetAttribute(cudaDevAt | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1233-1](../sources/experiences/exp-a-kd-20260519-1233-1.md) | Replace hardcoded SM count with runtime query via cudaDeviceGetAttribute(cudaDev | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1254-1](../sources/experiences/exp-a-kd-20260519-1254-1.md) | Switch accumulation from native fp16 (__hadd/__hmul) to fp32 by converting share | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1254-2](../sources/experiences/exp-a-kd-20260519-1254-2.md) | Fuse bias addition into the GEMM epilogue by loading the bias vector into a shar | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1262-1](../sources/experiences/exp-a-kd-20260519-1262-1.md) | Doubling TILE_K from 64 to 128 halves K iterations and sync barriers but increas | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1263-1](../sources/experiences/exp-a-kd-20260519-1263-1.md) | Doubled TILE_K from 64 to 128 to match CUTLASS sm75_config_M64 (GemmShape<64,128 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1264-1](../sources/experiences/exp-a-kd-20260519-1264-1.md) | Adapt tile shape to BM=8, BN=32 for small M workloads, doubling grid parallelism | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1268-1](../sources/experiences/exp-a-kd-20260519-1268-1.md) | Refactor monolithic dispatch into a templated dispatch_scaled_mm that routes per | analysis | sm100 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-1277-1](../sources/experiences/exp-a-kd-20260519-1277-1.md) | Replace the two-pass bf16-GEMM + cast-kernel pipeline with a single cublasGemmEx | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1278-1](../sources/experiences/exp-a-kd-20260519-1278-1.md) | Replace the two-step bf16 GEMM + cast pipeline with a single cublasGemmEx call u | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1279-1](../sources/experiences/exp-a-kd-20260519-1279-1.md) | Use cublasGemmEx with CUDA_R_32F as the output type (d_C_fp32 buffer, C-type CUD | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1280-1](../sources/experiences/exp-a-kd-20260519-1280-1.md) | Use cublasGemmEx with CUDA_R_32F as the output matrix dtype instead of CUDA_R_16 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1281-1](../sources/experiences/exp-a-kd-20260519-1281-1.md) | Use cublasGemmEx with CUDA_R_32F output type instead of CUDA_R_16BF, so the GEMM | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1350-1](../sources/experiences/exp-a-kd-20260519-1350-1.md) | Switch to an M-appropriate small tile configuration (BM=32, BN=64, BK=64, TM=1,  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1351-1](../sources/experiences/exp-a-kd-20260519-1351-1.md) | Switch to an M-appropriate tile (BM=32, BN=64, BK=64) where M=64 maps to exactly | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1352-1](../sources/experiences/exp-a-kd-20260519-1352-1.md) | Reduce tile BM from 128 to 64 (and TM from 4 to 2) to cut shared memory per bloc | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1353-1](../sources/experiences/exp-a-kd-20260519-1353-1.md) | Swap A/B operands to reformulate the GEMM as (N,K)x(K,M)=(1024,1536)x(1536,2), s | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1354-1](../sources/experiences/exp-a-kd-20260519-1354-1.md) | Swap A and B operands to recast the problem as (N,K)x(K,M) = (3072,1536)x(1536,4 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1355-1](../sources/experiences/exp-a-kd-20260519-1355-1.md) | Swap A and B matrices (swap_ab) so computation becomes (N,K)x(K,M) with tile con | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1356-1](../sources/experiences/exp-a-kd-20260519-1356-1.md) | Swap matrix operands (swap_ab) to reinterpret the GEMM as (N,K)x(K,M) with tile  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1357-1](../sources/experiences/exp-a-kd-20260519-1357-1.md) | Apply the swap_ab transpose trick: compute C^T = B^T * A^T via cublasSgemm with  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1358-1](../sources/experiences/exp-a-kd-20260519-1358-1.md) | Swap A/B operands using CUBLAS_OP_T for both, reinterpreting the problem as C^T[ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1360-1](../sources/experiences/exp-a-kd-20260519-1360-1.md) | Templatize compute_problem_sizes with a SWAP_AB<bool> parameter; when token coun | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-1361-1](../sources/experiences/exp-a-kd-20260519-1361-1.md) | Apply swapAB transformation: transpose both operands via CUBLAS_OP_T and swap A/ | analysis | sm120 | cuda-cpp |
| [exp-a-kd-20260519-1362-1](../sources/experiences/exp-a-kd-20260519-1362-1.md) | Swap A/B operands via CUBLAS_OP_T on both matrices so the small M=4 dimension be | analysis | sm120 | cuda-cpp |
| [exp-a-kd-20260519-1363-1](../sources/experiences/exp-a-kd-20260519-1363-1.md) | Swap operands A and B and apply CUBLAS_OP_T on both, reformulating the GEMM as ( | analysis | sm120 | cuda-cpp |
| [exp-a-kd-20260519-1364-1](../sources/experiences/exp-a-kd-20260519-1364-1.md) | Apply swapAB heuristic (swap when M<=64 or M%4!=0) by transposing the GEMM into  | analysis | sm120 | cuda-cpp |
| [exp-a-kd-20260519-1365-1](../sources/experiences/exp-a-kd-20260519-1365-1.md) | Apply swapAB heuristic: when M<=64 or M%4!=0, transpose the GEMM by swapping A/B | analysis | sm120 | cuda-cpp |
| [exp-a-kd-20260519-1389-1](../sources/experiences/exp-a-kd-20260519-1389-1.md) | Fuse bias addition into the GEMM epilogue: keep the scaled dot-product result in | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1390-1](../sources/experiences/exp-a-kd-20260519-1390-1.md) | Fuse bias addition into the GEMM kernel epilogue so D = scaleA*(scaleB*(A*B)) +  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1391-1](../sources/experiences/exp-a-kd-20260519-1391-1.md) | Fuse the bias addition into the GEMM epilogue by computing C = scaleA * (scaleB  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1392-1](../sources/experiences/exp-a-kd-20260519-1392-1.md) | Place the reduction region at a dedicated non-overlapping offset beyond the full | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1395-1](../sources/experiences/exp-a-kd-20260519-1395-1.md) | Use the swap_ab identity C^T = B^T * A^T (CUBLAS_OP_T on both operands) so that  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1396-1](../sources/experiences/exp-a-kd-20260519-1396-1.md) | Use swap_ab strategy: compute C^T = B^T * A^T via cublasHgemm with CUBLAS_OP_T o | analysis | sm100 | cuda-cpp |
| [exp-a-kd-20260519-1397-1](../sources/experiences/exp-a-kd-20260519-1397-1.md) | Replace the binary 2SM/1SM heuristic with a three-tier adaptive tile_m selection | analysis | sm100 | cuda-cpp |
| [exp-a-kd-20260519-1400-1](../sources/experiences/exp-a-kd-20260519-1400-1.md) | Reorder pipeline stages to issue matmul compute before the cp_async_wait<0>() ba | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1401-1](../sources/experiences/exp-a-kd-20260519-1401-1.md) | Increase max_par from 16 to 64 so that all column slices for N=4096 can be batch | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1413-1](../sources/experiences/exp-a-kd-20260519-1413-1.md) | Replace two dense mma.sync.m16n8k16 instructions with a single mma.sp.sync.align | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1415-1](../sources/experiences/exp-a-kd-20260519-1415-1.md) | Replace four dense mma.sync.aligned.m16n8k16 instructions with four sparse mma.s | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1421-1](../sources/experiences/exp-a-kd-20260519-1421-1.md) | Pass the actual leading dimension (lda) as an explicit kernel parameter and comp | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1433-1](../sources/experiences/exp-a-kd-20260519-1433-1.md) | Query cudaDevAttrMaxSharedMemoryPerBlockOptin once at static-init time and branc | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1434-1](../sources/experiences/exp-a-kd-20260519-1434-1.md) | Query cudaDevAttrMaxSharedMemoryPerBlockOptin at dispatch time to detect availab | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1449-1](../sources/experiences/exp-a-kd-20260519-1449-1.md) | Replace single-kernel atomicAdd reduction with a two-phase approach: (1) splitk_ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1452-1](../sources/experiences/exp-a-kd-20260519-1452-1.md) | Replace the half-typed intermediate buffer with a float-typed buffer, eliminatin | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1453-1](../sources/experiences/exp-a-kd-20260519-1453-1.md) | Replace the FP16 intermediate buffer with FP32 storage, eliminating __float2half | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1466-1](../sources/experiences/exp-a-kd-20260519-1466-1.md) | Replace TileShape<128,128,64>/WarpShape<64,64,64> with TileShape<16,64,128>/Warp | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-1467-1](../sources/experiences/exp-a-kd-20260519-1467-1.md) | Reduce tile M to 16 to exactly match the problem dimension (TileShape<16,64,128> | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-1468-1](../sources/experiences/exp-a-kd-20260519-1468-1.md) | Shrink TileShape M from 128 to 32 to exactly match the problem dimension M=32, a | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-1469-1](../sources/experiences/exp-a-kd-20260519-1469-1.md) | Shrink TileShape M from 128 to 64 to exactly match the actual M dimension (elimi | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-1470-1](../sources/experiences/exp-a-kd-20260519-1470-1.md) | Control case: both before and after use the identical GemmShape<128,128,64> tile | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-1471-1](../sources/experiences/exp-a-kd-20260519-1471-1.md) | Switch to TileShape<64,128,128> via N-dependent dispatch: tile M=64 better match | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-1472-1](../sources/experiences/exp-a-kd-20260519-1472-1.md) | The N-dependent dispatch correctly preserves the default TileShape<128,128,64> w | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-1520-1](../sources/experiences/exp-a-kd-20260519-1520-1.md) | Replace the platform-dependent WARP_SIZE=64 macro with a dedicated WARP_SIZE_GGU | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1526-1](../sources/experiences/exp-a-kd-20260519-1526-1.md) | Add a compile-time bool SWAP_AB template parameter with if constexpr to select b | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1527-1](../sources/experiences/exp-a-kd-20260519-1527-1.md) | Add a compile-time SWAP_AB template parameter to conditionally swap M and N in p | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1537-1](../sources/experiences/exp-a-kd-20260519-1537-1.md) | Add a {thread_k=128, thread_n=64, num_threads=128} config to the thread config t | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1538-1](../sources/experiences/exp-a-kd-20260519-1538-1.md) | Swap tile dimensions to {TILE_K=128, TILE_N=64} which produces 2 N-tiles × 32 K- | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1539-1](../sources/experiences/exp-a-kd-20260519-1539-1.md) | Replace whole-tile persistent scheduling with StreamK decomposition: split each  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1540-1](../sources/experiences/exp-a-kd-20260519-1540-1.md) | StreamK decomposition breaks each tile's K-dimension into independent K-iteratio | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1541-1](../sources/experiences/exp-a-kd-20260519-1541-1.md) | The heuristic correctly selects PersistentScheduler for balanced GEMM shapes (K  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1542-1](../sources/experiences/exp-a-kd-20260519-1542-1.md) | StreamK scheduling distributes M*N output elements evenly across grid_size=num_s | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1543-1](../sources/experiences/exp-a-kd-20260519-1543-1.md) | Introduce a shape-aware heuristic dispatch that selects PersistentScheduler when | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1544-1](../sources/experiences/exp-a-kd-20260519-1544-1.md) | Introduce a K > 3*N heuristic to detect tall-and-skinny shapes and switch from p | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1545-1](../sources/experiences/exp-a-kd-20260519-1545-1.md) | Promote num_tokens to a compile-time template parameter kNumTokens so the NVCC c | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1546-1](../sources/experiences/exp-a-kd-20260519-1546-1.md) | Promote num_tokens to a compile-time template parameter kNumTokens, enabling exa | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1547-1](../sources/experiences/exp-a-kd-20260519-1547-1.md) | Replace 8 individual 16-bit scalar bf16 loads with a single uint4 (128-bit) vect | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1548-1](../sources/experiences/exp-a-kd-20260519-1548-1.md) | Replace 8 scalar bf16 loads per matrix access with a single uint4 (128-bit) vect | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1587-1](../sources/experiences/exp-a-kd-20260519-1587-1.md) | Introduce problem-size-aware host-side dispatch that selects block dimensions ba | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1588-1](../sources/experiences/exp-a-kd-20260519-1588-1.md) | Introduce problem-size-aware block dimension dispatch: when M<=16 and N,K are no | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1589-1](../sources/experiences/exp-a-kd-20260519-1589-1.md) | Problem-size-aware dispatch selects wider block dimensions (32x8) for N>=8192, k | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1590-1](../sources/experiences/exp-a-kd-20260519-1590-1.md) | Add problem-size-aware dispatch logic that selects block dimensions based on M/N | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1595-1](../sources/experiences/exp-a-kd-20260519-1595-1.md) | Replace the unconditional return false in the SM89 branch with return cuda_versi | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-1620-1](../sources/experiences/exp-a-kd-20260519-1620-1.md) | Swap GEMM operands to compute C^T(NxM) = B^T(NxK) x A^T(KxM) with TILE_N_SWAP=12 | analysis | sm100 | cuda-cpp |
| [exp-a-kd-20260519-1621-1](../sources/experiences/exp-a-kd-20260519-1621-1.md) | Swap A and B operands to restructure the GEMM as C^T(NxM) = B^T(NxK) x A^T(KxM)  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1652-1](../sources/experiences/exp-a-kd-20260519-1652-1.md) | Switch to M-adaptive TileShape 16x64x128 with WarpShape 16x64x64 so that the til | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-1653-1](../sources/experiences/exp-a-kd-20260519-1653-1.md) | Switch to M-adaptive TileShape 32x64x128 with WarpShape 32x64x64, which matches  | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-1654-1](../sources/experiences/exp-a-kd-20260519-1654-1.md) | Adapt TileShape from 128x128x64 to 64x128x128, matching the M=64 dimension exact | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-1674-1](../sources/experiences/exp-a-kd-20260519-1674-1.md) | Shape-aware tile selection dispatches TileShape<16,64,128> for M<=16 and splits  | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-1675-1](../sources/experiences/exp-a-kd-20260519-1675-1.md) | Added shape-aware tile selection logic (select_tile_config) that picks TileShape | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1676-1](../sources/experiences/exp-a-kd-20260519-1676-1.md) | Replace fixed tile configuration with shape-aware selection: for large M (mp2>25 | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-1676-2](../sources/experiences/exp-a-kd-20260519-1676-2.md) | Reduce pipeline stages from 5 to 3 for large M/N configurations in the shape-awa | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-1685-1](../sources/experiences/exp-a-kd-20260519-1685-1.md) | Widen expert_offsets from int32_t* to int64_t* so pointer arithmetic uses the fu | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1686-1](../sources/experiences/exp-a-kd-20260519-1686-1.md) | Change the expert_offsets parameter type from int32_t* to int64_t* so the full 6 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1754-1](../sources/experiences/exp-a-kd-20260519-1754-1.md) | Lower the dispatch clamp from min 32 to min 16 so that M=1 maps to the TILE_M=16 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1755-1](../sources/experiences/exp-a-kd-20260519-1755-1.md) | Lower the dispatch clamp minimum from 32 to 16 so that M=8 maps to next_pow_2(8) | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1756-1](../sources/experiences/exp-a-kd-20260519-1756-1.md) | Lower the dispatch floor from std::max(32, ...) to std::max(16, ...) so that M<= | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1757-1](../sources/experiences/exp-a-kd-20260519-1757-1.md) | Lower the dispatch clamp minimum from 32 to 16, allowing M<=16 cases to select t | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1758-1](../sources/experiences/exp-a-kd-20260519-1758-1.md) | Replace the hardcoded alignment constant with a computed alignment derived from  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1759-1](../sources/experiences/exp-a-kd-20260519-1759-1.md) | Derive alignment from element bit width via 128 / (sizeof(ElementAB) * 8), so fo | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-1760-1](../sources/experiences/exp-a-kd-20260519-1760-1.md) | Replace the hardcoded alignment constant with a compile-time computed expression | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-1763-1](../sources/experiences/exp-a-kd-20260519-1763-1.md) | Convert the int32_t accumulator to float immediately upon read so the epilogue c | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1765-1](../sources/experiences/exp-a-kd-20260519-1765-1.md) | Replace Pingpong double-buffered schedule with WarpSpecialized single-buffered s | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1767-1](../sources/experiences/exp-a-kd-20260519-1767-1.md) | Remove the conditional StreamK/Persistent heuristic entirely and always use a si | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1768-1](../sources/experiences/exp-a-kd-20260519-1768-1.md) | Remove the split-K heuristic entirely and issue a single cuBLAS Sgemm with the f | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1772-1](../sources/experiences/exp-a-kd-20260519-1772-1.md) | Swap operands to compute D=B^T*A^T using CUBLAS_OP_T/CUBLAS_OP_N, which is mathe | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1773-1](../sources/experiences/exp-a-kd-20260519-1773-1.md) | Swap the transpose flags from (CUBLAS_OP_N, CUBLAS_OP_T) to (CUBLAS_OP_T, CUBLAS | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1774-1](../sources/experiences/exp-a-kd-20260519-1774-1.md) | Swap operand order to compute D=matmul(B^T, A^T) then C=D^T, which yields the sa | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1775-1](../sources/experiences/exp-a-kd-20260519-1775-1.md) | Swap operand order to compute D = B^T * A^T then transpose to recover C = D^T, w | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1776-1](../sources/experiences/exp-a-kd-20260519-1776-1.md) | Swap AB operands to compute D=B^T*A^T then C=D^T, which is mathematically equiva | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1777-1](../sources/experiences/exp-a-kd-20260519-1777-1.md) | Swap the GEMM operand order so the larger-dimension matrix (B^T, 4096 rows) beco | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1778-1](../sources/experiences/exp-a-kd-20260519-1778-1.md) | Swap-AB reorders GEMM operands to D = B^T * A^T, which on SM90 hardware can impr | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1779-1](../sources/experiences/exp-a-kd-20260519-1779-1.md) | Swap operand order by computing D = B^T * A^T instead of C = A * B, which transp | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1780-1](../sources/experiences/exp-a-kd-20260519-1780-1.md) | Swap-AB reformulation (C=A*B becomes D=B^T*A^T) to trigger a dispatch path using | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1781-1](../sources/experiences/exp-a-kd-20260519-1781-1.md) | Swap-AB transformation reformulates C=A*B as D=B^T*A^T, combined with dimension- | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-1782-1](../sources/experiences/exp-a-kd-20260519-1782-1.md) | Swap-AB reformulation transposes both operands and reverses multiplication order | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-1783-1](../sources/experiences/exp-a-kd-20260519-1783-1.md) | Swap A and B operands via transposition (compute C^T = B^T * A^T) so that grid.y | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1784-1](../sources/experiences/exp-a-kd-20260519-1784-1.md) | Swap A and B matrices via host-side transpose (A_swap=B^T, B_swap=A^T) so that C | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1785-1](../sources/experiences/exp-a-kd-20260519-1785-1.md) | Retune tile configuration from 32x32x64 to 32x8x128: narrowing TN from 32 to 8 q | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1786-1](../sources/experiences/exp-a-kd-20260519-1786-1.md) | Double the K-tile depth from 64 to 128 (tile 32x32x128) to increase arithmetic i | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1787-1](../sources/experiences/exp-a-kd-20260519-1787-1.md) | After code transposes operands (B^T as A, A^T as B) and calls with shape (N,M,K) | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1788-1](../sources/experiences/exp-a-kd-20260519-1788-1.md) | Apply N-aware dispatch with swap_ab: transpose both A and B matrices on the host | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1810-1](../sources/experiences/exp-a-kd-20260519-1810-1.md) | Replace the compile-time constant pipe_stages=4 with a runtime stages parameter  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1810-2](../sources/experiences/exp-a-kd-20260519-1810-2.md) | Add an is_a_8bit boolean parameter to get_kernel_cache_size and is_valid_config, | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1811-1](../sources/experiences/exp-a-kd-20260519-1811-1.md) | Convert the compile-time pipe_stages constant into a runtime stages parameter pr | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1812-1](../sources/experiences/exp-a-kd-20260519-1812-1.md) | Convert compile-time pipe_stages=4 constant into a runtime stages parameter (set | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1813-1](../sources/experiences/exp-a-kd-20260519-1813-1.md) | Replace the compile-time constexpr pipe_stages=4 with a runtime stages parameter | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1813-2](../sources/experiences/exp-a-kd-20260519-1813-2.md) | Add an is_a_8bit boolean parameter to conditionally select 1 byte per element fo | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1814-1](../sources/experiences/exp-a-kd-20260519-1814-1.md) | Replace the hardcoded 2-byte multiplier with a runtime conditional (is_a_8bit ?  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1815-1](../sources/experiences/exp-a-kd-20260519-1815-1.md) | Add an is_a_8bit runtime flag and conditionally select 1 byte per A-matrix eleme | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1816-1](../sources/experiences/exp-a-kd-20260519-1816-1.md) | Parameterize both element size (is_a_8bit ? 1 : 2) and pipeline depth (stages) s | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1818-1](../sources/experiences/exp-a-kd-20260519-1818-1.md) | Decompose the single m16n8k16 MMA into two m16n8k8 MMA instructions — the first  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1819-1](../sources/experiences/exp-a-kd-20260519-1819-1.md) | Replace one m16n8k16 MMA with two sequential m16n8k8 MMA calls, feeding a[0..1]/ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1820-1](../sources/experiences/exp-a-kd-20260519-1820-1.md) | Decompose one m16n8k32 MMA call into four m8n8k16 calls by splitting the A matri | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1821-1](../sources/experiences/exp-a-kd-20260519-1821-1.md) | Decompose the 16×8×32 output tile into four 8×8×16 sub-tiles by splitting A into | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1822-1](../sources/experiences/exp-a-kd-20260519-1822-1.md) | Replace FP32 accumulation MMA with FP16 accumulation (mma.sync.f16 variant) to h | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1824-1](../sources/experiences/exp-a-kd-20260519-1824-1.md) | Replace the hardcoded pipe_stages=4 constant with a runtime stages parameter set | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1825-1](../sources/experiences/exp-a-kd-20260519-1825-1.md) | Replace the hardcoded const pipe_stages=4 with a runtime stages=2 parameter (Tur | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1826-1](../sources/experiences/exp-a-kd-20260519-1826-1.md) | Reduce pipeline stages from 4 to 2 and thread the stage count as a runtime param | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1828-1](../sources/experiences/exp-a-kd-20260519-1828-1.md) | Right-size the GEMM configuration for small M by switching to 128x128 tiles with | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1829-1](../sources/experiences/exp-a-kd-20260519-1829-1.md) | Switch from type-based config selection to M-dimension-based selection for mediu | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1830-1](../sources/experiences/exp-a-kd-20260519-1830-1.md) | Reduce cluster shape from 4x4 (16 SMs) to 2x1 (2 SMs) and simplify tile indexing | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1831-1](../sources/experiences/exp-a-kd-20260519-1831-1.md) | Replace conditional break statements with clamped index access using a min__() h | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1855-1](../sources/experiences/exp-a-kd-20260519-1855-1.md) | Replace permutation loop with direct threadIdx.y-based indexing using a threadId | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1856-1](../sources/experiences/exp-a-kd-20260519-1856-1.md) | Replace the permutation-loop modulo-scatter pattern with direct threadIdx.y-base | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1857-1](../sources/experiences/exp-a-kd-20260519-1857-1.md) | Split the single thread_configs table into batch-size-aware tables (small_batch_ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1858-1](../sources/experiences/exp-a-kd-20260519-1858-1.md) | Split the thread configuration table into small_batch_thread_configs (first entr | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2331-1](../sources/experiences/exp-a-kd-20260519-2331-1.md) | Replace scalar per-element multiply-add loop with WMMA 16x16x16 tensor core frag | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2334-1](../sources/experiences/exp-a-kd-20260519-2334-1.md) | Split the K dimension into NUM_K_SHARDS=2 shards along a third grid dimension (b | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2339-1](../sources/experiences/exp-a-kd-20260519-2339-1.md) | Replace shared-memory pipeline loads with direct global-memory vector loads into | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2339-2](../sources/experiences/exp-a-kd-20260519-2339-2.md) | Replace the multi-warp block with a single-warp thread_block_tile so the entire  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2339-3](../sources/experiences/exp-a-kd-20260519-2339-3.md) | Coarsen the grid to 64 blocks per batch element by having each block compute 4 o | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2345-1](../sources/experiences/exp-a-kd-20260519-2345-1.md) | Fuse stride array writes into the existing init_offsets_kernel by passing stride | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2347-1](../sources/experiences/exp-a-kd-20260519-2347-1.md) | Adapt tile shape to TILE_M=16 TILE_N=64 so blockDim(64,16) matches M=16 exactly, | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2349-1](../sources/experiences/exp-a-kd-20260519-2349-1.md) | Widen M tile to 64 and narrow N tile to 16 (blockDim 16x64) to increase M-axis p | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2358-1](../sources/experiences/exp-a-kd-20260519-2358-1.md) | Replace manual stride assignment with cutlass::make_cute_packed_stride(StrideTyp | analysis | sm100 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-2359-1](../sources/experiences/exp-a-kd-20260519-2359-1.md) | Replace manual stride assignment with a packed-stride-from-shape helper that der | analysis | sm100 | cuda-cpp |
| [exp-a-kd-20260519-2369-1](../sources/experiences/exp-a-kd-20260519-2369-1.md) | Apply XOR-based index remapping (transform_a(i) = a_gl_rd_delta_o * row + (i % a | analysis | sm90 | cuda-cpp |
| [exp-i-20260508-120001-sol-execbench-file-template](../sources/experiences/exp-i-20260508-120001-sol-execbench-file-template.md) | How to structure CUDA C++ solution files for SOL-ExecBench GEMM problems to avoi | implementation | sm90 | cuda-cpp |
| [exp-i-20260517-200010-int8-gemm-template](../sources/experiences/exp-i-20260517-200010-int8-gemm-template.md) | INT8 GEMM kernel implementation template for SOL-ExecBench | implementation | sm90 | cuda-cpp |
| [exp-i-20260517-200011-bf16-gemm-template](../sources/experiences/exp-i-20260517-200011-bf16-gemm-template.md) | BF16 GEMM kernel implementation template for SOL-ExecBench | implementation | sm90 | cuda-cpp |
| [exp-i-20260517-200012-sol-execbench-cpp-template](../sources/experiences/exp-i-20260517-200012-sol-execbench-cpp-template.md) | SOL-ExecBench cuda_cpp solution.json and source file template | implementation | sm90 | cuda-cpp |
| [exp-i-20260527-080001-cublaslt-fp16-gemm-best-config](../sources/experiences/exp-i-20260527-080001-cublaslt-fp16-gemm-best-config.md) | SOL-ExecBench GEMM: cublasLt FP16 reference implementation achieving 0.9999x | implementation | sm90 | cuda-cpp |
| [exp-i-kd-20260518-0002](../sources/experiences/exp-i-kd-20260518-0002.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0003](../sources/experiences/exp-i-kd-20260518-0003.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0006](../sources/experiences/exp-i-kd-20260518-0006.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0007](../sources/experiences/exp-i-kd-20260518-0007.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0008](../sources/experiences/exp-i-kd-20260518-0008.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0009](../sources/experiences/exp-i-kd-20260518-0009.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0010](../sources/experiences/exp-i-kd-20260518-0010.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0011](../sources/experiences/exp-i-kd-20260518-0011.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0015](../sources/experiences/exp-i-kd-20260518-0015.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm100 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0016](../sources/experiences/exp-i-kd-20260518-0016.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp |
| [exp-i-kd-20260518-0017](../sources/experiences/exp-i-kd-20260518-0017.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0018](../sources/experiences/exp-i-kd-20260518-0018.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0019](../sources/experiences/exp-i-kd-20260518-0019.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0020](../sources/experiences/exp-i-kd-20260518-0020.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0021](../sources/experiences/exp-i-kd-20260518-0021.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0056](../sources/experiences/exp-i-kd-20260518-0056.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0059](../sources/experiences/exp-i-kd-20260518-0059.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0062](../sources/experiences/exp-i-kd-20260518-0062.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0063](../sources/experiences/exp-i-kd-20260518-0063.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0064](../sources/experiences/exp-i-kd-20260518-0064.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0065](../sources/experiences/exp-i-kd-20260518-0065.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0069](../sources/experiences/exp-i-kd-20260518-0069.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2387-1](../sources/experiences/exp-i-kd-20260519-2387-1.md) | Use a 2D thread grid where each thread computes one output element C[i][j] via a | implementation | sm90 | cuda-cpp |
| [exp-i-kd-20260519-2390-1](../sources/experiences/exp-i-kd-20260519-2390-1.md) | Declare shared memory arrays matching template dimensions, stage data via thread | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2391-1](../sources/experiences/exp-i-kd-20260519-2391-1.md) | Define shared memory tiles for A (row-major), B (column-major), C matrices with  | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2393-1](../sources/experiences/exp-i-kd-20260519-2393-1.md) | Map each thread to one output element via 2D index (threadIdx + blockIdx*blockDi | implementation | sm90 | cuda-cpp |
| [exp-i-kd-20260519-2395-1](../sources/experiences/exp-i-kd-20260519-2395-1.md) | Leverage CUTLASS Trmm device operation with OpClassTensorOp targeting SM80 tenso | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2400-1](../sources/experiences/exp-i-kd-20260519-2400-1.md) | Implement a CuTe-based GEMM with three-phase structure: (1) partition gmem/smem/ | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2401-1](../sources/experiences/exp-i-kd-20260519-2401-1.md) | Implement a double-buffered circular pipeline using PipelineState for automatic  | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2402-1](../sources/experiences/exp-i-kd-20260519-2402-1.md) | Use CUTE tensor abstractions to build the GEMM: construct global tensors with ma | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2403-1](../sources/experiences/exp-i-kd-20260519-2403-1.md) | Construct global tensors via make_tensor(make_gmem_ptr, shape, stride), tile per | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2404-1](../sources/experiences/exp-i-kd-20260519-2404-1.md) | Build the cute tensor hierarchy bottom-up: global tensors via make_tensor(make_g | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2404-2](../sources/experiences/exp-i-kd-20260519-2404-2.md) | Implement a two-level pipelined loop: outer loop iterates k_tiles (gmem tiles, C | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2405-1](../sources/experiences/exp-i-kd-20260519-2405-1.md) | Implement a three-level pipelined GEMM: (1) construct CuTe global/shared/registe | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2442-1](../sources/experiences/exp-i-kd-20260519-2442-1.md) | Use cutlass::epilogue::thread::LinearCombinationPlanarComplex<half_t, 4, half_t, | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2443-1](../sources/experiences/exp-i-kd-20260519-2443-1.md) | Define LinearCombinationPlanarComplex type aliases with correct mixed-precision  | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2445-1](../sources/experiences/exp-i-kd-20260519-2445-1.md) | Uncomment and complete the nested iteration loop: outer loop iterates over tile  | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2446-1](../sources/experiences/exp-i-kd-20260519-2446-1.md) | Use CUTLASS's GemmGroupedProblemVisitor to manage shared storage and iterate til | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2447-1](../sources/experiences/exp-i-kd-20260519-2447-1.md) | Initialize PersistentTileSchedulerSm90StreamK from params, then loop over valid  | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2449-1](../sources/experiences/exp-i-kd-20260519-2449-1.md) | Initialize FragmentC accumulator elements using warp_id * blockDim.x + lane_id a | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2453-1](../sources/experiences/exp-i-kd-20260519-2453-1.md) | Construct a zero-initialized fragment, compute per-thread input pointers using ( | implementation | sm90 | cuda-cpp, cute-dsl |
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
| [exp-o-20260508-120001-cublas-row-major-mapping](../sources/experiences/exp-o-20260508-120001-cublas-row-major-mapping.md) | SOL-ExecBench defines GEMM as C[M,N] = A[M,K] @ B[N,K].T with row-major inputs | optimization | sm90 | cuda-cpp |
| [exp-o-20260508-120002-cublas-handle-persistence](../sources/experiences/exp-o-20260508-120002-cublas-handle-persistence.md) | Creating and destroying cuBLAS handle on every call introduces 50-100ms overhead | optimization | sm90 | cuda-cpp |
| [exp-o-20260508-120003-int8-gemm-prefer-cublas](../sources/experiences/exp-o-20260508-120003-int8-gemm-prefer-cublas.md) | INT8 GEMM has 19.2% pass rate overall (5/26 attempts) | optimization | sm90 | cuda-cpp |
| [exp-o-20260508-120004-bf16-fp32-accumulation](../sources/experiences/exp-o-20260508-120004-bf16-fp32-accumulation.md) | Which compute type should be used for BF16 GEMM — CUDA_R_16BF or CUDA_R_32F? | optimization | sm90 | cuda-cpp |
| [exp-o-20260508-120005-small-matrix-torch-mm](../sources/experiences/exp-o-20260508-120005-small-matrix-torch-mm.md) | Small matrix GEMM (m<=50 or n<=256) has 15.8% pass rate with cuBLAS | optimization | sm90 | python |
| [exp-o-20260508-120006-problem-size-speedup](../sources/experiences/exp-o-20260508-120006-problem-size-speedup.md) | What speedup can be expected for different GEMM problem sizes? Setting realistic | optimization | sm90 | cuda-cpp |
| [exp-o-20260508-160201-benchmark-timing-hygiene](../sources/experiences/exp-o-20260508-160201-benchmark-timing-hygiene.md) | Speedup values are unstable or suspiciously high due to inconsistent benchmark t | optimization | sm90 | cuda-cpp |
| [exp-o-20260508-160202-gemm-strategy-dispatch-by-shape](../sources/experiences/exp-o-20260508-160202-gemm-strategy-dispatch-by-shape.md) | No single GEMM path dominates all shapes | optimization | sm90 | cuda-cpp |
| [exp-o-20260508-180001-bf16-cublas-swap-mapping](../sources/experiences/exp-o-20260508-180001-bf16-cublas-swap-mapping.md) | Gemm optimization: BF16 and INT8 use the EXACT SAME swap mapping: m=N, n=M, A_p | optimization | sm90 | cuda-cpp |
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
| [exp-o-kd-20260518-0012](../sources/experiences/exp-o-kd-20260518-0012.md) | b2b_gemm_f16_sm80_medium | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0035](../sources/experiences/exp-o-kd-20260518-0035.md) | epilogue_inline_vs_smem | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0036](../sources/experiences/exp-o-kd-20260518-0036.md) | b2b_gemm_f16_rf | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260518-0060](../sources/experiences/exp-o-kd-20260518-0060.md) | gemm_m128_n128_k2048_split4 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0099](../sources/experiences/exp-o-kd-20260518-0099.md) | flash_attn_split_kv_headdim64_seq1024 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0108](../sources/experiences/exp-o-kd-20260518-0108.md) | d64_s512 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0117](../sources/experiences/exp-o-kd-20260518-0117.md) | hgemm_256 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0145](../sources/experiences/exp-o-kd-20260518-0145.md) | sgemm_8x16_m512 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0146](../sources/experiences/exp-o-kd-20260518-0146.md) | sgemm_8x16_m1024 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0201](../sources/experiences/exp-o-kd-20260518-0201.md) | Guard the accumulator pipeline consumer_wait with is_accumulator_needed so that  | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260518-0228](../sources/experiences/exp-o-kd-20260518-0228.md) | concurrent_overlap | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0245](../sources/experiences/exp-o-kd-20260518-0245.md) | Replace inline per-warp scale/bias with a centralized EpilogueSmemAccumulator pa | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0273](../sources/experiences/exp-o-kd-20260518-0273.md) | moe_dispatch_k256 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0285](../sources/experiences/exp-o-kd-20260518-0285.md) | Replace occupancy-rounded waveset formula with fast_max(work_blocks, avail_sms*4 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0335](../sources/experiences/exp-o-kd-20260518-0335.md) | int8_k32_vs_two_k16 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0351](../sources/experiences/exp-o-kd-20260518-0351.md) | medium_kernel_sync | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260518-0355](../sources/experiences/exp-o-kd-20260518-0355.md) | grouped_4096_32x32 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0378](../sources/experiences/exp-o-kd-20260518-0378.md) | tokens_64_256ep | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0396](../sources/experiences/exp-o-kd-20260518-0396.md) | Vectorize to f16x4 (half2 pair) loads per thread using reinterpret_cast<half2*>  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0397](../sources/experiences/exp-o-kd-20260518-0397.md) | Replace scalar half loads with half2 vectorized loads (f16x4 style), loading 4 h | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0398](../sources/experiences/exp-o-kd-20260518-0398.md) | Vectorize the inner loop to process 4 half elements per thread per iteration usi | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0422](../sources/experiences/exp-o-kd-20260518-0422.md) | small_m_4_n_1024_k_512 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0431](../sources/experiences/exp-o-kd-20260518-0431.md) | Replace synchronous FLOAT4 global-to-shared loads for B with cp.async.ca asynchr | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0432](../sources/experiences/exp-o-kd-20260518-0432.md) | Replace synchronous FLOAT4 global-to-shared stores for B with cp.async.ca asynch | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0435](../sources/experiences/exp-o-kd-20260518-0435.md) | int8_m128_n1024_k512 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0436](../sources/experiences/exp-o-kd-20260518-0436.md) | bf16_m64_n128_k256 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0441](../sources/experiences/exp-o-kd-20260518-0441.md) | sparse_mma_dense | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0444](../sources/experiences/exp-o-kd-20260518-0444.md) | Replace scalar f32 loads with vectorized float4 (f32x4) loads so each thread fet | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0487](../sources/experiences/exp-o-kd-20260518-0487.md) | streamk_tall_skinny | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0528](../sources/experiences/exp-o-kd-20260518-0528.md) | large_m_large_n | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0553](../sources/experiences/exp-o-kd-20260518-0553.md) | block16_vs_block32_short_seq | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0564](../sources/experiences/exp-o-kd-20260518-0564.md) | tall_skinny | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0567](../sources/experiences/exp-o-kd-20260518-0567.md) | small_m_noswap | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0587](../sources/experiences/exp-o-kd-20260518-0587.md) | half_small_M | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0603](../sources/experiences/exp-o-kd-20260518-0603.md) | mfma_wider_instr | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0605](../sources/experiences/exp-o-kd-20260518-0605.md) | adaptive_splitk | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0620](../sources/experiences/exp-o-kd-20260518-0620.md) | The TMEM buffer, so the pipeline never transitions to a state where the consumer | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0623](../sources/experiences/exp-o-kd-20260518-0623.md) | The optimization is most impactful for narrow data types (INT4) in mixed-precisi | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0629](../sources/experiences/exp-o-kd-20260518-0629.md) | For both the source-load and the no-source branches, retaining unnecessary globa | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0631](../sources/experiences/exp-o-kd-20260518-0631.md) | , creating a significant synchronization bottleneck especially for large output  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0634](../sources/experiences/exp-o-kd-20260518-0634.md) | Red-memory pipeline stages. The first GEMM (Q @ K^T) always used the maximum num | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0636](../sources/experiences/exp-o-kd-20260518-0636.md) | The Zij shared-memory region, competing with other shared-memory accesses, and r | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260518-0637](../sources/experiences/exp-o-kd-20260518-0637.md) | N a single GEMM tile iteration. This caused unnecessary loop overhead, prologue  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0639](../sources/experiences/exp-o-kd-20260518-0639.md) | The iterator had no way to express the wider instruction shape. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0644](../sources/experiences/exp-o-kd-20260518-0644.md) | H forming an SK wave for load balancing makes no sense when there is no multi-oc | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0645](../sources/experiences/exp-o-kd-20260518-0645.md) | Eding 450 work blocks would round up to 864 launched blocks — 414 idle CTAs that | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0648](../sources/experiences/exp-o-kd-20260518-0648.md) | ThreadIdx.x / 32 result), so the shuffle adds unnecessary synchronization overhe | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0650](../sources/experiences/exp-o-kd-20260518-0650.md) | Uction. The __shfl_sync acts as a warp-level barrier and consumes extra register | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0651](../sources/experiences/exp-o-kd-20260518-0651.md) | P threads are not converged (e.g., due to divergent control flow from prior bran | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0680](../sources/experiences/exp-o-kd-20260518-0680.md) | Erializes B loading with A loading and transpose operations. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0681](../sources/experiences/exp-o-kd-20260518-0681.md) | Il the global read completes, preventing overlap with the compute-intensive BK i | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0682](../sources/experiences/exp-o-kd-20260518-0682.md) | Verlap with the A-tile loading and transpose work that follows. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0683](../sources/experiences/exp-o-kd-20260518-0683.md) | Preventing overlap with the BK=16 compute iterations and A-tile transpose of the | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0684](../sources/experiences/exp-o-kd-20260518-0684.md) | The synchronous nature prevents overlap with the A-tile loading and online trans | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0685](../sources/experiences/exp-o-kd-20260518-0685.md) | BK=16 iteration loop (which performs 8x16=128 FMAs per thread per BK step) and t | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0686](../sources/experiences/exp-o-kd-20260518-0686.md) | GPUs this leaves significant tensor-core FLOPS untapped for FP32 GEMM workloads. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0687](../sources/experiences/exp-o-kd-20260518-0687.md) | STAGE=4 already uses ~41 KB (with A_PAD=4), and K_STAGE=5 would exceed the 48 KB | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0694](../sources/experiences/exp-o-kd-20260518-0694.md) | Oor utilization of the Ada SM89 tensor cores. The K=128 dimension also consumes  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0721](../sources/experiences/exp-o-kd-20260518-0721.md) | Efault-stream launch serializes with all other default-stream work, preventing c | optimization | sm100 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260518-0740](../sources/experiences/exp-o-kd-20260518-0740.md) | PUs which have 132 SMs and more shared memory — the Pingpong schedule with its s | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260518-0761](../sources/experiences/exp-o-kd-20260518-0761.md) | Rtized when there are few tiles to iterate over. | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260518-0764](../sources/experiences/exp-o-kd-20260518-0764.md) | Barrier and instruction overhead. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0773](../sources/experiences/exp-o-kd-20260518-0773.md) | Ransfer can start, and the CPU must wait until the transfer finishes. Additional | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260518-0774](../sources/experiences/exp-o-kd-20260518-0774.md) | Ons where kernel execution time is short, this synchronization overhead can domi | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0776](../sources/experiences/exp-o-kd-20260518-0776.md) | Ary across expert groups, inaccurate occupancy estimation leads to suboptimal ti | optimization | sm100 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260518-0788](../sources/experiences/exp-o-kd-20260518-0788.md) | Es (1-64 or 65-128), the large 256-wide M tile leaves most threads idle computin | optimization | sm100 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260518-0789](../sources/experiences/exp-o-kd-20260518-0789.md) | E rows carry useful data, wasting 97% of the M-dimension compute. The N dimensio | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0790](../sources/experiences/exp-o-kd-20260518-0790.md) | The optimization is enabled for small M only (M <= 64) via the dispatch logic in | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260518-0794](../sources/experiences/exp-o-kd-20260518-0794.md) | Memory allocation overhead, increases computation volume on dummy rows, and requ | optimization | sm100 | cuda-cpp |
| [exp-o-kd-20260518-0796](../sources/experiences/exp-o-kd-20260518-0796.md) | Arithmetic would skip incorrect amounts, causing wrong data to be read in subseq | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0812](../sources/experiences/exp-o-kd-20260518-0812.md) | Ip the optimized DP4A-based dot product path and fall through to the scalar fall | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0817](../sources/experiences/exp-o-kd-20260518-0817.md) | Istent scheduler leaves SMs underutilized because the number of output tiles alo | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260518-0818](../sources/experiences/exp-o-kd-20260518-0818.md) | Ts intended mode or may use a less efficient default reduction strategy. | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260518-0819](../sources/experiences/exp-o-kd-20260518-0819.md) | Used in LLM inference where the weight matrix may have a small N dimension relat | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0826](../sources/experiences/exp-o-kd-20260518-0826.md) | Workloads to fall back to slower torch.mm paths, wasting the FP8 tensor core sup | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260518-0830](../sources/experiences/exp-o-kd-20260518-0830.md) | Memory bandwidth underutilized and creating a serial load-then-compute dependenc | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0833](../sources/experiences/exp-o-kd-20260518-0833.md) | The tile, resulting in low GPU occupancy and wasted compute resources. This is p | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260518-0836](../sources/experiences/exp-o-kd-20260518-0836.md) | Nderutilize shared memory with too few stages. | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260518-0838](../sources/experiences/exp-o-kd-20260518-0838.md) | Into frag_zp array, then (3) apply via sub_zp. This adds dequant arithmetic and  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0839](../sources/experiences/exp-o-kd-20260518-0839.md) | S launched unconditionally. When CUTLASS group gemm is used instead of DeepGemm, | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260518-0844](../sources/experiences/exp-o-kd-20260518-0844.md) | E dispatch path to instantiate BLOCK_SIZE=32 was missing. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0847](../sources/experiences/exp-o-kd-20260518-0847.md) | The fix prevents misaligned memory access and potential compilation failures or  | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260518-0850](../sources/experiences/exp-o-kd-20260518-0850.md) | Arithmetic intensity than a 256-deep tile, and (3) the Pingpong schedule adds ov | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0857](../sources/experiences/exp-o-kd-20260518-0857.md) | (pipe_stages * tb_k * tb_n / pack_factor * 4 bytes) alone exceeds 64KB, making t | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0858](../sources/experiences/exp-o-kd-20260518-0858.md) | Nference) leave most tile elements unused under large tiles, while large M benef | optimization | sm100 | cuda-cpp |
| [exp-o-kd-20260518-0867](../sources/experiences/exp-o-kd-20260518-0867.md) | Participate, leaving many CUs idle and wasting compute resources. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0871](../sources/experiences/exp-o-kd-20260518-0871.md) | Ver dispatch) for what is essentially a trivial fill operation that could be don | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0872](../sources/experiences/exp-o-kd-20260518-0872.md) | . The transpose was an extra host-side memory copy that added latency and requir | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260518-0873](../sources/experiences/exp-o-kd-20260518-0873.md) | Lation already applies min__(K * actlN - A_CHUNK, ...) to prevent hardware-level | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0199-1](../sources/experiences/exp-o-kd-20260519-0199-1.md) | Introduce a runtime guard (K > 0) that branches between copying valid accumulato | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0200-1](../sources/experiences/exp-o-kd-20260519-0200-1.md) | Guard the accumulator-buffer copy with an is_accumulator_needed flag (K > 0); wh | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0201-1](../sources/experiences/exp-o-kd-20260519-0201-1.md) | Add is_accumulator_needed guard to the first-iteration accumulator wait conditio | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0202-1](../sources/experiences/exp-o-kd-20260519-0202-1.md) | Guard the TMEM-to-register copy with an is_accumulator_needed check: when true t | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0203-1](../sources/experiences/exp-o-kd-20260519-0203-1.md) | Guard the accumulator release block with is_accumulator_needed so that when K=0  | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0204-1](../sources/experiences/exp-o-kd-20260519-0204-1.md) | Reorder shared memory layout on the host side so that all 16 INT4 elements owned | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0205-1](../sources/experiences/exp-o-kd-20260519-0205-1.md) | Compute a reordering atom (LayoutAtomQuant) from the WGMMA thread-value layout v | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0218-1](../sources/experiences/exp-o-kd-20260519-0218-1.md) | Replace two separate Gemm kernel launches with a single fused B2bGemm kernel tha | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0219-1](../sources/experiences/exp-o-kd-20260519-0219-1.md) | Fuse both GEMMs into a single cutlass::gemm::device::B2bGemm kernel where GEMM0' | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0224-1](../sources/experiences/exp-o-kd-20260519-0224-1.md) | Add a ScaleType::Kind template parameter (with default ScaleType::Default for ba | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0228-1](../sources/experiences/exp-o-kd-20260519-0228-1.md) | Increase FragmentsPerPartition from 1 to 2: the outer loop strides by 2, an inne | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0229-1](../sources/experiences/exp-o-kd-20260519-0229-1.md) | Increase FragmentsPerPartition from 1 to 2, allocating double SMEM (1024 floats) | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0230-1](../sources/experiences/exp-o-kd-20260519-0230-1.md) | Coarsen the loop by processing FPP=2 fragments per outer iteration, using partit | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0232-1](../sources/experiences/exp-o-kd-20260519-0232-1.md) | Add a FragmentsPerPartition template parameter (defaulting to 1 for backward com | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0233-1](../sources/experiences/exp-o-kd-20260519-0233-1.md) | Coarsen the outer loop stride from 1 to kFragmentsPerIteration and add inner loo | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0238-1](../sources/experiences/exp-o-kd-20260519-0238-1.md) | Use the compute_source_not_needed_() path: completely eliminate all source-relat | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0239-1](../sources/experiences/exp-o-kd-20260519-0239-1.md) | Split monolithic compute() into compute_source_not_needed_() and compute_source_ | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0244-1](../sources/experiences/exp-o-kd-20260519-0244-1.md) | Move scale/bias from GEMM1's inner loop into a centralized epilogue after GEMM0: | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0245-1](../sources/experiences/exp-o-kd-20260519-0245-1.md) | Apply scale/bias once per accumulator element in a centralized epilogue pass tha | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0246-1](../sources/experiences/exp-o-kd-20260519-0246-1.md) | Fuse both GEMMs into a single B2bGemm kernel using register-file residency: GEMM | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0253-1](../sources/experiences/exp-o-kd-20260519-0253-1.md) | Replace GemmIdentityThreadblockSwizzle with ThreadblockSwizzleStreamK, which spl | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0269-1](../sources/experiences/exp-o-kd-20260519-0269-1.md) | Replace the triple-nested unrolled loop with direct integer division and modulo  | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0270-1](../sources/experiences/exp-o-kd-20260519-0270-1.md) | Replace the triple-nested loop and conditional branch with three direct integer- | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0272-1](../sources/experiences/exp-o-kd-20260519-0272-1.md) | Replace the triple-nested loop with direct index arithmetic: access_m_idx = ldsm | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0280-1](../sources/experiences/exp-o-kd-20260519-0280-1.md) | Split K=2048 into 4 independent slices of K=512, launch 4 gemm_partial kernels c | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0281-1](../sources/experiences/exp-o-kd-20260519-0281-1.md) | Split K=4096 into 8 slices of K_len=512 and launch 8 gemm_partial kernels concur | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0283-1](../sources/experiences/exp-o-kd-20260519-0283-1.md) | Change the template parameter from sizeof_bits<ElementOutput> to sizeof_bits<Ele | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0284-1](../sources/experiences/exp-o-kd-20260519-0284-1.md) | Add sm_occupancy > 1 guard before the modulo-based wave-boundary condition so th | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0285-1](../sources/experiences/exp-o-kd-20260519-0285-1.md) | Replace the occupancy-rounded waveset formula (ceiling division into gpu_occupan | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0286-1](../sources/experiences/exp-o-kd-20260519-0286-1.md) | Add an `sm_occupancy > 1` guard to the SK wave formation branch condition, so it | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0287-1](../sources/experiences/exp-o-kd-20260519-0287-1.md) | Replace the occupancy-rounded waveset formula with a two-tier approach: return t | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0288-1](../sources/experiences/exp-o-kd-20260519-0288-1.md) | Replace the hardcoded % 4 divisibility check with a dynamically computed divisor | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0289-1](../sources/experiences/exp-o-kd-20260519-0289-1.md) | Replace the hardcoded constant 4 with the dynamically computed ratio size<2>(Til | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0294-1](../sources/experiences/exp-o-kd-20260519-0294-1.md) | Replace the redundant __shfl_sync warp shuffle with canonical_warp_idx(), which  | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0296-1](../sources/experiences/exp-o-kd-20260519-0296-1.md) | Replace __shfl_sync broadcast with canonical_warp_idx() which simply returns thr | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0298-1](../sources/experiences/exp-o-kd-20260519-0298-1.md) | Replace __shfl_sync broadcast with canonical_warp_idx() which computes threadIdx | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0301-1](../sources/experiences/exp-o-kd-20260519-0301-1.md) | Replace __shfl_sync broadcast with canonical_warp_idx() which computes threadIdx | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0304-1](../sources/experiences/exp-o-kd-20260519-0304-1.md) | Replace the __shfl_sync warp-id broadcast with canonical_warp_idx(), which compu | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0344-1](../sources/experiences/exp-o-kd-20260519-0344-1.md) | Fuse the two GEMM projections and the SiLU-gated multiply into a single kernel:  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0353-1](../sources/experiences/exp-o-kd-20260519-0353-1.md) | Right-size shared memory to the actual 64×128 and 128×64 working sets, split the | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0355-1](../sources/experiences/exp-o-kd-20260519-0355-1.md) | Halve the shared memory allocation from 48 KB to 24 KB by reducing the padding b | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0389-1](../sources/experiences/exp-o-kd-20260519-0389-1.md) | Enable block-level swizzle by setting BLOCK_SWIZZLE=true and launching with a 3D | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0390-1](../sources/experiences/exp-o-kd-20260519-0390-1.md) | Replace B_PAD=8 padding with B_PAD=0 and apply XOR-permutation swizzle (swizzle_ | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0391-1](../sources/experiences/exp-o-kd-20260519-0391-1.md) | Replace B_PAD=8 padding with B_PAD=0 and use XOR-permuted swizzle addressing (sw | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0392-1](../sources/experiences/exp-o-kd-20260519-0392-1.md) | Enable block swizzle via a 3D grid (BLOCK_SWIZZLE=true) that reorders thread blo | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0393-1](../sources/experiences/exp-o-kd-20260519-0393-1.md) | Enable block swizzle (BLOCK_SWIZZLE=true) by switching to a 3D grid launch with  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0394-1](../sources/experiences/exp-o-kd-20260519-0394-1.md) | Replace column padding (B_PAD=8) with XOR-based swizzle address permutation via  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0395-1](../sources/experiences/exp-o-kd-20260519-0395-1.md) | Replace scalar half loads with half2 vectorized loads (f16x4 pattern) using HALF | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0396-1](../sources/experiences/exp-o-kd-20260519-0396-1.md) | Replace scalar half loads with half2 vectorized loads (f16x4 pattern) using rein | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0397-1](../sources/experiences/exp-o-kd-20260519-0397-1.md) | Replace scalar half loads with half2 vectorized loads (f16x4 pattern): each thre | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0398-1](../sources/experiences/exp-o-kd-20260519-0398-1.md) | Replace scalar half loads with half2 vectorized loads (f16x4 pattern), where eac | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0417-1](../sources/experiences/exp-o-kd-20260519-0417-1.md) | Use shared memory tiling (block tile + K tile): a 32x32 block cooperatively load | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0418-1](../sources/experiences/exp-o-kd-20260519-0418-1.md) | Transpose A's shared memory layout from s_a[BM][BK] to s_a[BK][BM+OFFSET] so con | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0419-1](../sources/experiences/exp-o-kd-20260519-0419-1.md) | Double-buffer shared memory with s_a[2][BK][BM] and s_b[2][BK][BN] to create a 2 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0420-1](../sources/experiences/exp-o-kd-20260519-0420-1.md) | Replace synchronous B-tile global-to-shared FLOAT4 stores with cp.async.ca.share | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0421-1](../sources/experiences/exp-o-kd-20260519-0421-1.md) | Replace synchronous FLOAT4 B-tile loads with cp.async.ca.shared.global (CP_ASYNC | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0422-1](../sources/experiences/exp-o-kd-20260519-0422-1.md) | Replace synchronous B-matrix global-to-shared FLOAT4 loads with cp.async.ca.shar | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0423-1](../sources/experiences/exp-o-kd-20260519-0423-1.md) | Replace synchronous FLOAT4 stores for B-tile loads with cp.async.ca (copy-async  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0424-1](../sources/experiences/exp-o-kd-20260519-0424-1.md) | Replace synchronous FLOAT4 B-tile loads with cp.async.ca (async copy from global | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0425-1](../sources/experiences/exp-o-kd-20260519-0425-1.md) | Replace synchronous B-tile shared memory stores with cp.async.ca.shared.global i | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0426-1](../sources/experiences/exp-o-kd-20260519-0426-1.md) | Replace synchronous FLOAT4 B-tile loads with cp.async.ca.shared.global instructi | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0427-1](../sources/experiences/exp-o-kd-20260519-0427-1.md) | Replace synchronous B-matrix global-to-shared FLOAT4 stores with cp.async.ca (co | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0428-1](../sources/experiences/exp-o-kd-20260519-0428-1.md) | Replace synchronous B-matrix global-to-shared FLOAT4 loads with cp.async.ca.shar | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0429-1](../sources/experiences/exp-o-kd-20260519-0429-1.md) | Replace synchronous B-matrix global-to-shared loads with PTX cp.async.ca.shared. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0430-1](../sources/experiences/exp-o-kd-20260519-0430-1.md) | Replace synchronous FLOAT4 global-to-shared loads for B with cp.async.ca asynchr | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0431-1](../sources/experiences/exp-o-kd-20260519-0431-1.md) | Issue cp.async.ca instructions for the next B tile at the start of each loop ite | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0432-1](../sources/experiences/exp-o-kd-20260519-0432-1.md) | Replace synchronous FLOAT4 global-to-shared loads for B with cp.async.ca asynchr | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0433-1](../sources/experiences/exp-o-kd-20260519-0433-1.md) | Issue cp.async.ca instructions for the next B tile at the start of the loop body | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0434-1](../sources/experiences/exp-o-kd-20260519-0434-1.md) | Replace synchronous FLOAT4 global-to-shared stores for B with cp.async.ca asynch | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0435-1](../sources/experiences/exp-o-kd-20260519-0435-1.md) | Issue 4 cp.async.ca instructions for the next B tile (16 bytes each, covering 16 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0436-1](../sources/experiences/exp-o-kd-20260519-0436-1.md) | Enable TF32 tensor core path by setting CUBLAS_TF32_TENSOR_OP_MATH as the handle | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0437-1](../sources/experiences/exp-o-kd-20260519-0437-1.md) | Enable TF32 tensor cores by setting CUBLAS_TF32_TENSOR_OP_MATH math mode and CUB | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0438-1](../sources/experiences/exp-o-kd-20260519-0438-1.md) | Set math mode to CUBLAS_TF32_TENSOR_OP_MATH and select CUBLAS_GEMM_DEFAULT_TENSO | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0439-1](../sources/experiences/exp-o-kd-20260519-0439-1.md) | Replace static 3D shared arrays with dynamic extern __shared__ plus manual point | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0440-1](../sources/experiences/exp-o-kd-20260519-0440-1.md) | Pre-compute __cvta_generic_to_shared once on the shared memory base pointers (s_ | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0441-1](../sources/experiences/exp-o-kd-20260519-0441-1.md) | Replace static 3D shared memory arrays with a single extern __shared__ float sme | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0442-1](../sources/experiences/exp-o-kd-20260519-0442-1.md) | Pre-compute shared memory base pointers once outside the loop via __cvta_generic | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0443-1](../sources/experiences/exp-o-kd-20260519-0443-1.md) | Replace scalar f32 loads with float4 vectorized loads so each thread fetches 4 e | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0444-1](../sources/experiences/exp-o-kd-20260519-0444-1.md) | Replace scalar f32 loads with vectorized float4 loads using reinterpret_cast<flo | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0600-1](../sources/experiences/exp-o-kd-20260519-0600-1.md) | Enlarge TileShape to <128,128,64> and WarpShape to <64,64,64>: each threadblock  | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0601-1](../sources/experiences/exp-o-kd-20260519-0601-1.md) | Scale up to TileShape<128,128,64> and WarpShape<64,64,64>, computing 16384 outpu | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0602-1](../sources/experiences/exp-o-kd-20260519-0602-1.md) | Switch the large-M fallback branch to TileShape <128,128,64> with WarpShape <64, | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0651-1](../sources/experiences/exp-o-kd-20260519-0651-1.md) | Replace ^row with ^(row % 8) in the XOR remapping, which constrains the XOR oper | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0653-1](../sources/experiences/exp-o-kd-20260519-0653-1.md) | Replace the XOR operand from the full `row` to `row % 8`, constraining the remap | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0692-1](../sources/experiences/exp-o-kd-20260519-0692-1.md) | Create two explicit CUDA streams (stream1, stream2) and launch each independent  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0693-1](../sources/experiences/exp-o-kd-20260519-0693-1.md) | Add at::cuda::CUDAGuard to pin the device context from the input tensor's device | optimization | sm100 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0716-1](../sources/experiences/exp-o-kd-20260519-0716-1.md) | Track the cumulative tile count across groups via group_total_tiles, and rotate  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0717-1](../sources/experiences/exp-o-kd-20260519-0717-1.md) | Introduce Flatten scheduling with rotating block offsets: track cumulative tiles | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0756-1](../sources/experiences/exp-o-kd-20260519-0756-1.md) | Add hardware-aware dispatch by gating sequential mode on sm_count == 78 (H20 GPU | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0757-1](../sources/experiences/exp-o-kd-20260519-0757-1.md) | Add a hardware-aware guard checking multiProcessorCount == 78 to identify H20 GP | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-1890-1](../sources/experiences/exp-o-kd-20260519-1890-1.md) | Reduce TILE_M from 128 to 64 to exactly match the problem dimension M, eliminati | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1891-1](../sources/experiences/exp-o-kd-20260519-1891-1.md) | Reduce TILE_M from 128 to 32 to better match M=16, cutting per-thread accumulato | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1892-1](../sources/experiences/exp-o-kd-20260519-1892-1.md) | Replace the single config with five M/N-aware config structs (default, M128, M64 | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-1900-1](../sources/experiences/exp-o-kd-20260519-1900-1.md) | Replace two m16n8k16 MMA.sync calls with a single m16n8k32 MMA.sync instruction  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1901-1](../sources/experiences/exp-o-kd-20260519-1901-1.md) | Added a k_size template parameter (defaulting to 16) with a k_size==32 branch th | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1908-1](../sources/experiences/exp-o-kd-20260519-1908-1.md) | Pre-compute sorted_token_ids / top_k once into a separate shared memory array sh | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1909-1](../sources/experiences/exp-o-kd-20260519-1909-1.md) | Right-size the ldmatrix instruction from .x4 to .x2 via a compile-time template  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1910-1](../sources/experiences/exp-o-kd-20260519-1910-1.md) | Replace fixed ldsm4 with templated ldsm<count> using if constexpr to select ldma | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1912-1](../sources/experiences/exp-o-kd-20260519-1912-1.md) | Reduce TILE_M from 16 to 8 to match VALID_ROWS=8, halving per-block shared memor | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1913-1](../sources/experiences/exp-o-kd-20260519-1913-1.md) | Halve block metadata allocation from tb_m*4*2 to tb_m*4 by restructuring how sor | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1913-2](../sources/experiences/exp-o-kd-20260519-1913-2.md) | Allocate B weight tiles and reduction buffer at the same shared memory offset us | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1914-1](../sources/experiences/exp-o-kd-20260519-1914-1.md) | Add m_block_size_8 boolean parameter that computes tb_m = thread_m_blocks * 8 wh | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1925-1](../sources/experiences/exp-o-kd-20260519-1925-1.md) | Always pass the GPU pointer (data_ptr<float>()) directly to the CUTLASS epilogue | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-1928-1](../sources/experiences/exp-o-kd-20260519-1928-1.md) | Unify both branches by always passing scales as a device pointer with a boolean  | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-1931-1](../sources/experiences/exp-o-kd-20260519-1931-1.md) | Replace the hardcoded SM count with a runtime query via cudaDeviceGetAttribute(& | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1932-1](../sources/experiences/exp-o-kd-20260519-1932-1.md) | Query the actual device SM count at runtime via cudaDeviceGetAttribute(&sm_count | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1933-1](../sources/experiences/exp-o-kd-20260519-1933-1.md) | Query the actual device SM count via cutlass::KernelHardwareInfo::query_device_m | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-1935-1](../sources/experiences/exp-o-kd-20260519-1935-1.md) | Replace hardcoded per-N switch dispatch with an adaptive WVSPLIT_TILE heuristic  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1957-1](../sources/experiences/exp-o-kd-20260519-1957-1.md) | Replace the two-step bf16-GEMM + cast-kernel pattern with a single cublasGemmEx  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1958-1](../sources/experiences/exp-o-kd-20260519-1958-1.md) | Replace the two-step bf16-GEMM + cast-kernel pipeline with a single cublasGemmEx | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1959-1](../sources/experiences/exp-o-kd-20260519-1959-1.md) | Replace the two-step bf16-GEMM + cast-kernel pipeline with a single cublasGemmEx | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1960-1](../sources/experiences/exp-o-kd-20260519-1960-1.md) | Eliminate the separate cast kernel entirely by using cublasGemmEx with CUDA_R_32 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1961-1](../sources/experiences/exp-o-kd-20260519-1961-1.md) | Use cublasGemmEx with CUDA_R_32F as the output type so the GEMM writes fp32 resu | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2003-1](../sources/experiences/exp-o-kd-20260519-2003-1.md) | Reconfigure tile to BM=32, BN=64, BK=64, TM=1, TN=2 — smaller BM reduces M-dimen | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2004-1](../sources/experiences/exp-o-kd-20260519-2004-1.md) | Reconfigure tile shape to BM=32, BN=64, BK=64, TM=1, TN=2 so that M=64 produces  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2005-1](../sources/experiences/exp-o-kd-20260519-2005-1.md) | Reduce tile BM from 128 to 64 (with TM from 4 to 2) to cut shared memory per blo | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2006-1](../sources/experiences/exp-o-kd-20260519-2006-1.md) | Add runtime M-dimension-based dispatch that selects one of three CUTLASS tile sh | optimization | sm100 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-2007-1](../sources/experiences/exp-o-kd-20260519-2007-1.md) | Swap the multiplication to compute (N,K)×(K,M)=(1024,1536)×(1536,2) so the large | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2008-1](../sources/experiences/exp-o-kd-20260519-2008-1.md) | Apply swap_ab to reinterpret the GEMM as (N,K)x(K,M), making the large dimension | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2009-1](../sources/experiences/exp-o-kd-20260519-2009-1.md) | Swap A and B matrices (swap_ab) to reinterpret the problem as (N,K)×(K,M) = (102 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2010-1](../sources/experiences/exp-o-kd-20260519-2010-1.md) | Swap A and B operands (swap_ab) to reinterpret the problem as (N,K)x(K,M) with t | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2011-1](../sources/experiences/exp-o-kd-20260519-2011-1.md) | Replace the single M16 config with two fine-grained configs (M4, M64) using swap | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-2012-1](../sources/experiences/exp-o-kd-20260519-2012-1.md) | Swap A and B operands and use CUBLAS_OP_T for both to compute C^T = B^T[N×K] * A | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2013-1](../sources/experiences/exp-o-kd-20260519-2013-1.md) | Swap A and B operands with CUBLAS_OP_T on both, computing C^T = B^T * A^T where  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2014-1](../sources/experiences/exp-o-kd-20260519-2014-1.md) | Add a compile-time swap_ab template parameter that conditionally transposes A an | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-2030-1](../sources/experiences/exp-o-kd-20260519-2030-1.md) | Fuse bias addition into the GEMM epilogue by computing the scaled dot-product re | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2031-1](../sources/experiences/exp-o-kd-20260519-2031-1.md) | Fuse the bias addition into the GEMM kernel epilogue by computing scaled + __hal | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2032-1](../sources/experiences/exp-o-kd-20260519-2032-1.md) | Use swap_ab strategy: compute C^T = B^T * A^T via cublasHgemm with CUBLAS_OP_T o | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2033-1](../sources/experiences/exp-o-kd-20260519-2033-1.md) | Swap A/B matrices in GEMM dispatch when M < 16 or M % 4 != 0, computing B^T * A^ | optimization | sm100 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-2037-1](../sources/experiences/exp-o-kd-20260519-2037-1.md) | Replace two sequential dense mma.sync.m16n8k16 calls with a single mma.sp.sync.a | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2039-1](../sources/experiences/exp-o-kd-20260519-2039-1.md) | Replace the stride computation prob_k/8 with lda/8, where lda is the actual lead | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2041-1](../sources/experiences/exp-o-kd-20260519-2041-1.md) | Add an lda parameter (A.stride(0)) to the Marlin kernel and replace all prob_k-b | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2069-1](../sources/experiences/exp-o-kd-20260519-2069-1.md) | Reduce tile M dimension from 128 to 16 via GemmShape<16,64,128> and WarpShape<16 | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-2070-1](../sources/experiences/exp-o-kd-20260519-2070-1.md) | Match the TileShape M dimension exactly to the problem M=16 by switching to Gemm | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-2071-1](../sources/experiences/exp-o-kd-20260519-2071-1.md) | Match TileShape M dimension exactly to the problem M=32 and increase K to 128 to | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-2072-1](../sources/experiences/exp-o-kd-20260519-2072-1.md) | Match tile M dimension exactly to problem M (TileShape<64,128,128> for M=64), el | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-2073-1](../sources/experiences/exp-o-kd-20260519-2073-1.md) | Switch to TileShape<64,128,128> so that M=96 maps onto two 64-wide tiles (96/64≈ | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-2089-1](../sources/experiences/exp-o-kd-20260519-2089-1.md) | Extend each preprocessor guard to include '|| defined USE_ROCM' so that HIP comp | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2103-1](../sources/experiences/exp-o-kd-20260519-2103-1.md) | Replace persistent whole-tile scheduler with StreamK-style decomposition: split  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2104-1](../sources/experiences/exp-o-kd-20260519-2104-1.md) | Replace whole-tile persistent scheduling with StreamK-style decomposition that b | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2105-1](../sources/experiences/exp-o-kd-20260519-2105-1.md) | Add a TileSchedulerArguments parameter with default initialization and construct | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-2106-1](../sources/experiences/exp-o-kd-20260519-2106-1.md) | Replace persistent tile scheduling with StreamK-style work distribution: launch  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2107-1](../sources/experiences/exp-o-kd-20260519-2107-1.md) | Introduce a K > 3*N heuristic to detect tall-and-skinny shapes where persistent  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2108-1](../sources/experiences/exp-o-kd-20260519-2108-1.md) | Add compile-time detection of StreamKScheduler via cute::is_same_v on TileSchedu | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-2109-1](../sources/experiences/exp-o-kd-20260519-2109-1.md) | Add a runtime heuristic in the dispatch function: if k > 3*n, use StreamKSchedul | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-2110-1](../sources/experiences/exp-o-kd-20260519-2110-1.md) | Convert num_tokens from a runtime function parameter to a compile-time template  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2111-1](../sources/experiences/exp-o-kd-20260519-2111-1.md) | Promote num_tokens from a runtime parameter to a compile-time template parameter | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2112-1](../sources/experiences/exp-o-kd-20260519-2112-1.md) | Replace 8 scalar bf16 loads with a single uint4 (128-bit) vectorized load via re | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2113-1](../sources/experiences/exp-o-kd-20260519-2113-1.md) | Replace per-element scalar bf16 loads with vectorized uint4 reinterpret_cast loa | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2135-1](../sources/experiences/exp-o-kd-20260519-2135-1.md) | Replace the unconditional return false in the SM89 branch with a CUDA version ch | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-2136-1](../sources/experiences/exp-o-kd-20260519-2136-1.md) | Replace the unconditional return false with return CUDA_VERSION >= 12040, enabli | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-2155-1](../sources/experiences/exp-o-kd-20260519-2155-1.md) | Switch to M-adaptive TileShape 16x64x128 with WarpShape 16x64x64 so the tile M d | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-2156-1](../sources/experiences/exp-o-kd-20260519-2156-1.md) | Adapt TileShape to 32x64x128 with WarpShape 32x64x64 to match M=32 exactly, elim | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-2157-1](../sources/experiences/exp-o-kd-20260519-2157-1.md) | Reconfigure TileShape from 128x128x64 to 64x128x128: halving the M tile dimensio | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-2158-1](../sources/experiences/exp-o-kd-20260519-2158-1.md) | Introduce four M-dimension-aware SM80 GEMM config structs with progressively sma | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-2164-1](../sources/experiences/exp-o-kd-20260519-2164-1.md) | Introduce shape-aware tile configuration via select_tile_config() that maps M/N  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2165-1](../sources/experiences/exp-o-kd-20260519-2165-1.md) | Introduce shape-aware tile configuration selection that chooses TileShape<256,12 | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-2166-1](../sources/experiences/exp-o-kd-20260519-2166-1.md) | Replace the single fixed CUTLASS 2.x GEMM instantiation with cutlass_gemm_sm89_i | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-2173-1](../sources/experiences/exp-o-kd-20260519-2173-1.md) | Add a dedicated is_zp_float code path that loads the entire 16-byte zero-point f | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2174-1](../sources/experiences/exp-o-kd-20260519-2174-1.md) | Add a compile-time branched fast path: when zero-points are float (is_zp_float), | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2211-1](../sources/experiences/exp-o-kd-20260519-2211-1.md) | Derive alignment from element bit width using 128 / sizeof_bits<ElementAB>, so f | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2212-1](../sources/experiences/exp-o-kd-20260519-2212-1.md) | Introduce static constexpr AlignmentAB = 128 / sizeof_bits<ElementAB>::value and | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-2213-1](../sources/experiences/exp-o-kd-20260519-2213-1.md) | Remove the split-K heuristic entirely and issue a single cublasSgemm with the fu | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2214-1](../sources/experiences/exp-o-kd-20260519-2214-1.md) | Remove the conditional StreamK/Persistent scheduler heuristic and hardcode a sin | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-2218-1](../sources/experiences/exp-o-kd-20260519-2218-1.md) | Swap the two cuBLAS operands and their transpose flags to compute D = B^T * A^T  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2219-1](../sources/experiences/exp-o-kd-20260519-2219-1.md) | Swap A and B operands by transposing inputs so that M_swap=N=4096 and N_swap=M=1 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2220-1](../sources/experiences/exp-o-kd-20260519-2220-1.md) | Reconfigure tile from 32x32x64 to 32x8x128: narrower N-tile (8 vs 32) spawns 128 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2221-1](../sources/experiences/exp-o-kd-20260519-2221-1.md) | Split into four N-aware configs: narrower N-tile (16 vs 64) for small N reduces  | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-2236-1](../sources/experiences/exp-o-kd-20260519-2236-1.md) | Replace compile-time pipe_stages=4 with a runtime stages parameter set to 2 on m | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2237-1](../sources/experiences/exp-o-kd-20260519-2237-1.md) | Convert pipe_stages from a compile-time constexpr to a runtime parameter (stages | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2237-2](../sources/experiences/exp-o-kd-20260519-2237-2.md) | Add an is_a_8bit flag to the cache size calculation, using 1 byte per element fo | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2238-1](../sources/experiences/exp-o-kd-20260519-2238-1.md) | Introduce an is_a_8bit flag to conditionally select 1 byte per A-matrix element  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2239-1](../sources/experiences/exp-o-kd-20260519-2239-1.md) | Add an is_a_8bit boolean parameter to conditionally select 1 byte per A-matrix e | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2239-2](../sources/experiences/exp-o-kd-20260519-2239-2.md) | Replace the hardcoded global pipe_stages=4 constant with a runtime stages parame | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2240-1](../sources/experiences/exp-o-kd-20260519-2240-1.md) | Replace the compile-time pipe_stages=4 constant with a runtime stages parameter: | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2241-1](../sources/experiences/exp-o-kd-20260519-2241-1.md) | Detect 8-bit activation at runtime via a_type.size_bits() == 8 and conditionally | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2242-1](../sources/experiences/exp-o-kd-20260519-2242-1.md) | Replace hardcoded pipe_stages=4 with a runtime stages parameter set to 2 for Tur | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2243-1](../sources/experiences/exp-o-kd-20260519-2243-1.md) | Reduce pipeline stages from 4 to 2 and parameterize the stages count through fun | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2244-1](../sources/experiences/exp-o-kd-20260519-2244-1.md) | Reduce pipeline stages from 4 to 2 and propagate stages as a runtime parameter t | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2245-1](../sources/experiences/exp-o-kd-20260519-2245-1.md) | Replace the hardcoded compile-time constant pipe_stages=4 with a runtime stages  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2246-1](../sources/experiences/exp-o-kd-20260519-2246-1.md) | Right-size tile and cluster dimensions for small M: reduce tiles from 256x256 to | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2247-1](../sources/experiences/exp-o-kd-20260519-2247-1.md) | Reduce cluster from 4x4 (16 SMs) to 2x1 (2 SMs) and shrink the N tile from 256 t | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2248-1](../sources/experiences/exp-o-kd-20260519-2248-1.md) | Reduce cluster shape from 4x4x1 (16 SMs) to 2x1x1 (2 SMs) to minimize inter-SM c | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2249-1](../sources/experiences/exp-o-kd-20260519-2249-1.md) | Replace type-based KernelTraits<T> specialization with three M-range config stru | optimization | sm100 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-2269-1](../sources/experiences/exp-o-kd-20260519-2269-1.md) | Replace the scalar K-loop with WMMA 16x16x16 tensor-core fragments: each mma_syn | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2271-1](../sources/experiences/exp-o-kd-20260519-2271-1.md) | Split the K dimension into NUM_K_SHARDS=2 shards using a 3D grid (grid.z=2), dou | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2272-1](../sources/experiences/exp-o-kd-20260519-2272-1.md) | Replace the pair of 16x16x16 MFMA calls (.h4[0]/.h4[1] half-vector operands) wit | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2273-1](../sources/experiences/exp-o-kd-20260519-2273-1.md) | Insert an explicit asm volatile("s_waitcnt 0") barrier immediately before __sync | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2274-1](../sources/experiences/exp-o-kd-20260519-2274-1.md) | Add a CHUNKK template parameter (1 or 2) that halves the per-shard K-dimension f | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2281-1](../sources/experiences/exp-o-kd-20260519-2281-1.md) | Replace the cuda::memcpy_async pipeline-based shared memory loads with direct gl | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2282-1](../sources/experiences/exp-o-kd-20260519-2282-1.md) | Change the dispatch condition from feat_in < feat_out to feat_in <= feat_out so  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2283-1](../sources/experiences/exp-o-kd-20260519-2283-1.md) | Fuse all four kernels into a single init_offsets_fused_kernel that writes stride | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2284-1](../sources/experiences/exp-o-kd-20260519-2284-1.md) | Replace torch::full() with torch::empty() (zero-cost allocation, no GPU kernel)  | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-2287-1](../sources/experiences/exp-o-kd-20260519-2287-1.md) | Add explicit GMMA major-mode template parameters (cute::GMMA::Major::MN for B-si | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-2289-1](../sources/experiences/exp-o-kd-20260519-2289-1.md) | Re-enable the min__ clamping guard on kOffcp so that kOffcp = min__(K - A_CHUNK, | optimization | sm90 | cuda-cpp |
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
| [exp-r-20260508-120002-cutlass-int8-opclass](../sources/experiences/exp-r-20260508-120002-cutlass-int8-opclass.md) | CUTLASS 2.x INT8 GEMM compilation fails with namespace errors or static assertio | repair | sm90 | cuda-cpp, cute-dsl |
| [exp-r-20260508-120003-cublasLt-api-misuse](../sources/experiences/exp-r-20260508-120003-cublasLt-api-misuse.md) | exp-r-20260508-120003-cublasLt-api-misuse | repair | sm90 | cuda-cpp |
| [exp-r-20260508-120005-cutlass-int8-alignment](../sources/experiences/exp-r-20260508-120005-cutlass-int8-alignment.md) | CUTLASS INT8 GEMM triggers static assertion: 'Vectors implied by the thread map  | repair | sm90 | cuda-cpp, cute-dsl |
| [exp-r-20260508-160101-dps-signature-contract](../sources/experiences/exp-r-20260508-160101-dps-signature-contract.md) | DPS entrypoint contract mismatch causes compile-time or runtime binding failure  | repair | sm90 | cuda-cpp |
| [exp-r-20260508-160102-gemm-contiguous-stride-correctness](../sources/experiences/exp-r-20260508-160102-gemm-contiguous-stride-correctness.md) | Correctness failures occur when non-contiguous tensors are passed to GEMM kernel | repair | sm90 | cuda-cpp |
| [exp-r-20260508-160103-gemm-lda-ldb-ldc-selfcheck](../sources/experiences/exp-r-20260508-160103-gemm-lda-ldb-ldc-selfcheck.md) | Wrong lda/ldb/ldc or m/n/k assignment leads to incorrect output despite successf | repair | sm90 | cuda-cpp |
| [exp-r-20260508-160104-cuda-linker-symbol-errors](../sources/experiences/exp-r-20260508-160104-cuda-linker-symbol-errors.md) | Build fails at link stage due to unresolved CUDA/cuBLAS/PyTorch symbols after so | repair | sm90 | cuda-cpp |
| [exp-r-20260508-180001-cublas-lda-ldb-correctness](../sources/experiences/exp-r-20260508-180001-cublas-lda-ldb-correctness.md) | cuBLAS GEMM correctness fails silently when lda/ldb use row-major leading dimens | repair | sm90 | cuda-cpp |
| [exp-r-20260508-180002-cutlass-extreme-aspect-ratio](../sources/experiences/exp-r-20260508-180002-cutlass-extreme-aspect-ratio.md) | Switch to cuBLAS cublasGemmEx for these problem sizes. cuBLAS handles all matrix | repair | sm90 | cuda-cpp, cute-dsl |
| [exp-r-20260508-180003-missing-cstdint-for-int-types](../sources/experiences/exp-r-20260508-180003-missing-cstdint-for-int-types.md) | Compilation fails when kernel.h uses int8_t or int32_t types without including < | repair | sm90 | cuda-cpp |
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

## gemv

| ID | Title | Type | Architectures | Languages |
|----|-------|------|--------------|-----------|
| [exp-a-kd-20260519-0540-1](../sources/experiences/exp-a-kd-20260519-0540-1.md) | Vectorize memory access using half2 reinterpret_cast loads (HALF2 macro) to load | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0542-1](../sources/experiences/exp-a-kd-20260519-0542-1.md) | Replace scalar half loads with half2 vectorized loads, processing 4 half element | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0544-1](../sources/experiences/exp-a-kd-20260519-0544-1.md) | Replace scalar half loads with half2 vectorized loads (f16x4 pattern) using rein | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0581-1](../sources/experiences/exp-a-kd-20260519-0581-1.md) | Replace scalar f32 loads with vectorized float4 loads using the FLOAT4 macro, so | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0582-1](../sources/experiences/exp-a-kd-20260519-0582-1.md) | Replace scalar f32 loads with float4 vectorized loads so each thread processes 4 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0585-1](../sources/experiences/exp-a-kd-20260519-0585-1.md) | Split each 32-thread warp into 2 sub-groups of 16 threads (K_WARP_SIZE=16) via l | analysis | sm90 | cuda-cpp |
| [exp-i-kd-20260519-2448-1](../sources/experiences/exp-i-kd-20260519-2448-1.md) | Advance each TensorRef to the correct batch via add_pointer_offset(threadIdx.y * | implementation | sm90 | cuda-cpp, cute-dsl |

## layer-norm

| ID | Title | Type | Architectures | Languages |
|----|-------|------|--------------|-----------|
| [exp-a-kd-20260518-0380](../sources/experiences/exp-a-kd-20260518-0380.md) | fuse_rescale_topk8_bs4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0397](../sources/experiences/exp-a-kd-20260518-0397.md) | nonpow2_15ep_4topk | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0398](../sources/experiences/exp-a-kd-20260518-0398.md) | nonpow2_7ep_2topk | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0400](../sources/experiences/exp-a-kd-20260518-0400.md) | pow2_8ep_2topk | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0470](../sources/experiences/exp-a-kd-20260518-0470.md) | topk8_rows128 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0491](../sources/experiences/exp-a-kd-20260518-0491.md) | fp16_4096_1000tok | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0508](../sources/experiences/exp-a-kd-20260518-0508.md) | small_half_hdim1024 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0582](../sources/experiences/exp-a-kd-20260518-0582.md) | float_h128_std | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0603](../sources/experiences/exp-a-kd-20260518-0603.md) | fp16_hidden4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0612](../sources/experiences/exp-a-kd-20260518-0612.md) | bf16_hidden_4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0661](../sources/experiences/exp-a-kd-20260518-0661.md) | vecload_exp64 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0726](../sources/experiences/exp-a-kd-20260518-0726.md) | renorm_false_8topk | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0779](../sources/experiences/exp-a-kd-20260518-0779.md) | half_aligned_hs4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0780](../sources/experiences/exp-a-kd-20260518-0780.md) | float_aligned_hs4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0804](../sources/experiences/exp-a-kd-20260518-0804.md) | fp8_kv_quant_float | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0899](../sources/experiences/exp-a-kd-20260518-0899.md) | h4096_t256 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0905](../sources/experiences/exp-a-kd-20260518-0905.md) | contiguous_float | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0910](../sources/experiences/exp-a-kd-20260518-0910.md) | strided_half_hs512_stride768 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0985](../sources/experiences/exp-a-kd-20260518-0985.md) | fp16_h4096_t1 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1019](../sources/experiences/exp-a-kd-20260518-1019.md) | renorm_topk2_8exp | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1020](../sources/experiences/exp-a-kd-20260518-1020.md) | renorm_topk4_64exp | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1023](../sources/experiences/exp-a-kd-20260518-1023.md) | renorm_topk2_8exp_fallback | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1164](../sources/experiences/exp-a-kd-20260518-1164.md) | noncontiguous_fp32_int8 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1415](../sources/experiences/exp-a-kd-20260518-1415.md) | float_h4096 | analysis | sm90 | cuda-cpp |
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
| [exp-o-20260328-172621-43b40b9c](../sources/experiences/exp-o-20260328-172621-43b40b9c.md) | Layer Norm optimization: __ldg intrinsic already near-optimal | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0168](../sources/experiences/exp-o-kd-20260518-0168.md) | fuse_rescale_topk6_bs2048 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0175](../sources/experiences/exp-o-kd-20260518-0175.md) | pow2_64ep_4topk | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0214](../sources/experiences/exp-o-kd-20260518-0214.md) | topk8_rows4096 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0269](../sources/experiences/exp-o-kd-20260518-0269.md) | float_h128_neox | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0279](../sources/experiences/exp-o-kd-20260518-0279.md) | bf16_hd1024 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0360](../sources/experiences/exp-o-kd-20260518-0360.md) | fp8_fusion_128 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0408](../sources/experiences/exp-o-kd-20260518-0408.md) | vec_h4096_t256 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0409](../sources/experiences/exp-o-kd-20260518-0409.md) | vec_h4096_t32 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0412](../sources/experiences/exp-o-kd-20260518-0412.md) | strided_half8 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0459](../sources/experiences/exp-o-kd-20260518-0459.md) | renorm_topk4_64exp_fallback | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0592](../sources/experiences/exp-o-kd-20260518-0592.md) | float_h8192 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0676](../sources/experiences/exp-o-kd-20260518-0676.md) | Te 32-bit store to y[], wasting memory bandwidth potential. With K threads all e | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0677](../sources/experiences/exp-o-kd-20260518-0677.md) | Bit load/store, which is suboptimal because GPU memory controllers prefer wider  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0695](../sources/experiences/exp-o-kd-20260518-0695.md) | Topk weight was read and written twice: once for normalization and once for scal | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0699](../sources/experiences/exp-o-kd-20260518-0699.md) | El launch overhead and an extra round-trip through global memory. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0700](../sources/experiences/exp-o-kd-20260518-0700.md) | Und-trip for the top-K weights. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0714](../sources/experiences/exp-o-kd-20260518-0714.md) | Separate kernel launch for the scaling, adding latency and reducing throughput f | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0770](../sources/experiences/exp-o-kd-20260518-0770.md) | Bus width, increasing the total number of memory transactions and reducing effec | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0771](../sources/experiences/exp-o-kd-20260518-0771.md) | R transaction), and many small transactions incur proportionally more overhead p | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0778](../sources/experiences/exp-o-kd-20260518-0778.md) | Ue wider load/store transactions, and the per-element loop creates high loop ove | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0797](../sources/experiences/exp-o-kd-20260518-0797.md) | Assumed divisibility. It also prevented using wider vector sizes (e.g., VEC_SIZE | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0798](../sources/experiences/exp-o-kd-20260518-0798.md) | . Since rms_norm is memory-latency bound, having fewer concurrent blocks reduced | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0805](../sources/experiences/exp-o-kd-20260518-0805.md) | Ycle over the topk weight output. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0807](../sources/experiences/exp-o-kd-20260518-0807.md) | Kernel launch and global memory read+write. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0829](../sources/experiences/exp-o-kd-20260518-0829.md) | On or layout transformations, causing incorrect memory addressing and wrong resu | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0840](../sources/experiences/exp-o-kd-20260518-0840.md) | Ses into wider vector loads, and packed half2/bfloat162 arithmetic was not explo | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0861](../sources/experiences/exp-o-kd-20260518-0861.md) | Slot for a value that is entirely determined by the scalar_out_t template type a | optimization | sm90 | cuda-cpp |
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
| [exp-r-20260508-120004-bf16-intrinsic-undefined](../sources/experiences/exp-r-20260508-120004-bf16-intrinsic-undefined.md) | Direct use of __bfloat162float() or __float2bfloat16() in .cu files causes 'iden | repair | sm90 | cuda-cpp |

## quantization

| ID | Title | Type | Architectures | Languages |
|----|-------|------|--------------|-----------|
| [exp-a-kd-20260519-0782-1](../sources/experiences/exp-a-kd-20260519-0782-1.md) | Replace the triple-chevron launch with cudaLaunchKernelEx and set cudaLaunchAttr | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0816-1](../sources/experiences/exp-a-kd-20260519-0816-1.md) | Add a bool IS_COLUMN_MAJOR template parameter (defaulting to false) and use if c | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0887-1](../sources/experiences/exp-a-kd-20260519-0887-1.md) | Replace scalar half loads with 16-byte vector loads via vec_t<T,8>::cast_load (m | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0887-2](../sources/experiences/exp-a-kd-20260519-0887-2.md) | Replace the shared-memory tree reduction with a warp-shuffle GroupReduceMax usin | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0887-3](../sources/experiences/exp-a-kd-20260519-0887-3.md) | Pack 16 groups per block using 16 threads per group (16 × 16 = 256 threads/block | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0968-1](../sources/experiences/exp-a-kd-20260519-0968-1.md) | Pad shared memory stride from 16 to 17 (s_absmax[16][17]) to eliminate potential | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0972-1](../sources/experiences/exp-a-kd-20260519-0972-1.md) | Replace the 4-step looped reduction with a fully unrolled WarpReduce helper that | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1720-1](../sources/experiences/exp-a-kd-20260519-1720-1.md) | Replaced scalar loop with vectorize_with_alignment<16> to batch 16 float loads i | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1854-1](../sources/experiences/exp-a-kd-20260519-1854-1.md) | Replace the single kernel launch with a chunked loop that iterates over ky in bl | analysis | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0737-1](../sources/experiences/exp-o-kd-20260519-0737-1.md) | Bundle 16 groups into each block with 256 threads (8 warps) instead of 1 group w | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0738-1](../sources/experiences/exp-o-kd-20260519-0738-1.md) | Consolidate 16 groups per block with 256 threads (8 warps), mapping threads via  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0762-1](../sources/experiences/exp-o-kd-20260519-0762-1.md) | Cache input data in dynamically-allocated shared memory during Pass-1 with 32-by | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1865-1](../sources/experiences/exp-o-kd-20260519-1865-1.md) | Replace the raw m grid dimension with effectiveRows = round_up(m, 128), launchin | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2028-1](../sources/experiences/exp-o-kd-20260519-2028-1.md) | Replace atomicOr with direct byte-level writes via reinterpret_cast<uint8_t*>, w | optimization | sm90 | cuda-cpp |

## reduction

| ID | Title | Type | Architectures | Languages |
|----|-------|------|--------------|-----------|
| [exp-a-20260324-085331-7e045fdc](../sources/experiences/exp-a-20260324-085331-7e045fdc.md) | 请先调用 rag_search_experiences，查询与 'cuda shared memory bank conflict reduction' 相关的历史经验，总结找到的模式和建议，然后 finish。不要修改代码，不要使用
  web_search。 | analysis | sm90 | cuda-cpp |
| [exp-a-20260324-091458-7e045fdc](../sources/experiences/exp-a-20260324-091458-7e045fdc.md) | 请先调用 rag_search_experiences，查询与 'cuda shared memory bank conflict reduction' 相关的历史经验，总结找到的模式和建议，然后 finish。不要修改代码，不要使用
  web_search。 | analysis | sm90 | cuda-cpp |
| [exp-a-20260325-100250-12da447b](../sources/experiences/exp-a-20260325-100250-12da447b.md) | ## Task
Create v4 of the top-k sampling kernel for TK_09. The goal is to reduce kernel latency (currently ~4.7ms for all | analysis | sm90 | cuda-cpp |
| [exp-a-20260325-144943-f5b0965a](../sources/experiences/exp-a-20260325-144943-f5b0965a.md) | ## Task
Seed a pure CUDA kernel from baseline for RN_06 rms_norm task

## Goal
Create kernel.cu in attempt dir, strip al | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0011](../sources/experiences/exp-a-kd-20260518-0011.md) | double_elect | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0015](../sources/experiences/exp-a-kd-20260518-0015.md) | half_N8 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0020](../sources/experiences/exp-a-kd-20260518-0020.md) | long_seq | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0021](../sources/experiences/exp-a-kd-20260518-0021.md) | normal_lse | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0022](../sources/experiences/exp-a-kd-20260518-0022.md) | nan_lse | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0025](../sources/experiences/exp-a-kd-20260518-0025.md) | workspace_reduction_H128_D512 | analysis | sm100 | cuda-cpp |
| [exp-a-kd-20260518-0026](../sources/experiences/exp-a-kd-20260518-0026.md) | two_kernel_dispatch_H128_D512 | analysis | sm100 | cuda-cpp |
| [exp-a-kd-20260518-0037](../sources/experiences/exp-a-kd-20260518-0037.md) | gelu_erff_half | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0041](../sources/experiences/exp-a-kd-20260518-0041.md) | cache_op_hint | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0042](../sources/experiences/exp-a-kd-20260518-0042.md) | double_buffer_warp | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-0054](../sources/experiences/exp-a-kd-20260518-0054.md) | float_x4 | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-0056](../sources/experiences/exp-a-kd-20260518-0056.md) | float_epilogue | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-0057](../sources/experiences/exp-a-kd-20260518-0057.md) | partitions1 | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-0059](../sources/experiences/exp-a-kd-20260518-0059.md) | float_only_alpha | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0061](../sources/experiences/exp-a-kd-20260518-0061.md) | float_nobeta_4 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0065](../sources/experiences/exp-a-kd-20260518-0065.md) | conv3d_dgrad_medium | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0066](../sources/experiences/exp-a-kd-20260518-0066.md) | conv3d_dgrad_small | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0068](../sources/experiences/exp-a-kd-20260518-0068.md) | smem_fpi_2 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0069](../sources/experiences/exp-a-kd-20260518-0069.md) | smem_fpi_4 | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-0071](../sources/experiences/exp-a-kd-20260518-0071.md) | frag4_fpp1 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0072](../sources/experiences/exp-a-kd-20260518-0072.md) | sync16_per_iter | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0074](../sources/experiences/exp-a-kd-20260518-0074.md) | Replace row-based add_tile_offset({tile_row_offset, 0}) with flat add_pointer_of | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0075](../sources/experiences/exp-a-kd-20260518-0075.md) | bit_and_128 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0085](../sources/experiences/exp-a-kd-20260518-0085.md) | land_N128 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0093](../sources/experiences/exp-a-kd-20260518-0093.md) | register_spill_fix | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-0105](../sources/experiences/exp-a-kd-20260518-0105.md) | reduction_dispatch | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0112](../sources/experiences/exp-a-kd-20260518-0112.md) | small_4warp | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0115](../sources/experiences/exp-a-kd-20260518-0115.md) | many_atomic | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0116](../sources/experiences/exp-a-kd-20260518-0116.md) | scale_after_max | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0121](../sources/experiences/exp-a-kd-20260518-0121.md) | small_head_k64 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0122](../sources/experiences/exp-a-kd-20260518-0122.md) | float_scalar | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0124](../sources/experiences/exp-a-kd-20260518-0124.md) | int32_scalar | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0125](../sources/experiences/exp-a-kd-20260518-0125.md) | remat_basic | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0151](../sources/experiences/exp-a-kd-20260518-0151.md) | The after code adds a full ThreadMap coordinate decomposition (row_idx, group_id | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0152](../sources/experiences/exp-a-kd-20260518-0152.md) | aligned_tile | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0154](../sources/experiences/exp-a-kd-20260518-0154.md) | asymmetric_128x256_k4 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0155](../sources/experiences/exp-a-kd-20260518-0155.md) | Swap the block/thread mapping by exchanging grid dimensions from <<<M, N>>> to < | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0158](../sources/experiences/exp-a-kd-20260518-0158.md) | Fix kCount to 128-bit / 32-bit (float) = 4 instead of 128-bit / 16-bit (half_t)  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0159](../sources/experiences/exp-a-kd-20260518-0159.md) | Reduce kCount from 8 to 4 to double grid blocks (16 to 32) and halve per-thread  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0161](../sources/experiences/exp-a-kd-20260518-0161.md) | pdl_short_chain | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0171](../sources/experiences/exp-a-kd-20260518-0171.md) | half_t_odd7 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0173](../sources/experiences/exp-a-kd-20260518-0173.md) | int8_4x4_transpose | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0175](../sources/experiences/exp-a-kd-20260518-0175.md) | software_transpose | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0178](../sources/experiences/exp-a-kd-20260518-0178.md) | naive_warp_idx | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0179](../sources/experiences/exp-a-kd-20260518-0179.md) | naive_warp_group_idx | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0185](../sources/experiences/exp-a-kd-20260518-0185.md) | float_reduce_4M | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0187](../sources/experiences/exp-a-kd-20260518-0187.md) | tight_loop | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0192](../sources/experiences/exp-a-kd-20260518-0192.md) | warp_idx_divergent | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0194](../sources/experiences/exp-a-kd-20260518-0194.md) | warp_idx_compute | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0196](../sources/experiences/exp-a-kd-20260518-0196.md) | converged_warp_path | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0206](../sources/experiences/exp-a-kd-20260518-0206.md) | maxk128 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0207](../sources/experiences/exp-a-kd-20260518-0207.md) | maxk64 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0215](../sources/experiences/exp-a-kd-20260518-0215.md) | backward_fused_tile | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0222](../sources/experiences/exp-a-kd-20260518-0222.md) | shared_mem_limit | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0226](../sources/experiences/exp-a-kd-20260518-0226.md) | f32_vs_f32x4_batched | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0228](../sources/experiences/exp-a-kd-20260518-0228.md) | f16_vs_f16x2_batched | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0229](../sources/experiences/exp-a-kd-20260518-0229.md) | f16x2_vs_f16x8_pack | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0232](../sources/experiences/exp-a-kd-20260518-0232.md) | f16_1M | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0233](../sources/experiences/exp-a-kd-20260518-0233.md) | f16x2_1M | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0236](../sources/experiences/exp-a-kd-20260518-0236.md) | f32_medium | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0237](../sources/experiences/exp-a-kd-20260518-0237.md) | f32_large | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0238](../sources/experiences/exp-a-kd-20260518-0238.md) | f16_small | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0239](../sources/experiences/exp-a-kd-20260518-0239.md) | f16_medium | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0241](../sources/experiences/exp-a-kd-20260518-0241.md) | f16x2_small | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0243](../sources/experiences/exp-a-kd-20260518-0243.md) | f16x2_large | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0246](../sources/experiences/exp-a-kd-20260518-0246.md) | pack_large | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0247](../sources/experiences/exp-a-kd-20260518-0247.md) | embedding_f32_vs_f32x4 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0249](../sources/experiences/exp-a-kd-20260518-0249.md) | embedding_f16_vs_f16x8 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0250](../sources/experiences/exp-a-kd-20260518-0250.md) | embedding_f16x8_vs_f16x8_pack | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0251](../sources/experiences/exp-a-kd-20260518-0251.md) | flash_attn_split_kv_headdim64_seq256 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0253](../sources/experiences/exp-a-kd-20260518-0253.md) | flash_attn_split_kv_headdim64_seq2048 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0256](../sources/experiences/exp-a-kd-20260518-0256.md) | d64_s512 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0257](../sources/experiences/exp-a-kd-20260518-0257.md) | d64_s2048 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0260](../sources/experiences/exp-a-kd-20260518-0260.md) | flash_attn_d128_N1024 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0263](../sources/experiences/exp-a-kd-20260518-0263.md) | stage2_s512 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0277](../sources/experiences/exp-a-kd-20260518-0277.md) | f16x2_to_x8_large | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0279](../sources/experiences/exp-a-kd-20260518-0279.md) | f32_scalar_vs_f32x4 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0283](../sources/experiences/exp-a-kd-20260518-0283.md) | f32_large | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0284](../sources/experiences/exp-a-kd-20260518-0284.md) | f32_medium | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0288](../sources/experiences/exp-a-kd-20260518-0288.md) | f16x2_medium | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0289](../sources/experiences/exp-a-kd-20260518-0289.md) | f16x8_large | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0294](../sources/experiences/exp-a-kd-20260518-0294.md) | hgemm_tn_1024 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0300](../sources/experiences/exp-a-kd-20260518-0300.md) | hgemm_512 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0301](../sources/experiences/exp-a-kd-20260518-0301.md) | hgemm_1024 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0309](../sources/experiences/exp-a-kd-20260518-0309.md) | M1024_K128 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0314](../sources/experiences/exp-a-kd-20260518-0314.md) | Keep the running sum in a dedicated fp32 accumulator buffer throughout all round | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0315](../sources/experiences/exp-a-kd-20260518-0315.md) | f16_scalar_vs_f16x2 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0316](../sources/experiences/exp-a-kd-20260518-0316.md) | f16x2_vs_f16x8_unpack | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0317](../sources/experiences/exp-a-kd-20260518-0317.md) | f16x8_unpack_vs_f16x8_pack | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0318](../sources/experiences/exp-a-kd-20260518-0318.md) | relu_f32_vs_f32x4 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0319](../sources/experiences/exp-a-kd-20260518-0319.md) | relu_f16_vs_f16x2 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0320](../sources/experiences/exp-a-kd-20260518-0320.md) | relu_f16x2_vs_f16x8 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0321](../sources/experiences/exp-a-kd-20260518-0321.md) | relu_f16x8_vs_f16x8_pack | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0325](../sources/experiences/exp-a-kd-20260518-0325.md) | seq4096_hid512 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0329](../sources/experiences/exp-a-kd-20260518-0329.md) | Replace scalar loads with float4 vectorized loads to coalesce 4 adjacent floats  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0347](../sources/experiences/exp-a-kd-20260518-0347.md) | sgemm128_stage4 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0348](../sources/experiences/exp-a-kd-20260518-0348.md) | sgemm128_cvta | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0349](../sources/experiences/exp-a-kd-20260518-0349.md) | M1024_K512 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0351](../sources/experiences/exp-a-kd-20260518-0351.md) | M512_K128 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0352](../sources/experiences/exp-a-kd-20260518-0352.md) | M1024_K16 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0358](../sources/experiences/exp-a-kd-20260518-0358.md) | f32_N16M | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0359](../sources/experiences/exp-a-kd-20260518-0359.md) | f32_N1M | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0360](../sources/experiences/exp-a-kd-20260518-0360.md) | f16_N16M | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0361](../sources/experiences/exp-a-kd-20260518-0361.md) | f16_N1M | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0373](../sources/experiences/exp-a-kd-20260518-0373.md) | large_batch_fp16 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0378](../sources/experiences/exp-a-kd-20260518-0378.md) | int64_small_256 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0385](../sources/experiences/exp-a-kd-20260518-0385.md) | subwarp_16 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0386](../sources/experiences/exp-a-kd-20260518-0386.md) | scale_compute_many_groups | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0390](../sources/experiences/exp-a-kd-20260518-0390.md) | fp16_256grp_64gs_vec | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0393](../sources/experiences/exp-a-kd-20260518-0393.md) | reduction_512tb | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0394](../sources/experiences/exp-a-kd-20260518-0394.md) | reduction_256tb | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0395](../sources/experiences/exp-a-kd-20260518-0395.md) | twoshot_launch_4gpu | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0396](../sources/experiences/exp-a-kd-20260518-0396.md) | twoshot_launch_8gpu | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0403](../sources/experiences/exp-a-kd-20260518-0403.md) | row_major_fp16_fp8 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0410](../sources/experiences/exp-a-kd-20260518-0410.md) | aligned_128B | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0411](../sources/experiences/exp-a-kd-20260518-0411.md) | aligned_256B | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0412](../sources/experiences/exp-a-kd-20260518-0412.md) | unaligned_136B | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0418](../sources/experiences/exp-a-kd-20260518-0418.md) | float_k4 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0419](../sources/experiences/exp-a-kd-20260518-0419.md) | float_k32 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0421](../sources/experiences/exp-a-kd-20260518-0421.md) | medium_batch_32 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0424](../sources/experiences/exp-a-kd-20260518-0424.md) | small_batch_8 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0431](../sources/experiences/exp-a-kd-20260518-0431.md) | float_full_warp_32 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0437](../sources/experiences/exp-a-kd-20260518-0437.md) | half_64hd_512t | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0438](../sources/experiences/exp-a-kd-20260518-0438.md) | half_2rank_256k | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0450](../sources/experiences/exp-a-kd-20260518-0450.md) | lru_256buf_32miss | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0457](../sources/experiences/exp-a-kd-20260518-0457.md) | smem_occupancy | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0458](../sources/experiences/exp-a-kd-20260518-0458.md) | Replace scalar float loads with float4 vectorized loads (4 floats per thread) to | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0461](../sources/experiences/exp-a-kd-20260518-0461.md) | Replace half2 (64-bit) loads with LDST128BITS 128-bit vectorized loads to fetch  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0466](../sources/experiences/exp-a-kd-20260518-0466.md) | vec_vs_scalar_hidden4096_topk8 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0467](../sources/experiences/exp-a-kd-20260518-0467.md) | small_batch | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0469](../sources/experiences/exp-a-kd-20260518-0469.md) | fill_64K | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0477](../sources/experiences/exp-a-kd-20260518-0477.md) | int8_group64 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0479](../sources/experiences/exp-a-kd-20260518-0479.md) | rmsnorm_hf_8192 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0487](../sources/experiences/exp-a-kd-20260518-0487.md) | twoshot_8ranks_fp16 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0490](../sources/experiences/exp-a-kd-20260518-0490.md) | fp16_512_1000tok | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0492](../sources/experiences/exp-a-kd-20260518-0492.md) | fp16_64_1000tok | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0499](../sources/experiences/exp-a-kd-20260518-0499.md) | reduce_32k_256ep | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0500](../sources/experiences/exp-a-kd-20260518-0500.md) | reduce_8k_256ep | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0510](../sources/experiences/exp-a-kd-20260518-0510.md) | small_experts_8 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0511](../sources/experiences/exp-a-kd-20260518-0511.md) | medium_experts_16 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0519](../sources/experiences/exp-a-kd-20260518-0519.md) | gelu_fp16_4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0523](../sources/experiences/exp-a-kd-20260518-0523.md) | imbalanced_4groups_8cta | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0531](../sources/experiences/exp-a-kd-20260518-0531.md) | launch_bounds_float_4ranks | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0535](../sources/experiences/exp-a-kd-20260518-0535.md) | fp16_large_256tok | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0548](../sources/experiences/exp-a-kd-20260518-0548.md) | float_large | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0554](../sources/experiences/exp-a-kd-20260518-0554.md) | qknorm_fp16_hd128 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0555](../sources/experiences/exp-a-kd-20260518-0555.md) | qknorm_fp16_hd256 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0556](../sources/experiences/exp-a-kd-20260518-0556.md) | float_gs64_ng8192 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0557](../sources/experiences/exp-a-kd-20260518-0557.md) | float_gs256_ng2048 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0569](../sources/experiences/exp-a-kd-20260518-0569.md) | dtn8_bs4 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0586](../sources/experiences/exp-a-kd-20260518-0586.md) | all_layer_4l | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0589](../sources/experiences/exp-a-kd-20260518-0589.md) | stream_hoist_multicall | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0597](../sources/experiences/exp-a-kd-20260518-0597.md) | bf16_blk128_vs_256 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0604](../sources/experiences/exp-a-kd-20260518-0604.md) | fp16_hidden8192 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0605](../sources/experiences/exp-a-kd-20260518-0605.md) | bf16_hd512 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0610](../sources/experiences/exp-a-kd-20260518-0610.md) | fp16_4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0628](../sources/experiences/exp-a-kd-20260518-0628.md) | count_64exp | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0636](../sources/experiences/exp-a-kd-20260518-0636.md) | bf16_hdim8192_large_batch | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0637](../sources/experiences/exp-a-kd-20260518-0637.md) | fp16_hdim4096_large_batch | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0640](../sources/experiences/exp-a-kd-20260518-0640.md) | fp16_hdim512_smem_vs_reload | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0645](../sources/experiences/exp-a-kd-20260518-0645.md) | fp32_256ep16grp | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0658](../sources/experiences/exp-a-kd-20260518-0658.md) | softmax_exp8 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0685](../sources/experiences/exp-a-kd-20260518-0685.md) | sf_offset_m512_n4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0694](../sources/experiences/exp-a-kd-20260518-0694.md) | rms_norm_half_h4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0695](../sources/experiences/exp-a-kd-20260518-0695.md) | float_basic | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0696](../sources/experiences/exp-a-kd-20260518-0696.md) | float_heavy | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0697](../sources/experiences/exp-a-kd-20260518-0697.md) | float_block_1024 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0698](../sources/experiences/exp-a-kd-20260518-0698.md) | float_block_256 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0711](../sources/experiences/exp-a-kd-20260518-0711.md) | fp16x2_cvt_mixed | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0713](../sources/experiences/exp-a-kd-20260518-0713.md) | broadcast_fma | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0714](../sources/experiences/exp-a-kd-20260518-0714.md) | reduce_uint4 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0722](../sources/experiences/exp-a-kd-20260518-0722.md) | scoring_none_8epg | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0723](../sources/experiences/exp-a-kd-20260518-0723.md) | scoring_sigmoid_8epg | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0724](../sources/experiences/exp-a-kd-20260518-0724.md) | ngroup_8 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0729](../sources/experiences/exp-a-kd-20260518-0729.md) | float2_vec_dot | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0733](../sources/experiences/exp-a-kd-20260518-0733.md) | medium_m_64 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0737](../sources/experiences/exp-a-kd-20260518-0737.md) | fp8_quant_256k | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0773](../sources/experiences/exp-a-kd-20260518-0773.md) | not_limited | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0775](../sources/experiences/exp-a-kd-20260518-0775.md) | large_m | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0776](../sources/experiences/exp-a-kd-20260518-0776.md) | half_aligned_4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0777](../sources/experiences/exp-a-kd-20260518-0777.md) | half_aligned_256 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0781](../sources/experiences/exp-a-kd-20260518-0781.md) | fp16_aligned_4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0799](../sources/experiences/exp-a-kd-20260518-0799.md) | large_M_50000 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0800](../sources/experiences/exp-a-kd-20260518-0800.md) | small_M_2048 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0802](../sources/experiences/exp-a-kd-20260518-0802.md) | N1_sYT1_M432 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0803](../sources/experiences/exp-a-kd-20260518-0803.md) | N2_sYT16_M6912 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0808](../sources/experiences/exp-a-kd-20260518-0808.md) | half_hidden_4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0815](../sources/experiences/exp-a-kd-20260518-0815.md) | e8m0_16k | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0829](../sources/experiences/exp-a-kd-20260518-0829.md) | float_sparse | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0838](../sources/experiences/exp-a-kd-20260518-0838.md) | bf16_reduce_direct | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0877](../sources/experiences/exp-a-kd-20260518-0877.md) | mla_decode_bs4_sl256 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0878](../sources/experiences/exp-a-kd-20260518-0878.md) | mla_decode_bs16_sl1024 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0879](../sources/experiences/exp-a-kd-20260518-0879.md) | mla_decode_bs32_sl4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0896](../sources/experiences/exp-a-kd-20260518-0896.md) | weight_preload_hd128 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0903](../sources/experiences/exp-a-kd-20260518-0903.md) | bf16_vec_add | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0904](../sources/experiences/exp-a-kd-20260518-0904.md) | fp16_vec_add | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0909](../sources/experiences/exp-a-kd-20260518-0909.md) | contiguous_half_hs512 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0913](../sources/experiences/exp-a-kd-20260518-0913.md) | m16_n2048_k2048 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0915](../sources/experiences/exp-a-kd-20260518-0915.md) | m128_n2048_k2048 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0917](../sources/experiences/exp-a-kd-20260518-0917.md) | small_m_m4_n3072_k1536 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0918](../sources/experiences/exp-a-kd-20260518-0918.md) | medium_m_m8_n1024_k1024 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0932](../sources/experiences/exp-a-kd-20260518-0932.md) | bf16_256tok_128h | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0933](../sources/experiences/exp-a-kd-20260518-0933.md) | bf16_8tok_128h | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0946](../sources/experiences/exp-a-kd-20260518-0946.md) | fp16_medium_64k | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0948](../sources/experiences/exp-a-kd-20260518-0948.md) | mn128_k7168_gs128 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0964](../sources/experiences/exp-a-kd-20260518-0964.md) | max_par_dispatch | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0986](../sources/experiences/exp-a-kd-20260518-0986.md) | fp16_h4096_t512 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1002](../sources/experiences/exp-a-kd-20260518-1002.md) | safe_values | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1011](../sources/experiences/exp-a-kd-20260518-1011.md) | splitk_large | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1012](../sources/experiences/exp-a-kd-20260518-1012.md) | splitk_small | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1035](../sources/experiences/exp-a-kd-20260518-1035.md) | m96_n16k | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1038](../sources/experiences/exp-a-kd-20260518-1038.md) | fp16_gs128_4kgrp | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1039](../sources/experiences/exp-a-kd-20260518-1039.md) | fp16_gs128_4kgrp | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1040](../sources/experiences/exp-a-kd-20260518-1040.md) | bf16_576_16ktokens | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1041](../sources/experiences/exp-a-kd-20260518-1041.md) | bf16_576_4ktokens | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1046](../sources/experiences/exp-a-kd-20260518-1046.md) | bf16_576_16ktokens_blockloop_vs_direct | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1047](../sources/experiences/exp-a-kd-20260518-1047.md) | bf16_576_4ktokens_blockloop_vs_direct | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1048](../sources/experiences/exp-a-kd-20260518-1048.md) | float_aligned_256 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1049](../sources/experiences/exp-a-kd-20260518-1049.md) | float_aligned_4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1051](../sources/experiences/exp-a-kd-20260518-1051.md) | float_aligned_4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1054](../sources/experiences/exp-a-kd-20260518-1054.md) | float_absmax_aligned_1024 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1057](../sources/experiences/exp-a-kd-20260518-1057.md) | experts_32_block64 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1059](../sources/experiences/exp-a-kd-20260518-1059.md) | block_full_1024 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1060](../sources/experiences/exp-a-kd-20260518-1060.md) | block_partial_256 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1061](../sources/experiences/exp-a-kd-20260518-1061.md) | block_sz_1024 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1062](../sources/experiences/exp-a-kd-20260518-1062.md) | block_sz_256 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1063](../sources/experiences/exp-a-kd-20260518-1063.md) | block_sz_512 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1064](../sources/experiences/exp-a-kd-20260518-1064.md) | rms_block1024 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1065](../sources/experiences/exp-a-kd-20260518-1065.md) | rms_block512 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1066](../sources/experiences/exp-a-kd-20260518-1066.md) | fused_large_batch | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1067](../sources/experiences/exp-a-kd-20260518-1067.md) | fused_small_batch | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1068](../sources/experiences/exp-a-kd-20260518-1068.md) | generic_large_batch | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1069](../sources/experiences/exp-a-kd-20260518-1069.md) | generic_small_batch | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1070](../sources/experiences/exp-a-kd-20260518-1070.md) | block_size_1024 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1071](../sources/experiences/exp-a-kd-20260518-1071.md) | large_block_256 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1072](../sources/experiences/exp-a-kd-20260518-1072.md) | small_block_128 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1073](../sources/experiences/exp-a-kd-20260518-1073.md) | max_block_1024 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1074](../sources/experiences/exp-a-kd-20260518-1074.md) | float_ctx2048 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1084](../sources/experiences/exp-a-kd-20260518-1084.md) | butterfly_reduce | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1098](../sources/experiences/exp-a-kd-20260518-1098.md) | arch_guard_sm75 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1116](../sources/experiences/exp-a-kd-20260518-1116.md) | large_64epg_bs64 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1121](../sources/experiences/exp-a-kd-20260518-1121.md) | half_d512 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1133](../sources/experiences/exp-a-kd-20260518-1133.md) | topk2_epg8 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1135](../sources/experiences/exp-a-kd-20260518-1135.md) | compile_bloat | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1145](../sources/experiences/exp-a-kd-20260518-1145.md) | float_output | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1184](../sources/experiences/exp-a-kd-20260518-1184.md) | small_m_withbias | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-1187](../sources/experiences/exp-a-kd-20260518-1187.md) | warp_reduce_H128_T32 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1188](../sources/experiences/exp-a-kd-20260518-1188.md) | warp_reduce_H128_T128 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1229](../sources/experiences/exp-a-kd-20260518-1229.md) | float_hs4096_gs128 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1230](../sources/experiences/exp-a-kd-20260518-1230.md) | float_hs8192_gs256 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1233](../sources/experiences/exp-a-kd-20260518-1233.md) | float_hs4096_gs128 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1234](../sources/experiences/exp-a-kd-20260518-1234.md) | float_hs8192_gs256 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1243](../sources/experiences/exp-a-kd-20260518-1243.md) | seq8k | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1260](../sources/experiences/exp-a-kd-20260518-1260.md) | absmax_16384 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1265](../sources/experiences/exp-a-kd-20260518-1265.md) | smem_dynamic_4rows | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1266](../sources/experiences/exp-a-kd-20260518-1266.md) | vec_load | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1270](../sources/experiences/exp-a-kd-20260518-1270.md) | fp16_hidden4096_tokens512_block256 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1271](../sources/experiences/exp-a-kd-20260518-1271.md) | fp16_hidden4096_tokens64_block1024 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1273](../sources/experiences/exp-a-kd-20260518-1273.md) | fp32_hidden4096_tokens512_nocast | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1274](../sources/experiences/exp-a-kd-20260518-1274.md) | numLanes_16 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1275](../sources/experiences/exp-a-kd-20260518-1275.md) | numLanes_2 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1276](../sources/experiences/exp-a-kd-20260518-1276.md) | numLanes_4 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1277](../sources/experiences/exp-a-kd-20260518-1277.md) | numLanes_8 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1278](../sources/experiences/exp-a-kd-20260518-1278.md) | multi_warp_64 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1280](../sources/experiences/exp-a-kd-20260518-1280.md) | single_warp_32 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1284](../sources/experiences/exp-a-kd-20260518-1284.md) | float_h4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1294](../sources/experiences/exp-a-kd-20260518-1294.md) | offset_ptr_4k | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1307](../sources/experiences/exp-a-kd-20260518-1307.md) | uniform_chunk | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1313](../sources/experiences/exp-a-kd-20260518-1313.md) | fp16_gs128 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1314](../sources/experiences/exp-a-kd-20260518-1314.md) | fp16_gs64 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1322](../sources/experiences/exp-a-kd-20260518-1322.md) | fp16_alignment | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1332](../sources/experiences/exp-a-kd-20260518-1332.md) | align_offset | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1334](../sources/experiences/exp-a-kd-20260518-1334.md) | experts_8 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1349](../sources/experiences/exp-a-kd-20260518-1349.md) | m64_large_n | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1363](../sources/experiences/exp-a-kd-20260518-1363.md) | warp_reduce_sum_float | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1364](../sources/experiences/exp-a-kd-20260518-1364.md) | warp_reduce_max_float | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1365](../sources/experiences/exp-a-kd-20260518-1365.md) | warp_reduce_sum_half | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1366](../sources/experiences/exp-a-kd-20260518-1366.md) | block_reduce_sum_float | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1367](../sources/experiences/exp-a-kd-20260518-1367.md) | block_reduce_max_float | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1375](../sources/experiences/exp-a-kd-20260518-1375.md) | stages_fp16_turing_4stages | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1386](../sources/experiences/exp-a-kd-20260518-1386.md) | warp_reduce_4warp | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1388](../sources/experiences/exp-a-kd-20260518-1388.md) | smem_large_batch | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1389](../sources/experiences/exp-a-kd-20260518-1389.md) | smem_w8a8 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1392](../sources/experiences/exp-a-kd-20260518-1392.md) | half_medium_M | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1395](../sources/experiences/exp-a-kd-20260518-1395.md) | asm_reduction | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1422](../sources/experiences/exp-a-kd-20260518-1422.md) | half_256tok_40h_128sz | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1454](../sources/experiences/exp-a-kd-20260518-1454.md) | float_8h_128hs | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1455](../sources/experiences/exp-a-kd-20260518-1455.md) | half_8h_128hs | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1469](../sources/experiences/exp-a-kd-20260518-1469.md) | vec_vs_scalar_float_512 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1472](../sources/experiences/exp-a-kd-20260518-1472.md) | small_m_16 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1487](../sources/experiences/exp-a-kd-20260518-1487.md) | scale_transpose_only | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1497](../sources/experiences/exp-a-kd-20260518-1497.md) | shuffle_required_8elts | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0001-1](../sources/experiences/exp-a-kd-20260519-0001-1.md) | Load directly into source array elements by reinterpret_cast-ing the Array struc | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0022-1](../sources/experiences/exp-a-kd-20260519-0022-1.md) | Replace max() with fmax() in both the per-thread LSE maximum loop and the warp s | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0031-1](../sources/experiences/exp-a-kd-20260519-0031-1.md) | Add !is_fused_reduction guard to the reduction kernel launch condition so the se | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0074-1](../sources/experiences/exp-a-kd-20260519-0074-1.md) | Replace row-based add_tile_offset with add_pointer_offset(kSmemPointerOffset) co | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0085-1](../sources/experiences/exp-a-kd-20260519-0085-1.md) | Reinterpret the packed 1-bit storage as a byte pointer and scan entire bytes: if | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0086-1](../sources/experiences/exp-a-kd-20260519-0086-1.md) | Replace 32 per-element bit extractions and AND operations with 4 byte-level read | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0087-1](../sources/experiences/exp-a-kd-20260519-0087-1.md) | Replace 128 per-element bit extractions with 16 byte-level reads and a simple no | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0088-1](../sources/experiences/exp-a-kd-20260519-0088-1.md) | Replace 32 per-element bit extractions with 4 byte-level zero-checks: since a by | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0105-1](../sources/experiences/exp-a-kd-20260519-0105-1.md) | Replace the single cooperative reduction kernel with a dispatch to a separate re | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0106-1](../sources/experiences/exp-a-kd-20260519-0106-1.md) | Pad each threadblock's workspace region up to the next 128-byte cacheline bounda | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0151-1](../sources/experiences/exp-a-kd-20260519-0151-1.md) | The after code adds an OOB guard via ThreadMap coordinate decomposition (modulo/ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0152-1](../sources/experiences/exp-a-kd-20260519-0152-1.md) | The after code adds OOB guard infrastructure with ThreadMap coordinate decomposi | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0154-1](../sources/experiences/exp-a-kd-20260519-0154-1.md) | Swap problem dimensions from (M, N) to (N, M) so blockIdx.x maps to original col | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0155-1](../sources/experiences/exp-a-kd-20260519-0155-1.md) | Swap grid/block dimensions to <<<N=1024, M=64>>> and reverse the indexing from r | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0158-1](../sources/experiences/exp-a-kd-20260519-0158-1.md) | Correct kCount to match ElementWorkspace (float, 32-bit): 128/32=4, which halves | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260519-0159-1](../sources/experiences/exp-a-kd-20260519-0159-1.md) | Reduce kCount from 8 to 4 (TILE_COLS from 256 to 128), doubling the number of th | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0184-1](../sources/experiences/exp-a-kd-20260519-0184-1.md) | Replace the multi-instruction isnan+branch sequence with a single PTX max.NaN.f3 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0185-1](../sources/experiences/exp-a-kd-20260519-0185-1.md) | Replace the multi-instruction isnan+ternary sequence with a single PTX max.NaN.f | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0316-1](../sources/experiences/exp-a-kd-20260519-0316-1.md) | Split the key range into 64 chunks, launch one CTA per chunk so 64×256=16 384 th | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0317-1](../sources/experiences/exp-a-kd-20260519-0317-1.md) | Split the 512-key reduction into 2 partial blocks per output using a 2D grid (di | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0328-1](../sources/experiences/exp-a-kd-20260519-0328-1.md) | Fuse the reduction and consumer into a single kernel so the shared-memory reduct | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0329-1](../sources/experiences/exp-a-kd-20260519-0329-1.md) | Cast input pointers to float4 and load four elements per LDG instruction, accumu | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0329-2](../sources/experiences/exp-a-kd-20260519-0329-2.md) | Replace shared-memory tree reduction with warp-level __shfl_xor_sync reduction ( | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0457-1](../sources/experiences/exp-a-kd-20260519-0457-1.md) | Replace scalar float loads with float4 vectorized loads (128-bit transactions) s | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0458-1](../sources/experiences/exp-a-kd-20260519-0458-1.md) | Replace scalar float loads with float4 vectorized loads (4 floats per thread) to | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0459-1](../sources/experiences/exp-a-kd-20260519-0459-1.md) | Replace scalar half loads with half2 vectorized loads so each thread processes t | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0460-1](../sources/experiences/exp-a-kd-20260519-0460-1.md) | Vectorize memory access using half2 loads (2 half elements per thread via reinte | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0461-1](../sources/experiences/exp-a-kd-20260519-0461-1.md) | Widen per-thread memory access from half2 (64-bit) to LDST128BITS/float4 (128-bi | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0462-1](../sources/experiences/exp-a-kd-20260519-0462-1.md) | Increase per-thread vectorization to 8 half elements using 128-bit LDST128BITS ( | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0545-1](../sources/experiences/exp-a-kd-20260519-0545-1.md) | Use int4 vectorized loads (128-bit) to read 4 integers per thread in a single me | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0781-1](../sources/experiences/exp-a-kd-20260519-0781-1.md) | Add PDL (Programmatic Dependent Launch) barriers — cudaGridDependencySynchronize | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0793-1](../sources/experiences/exp-a-kd-20260519-0793-1.md) | After code replaces the two-kernel pipeline with a single cooperative multi-bloc | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0795-1](../sources/experiences/exp-a-kd-20260519-0795-1.md) | Reorganize reduction using int4 vector loads (4× int32 per access) with warp-lev | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0796-1](../sources/experiences/exp-a-kd-20260519-0796-1.md) | Template GroupReduceMax on THREADS_PER_SUBWARP and guard each shuffle step with  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0799-1](../sources/experiences/exp-a-kd-20260519-0799-1.md) | Replace the shared memory max-reduction with __shfl_xor_sync warp shuffle reduct | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0804-1](../sources/experiences/exp-a-kd-20260519-0804-1.md) | Make the trailing __syncthreads() conditional via if constexpr (start || need_fe | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0805-1](../sources/experiences/exp-a-kd-20260519-0805-1.md) | Templatize block_barrier on <bool start, bool need_fence> and use if constexpr t | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0806-1](../sources/experiences/exp-a-kd-20260519-0806-1.md) | Replace the two while-loops with a direct min/divUp formula: threads_per_block = | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0807-1](../sources/experiences/exp-a-kd-20260519-0807-1.md) | Replace the iterative while-loop block/thread search with direct std::min/divUp  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0828-1](../sources/experiences/exp-a-kd-20260519-0828-1.md) | Replace shared-memory butterfly reduction with a templated reduce_sum<kNumThread | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0829-1](../sources/experiences/exp-a-kd-20260519-0829-1.md) | Replace shared-memory butterfly reduction with a parameterized warp shuffle redu | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0830-1](../sources/experiences/exp-a-kd-20260519-0830-1.md) | Parameterize reduce_sum with a compile-time kNumThreads template parameter, comp | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0838-1](../sources/experiences/exp-a-kd-20260519-0838-1.md) | Replace serial global-memory scan with cooperative shared-memory load (moe_block | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0842-1](../sources/experiences/exp-a-kd-20260519-0842-1.md) | Parameterize the reduction via a kNumThreads non-type template parameter with st | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0843-1](../sources/experiences/exp-a-kd-20260519-0843-1.md) | Parameterize the reduction with a kNumThreads template and switch to __shfl_xor_ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0849-1](../sources/experiences/exp-a-kd-20260519-0849-1.md) | Replace one-shot single-pass reduce with two-shot reduce-then-gather: Phase 1 re | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0858-1](../sources/experiences/exp-a-kd-20260519-0858-1.md) | Fuse all three operations (shuffle, multiply, sum-reduce) into a single kernel w | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0859-1](../sources/experiences/exp-a-kd-20260519-0859-1.md) | Fuse all three operations into a single kernel where each thread block handles o | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0860-1](../sources/experiences/exp-a-kd-20260519-0860-1.md) | Fuse the three separate kernels into a single kernel that reads input directly v | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0869-1](../sources/experiences/exp-a-kd-20260519-0869-1.md) | Replace hardcoded float accumulator with type-generic opmath_t<scalar_t> pattern | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0870-1](../sources/experiences/exp-a-kd-20260519-0870-1.md) | Replace the hardcoded float accumulator with an opmath_t<double>=double accumula | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0871-1](../sources/experiences/exp-a-kd-20260519-0871-1.md) | Replace the compile-time TOPK template with a runtime int topk_num parameter and | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0897-1](../sources/experiences/exp-a-kd-20260519-0897-1.md) | Replace the embedded pointer array with a RankData* indirection to a GPU-residen | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0898-1](../sources/experiences/exp-a-kd-20260519-0898-1.md) | Merge the D2D copy into the reduction kernel using a compile-time COPY_INPUT tem | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0910-1](../sources/experiences/exp-a-kd-20260519-0910-1.md) | Replace atomicAdd-to-global-memory with CUB BlockReduce, which performs the sum  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0911-1](../sources/experiences/exp-a-kd-20260519-0911-1.md) | Replace the global atomicAdd reduction with CUB BlockReduce, which performs a co | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0921-1](../sources/experiences/exp-a-kd-20260519-0921-1.md) | Adapt thread count to 256 and experts_per_warp to 8 for small expert counts, red | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0922-1](../sources/experiences/exp-a-kd-20260519-0922-1.md) | Reduce thread count to 512 and experts_per_warp to 16 (matching num_experts=16)  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0942-1](../sources/experiences/exp-a-kd-20260519-0942-1.md) | Add __launch_bounds__(512, 1) to the kernel declaration, informing NVCC that max | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0959-1](../sources/experiences/exp-a-kd-20260519-0959-1.md) | Extract the inline two-phase block reduction (warpReduceMax → shared memory inte | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0960-1](../sources/experiences/exp-a-kd-20260519-0960-1.md) | Extract the inline block reduction logic (shared memory allocation, lane/warp ID | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0963-1](../sources/experiences/exp-a-kd-20260519-0963-1.md) | Replace static 2D shared memory with extern dynamically-allocated 1D shared memo | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0964-1](../sources/experiences/exp-a-kd-20260519-0964-1.md) | Replace static 2D shared memory with extern __shared__ dynamic allocation and fl | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0973-1](../sources/experiences/exp-a-kd-20260519-0973-1.md) | Replace scalar per-element loads with __align__(16) array_t<half,8> packed 128-b | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0974-1](../sources/experiences/exp-a-kd-20260519-0974-1.md) | Replace scalar half loads with 128-bit aligned packed types (array_t<half,8>) th | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0986-1](../sources/experiences/exp-a-kd-20260519-0986-1.md) | Replaced 256 scalar bf16 threads with 32 vectorized threads using flashinfer::ve | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0987-1](../sources/experiences/exp-a-kd-20260519-0987-1.md) | Replace scalar per-element loads and stores with flashinfer::vec_t vectorized 12 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0987-2](../sources/experiences/exp-a-kd-20260519-0987-2.md) | Accumulate in float32 via native FFMA instructions using unrolled vector multipl | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1004-1](../sources/experiences/exp-a-kd-20260519-1004-1.md) | Replace 4096 scalar 2-byte loads with 512 vectorized 128-bit loads via uint4 rei | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1005-1](../sources/experiences/exp-a-kd-20260519-1005-1.md) | Replace scalar __half loads with 128-bit vectorized loads via uint4 reinterpret_ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1028-1](../sources/experiences/exp-a-kd-20260519-1028-1.md) | Replace contiguous-block iteration with stride-based (grid-stride) iteration whe | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1029-1](../sources/experiences/exp-a-kd-20260519-1029-1.md) | Replace contiguous-block iteration with grid-stride loop (tid = threadIdx.x, str | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1032-1](../sources/experiences/exp-a-kd-20260519-1032-1.md) | Replace the two-kernel atomicAdd pipeline with a single kernel using per-thread  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1061-1](../sources/experiences/exp-a-kd-20260519-1061-1.md) | Replace scalar bf16 loads/stores with 128-bit uint4 vectorized loads/stores via  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1062-1](../sources/experiences/exp-a-kd-20260519-1062-1.md) | Replace scalar bf16 load/store with uint4 (Pack16B) vectorized load/store proces | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1063-1](../sources/experiences/exp-a-kd-20260519-1063-1.md) | Replaced block-level dispatch with warp-per-token dispatch: each warp (32 lanes) | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1064-1](../sources/experiences/exp-a-kd-20260519-1064-1.md) | The warp-per-token kernel assigns one warp per token via warp_id/lane decomposit | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1073-1](../sources/experiences/exp-a-kd-20260519-1073-1.md) | Replace scalar per-element half loads and stores with half2 vectorized access vi | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1074-1](../sources/experiences/exp-a-kd-20260519-1074-1.md) | Vectorize the MoE reduce kernel using half2 loads with vec_size=8: replace scala | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1127-1](../sources/experiences/exp-a-kd-20260519-1127-1.md) | Fuse the sigmoid+bias computation directly into the candidates kernel by reading | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1132-1](../sources/experiences/exp-a-kd-20260519-1132-1.md) | Replace __shfl_down_sync sequential reduction plus explicit __shfl_sync broadcas | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1133-1](../sources/experiences/exp-a-kd-20260519-1133-1.md) | Replace __shfl_down_sync reduction plus __shfl_sync broadcast with __shfl_xor_sy | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1134-1](../sources/experiences/exp-a-kd-20260519-1134-1.md) | Replace integer bit-shift (>>5) with float division (/32.f) in the cross-warp gu | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1135-1](../sources/experiences/exp-a-kd-20260519-1135-1.md) | Replace integer bit-shift (>>5) with float division (/32.f) so the warp count be | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1151-1](../sources/experiences/exp-a-kd-20260519-1151-1.md) | Replace tree reduction with sequential reduction (3-step chain: c=add(v.x,v.y),  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1152-1](../sources/experiences/exp-a-kd-20260519-1152-1.md) | Replace the mul-then-add pattern with FMA-accumulated chaining: compute mul(a.x, | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1161-1](../sources/experiences/exp-a-kd-20260519-1161-1.md) | Convert the runtime n_group parameter to a compile-time template parameter NGrou | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1162-1](../sources/experiences/exp-a-kd-20260519-1162-1.md) | Convert the runtime n_group parameter into a compile-time template parameter NGr | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1166-1](../sources/experiences/exp-a-kd-20260519-1166-1.md) | Replace the generic dot<T> template with a specialized dot(float2,float2) overlo | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1167-1](../sources/experiences/exp-a-kd-20260519-1167-1.md) | Replace the generic template chain with a specialized dot(float, float) overload | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1173-1](../sources/experiences/exp-a-kd-20260519-1173-1.md) | Move the max-abs-value reduction to the CPU via a sequential scan over the alrea | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1174-1](../sources/experiences/exp-a-kd-20260519-1174-1.md) | Replace the GPU-based segmented max reduction with a CPU pre-computed scale from | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1184-1](../sources/experiences/exp-a-kd-20260519-1184-1.md) | Replace the two-pass global memory access pattern with a single cp.async bulk lo | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1184-2](../sources/experiences/exp-a-kd-20260519-1184-2.md) | Replace the sequential scan with warp-level parallel counting: 32 lanes each cou | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1189-1](../sources/experiences/exp-a-kd-20260519-1189-1.md) | Introduced vectorized_process helper using float4 wide loads with alignment hand | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1190-1](../sources/experiences/exp-a-kd-20260519-1190-1.md) | Replace the scalar stride loop with a generic vectorized_process<float4> templat | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1209-1](../sources/experiences/exp-a-kd-20260519-1209-1.md) | Overlap the Phase 1 tile buffer (sh_b) and Phase 2 reduction buffer (sh_red) at  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1210-1](../sources/experiences/exp-a-kd-20260519-1210-1.md) | Overlap sh_b and sh_red to the same shared memory region (both alias smem + TB_M | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1222-1](../sources/experiences/exp-a-kd-20260519-1222-1.md) | Split the monolithic single-block kernel into two kernels: (1) an align-only ker | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1236-1](../sources/experiences/exp-a-kd-20260519-1236-1.md) | Replace truncating division (N/nPrRnd) with ceiling division ((N+nPrRnd-1)/nPrRn | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1237-1](../sources/experiences/exp-a-kd-20260519-1237-1.md) | Replace sparse hardcoded division/check logic with a full-range loop using ceili | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1238-1](../sources/experiences/exp-a-kd-20260519-1238-1.md) | Replace the hard-coded truncating-division mindiv with a loop-based ceiling-divi | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1239-1](../sources/experiences/exp-a-kd-20260519-1239-1.md) | Increase UNRL from 2 to 4 so each thread processes 128 K-elements per iteration  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1239-2](../sources/experiences/exp-a-kd-20260519-1239-2.md) | Set YTILE=1 to eliminate the outer row-loop entirely, so each wavefront processe | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1240-1](../sources/experiences/exp-a-kd-20260519-1240-1.md) | Increase YTILE from 2 to 4 via an adaptive heuristic (sYT=ceil(6912/(108*4))=16) | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1266-1](../sources/experiences/exp-a-kd-20260519-1266-1.md) | Remove both __syncwarp() calls: the first is unnecessary because the preceding l | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1267-1](../sources/experiences/exp-a-kd-20260519-1267-1.md) | Remove both __syncwarp() barriers because warp shuffle intrinsics (__shfl_xor_sy | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1271-1](../sources/experiences/exp-a-kd-20260519-1271-1.md) | Cap the thread block count at 36 via a BLOCK_LIMIT constant, reducing total atom | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1272-1](../sources/experiences/exp-a-kd-20260519-1272-1.md) | Cap the grid size to 36 blocks via a BLOCK_LIMIT constant, reducing the number o | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1275-1](../sources/experiences/exp-a-kd-20260519-1275-1.md) | Use a packed array_t<nv_bfloat16,8> type with __align__(16) to load 8 bf16 value | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1276-1](../sources/experiences/exp-a-kd-20260519-1276-1.md) | Replace scalar element-wise loads with packed 128-bit array_t<half,8> loads (8 h | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1310-1](../sources/experiences/exp-a-kd-20260519-1310-1.md) | Reinterpret float pointers as uint4 (128-bit) to load and store 4 floats per ins | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1311-1](../sources/experiences/exp-a-kd-20260519-1311-1.md) | Replace scalar half loads with 128-bit uint4 vectorized loads that fetch 8 half  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1323-1](../sources/experiences/exp-a-kd-20260519-1323-1.md) | Replace conditional can_vectorize dispatch with unconditional vectorize_read_wit | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1324-1](../sources/experiences/exp-a-kd-20260519-1324-1.md) | Replace the conditional thread_max_vec call with vectorize_read_with_alignment,  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1325-1](../sources/experiences/exp-a-kd-20260519-1325-1.md) | Replace the conditional can_vectorize branch with vectorize_read_with_alignment, | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1375-1](../sources/experiences/exp-a-kd-20260519-1375-1.md) | Make TOPK a compile-time template parameter and add #pragma unroll so the compil | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1375-2](../sources/experiences/exp-a-kd-20260519-1375-2.md) | Use __ldg() intrinsic to route read-only input loads through the GPU's dedicated | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1376-1](../sources/experiences/exp-a-kd-20260519-1376-1.md) | Make TOPK a compile-time template parameter to enable #pragma unroll, fully unro | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1441-1](../sources/experiences/exp-a-kd-20260519-1441-1.md) | The before code uses PTX createpolicy.fractional.L2::evict_first to mark 100% of | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1442-1](../sources/experiences/exp-a-kd-20260519-1442-1.md) | Remove the L2::evict_first cache hint and use plain cp.async.cg.shared.global wi | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1448-1](../sources/experiences/exp-a-kd-20260519-1448-1.md) | Replace single-kernel atomicAdd with two kernels: per-shard plain writes to non- | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1485-1](../sources/experiences/exp-a-kd-20260519-1485-1.md) | Replace the scalar absmax for-loop with vectorize_read_with_alignment<16> templa | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1486-1](../sources/experiences/exp-a-kd-20260519-1486-1.md) | Replace the scalar loop with vectorize_read_with_alignment<16> template that loa | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1487-1](../sources/experiences/exp-a-kd-20260519-1487-1.md) | Replace the scalar element-by-element min/max loop with vectorize_read_with_alig | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1488-1](../sources/experiences/exp-a-kd-20260519-1488-1.md) | Replace the scalar loop with vectorize_read_with_alignment<16> which loads 128-b | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1491-1](../sources/experiences/exp-a-kd-20260519-1491-1.md) | Replace scalar strided loop with vectorize_read_with_alignment<16> that loads 16 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1492-1](../sources/experiences/exp-a-kd-20260519-1492-1.md) | Replace the scalar stride loop with vectorize_read_with_alignment<16> to load 16 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1496-1](../sources/experiences/exp-a-kd-20260519-1496-1.md) | Replace custom shared-memory blockReduceMax with CUB BlockReduce, which uses war | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1497-1](../sources/experiences/exp-a-kd-20260519-1497-1.md) | Replace the hand-written sequential-halving blockReduceMax with CUB BlockReduce, | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1498-1](../sources/experiences/exp-a-kd-20260519-1498-1.md) | Replace the hand-rolled two-phase block reduction (warp shuffle + shared memory  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1499-1](../sources/experiences/exp-a-kd-20260519-1499-1.md) | The custom vllm::blockReduceMax allocates only maxActiveLanes=32 floats (128 byt | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1507-1](../sources/experiences/exp-a-kd-20260519-1507-1.md) | Replace the custom function-pointer-based blockReduceSum with CUB's cub::BlockRe | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1508-1](../sources/experiences/exp-a-kd-20260519-1508-1.md) | Replace the custom blockReduceSum with cub::BlockReduce<float,1024>.Reduce(val,  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1509-1](../sources/experiences/exp-a-kd-20260519-1509-1.md) | Replace the custom blockReduceSum with if-else dispatch with a single cub::Block | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1510-1](../sources/experiences/exp-a-kd-20260519-1510-1.md) | Replace custom blockReduceMax with cub::BlockReduce<float,1024>.Reduce using cub | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1513-1](../sources/experiences/exp-a-kd-20260519-1513-1.md) | Wrap min() in an explicit __device__ inline min__(uint32_t, uint32_t) function t | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1521-1](../sources/experiences/exp-a-kd-20260519-1521-1.md) | Replace hardcoded constants with WARP_SIZE/2 for the initial mask and introduce  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1552-1](../sources/experiences/exp-a-kd-20260519-1552-1.md) | Launch <<<2,1024>>> instead of <<<1,1024>>>, delegating sorted_token_ids initial | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1553-1](../sources/experiences/exp-a-kd-20260519-1553-1.md) | Launch two threadblocks instead of one: block 1 handles the sorted_token_ids glo | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1559-1](../sources/experiences/exp-a-kd-20260519-1559-1.md) | Replace the hardcoded stride expression (seq_idx * num_heads * HEAD_SIZE) with a | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1564-1](../sources/experiences/exp-a-kd-20260519-1564-1.md) | Add a loop-bound condition ib0 + ir * BPW / QR < bpr to the inner ir loop so tha | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1565-1](../sources/experiences/exp-a-kd-20260519-1565-1.md) | Remove the explicit __float2half intrinsic and rely on implicit float-to-half co | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1591-1](../sources/experiences/exp-a-kd-20260519-1591-1.md) | Replace per-element atomicAdd inside the strided loop with register-local accumu | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1592-1](../sources/experiences/exp-a-kd-20260519-1592-1.md) | Accumulate match counts in a per-thread register variable across all loop iterat | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1597-1](../sources/experiences/exp-a-kd-20260519-1597-1.md) | Replace the per-thread 2D token-count matrix with a warp-partitioned static shar | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1597-2](../sources/experiences/exp-a-kd-20260519-1597-2.md) | Replace per-thread offset tracking with atomicAdd on a flat local_offsets array: | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1666-1](../sources/experiences/exp-a-kd-20260519-1666-1.md) | Replaces single CUB BlockReduce with groupwise shared-memory reduction: partitio | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1670-1](../sources/experiences/exp-a-kd-20260519-1670-1.md) | Partition 256 threads into 32 groups of 8 threads each (group_size=128) to compu | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1687-1](../sources/experiences/exp-a-kd-20260519-1687-1.md) | Eliminate the compute_expert_offsets and compute_arg_sorts kernel launches entir | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1697-1](../sources/experiences/exp-a-kd-20260519-1697-1.md) | Replace scalar float loads with 4-wide vec4_t reinterpretation loads to process  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1698-1](../sources/experiences/exp-a-kd-20260519-1698-1.md) | Replace scalar float loads with 4-wide vec4_t struct loads via reinterpret_cast, | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1711-1](../sources/experiences/exp-a-kd-20260519-1711-1.md) | Parameterize warpReduceSum with a numLanes template to reduce shuffle rounds to  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1712-1](../sources/experiences/exp-a-kd-20260519-1712-1.md) | Parameterize warpReduceSum with a compile-time numLanes template to perform only | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1713-1](../sources/experiences/exp-a-kd-20260519-1713-1.md) | Template-parameterize warpReduceSum with a compile-time numLanes count and compu | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1714-1](../sources/experiences/exp-a-kd-20260519-1714-1.md) | Parameterize warpReduceSum with a compile-time numLanes template argument so the | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1715-1](../sources/experiences/exp-a-kd-20260519-1715-1.md) | Parameterize warpReduceSum with a numLanes template to perform only the minimum  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1716-1](../sources/experiences/exp-a-kd-20260519-1716-1.md) | Parameterize blockReduceSum with a compile-time maxBlockSize template and use if | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1717-1](../sources/experiences/exp-a-kd-20260519-1717-1.md) | Add compile-time maxBlockSize template parameter to blockReduceSum and numLanes  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1733-1](../sources/experiences/exp-a-kd-20260519-1733-1.md) | Replace modulo-2 double-buffered peer_counter[2] arrays and multi-thread read-mo | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1734-1](../sources/experiences/exp-a-kd-20260519-1734-1.md) | Replace per-thread read-modify-write with a centralized _flag[blockIdx.x] read b | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1735-1](../sources/experiences/exp-a-kd-20260519-1735-1.md) | Split the unified barrier into barrier_at_start_sim and barrier_at_end_sim with  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1736-1](../sources/experiences/exp-a-kd-20260519-1736-1.md) | Refactor into separate barrier_at_start_sim and barrier_at_end_sim functions wit | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1800-1](../sources/experiences/exp-a-kd-20260519-1800-1.md) | Replace the hardcoded += with a function pointer dispatch pattern: val = fn(val, | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1801-1](../sources/experiences/exp-a-kd-20260519-1801-1.md) | Consolidate duplicate warp reduction templates into a single warpReduce that acc | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1802-1](../sources/experiences/exp-a-kd-20260519-1802-1.md) | Generalize the warp reduction by replacing the hardcoded += operator with a func | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1803-1](../sources/experiences/exp-a-kd-20260519-1803-1.md) | Generalize the reduction primitive by accepting a ReduceFnType<T> function point | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1804-1](../sources/experiences/exp-a-kd-20260519-1804-1.md) | Generalize the reduction template by parameterizing the reduction operator via a | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1817-1](../sources/experiences/exp-a-kd-20260519-1817-1.md) | Use PTX cp.async.cg.shared.global instructions with a 4-stage pipeline and cp_as | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1823-1](../sources/experiences/exp-a-kd-20260519-1823-1.md) | Replace __reduce_add_sync with a manual cascaded __shfl_down_sync reduction usin | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1832-1](../sources/experiences/exp-a-kd-20260519-1832-1.md) | Replace inline PTX asm shfl with the compiler-visible __shfl_down_sync() intrins | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2307-1](../sources/experiences/exp-a-kd-20260519-2307-1.md) | Replace direct std::numeric_limits<int8_t>::max() with a centralized quant_type_ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2308-1](../sources/experiences/exp-a-kd-20260519-2308-1.md) | Replace the runtime kernel parameter with a type-specialized trait struct (min_s | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2309-1](../sources/experiences/exp-a-kd-20260519-2309-1.md) | Remove the runtime min_scaling_factor parameter and replace it with a type-speci | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2321-1](../sources/experiences/exp-a-kd-20260519-2321-1.md) | Attempted mask-based filtering by adding a null-pointer check and global-memory  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2322-1](../sources/experiences/exp-a-kd-20260519-2322-1.md) | Adding a conditional mask parameter (token_mask) with a runtime null-pointer ter | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2332-1](../sources/experiences/exp-a-kd-20260519-2332-1.md) | Insert __threadfence_block() before every __syncthreads() call — both after the  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2333-1](../sources/experiences/exp-a-kd-20260519-2333-1.md) | Remap output addressing to coalesced layout: g_mindx = m*4 + (tid%64) groups 4 a | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2362-1](../sources/experiences/exp-a-kd-20260519-2362-1.md) | Eliminate the transpose kernel entirely by computing the sum reduction directly  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2363-1](../sources/experiences/exp-a-kd-20260519-2363-1.md) | Clamp kOffcp to K - A_CHUNK using min__(K - A_CHUNK_VAL, k_str + kOff), so out-o | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2364-1](../sources/experiences/exp-a-kd-20260519-2364-1.md) | Add a min__ clamping guard so kOffcp = min__(K - A_CHUNK_VAL, k_str + kOff) ensu | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2373-1](../sources/experiences/exp-a-kd-20260519-2373-1.md) | Replace the branch with a predicated PTX ld.global.cg.v4.u32 inline-asm load (ld | analysis | sm100 | cuda-cpp |
| [exp-a-kd-20260519-2374-1](../sources/experiences/exp-a-kd-20260519-2374-1.md) | Replace the divergent branch with a single predicated PTX inline asm load (ld.gl | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2379-1](../sources/experiences/exp-a-kd-20260519-2379-1.md) | Replace per-thread global memory rows with warp-grouped atomicAdd into a compact | analysis | sm90 | cuda-cpp |
| [exp-i-kd-20260518-0045](../sources/experiences/exp-i-kd-20260518-0045.md) | Implement kernel following the CUTLASS_kernel_template interface pattern with co | implementation | sm90 | cuda-cpp |
| [exp-i-kd-20260518-0050](../sources/experiences/exp-i-kd-20260518-0050.md) | Implement kernel following the CUTLASS_kernel_template interface pattern with co | implementation | sm90 | cuda-cpp |
| [exp-i-kd-20260518-0067](../sources/experiences/exp-i-kd-20260518-0067.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2451-1](../sources/experiences/exp-i-kd-20260519-2451-1.md) | Delegate all reduction logic to CUTLASS's ReduceSplitK functor pattern: declare  | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260518-0005](../sources/experiences/exp-o-kd-20260518-0005.md) | asymmetric_qk | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0006](../sources/experiences/exp-o-kd-20260518-0006.md) | small_q_large_cache | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0009](../sources/experiences/exp-o-kd-20260518-0009.md) | short_seq | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0010](../sources/experiences/exp-o-kd-20260518-0010.md) | double_reduction | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0017](../sources/experiences/exp-o-kd-20260518-0017.md) | float_source_elimination | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260518-0021](../sources/experiences/exp-o-kd-20260518-0021.md) | frag2_fpp1 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0024](../sources/experiences/exp-o-kd-20260518-0024.md) | sync_per_iter | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0027](../sources/experiences/exp-o-kd-20260518-0027.md) | bit_not_128 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0029](../sources/experiences/exp-o-kd-20260518-0029.md) | beta0_skip_src_float | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0031](../sources/experiences/exp-o-kd-20260518-0031.md) | land_N32 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0037](../sources/experiences/exp-o-kd-20260518-0037.md) | float_1x224x224_3to4 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0044](../sources/experiences/exp-o-kd-20260518-0044.md) | large_8warp | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0048](../sources/experiences/exp-o-kd-20260518-0048.md) | medium_head_k128 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0054](../sources/experiences/exp-o-kd-20260518-0054.md) | constructor_loop | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0056](../sources/experiences/exp-o-kd-20260518-0056.md) | gelu_double | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0057](../sources/experiences/exp-o-kd-20260518-0057.md) | gelu_float | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0064](../sources/experiences/exp-o-kd-20260518-0064.md) | multiocc_large | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0067](../sources/experiences/exp-o-kd-20260518-0067.md) | float_reduce_1M | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0069](../sources/experiences/exp-o-kd-20260518-0069.md) | warp_idx_compute | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0070](../sources/experiences/exp-o-kd-20260518-0070.md) | warp_idx_shfl | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0071](../sources/experiences/exp-o-kd-20260518-0071.md) | warp_idx_basic | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0074](../sources/experiences/exp-o-kd-20260518-0074.md) | divergent_warp_path | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0080](../sources/experiences/exp-o-kd-20260518-0080.md) | long_keys_low_parallelism | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0086](../sources/experiences/exp-o-kd-20260518-0086.md) | fused_row_reduction | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0087](../sources/experiences/exp-o-kd-20260518-0087.md) | aligned_float4 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0093](../sources/experiences/exp-o-kd-20260518-0093.md) | f32_small | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0101](../sources/experiences/exp-o-kd-20260518-0101.md) | d64_s512 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0110](../sources/experiences/exp-o-kd-20260518-0110.md) | f32_large | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0113](../sources/experiences/exp-o-kd-20260518-0113.md) | f16x2_large | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0114](../sources/experiences/exp-o-kd-20260518-0114.md) | hgemm_tn_4096 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0121](../sources/experiences/exp-o-kd-20260518-0121.md) | M4096_K512 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0122](../sources/experiences/exp-o-kd-20260518-0122.md) | M4096_K1024 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0125](../sources/experiences/exp-o-kd-20260518-0125.md) | f32_K256 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0126](../sources/experiences/exp-o-kd-20260518-0126.md) | f16_K256 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0127](../sources/experiences/exp-o-kd-20260518-0127.md) | seq4096_hid1024 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0130](../sources/experiences/exp-o-kd-20260518-0130.md) | seq8192_hid512 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0140](../sources/experiences/exp-o-kd-20260518-0140.md) | sgemm_8x4_loop_m1024 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0153](../sources/experiences/exp-o-kd-20260518-0153.md) | f32_16M | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0180](../sources/experiences/exp-o-kd-20260518-0180.md) | float_k8 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0186](../sources/experiences/exp-o-kd-20260518-0186.md) | small_batch_4 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0190](../sources/experiences/exp-o-kd-20260518-0190.md) | float_sub_warp_8 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0206](../sources/experiences/exp-o-kd-20260518-0206.md) | vec_copy_vpt16 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0216](../sources/experiences/exp-o-kd-20260518-0216.md) | many_short_runs | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0218](../sources/experiences/exp-o-kd-20260518-0218.md) | int8_group128 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0223](../sources/experiences/exp-o-kd-20260518-0223.md) | rmsnorm_warp_256 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0226](../sources/experiences/exp-o-kd-20260518-0226.md) | reduce_8ranks_fp16 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0230](../sources/experiences/exp-o-kd-20260518-0230.md) | fp16_128_1000tok | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0231](../sources/experiences/exp-o-kd-20260518-0231.md) | fp16_256_1000tok | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0242](../sources/experiences/exp-o-kd-20260518-0242.md) | large_1024rows_topk6 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0250](../sources/experiences/exp-o-kd-20260518-0250.md) | fusion_medium_batch | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0259](../sources/experiences/exp-o-kd-20260518-0259.md) | float_gs128_ng2048 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0261](../sources/experiences/exp-o-kd-20260518-0261.md) | half_1m | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0262](../sources/experiences/exp-o-kd-20260518-0262.md) | half_64k | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0284](../sources/experiences/exp-o-kd-20260518-0284.md) | small_batch_256_8exp | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0292](../sources/experiences/exp-o-kd-20260518-0292.md) | fp32_256ep8grp | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0299](../sources/experiences/exp-o-kd-20260518-0299.md) | softmax_exp16 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0300](../sources/experiences/exp-o-kd-20260518-0300.md) | vecload_exp16 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0305](../sources/experiences/exp-o-kd-20260518-0305.md) | bs256_draft16 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0316](../sources/experiences/exp-o-kd-20260518-0316.md) | rms_norm_float32_h512 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0327](../sources/experiences/exp-o-kd-20260518-0327.md) | float_4layer_8pairs | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0329](../sources/experiences/exp-o-kd-20260518-0329.md) | small_m_16 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0331](../sources/experiences/exp-o-kd-20260518-0331.md) | fp8_quant_32k | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0342](../sources/experiences/exp-o-kd-20260518-0342.md) | occupancy_limited | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0343](../sources/experiences/exp-o-kd-20260518-0343.md) | small_m | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0347](../sources/experiences/exp-o-kd-20260518-0347.md) | fp16_aligned_8192 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0354](../sources/experiences/exp-o-kd-20260518-0354.md) | grouped_2048_64x64 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0362](../sources/experiences/exp-o-kd-20260518-0362.md) | e8m0_4k | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0369](../sources/experiences/exp-o-kd-20260518-0369.md) | large_data_unlimited | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0374](../sources/experiences/exp-o-kd-20260518-0374.md) | half_reduce_direct | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0417](../sources/experiences/exp-o-kd-20260518-0417.md) | small_m_m2_n1024_k1536 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0420](../sources/experiences/exp-o-kd-20260518-0420.md) | medium_m_m32_n3072_k1024 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0428](../sources/experiences/exp-o-kd-20260518-0428.md) | small_8epg_bs4 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0461](../sources/experiences/exp-o-kd-20260518-0461.md) | small_m_16 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0465](../sources/experiences/exp-o-kd-20260518-0465.md) | bf16_576_16ktokens_batchsplit | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0466](../sources/experiences/exp-o-kd-20260518-0466.md) | bf16_576_4ktokens_batchsplit | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0490](../sources/experiences/exp-o-kd-20260518-0490.md) | tokens_8 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0536](../sources/experiences/exp-o-kd-20260518-0536.md) | moe_8ep_64tk | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0544](../sources/experiences/exp-o-kd-20260518-0544.md) | fp16_hidden4096_tokens512 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0545](../sources/experiences/exp-o-kd-20260518-0545.md) | fp16_hidden4096_tokens64 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0546](../sources/experiences/exp-o-kd-20260518-0546.md) | single_warp_16 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0548](../sources/experiences/exp-o-kd-20260518-0548.md) | float_to_int8_aligned | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0551](../sources/experiences/exp-o-kd-20260518-0551.md) | barrier_sync_2gpu | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0556](../sources/experiences/exp-o-kd-20260518-0556.md) | mq_block16_vs_block32_medium | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0557](../sources/experiences/exp-o-kd-20260518-0557.md) | mq_block16_vs_block32_long | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0559](../sources/experiences/exp-o-kd-20260518-0559.md) | varlen_chunk | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0565](../sources/experiences/exp-o-kd-20260518-0565.md) | experts_64 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0584](../sources/experiences/exp-o-kd-20260518-0584.md) | smem_small_batch | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0589](../sources/experiences/exp-o-kd-20260518-0589.md) | half_large_M | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0604](../sources/experiences/exp-o-kd-20260518-0604.md) | sync_barrier | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0610](../sources/experiences/exp-o-kd-20260518-0610.md) | eq256_bf16 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0615](../sources/experiences/exp-o-kd-20260518-0615.md) | half_d4096 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0627](../sources/experiences/exp-o-kd-20260518-0627.md) | Ode would still allocate shared memory (sLseScale[kMaxSplits]) and construct glo | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0630](../sources/experiences/exp-o-kd-20260518-0630.md) | S significant, as each barrier forces all threads in the block to wait even when | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0632](../sources/experiences/exp-o-kd-20260518-0632.md) | Teration. This wasted memory bandwidth on unnecessary source loads and forced th | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0640](../sources/experiences/exp-o-kd-20260518-0640.md) | Sting computation in the constructor hot path. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0642](../sources/experiences/exp-o-kd-20260518-0642.md) | Ent overhead in a hot path. | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260518-0643](../sources/experiences/exp-o-kd-20260518-0643.md) | Access width should be kCount = 128/32 = 4. The mismatch meant the epilogue trie | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0647](../sources/experiences/exp-o-kd-20260518-0647.md) | Lect, and the result merge. This multi-instruction sequence is slower than neces | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0649](../sources/experiences/exp-o-kd-20260518-0649.md) | Ice a thread belongs to, and all threads in the same warp naturally compute the  | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260518-0652](../sources/experiences/exp-o-kd-20260518-0652.md) | _shfl_sync. Since every thread in a warp computes the same warp_idx (threadIdx.x | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260518-0656](../sources/experiences/exp-o-kd-20260518-0656.md) | The optimization from over-splitting tiny problems or exploding workspace traffi | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260518-0660](../sources/experiences/exp-o-kd-20260518-0660.md) | `tmp_sum_i` and then loading that tensor back in the second kernel. That made a  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0663](../sources/experiences/exp-o-kd-20260518-0663.md) | Fill the memory bus width, wasting bandwidth. The total thread count equals N, w | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0664](../sources/experiences/exp-o-kd-20260518-0664.md) | Nsactions into a single 128-bit wide transaction, depending on optimization leve | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0665](../sources/experiences/exp-o-kd-20260518-0665.md) | These 8 narrow 2-byte memory operations into efficient 128-bit wide transactions | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0669](../sources/experiences/exp-o-kd-20260518-0669.md) | Sced memory transactions are required, under-utilizing the GPU's 128-byte memory | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0670](../sources/experiences/exp-o-kd-20260518-0670.md) | Leading to poor bandwidth utilization since each 32-bit segment in a coalesced t | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0671](../sources/experiences/exp-o-kd-20260518-0671.md) | S only 2 bytes, individual accesses cannot efficiently fill the memory bus width | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0672](../sources/experiences/exp-o-kd-20260518-0672.md) | Nt scheduling overhead and limited instruction-level parallelism within each thr | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0673](../sources/experiences/exp-o-kd-20260518-0673.md) | =2 and BN=128, the padding costs 128*(16+8)*2 = 6144 bytes vs 128*16*2 = 4096 by | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0674](../sources/experiences/exp-o-kd-20260518-0674.md) | Y and the half2 SIMD instruction capability. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0678](../sources/experiences/exp-o-kd-20260518-0678.md) | Overhead per element processed. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0679](../sources/experiences/exp-o-kd-20260518-0679.md) | 0 reads x[0], thread 1 reads x[2*N], thread 2 reads x[4*N]), producing a non-coa | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0688](../sources/experiences/exp-o-kd-20260518-0688.md) | Ress. This is called per-iteration inside the main k-loop, incurring repeated cv | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0689](../sources/experiences/exp-o-kd-20260518-0689.md) | E memory bandwidth and increasing loop trip count by 4x compared to vectorized a | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0701](../sources/experiences/exp-o-kd-20260518-0701.md) | Consuming instruction slots and increasing latency without contributing to the r | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0704](../sources/experiences/exp-o-kd-20260518-0704.md) | Cles exchanging values with inactive or irrelevant lanes. The hardcoded mask=16  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0719](../sources/experiences/exp-o-kd-20260518-0719.md) | Ents at capture time, making the pointers stale if buffer assignments change acr | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0720](../sources/experiences/exp-o-kd-20260518-0720.md) | Without clobbering the shared buffer. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0727](../sources/experiences/exp-o-kd-20260518-0727.md) | Pattern also increases pressure on the memory subsystem as adjacent lanes access | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0728](../sources/experiences/exp-o-kd-20260518-0728.md) | Total work across all groups while others remain underutilized, increasing tail  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0739](../sources/experiences/exp-o-kd-20260518-0739.md) | all_layer_4l | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0748](../sources/experiences/exp-o-kd-20260518-0748.md) | MAX_VPT=32) mismatched the actual data footprint (VPT could be smaller). The sca | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0752](../sources/experiences/exp-o-kd-20260518-0752.md) | Array of the vec_n_t pack, NVCC may scalarize the global load into multiple narr | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0763](../sources/experiences/exp-o-kd-20260518-0763.md) | IZE separate scalar compute operations per vector chunk. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0767](../sources/experiences/exp-o-kd-20260518-0767.md) | Nts were unused, wasting shared memory bandwidth and filling 2 unused A-fragment | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0777](../sources/experiences/exp-o-kd-20260518-0777.md) | Alues, a small YTILE creates excessive wavefronts with poor per-wavefront effici | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0791](../sources/experiences/exp-o-kd-20260518-0791.md) | E beyond the allocated shared memory region. The expert accumulation and expert_ | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0792](../sources/experiences/exp-o-kd-20260518-0792.md) | E token had any prefix KV context. For tokens without prefix context (e.g., deco | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0799](../sources/experiences/exp-o-kd-20260518-0799.md) | Concurrent block occupancy and reducing the scheduler's ability to hide global m | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0808](../sources/experiences/exp-o-kd-20260518-0808.md) | 4-thread CTA with only 576 scalar elements per entry left most threads idle (576 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0810](../sources/experiences/exp-o-kd-20260518-0810.md) | For extremely long sequences with hundreds of blocks, this caused many redundant | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0820](../sources/experiences/exp-o-kd-20260518-0820.md) | Kens_kernel launched afterward), this initialization was purely a write-only pre | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0823](../sources/experiences/exp-o-kd-20260518-0823.md) | Ng both halves of each head dimension separately rather than computing the rotat | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0841](../sources/experiences/exp-o-kd-20260518-0841.md) | L performed a full warp reduction plus shared-memory write/read/sync, which is w | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0843](../sources/experiences/exp-o-kd-20260518-0843.md) | And (3) the two phases share the same peer_counter array, requiring the alternat | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0849](../sources/experiences/exp-o-kd-20260518-0849.md) | The optimization removes shared memory allocation from the expand kernel launch  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0860](../sources/experiences/exp-o-kd-20260518-0860.md) | The optimization is most effective at smaller token counts where the kernel has  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0865](../sources/experiences/exp-o-kd-20260518-0865.md) | T zeros into the accumulator on the first K-iteration. This doubled the instruct | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0870](../sources/experiences/exp-o-kd-20260518-0870.md) | Across ty warps, and staged load/compute/release cycles. For the equal-dimension | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0215-1](../sources/experiences/exp-o-kd-20260519-0215-1.md) | Guard the separate reduction kernel launch with !is_fused_reduction so it only r | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0240-1](../sources/experiences/exp-o-kd-20260519-0240-1.md) | Reinterpret the packed storage as raw bytes and scan only ceil(N/8)=16 bytes, ch | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0241-1](../sources/experiences/exp-o-kd-20260519-0241-1.md) | Replace 32 per-element bit extractions with 4 byte-level reads: iterate over the | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0242-1](../sources/experiences/exp-o-kd-20260519-0242-1.md) | Replace 128 per-element bit extractions with 16 direct byte-level reads via rein | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0243-1](../sources/experiences/exp-o-kd-20260519-0243-1.md) | Replace per-element bit extraction loop (32 iterations) with direct byte-level s | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0255-1](../sources/experiences/exp-o-kd-20260519-0255-1.md) | Allocate per-warp disjoint slots in addition_storage[kQueriesPerBlock * kNumWarp | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0278-1](../sources/experiences/exp-o-kd-20260519-0278-1.md) | Swap grid dimensions from <<<M, N>>> to <<<N, M>>> and reverse the indexing form | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0279-1](../sources/experiences/exp-o-kd-20260519-0279-1.md) | Swap grid/block dimensions to <<<N=1024 blocks, M=64 threads>>> and remap array  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0282-1](../sources/experiences/exp-o-kd-20260519-0282-1.md) | Resize kCount from 8 to 4 (128 bits / sizeof(float)) to match the workspace elem | optimization | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260519-0291-1](../sources/experiences/exp-o-kd-20260519-0291-1.md) | Replace the multi-instruction isnan+branch sequence with PTX inline asm max.NaN. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0292-1](../sources/experiences/exp-o-kd-20260519-0292-1.md) | On SM80+ (Ampere and later), use PTX inline asm max.NaN.f32 which maps to a sing | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0338-1](../sources/experiences/exp-o-kd-20260519-0338-1.md) | Split the input range into 64 contiguous chunks, launch one block per chunk so e | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0340-1](../sources/experiences/exp-o-kd-20260519-0340-1.md) | Reduce kBlockSizeI from 128 to 64 so kThreads drops from 256 (8 warps) to 128 (4 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0347-1](../sources/experiences/exp-o-kd-20260519-0347-1.md) | Fuse the reduction and consumer into a single kernel so the shared-memory reduct | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0348-1](../sources/experiences/exp-o-kd-20260519-0348-1.md) | Cast the row-aligned float pointers to float4 and iterate over kCols/4 elements, | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0624-1](../sources/experiences/exp-o-kd-20260519-0624-1.md) | Replace the entire shared-memory butterfly reduction with a parameterized reduce | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0625-1](../sources/experiences/exp-o-kd-20260519-0625-1.md) | Replace the shared-memory butterfly reduction with a parameterized reduce_sum<kN | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0626-1](../sources/experiences/exp-o-kd-20260519-0626-1.md) | Add a compile-time kNumThreads template parameter (default 32) that controls the | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0632-1](../sources/experiences/exp-o-kd-20260519-0632-1.md) | Replace serial global-memory scan with cooperative shared-memory load (moe_block | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0637-1](../sources/experiences/exp-o-kd-20260519-0637-1.md) | Replace __shfl_down_sync with __shfl_xor_sync parameterized by a kNumThreads tem | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0638-1](../sources/experiences/exp-o-kd-20260519-0638-1.md) | Add a kNumThreads template parameter (defaulting to kWarpThreads=32 for backward | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0655-1](../sources/experiences/exp-o-kd-20260519-0655-1.md) | Fuse all three operations into a single kernel where each thread accumulates fac | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0656-1](../sources/experiences/exp-o-kd-20260519-0656-1.md) | Fuse the three-kernel gather-scale-reduce pipeline into a single kernel where ea | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0657-1](../sources/experiences/exp-o-kd-20260519-0657-1.md) | Fuse all three operations into a single kernel that reads input directly via the | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0665-1](../sources/experiences/exp-o-kd-20260519-0665-1.md) | Add a greedy shortcut clause (target_prob_single >= threshold_single with thresh | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0688-1](../sources/experiences/exp-o-kd-20260519-0688-1.md) | Move peer buffer pointers into a separate GPU-resident RankData struct accessed  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0689-1](../sources/experiences/exp-o-kd-20260519-0689-1.md) | Merge the host-side cudaMemcpyAsync into the reduce kernel via a compile-time CO | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0690-1](../sources/experiences/exp-o-kd-20260519-0690-1.md) | Introduce a RankData struct that bundles the MAX_RANKS_PER_NODE pointer array in | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0697-1](../sources/experiences/exp-o-kd-20260519-0697-1.md) | Pre-allocate d_tokens_cnts and d_cumsum once before the benchmark loop and reuse | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0701-1](../sources/experiences/exp-o-kd-20260519-0701-1.md) | Replace global-memory atomicAdd + __syncthreads + global read with CUB BlockRedu | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0702-1](../sources/experiences/exp-o-kd-20260519-0702-1.md) | Replace atomicAdd-based global reduction with CUB BlockReduce cooperative reduct | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0705-1](../sources/experiences/exp-o-kd-20260519-0705-1.md) | When the topk_ids pointer is 16-byte aligned, use int4 vector loads (128-bit) to | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0706-1](../sources/experiences/exp-o-kd-20260519-0706-1.md) | Replace atomicAdd + __syncthreads + global read with CUB BlockReduce, which coop | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0731-1](../sources/experiences/exp-o-kd-20260519-0731-1.md) | Replace the serial O(N) cumsum loop with a parallel Blelloch (work-efficient) pr | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0731-2](../sources/experiences/exp-o-kd-20260519-0731-2.md) | Replace the two-level warp-based indexing with direct shared_counts[expert_id] a | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0731-3](../sources/experiences/exp-o-kd-20260519-0731-3.md) | Replace the per-expert sequential fill with cooperative binary search: all 1024  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0739-1](../sources/experiences/exp-o-kd-20260519-0739-1.md) | Replace scalar per-element loads with __align__(16) array_t<half,8> packed struc | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0740-1](../sources/experiences/exp-o-kd-20260519-0740-1.md) | Replace scalar half loads with aligned 128-bit packed loads (8 half values per t | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0745-1](../sources/experiences/exp-o-kd-20260519-0745-1.md) | Replace scalar iteration with vectorized access using flashinfer::vec_t<>::cast_ | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0745-2](../sources/experiences/exp-o-kd-20260519-0745-2.md) | Replace bf16 accumulation (__hadd/__hmul) with float32 accumulation using native | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0746-1](../sources/experiences/exp-o-kd-20260519-0746-1.md) | Replace scalar per-thread loads/stores with flashinfer::vec_t vectorized 128-bit | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0758-1](../sources/experiences/exp-o-kd-20260519-0758-1.md) | Replace scalar bfloat16 loads with 128-bit vectorized loads via uint4 reinterpre | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0759-1](../sources/experiences/exp-o-kd-20260519-0759-1.md) | Replace scalar loads with 128-bit vectorized loads via uint4 reinterpret_cast, f | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0774-1](../sources/experiences/exp-o-kd-20260519-0774-1.md) | Replace contiguous-block iteration (threadIdx.x * tokens_per_thread start with s | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1090-1](../sources/experiences/exp-o-kd-20260519-1090-1.md) | Replace scalar 16-bit bf16 loads/stores with 128-bit uint4 vectorized accesses v | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1091-1](../sources/experiences/exp-o-kd-20260519-1091-1.md) | Vectorize the inner loop to process 16 consecutive BFloat16 elements per iterati | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1098-1](../sources/experiences/exp-o-kd-20260519-1098-1.md) | Replace scalar half load+convert with half2 vectorized loads via reinterpret_cas | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1099-1](../sources/experiences/exp-o-kd-20260519-1099-1.md) | Vectorize the element-wise loop with vec_size=8 using half2 loads via reinterpre | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1875-1](../sources/experiences/exp-o-kd-20260519-1875-1.md) | Replace __shfl_down_sync + separate __shfl_sync broadcast (6 ops) with __shfl_xo | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1885-1](../sources/experiences/exp-o-kd-20260519-1885-1.md) | Convert n_group from a runtime parameter to a compile-time template parameter NG | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1895-1](../sources/experiences/exp-o-kd-20260519-1895-1.md) | Compute the max-abs scale on the CPU where the input data already resides in hos | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1906-1](../sources/experiences/exp-o-kd-20260519-1906-1.md) | Pre-compute sh_ids[i] / top_k once into a second shared-memory array (sh_precomp | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1911-1](../sources/experiences/exp-o-kd-20260519-1911-1.md) | Overlap the Phase 1 load buffer (sh_b) and Phase 2 reduction buffer (sh_red) at  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1921-1](../sources/experiences/exp-o-kd-20260519-1921-1.md) | Split the monolithic single-block kernel into two kernels: a lightweight align/c | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1934-1](../sources/experiences/exp-o-kd-20260519-1934-1.md) | Adaptive heuristic selects YTILE=1 and UNRL=4 for sYT=1 workloads: YTILE=1 elimi | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1951-1](../sources/experiences/exp-o-kd-20260519-1951-1.md) | Cap the number of launched thread blocks at 36 (BLOCK_LIMIT) via a min clamp aft | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1952-1](../sources/experiences/exp-o-kd-20260519-1952-1.md) | Cap the grid to at most 36 blocks via a BLOCK_LIMIT constant; with 36 blocks × 5 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1955-1](../sources/experiences/exp-o-kd-20260519-1955-1.md) | Use __align__(16) array_t<nv_bfloat16,8> packed type to cast input pointers and  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1955-2](../sources/experiences/exp-o-kd-20260519-1955-2.md) | Upcast each bf16 value to float32 via __bfloat162float in an unrolled loop, accu | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1956-1](../sources/experiences/exp-o-kd-20260519-1956-1.md) | Use packed 128-bit loads via array_t<half,8> to fetch 8 half values per transact | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1978-1](../sources/experiences/exp-o-kd-20260519-1978-1.md) | Reinterpret float pointers as uint4 (128-bit) to load 4 floats per instruction,  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1979-1](../sources/experiences/exp-o-kd-20260519-1979-1.md) | Replace scalar half loads with 128-bit uint4 vectorized loads that fetch 8 half  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2021-1](../sources/experiences/exp-o-kd-20260519-2021-1.md) | Convert TOPK from a runtime parameter to a compile-time template constant, enabl | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2021-2](../sources/experiences/exp-o-kd-20260519-2021-2.md) | Use __ldg(&input[...]) to route each read-only global load through the dedicated | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2022-1](../sources/experiences/exp-o-kd-20260519-2022-1.md) | Convert topk to a compile-time template parameter with #pragma unroll to fully u | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2083-1](../sources/experiences/exp-o-kd-20260519-2083-1.md) | Replace the custom shared-memory sequential halving reduction with cub::BlockRed | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2084-1](../sources/experiences/exp-o-kd-20260519-2084-1.md) | Replace custom shared-memory halving reduction with CUB BlockReduce, passing blo | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2085-1](../sources/experiences/exp-o-kd-20260519-2085-1.md) | Replace the custom blockReduceMax with cub::BlockReduce<float, 1024> which uses  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2114-1](../sources/experiences/exp-o-kd-20260519-2114-1.md) | Offload the sorted_token_ids initialization loop to a second threadblock (blockI | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2131-1](../sources/experiences/exp-o-kd-20260519-2131-1.md) | Replace per-element atomicAdd with register-local accumulation using a thread-pr | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2137-1](../sources/experiences/exp-o-kd-20260519-2137-1.md) | Replace the 262KB global-memory token-counts matrix with warp-partitioned shared | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2138-1](../sources/experiences/exp-o-kd-20260519-2138-1.md) | Replace per-thread 2D matrix counting with warp-partitioned shared_counts[32][8] | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2141-1](../sources/experiences/exp-o-kd-20260519-2141-1.md) | Replace the large 2D per-thread token-count matrix with a warp-partitioned share | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2188-1](../sources/experiences/exp-o-kd-20260519-2188-1.md) | Add a maxBlockSize template parameter to blockReduceSum and use if constexpr to  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2189-1](../sources/experiences/exp-o-kd-20260519-2189-1.md) | Introduce a compile-time maxBlockSize template parameter: when maxBlockSize > WA | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2191-1](../sources/experiences/exp-o-kd-20260519-2191-1.md) | Introduce a MinMax struct carrying both min and max in a single object, accumula | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2195-1](../sources/experiences/exp-o-kd-20260519-2195-1.md) | Replace the multi-thread read-modify-write self_counter with a compact _flag[kMa | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2196-1](../sources/experiences/exp-o-kd-20260519-2196-1.md) | Redesign the Signal struct to separate start/end phases into distinct fields and | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2197-1](../sources/experiences/exp-o-kd-20260519-2197-1.md) | Replace self_counter + peer_counter[2] with three dedicated arrays: start and en | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2270-1](../sources/experiences/exp-o-kd-20260519-2270-1.md) | Insert __threadfence_block() before every __syncthreads() call — both after the  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2288-1](../sources/experiences/exp-o-kd-20260519-2288-1.md) | Clamp kOffcp to min__(K - A_CHUNK_VAL, k_str + kOff) so that OOB threads read th | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2291-1](../sources/experiences/exp-o-kd-20260519-2291-1.md) | Replace per-thread global memory rows with warp-grouped atomicAdd on a tiny exte | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2292-1](../sources/experiences/exp-o-kd-20260519-2292-1.md) | Replace per-thread local counting + manual prefix-sum with warp-partitioned atom | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2295-1](../sources/experiences/exp-o-kd-20260519-2295-1.md) | Replace per-thread counting rows with warp-based atomicAdd on a flat 1D shared_c | optimization | sm90 | cuda-cpp |
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
| [exp-a-kd-20260519-0554-1](../sources/experiences/exp-a-kd-20260519-0554-1.md) | Vectorize memory access using float4 reinterpret_cast to load/store 4 contiguous | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0555-1](../sources/experiences/exp-a-kd-20260519-0555-1.md) | Replace scalar half loads/stores with half2 vectorized 32-bit memory transaction | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0889-1](../sources/experiences/exp-a-kd-20260519-0889-1.md) | Cache each fp32 input element in a per-thread register array (xi_cache[kElemsPer | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0890-1](../sources/experiences/exp-a-kd-20260519-0890-1.md) | Cache each thread's fp32 input elements in a register array xi_cache[16] during  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0891-1](../sources/experiences/exp-a-kd-20260519-0891-1.md) | Replace one-block-per-row launch with occupancy-optimal grid sizing (cudaOccupan | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0892-1](../sources/experiences/exp-a-kd-20260519-0892-1.md) | Replace one-block-per-row launch with occupancy-based grid sizing (cudaOccupancy | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0901-1](../sources/experiences/exp-a-kd-20260519-0901-1.md) | Replace deferred-write software pipeline with immediate compute-and-store patter | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0902-1](../sources/experiences/exp-a-kd-20260519-0902-1.md) | Remove the deferred-write pattern entirely: eliminate the register array my_out[ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0903-1](../sources/experiences/exp-a-kd-20260519-0903-1.md) | Replace the 2-warp CTA block with a single 32-thread warp, eliminating all share | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0904-1](../sources/experiences/exp-a-kd-20260519-0904-1.md) | Replace the 4-warp CTA block with a single-warp (32-thread) block where each thr | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0905-1](../sources/experiences/exp-a-kd-20260519-0905-1.md) | Replace 8-warp CTA block with a single warp (32 threads) where each thread handl | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0953-1](../sources/experiences/exp-a-kd-20260519-0953-1.md) | Replace device_vec with aligned_vector featuring alignas(sizeof(T)*N) on its sto | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0954-1](../sources/experiences/exp-a-kd-20260519-0954-1.md) | Replace device_vec with aligned_vector using alignas(16) on an aligned_storage<u | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0965-1](../sources/experiences/exp-a-kd-20260519-0965-1.md) | Decompose monolithic function into separate phases: TileMemWarp struct for coope | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0966-1](../sources/experiences/exp-a-kd-20260519-0966-1.md) | Decompose the monolithic function into a TileMemWarp struct for cooperative warp | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0993-1](../sources/experiences/exp-a-kd-20260519-0993-1.md) | Fuse QKNorm and RoPE into a single kernel so that RMSNorm+weight-normalized valu | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1014-1](../sources/experiences/exp-a-kd-20260519-1014-1.md) | Split Q and K normalization into separate CTAs via blockIdx.y (dim3 grid with y= | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1015-1](../sources/experiences/exp-a-kd-20260519-1015-1.md) | Split the fused kernel into separate Q and K CTAs using blockIdx.y dispatch (dim | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1016-1](../sources/experiences/exp-a-kd-20260519-1016-1.md) | Reorganize from warp-level to CTA-level processing: 64 threads (2 warps) each lo | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1017-1](../sources/experiences/exp-a-kd-20260519-1017-1.md) | Restructure from warp-level two-pass to CTA-level single-pass: use 128 threads ( | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1021-1](../sources/experiences/exp-a-kd-20260519-1021-1.md) | Replace runtime cc_major detection and ternary dispatch with a compile-time cons | analysis | sm100 | cuda-cpp |
| [exp-a-kd-20260519-1022-1](../sources/experiences/exp-a-kd-20260519-1022-1.md) | Replace runtime cc_major detection and ternary dispatch with a compile-time cons | analysis | sm100 | cuda-cpp |
| [exp-a-kd-20260519-1023-1](../sources/experiences/exp-a-kd-20260519-1023-1.md) | Replace per-iteration runtime cudaGetDeviceProperties lookup with a compile-time | analysis | sm100 | cuda-cpp |
| [exp-a-kd-20260519-1024-1](../sources/experiences/exp-a-kd-20260519-1024-1.md) | Replace runtime cudaGetDeviceProperties() lookup with a compile-time constexpr i | analysis | sm100 | cuda-cpp |
| [exp-a-kd-20260519-1130-1](../sources/experiences/exp-a-kd-20260519-1130-1.md) | Replace serial block reduction with a two-phase warp-shuffle blockReduceSum: eac | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1131-1](../sources/experiences/exp-a-kd-20260519-1131-1.md) | Replace the serial single-thread reduction with a two-phase warp-shuffle block r | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1213-1](../sources/experiences/exp-a-kd-20260519-1213-1.md) | Replace scalar strided loads with vectorize_read_with_alignment<8> which casts t | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1214-1](../sources/experiences/exp-a-kd-20260519-1214-1.md) | Replace the scalar strided loop with vectorize_read_with_alignment<8> that issue | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1215-1](../sources/experiences/exp-a-kd-20260519-1215-1.md) | Replace the scalar strided loop with vectorize_read_with_alignment<8> which issu | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1216-1](../sources/experiences/exp-a-kd-20260519-1216-1.md) | Replace the scalar variance accumulation loop with vectorize_read_with_alignment | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1217-1](../sources/experiences/exp-a-kd-20260519-1217-1.md) | Replace scalar variance loop with vectorized reads using vllm's vectorize_read_w | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1218-1](../sources/experiences/exp-a-kd-20260519-1218-1.md) | Replace scalar stride loop with vectorize_read_with_alignment_impl<__half, 8> wh | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1219-1](../sources/experiences/exp-a-kd-20260519-1219-1.md) | Replace scalar __half loads with vectorized HalfVec8 (8×__half = 16 bytes) loads | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1220-1](../sources/experiences/exp-a-kd-20260519-1220-1.md) | Replace scalar loads with an alignment-aware vectorized read utility (vectorize_ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1244-1](../sources/experiences/exp-a-kd-20260519-1244-1.md) | Replace scalar float loads with vec4_t aligned loads (4 floats per struct) to re | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1245-1](../sources/experiences/exp-a-kd-20260519-1245-1.md) | Reinterpret the half input array as vec4_t<half> (8-byte aligned struct of 4 hal | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1246-1](../sources/experiences/exp-a-kd-20260519-1246-1.md) | Adding #pragma unroll 4 to the vectorized reduction loop has no measurable effec | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1247-1](../sources/experiences/exp-a-kd-20260519-1247-1.md) | Add #pragma unroll 4 to the vectorized accumulation loop, but it has no measurab | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1333-1](../sources/experiences/exp-a-kd-20260519-1333-1.md) | Hoist loop-invariant weight loads out of the head loop by preloading q_weight an | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1336-1](../sources/experiences/exp-a-kd-20260519-1336-1.md) | Fuse rms_norm and fp8_quant into a single kernel that computes the normalized va | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1337-1](../sources/experiences/exp-a-kd-20260519-1337-1.md) | Fuse RMSNorm and FP8 quantization into a single kernel that computes the normali | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1338-1](../sources/experiences/exp-a-kd-20260519-1338-1.md) | Reinterpret __half arrays as HalfVec8 (8 elements packed in a 128-bit aligned st | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1339-1](../sources/experiences/exp-a-kd-20260519-1339-1.md) | Reinterpret input/residual/weight arrays as HalfVec8 (128-bit aligned struct of  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1342-1](../sources/experiences/exp-a-kd-20260519-1342-1.md) | Add an int64_t input_stride parameter to the kernel signature and replace all oc | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1343-1](../sources/experiences/exp-a-kd-20260519-1343-1.md) | Add an input_stride parameter to rms_norm_kernel and replace blockIdx.x * hidden | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1344-1](../sources/experiences/exp-a-kd-20260519-1344-1.md) | Add an explicit int64_t input_stride parameter and compute a separate strided_id | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1345-1](../sources/experiences/exp-a-kd-20260519-1345-1.md) | Eliminate the separate contiguous-copy kernel by adding an input_stride paramete | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1346-1](../sources/experiences/exp-a-kd-20260519-1346-1.md) | Introduce a separate input_stride kernel parameter so that input row addressing  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1347-1](../sources/experiences/exp-a-kd-20260519-1347-1.md) | Replace the two-kernel copy+norm pipeline with a single rms_norm_kernel that acc | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1422-1](../sources/experiences/exp-a-kd-20260519-1422-1.md) | Replace scalar element-wise loads/stores with vec_n_t<half,8> 128-bit packed vec | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1423-1](../sources/experiences/exp-a-kd-20260519-1423-1.md) | Replace scalar half loads/stores with vec_n_t<half,8> (128-bit) vectorized acces | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1424-1](../sources/experiences/exp-a-kd-20260519-1424-1.md) | Replace hardcoded VEC_SIZE with a dynamic computation using gcd(max_vector_bytes | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1425-1](../sources/experiences/exp-a-kd-20260519-1425-1.md) | Replace the hardcoded 1024-thread cap with an adaptive 256-thread cap and comput | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1426-1](../sources/experiences/exp-a-kd-20260519-1426-1.md) | Use adaptive max_block_size based on grid size: cap at 256 threads per block whe | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1427-1](../sources/experiences/exp-a-kd-20260519-1427-1.md) | Introduce adaptive max_block_size that reduces to 256 when num_tokens >= 256, al | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1428-1](../sources/experiences/exp-a-kd-20260519-1428-1.md) | Replace scalar half2float loads with explicit vec_n_t<__half, VEC_SIZE> loads vi | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1429-1](../sources/experiences/exp-a-kd-20260519-1429-1.md) | Replace scalar half loads with a vec_n_t<__half, VEC_SIZE> struct loaded via rei | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1430-1](../sources/experiences/exp-a-kd-20260519-1430-1.md) | Promote VEC_SIZE from a hardcoded constexpr inside the kernel body to a template | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1431-1](../sources/experiences/exp-a-kd-20260519-1431-1.md) | Use adaptive block sizing that selects smaller blocks (256 threads) for large ba | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1432-1](../sources/experiences/exp-a-kd-20260519-1432-1.md) | The after code computes an adaptive max_block_size=(num_tokens<256)?1024:256 and | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1501-1](../sources/experiences/exp-a-kd-20260519-1501-1.md) | Replace the custom blockReduceSum with cub::BlockReduce<float, 1024>, which inte | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1502-1](../sources/experiences/exp-a-kd-20260519-1502-1.md) | Replace custom blockReduceSum with cub::BlockReduce<float,1024> passing blockDim | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1503-1](../sources/experiences/exp-a-kd-20260519-1503-1.md) | Replace the runtime-conditional custom blockReduceSum templates with a single cu | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1504-1](../sources/experiences/exp-a-kd-20260519-1504-1.md) | Replace the custom blockReduceSum template and its runtime conditional with a si | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1505-1](../sources/experiences/exp-a-kd-20260519-1505-1.md) | Replace the runtime-conditional blockReduceSum with a single cub::BlockReduce<fl | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1506-1](../sources/experiences/exp-a-kd-20260519-1506-1.md) | Replace the runtime-conditional hand-rolled blockReduceSum with a single cub::Bl | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1600-1](../sources/experiences/exp-a-kd-20260519-1600-1.md) | Add an explicit input_stride kernel parameter and replace all hardcoded hidden_s | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1601-1](../sources/experiences/exp-a-kd-20260519-1601-1.md) | Pass input_stride directly to the RMS norm kernel so each thread computes the co | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1602-1](../sources/experiences/exp-a-kd-20260519-1602-1.md) | Introduce an explicit input_stride parameter and compute a separate input_token_ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1603-1](../sources/experiences/exp-a-kd-20260519-1603-1.md) | Add an explicit input_stride parameter and compute input_token_offset separately | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1665-1](../sources/experiences/exp-a-kd-20260519-1665-1.md) | Extract the quantization loop into a separate norm_and_quant_ptr device helper t | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1668-1](../sources/experiences/exp-a-kd-20260519-1668-1.md) | Replace register-resident scalar scale with per-group scale array indexing via i | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1669-1](../sources/experiences/exp-a-kd-20260519-1669-1.md) | Replace the single scalar scale with a per-group scale array in global memory, c | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1672-1](../sources/experiences/exp-a-kd-20260519-1672-1.md) | Replace the single scalar scale with a groupwise scale lookup that computes a pe | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1673-1](../sources/experiences/exp-a-kd-20260519-1673-1.md) | Replace the single scalar scale with a groupwise scale lookup from a per-group s | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1704-1](../sources/experiences/exp-a-kd-20260519-1704-1.md) | Reinterpret FP16 pointers as _f16Vec<__half,8> (128-bit aligned vector struct) t | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1705-1](../sources/experiences/exp-a-kd-20260519-1705-1.md) | Replace scalar __half loads with 128-bit vectorized _f16Vec<__half,8> loads (8 F | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1706-1](../sources/experiences/exp-a-kd-20260519-1706-1.md) | Introduce a vectorized _f16Vec<__half,8> wrapper providing 128-bit aligned loads | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1707-1](../sources/experiences/exp-a-kd-20260519-1707-1.md) | Use an adaptive block size formula: when num_tokens >= 256, reduce block_size to | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1708-1](../sources/experiences/exp-a-kd-20260519-1708-1.md) | Introduce adaptive block sizing: when num_tokens < 256, keep block_size=1024 for | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1709-1](../sources/experiences/exp-a-kd-20260519-1709-1.md) | Add input and residual in native __half using the hardware __hadd instruction, c | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1710-1](../sources/experiences/exp-a-kd-20260519-1710-1.md) | Eliminate redundant round-trip casts by performing the addition in native scalar | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1852-1](../sources/experiences/exp-a-kd-20260519-1852-1.md) | Fuse residual addition and RMS normalization into a single kernel where the firs | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1853-1](../sources/experiences/exp-a-kd-20260519-1853-1.md) | Fuse residual_add_kernel and rms_norm_kernel into a single fused_add_rms_norm_ke | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2304-1](../sources/experiences/exp-a-kd-20260519-2304-1.md) | Replace the runtime min_scaling_factor kernel parameter with a compile-time cons | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2305-1](../sources/experiences/exp-a-kd-20260519-2305-1.md) | Replace the runtime min_scaling_factor kernel parameter with a compile-time cons | analysis | sm90 | cuda-cpp |
| [exp-o-20260513-100004-rmsnorm-warp-level-reduction](../sources/experiences/exp-o-20260513-100004-rmsnorm-warp-level-reduction.md) | FlashInfer-Bench RMSNorm: warp-level reduction achieves 4.7x-5.4x speedup | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0403-1](../sources/experiences/exp-o-kd-20260519-0403-1.md) | Replace scalar float loads/stores with float4 reinterpret_cast vectorized 128-bi | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0404-1](../sources/experiences/exp-o-kd-20260519-0404-1.md) | Replace scalar half loads/stores with half2 vectorized access via reinterpret_ca | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0405-1](../sources/experiences/exp-o-kd-20260519-0405-1.md) | Vectorize to float4 (128-bit) loads/stores via FLOAT4 reinterpret, processing 4  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0406-1](../sources/experiences/exp-o-kd-20260519-0406-1.md) | Vectorize from scalar half to half2 type: each thread loads two packed halves in | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0681-1](../sources/experiences/exp-o-kd-20260519-0681-1.md) | Cache each fp32 input element in a per-thread register array (xi_cache[kElemsPer | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0682-1](../sources/experiences/exp-o-kd-20260519-0682-1.md) | Cache each fp32-converted input element in a per-thread register array (xi_cache | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0683-1](../sources/experiences/exp-o-kd-20260519-0683-1.md) | Replace one-block-per-row launch with occupancy-aware grid sizing via cudaOccupa | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0684-1](../sources/experiences/exp-o-kd-20260519-0684-1.md) | Replace one-block-per-row launch with occupancy-aware grid sizing and a grid-str | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0694-1](../sources/experiences/exp-o-kd-20260519-0694-1.md) | Replace the multi-warp CTA block with a single-warp (32-thread) block: the sum-o | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0695-1](../sources/experiences/exp-o-kd-20260519-0695-1.md) | Replace the 4-warp CTA kernel (128 threads, shared memory, 2x __syncthreads()) w | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0696-1](../sources/experiences/exp-o-kd-20260519-0696-1.md) | Replace the 8-warp CTA kernel with a single-warp (32 threads) kernel where each  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0750-1](../sources/experiences/exp-o-kd-20260519-0750-1.md) | Fuse the two kernels into one: keep RMSNorm+weight results in the register array | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0751-1](../sources/experiences/exp-o-kd-20260519-0751-1.md) | Fuse QKNorm and RoPE into a single kernel where the RMSNorm+weight normalized va | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0766-1](../sources/experiences/exp-o-kd-20260519-0766-1.md) | Replace warp-level two-pass (32 threads, 16 pairs/thread) with CTA-level single- | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1873-1](../sources/experiences/exp-o-kd-20260519-1873-1.md) | Replace the serial reduction with a two-phase warp-shuffle blockReduceSum: each  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1874-1](../sources/experiences/exp-o-kd-20260519-1874-1.md) | Replace the serial naiveBlockReduceSum with a two-phase warp-shuffle blockReduce | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1915-1](../sources/experiences/exp-o-kd-20260519-1915-1.md) | Replace the scalar strided loop with vectorize_read_with_alignment<8> which cast | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1916-1](../sources/experiences/exp-o-kd-20260519-1916-1.md) | Replace the scalar strided loop with vectorize_read_with_alignment<8> which load | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1917-1](../sources/experiences/exp-o-kd-20260519-1917-1.md) | Replace the scalar strided loop with vectorize_read_with_alignment<8> which perf | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1918-1](../sources/experiences/exp-o-kd-20260519-1918-1.md) | Replace the scalar stride loop with vectorize_read_with_alignment<8> that issues | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1919-1](../sources/experiences/exp-o-kd-20260519-1919-1.md) | Replace the scalar element-by-element load loop with vectorize_read_with_alignme | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1920-1](../sources/experiences/exp-o-kd-20260519-1920-1.md) | Replace the scalar variance loop with vllm::vectorize_read_with_alignment<8>, wh | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1936-1](../sources/experiences/exp-o-kd-20260519-1936-1.md) | Replace scalar per-element loads with vec4_t<half> aligned vector loads (8 bytes | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1937-1](../sources/experiences/exp-o-kd-20260519-1937-1.md) | Replace scalar loads with vec4_t<scalar_t> vectorized loads that reinterpret the | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1992-1](../sources/experiences/exp-o-kd-20260519-1992-1.md) | Fuse rms_norm and fp8_quant into a single kernel (rms_norm_static_fp8_quant_kern | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1993-1](../sources/experiences/exp-o-kd-20260519-1993-1.md) | Fuse RMSNorm and FP8 quantization into a single kernel that computes the normali | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1994-1](../sources/experiences/exp-o-kd-20260519-1994-1.md) | Introduce an alignas(16) HalfVec8 struct packing 8 __half values into a single 1 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1995-1](../sources/experiences/exp-o-kd-20260519-1995-1.md) | Replace scalar __half element processing with a 128-bit aligned HalfVec8 struct  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1997-1](../sources/experiences/exp-o-kd-20260519-1997-1.md) | Add input_stride parameter to rms_norm_kernel so it computes blockIdx.x * input_ | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1998-1](../sources/experiences/exp-o-kd-20260519-1998-1.md) | Add input_stride parameter to the kernel, compute vec_input_stride = input_strid | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1999-1](../sources/experiences/exp-o-kd-20260519-1999-1.md) | Add an explicit int64_t input_stride parameter to the kernel signature and repla | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2000-1](../sources/experiences/exp-o-kd-20260519-2000-1.md) | Introduce vec_input_stride = input_stride / width derived from the element-level | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2001-1](../sources/experiences/exp-o-kd-20260519-2001-1.md) | Pass input_stride as a kernel parameter and read directly from strided memory us | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2002-1](../sources/experiences/exp-o-kd-20260519-2002-1.md) | Introduce an input_stride kernel parameter extracted from input.stride(-2) at th | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2042-1](../sources/experiences/exp-o-kd-20260519-2042-1.md) | Cap block size to 256 threads instead of 1024, allowing 4x more blocks to reside | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2042-2](../sources/experiences/exp-o-kd-20260519-2042-2.md) | Compute VEC_SIZE dynamically using std::gcd(16/sizeof(scalar_t), hidden_size) to | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2043-1](../sources/experiences/exp-o-kd-20260519-2043-1.md) | Use adaptive max_block_size based on batch size: 256 threads per block for large | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2044-1](../sources/experiences/exp-o-kd-20260519-2044-1.md) | Replace hardcoded VEC_SIZE with runtime-calculated vector size using std::gcd(16 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2045-1](../sources/experiences/exp-o-kd-20260519-2045-1.md) | Introduce an adaptive max_block_size — 1024 when num_tokens < 256, else 256 — so | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2046-1](../sources/experiences/exp-o-kd-20260519-2046-1.md) | Adaptively reduce block size to 256 threads when num_tokens >= 256, allowing eac | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2143-1](../sources/experiences/exp-o-kd-20260519-2143-1.md) | Pass input_stride as a kernel parameter and compute input offsets as blockIdx.x  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2144-1](../sources/experiences/exp-o-kd-20260519-2144-1.md) | Add an input_stride parameter to the kernel function and propagate it through al | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2184-1](../sources/experiences/exp-o-kd-20260519-2184-1.md) | Reinterpret scalar __half pointers as aligned _f16Vec<__half,8> structs (128-bit | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2185-1](../sources/experiences/exp-o-kd-20260519-2185-1.md) | Replace scalar __half loads with 128-bit _f16Vec<__half,8> vectorized loads via  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2186-1](../sources/experiences/exp-o-kd-20260519-2186-1.md) | Replace scalar __half loads with 128-bit aligned _f16Vec<__half,8> vectorized st | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2187-1](../sources/experiences/exp-o-kd-20260519-2187-1.md) | Introduce _f16Vec<scalar_t,width> (alignas(16) POD struct) to reinterpret scalar | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2252-1](../sources/experiences/exp-o-kd-20260519-2252-1.md) | Fuse residual addition and RMS normalization into a single kernel where the firs | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2253-1](../sources/experiences/exp-o-kd-20260519-2253-1.md) | Fuse residual addition and RMS normalization into a single fused_add_rms_norm_ke | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2258-1](../sources/experiences/exp-o-kd-20260519-2258-1.md) | Replace the runtime min_scaling_factor kernel parameter with a compile-time cons | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2259-1](../sources/experiences/exp-o-kd-20260519-2259-1.md) | Remove the runtime min_scaling_factor parameter from all kernel and device funct | optimization | sm90 | cuda-cpp |

## rotary-embedding

| ID | Title | Type | Architectures | Languages |
|----|-------|------|--------------|-----------|
| [exp-a-kd-20260518-0328](../sources/experiences/exp-a-kd-20260518-0328.md) | seq4096_hid1024 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0364](../sources/experiences/exp-a-kd-20260518-0364.md) | tokens_512 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0365](../sources/experiences/exp-a-kd-20260518-0365.md) | tokens_2048 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0366](../sources/experiences/exp-a-kd-20260518-0366.md) | tokens_512 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0369](../sources/experiences/exp-a-kd-20260518-0369.md) | tokens_2048 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0422](../sources/experiences/exp-a-kd-20260518-0422.md) | small_batch_4 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0452](../sources/experiences/exp-a-kd-20260518-0452.md) | concat_mla_16384tokens | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0453](../sources/experiences/exp-a-kd-20260518-0453.md) | concat_mla_256tokens | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0454](../sources/experiences/exp-a-kd-20260518-0454.md) | concat_mla_4096tokens | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0532](../sources/experiences/exp-a-kd-20260518-0532.md) | fusion_small_batch | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0534](../sources/experiences/exp-a-kd-20260518-0534.md) | fp16_small_8tok | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0613](../sources/experiences/exp-a-kd-20260518-0613.md) | bf16_hidden_8192 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0792](../sources/experiences/exp-a-kd-20260518-0792.md) | rope_copy_128tokens | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1088](../sources/experiences/exp-a-kd-20260518-1088.md) | multiple_lora_16grp_4tok | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1405](../sources/experiences/exp-a-kd-20260518-1405.md) | padded_fp32_8h_64dim | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0556-1](../sources/experiences/exp-a-kd-20260519-0556-1.md) | Replace two scalar float loads and two scalar stores with a single float4 (128-b | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0557-1](../sources/experiences/exp-a-kd-20260519-0557-1.md) | Replace scalar float2 loads/stores with a single float4 (128-bit) vectorized loa | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0558-1](../sources/experiences/exp-a-kd-20260519-0558-1.md) | Pack the RoPE computation to process four floats per thread using float4 (128-bi | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0559-1](../sources/experiences/exp-a-kd-20260519-0559-1.md) | Replace scalar float loads/stores with float4 (128-bit) vectorized loads/stores  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0560-1](../sources/experiences/exp-a-kd-20260519-0560-1.md) | Remap threads so each block corresponds to one token position (blockIdx.x = toke | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0561-1](../sources/experiences/exp-a-kd-20260519-0561-1.md) | Restructure the thread-to-data mapping so blockIdx.x corresponds to token_pos an | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0562-1](../sources/experiences/exp-a-kd-20260519-0562-1.md) | Remap threads so one block maps to one token position (blockIdx.x = token_pos, t | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0563-1](../sources/experiences/exp-a-kd-20260519-0563-1.md) | Remap threads so each CUDA block processes one token position (blockIdx.x = toke | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0817-1](../sources/experiences/exp-a-kd-20260519-0817-1.md) | Query GPU occupancy at runtime via cudaOccupancyMaxActiveBlocksPerMultiprocessor | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0818-1](../sources/experiences/exp-a-kd-20260519-0818-1.md) | Add #pragma unroll 1 to both head iteration loops to explicitly prevent compiler | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0819-1](../sources/experiences/exp-a-kd-20260519-0819-1.md) | Introduce a head-parallel kernel where each block processes exactly one head (bl | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0819-2](../sources/experiences/exp-a-kd-20260519-0819-2.md) | Query runtime occupancy via cudaOccupancyMaxActiveBlocksPerMultiprocessor and cu | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0820-1](../sources/experiences/exp-a-kd-20260519-0820-1.md) | Add #pragma unroll 1 to both qo_heads and kv_heads iteration loops to explicitly | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0943-1](../sources/experiences/exp-a-kd-20260519-0943-1.md) | Fuse the two kernels into a single fused_rope_kv_kernel that keeps k_out in regi | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0944-1](../sources/experiences/exp-a-kd-20260519-0944-1.md) | Fuse rope_only_kernel and kv_save_kernel into a single fused_rope_kv_kernel that | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0945-1](../sources/experiences/exp-a-kd-20260519-0945-1.md) | Fuse RoPE and KV write-back into a single kernel: after computing post-RoPE K va | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0946-1](../sources/experiences/exp-a-kd-20260519-0946-1.md) | Fuse rope_only_kernel and kv_writeback_kernel into a single fused_rope_kv_kernel | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0992-1](../sources/experiences/exp-a-kd-20260519-0992-1.md) | Fuse QKNorm (RMSNorm+weight) and NeoX RoPE into a single kernel, keeping normali | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1196-1](../sources/experiences/exp-a-kd-20260519-1196-1.md) | Split the fused loop into two independent loops: a query loop over num_heads*emb | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1197-1](../sources/experiences/exp-a-kd-20260519-1197-1.md) | Split the single fused loop into two independent loops: one iterating over num_h | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1198-1](../sources/experiences/exp-a-kd-20260519-1198-1.md) | Split the single combined query+key loop into two independent loops — one iterat | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1229-1](../sources/experiences/exp-a-kd-20260519-1229-1.md) | Replace the divergent scalar bf16 copy with a warp-cooperative int-width vectori | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1332-1](../sources/experiences/exp-a-kd-20260519-1332-1.md) | Use cp.async two-group pipelining: group 0 async loads QKV tiles into shared mem | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1332-2](../sources/experiences/exp-a-kd-20260519-1332-2.md) | Preload weight values into thread-private registers once before the multi-head l | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1334-1](../sources/experiences/exp-a-kd-20260519-1334-1.md) | Consolidate HEADS_PER_WARP=4 heads onto each warp so one warp iterates over 4 he | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1334-2](../sources/experiences/exp-a-kd-20260519-1334-2.md) | Load cos/sin data into per-warp shared memory via cp.async (16-byte cache-global | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1524-1](../sources/experiences/exp-a-kd-20260519-1524-1.md) | Consolidate all 64 tokens into a single batched_rotary_embedding_kernel launch w | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1525-1](../sources/experiences/exp-a-kd-20260519-1525-1.md) | Replace 16 separate small kernel launches with a single batched kernel launch co | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1533-1](../sources/experiences/exp-a-kd-20260519-1533-1.md) | Fuse RoPE computation on k_pe with the paged KV-cache write into a single kernel | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1534-1](../sources/experiences/exp-a-kd-20260519-1534-1.md) | Fuse RoPE computation and KV-cache write into a single kernel (concat_and_cache_ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1561-1](../sources/experiences/exp-a-kd-20260519-1561-1.md) | Convert to in-place operation by removing separate output buffers and reading/wr | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1562-1](../sources/experiences/exp-a-kd-20260519-1562-1.md) | Restructure the loop to iterate over num_heads*embed_dim instead of num_heads*he | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1841-1](../sources/experiences/exp-a-kd-20260519-1841-1.md) | Replace the hardcoded head_size stride with a configurable int64_t head_stride k | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1842-1](../sources/experiences/exp-a-kd-20260519-1842-1.md) | Replace hardcoded head_size stride with a configurable int64_t head_stride param | analysis | sm90 | cuda-cpp |
| [exp-i-kd-20260518-0004](../sources/experiences/exp-i-kd-20260518-0004.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0027](../sources/experiences/exp-i-kd-20260518-0027.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm100 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0030](../sources/experiences/exp-i-kd-20260518-0030.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0046](../sources/experiences/exp-i-kd-20260518-0046.md) | Implement kernel following the CUTLASS_kernel_template interface pattern with co | implementation | sm90 | cuda-cpp |
| [exp-i-kd-20260518-0047](../sources/experiences/exp-i-kd-20260518-0047.md) | Implement kernel following the CUTLASS_kernel_template interface pattern with co | implementation | sm90 | cuda-cpp |
| [exp-i-kd-20260518-0048](../sources/experiences/exp-i-kd-20260518-0048.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0049](../sources/experiences/exp-i-kd-20260518-0049.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0051](../sources/experiences/exp-i-kd-20260518-0051.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0052](../sources/experiences/exp-i-kd-20260518-0052.md) | Implement kernel following the CUTLASS_kernel_template interface pattern with co | implementation | sm90 | cuda-cpp |
| [exp-i-kd-20260518-0060](../sources/experiences/exp-i-kd-20260518-0060.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-o-kd-20260518-0161](../sources/experiences/exp-o-kd-20260518-0161.md) | tokens_512 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0178](../sources/experiences/exp-o-kd-20260518-0178.md) | small_batch_64heads | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0222](../sources/experiences/exp-o-kd-20260518-0222.md) | rmsnorm_warp_128 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0407](../sources/experiences/exp-o-kd-20260518-0407.md) | Vectorize loads/stores with float4 so each thread processes two adjacent RoPE pa | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0415](../sources/experiences/exp-o-kd-20260518-0415.md) | Replace scalar per-element load/store with vectorized float4 packed access via F | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0476](../sources/experiences/exp-o-kd-20260518-0476.md) | multiple_lora_8grp_64tok | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0713](../sources/experiences/exp-o-kd-20260518-0713.md) | Between the alignment and padding operations). For MoE models with frequent expe | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0859](../sources/experiences/exp-o-kd-20260518-0859.md) | Dimension has padding (e.g., [batch, seq, num_heads, head_size + 64]). The kerne | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0407-1](../sources/experiences/exp-o-kd-20260519-0407-1.md) | Pack two adjacent RoPE pairs into a single float4 (128-bit) vector so each threa | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0408-1](../sources/experiences/exp-o-kd-20260519-0408-1.md) | Replace four scalar 32-bit global loads/stores per thread with one float4 (128-b | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0409-1](../sources/experiences/exp-o-kd-20260519-0409-1.md) | Replace scalar float2 loads/stores with float4 vectorized 128-bit transactions,  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0410-1](../sources/experiences/exp-o-kd-20260519-0410-1.md) | Pack two adjacent (x1,x2) pairs into a single float4 vector, loading and storing | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0411-1](../sources/experiences/exp-o-kd-20260519-0411-1.md) | Restructure thread-to-data mapping so each CUDA block handles one token position | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0412-1](../sources/experiences/exp-o-kd-20260519-0412-1.md) | Reorganize the thread-to-data mapping so that blockIdx.x maps to token_pos and t | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0413-1](../sources/experiences/exp-o-kd-20260519-0413-1.md) | Remap threads so each block handles one token position (blockIdx.x = token_pos,  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0414-1](../sources/experiences/exp-o-kd-20260519-0414-1.md) | Restructure the kernel to use one block per token position (blockIdx.x = token_p | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0415-1](../sources/experiences/exp-o-kd-20260519-0415-1.md) | Replace scalar f32 load/store with vectorized float4 packed load/store using the | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0416-1](../sources/experiences/exp-o-kd-20260519-0416-1.md) | Map one CUDA block to one token position (blockIdx.x = token_pos, threadIdx.x =  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0621-1](../sources/experiences/exp-o-kd-20260519-0621-1.md) | Replace the serial head loop with a head-parallel kernel where blockIdx.y select | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0622-1](../sources/experiences/exp-o-kd-20260519-0622-1.md) | Introduce adaptive occupancy-based dispatch: query cudaOccupancyMaxActiveBlocksP | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0723-1](../sources/experiences/exp-o-kd-20260519-0723-1.md) | Fuse rope_only_kernel and kv_save_kernel into a single fused_rope_kv_kernel that | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0724-1](../sources/experiences/exp-o-kd-20260519-0724-1.md) | Fuse rope_only_kernel and kv_save_kernel into a single fused_rope_kv_kernel so t | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0725-1](../sources/experiences/exp-o-kd-20260519-0725-1.md) | Fuse rope_only_kernel and kv_writeback_kernel into a single fused_rope_kv_kernel | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0726-1](../sources/experiences/exp-o-kd-20260519-0726-1.md) | Fuse rope_only_kernel and kv_writeback_kernel into a single fused_rope_kv_kernel | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0727-1](../sources/experiences/exp-o-kd-20260519-0727-1.md) | Fused KV cache write-back into the RoPE kernel by conditionally dispatching to B | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2090-1](../sources/experiences/exp-o-kd-20260519-2090-1.md) | Consolidate 8 per-group kernel launches into a single batched_rotary_embedding_k | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2091-1](../sources/experiences/exp-o-kd-20260519-2091-1.md) | Replace 16 per-group kernel launches (4 blocks each) with a single batched_rotar | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2099-1](../sources/experiences/exp-o-kd-20260519-2099-1.md) | Fuse the RoPE computation on k_pe with the KV-cache write into a single kernel:  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2100-1](../sources/experiences/exp-o-kd-20260519-2100-1.md) | Fuse RoPE computation and KV-cache write into a single kernel: compute RoPE on k | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2122-1](../sources/experiences/exp-o-kd-20260519-2122-1.md) | Restructure the loop to iterate over num_heads*embed_dim instead of num_heads*he | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2123-1](../sources/experiences/exp-o-kd-20260519-2123-1.md) | Restructure the loop to iterate over num_heads*embed_dim (half the count) and ha | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2250-1](../sources/experiences/exp-o-kd-20260519-2250-1.md) | Replace the hardcoded head_size stride parameter with a configurable int64_t hea | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2251-1](../sources/experiences/exp-o-kd-20260519-2251-1.md) | Replace hardcoded head_size stride with a configurable head_stride parameter (in | optimization | sm90 | cuda-cpp |

## sampling

| ID | Title | Type | Architectures | Languages |
|----|-------|------|--------------|-----------|
| [exp-o-kd-20260519-0666-1](../sources/experiences/exp-o-kd-20260519-0666-1.md) | Replace the pure-stochastic acceptance condition with a combined greedy+stochast | optimization | sm90 | cuda-cpp |

## scan

| ID | Title | Type | Architectures | Languages |
|----|-------|------|--------------|-----------|
| [exp-a-kd-20260518-0001](../sources/experiences/exp-a-kd-20260518-0001.md) | SSM multi-row scan shared memory write index fix | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0087](../sources/experiences/exp-a-kd-20260518-0087.md) | lor_N128 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0383](../sources/experiences/exp-a-kd-20260518-0383.md) | prefix_sum_256exp_serial | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0441](../sources/experiences/exp-a-kd-20260518-0441.md) | scan_8experts | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0442](../sources/experiences/exp-a-kd-20260518-0442.md) | scan_64experts | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0462](../sources/experiences/exp-a-kd-20260518-0462.md) | ldca_vectorized_experts | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0472](../sources/experiences/exp-a-kd-20260518-0472.md) | few_long_runs | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0501](../sources/experiences/exp-a-kd-20260518-0501.md) | scan_256ep | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0502](../sources/experiences/exp-a-kd-20260518-0502.md) | scan_64ep | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0539](../sources/experiences/exp-a-kd-20260518-0539.md) | experts_256_bs64 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0540](../sources/experiences/exp-a-kd-20260518-0540.md) | fill_64exp | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0541](../sources/experiences/exp-a-kd-20260518-0541.md) | fill_256exp | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0544](../sources/experiences/exp-a-kd-20260518-0544.md) | scan_8_experts | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0545](../sources/experiences/exp-a-kd-20260518-0545.md) | scan_16_experts | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0549](../sources/experiences/exp-a-kd-20260518-0549.md) | float_medium | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0551](../sources/experiences/exp-a-kd-20260518-0551.md) | topk_zero_offset | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0579](../sources/experiences/exp-a-kd-20260518-0579.md) | medium_4k_tokens | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0619](../sources/experiences/exp-a-kd-20260518-0619.md) | small_batch_128_16exp | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0622](../sources/experiences/exp-a-kd-20260518-0622.md) | small_16exp_512tok | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0623](../sources/experiences/exp-a-kd-20260518-0623.md) | small_64exp_1024tok | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0667](../sources/experiences/exp-a-kd-20260518-0667.md) | scan_multichunk_2rows | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0719](../sources/experiences/exp-a-kd-20260518-0719.md) | align_256ep_64bs | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0720](../sources/experiences/exp-a-kd-20260518-0720.md) | align_64ep_64bs | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0721](../sources/experiences/exp-a-kd-20260518-0721.md) | align_8ep_64bs | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0793](../sources/experiences/exp-a-kd-20260518-0793.md) | ssm_half_d8_s256 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0794](../sources/experiences/exp-a-kd-20260518-0794.md) | ssm_half_d16_s512 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0801](../sources/experiences/exp-a-kd-20260518-0801.md) | tiny_M_512 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0865](../sources/experiences/exp-a-kd-20260518-0865.md) | mindices_align_8ep | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0868](../sources/experiences/exp-a-kd-20260518-0868.md) | expert_offset_seqscan_8ep | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1013](../sources/experiences/exp-a-kd-20260518-1013.md) | shared_both_fit_64ep | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1014](../sources/experiences/exp-a-kd-20260518-1014.md) | i16_only_fits_256ep | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1118](../sources/experiences/exp-a-kd-20260518-1118.md) | small_64epg_bs64_960tok | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1132](../sources/experiences/exp-a-kd-20260518-1132.md) | topk2_epg32 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1161](../sources/experiences/exp-a-kd-20260518-1161.md) | sort_256ep | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1162](../sources/experiences/exp-a-kd-20260518-1162.md) | sort_64ep | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1244](../sources/experiences/exp-a-kd-20260518-1244.md) | seq8k | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1258](../sources/experiences/exp-a-kd-20260518-1258.md) | float_n8_k4 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1259](../sources/experiences/exp-a-kd-20260518-1259.md) | half_n16_k8 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1264](../sources/experiences/exp-a-kd-20260518-1264.md) | decode_4rows | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1288](../sources/experiences/exp-a-kd-20260518-1288.md) | dyn_h4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1448](../sources/experiences/exp-a-kd-20260518-1448.md) | offset_zero | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1449](../sources/experiences/exp-a-kd-20260518-1449.md) | ep64_n1536 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1451](../sources/experiences/exp-a-kd-20260518-1451.md) | ep128_n6144 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1492](../sources/experiences/exp-a-kd-20260518-1492.md) | padding_ratio_075 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0792-1](../sources/experiences/exp-a-kd-20260519-0792-1.md) | Replace single-block <<<1,1024>>> kernel with a multi-block cooperative kernel l | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0794-1](../sources/experiences/exp-a-kd-20260519-0794-1.md) | Replace the single-thread serial loop with a parallel segmented prefix sum using | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0839-1](../sources/experiences/exp-a-kd-20260519-0839-1.md) | Replace serial global-memory scan with cooperative shared-memory load (8 threads | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0852-1](../sources/experiences/exp-a-kd-20260519-0852-1.md) | Replace Blelloch shared-memory scan with a warp-shuffle (__shfl_up_sync) based t | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0853-1](../sources/experiences/exp-a-kd-20260519-0853-1.md) | Replace the shared-memory Blelloch scan with a warp-shuffle (__shfl_up_sync) bas | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0854-1](../sources/experiences/exp-a-kd-20260519-0854-1.md) | Replace the Blelloch scan algorithm (O(log n) __syncthreads barriers per phase,  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0873-1](../sources/experiences/exp-a-kd-20260519-0873-1.md) | Replaced direct global memory reads with __ldca cache-all allocation hints to fo | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0906-1](../sources/experiences/exp-a-kd-20260519-0906-1.md) | Pre-allocate the tokens_cnts and cumsum buffers once before the benchmark loop a | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0912-1](../sources/experiences/exp-a-kd-20260519-0912-1.md) | Replace the single-thread sequential loop with a <<<1,256>>> CUB BlockScan that  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0913-1](../sources/experiences/exp-a-kd-20260519-0913-1.md) | Replace the single-thread serial loop with a CUB BlockScan inclusive prefix sum  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0936-1](../sources/experiences/exp-a-kd-20260519-0936-1.md) | Remove the zero_buffer_kernel entirely because moe_align_block_size_kernel alrea | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0949-1](../sources/experiences/exp-a-kd-20260519-0949-1.md) | Replace the single-thread serial cumsum with a parallel Blelloch prefix scan on  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0949-2](../sources/experiences/exp-a-kd-20260519-0949-2.md) | Replace warp-based div/mod index decomposition with direct shared_counts[expert_ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0949-3](../sources/experiences/exp-a-kd-20260519-0949-3.md) | Replace per-expert thread-mapped fill with a cooperative binary search over the  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0950-1](../sources/experiences/exp-a-kd-20260519-0950-1.md) | Replace the serial O(N) cumsum loop with a parallel Blelloch prefix scan that en | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0950-2](../sources/experiences/exp-a-kd-20260519-0950-2.md) | Use direct shared_counts[expert_id] indexing in the counting loop, eliminating t | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0950-3](../sources/experiences/exp-a-kd-20260519-0950-3.md) | Fill expert_ids cooperatively across all 1024 threads using binary search into t | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0955-1](../sources/experiences/exp-a-kd-20260519-0955-1.md) | Replace the Blelloch shared-memory scan with a two-level warp shuffle exclusive  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0956-1](../sources/experiences/exp-a-kd-20260519-0956-1.md) | Replace the Blelloch shared-memory scan (8 scan-phase __syncthreads across all 1 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0957-1](../sources/experiences/exp-a-kd-20260519-0957-1.md) | Replace Blelloch shared-memory scan with a two-level warp shuffle scan using __s | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0958-1](../sources/experiences/exp-a-kd-20260519-0958-1.md) | Replace the shared-memory Blelloch scan with a two-level warp-shuffle scan using | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1027-1](../sources/experiences/exp-a-kd-20260519-1027-1.md) | Replace contiguous-block iteration with stride-based (grid-stride) iteration whe | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1033-1](../sources/experiences/exp-a-kd-20260519-1033-1.md) | The after kernel eliminates atomics by giving each thread its own per-expert cou | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1034-1](../sources/experiences/exp-a-kd-20260519-1034-1.md) | Replace warp-atomicAdd counting with per-thread private token-count rows in shar | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1035-1](../sources/experiences/exp-a-kd-20260519-1035-1.md) | Replace the Blelloch shared-memory prefix scan with a two-level warp-exclusive s | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1036-1](../sources/experiences/exp-a-kd-20260519-1036-1.md) | Replace the Blelloch algorithm with a two-level warp exclusive scan using __shfl | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1055-1](../sources/experiences/exp-a-kd-20260519-1055-1.md) | Replace Blelloch up-sweep/down-sweep with a two-level warp shuffle approach: com | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1104-1](../sources/experiences/exp-a-kd-20260519-1104-1.md) | Align the shared memory write index with the read index by adding the row offset | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1156-1](../sources/experiences/exp-a-kd-20260519-1156-1.md) | Replace the serial single-thread prefix sum with CUB BlockScan<int32_t, 1024> wh | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1157-1](../sources/experiences/exp-a-kd-20260519-1157-1.md) | Replace the single-thread serial prefix sum loop with CUB BlockScan ExclusiveSum | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1158-1](../sources/experiences/exp-a-kd-20260519-1158-1.md) | Replace the single-thread serial loop with CUB BlockScan<int32_t,1024> Exclusive | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1230-1](../sources/experiences/exp-a-kd-20260519-1230-1.md) | Decouple state storage type from input type by storing ssm_states as float inste | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1231-1](../sources/experiences/exp-a-kd-20260519-1231-1.md) | Change ssm_states storage from __half to float, eliminating all half-to-float an | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1304-1](../sources/experiences/exp-a-kd-20260519-1304-1.md) | Replace the O(N) sequential scan with O(log N) binary search via findTotalEltsLe | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1305-1](../sources/experiences/exp-a-kd-20260519-1305-1.md) | Replace the O(N) linear scan with O(log N) binary search on the sorted array, re | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1312-1](../sources/experiences/exp-a-kd-20260519-1312-1.md) | Cooperatively load all 65 int64_t offsets (520 bytes) into shared memory via __l | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1402-1](../sources/experiences/exp-a-kd-20260519-1402-1.md) | Fuse both expert_offsets and 128-aligned blockscale_offsets prefix-sum computati | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1403-1](../sources/experiences/exp-a-kd-20260519-1403-1.md) | Fuse both expert_offsets and blockscale_offsets prefix-sum computations into a s | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1494-1](../sources/experiences/exp-a-kd-20260519-1494-1.md) | Replace static 2D shared memory with dynamically allocated flat array sized at r | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1517-1](../sources/experiences/exp-a-kd-20260519-1517-1.md) | Replace per-thread O(E) linear scan with warp-cooperative search: all 32 lanes s | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1518-1](../sources/experiences/exp-a-kd-20260519-1518-1.md) | Replace per-thread linear scan with warp-cooperative search: each of 32 lanes pr | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1554-1](../sources/experiences/exp-a-kd-20260519-1554-1.md) | Partition the single block's threads into 256 fill threads (stride=256, only 32  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1599-1](../sources/experiences/exp-a-kd-20260519-1599-1.md) | Replace the per-thread prefix-sum counter matrix with warp-level shared_counts[3 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1744-1](../sources/experiences/exp-a-kd-20260519-1744-1.md) | Replace compile-time fixed kChunkSize=512 chunk iteration with a runtime cu_chun | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1746-1](../sources/experiences/exp-a-kd-20260519-1746-1.md) | The after code unconditionally checks chunk_tokens per item for correctness acro | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1747-1](../sources/experiences/exp-a-kd-20260519-1747-1.md) | Remove the outer seqlen-modulo guard and replace chunk-index multiplication (chu | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2324-1](../sources/experiences/exp-a-kd-20260519-2324-1.md) | Replace per-thread 2D array accumulation with 1024 threads all using atomicAdd o | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2324-2](../sources/experiences/exp-a-kd-20260519-2324-2.md) | Replace the two serial phases with a single CUB BlockScan ExclusiveSum call wher | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2325-1](../sources/experiences/exp-a-kd-20260519-2325-1.md) | Replace thread-private shared memory row counting with a grid-stride loop using  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2325-2](../sources/experiences/exp-a-kd-20260519-2325-2.md) | Replace the serial prefix-sum loop with CUB BlockScan ExclusiveSum, which comput | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2326-1](../sources/experiences/exp-a-kd-20260519-2326-1.md) | Replace per-thread 2D counting rows with atomicAdd into a flat padded shared_cou | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2326-2](../sources/experiences/exp-a-kd-20260519-2326-2.md) | Replace the serial single-thread cumsum loop with CUB BlockScan ExclusiveSum, wh | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2365-1](../sources/experiences/exp-a-kd-20260519-2365-1.md) | Add an early-return guard that checks if cache_index equals pad_slot_id and imme | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2366-1](../sources/experiences/exp-a-kd-20260519-2366-1.md) | Add an early-return guard after cache_index resolution: if (cache_index == param | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2367-1](../sources/experiences/exp-a-kd-20260519-2367-1.md) | Add an early-return guard that checks if the cache_index equals the pad_slot_id  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2380-1](../sources/experiences/exp-a-kd-20260519-2380-1.md) | Replace per-thread sharded counting plus prefix-sum with stride-based atomicAdd  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2383-1](../sources/experiences/exp-a-kd-20260519-2383-1.md) | Replace per-thread contiguous sharding with stride-based iteration (tid/stride p | analysis | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0033](../sources/experiences/exp-o-kd-20260518-0033.md) | lor_N32 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0170](../sources/experiences/exp-o-kd-20260518-0170.md) | moe_align_256exp_32k_tokens | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0200](../sources/experiences/exp-o-kd-20260518-0200.md) | scan_256experts | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0232](../sources/experiences/exp-o-kd-20260518-0232.md) | moe_64ep_blk8_tok256 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0233](../sources/experiences/exp-o-kd-20260518-0233.md) | moe_64ep_blk16_tok4096 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0240](../sources/experiences/exp-o-kd-20260518-0240.md) | small_128rows_topk6 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0246](../sources/experiences/exp-o-kd-20260518-0246.md) | moe_64e_4kt | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0247](../sources/experiences/exp-o-kd-20260518-0247.md) | moe_256e_16kt | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0254](../sources/experiences/exp-o-kd-20260518-0254.md) | experts_64_bs32 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0257](../sources/experiences/exp-o-kd-20260518-0257.md) | scan_64_experts | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0258](../sources/experiences/exp-o-kd-20260518-0258.md) | scan_128_experts | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0286](../sources/experiences/exp-o-kd-20260518-0286.md) | scan_256exp | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0287](../sources/experiences/exp-o-kd-20260518-0287.md) | scan_64exp | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0290](../sources/experiences/exp-o-kd-20260518-0290.md) | scan_experts_64 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0348](../sources/experiences/exp-o-kd-20260518-0348.md) | sort_16k_tokens | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0349](../sources/experiences/exp-o-kd-20260518-0349.md) | sort_32k_tokens | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0390](../sources/experiences/exp-o-kd-20260518-0390.md) | expert_offset_seqscan_64ep | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0473](../sources/experiences/exp-o-kd-20260518-0473.md) | warp_expert_search_64ep | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0474](../sources/experiences/exp-o-kd-20260518-0474.md) | warp_expert_search_256ep | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0495](../sources/experiences/exp-o-kd-20260518-0495.md) | small_64epg_bs64 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0510](../sources/experiences/exp-o-kd-20260518-0510.md) | experts_64 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0531](../sources/experiences/exp-o-kd-20260518-0531.md) | seq8k | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0535](../sources/experiences/exp-o-kd-20260518-0535.md) | moe_64ep_512tk | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0601](../sources/experiences/exp-o-kd-20260518-0601.md) | ep64_n6144 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0696](../sources/experiences/exp-o-kd-20260518-0696.md) | Hat prevents utilizing multiple SMs on the GPU. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0697](../sources/experiences/exp-o-kd-20260518-0697.md) | , wasting warp utilization. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0706](../sources/experiences/exp-o-kd-20260518-0706.md) | Ame, totaling roughly 2*log2(scan_size) global barriers just for the scan. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0715](../sources/experiences/exp-o-kd-20260518-0715.md) | Transfer. Each small copy_() incurs dispatch overhead and cannot benefit from th | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0722](../sources/experiences/exp-o-kd-20260518-0722.md) | The optimization eliminates four per-call synchronous cudaMalloc/cudaFree calls  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0725](../sources/experiences/exp-o-kd-20260518-0725.md) | Hen num_experts is large (e.g., 256 for DeepSeek-V3). | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0729](../sources/experiences/exp-o-kd-20260518-0729.md) | Ites cumsum[0] = 0 and computes cumsum[i] = cumsum[i-1] + padded_count for all i | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0733](../sources/experiences/exp-o-kd-20260518-0733.md) | While all other 1023 threads were idle, creating a significant serialization bot | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0734](../sources/experiences/exp-o-kd-20260518-0734.md) | Threads are idle during the Blelloch scan (only tid < d threads participate per  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0737](../sources/experiences/exp-o-kd-20260518-0737.md) | Ites here'. The previous attempt to use multiple blocks caused illegal memory ac | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0746](../sources/experiences/exp-o-kd-20260518-0746.md) | Ia computed indices (offset * (2*tid+1) - 1), which can cause bank conflicts and | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0758](../sources/experiences/exp-o-kd-20260518-0758.md) | E, creating a significant serial bottleneck especially when num_experts is large | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0772](../sources/experiences/exp-o-kd-20260518-0772.md) | Ed shared memory (1024 bytes for local_offsets) and required an extra __syncthre | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0821](../sources/experiences/exp-o-kd-20260518-0821.md) | On the critical path. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0827](../sources/experiences/exp-o-kd-20260518-0827.md) | E uint16 fallback, can exceed device shared memory limits, forcing a fallback to | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0828](../sources/experiences/exp-o-kd-20260518-0828.md) | Quires the full 2D tokens_cnts matrix to be resident in shared memory with the p | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0846](../sources/experiences/exp-o-kd-20260518-0846.md) | Ave partially-computed tokens at the start (from a prior incomplete block), so t | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0874](../sources/experiences/exp-o-kd-20260518-0874.md) | Arge expert counts (e.g., 256 experts), forcing fallback to global memory or uin | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0875](../sources/experiences/exp-o-kd-20260518-0875.md) | Ts shard, writing sequentially. This limited parallelism to a single block and t | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0609-1](../sources/experiences/exp-o-kd-20260519-0609-1.md) | Replace single-block launch with multi-block cooperative kernel via cudaLaunchCo | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0610-1](../sources/experiences/exp-o-kd-20260519-0610-1.md) | Replace serial single-thread loop with a parallel segmented prefix sum: 16 activ | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0611-1](../sources/experiences/exp-o-kd-20260519-0611-1.md) | Replace the single-block <<<1,1024>>> launch with cudaLaunchCooperativeKernel us | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0612-1](../sources/experiences/exp-o-kd-20260519-0612-1.md) | Partition the prefix sum into segments of kElementsPerThr (16) experts per threa | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0633-1](../sources/experiences/exp-o-kd-20260519-0633-1.md) | Replace serial global-memory scan with cooperative shared-memory load where thre | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0647-1](../sources/experiences/exp-o-kd-20260519-0647-1.md) | Replace Blelloch shared-memory scan with warp shuffle-based two-level exclusive  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0648-1](../sources/experiences/exp-o-kd-20260519-0648-1.md) | Replace Blelloch scan with a warp shuffle (__shfl_up_sync) based two-level exclu | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0649-1](../sources/experiences/exp-o-kd-20260519-0649-1.md) | Replace Blelloch's two-phase scan with a two-level warp-shuffle exclusive prefix | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0650-1](../sources/experiences/exp-o-kd-20260519-0650-1.md) | Replace Blelloch scan with a two-level warp-based exclusive prefix sum: each war | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0668-1](../sources/experiences/exp-o-kd-20260519-0668-1.md) | Fuse the alignment and padding kernels into a single fused_align_and_padding_ker | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0668-2](../sources/experiences/exp-o-kd-20260519-0668-2.md) | Replace scalar int32_t stores with 4-wide vectorized stores using an alignas(16) | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0699-1](../sources/experiences/exp-o-kd-20260519-0699-1.md) | Extend the function signature to accept pre-allocated torch.Tensor buffers (toke | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0703-1](../sources/experiences/exp-o-kd-20260519-0703-1.md) | Replace the single-thread sequential loop with a <<<1,256>>> parallel CUB BlockS | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0704-1](../sources/experiences/exp-o-kd-20260519-0704-1.md) | Replace the single-thread serial loop with a CUB BlockScan-based parallel prefix | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0707-1](../sources/experiences/exp-o-kd-20260519-0707-1.md) | Replace the single-thread sequential loop with a parallel CUB BlockScan Inclusiv | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0719-1](../sources/experiences/exp-o-kd-20260519-0719-1.md) | Remove the redundant zero_buffer_kernel launch since moe_align_block_size_kernel | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0730-1](../sources/experiences/exp-o-kd-20260519-0730-1.md) | Replace serial single-thread cumsum with a parallel Blelloch prefix scan: all th | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0730-2](../sources/experiences/exp-o-kd-20260519-0730-2.md) | Use direct expert_id indexing into a flat shared_counts array (atomicAdd(&shared | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0730-3](../sources/experiences/exp-o-kd-20260519-0730-3.md) | Replace per-expert assignment with cooperative binary search: all threads stride | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0732-1](../sources/experiences/exp-o-kd-20260519-0732-1.md) | Replace the single-thread serial cumsum loop with a parallel Blelloch (work-effi | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0733-1](../sources/experiences/exp-o-kd-20260519-0733-1.md) | Replace Blelloch shared-memory scan (8 scan-phase + 2 auxiliary __syncthreads =  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0734-1](../sources/experiences/exp-o-kd-20260519-0734-1.md) | Replace Blelloch shared-memory scan with a two-level warp shuffle scan: use warp | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0735-1](../sources/experiences/exp-o-kd-20260519-0735-1.md) | Replace shared-memory Blelloch up-sweep/down-sweep with barrier-free __shfl_up_s | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0736-1](../sources/experiences/exp-o-kd-20260519-0736-1.md) | Replace the Blelloch shared-memory prefix sum with a two-level warp shuffle excl | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0770-1](../sources/experiences/exp-o-kd-20260519-0770-1.md) | Replace contiguous-block iteration with stride-based iteration (thread i starts  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0772-1](../sources/experiences/exp-o-kd-20260519-0772-1.md) | Merge the two-kernel pipeline into a single kernel with only 32 threads, replaci | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1078-1](../sources/experiences/exp-o-kd-20260519-1078-1.md) | Replace Blelloch algorithm with a two-level warp exclusive scan using __shfl_up_ | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1079-1](../sources/experiences/exp-o-kd-20260519-1079-1.md) | Replace the Blelloch algorithm with a two-level warp exclusive scan using __shfl | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1080-1](../sources/experiences/exp-o-kd-20260519-1080-1.md) | Replace Blelloch scan with a two-level warp exclusive scan using __shfl_up_sync: | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1083-1](../sources/experiences/exp-o-kd-20260519-1083-1.md) | Replace Blelloch scan with a two-level warp-shuffle hierarchical exclusive scan  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1882-1](../sources/experiences/exp-o-kd-20260519-1882-1.md) | Replace the single-thread serial prefix sum loop with CUB BlockScan<int32_t, 102 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1883-1](../sources/experiences/exp-o-kd-20260519-1883-1.md) | Replace the serial single-thread prefix sum with CUB BlockScan parallel exclusiv | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1884-1](../sources/experiences/exp-o-kd-20260519-1884-1.md) | Replace the serial single-thread loop with CUB BlockScan's ExclusiveSum primitiv | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1974-1](../sources/experiences/exp-o-kd-20260519-1974-1.md) | Replace the per-thread linear scan with a templated binary search (findTotalElts | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1975-1](../sources/experiences/exp-o-kd-20260519-1975-1.md) | Replace the per-thread O(N) linear scan with a templated binary search (findTota | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2023-1](../sources/experiences/exp-o-kd-20260519-2023-1.md) | Launch max(num_experts, WARP_SIZE) threads to guarantee full-warp execution, res | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2034-1](../sources/experiences/exp-o-kd-20260519-2034-1.md) | Fuse the GPU kernel and CPU host function into a single GPU kernel that computes | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2035-1](../sources/experiences/exp-o-kd-20260519-2035-1.md) | Fuse the separate GPU expert_offsets kernel and the CPU blockscale_offsets compu | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2056-1](../sources/experiences/exp-o-kd-20260519-2056-1.md) | Reorder shared memory so cumsum (always int32_t) sits at the base and tokens_cnt | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2115-1](../sources/experiences/exp-o-kd-20260519-2115-1.md) | Overlap sorted_token_ids global-memory initialization with expert counting by la | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2116-1](../sources/experiences/exp-o-kd-20260519-2116-1.md) | Launch 320 total threads (256 fill_threads + 64 working threads) in a single blo | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2140-1](../sources/experiences/exp-o-kd-20260519-2140-1.md) | Replace the per-thread 2D prefix-sum counter matrix with warp-partitioned atomic | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2205-1](../sources/experiences/exp-o-kd-20260519-2205-1.md) | Replace fixed-size kChunkSize=512 chunking with variable-length chunks read from | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2206-1](../sources/experiences/exp-o-kd-20260519-2206-1.md) | Replace uniform kChunkSize iteration with variable-length chunks read from a pre | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2207-1](../sources/experiences/exp-o-kd-20260519-2207-1.md) | Replace uniform kChunkSize-based chunk iteration with variable-length chunk iter | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2266-1](../sources/experiences/exp-o-kd-20260519-2266-1.md) | Replace per-thread private 2D counting array with a flat shared_counts array upd | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2266-2](../sources/experiences/exp-o-kd-20260519-2266-2.md) | Replace the two-phase serial prefix-sum + serial aligned cumsum with a single CU | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2267-1](../sources/experiences/exp-o-kd-20260519-2267-1.md) | Scale to 1024 threads using a grid-stride loop with atomicAdd into a flat padded | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2267-2](../sources/experiences/exp-o-kd-20260519-2267-2.md) | Replace the serial two-phase prefix sum (per-expert column scan by num_experts t | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2268-1](../sources/experiences/exp-o-kd-20260519-2268-1.md) | Replace the 2D per-thread tokens_cnts array with a flat shared_counts array upda | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2268-2](../sources/experiences/exp-o-kd-20260519-2268-2.md) | Replace the single-thread serial cumsum loop with CUB BlockScan::ExclusiveSum, c | optimization | sm90 | cuda-cpp |

## softmax

| ID | Title | Type | Architectures | Languages |
|----|-------|------|--------------|-----------|
| [exp-a-20260325-191646-f77b236f](../sources/experiences/exp-a-20260325-191646-f77b236f.md) | ## Task
Fix the flash attention kernel for FA_14 (fp32_flash_attention_qwen2_5_7b_q4_0_cache4096). The kernel must:
1. L | analysis | sm90 | cuda-cpp |
| [exp-a-20260326-095034-2fac4e75](../sources/experiences/exp-a-20260326-095034-2fac4e75.md) | ## Task
Optimize the flash attention kernel for FA_15 (Qwen2.5-7B Q4_0 KV cache). The baseline (v1) achieves 0.0046x spe | analysis | sm90 | cuda-cpp |
| [exp-a-20260326-103616-7d4a9433](../sources/experiences/exp-a-20260326-103616-7d4a9433.md) | ## Task
Write a pure CUDA flash attention kernel for Q4_0 KV cache dequantization

## Goal
Create kernel.cu with extern  | analysis | sm90 | cuda-cpp |
| [exp-a-20260326-173130-2b19071b](../sources/experiences/exp-a-20260326-173130-2b19071b.md) | ## Task
Optimize flash attention kernel for FA_12 task

## Goal
Improve speedup from 0.005 to >0.5 with correct output

 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0135](../sources/experiences/exp-a-kd-20260518-0135.md) | Divide mi by kLog2e before adding to logf(s_prime) to convert from log2-scaled s | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0255](../sources/experiences/exp-a-kd-20260518-0255.md) | pipeline_d64_seq256 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0264](../sources/experiences/exp-a-kd-20260518-0264.md) | head64_seq512 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0969](../sources/experiences/exp-a-kd-20260518-0969.md) | softmax_vs_sigmoid_256experts | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0970](../sources/experiences/exp-a-kd-20260518-0970.md) | softmax_vs_sigmoid_64experts | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1017](../sources/experiences/exp-a-kd-20260518-1017.md) | bf16_64experts | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1021](../sources/experiences/exp-a-kd-20260518-1021.md) | bf16_64experts_fallback | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1022](../sources/experiences/exp-a-kd-20260518-1022.md) | bf16_8experts_fallback | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1390](../sources/experiences/exp-a-kd-20260518-1390.md) | smem_within_default | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0007-1](../sources/experiences/exp-a-kd-20260519-0007-1.md) | Change fast_exp return type from float to half_t so ::hexp() result stays in FP1 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0008-1](../sources/experiences/exp-a-kd-20260519-0008-1.md) | Widening from 32-bit (uint32_t) to 128-bit (uint4) vectorized load/store process | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0021-1](../sources/experiences/exp-a-kd-20260519-0021-1.md) | Replace max() with fmax() for explicit IEEE 754 float max semantics, but the CUD | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0111-1](../sources/experiences/exp-a-kd-20260519-0111-1.md) | Replace atomicAdd with warp-partitioned addition_storage where each warp writes  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0112-1](../sources/experiences/exp-a-kd-20260519-0112-1.md) | Replace contended atomicAdd with per-warp disjoint slots in addition_storage[] ( | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0115-1](../sources/experiences/exp-a-kd-20260519-0115-1.md) | Pre-scale input values by (scaling * kLog2e) before computing the row-wise max s | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0116-1](../sources/experiences/exp-a-kd-20260519-0116-1.md) | Pre-scale the fragment with scaling * kLog2e before the max-reduction so atomicM | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0132-1](../sources/experiences/exp-a-kd-20260519-0132-1.md) | Replace atomicAdd with warp-partitioned addition_storage where each warp writes  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0133-1](../sources/experiences/exp-a-kd-20260519-0133-1.md) | Distribute exp2f computation across warps so each warp owns kLinesPerWarp rows a | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0135-1](../sources/experiences/exp-a-kd-20260519-0135-1.md) | Divide mi by kLog2e before adding to logf(s_prime), undoing the log2 scaling so  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0978-1](../sources/experiences/exp-a-kd-20260519-0978-1.md) | Read input once in pass 1 and write converted float values to the output array,  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0979-1](../sources/experiences/exp-a-kd-20260519-0979-1.md) | Cache converted float values by writing them to the output buffer during pass 1, | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1069-1](../sources/experiences/exp-a-kd-20260519-1069-1.md) | Replace CUB BlockReduce with a warp-level butterfly design where each thread own | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1070-1](../sources/experiences/exp-a-kd-20260519-1070-1.md) | Set VPT=16 so each thread owns all 16 expert values of a row (THREADS_PER_ROW=1) | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1071-1](../sources/experiences/exp-a-kd-20260519-1071-1.md) | Replace three-pass scalar strided loads with AlignedArray<float,4> vectorized pa | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1071-2](../sources/experiences/exp-a-kd-20260519-1071-2.md) | Eliminate shared-memory BlockReduce entirely by assigning each thread an entire  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1072-1](../sources/experiences/exp-a-kd-20260519-1072-1.md) | Replace scalar stride-256 loads with vectorized 16-byte packed loads via Aligned | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1072-2](../sources/experiences/exp-a-kd-20260519-1072-2.md) | Load the row chunk into registers once (row_chunk[VPT]), then perform all three  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1250-1](../sources/experiences/exp-a-kd-20260519-1250-1.md) | Fuse the reduce and quantize kernels into a single kernel that computes softmax  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1406-1](../sources/experiences/exp-a-kd-20260519-1406-1.md) | Replace always-softmax scoring with compile-time branched scoring via if constex | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1408-1](../sources/experiences/exp-a-kd-20260519-1408-1.md) | Replace softmax with element-wise sigmoid (1/(1+exp(-x))) which needs only a sin | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1454-1](../sources/experiences/exp-a-kd-20260519-1454-1.md) | Fuse the BF16-to-float conversion directly into the softmax kernel by replacing  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1455-1](../sources/experiences/exp-a-kd-20260519-1455-1.md) | Fuse BF16→float conversion directly into the softmax kernel by calling __bfloat1 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1458-1](../sources/experiences/exp-a-kd-20260519-1458-1.md) | Fuse the BF16→float conversion into the softmax kernel by inlining __bfloat162fl | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1459-1](../sources/experiences/exp-a-kd-20260519-1459-1.md) | Fuse BF16→float conversion directly into the softmax kernel by calling __bfloat1 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1827-1](../sources/experiences/exp-a-kd-20260519-1827-1.md) | Add cudaFuncSetAttribute with cudaFuncAttributeMaxDynamicSharedMemorySize before | analysis | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0105](../sources/experiences/exp-o-kd-20260518-0105.md) | head64_acc | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0109](../sources/experiences/exp-o-kd-20260518-0109.md) | d64_s512 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0440](../sources/experiences/exp-o-kd-20260518-0440.md) | softmax_vs_sigmoid_fallback | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0453](../sources/experiences/exp-o-kd-20260518-0453.md) | bf16_8experts | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0633](../sources/experiences/exp-o-kd-20260518-0633.md) | Fferences across runs and create contention when multiple warps target the same  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0666](../sources/experiences/exp-o-kd-20260518-0666.md) | Nd each conversion introduces rounding error that accumulates across the K-seqle | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0667](../sources/experiences/exp-o-kd-20260518-0667.md) | 6 (__float2half_rn). This repeated FP16->FP32->FP16 round-trip loses precision a | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0806](../sources/experiences/exp-o-kd-20260518-0806.md) | Applied change: The moeSoftmax kernel was templated on InputType (float, __nv_bf | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0254-1](../sources/experiences/exp-o-kd-20260519-0254-1.md) | Replace atomicAdd cross-warp reduction with a per-warp addition_storage array (n | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1094-1](../sources/experiences/exp-o-kd-20260519-1094-1.md) | Pack all 8 elements per row into a single thread via VPT=8 (THREADS_PER_ROW=1),  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1095-1](../sources/experiences/exp-o-kd-20260519-1095-1.md) | Set VPT=16 so each single thread owns all 16 elements of a row, eliminating cros | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1096-1](../sources/experiences/exp-o-kd-20260519-1096-1.md) | Replace scalar strided loads with AlignedArray<float, 4> vectorized packed loads | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1096-2](../sources/experiences/exp-o-kd-20260519-1096-2.md) | Reorganize data ownership so each thread owns VPT=16 elements (entire row), enab | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1097-1](../sources/experiences/exp-o-kd-20260519-1097-1.md) | Replace scalar strided loads with vectorized packed loads (VPT=4, BYTES_PER_LDG= | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2036-1](../sources/experiences/exp-o-kd-20260519-2036-1.md) | Replace the reduction-heavy per-row softmax (3 global passes + 2 shared-memory r | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2057-1](../sources/experiences/exp-o-kd-20260519-2057-1.md) | Fuse BF16-to-float conversion directly into the softmax kernel by inlining __bfl | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2058-1](../sources/experiences/exp-o-kd-20260519-2058-1.md) | Fuse the BF16→float conversion into the softmax kernel by calling __bfloat162flo | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2061-1](../sources/experiences/exp-o-kd-20260519-2061-1.md) | Fuse the two kernels into a single fusedBf16Softmax kernel that reads BF16 input | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2062-1](../sources/experiences/exp-o-kd-20260519-2062-1.md) | Fuse the BF16-to-float conversion directly into the softmax kernel by calling __ | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2067-1](../sources/experiences/exp-o-kd-20260519-2067-1.md) | Template the moeSoftmax kernel on InputType (float, __nv_bfloat16, or __half) an | optimization | sm90 | cuda-cpp |

## topk

| ID | Title | Type | Architectures | Languages |
|----|-------|------|--------------|-----------|
| [exp-a-kd-20260518-0448](../sources/experiences/exp-a-kd-20260518-0448.md) | bf16_m512_topk8_k4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0449](../sources/experiences/exp-a-kd-20260518-0449.md) | bf16_m64_topk2_k2048 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0459](../sources/experiences/exp-a-kd-20260518-0459.md) | fp64_float_acc_vs_double_acc | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0460](../sources/experiences/exp-a-kd-20260518-0460.md) | compile_time_topk_vs_runtime_topk | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0512](../sources/experiences/exp-a-kd-20260518-0512.md) | nfs1_topk7 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0514](../sources/experiences/exp-a-kd-20260518-0514.md) | small_16rows_topk6 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0516](../sources/experiences/exp-a-kd-20260518-0516.md) | small_512rows_topk6 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0527](../sources/experiences/exp-a-kd-20260518-0527.md) | float_256epg8_nshared0_topk6 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0528](../sources/experiences/exp-a-kd-20260518-0528.md) | float_256epg8_nshared1_topk7 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0536](../sources/experiences/exp-a-kd-20260518-0536.md) | smem_layout_32_512 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0550](../sources/experiences/exp-a-kd-20260518-0550.md) | topk_nonzero_offset | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0564](../sources/experiences/exp-a-kd-20260518-0564.md) | float_per_token_topk8_h256 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0576](../sources/experiences/exp-a-kd-20260518-0576.md) | bf16_m512_topk8_row4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0614](../sources/experiences/exp-a-kd-20260518-0614.md) | bfloat16_topk6_4096rows | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0618](../sources/experiences/exp-a-kd-20260518-0618.md) | small_batch_256_8exp | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0631](../sources/experiences/exp-a-kd-20260518-0631.md) | varied_nnz_extreme | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0648](../sources/experiences/exp-a-kd-20260518-0648.md) | fused_loop | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0653](../sources/experiences/exp-a-kd-20260518-0653.md) | bf16_topk8_hidden4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0654](../sources/experiences/exp-a-kd-20260518-0654.md) | float_8exp_k2 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0656](../sources/experiences/exp-a-kd-20260518-0656.md) | topk_k2_exp64 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0657](../sources/experiences/exp-a-kd-20260518-0657.md) | topk_k4_exp64 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0662](../sources/experiences/exp-a-kd-20260518-0662.md) | fp16_topk2_r2048 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0688](../sources/experiences/exp-a-kd-20260518-0688.md) | float_32epg | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0689](../sources/experiences/exp-a-kd-20260518-0689.md) | float_64epg | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0750](../sources/experiences/exp-a-kd-20260518-0750.md) | spread_32k | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0766](../sources/experiences/exp-a-kd-20260518-0766.md) | topk3_512rows | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0863](../sources/experiences/exp-a-kd-20260518-0863.md) | smem_expert_map_64ep | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0864](../sources/experiences/exp-a-kd-20260518-0864.md) | smem_expert_map_8ep | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0869](../sources/experiences/exp-a-kd-20260518-0869.md) | large_64experts | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0870](../sources/experiences/exp-a-kd-20260518-0870.md) | smoke_small | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0922](../sources/experiences/exp-a-kd-20260518-0922.md) | large_m_noswap | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0966](../sources/experiences/exp-a-kd-20260518-0966.md) | experts_64_topk8 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0999](../sources/experiences/exp-a-kd-20260518-0999.md) | clone_always_small | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1000](../sources/experiences/exp-a-kd-20260518-1000.md) | no_expert_map | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1001](../sources/experiences/exp-a-kd-20260518-1001.md) | with_expert_map | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1082](../sources/experiences/exp-a-kd-20260518-1082.md) | valid_only_8experts | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1094](../sources/experiences/exp-a-kd-20260518-1094.md) | smem_writes | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1115](../sources/experiences/exp-a-kd-20260518-1115.md) | large_256epg_bs64 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1129](../sources/experiences/exp-a-kd-20260518-1129.md) | topk_k16_N256 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1130](../sources/experiences/exp-a-kd-20260518-1130.md) | topk_k4_N64 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1131](../sources/experiences/exp-a-kd-20260518-1131.md) | topk_k8_N128 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1154](../sources/experiences/exp-a-kd-20260518-1154.md) | large_64experts | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1156](../sources/experiences/exp-a-kd-20260518-1156.md) | large_64experts | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1157](../sources/experiences/exp-a-kd-20260518-1157.md) | small_8experts | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1254](../sources/experiences/exp-a-kd-20260518-1254.md) | float_k4 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1255](../sources/experiences/exp-a-kd-20260518-1255.md) | half_k8 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1418](../sources/experiences/exp-a-kd-20260518-1418.md) | q4_0_need_sum_true | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1446](../sources/experiences/exp-a-kd-20260518-1446.md) | mask_active | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1447](../sources/experiences/exp-a-kd-20260518-1447.md) | mask_nullptr | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1506](../sources/experiences/exp-a-kd-20260518-1506.md) | sort_256ep_4096tok | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1509](../sources/experiences/exp-a-kd-20260518-1509.md) | small_8ep_512tok | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0790-1](../sources/experiences/exp-a-kd-20260519-0790-1.md) | Fuse both normalize and scale operations into a single fused_rescale_kernel wher | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0808-1](../sources/experiences/exp-a-kd-20260519-0808-1.md) | Fuse renormalization directly into the moeTopK kernel: accumulate the topk weigh | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0809-1](../sources/experiences/exp-a-kd-20260519-0809-1.md) | Fuse renormalization into moeTopK by accumulating row_sum_for_renormalize during | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0810-1](../sources/experiences/exp-a-kd-20260519-0810-1.md) | Fuse renormalization into the topk gating softmax kernel by accumulating the top | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0811-1](../sources/experiences/exp-a-kd-20260519-0811-1.md) | Fuse renormalization into the topkGatingSoftmax kernel by accumulating row_sum_f | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0850-1](../sources/experiences/exp-a-kd-20260519-0850-1.md) | Fuse both kernels into a single topk_fused_ragged_kernel that performs top-K sel | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0851-1](../sources/experiences/exp-a-kd-20260519-0851-1.md) | Fuse topk selection and offset addition into a single kernel (topk_fused_ragged_ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0866-1](../sources/experiences/exp-a-kd-20260519-0866-1.md) | Replace the bulk AccessType<T> assignment with a #pragma unroll loop that extrac | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0867-1](../sources/experiences/exp-a-kd-20260519-0867-1.md) | The before code uses direct struct copy (row_chunk_vec_ptr[0] = vec_thread_read_ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0868-1](../sources/experiences/exp-a-kd-20260519-0868-1.md) | Reduce per-block dynamic shared memory from 128KB to 32KB (kSmem = 8*1024*sizeof | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0907-1](../sources/experiences/exp-a-kd-20260519-0907-1.md) | Pre-allocate the reusable tokens_cnts and cumsum buffers once before the benchma | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0908-1](../sources/experiences/exp-a-kd-20260519-0908-1.md) | Replace scalar int32 loads with int4 (128-bit) vectorized loads, fetching four i | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0909-1](../sources/experiences/exp-a-kd-20260519-0909-1.md) | Replace scalar int32 loads with int4 vectorized loads (4×int32 per transaction)  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0923-1](../sources/experiences/exp-a-kd-20260519-0923-1.md) | Generalize the shared expert handling by replacing the binary conditional with d | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0924-1](../sources/experiences/exp-a-kd-20260519-0924-1.md) | Replace round-robin single-slot assignment with sequential assignment starting f | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0925-1](../sources/experiences/exp-a-kd-20260519-0925-1.md) | Replace per-warp subset scanning with one-thread-per-expert: each thread reads i | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0926-1](../sources/experiences/exp-a-kd-20260519-0926-1.md) | Replace per-warp subset scanning with one-thread-per-expert direct mapping where | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0926-2](../sources/experiences/exp-a-kd-20260519-0926-2.md) | Add #pragma unroll directive and replace WARP_SIZE/2 with compile-time constant  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0927-1](../sources/experiences/exp-a-kd-20260519-0927-1.md) | Replace per-warp subset scanning with one-thread-per-expert assignment: each thr | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0928-1](../sources/experiences/exp-a-kd-20260519-0928-1.md) | Replace scalar stride loads with float4 vectorized loads via reinterpret_cast<fl | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0929-1](../sources/experiences/exp-a-kd-20260519-0929-1.md) | Replace scalar stride loads with float4 vectorized loads: reinterpret input and  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0937-1](../sources/experiences/exp-a-kd-20260519-0937-1.md) | Remove the zero_buffer_kernel call entirely: moe_align_block_size_kernel already | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0938-1](../sources/experiences/exp-a-kd-20260519-0938-1.md) | Remove the redundant always-true guard and dedent the body, compute topk_excludi | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0939-1](../sources/experiences/exp-a-kd-20260519-0939-1.md) | Reduce the cooperative topk loop from 7 to 6 iterations by computing topk_exclud | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0947-1](../sources/experiences/exp-a-kd-20260519-0947-1.md) | Replace static __shared__ declarations with extern __shared__ dynamic allocation | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0948-1](../sources/experiences/exp-a-kd-20260519-0948-1.md) | Replace static __shared__ declarations with a single extern __shared__ buffer ma | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0961-1](../sources/experiences/exp-a-kd-20260519-0961-1.md) | Add a per-row row_start parameter to fast_topk_cuda_tl and a row_starts array in | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0962-1](../sources/experiences/exp-a-kd-20260519-0962-1.md) | Add a row_start parameter to fast_topk_cuda_tl and change all five input access  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0985-1](../sources/experiences/exp-a-kd-20260519-0985-1.md) | Replace scalar bf16 access with flashinfer::vec_t vectorized load/store (8 bf16  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0990-1](../sources/experiences/exp-a-kd-20260519-0990-1.md) | Extract the token-sorting phase into a separate moe_token_sort_kernel launched w | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0991-1](../sources/experiences/exp-a-kd-20260519-0991-1.md) | Decompose the monolithic kernel into two phases: keep the counting/cumsum in a s | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1025-1](../sources/experiences/exp-a-kd-20260519-1025-1.md) | Fuse the rescale (divide-by-sum) and scale (multiply-by-factor) into a single ke | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1026-1](../sources/experiences/exp-a-kd-20260519-1026-1.md) | Fuse rescale (divide by sum) and scale (multiply by routed_scaling_factor) into  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1030-1](../sources/experiences/exp-a-kd-20260519-1030-1.md) | Consolidate the two-kernel pipeline into a single kernel where each thread maint | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1031-1](../sources/experiences/exp-a-kd-20260519-1031-1.md) | Fuse the two-kernel pipeline into a single kernel using per-thread counting arra | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1039-1](../sources/experiences/exp-a-kd-20260519-1039-1.md) | Replace the per-thread counting matrix with atomicAdd to a single shared_counts[ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1056-1](../sources/experiences/exp-a-kd-20260519-1056-1.md) | Convert KernelParamsDynamic (runtime int fields) into a templated KernelParams s | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1057-1](../sources/experiences/exp-a-kd-20260519-1057-1.md) | Replace KernelParamsDynamic (runtime int fields) with a templated KernelParams<V | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1060-1](../sources/experiences/exp-a-kd-20260519-1060-1.md) | Stage topk results in shared memory arrays (smem_score/smem_idx) instead of writ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1060-2](../sources/experiences/exp-a-kd-20260519-1060-2.md) | Replace the single-thread serial rescale loop with a warp-stride batched write t | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1065-1](../sources/experiences/exp-a-kd-20260519-1065-1.md) | Fuse sigmoid into the TopK kernel using AlignedArray<float,4> vector loads (16 b | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1065-2](../sources/experiences/exp-a-kd-20260519-1065-2.md) | Replace CUB BlockReduce with a warp-shuffle butterfly XOR reduction (__shfl_xor_ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1066-1](../sources/experiences/exp-a-kd-20260519-1066-1.md) | Fuse sigmoid and TopK into a single kernel where each thread computes sigmoid on | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1066-2](../sources/experiences/exp-a-kd-20260519-1066-2.md) | Use AlignedArray<float, 4> vector loads (16 bytes per LDG transaction) with inte | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1066-3](../sources/experiences/exp-a-kd-20260519-1066-3.md) | Replace CUB BlockReduce + global-memory exclusion checks with register-only TopK | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1067-1](../sources/experiences/exp-a-kd-20260519-1067-1.md) | Track top-2 elements simultaneously per thread using a TopKPair struct (max + se | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1068-1](../sources/experiences/exp-a-kd-20260519-1068-1.md) | Introduce a TopKPair struct tracking both max and secondMax per thread, with a c | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1125-1](../sources/experiences/exp-a-kd-20260519-1125-1.md) | Fuse sigmoid_accurate() and per-expert bias addition directly into the top-2 sea | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1126-1](../sources/experiences/exp-a-kd-20260519-1126-1.md) | Fuse sigmoid+bias computation directly into the top-2 selection loop: each threa | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1128-1](../sources/experiences/exp-a-kd-20260519-1128-1.md) | Fuse the two kernels into a single candidates_after_kernel that reads raw scores | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1163-1](../sources/experiences/exp-a-kd-20260519-1163-1.md) | Guard the warp_reduce_sum call with if(renormalize) so the entire warp cooperati | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1187-1](../sources/experiences/exp-a-kd-20260519-1187-1.md) | Replace the single-pass 512-bin histogram with a progressive 4-step refinement u | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1188-1](../sources/experiences/exp-a-kd-20260519-1188-1.md) | Increase bins from 512 to 2048 and replace the single all-bins BlockScan with a  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1188-2](../sources/experiences/exp-a-kd-20260519-1188-2.md) | Use a multi-step progressive refinement where each step applies isPartialMatch f | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1204-1](../sources/experiences/exp-a-kd-20260519-1204-1.md) | Pre-compute all sh_ids[i] / top_k results into a second shared memory buffer (sh | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1221-1](../sources/experiences/exp-a-kd-20260519-1221-1.md) | Split the fused kernel into two: the align kernel computes expert counts and cum | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1223-1](../sources/experiences/exp-a-kd-20260519-1223-1.md) | Split the monolithic single-block kernel into an align kernel (counting/cumsum,  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1300-1](../sources/experiences/exp-a-kd-20260519-1300-1.md) | Cache the expert_map into shared memory via a cooperative load loop with __synct | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1306-1](../sources/experiences/exp-a-kd-20260519-1306-1.md) | Cache the expert_map into shared memory via cooperative strided loading with __s | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1307-1](../sources/experiences/exp-a-kd-20260519-1307-1.md) | Add cooperative shared-memory loading of expert_map with __syncthreads() barrier | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1335-1](../sources/experiences/exp-a-kd-20260519-1335-1.md) | Fuse softmax and topk into a single topkGatingSoftmax kernel using 8-byte vector | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1359-1](../sources/experiences/exp-a-kd-20260519-1359-1.md) | Introduce a compile-time template parameter SWAP_AB with a threshold constant, u | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1373-1](../sources/experiences/exp-a-kd-20260519-1373-1.md) | Launch max(num_experts, WARP_SIZE)=32 threads to fill the entire warp, halving p | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1374-1](../sources/experiences/exp-a-kd-20260519-1374-1.md) | Launch max(num_experts, 32) threads to fill all warp lanes, distributing token-c | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1407-1](../sources/experiences/exp-a-kd-20260519-1407-1.md) | Replace softmax scoring with per-element sigmoid scoring (1/(1+exp(-x))) via a c | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1435-1](../sources/experiences/exp-a-kd-20260519-1435-1.md) | Add const-correctness to sortAndScanExpert and CubKeyValueSorter::run by changin | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1436-1](../sources/experiences/exp-a-kd-20260519-1436-1.md) | Change sortAndScanExpert's first parameter from int* to const int* and propagate | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1438-1](../sources/experiences/exp-a-kd-20260519-1438-1.md) | Introduce a lazy-clone pattern: alias the original buffer via a shallow pointer  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1450-1](../sources/experiences/exp-a-kd-20260519-1450-1.md) | Template the token count storage type as uint16_t, halving the tokens_cnts share | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1451-1](../sources/experiences/exp-a-kd-20260519-1451-1.md) | Reduce token count type from int32_t to uint16_t and relocate both tokens_cnts a | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1456-1](../sources/experiences/exp-a-kd-20260519-1456-1.md) | Fuse topk selection and renormalize into a single fusedTopkRenormKernel: accumul | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1457-1](../sources/experiences/exp-a-kd-20260519-1457-1.md) | Fuse renormalization into the topk selection loop: thread 0 accumulates selected | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1460-1](../sources/experiences/exp-a-kd-20260519-1460-1.md) | Fuse the topk selection and renormalize into a single kernel by accumulating sel | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1461-1](../sources/experiences/exp-a-kd-20260519-1461-1.md) | Fuse renormalization into the topk kernel by accumulating selected_sum during ea | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1493-1](../sources/experiences/exp-a-kd-20260519-1493-1.md) | Replace static __shared__ 2D arrays with extern __shared__ dynamic allocation si | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1495-1](../sources/experiences/exp-a-kd-20260519-1495-1.md) | Replace static shared memory with dynamic shared memory (extern __shared__) and  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1519-1](../sources/experiences/exp-a-kd-20260519-1519-1.md) | Load topk_ids[i] into a local const register (expert_id), add an expert_id == -1 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1528-1](../sources/experiences/exp-a-kd-20260519-1528-1.md) | Remove the outLogits output entirely: eliminate the float* outLogits parameter,  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1529-1](../sources/experiences/exp-a-kd-20260519-1529-1.md) | Remove the 8KB smemLogits shared memory buffer entirely, eliminate logit writes  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1530-1](../sources/experiences/exp-a-kd-20260519-1530-1.md) | Remove the outLogits output pointer, the topkVals shared memory array, and all c | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1531-1](../sources/experiences/exp-a-kd-20260519-1531-1.md) | Remove the smemLogits[kTopK] shared-memory buffer entirely; only store indices i | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1532-1](../sources/experiences/exp-a-kd-20260519-1532-1.md) | Eliminate the TopKSort stage entirely since only unsorted top-K indices are requ | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1555-1](../sources/experiences/exp-a-kd-20260519-1555-1.md) | Split the 320 total threads into 256 dedicated fill_threads that initialize sort | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1566-1](../sources/experiences/exp-a-kd-20260519-1566-1.md) | Replace O(N*K) iterative selection with WarpSelect incremental algorithm: read i | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1567-1](../sources/experiences/exp-a-kd-20260519-1567-1.md) | Replace iterative max-selection with WarpSelect incremental top-k: process eleme | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1568-1](../sources/experiences/exp-a-kd-20260519-1568-1.md) | WarpSelect replaces iterative max-selection with an incremental top-k buffer: el | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1569-1](../sources/experiences/exp-a-kd-20260519-1569-1.md) | Replace manual __shfl_xor_sync reduction loops with cooperative_groups::reduce(t | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1570-1](../sources/experiences/exp-a-kd-20260519-1570-1.md) | Replace manual __shfl_xor_sync reduction loops with cooperative_groups::reduce u | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1570-2](../sources/experiences/exp-a-kd-20260519-1570-2.md) | Add a runtime branch on num_experts_per_group > WARP_SIZE: when false, each thre | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1593-1](../sources/experiences/exp-a-kd-20260519-1593-1.md) | Replace the sort-based pipeline (init_indices + radix sort + build_perms_from_so | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1594-1](../sources/experiences/exp-a-kd-20260519-1594-1.md) | Replace the sort-based pipeline with a single-pass atomic scatter: compute_arg_s | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1596-1](../sources/experiences/exp-a-kd-20260519-1596-1.md) | Replace the large per-thread global-memory counts matrix with warp-partitioned s | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1598-1](../sources/experiences/exp-a-kd-20260519-1598-1.md) | Replace the global-memory tokens_cnts matrix with warp-partitioned shared_counts | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1598-2](../sources/experiences/exp-a-kd-20260519-1598-2.md) | Replace per-thread counter + cumsum lookup with a single atomicAdd on shared-mem | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1677-1](../sources/experiences/exp-a-kd-20260519-1677-1.md) | Replace full O(N log N) sort with multi-pass radix selection: a coarse 256-bin F | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1678-1](../sources/experiences/exp-a-kd-20260519-1678-1.md) | Replace full sort with multi-pass radix selection: build a coarse 256-bin FP16 h | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1679-1](../sources/experiences/exp-a-kd-20260519-1679-1.md) | Fuse histogram construction into the candidate buffering scan by computing the n | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1680-1](../sources/experiences/exp-a-kd-20260519-1680-1.md) | Reduce shared memory allocation from 128KB to 32KB (kSmem=8*1024*sizeof(uint32_t | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1681-1](../sources/experiences/exp-a-kd-20260519-1681-1.md) | Add early-exit checks (remaining_k == 0) both after initial threshold finding an | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1682-1](../sources/experiences/exp-a-kd-20260519-1682-1.md) | Replace FP32-based 32-bit sign-flip and shift-mask with convert_to_uint8 which c | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1688-1](../sources/experiences/exp-a-kd-20260519-1688-1.md) | Eliminate the downstream compute_expert_offsets and compute_arg_sorts kernel lau | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1691-1](../sources/experiences/exp-a-kd-20260519-1691-1.md) | Pack the float value and int32_t index into a single uint64_t word using cub::Tr | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1692-1](../sources/experiences/exp-a-kd-20260519-1692-1.md) | Pack half-precision value bits and index into a single uint32_t via cub::Traits: | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1693-1](../sources/experiences/exp-a-kd-20260519-1693-1.md) | Replace the branching bubble-sort with a fixed 5-swap branchless sorting network | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1694-1](../sources/experiences/exp-a-kd-20260519-1694-1.md) | Replace the branch-based conditional swap with a branchless TOPK_SWAP macro that | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1695-1](../sources/experiences/exp-a-kd-20260519-1695-1.md) | Split N=8 candidates into 2 groups of 4, apply a sorting network (Sort4) and per | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1696-1](../sources/experiences/exp-a-kd-20260519-1696-1.md) | Replace flat scan-all-N with hierarchical strategy: split N=16 into 4 groups of  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1701-1](../sources/experiences/exp-a-kd-20260519-1701-1.md) | Replace 256-bin histogram with 2048-bin (11-bit half-precision binning) and use  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1701-2](../sources/experiences/exp-a-kd-20260519-1701-2.md) | Introduce float4 vectorized loads via PTX inline asm with cache-global hint (ld. | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1702-1](../sources/experiences/exp-a-kd-20260519-1702-1.md) | Replace compile-time fixed 32KB shared memory with dynamic shared memory sized a | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1703-1](../sources/experiences/exp-a-kd-20260519-1703-1.md) | Replace scalar float loads with vectorized float4 loads using PTX inline asm ld. | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1837-1](../sources/experiences/exp-a-kd-20260519-1837-1.md) | Fuse global_scale into the topk weight at load time by pre-multiplying global_sc | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2323-1](../sources/experiences/exp-a-kd-20260519-2323-1.md) | The after kernel introduces offset-based indexing (sorted_token_ids_offset + it, | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2328-1](../sources/experiences/exp-a-kd-20260519-2328-1.md) | Replace atomicAdd with if (masks[i]) conditional direct assignment to avoid atom | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2381-1](../sources/experiences/exp-a-kd-20260519-2381-1.md) | Replace the 3-phase single-block count-prefix-sum-scatter algorithm with a multi | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2382-1](../sources/experiences/exp-a-kd-20260519-2382-1.md) | Replace the single-block 3-phase shared-memory kernel with a multi-block (8 bloc | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-2384-1](../sources/experiences/exp-a-kd-20260519-2384-1.md) | Replace per-thread contiguous sharding with stride-based iteration (tid, stride= | analysis | sm90 | cuda-cpp |
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
| [exp-i-kd-20260518-0005](../sources/experiences/exp-i-kd-20260518-0005.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0061](../sources/experiences/exp-i-kd-20260518-0061.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-o-20260324-175225-a14b261c](../sources/experiences/exp-o-20260324-175225-a14b261c.md) | fp32_top_k_sampling_llama3_8b_k8 | optimization | sm90 | cuda-cpp |
| [exp-o-20260324-180317-1365822b](../sources/experiences/exp-o-20260324-180317-1365822b.md) | fp32_top_k_sampling_llama3_8b_k8 | optimization | sm90 | cuda-cpp |
| [exp-o-20260325-073648-c4965aad](../sources/experiences/exp-o-20260325-073648-c4965aad.md) | fp32_top_k_sampling_qwen2_5_7b_k8_ne0160 | optimization | sm90 | cuda-cpp |
| [exp-o-20260325-074027-38b02cab](../sources/experiences/exp-o-20260325-074027-38b02cab.md) | fp32_top_k_sampling_qwen2_5_7b_k8_ne0160 | optimization | sm90 | cuda-cpp |
| [exp-o-20260325-082251-2f09a524](../sources/experiences/exp-o-20260325-082251-2f09a524.md) | fp32_top_k_sampling_qwen2_5_7b_k8_ne0160 | optimization | sm90 | cuda-cpp |
| [exp-o-20260325-100754-825e6ce7](../sources/experiences/exp-o-20260325-100754-825e6ce7.md) | fp32_top_k_sampling_qwen2_5_7b_k6_ne0256 | optimization | sm90 | cuda-cpp |
| [exp-o-20260325-101903-3a2ff77a](../sources/experiences/exp-o-20260325-101903-3a2ff77a.md) | fp32_top_k_sampling_qwen2_5_7b_k6_ne0256 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0196](../sources/experiences/exp-o-kd-20260518-0196.md) | bs4_len4096 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0197](../sources/experiences/exp-o-kd-20260518-0197.md) | bs4_len16384 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0202](../sources/experiences/exp-o-kd-20260518-0202.md) | prediv_sorted_ids | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0203](../sources/experiences/exp-o-kd-20260518-0203.md) | bf16_m2048_topk4_k7168 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0243](../sources/experiences/exp-o-kd-20260518-0243.md) | large_2048rows_topk6 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0253](../sources/experiences/exp-o-kd-20260518-0253.md) | smem_layout_64_1024 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0281](../sources/experiences/exp-o-kd-20260518-0281.md) | float_topk8_8192rows | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0282](../sources/experiences/exp-o-kd-20260518-0282.md) | medium_batch_512_32exp | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0294](../sources/experiences/exp-o-kd-20260518-0294.md) | batched_output | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0297](../sources/experiences/exp-o-kd-20260518-0297.md) | float_64exp_k8 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0303](../sources/experiences/exp-o-kd-20260518-0303.md) | fp16_topk4_r4096 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0337](../sources/experiences/exp-o-kd-20260518-0337.md) | large_64k | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0340](../sources/experiences/exp-o-kd-20260518-0340.md) | topk7_1024rows | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0405](../sources/experiences/exp-o-kd-20260518-0405.md) | experts_192 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0429](../sources/experiences/exp-o-kd-20260518-0429.md) | float_topk2_d2048 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0430](../sources/experiences/exp-o-kd-20260518-0430.md) | float_topk4_d2048 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0438](../sources/experiences/exp-o-kd-20260518-0438.md) | experts_256_topk8 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0447](../sources/experiences/exp-o-kd-20260518-0447.md) | clone_always_large | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0479](../sources/experiences/exp-o-kd-20260518-0479.md) | large_vocab | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0480](../sources/experiences/exp-o-kd-20260518-0480.md) | shortcut_only | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0481](../sources/experiences/exp-o-kd-20260518-0481.md) | topk_sort | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0505](../sources/experiences/exp-o-kd-20260518-0505.md) | small_8experts | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0529](../sources/experiences/exp-o-kd-20260518-0529.md) | seq16k | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0530](../sources/experiences/exp-o-kd-20260518-0530.md) | seq8k | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0619](../sources/experiences/exp-o-kd-20260518-0619.md) | sort_64ep_2048tok | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0710](../sources/experiences/exp-o-kd-20260518-0710.md) | smem_occupancy | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0711](../sources/experiences/exp-o-kd-20260518-0711.md) | For example, with m_topk=8 and gridDim.x=100, only 8 blocks do real work while 9 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0724](../sources/experiences/exp-o-kd-20260518-0724.md) | Serializes writes from all threads in a block to the same address, and the subse | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0726](../sources/experiences/exp-o-kd-20260518-0726.md) | Y, which is not valid CUDA C++ (shared memory must be at kernel scope), and wrot | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0732](../sources/experiences/exp-o-kd-20260518-0732.md) | . Static __shared__ is also capped at 48KB by default; configurations requiring  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0744](../sources/experiences/exp-o-kd-20260518-0744.md) | D_scaling_factor was performed as a separate operation (likely a separate kernel | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0745](../sources/experiences/exp-o-kd-20260518-0745.md) | Ly, breaking memory coalescing on GPU. It also requires computing CEILDIV(numel, | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0754](../sources/experiences/exp-o-kd-20260518-0754.md) | _with_bias, and then read again by topk_with_k2. For DeepSeek models that apply  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0755](../sources/experiences/exp-o-kd-20260518-0755.md) | Also mixed the bounds check with the value read in a single expression, which co | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0759](../sources/experiences/exp-o-kd-20260518-0759.md) | Overhead (branch, counter update) and prevents the compiler from interleaving it | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0765](../sources/experiences/exp-o-kd-20260518-0765.md) | Cal and could produce incorrect top-k selections for extreme logit values. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0784](../sources/experiences/exp-o-kd-20260518-0784.md) | Oats per load makes THREADS_PER_ROW non-power-of-2, breaking the butterfly shuff | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0800](../sources/experiences/exp-o-kd-20260518-0800.md) | NdScanExpert. The sortAndScanExpert function's first parameter was typed as 'int | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0801](../sources/experiences/exp-o-kd-20260518-0801.md) | -device memcpy of the topk_ids tensor plus a GPU memory allocation, adding laten | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0803](../sources/experiences/exp-o-kd-20260518-0803.md) | Often well below 65535 (e.g., 8 top-k for DeepSeek-V3). The old layout placed to | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0804](../sources/experiences/exp-o-kd-20260518-0804.md) | And an extra kernel launch overhead. | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0813](../sources/experiences/exp-o-kd-20260518-0813.md) | He caller. This wasted 8KB of shared memory per block and forced the kernel to t | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0814](../sources/experiences/exp-o-kd-20260518-0814.md) | Sor and writes to the outLogits output, even though only the indices were needed | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0815](../sources/experiences/exp-o-kd-20260518-0815.md) | As unnecessary because the caller only needs the indices, not sorted logits, and | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0607-1](../sources/experiences/exp-o-kd-20260519-0607-1.md) | Fuse the normalize and scale operations into a single kernel that reads each ele | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0608-1](../sources/experiences/exp-o-kd-20260519-0608-1.md) | Fuse the routed_scaling_factor multiplication into the same unrolled loop that d | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0615-1](../sources/experiences/exp-o-kd-20260519-0615-1.md) | Fuse renormalization into the moeTopK kernel by accumulating the row sum as each | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0616-1](../sources/experiences/exp-o-kd-20260519-0616-1.md) | Fuse renormalization into the moeTopK kernel by accumulating row_sum_for_renorma | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0617-1](../sources/experiences/exp-o-kd-20260519-0617-1.md) | Fuse renormalization into the topk-gating-softmax kernel by accumulating the top | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0618-1](../sources/experiences/exp-o-kd-20260519-0618-1.md) | Fuse renormalization into the topkGatingSoftmax kernel by accumulating row_sum_f | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0619-1](../sources/experiences/exp-o-kd-20260519-0619-1.md) | Fuse renormalization directly into the moeTopK kernel by accumulating the sum of | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0620-1](../sources/experiences/exp-o-kd-20260519-0620-1.md) | Fuse renormalization into the topkGatingSoftmax kernel by accumulating row_sum_f | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0634-1](../sources/experiences/exp-o-kd-20260519-0634-1.md) | Replace serial global-memory scan with cp_async bulk load into shared memory fol | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0645-1](../sources/experiences/exp-o-kd-20260519-0645-1.md) | Fuse both kernels into a single topk_fused_ragged_kernel that allocates shared m | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0646-1](../sources/experiences/exp-o-kd-20260519-0646-1.md) | Fuse top-K selection and offset addition into a single kernel that writes interm | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0652-1](../sources/experiences/exp-o-kd-20260519-0652-1.md) | Pre-compute the integer division once during the shared memory loading phase int | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0654-1](../sources/experiences/exp-o-kd-20260519-0654-1.md) | Pre-compute sorted_id / top_k once during the block data load phase into a dedic | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0658-1](../sources/experiences/exp-o-kd-20260519-0658-1.md) | Replace the bulk AccessType<T> struct assignment with a #pragma unroll loop that | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0660-1](../sources/experiences/exp-o-kd-20260519-0660-1.md) | Reduce dynamic shared memory from 128KB to 32KB (kSmem = 8*1024*sizeof(uint32_t) | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0661-1](../sources/experiences/exp-o-kd-20260519-0661-1.md) | Reduce kSmem from 32*1024*sizeof(uint32_t) (128KB) to 8*1024*sizeof(uint32_t) (3 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0672-1](../sources/experiences/exp-o-kd-20260519-0672-1.md) | Fuse the conditional routed_scaling_factor multiplication directly into the exis | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0698-1](../sources/experiences/exp-o-kd-20260519-0698-1.md) | Pre-allocate the fixed-size temporary buffers (tokens_cnts and cumsum) once befo | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0700-1](../sources/experiences/exp-o-kd-20260519-0700-1.md) | Replace scalar int32 loads with int4 vector loads (128-bit transactions fetching | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0708-1](../sources/experiences/exp-o-kd-20260519-0708-1.md) | Replace per-warp subset scanning with direct one-thread-per-expert mapping where | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0709-1](../sources/experiences/exp-o-kd-20260519-0709-1.md) | Replace per-warp subset scanning with one-thread-per-expert direct mapping where | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0710-1](../sources/experiences/exp-o-kd-20260519-0710-1.md) | Replace per-warp strided scanning with one-thread-per-expert assignment where ea | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0711-1](../sources/experiences/exp-o-kd-20260519-0711-1.md) | Replace scalar stride loads with float4 vectorized loads via reinterpret_cast<fl | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0712-1](../sources/experiences/exp-o-kd-20260519-0712-1.md) | Replace scalar stride loads with float4 vectorized loads via reinterpret_cast, r | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0713-1](../sources/experiences/exp-o-kd-20260519-0713-1.md) | Map each thread to exactly one expert (tid == expert index) so each thread alrea | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0718-1](../sources/experiences/exp-o-kd-20260519-0718-1.md) | Remove the zero_buffer_kernel entirely because moe_align_block_size_kernel's ser | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0720-1](../sources/experiences/exp-o-kd-20260519-0720-1.md) | Remove the redundant cumsum_buffer.zero_() call entirely since align_kernel expl | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0728-1](../sources/experiences/exp-o-kd-20260519-0728-1.md) | Replace static __shared__ declarations with dynamic extern __shared__ plus an ex | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0729-1](../sources/experiences/exp-o-kd-20260519-0729-1.md) | Replace all static __shared__ declarations with a single extern __shared__ char  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0747-1](../sources/experiences/exp-o-kd-20260519-0747-1.md) | Extract the sorting loop into a dedicated moe_token_sort_kernel launched across  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0748-1](../sources/experiences/exp-o-kd-20260519-0748-1.md) | Extract the sorting phase into a separate multi-block kernel (moe_token_sort_ker | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0749-1](../sources/experiences/exp-o-kd-20260519-0749-1.md) | Extract the sorting loop into a separate moe_token_sort_kernel that uses the glo | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0767-1](../sources/experiences/exp-o-kd-20260519-0767-1.md) | Fuse the rescale (divide by sum) and scale (multiply by factor) operations into  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0768-1](../sources/experiences/exp-o-kd-20260519-0768-1.md) | Fuse rescale (divide by sum) and scale (multiply by factor) into a single kernel | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0769-1](../sources/experiences/exp-o-kd-20260519-0769-1.md) | Fuse the routed_scaling_factor multiplication into the existing rescale loop by  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0771-1](../sources/experiences/exp-o-kd-20260519-0771-1.md) | Consolidate two kernels into one single-warp kernel (32 threads) using per-threa | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0773-1](../sources/experiences/exp-o-kd-20260519-0773-1.md) | Fuse the two kernels into a single kernel launched with only 32 threads (one war | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1085-1](../sources/experiences/exp-o-kd-20260519-1085-1.md) | Replace KernelParamsDynamic (runtime int fields) with a templated KernelParams<V | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1086-1](../sources/experiences/exp-o-kd-20260519-1086-1.md) | Replace KernelParamsDynamic (runtime mutable int fields) with a templated Kernel | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1088-1](../sources/experiences/exp-o-kd-20260519-1088-1.md) | Stage topk results in shared memory arrays (smem_score/smem_idx) instead of writ | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1088-2](../sources/experiences/exp-o-kd-20260519-1088-2.md) | Replace the single-thread serial rescale loop with a warp-stride batched write ( | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1092-1](../sources/experiences/exp-o-kd-20260519-1092-1.md) | Fuse sigmoid and TopK into a single kernel (topkGatingSigmoid_kernel) that appli | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1092-2](../sources/experiences/exp-o-kd-20260519-1092-2.md) | Use AlignedArray<float,4> (16-byte) vector loads with interleaved addressing so  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1092-3](../sources/experiences/exp-o-kd-20260519-1092-3.md) | Replace CUB BlockReduce with a __shfl_xor_sync butterfly XOR reduction scoped to | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1093-1](../sources/experiences/exp-o-kd-20260519-1093-1.md) | Fuse sigmoid into the TopK kernel using vectorized 128-bit AlignedArray loads (4 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1093-2](../sources/experiences/exp-o-kd-20260519-1093-2.md) | Replace CUB BlockReduce TopK with register-resident local argmax followed by war | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1100-1](../sources/experiences/exp-o-kd-20260519-1100-1.md) | Replace scalar per-element load/accumulate/store with flashinfer::vec_t vectoriz | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1867-1](../sources/experiences/exp-o-kd-20260519-1867-1.md) | Fuse sigmoid_accurate() and per-group bias addition directly into the top-2 sele | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1868-1](../sources/experiences/exp-o-kd-20260519-1868-1.md) | Fuse sigmoid+bias computation inline within the top-2 selection loop of a single | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1869-1](../sources/experiences/exp-o-kd-20260519-1869-1.md) | Fuse sigmoid+bias computation directly into the candidates kernel: each thread r | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1870-1](../sources/experiences/exp-o-kd-20260519-1870-1.md) | Fuse the two separate kernels into a single candidates_after_kernel that reads r | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1871-1](../sources/experiences/exp-o-kd-20260519-1871-1.md) | Fuse sigmoid activation (via apply_sigmoid()) and per-element bias addition dire | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1872-1](../sources/experiences/exp-o-kd-20260519-1872-1.md) | Replace the single scores_with_bias buffer read with inline fused computation: r | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1886-1](../sources/experiences/exp-o-kd-20260519-1886-1.md) | Add a compile-time NGroup template parameter to the kernel; when NGroup > 0, wra | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1902-1](../sources/experiences/exp-o-kd-20260519-1902-1.md) | Replace single-pass 512-bin approach with progressive multi-step refinement usin | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1903-1](../sources/experiences/exp-o-kd-20260519-1903-1.md) | Replace the single-pass 512-bin histogram with a progressive 4-step refinement:  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1904-1](../sources/experiences/exp-o-kd-20260519-1904-1.md) | Replace single-pass 512-bin histogram with 4-step progressive refinement using 2 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1922-1](../sources/experiences/exp-o-kd-20260519-1922-1.md) | Decouple the token sort into a dedicated multi-block kernel (128 blocks × 256 th | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1923-1](../sources/experiences/exp-o-kd-20260519-1923-1.md) | Extract the token-sorting loop into a separate sgl_moe_token_sort_kernel launche | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1990-1](../sources/experiences/exp-o-kd-20260519-1990-1.md) | Fuse softmax and topk into a single topkGatingSoftmax kernel that keeps all inte | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1990-2](../sources/experiences/exp-o-kd-20260519-1990-2.md) | Use 8-byte vector loads (BYTES_PER_LDG=8, ELTS_PER_LDG=2) so that THREADS_PER_RO | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1991-1](../sources/experiences/exp-o-kd-20260519-1991-1.md) | Remove the power-of-2 static_asserts on VPT and NUM_EXPERTS, and promote MAX_BYT | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2019-1](../sources/experiences/exp-o-kd-20260519-2019-1.md) | Launch with max(num_experts, WARP_SIZE)=32 threads to fill the entire warp, resi | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2020-1](../sources/experiences/exp-o-kd-20260519-2020-1.md) | Increase block thread count from num_experts (8) to max(num_experts, WARP_SIZE=3 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2048-1](../sources/experiences/exp-o-kd-20260519-2048-1.md) | Propagate const-correctness through the call chain: change CubKeyValueSorter::ru | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2049-1](../sources/experiences/exp-o-kd-20260519-2049-1.md) | Change sortAndScanExpert and CubKeyValueSorter::run to accept const int* for the | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2050-1](../sources/experiences/exp-o-kd-20260519-2050-1.md) | Change the first parameter from int* to const int* so the caller can pass topk_i | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2051-1](../sources/experiences/exp-o-kd-20260519-2051-1.md) | Replace the unconditional cudaMalloc + cudaMemcpy clone with a shallow pointer a | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2052-1](../sources/experiences/exp-o-kd-20260519-2052-1.md) | Replace the unconditional clone with a lazy clone pattern: initialize topk_ids_f | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2055-1](../sources/experiences/exp-o-kd-20260519-2055-1.md) | Replace int32_t with uint16_t for the token_cnts working array and reorganize sh | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2059-1](../sources/experiences/exp-o-kd-20260519-2059-1.md) | Fuse topk selection and renormalization into a single kernel (fusedTopkRenormKer | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2060-1](../sources/experiences/exp-o-kd-20260519-2060-1.md) | Fuse renormalization into the topk kernel by accumulating selected_sum in shared | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2063-1](../sources/experiences/exp-o-kd-20260519-2063-1.md) | Fuse topk selection and renormalization into a single kernel by accumulating sel | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2064-1](../sources/experiences/exp-o-kd-20260519-2064-1.md) | Fuse renormalization into the topk kernel by having thread 0 accumulate selected | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2065-1](../sources/experiences/exp-o-kd-20260519-2065-1.md) | Templatize the kernel on InputType (float/__nv_bfloat16/__half) and fuse vectori | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2066-1](../sources/experiences/exp-o-kd-20260519-2066-1.md) | Add a renormalize boolean parameter to the topkGatingSoftmax kernel; when enable | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2068-1](../sources/experiences/exp-o-kd-20260519-2068-1.md) | Fuse renormalize into moeTopK by adding a renormalize boolean parameter, accumul | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2086-1](../sources/experiences/exp-o-kd-20260519-2086-1.md) | Replace per-thread O(E) linear scan with warp-cooperative search where all 32 la | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2087-1](../sources/experiences/exp-o-kd-20260519-2087-1.md) | Replace per-thread linear scan with warp-cooperative binary-style search: each w | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2092-1](../sources/experiences/exp-o-kd-20260519-2092-1.md) | Remove the outLogits output parameter entirely along with the smemLogits shared  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2093-1](../sources/experiences/exp-o-kd-20260519-2093-1.md) | Remove the smemLogits shared memory buffer entirely and skip all logit writes to | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2093-2](../sources/experiences/exp-o-kd-20260519-2093-2.md) | Remove the TopKSort (cub::BlockRadixSort) and its temp storage entirely, replaci | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2094-1](../sources/experiences/exp-o-kd-20260519-2094-1.md) | Remove the outLogits output buffer entirely from the kernel signature, eliminate | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2095-1](../sources/experiences/exp-o-kd-20260519-2095-1.md) | Eliminate the TopKSort radix sort stage entirely and write smemIndices directly  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2096-1](../sources/experiences/exp-o-kd-20260519-2096-1.md) | Remove the outLogits output parameter and smemLogits[kTopK] shared memory buffer | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2097-1](../sources/experiences/exp-o-kd-20260519-2097-1.md) | Remove all outLogits writes and the corresponding logits reads in both loops of  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2098-1](../sources/experiences/exp-o-kd-20260519-2098-1.md) | Remove the entire TopKSort stage including register arrays, smemLogits loads, cu | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2117-1](../sources/experiences/exp-o-kd-20260519-2117-1.md) | Split 320 total threads into 256 fill_threads and 64 working_threads launched in | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2119-1](../sources/experiences/exp-o-kd-20260519-2119-1.md) | Reserve a compile-time fill_threads subgroup (256 threads) for initialization wh | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2124-1](../sources/experiences/exp-o-kd-20260519-2124-1.md) | Replace O(N*K) iterative selection with WarpSelect incremental top-k: read input | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2132-1](../sources/experiences/exp-o-kd-20260519-2132-1.md) | Accumulate match counts in a register-local variable across all loop iterations, | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2133-1](../sources/experiences/exp-o-kd-20260519-2133-1.md) | Replace CUB radix sort and post-sort permutation building with an atomicAdd-base | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2134-1](../sources/experiences/exp-o-kd-20260519-2134-1.md) | Replace the CUB radix sort + build_perms two-phase pipeline with a single-pass a | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2139-1](../sources/experiences/exp-o-kd-20260519-2139-1.md) | Replace the global-memory per-thread counter matrix with shared memory shared_co | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2139-2](../sources/experiences/exp-o-kd-20260519-2139-2.md) | Replace the per-thread counter + cumsum lookup with a single atomicAdd on local_ | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2142-1](../sources/experiences/exp-o-kd-20260519-2142-1.md) | Replace per-thread counter + cumsum lookup with atomicAdd on local_offsets[exper | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2167-1](../sources/experiences/exp-o-kd-20260519-2167-1.md) | Replace full O(N log N) CUB radix sort with a custom multi-pass radix selection  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2168-1](../sources/experiences/exp-o-kd-20260519-2168-1.md) | Replace full O(N log N) sort with multi-pass radix selection: build a coarse 256 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2169-1](../sources/experiences/exp-o-kd-20260519-2169-1.md) | Fuse the next-pass histogram construction directly into the threshold-bin buffer | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2170-1](../sources/experiences/exp-o-kd-20260519-2170-1.md) | Reduce shared memory allocation from 128KB to 32KB by changing kSmem from 32*102 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2175-1](../sources/experiences/exp-o-kd-20260519-2175-1.md) | Eliminate compute_expert_offsets and compute_arg_sorts kernels entirely, reducin | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2176-1](../sources/experiences/exp-o-kd-20260519-2176-1.md) | Eliminate 2 out of 3 kernel launches by skipping compute_expert_offsets and comp | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2180-1](../sources/experiences/exp-o-kd-20260519-2180-1.md) | Pack the float value and its int32 index into a single uint64_t word using cub:: | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2181-1](../sources/experiences/exp-o-kd-20260519-2181-1.md) | Pack half-precision value (16 bits) and index (16 bits) into a single uint32_t u | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2293-1](../sources/experiences/exp-o-kd-20260519-2293-1.md) | Replace the single-block prefix-sum architecture with a multi-block kernel where | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2294-1](../sources/experiences/exp-o-kd-20260519-2294-1.md) | Replace the 3-phase shared-memory single-block kernel (64 threads) with a single | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2296-1](../sources/experiences/exp-o-kd-20260519-2296-1.md) | Decouple sorting into a dedicated multi-block kernel (up to 65535 blocks x 256 t | optimization | sm90 | cuda-cpp |
| [exp-r-20260327-182901-8a499e71](../sources/experiences/exp-r-20260327-182901-8a499e71.md) | fp32_top_k_sampling_qwen2_5_7b_k6_ne0256 | repair | sm90 | cuda-cpp |

## transpose

| ID | Title | Type | Architectures | Languages |
|----|-------|------|--------------|-----------|
| [exp-a-kd-20260518-0333](../sources/experiences/exp-a-kd-20260518-0333.md) | sgemm_512x512x512 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0334](../sources/experiences/exp-a-kd-20260518-0334.md) | sgemm_512x512x512 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0336](../sources/experiences/exp-a-kd-20260518-0336.md) | sgemm_8x4_m512 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0362](../sources/experiences/exp-a-kd-20260518-0362.md) | int1024 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0363](../sources/experiences/exp-a-kd-20260518-0363.md) | int1024 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0436](../sources/experiences/exp-a-kd-20260518-0436.md) | half_32hd_1024t | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0928](../sources/experiences/exp-a-kd-20260518-0928.md) | m65_non_aligned | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0967](../sources/experiences/exp-a-kd-20260518-0967.md) | row_shuffle_fp16_4096cols | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-0968](../sources/experiences/exp-a-kd-20260518-0968.md) | row_shuffle_fp16_7168cols | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1342](../sources/experiences/exp-a-kd-20260518-1342.md) | m32_n1280_k4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1346](../sources/experiences/exp-a-kd-20260518-1346.md) | small_m_decode | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1347](../sources/experiences/exp-a-kd-20260518-1347.md) | tiny_m_decode | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-1350](../sources/experiences/exp-a-kd-20260518-1350.md) | swap_caller | analysis | sm90 | cuda-cpp, cute-dsl |
| [exp-a-kd-20260518-1458](../sources/experiences/exp-a-kd-20260518-1458.md) | coalesced_atomic | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1485](../sources/experiences/exp-a-kd-20260518-1485.md) | block_fp8_e2e_4096 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260518-1486](../sources/experiences/exp-a-kd-20260518-1486.md) | block_fp8_e2e_8192 | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0173-1](../sources/experiences/exp-a-kd-20260519-0173-1.md) | Replace all 12 asm volatile prmt.b32 calls with the __byte_perm CUDA intrinsic,  | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0175-1](../sources/experiences/exp-a-kd-20260519-0175-1.md) | Replace the four __shfl_sync warp-shuffle instructions plus four scalar shared-m | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0594-1](../sources/experiences/exp-a-kd-20260519-0594-1.md) | Pad the shared memory array from s_data[32][32] to s_data[32][33], adding one el | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-0595-1](../sources/experiences/exp-a-kd-20260519-0595-1.md) | Replace padding-based bank conflict avoidance (32x33 array) with XOR swizzle (th | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1284-1](../sources/experiences/exp-a-kd-20260519-1284-1.md) | The after code switches from GPTQ's two-step column-prefill-then-extract pattern | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1419-1](../sources/experiences/exp-a-kd-20260519-1419-1.md) | Decouple input and output row strides by introducing an explicit lda (leading di | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1420-1](../sources/experiences/exp-a-kd-20260519-1420-1.md) | Accept lda as a separate kernel parameter and compute independent strides — inpu | analysis | sm90 | cuda-cpp |
| [exp-a-kd-20260519-1764-1](../sources/experiences/exp-a-kd-20260519-1764-1.md) | Replace hardcoded stride constants with explicit int64_t stride parameters (inpu | analysis | sm90 | cuda-cpp |
| [exp-i-kd-20260518-0014](../sources/experiences/exp-i-kd-20260518-0014.md) | Implement kernel following the CUTLASS_device_function interface pattern with co | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260518-0053](../sources/experiences/exp-i-kd-20260518-0053.md) | Implement kernel following the CUTLASS_kernel_template interface pattern with co | implementation | sm90 | cuda-cpp |
| [exp-i-kd-20260519-2398-1](../sources/experiences/exp-i-kd-20260519-2398-1.md) | Implement a grid-stride loop where each thread strides by blockDim.x*gridDim.x t | implementation | sm90 | cuda-cpp, cute-dsl |
| [exp-i-kd-20260519-2437-1](../sources/experiences/exp-i-kd-20260519-2437-1.md) | Use reinterpret_cast<uint32_t*> to load paired uint16_t values in a single 32-bi | implementation | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0138](../sources/experiences/exp-o-kd-20260518-0138.md) | sgemm_8x4_m1024 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0139](../sources/experiences/exp-o-kd-20260518-0139.md) | sgemm_8x4_loop_m512 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0141](../sources/experiences/exp-o-kd-20260518-0141.md) | sgemm_8x8_m512 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0144](../sources/experiences/exp-o-kd-20260518-0144.md) | sgemm_8x8_m1024 | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0424](../sources/experiences/exp-o-kd-20260518-0424.md) | noncontiguous_64tok | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260518-0795](../sources/experiences/exp-o-kd-20260518-0795.md) | Ing wrong permutation results because the input row pointer advancement skipped  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0290-1](../sources/experiences/exp-o-kd-20260519-0290-1.md) | Replace the four warp-shuffle instructions and four scalar shared-memory stores  | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-0454-1](../sources/experiences/exp-o-kd-20260519-0454-1.md) | Pad the shared memory array from s_data[32][32] to s_data[32][33], adding one el | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-1962-1](../sources/experiences/exp-o-kd-20260519-1962-1.md) | Eliminate the b1_vals/b2_vals intermediate local arrays by computing packed indi | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2040-1](../sources/experiences/exp-o-kd-20260519-2040-1.md) | Add an explicit lda (leading dimension of A) parameter and decouple input row st | optimization | sm90 | cuda-cpp |
| [exp-o-kd-20260519-2286-1](../sources/experiences/exp-o-kd-20260519-2286-1.md) | Eliminate the unnecessary transpose kernel entirely by consuming the scale tenso | optimization | sm90 | cuda-cpp |

