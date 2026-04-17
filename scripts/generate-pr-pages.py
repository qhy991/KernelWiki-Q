#!/usr/bin/env python3
"""Generate PR source pages from candidate ledger YAML files.

Reads candidates/{repo}.yaml, fetches PR details from GitHub API,
and creates sources/prs/{repo_slug}/PR-{number}.md for each included PR.

Usage:
    python3 scripts/generate-pr-pages.py candidates/cutlass.yaml
    python3 scripts/generate-pr-pages.py --all
"""

import json
import os
import re
import sys
import time
import urllib.request
import yaml
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
TAGS_PATH = REPO_ROOT / "data" / "tags.yaml"

# Load controlled vocabulary
with open(TAGS_PATH, encoding="utf-8") as f:
    TAGS_DATA = yaml.safe_load(f)

VALID_HW = set(TAGS_DATA.get("hardware_features", []))
VALID_TECHNIQUES = set(TAGS_DATA.get("techniques", []))
VALID_KT = set(TAGS_DATA.get("kernel_types", []))
VALID_LANGS = set(TAGS_DATA.get("languages", []))
ALL_TAGS = VALID_HW | VALID_TECHNIQUES | VALID_KT | VALID_LANGS

# Keyword -> tag mappings for auto-tagging from PR titles/files
KW_TO_TAGS = {
    "tcgen05": "tcgen05", "tmem": "tmem", "tma": "tma", "clc": "clc",
    "nvfp4": "nvfp4", "fp8": "fp8", "fp4": "fp4", "block_scale": "block-scale",
    "block-scale": "block-scale", "mbarrier": "mbarrier", "wgmma": "wgmma",
    "2sm": "2sm-cooperative", "2cta": "2sm-cooperative", "cta_group": "2sm-cooperative",
}
KW_TO_KT = {
    "gemm": "gemm", "attention": "attention", "moe": "moe", "fmha": "flash-attention",
    "flash_attention": "flash-attention", "flash-attention": "flash-attention",
    "mla": "mla", "gemv": "gemv", "grouped_gemm": "grouped-gemm",
    "grouped-gemm": "grouped-gemm", "decode": "decode", "prefill": "prefill",
    "sparse_attention": "sparse-attention", "sparse-attention": "sparse-attention",
    "gated_delta": "gated-delta-net", "quantiz": "quantization",
}
KW_TO_TECH = {
    "warp_special": "warp-specialization", "warp-specialization": "warp-specialization",
    "persistent": "persistent-kernel", "swizzl": "swizzling",
    "pipeline": "pipeline-stages", "epilogue": "epilogue-fusion",
    "tile_schedul": "tile-scheduling", "double_buffer": "double-buffering",
    "fusion": "kernel-fusion", "fused": "kernel-fusion",
}
KW_TO_LANG = {
    ".cu": "cuda-cpp", ".cuh": "cuda-cpp", "cuda": "cuda-cpp",
    "cute_dsl": "cute-dsl", "cute-dsl": "cute-dsl", "cutedsl": "cute-dsl",
    "triton": "triton", ".ptx": "ptx", "ptx": "ptx",
    "python": "python", "tilelang": "tilelang",
}

EXCLUDE_TITLE_PATTERNS = [
    r'\[ci\]', r'\[doc\]', r'\[docs\]', r'bump', r'typo', r'format',
    r'lint', r'\bnit\b', r'revert', r'readme', r'changelog', r'pre-commit',
    r'ruff', r'deprecat', r'release\s+note', r'committers\.md',
]


def fetch_pr(repo, number):
    """Fetch PR details from GitHub API."""
    url = f"https://api.github.com/repos/{repo}/pulls/{number}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "bw-wiki-bot"})
        resp = urllib.request.urlopen(req, timeout=30)
        return json.loads(resp.read())
    except Exception as e:
        print(f"  WARN: Could not fetch {repo}#{number}: {e}")
        return None


def fetch_pr_files(repo, number):
    """Fetch list of changed files for a PR."""
    url = f"https://api.github.com/repos/{repo}/pulls/{number}/files?per_page=100"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "bw-wiki-bot"})
        resp = urllib.request.urlopen(req, timeout=30)
        files = json.loads(resp.read())
        return [f["filename"] for f in files]
    except Exception:
        return []


def is_kernel_related(title, files):
    """Check if PR is kernel-related based on title + changed files."""
    title_lower = title.lower()

    # Title-based exclusion
    for pat in EXCLUDE_TITLE_PATTERNS:
        if re.search(pat, title_lower):
            return False, "excluded by title pattern"

    # File-based inclusion
    kernel_exts = {".cu", ".cuh", ".ptx"}
    kernel_dirs = {"cutlass/", "csrc/", "kernel", "triton/", "cute/", "gemm", "attention", "moe"}

    has_kernel_file = False
    for f in files:
        ext = os.path.splitext(f)[1]
        if ext in kernel_exts:
            has_kernel_file = True
            break
        for kd in kernel_dirs:
            if kd in f.lower():
                has_kernel_file = True
                break

    # Semantic signals in title
    semantic_kws = ["kernel", "sm100", "blackwell", "tcgen05", "tmem", "nvfp4",
                     "fp8", "gemm", "attention", "moe", "mla", "cutlass",
                     "flashinfer", "deepgemm", "flashmla", "triton", "fmha"]
    has_semantic = any(kw in title_lower for kw in semantic_kws)

    if has_kernel_file:
        return True, "kernel file changes"
    if has_semantic and files:
        return True, "semantic match with file changes"
    if has_semantic and not files:
        return None, "semantic match but no file data"  # defer
    return False, "no kernel signals"


def auto_tag(title, files):
    """Auto-detect tags from title and changed files."""
    text = (title + " " + " ".join(files)).lower()

    tags = set()
    hw_features = set()
    kernel_types = set()
    techniques = set()
    languages = set()

    for kw, tag in KW_TO_TAGS.items():
        if kw in text:
            hw_features.add(tag)
            tags.add(tag)

    for kw, kt in KW_TO_KT.items():
        if kw in text:
            kernel_types.add(kt)
            tags.add(kt)

    for kw, tech in KW_TO_TECH.items():
        if kw in text:
            techniques.add(tech)
            tags.add(tech)

    for kw, lang in KW_TO_LANG.items():
        if kw in text:
            languages.add(lang)

    # Filter to valid vocabulary only
    tags = tags & ALL_TAGS
    hw_features = hw_features & VALID_HW
    kernel_types = kernel_types & VALID_KT
    techniques = techniques & VALID_TECHNIQUES
    languages = languages & VALID_LANGS

    # Default language if none detected
    if not languages:
        for f in files:
            if f.endswith((".cu", ".cuh")):
                languages.add("cuda-cpp")
            elif f.endswith(".py") and "triton" in f.lower():
                languages.add("triton")
            elif f.endswith(".py"):
                languages.add("python")

    return sorted(tags), sorted(hw_features), sorted(kernel_types), sorted(techniques), sorted(languages)


def generate_page(repo, pr_data, files, inclusion_reason):
    """Generate markdown page content for a PR."""
    repo_slug = repo.split("/")[1]
    number = pr_data["number"]
    title = pr_data["title"]
    author = pr_data["user"]["login"]
    date = pr_data["created_at"][:10]
    url = pr_data["html_url"]
    merge_sha = (pr_data.get("merge_commit_sha") or "unknown")[:8]
    body = pr_data.get("body") or ""

    # Determine architectures
    archs = ["sm100"]
    text = (title + " " + body).lower()
    if "sm90" in text or "hopper" in text:
        archs.append("sm90")

    tags, hw_features, kernel_types, techniques, languages = auto_tag(title, files)

    # Ensure tags include all kernel_types and hw_features
    all_tags = set(tags)
    for kt in kernel_types:
        if kt in ALL_TAGS:
            all_tags.add(kt)
    for hw in hw_features:
        if hw in ALL_TAGS:
            all_tags.add(hw)
    tags = sorted(all_tags & ALL_TAGS)

    # Kernel file paths only
    kernel_paths = [f for f in files if any(
        f.endswith(ext) for ext in [".cu", ".cuh", ".ptx", ".py"]
    )][:10]

    # Build frontmatter
    fm = {
        "id": f"pr-{repo_slug}-{number}",
        "repo": repo,
        "pr": number,
        "title": title,
        "author": author,
        "date": date,
        "url": url,
        "source_category": "upstream-code",
        "architectures": archs,
        "tags": tags if tags else ["gemm"],
        "techniques": techniques if techniques else [],
        "hardware_features": hw_features if hw_features else [],
        "kernel_types": kernel_types if kernel_types else [],
        "languages": languages if languages else ["cuda-cpp"],
        "captured_at": "2026-04-17",
        "status": "merged",
        "merge_sha": merge_sha,
        "inclusion_reason": inclusion_reason,
        "changed_paths": kernel_paths if kernel_paths else [],
    }

    # Build body summary from PR description
    summary = body[:500].strip() if body else "No description provided."
    summary = re.sub(r'<!--.*?-->', '', summary, flags=re.DOTALL).strip()
    summary = summary[:300] if len(summary) > 300 else summary

    content = "---\n"
    content += yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
    content += "---\n\n"
    content += f"## Summary\n\n{summary}\n\n"
    content += f"## Problem\n\n{title}\n\n"
    content += f"## Changed Files\n\n"
    for f in files[:15]:
        content += f"- `{f}`\n"
    content += "\n"

    return content


def process_ledger(ledger_path):
    """Process a candidate ledger and generate PR pages."""
    with open(ledger_path, encoding="utf-8") as f:
        ledger = yaml.safe_load(f)

    repo = ledger["repo"]
    repo_slug = repo.split("/")[1]
    outdir = REPO_ROOT / "sources" / "prs" / repo_slug
    outdir.mkdir(parents=True, exist_ok=True)

    # Get existing PR numbers to avoid re-fetching
    existing = set()
    for p in outdir.glob("PR-*.md"):
        try:
            existing.add(int(p.stem.split("-")[1]))
        except (ValueError, IndexError):
            pass

    # Get included candidates
    prs_key = "prs" if "prs" in ledger else "candidates"
    candidates = ledger.get(prs_key, [])

    included = []
    for c in candidates:
        decision = str(c.get("decision", "")).lower()
        if decision == "include":
            num = c["number"]
            if num not in existing:
                included.append(c)

    print(f"\n{repo}: {len(included)} new PRs to generate ({len(existing)} already exist)")

    generated = 0
    skipped = 0

    for i, candidate in enumerate(included):
        number = candidate["number"]
        title = candidate.get("title", "")

        # Fetch PR details
        pr_data = fetch_pr(repo, number)
        time.sleep(1)

        if not pr_data:
            skipped += 1
            continue

        files = fetch_pr_files(repo, number)
        time.sleep(1)

        # Re-triage with file data
        is_kernel, reason = is_kernel_related(title, files)
        if is_kernel is False:
            skipped += 1
            continue

        inclusion_reason = reason if is_kernel else "deferred-semantic"
        content = generate_page(repo, pr_data, files, inclusion_reason)

        outpath = outdir / f"PR-{number}.md"
        outpath.write_text(content, encoding="utf-8")
        generated += 1

        if generated % 10 == 0:
            print(f"  Generated {generated} pages so far...")

        # Rate limit
        if (i + 1) % 20 == 0:
            print(f"  Rate limit pause at {i+1}...")
            time.sleep(30)

    print(f"  Done: {generated} generated, {skipped} skipped, {len(existing)} pre-existing")
    return generated


def main():
    if "--all" in sys.argv:
        ledger_dir = REPO_ROOT / "candidates"
        for ledger_file in sorted(ledger_dir.glob("*.yaml")):
            process_ledger(ledger_file)
    elif len(sys.argv) > 1:
        process_ledger(sys.argv[1])
    else:
        print("Usage: python3 scripts/generate-pr-pages.py candidates/cutlass.yaml")
        print("       python3 scripts/generate-pr-pages.py --all")


if __name__ == "__main__":
    main()
