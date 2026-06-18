#!/usr/bin/env python3
"""Export high-confidence operator recipes from KernelWiki-Q.

The default recipe set is intentionally conservative:
  - verified/source-reported wiki kernel pages
  - verified/source-reported source experience pages

Experimental and inferred source experiences are not mixed into the default
retrieval set. They are summarized as a candidate pool for later promotion.
"""

import argparse
import re
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
HIGH_CONFIDENCE = {"verified", "source-reported"}
LOW_CONFIDENCE = {"experimental", "inferred"}
MAX_SAMPLES_PER_GROUP = 25


def extract_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return {}
    return yaml.safe_load(match.group(1)) or {}


def as_list(value):
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def relpath(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def recipe_from_page(root: Path, path: Path, fm: dict, source_type: str) -> dict:
    page_id = fm["id"]
    evidence_source_ids = as_list(fm.get("sources"))
    recipe = {
        "recipe_id": f"recipe-{page_id}",
        "title": fm.get("title", page_id),
        "source_type": source_type,
        "source_path": relpath(root, path),
        "source_ids": [page_id],
        "confidence": fm.get("confidence", "source-reported"),
        "reproducibility": fm.get("reproducibility", "concept"),
        "architectures": as_list(fm.get("architectures")),
        "kernel_types": as_list(fm.get("kernel_types")),
        "languages": as_list(fm.get("languages")),
        "techniques": as_list(fm.get("techniques")),
        "hardware_features": as_list(fm.get("hardware_features")),
        "tags": as_list(fm.get("tags")),
    }
    if evidence_source_ids:
        recipe["evidence_source_ids"] = evidence_source_ids
    if fm.get("performance_claims"):
        recipe["performance_claims"] = fm["performance_claims"]
    if fm.get("related"):
        recipe["related"] = as_list(fm.get("related"))
    return recipe


def source_experience_paths(root: Path):
    return sorted((root / "sources" / "experiences").glob("*.md"))


def wiki_kernel_paths(root: Path):
    return sorted((root / "wiki" / "kernels").glob("*.md"))


def collect_candidate_pool(root: Path) -> dict:
    by_confidence = Counter()
    groups = defaultdict(list)

    for path in source_experience_paths(root):
        fm = extract_frontmatter(path)
        confidence = fm.get("confidence", "experimental")
        if confidence not in LOW_CONFIDENCE:
            continue
        source_id = fm.get("id")
        if not source_id:
            continue
        by_confidence[confidence] += 1
        kernel_types = as_list(fm.get("kernel_types")) or ["unknown"]
        for kernel_type in kernel_types:
            groups[(confidence, kernel_type)].append(source_id)

    group_rows = []
    for (confidence, kernel_type), source_ids in sorted(groups.items()):
        group_rows.append({
            "confidence": confidence,
            "kernel_type": kernel_type,
            "count": len(source_ids),
            "sample_source_ids": sorted(source_ids)[:MAX_SAMPLES_PER_GROUP],
        })

    return {
        "policy": (
            "experimental/inferred source experiences are candidates only; "
            "promote manually after source evidence review"
        ),
        "total": sum(by_confidence.values()),
        "by_confidence": dict(sorted(by_confidence.items())),
        "groups": group_rows,
    }


def collect_recipe_export(root: Path = ROOT) -> dict:
    root = Path(root)
    default_recipes = []

    for path in wiki_kernel_paths(root):
        fm = extract_frontmatter(path)
        if fm.get("confidence") in HIGH_CONFIDENCE:
            default_recipes.append(recipe_from_page(root, path, fm, "wiki-kernel"))

    for path in source_experience_paths(root):
        fm = extract_frontmatter(path)
        if fm.get("confidence") in HIGH_CONFIDENCE:
            default_recipes.append(recipe_from_page(root, path, fm, "source-experience"))

    default_recipes.sort(key=lambda row: row["recipe_id"])

    return {
        "schema_version": 1,
        "generated_by": "scripts/export_operator_recipes.py",
        "default_policy": (
            "Only verified/source-reported kernel pages and source experiences "
            "are exported to the default operator recipe set."
        ),
        "default_recipe_count": len(default_recipes),
        "default_recipes": default_recipes,
        "candidate_pool": collect_candidate_pool(root),
    }


def write_export(export: dict, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        yaml.safe_dump(export, sort_keys=False, allow_unicode=False),
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Export high-confidence operator recipes")
    parser.add_argument("--root", type=Path, default=ROOT, help="KernelWiki-Q repository root")
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "data" / "operator-recipes.yaml",
        help="Output YAML path",
    )
    args = parser.parse_args()

    export = collect_recipe_export(args.root)
    output = args.output
    if not output.is_absolute():
        output = args.root / output
    write_export(export, output)

    candidate_pool = export["candidate_pool"]
    print(
        f"Wrote {output}: default_recipes={export['default_recipe_count']}, "
        f"candidate_experiences={candidate_pool['total']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
