"""Cross-KernelWiki CLI contract tests for KernelWiki-Q."""

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def run_cli(*args):
    return subprocess.run(
        [sys.executable, *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def test_query_supports_common_operator_filter():
    result = run_cli("scripts/query.py", "--type", "kernel", "--operator", "gemm", "--limit", "3", "--compact")

    assert result.returncode == 0, result.stderr
    assert "kernel-deepgemm" in result.stdout


def test_get_page_supports_common_frontmatter_body_and_field_flags():
    frontmatter = run_cli("scripts/get_page.py", "kernel-deepgemm", "--frontmatter")
    assert frontmatter.returncode == 0, frontmatter.stderr
    assert "id: kernel-deepgemm" in frontmatter.stdout

    body = run_cli("scripts/get_page.py", "kernel-deepgemm", "--body-only")
    assert body.returncode == 0, body.stderr
    assert "# DeepGEMM" in body.stdout
    assert "id: kernel-deepgemm" not in body.stdout

    field = run_cli("scripts/get_page.py", "kernel-deepgemm", "--field", "title")
    assert field.returncode == 0, field.stderr
    assert "DeepGEMM" in field.stdout


def test_generate_indices_writes_common_manifest_files():
    result = run_cli("scripts/generate-indices.py")

    assert result.returncode == 0, result.stderr
    index = ROOT / "queries" / "INDEX.md"
    manifest = ROOT / "queries" / "pages.json"
    assert index.exists()
    assert manifest.exists()

    records = json.loads(manifest.read_text(encoding="utf-8"))
    assert any(record["id"] == "kernel-deepgemm" for record in records)
