"""Tests for cross-platform migration skeleton validation."""

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import validate_migration_skeletons as vms  # noqa: E402


def write_page(path: Path, page_id: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "---\n"
        + yaml.safe_dump({"id": page_id, "title": page_id}, sort_keys=False)
        + "---\n\n# Page\n",
        encoding="utf-8",
    )


def write_skeleton(path: Path, skeletons: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.safe_dump({"schema_version": 1, "skeletons": skeletons}, sort_keys=False),
        encoding="utf-8",
    )


def test_validates_cross_repo_source_links(tmp_path):
    workspace = tmp_path
    cuda = workspace / "KernelWiki-Q"
    rocm = workspace / "ROCm-KernelWiki-Q"
    ascend = workspace / "Ascend-KernelWiki-Q"

    write_page(cuda / "sources" / "docs" / "cuda.md", "doc-cuda")
    write_page(rocm / "wiki" / "hardware" / "rocm.md", "hw-rocm")
    write_page(ascend / "sources" / "docs" / "ascend.md", "doc-ascend")

    skeleton_path = cuda / "data" / "migration-skeletons.yaml"
    write_skeleton(
        skeleton_path,
        [
            {
                "id": "migration-skeleton-test",
                "title": "CUDA to ROCm/Ascend test",
                "cuda_source_ids": ["doc-cuda"],
                "target_platforms": {
                    "rocm": {"target_source_ids": ["hw-rocm"]},
                    "ascend": {"target_source_ids": ["doc-ascend"]},
                },
            }
        ],
    )

    assert vms.validate_file(skeleton_path, workspace) == []


def test_rejects_missing_required_source_links(tmp_path):
    workspace = tmp_path
    cuda = workspace / "KernelWiki-Q"
    rocm = workspace / "ROCm-KernelWiki-Q"
    ascend = workspace / "Ascend-KernelWiki-Q"

    write_page(cuda / "sources" / "docs" / "cuda.md", "doc-cuda")
    write_page(rocm / "wiki" / "hardware" / "rocm.md", "hw-rocm")
    write_page(ascend / "sources" / "docs" / "ascend.md", "doc-ascend")

    skeleton_path = cuda / "data" / "migration-skeletons.yaml"
    write_skeleton(
        skeleton_path,
        [
            {
                "id": "migration-skeleton-bad",
                "title": "Bad skeleton",
                "cuda_source_ids": [],
                "target_platforms": {
                    "rocm": {"target_source_ids": ["missing-rocm"]},
                    "ascend": {"target_source_ids": []},
                },
            }
        ],
    )

    errors = vms.validate_file(skeleton_path, workspace)

    assert "migration-skeleton-bad: cuda_source_ids must not be empty" in errors
    assert "migration-skeleton-bad: rocm target_source_ids unresolved: missing-rocm" in errors
    assert "migration-skeleton-bad: ascend target_source_ids must not be empty" in errors
