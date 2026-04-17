#!/usr/bin/env python3
"""Retrieve a single wiki page by its id or path.

Usage:
    get_page.py kernel-flash-attention-4         # by id
    get_page.py pr-cutlass-2472                   # by id
    get_page.py wiki/kernels/flash-attention-4.md # by path
    get_page.py kernel-flash-attention-4 --body-only
    get_page.py kernel-flash-attention-4 --frontmatter-only
    get_page.py kernel-flash-attention-4 --follow-sources  # also print first 500 chars of each source
"""

import argparse
import re
import sys
import yaml
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _wiki_root import WIKI_ROOT  # noqa: E402


def find_page(lookup):
    """Find a page by id or by relative path. Returns Path or None."""
    # If it looks like a path, try it directly
    if "/" in lookup or lookup.endswith(".md"):
        p = WIKI_ROOT / lookup
        if p.exists():
            return p
        return None

    # Otherwise scan all md files and match by frontmatter id
    for subdir in ["wiki", "sources"]:
        base = WIKI_ROOT / subdir
        if not base.exists():
            continue
        for md in base.rglob("*.md"):
            try:
                content = md.read_text(encoding="utf-8")
            except Exception:
                continue
            m = re.match(r'^---\s*\r?\n(.*?)\r?\n---', content, re.DOTALL)
            if not m:
                continue
            try:
                fm = yaml.safe_load(m.group(1))
            except yaml.YAMLError:
                continue
            if isinstance(fm, dict) and fm.get("id") == lookup:
                return md
    return None


def split_frontmatter(content):
    m = re.match(r'^---\s*\r?\n(.*?)\r?\n---\s*\r?\n(.*)', content, re.DOTALL)
    if not m:
        return None, content
    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        fm = None
    return fm, m.group(2)


def main():
    parser = argparse.ArgumentParser(description="Get a wiki page by id or path")
    parser.add_argument("lookup", help="Page id (e.g. kernel-flash-attention-4) or relative path")
    parser.add_argument("--body-only", action="store_true", help="Print only the body (skip frontmatter)")
    parser.add_argument("--frontmatter-only", action="store_true", help="Print only the frontmatter as YAML")
    parser.add_argument("--follow-sources", action="store_true", help="Also print 500-char excerpt from each cited source")
    parser.add_argument("--include-code", action="store_true", help="After the page body, print all files under the page's artifact_dir (Phase 3)")
    args = parser.parse_args()

    page_path = find_page(args.lookup)
    if not page_path:
        print(f"ERROR: No page found for '{args.lookup}'", file=sys.stderr)
        sys.exit(1)

    content = page_path.read_text(encoding="utf-8")
    fm, body = split_frontmatter(content)

    if args.frontmatter_only:
        if fm:
            print(yaml.dump(fm, allow_unicode=True, sort_keys=False))
        return

    if args.body_only:
        print(body)
        return

    # Default: full page, prefixed with a path header for context
    print(f"# {page_path.relative_to(WIKI_ROOT)}")
    print()
    print(content)

    if args.follow_sources and fm and "sources" in fm:
        print()
        print("---")
        print("## Cited Sources (excerpts)")
        print()
        for src_id in fm.get("sources", []):
            src_page = find_page(src_id)
            if src_page:
                src_content = src_page.read_text(encoding="utf-8")
                _, src_body = split_frontmatter(src_content)
                excerpt = (src_body or "")[:500].strip()
                print(f"### {src_id}")
                print(f"`{src_page.relative_to(WIKI_ROOT)}`")
                print()
                print(excerpt)
                print()

    if args.include_code and fm and "artifact_dir" in fm:
        ad = fm.get("artifact_dir")
        ad_path = WIKI_ROOT / ad
        if ad_path.is_dir():
            print()
            print("---")
            print(f"## Artifact Bundle: `{ad}`")
            print()
            exts = {".cu", ".cuh", ".ptx", ".py", ".cpp", ".h", ".hpp", ".patch", ".md", ".yaml", ".txt"}
            for f in sorted(ad_path.rglob("*")):
                if not f.is_file() or f.suffix.lower() not in exts:
                    continue
                rel_to_bundle = f.relative_to(ad_path)
                print(f"### `{rel_to_bundle}`")
                print()
                try:
                    body_bytes = f.read_bytes()
                    if f.stat().st_size > 200 * 1024:
                        print(f"*(file is {f.stat().st_size} bytes; showing first 200 KiB)*")
                        body_bytes = body_bytes[:200 * 1024]
                    print("```" + (f.suffix.lstrip(".") or ""))
                    print(body_bytes.decode("utf-8", errors="replace"))
                    print("```")
                    print()
                except Exception as e:
                    print(f"*(could not read: {e})*")
                    print()
        else:
            print()
            print(f"*(artifact_dir '{ad}' not found on disk)*")


if __name__ == "__main__":
    main()
