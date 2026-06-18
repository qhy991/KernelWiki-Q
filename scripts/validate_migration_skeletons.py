#!/usr/bin/env python3
"""Validate CUDA -> ROCm/Ascend migration skeleton data."""

import argparse
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
WORKSPACE_ROOT = ROOT.parent
DEFAULT_SKELETON_FILE = ROOT / "data" / "migration-skeletons.yaml"
TARGET_REPOS = {
    "cuda": "KernelWiki-Q",
    "rocm": "ROCm-KernelWiki-Q",
    "ascend": "Ascend-KernelWiki-Q",
}


def extract_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return {}
    data = yaml.safe_load(match.group(1)) or {}
    return data if isinstance(data, dict) else {}


def collect_ids(repo_root: Path) -> set[str]:
    ids = set()
    for base in ("sources", "wiki"):
        root = repo_root / base
        if not root.exists():
            continue
        for path in root.rglob("*.md"):
            page_id = extract_frontmatter(path).get("id")
            if page_id:
                ids.add(str(page_id))
    return ids


def load_yaml(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data if isinstance(data, dict) else {}


def validate_file(path: Path = DEFAULT_SKELETON_FILE, workspace_root: Path = WORKSPACE_ROOT) -> list[str]:
    data = load_yaml(path)
    skeletons = data.get("skeletons")
    if not isinstance(skeletons, list):
        return ["skeletons must be a list"]

    ids_by_platform = {
        platform: collect_ids(Path(workspace_root) / repo_name)
        for platform, repo_name in TARGET_REPOS.items()
    }

    errors = []
    seen_ids = set()
    for index, skeleton in enumerate(skeletons):
        if not isinstance(skeleton, dict):
            errors.append(f"skeleton[{index}] must be a mapping")
            continue

        skeleton_id = skeleton.get("id") or f"skeleton[{index}]"
        if skeleton_id in seen_ids:
            errors.append(f"{skeleton_id}: duplicate id")
        seen_ids.add(skeleton_id)

        if not skeleton.get("title"):
            errors.append(f"{skeleton_id}: title is required")

        cuda_source_ids = skeleton.get("cuda_source_ids") or []
        if not cuda_source_ids:
            errors.append(f"{skeleton_id}: cuda_source_ids must not be empty")
        for source_id in cuda_source_ids:
            if source_id not in ids_by_platform["cuda"]:
                errors.append(f"{skeleton_id}: cuda_source_ids unresolved: {source_id}")

        target_platforms = skeleton.get("target_platforms") or {}
        for platform in ("rocm", "ascend"):
            target = target_platforms.get(platform) or {}
            target_source_ids = target.get("target_source_ids") or []
            if not target_source_ids:
                errors.append(f"{skeleton_id}: {platform} target_source_ids must not be empty")
                continue
            missing = [sid for sid in target_source_ids if sid not in ids_by_platform[platform]]
            if missing:
                errors.append(
                    f"{skeleton_id}: {platform} target_source_ids unresolved: "
                    + ", ".join(missing)
                )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", type=Path, default=DEFAULT_SKELETON_FILE)
    parser.add_argument("--workspace-root", type=Path, default=WORKSPACE_ROOT)
    args = parser.parse_args()

    errors = validate_file(args.file, args.workspace_root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    data = load_yaml(args.file)
    print(f"Migration skeletons valid: {len(data.get('skeletons') or [])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
