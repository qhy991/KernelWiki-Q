#!/usr/bin/env python3
"""Convert KernelOwl experience data to KernelWiki source-experience pages."""

import argparse
import json
import re
import sys
import yaml
from datetime import datetime
from pathlib import Path

KERNEL_TYPE_MAP = {
    "gemm": ["gemm"], "GEMM": ["gemm"], "MatMul": ["gemm"],
    "Attention": ["attention"], "attention": ["attention"],
    "FlashAttention": ["attention", "flash-attention"],
    "flash_attention": ["attention", "flash-attention"],
    "gqa": ["attention"],
    "TopK": ["topk"], "topk": ["topk"],
    "LayerNorm": ["layer-norm"], "layernorm": ["layer-norm"],
    "Softmax": ["softmax"], "softmax": ["softmax"],
    "Reduction": ["reduction"], "reduction": ["reduction"],
    "Linear": ["linear"], "linear": ["linear"],
    "ReLU": ["relu"], "relu": ["relu"],
    "RMSNorm": ["rmsnorm"], "rmsnorm": ["rmsnorm"],
    "Conv2d": ["conv2d"], "conv2d": ["conv2d"],
}

IMPL_FAMILY_MAP = {
    "cutlass": ["cuda-cpp", "cute-dsl"],
    "custom_cuda": ["cuda-cpp"],
    "custom_cuda_wmma": ["cuda-cpp"],
    "cublas": ["cuda-cpp"],
    "cublaslt": ["cuda-cpp"],
    "triton": ["triton"],
    "pytorch": ["python"],
    "unknown": ["cuda-cpp"],
}

TECHNIQUE_KEYWORDS = {
    "warp-specialization": ["warp-spec", "warp_specialization"],
    "shared-memory-optimization": ["smem", "shared_memory"],
    "pipeline-stages": ["pipeline", "double_buffer"],
    "tile-scheduling": ["tile", "cta_tile"],
    "register-reuse": ["register"],
    "fine-grained-quantization": ["quantiz", "int8", "fp8"],
    "epilogue-fusion": ["epilogue", "fusion"],
    "vectorized-loads": ["vectoriz"],
    "swizzling": ["swizzle"],
}



def sanitize_id(raw_id):
    """Convert source ID to KernelWiki-compatible exp- prefixed ID."""
    cleaned = raw_id.removesuffix(".json")
    if cleaned.startswith("exp_"):
        return "exp-" + cleaned[4:].replace("_", "-")
    return "exp-" + re.sub(r'[^a-z0-9-]', '-', cleaned.lower()).strip('-')


def infer_architecture(entry):
    """Infer architecture from experience data. Default to sm90."""
    text = json.dumps(entry).lower()
    if "blackwell" in text or "sm100" in text or "sm_100" in text:
        return ["sm100"]
    if "sm120" in text or "sm_120" in text:
        return ["sm120"]
    return ["sm90"]


def map_kernel_types(kernel_type):
    """Map free-text kernel_type to controlled vocabulary."""
    if not kernel_type:
        return []
    return KERNEL_TYPE_MAP.get(kernel_type, [])


def map_languages(impl_family):
    """Map impl_family to language tags."""
    if not impl_family or impl_family == "None":
        return ["cuda-cpp"]
    return IMPL_FAMILY_MAP.get(impl_family, ["cuda-cpp"])


def map_techniques(search_tags):
    """Map search_tags to technique tags via keyword matching."""
    if not search_tags:
        return []
    tags_lower = " ".join(str(t).lower() for t in search_tags)
    techniques = []
    for technique, keywords in TECHNIQUE_KEYWORDS.items():
        if any(kw in tags_lower for kw in keywords):
            techniques.append(technique)
    return techniques


def infer_confidence(entry):
    """Infer confidence level from entry data."""
    review = entry.get("review_status", "")
    outcome = entry.get("outcome", {})
    has_metrics = bool(outcome.get("result", {}).get("metrics"))
    if review == "published" and has_metrics:
        return "source-reported"
    if review == "published":
        return "inferred"
    return "experimental"


def infer_reproducibility(entry):
    """Infer reproducibility level from entry data."""
    solution = entry.get("solution", {})
    if solution.get("correct_approach") or solution.get("code_before") or solution.get("code_after"):
        return "snippet"
    if solution.get("approach") or solution.get("fix"):
        return "concept"
    return "concept"


def build_tags(kernel_types, techniques, languages):
    """Build the unified tags list from kernel_types + techniques."""
    tags = list(dict.fromkeys(kernel_types + techniques))
    return tags


def build_body(entry):
    """Build Markdown body from experience entry."""
    sections = []

    context = entry.get("context", {})
    summary = context.get("summary") or context.get("task_name", "")
    if summary:
        sections.append(summary)
        sections.append("")

    challenge = entry.get("challenge", {})
    problem = challenge.get("problem", "")
    if problem:
        sections.append("## Challenge")
        sections.append("")
        sections.append(problem)
        sections.append("")

    symptoms = challenge.get("symptoms", [])
    if symptoms:
        sections.append("### Symptoms")
        sections.append("")
        for s in symptoms:
            sections.append(f"- `{s}`")
        sections.append("")

    solution = entry.get("solution", {})
    approach = solution.get("approach") or solution.get("fix", "")
    if approach:
        sections.append("## Solution")
        sections.append("")
        sections.append(approach)
        sections.append("")

    details = solution.get("details", "")
    if details:
        sections.append(details)
        sections.append("")

    correct_approach = solution.get("correct_approach", "")
    if correct_approach:
        sections.append("### Implementation")
        sections.append("")
        sections.append("```cuda")
        sections.append(correct_approach)
        sections.append("```")
        sections.append("")

    outcome = entry.get("outcome", {})
    result = outcome.get("result", {})
    metrics = result.get("metrics", {})
    if metrics:
        sections.append("## Results")
        sections.append("")
        for k, v in metrics.items():
            sections.append(f"- **{k}**: {v}")
        sections.append("")

    lessons = entry.get("lessons_learned", [])
    if lessons:
        sections.append("## Key Lessons")
        sections.append("")
        for lesson in lessons:
            sections.append(f"- {lesson}")
        sections.append("")

    return "\n".join(sections)


def should_skip(entry):
    """Return (skip, reason) tuple."""
    ctx = entry.get("context", {})
    backend = ctx.get("backend", "")

    if backend.lower() in ("metal",):
        return True, "metal backend"

    valid_backends = {"cuda"}
    if backend.lower() not in valid_backends:
        return True, f"non-cuda backend: {backend}"

    quality = entry.get("quality_flag", "")
    if quality == "low":
        return True, "low quality"

    kernel_type = ctx.get("kernel_type") or ""
    if not kernel_type or kernel_type.lower() == "unknown":
        return True, "unknown/empty kernel type"

    lessons = entry.get("lessons_learned", [])
    if not lessons:
        return True, "no lessons learned"

    return False, ""


def convert_entry(entry):
    """Convert a single experience entry to KernelWiki page dict."""
    skip, reason = should_skip(entry)
    if skip:
        return None, reason

    ctx = entry.get("context", {})
    raw_id = entry.get("id", "")
    wiki_id = sanitize_id(raw_id)

    kernel_type = ctx.get("kernel_type", "")
    impl_family = ctx.get("impl_family", "")

    kernel_types = map_kernel_types(kernel_type)
    if not kernel_types:
        return None, f"unmappable kernel_type: {kernel_type}"

    languages = map_languages(impl_family)
    techniques = map_techniques(entry.get("search_tags", []))
    architectures = infer_architecture(entry)
    confidence = infer_confidence(entry)
    reproducibility = infer_reproducibility(entry)
    tags = build_tags(kernel_types, techniques, languages)

    title = ctx.get("task_name") or ctx.get("summary", wiki_id)

    timestamp = entry.get("timestamp", "")
    if timestamp:
        try:
            dt = datetime.fromisoformat(timestamp)
            captured_at = dt.strftime("%Y-%m-%d")
        except (ValueError, TypeError):
            captured_at = "2026-01-01"
    else:
        captured_at = "2026-01-01"

    frontmatter = {
        "id": wiki_id,
        "title": title,
        "experience_type": entry.get("experience_type", "optimization"),
        "source_category": "agent-experiment",
        "architectures": architectures,
        "tags": tags,
        "kernel_types": kernel_types,
        "languages": languages,
        "captured_at": captured_at,
        "confidence": confidence,
        "reproducibility": reproducibility,
    }

    if techniques:
        frontmatter["techniques"] = techniques
    if impl_family and impl_family not in ("unknown", "None", None):
        frontmatter["impl_family"] = impl_family

    outcome = entry.get("outcome", {})
    result = outcome.get("result", {})
    metrics = result.get("metrics", {})
    if metrics:
        speedup_str = next((str(v) for k, v in metrics.items() if "speedup" in k.lower()), None)
        if speedup_str:
            frontmatter["speedup"] = speedup_str

    body = build_body(entry)
    return {"frontmatter": frontmatter, "body": body, "id": wiki_id}, None


def write_page(page_data, output_dir):
    """Write a single page to disk."""
    fm = page_data["frontmatter"]
    body = page_data["body"]
    page_id = page_data["id"]

    filename = f"{page_id}.md"
    filepath = output_dir / filename

    fm_yaml = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)

    content = f"---\n{fm_yaml}---\n\n{body}"
    filepath.write_text(content, encoding="utf-8")
    return filepath


def load_experiences_from_jsonl(jsonl_path, knowledge_root):
    """Load experience entries from a JSONL curated dataset file.
    Each line has a source_path pointing to the full JSON."""
    entries = []
    with open(jsonl_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            pointer = json.loads(line)
            source_path = pointer.get("source_path", "")
            if not source_path:
                continue
            full_path = knowledge_root / source_path
            if not full_path.exists():
                print(f"  WARNING: source not found: {full_path}")
                continue
            with open(full_path, encoding="utf-8") as sf:
                entries.append(json.load(sf))
    return entries


def load_experiences_from_dir(exp_dir):
    """Load experience entries directly from JSON files in a directory tree."""
    entries = []
    for json_file in sorted(exp_dir.rglob("*.json")):
        if json_file.name == "index.json":
            continue
        with open(json_file, encoding="utf-8") as f:
            entries.append(json.load(f))
    return entries


def main():
    parser = argparse.ArgumentParser(
        description="Convert KernelOwl experiences to KernelWiki pages"
    )
    parser.add_argument("--source", required=True,
                       help="Path to KernelOwl knowledge/ directory")
    parser.add_argument("--output", required=True,
                       help="Path to KernelWiki sources/experiences/ directory")
    parser.add_argument("--scope", choices=["p0", "p1", "all"], default="all",
                       help="Conversion scope: p0 (curated_datasets), p1 (library_experiences CUDA), all")
    parser.add_argument("--dry-run", action="store_true",
                       help="Show what would be converted without writing files")
    args = parser.parse_args()

    source_root = Path(args.source)
    output_dir = Path(args.output)

    if not source_root.exists():
        print(f"ERROR: source directory not found: {source_root}")
        sys.exit(1)

    if not args.dry_run:
        output_dir.mkdir(parents=True, exist_ok=True)

    existing_ids = set()
    if output_dir.exists():
        for md in output_dir.glob("*.md"):
            existing_ids.add(md.stem)

    entries = []
    if args.scope in ("p0", "all"):
        curated_dir = source_root / "curated_datasets"
        if curated_dir.exists():
            for jsonl_file in sorted(curated_dir.glob("*.jsonl")):
                if "handwritten_operator" in jsonl_file.name:
                    loaded = load_experiences_from_jsonl(jsonl_file, source_root)
                    print(f"Loaded {len(loaded)} entries from {jsonl_file.name}")
                    entries.extend(loaded)

    if args.scope in ("p1", "all"):
        lib_dir = source_root / "library_experiences"
        if lib_dir.exists():
            for subdir_name in ("optimization", "implementation", "repair"):
                subdir = lib_dir / subdir_name
                if subdir.exists():
                    loaded = load_experiences_from_dir(subdir)
                    print(f"Loaded {len(loaded)} entries from library_experiences/{subdir_name}/")
                    entries.extend(loaded)

    seen_ids = set()
    converted = 0
    skipped = 0
    skipped_reasons = {}
    duplicate = 0

    for entry in entries:
        page_data, reason = convert_entry(entry)
        if page_data is None:
            skipped += 1
            skipped_reasons[reason] = skipped_reasons.get(reason, 0) + 1
            continue

        wiki_id = page_data["id"]
        if wiki_id in seen_ids or wiki_id in existing_ids:
            duplicate += 1
            continue
        seen_ids.add(wiki_id)

        if args.dry_run:
            print(f"  Would write: {wiki_id}.md")
        else:
            filepath = write_page(page_data, output_dir)
            print(f"  Wrote: {filepath.name}")
        converted += 1

    print(f"\nSummary: {converted} converted, {skipped} skipped, {duplicate} duplicates")
    if skipped_reasons:
        print("Skip reasons:")
        for reason, count in sorted(skipped_reasons.items(), key=lambda x: -x[1]):
            print(f"  {reason}: {count}")


if __name__ == "__main__":
    main()
