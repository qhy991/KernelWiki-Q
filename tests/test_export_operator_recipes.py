"""Tests for high-confidence operator recipe export."""

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import export_operator_recipes as recipes  # noqa: E402


def write_page(path: Path, frontmatter: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "---\n"
        + yaml.safe_dump(frontmatter, sort_keys=False)
        + "---\n\n# Page\n",
        encoding="utf-8",
    )


def test_export_separates_default_recipes_from_low_confidence_candidates(tmp_path):
    write_page(
        tmp_path / "wiki" / "kernels" / "gemm.md",
        {
            "id": "kernel-gemm",
            "title": "Verified GEMM",
            "type": "kernel",
            "confidence": "verified",
            "reproducibility": "snippet",
            "architectures": ["sm100"],
            "tags": ["gemm"],
            "kernel_types": ["gemm"],
            "languages": ["cuda-cpp"],
            "techniques": ["warp-specialization"],
            "hardware_features": ["tcgen05"],
            "sources": ["doc-sm100", "pr-cutlass-1"],
        },
    )
    write_page(
        tmp_path / "sources" / "experiences" / "exp-good.md",
        {
            "id": "exp-good",
            "title": "Source reported GEMM fallback",
            "experience_type": "optimization",
            "source_category": "agent-experiment",
            "confidence": "source-reported",
            "reproducibility": "concept",
            "architectures": ["sm90"],
            "tags": ["gemm"],
            "kernel_types": ["gemm"],
            "languages": ["cuda-cpp"],
            "captured_at": "2026-01-01",
        },
    )
    write_page(
        tmp_path / "sources" / "experiences" / "exp-low.md",
        {
            "id": "exp-low",
            "title": "Experimental topk trick",
            "experience_type": "optimization",
            "source_category": "agent-experiment",
            "confidence": "experimental",
            "reproducibility": "snippet",
            "architectures": ["sm90"],
            "tags": ["topk"],
            "kernel_types": ["topk"],
            "languages": ["cuda-cpp"],
            "captured_at": "2026-01-01",
        },
    )

    export = recipes.collect_recipe_export(tmp_path)

    default_ids = {entry["recipe_id"] for entry in export["default_recipes"]}
    assert default_ids == {"recipe-kernel-gemm", "recipe-exp-good"}

    for entry in export["default_recipes"]:
        assert entry["confidence"] in {"verified", "source-reported"}
        assert entry["source_ids"], entry

    assert export["candidate_pool"]["total"] == 1
    assert export["candidate_pool"]["by_confidence"] == {"experimental": 1}
    assert export["candidate_pool"]["groups"] == [
        {
            "confidence": "experimental",
            "kernel_type": "topk",
            "count": 1,
            "sample_source_ids": ["exp-low"],
        }
    ]
