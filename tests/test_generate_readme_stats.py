"""Tests for README corpus statistics generation."""

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import generate_readme_stats as stats  # noqa: E402


def write_page(path: Path, frontmatter: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "---\n" + yaml.safe_dump(frontmatter, sort_keys=False) + "---\n\n# Page\n",
        encoding="utf-8",
    )


def test_collect_stats_counts_pages_sources_bundles_and_ledgers(tmp_path):
    write_page(
        tmp_path / "sources" / "prs" / "cutlass" / "PR-1.md",
        {
            "id": "source-pr-cutlass-1",
            "source_category": "upstream-code",
            "confidence": "source-reported",
        },
    )
    write_page(
        tmp_path / "wiki" / "kernels" / "gemm.md",
        {
            "id": "kernel-gemm",
            "type": "kernel",
            "confidence": "verified",
        },
    )

    bundle = tmp_path / "artifacts" / "prs" / "cutlass" / "PR-1"
    bundle.mkdir(parents=True)
    (bundle / "PROVENANCE.yaml").write_text(
        yaml.safe_dump({"asset_mode": "verbatim"}),
        encoding="utf-8",
    )

    ledger = tmp_path / "candidates" / "cutlass.yaml"
    ledger.parent.mkdir(parents=True)
    ledger.write_text(
        yaml.safe_dump({
            "total_candidates": 3,
            "included": 1,
            "excluded": 1,
            "deferred": 1,
        }),
        encoding="utf-8",
    )

    result = stats.collect_stats(tmp_path)

    assert result["page_count"] == 2
    assert result["source_id_count"] == 1
    assert result["source_page_counts"] == {"prs": 1}
    assert result["wiki_page_counts"] == {"kernels": 1}
    assert result["asset_bundle_count"] == 1
    assert result["asset_mode_counts"] == {"verbatim": 1}
    assert result["candidate_ledger_count"] == 1
    assert result["candidate_totals"]["total_candidates"] == 3


def test_render_and_update_readme_stats_block():
    rendered = stats.render_stats({
        "page_count": 2,
        "source_count": 1,
        "wiki_count": 1,
        "source_id_count": 1,
        "source_page_counts": {"prs": 1},
        "wiki_page_counts": {"kernels": 1},
        "source_category_counts": {"upstream-code": 1},
        "confidence_counts": {"verified": 1, "source-reported": 1},
        "asset_bundle_count": 1,
        "asset_mode_counts": {"verbatim": 1},
        "candidate_ledger_count": 1,
        "candidate_totals": {
            "total_candidates": 3,
            "included": 1,
            "excluded": 1,
            "deferred": 1,
        },
    })

    assert "Markdown pages: 2" in rendered
    assert "Asset bundles: 1" in rendered

    original = (
        "# README\n\n"
        f"{stats.STATS_START}\n"
        "old\n"
        f"{stats.STATS_END}\n"
    )

    updated = stats.replace_stats_block(original, rendered)

    assert "old" not in updated
    assert "Markdown pages: 2" in updated
