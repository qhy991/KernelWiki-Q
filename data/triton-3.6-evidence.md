# Triton 3.6 Blackwell Evidence Memo

## Releases of Record
- 2026-01-21: Triton 3.6.0 (`v3.6.0`, release commit `7c56a5e`). Blackwell-relevant items in the official release notes include TMEM encoding/layout work (`#8136`, `#8148`, `#8202`), generic `tcgen05` load/store and copy lowering (`#8225`, `#8421`, `#8495`, `#8102`, `#8338`), `tcgen05.mma` generalization (`#8386`), initial 2CTA Gluon support (`#8644`, `#8653`), `reqnctapercluster` emission (`#8645`), warp-specialization end-to-end aref plumbing (`#8262`, `#7826`, `#8009`), and Gluon `tcgen05 mma scaled` support (`#8393`).
- No subsequent `3.6.x` patch release is visible on the official GitHub releases page as of 2026-04-27; the next older release shown there is 3.5.1 on 2025-11-12. If the wiki wants a machine-checked negative claim rather than a page inspection, mark this needs-verification.

## Lowering Surfaces
- Pathway: plain `tl.dot` / standard MMA without Blackwell-specific warp specialization or descriptor/TMA structure.
  Lowers to `tcgen05` / TMEM on SM100: needs-verification. Triton 3.6 clearly contains native Blackwell `tcgen05` + TMEM infrastructure, but the checked sources do not prove that arbitrary plain `tl.dot` kernels now automatically use that path.
  Introducing PRs/commits: needs-verification for this exact user-visible surface.
  Caveats: do not replace the old wiki sentence with the opposite blanket claim. The evidence supports “Triton 3.6 has native Blackwell lowering paths,” not “all Triton matmuls on SM100 are now TMEM-backed tcgen05 kernels.”

- Pathway: descriptor/TMA matmul with `tl.range(..., warp_specialize=True)` and `tl.dot`, as documented in the persistent matmul tutorial.
  Lowers to `tcgen05` / TMEM on SM100: yes for the Blackwell warp-specialized path; this is the strongest checked `tl.*`-surface evidence. The official tutorial says this warp-specialized mode “only works on Blackwell right now,” while the 3.6 release notes add the Blackwell TMEM/layout, `tcgen05`, and warp-specialization aref plumbing needed to make that path real on SM100.
  Introducing PRs/commits: warp-specialization lowering plumbing `#8262`, `#7826`, `#8009`, `#8123`, `#8534`, `#8451`, `#8651`; Blackwell TMEM / `tcgen05` backend work `#8136`, `#8148`, `#8202`, `#8386`, `#8421`, `#8495`, `#8102`, `#8338`, `#8225`.
  Caveats: the verified path is descriptor/TMA-oriented and warp-specialized, not generic. It is also Blackwell-targeted in the checked docs, and the tutorial evidence does not prove parity for every non-persistent or non-descriptor `tl.dot` kernel shape.

- Pathway: fused attention forward kernels using `warp_specialize=True` in the Triton tutorial path.
  Lowers to `tcgen05` / TMEM on SM100: likely yes on the Blackwell forward path, but some of this is inference from the shared warp-specialization/aref/TMEM lowering stack rather than an explicit “this emits `tcgen05.mma`” statement in the tutorial, so exact coverage should be treated as partially needs-verification.
  Introducing PRs/commits: same core Blackwell and warp-specialization lowering series as above, especially `#8262`, `#7826`, `#8009`, `#8136`, `#8148`, `#8202`, `#8386`, `#8421`, `#8495`, `#8102`, `#8338`.
  Caveats: the tutorial explicitly ties some forward-path behavior to Blackwell, including the FP8 non-transposed-`V` case. This is not evidence that all attention modes, backward paths, or production attention kernels are equally mature on SM100.

- Pathway: `tl.dot_scaled` / block-scaled matmul on Blackwell.
  Lowers to `tcgen05` / TMEM on SM100: yes for the supported hardware-accelerated Blackwell path. The official block-scaled matmul tutorial says these kernels are hardware-accelerated by fifth-generation Tensor Cores on compute capability 10, and the 3.6 dialect docs expose `ttng.tc_gen5_mma_scaled` with TMEM-token semantics plus `ttng.tmem_copy`.
  Introducing PRs/commits: Gluon NVIDIA `tcgen05 mma scaled` support `#8393`; frontend fixes around `dot_scaled` `#8564` and `#8658`; shared TMEM / `tcgen05` backend work `#8136`, `#8148`, `#8202`.
  Caveats: this path is format- and layout-constrained. The checked tutorial is centered on NVFP4 / MXFP formats and notes that mixed-precision extensions are still future work.

- Pathway: Gluon front-end `gl.warp_specialize`, `num_ctas`, and multi-CTA / 2CTA Blackwell lowering.
  Lowers to `tcgen05` / TMEM on SM100: yes. This is the most explicit Blackwell-native surface in the checked 3.6 materials: the release notes call out initial 2CTA support in Gluon, `num_ctas`, multi-CTA support, and `tcgen05 mma scaled` support, while the dialect docs expose TMEM allocation/copy and `tc_gen5_mma` / `tc_gen5_mma_scaled` ops directly.
  Introducing PRs/commits: Gluon API and multi-CTA work `#8527`, `#8468`, `#8587`, `#8602`, `#8644`; Blackwell backend 2CTA / cluster work `#8644`, `#8653`, `#8645`; Gluon NVIDIA `tcgen05 mma scaled` `#8393`.
  Caveats: the release notes describe this as initial support, so cluster-scope and 2CTA usage should still be treated as early-stage. This is also a Gluon-first story; it is stronger evidence for “Triton can target Blackwell natively” than for “classic `tl.dot` is universally first-class on SM100.”

## Caveats and Open Questions
- The old wiki claim “Triton compiler generates wgmma, not tcgen05” is no longer globally correct for Triton 3.6+, but the replacement should be qualified: native `tcgen05` + TMEM paths exist on SM100, especially through warp-specialized descriptor/TMA and Gluon flows.
- The old wiki claim “No TMEM: accumulators stay in registers” is also outdated as a blanket statement. The checked 3.6 dialect docs explicitly model TMEM allocation/copy/load/store and `tc_gen5_mma` / `tc_gen5_mma_scaled` ops with TMEM-token semantics.
- What remains weaker than CuTe-DSL / CUTLASS hand-written Blackwell kernels is production peak-performance coverage. In SGLang `pr-sglang-5390`, a CUTLASS `tcgen05_mla` backend reports about 27% higher throughput than the Triton baseline on Blackwell for MLA decode.
- Downstream routing decisions still show Triton is not the universal best path on Blackwell. In `pr-sglang-21595`, SGLang changes Blackwell datacenter multimodal attention default from `triton_attn` to `fa4`; in `pr-sglang-21914`, SGLang sets TRT-LLM kernels as the default for Blackwell.
- The clearest generally-available Blackwell story in checked sources is not “plain `tl.dot` everywhere,” but “warp-specialized descriptor/TMA kernels and Gluon multi-CTA/2CTA kernels.” Anything beyond that should be marked needs-verification until backed by PTX/IR or a downstream merged PR.
- A policy update from “narrow” toward “first-class” is justified, but only with qualifiers. Recommended interpretation: Triton 3.6+ is first-class for supported Blackwell-native lowering paths and for serious prototyping on SM100, but it is still not the default peak-performance answer for all compute-bound production kernels.
- Open question: find a downstream merged PR in `pytorch`, `vllm`, `sglang`, or `flashinfer` that explicitly depends on Triton 3.6+ and shows `ttng.tc_gen5_mma` / `tcgen05.*` emission for an SM100 Triton kernel. I could not verify that exact anchor from checked downstream sources, so this remains needs-verification.

## Evidence References

### Primary anchors

- `doc-triton-3.6-blackwell` — Triton 3.6 release notes / official tutorial and dialect-doc summary covering TMEM, `tcgen05`, `warp_specialize`, `num_ctas`, 2CTA mode, and `tcgen05 mma scaled` on Blackwell. (`source_category: official-doc`, file at `sources/docs/triton-3.6-blackwell.md`.)

The complete primary-anchor set comprises one official-doc anchor and one matmul-exercising downstream upstream-code anchor:
- `pr-sglang-22079` — primary downstream upstream-code anchor: a real Triton attention kernel doing actual `tl.dot(q, k)` / `tl.dot(p, v)` matmul on `architectures: [sm100, sm90]`, merged on `2026-04-03` (well after Triton 3.6.0 released `2026-01-21`). The kernel is the SGLang `extend_attention` Triton kernel for the Gemma4 NVFP4 attention path; tags include `attention`, `nvfp4`, `fp4`, `gemm`, `tcgen05`-relevant block-scaled matmul. Ships verbatim under `artifacts/prs/sglang/PR-22079/key-files/python/sglang/srt/layers/attention/triton_ops/extend_attention.py`. This is a genuine Triton matmul kernel exercising the post-3.6 Triton lowering on SM100, not a memory-rearrangement kernel. (`source_category: upstream-code`, `languages: [python, triton]`.)
- `pr-sglang-21019` — secondary downstream upstream-code anchor: `@triton.jit`-decorated kernel (`fused_qkvzba_split_reshape_cat_kernel` for Qwen3.5 GDN projection) landed for `architectures: [sm100]` on `2026-03-20`. This kernel is `tl.load`/`tl.store` only (memory rearrangement, no `tl.dot`), so it demonstrates "Triton on SM100 post-3.6" but not the matmul lowering surface. Retained as a secondary anchor.

### Caveat / ecosystem-readiness anchors

- `pr-sglang-5390` — downstream upstream-code anchor (caveat): CUTLASS `tcgen05_mla` backend outperforming the Triton MLA decode baseline by ~27% on Blackwell. Demonstrates that Triton's Blackwell coverage is not yet at peak parity with hand-written CUTLASS for compute-bound workloads. (`source_category: upstream-code`.)
- `pr-sglang-21595` — downstream upstream-code anchor (caveat): Blackwell multimodal attention default changed from `triton_attn` to FA4 in datacenter SKUs. Demonstrates that production routing decisions still favor non-Triton kernels for some Blackwell paths. (`source_category: upstream-code`.)
- `pr-pytorch-175826` — downstream upstream-code anchor (ecosystem-readiness): PyTorch inductor CI's B200 / SM100 lane moved to CUDA 13.0, reflecting the broader Blackwell toolchain maturation. (`source_category: upstream-code`.)

### Note on anchor scope

The plan's AC-1.1 positive test reads "At least one new sources/prs/<repo>/PR-<N>.md page demonstrates a kernel that lowers through the Triton 3.6 Blackwell path." `pr-sglang-22079` satisfies this: it is a Triton attention kernel performing actual `tl.dot` matmul on `architectures: [sm100, sm90]`, merged 2026-04-03 (well after the Triton 3.6.0 release date of 2026-01-21), in the NVFP4 (block-scaled) attention path. The kernel exercises the `tl.dot` lowering surface that the 3.6 release added Blackwell `tcgen05` infrastructure for, on the matmul path the plan called out (not a memory-rearrangement-only kernel).

The strongest possible demonstrations — explicit inspectable PTX showing `tcgen05.mma` emission, or kernels using `tl.dot_scaled` / `warp_specialize` with descriptor/TMA structure — were not found in any tracked-repo PR locally. They currently live in the upstream Triton tutorials. A future refresh round should backfill such an anchor if one becomes available in tracked downstream repos.

## Recommended wiki rewrite framing
- Triton 3.6 materially changes the Blackwell story.
- The old blanket claim that Triton on SM100 only emits WGMMA with register-resident accumulators is no longer correct.
- Triton 3.6 adds native Blackwell lowering infrastructure for `tcgen05` and TMEM, with the clearest documented path running through warp-specialized descriptor/TMA kernels and newer Gluon multi-CTA / 2CTA support.
- The important qualifier is that this is not yet proof that every plain `tl.dot` kernel on SM100 automatically becomes a TMEM-backed `tcgen05` kernel.
- Treat Triton 3.6+ as a first-class Blackwell language for supported warp-specialized matmul/attention building blocks and block-scaled GEMM.
- Keep CuTe-DSL / CUTLASS / FA4 / TRT-LLM as the expected leaders for many peak-performance production attention and decode kernels.
- Replace “no tcgen05 / no TMEM” with “native `tcgen05` + TMEM paths now exist, but coverage and performance leadership are workload-dependent.”
