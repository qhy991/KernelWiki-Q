#!/usr/bin/env python3
"""Extract fenced code blocks from sources/blogs/*.md into standalone files
under artifacts/blogs/<slug>/code/, with a MANIFEST.yaml that maps each
extracted file to its originating heading path and SHA-256 (AC-4).

Modes:
  extract   — write fresh files (default; overwrites existing if drift detected)
  --check <slug>   — idempotent check: re-parse markdown + verify checksums
  --check-all      — run --check across every blog slug

Extension mapping (fence language -> suffix):
  cuda, cu, c++, cpp, cxx -> .cu
  cuh                     -> .cuh
  ptx                     -> .ptx
  python, py, triton      -> .py (triton kernels are python code)
  cute                    -> .py   (CuTe DSL is python)
  yaml                    -> .yaml
  (unknown)               -> .txt

Output format: every extracted file carries a header comment documenting
provenance-in-source-blog; the PROVENANCE.yaml bundle metadata lives at
artifacts/blogs/<slug>/PROVENANCE.yaml (asset_mode: extracted).
"""

import argparse
import hashlib
import re
import sys
from pathlib import Path
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
BLOGS_DIR = REPO_ROOT / "sources" / "blogs"
OUT_DIR = REPO_ROOT / "artifacts" / "blogs"

EXT_MAP = {
    "cuda": "cu", "cu": "cu", "cpp": "cpp", "c++": "cpp", "cxx": "cpp", "c": "cpp",
    "cuh": "cuh",
    "ptx": "ptx", "asm": "ptx",
    "python": "py", "py": "py", "triton": "py", "cute": "py",
    "yaml": "yaml",
    "bash": "sh", "shell": "sh", "sh": "sh",
    "json": "json",
}

SLUGIFY_RE = re.compile(r"[^a-z0-9]+")


def slugify(s):
    s = s.lower().strip()
    s = SLUGIFY_RE.sub("-", s)
    return s.strip("-")[:60] or "section"


def parse_markdown(md_path):
    """Yield (heading_path, fence_lang, fence_body) for every fenced code block.

    heading_path is "## A > ### B" — the nearest ancestor chain of markdown
    headings above the fence.
    """
    try:
        text = md_path.read_text(encoding="utf-8")
    except OSError:
        return

    # Strip frontmatter
    m = re.match(r"^---\s*\r?\n.*?\r?\n---\s*\r?\n(.*)", text, re.DOTALL)
    body = m.group(1) if m else text

    lines = body.splitlines()
    heading_stack = []  # list of (level, text)
    i = 0
    while i < len(lines):
        line = lines[i]
        # heading detection
        mh = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if mh:
            level = len(mh.group(1))
            htext = mh.group(2).rstrip("#").strip()
            # Pop stack until we find a strictly-less-than level
            while heading_stack and heading_stack[-1][0] >= level:
                heading_stack.pop()
            heading_stack.append((level, htext))
            i += 1
            continue
        # fence detection (```lang or ~~~lang)
        mf = re.match(r"^```(\S*)\s*$", line)
        if mf:
            lang = mf.group(1).strip().lower()
            buf = []
            i += 1
            while i < len(lines) and not re.match(r"^```\s*$", lines[i]):
                buf.append(lines[i])
                i += 1
            # closing fence
            if i < len(lines):
                i += 1
            hp = " > ".join(f"{'#'*lvl} {t}" for lvl, t in heading_stack) if heading_stack else "(root)"
            yield hp, lang, "\n".join(buf) + "\n"
            continue
        i += 1


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def extract_one_blog(blog_md, force=False):
    """Extract code from a single blog. Returns (num_files_written, code_present_bool)."""
    slug = blog_md.stem
    bundle = OUT_DIR / slug
    code_dir = bundle / "code"
    manifest_path = bundle / "MANIFEST.yaml"
    prov_path = bundle / "PROVENANCE.yaml"

    blocks = list(parse_markdown(blog_md))

    # Read blog frontmatter for provenance metadata
    try:
        md_text = blog_md.read_text(encoding="utf-8")
    except OSError:
        return 0, False
    mf = re.match(r"^---\s*\r?\n(.*?)\r?\n---", md_text, re.DOTALL)
    fm = yaml.safe_load(mf.group(1)) if mf else {}
    origin_url = fm.get("url", "") if isinstance(fm, dict) else ""
    author = fm.get("author", "") if isinstance(fm, dict) else ""
    retrieved = fm.get("retrieved_at", "") if isinstance(fm, dict) else ""

    # Filter out trivial or non-code blocks
    code_blocks = [(hp, lang, body) for (hp, lang, body) in blocks
                   if lang in EXT_MAP and body.strip()]

    if not code_blocks:
        # Write a code_present: false manifest if the bundle doesn't exist
        bundle.mkdir(parents=True, exist_ok=True)
        manifest_path.write_text(yaml.dump({
            "slug": slug,
            "origin_url": origin_url,
            "code_present": False,
            "generated_by": "scripts/extract_blog_code.py",
        }, sort_keys=False), encoding="utf-8")
        # Also write a minimal PROVENANCE.yaml so validate.py is happy? Actually
        # the bundle root must have PROVENANCE.yaml OR not be a bundle. If code
        # is absent, the bundle is not a source-asset bundle; skip.
        return 0, False

    # Fresh extract: clear existing code dir to avoid orphan files
    if code_dir.is_dir():
        for f in code_dir.iterdir():
            if f.is_file():
                f.unlink()

    code_dir.mkdir(parents=True, exist_ok=True)

    manifest_files = []
    files_entries = []  # for PROVENANCE.yaml files[*]
    seen_names = set()
    for idx, (heading_path, lang, body) in enumerate(code_blocks, start=1):
        # Build a filename: NN-<slug-of-heading>.<ext>
        leaf = heading_path.split(" > ")[-1] if heading_path != "(root)" else "root"
        leaf = re.sub(r"^#+\s*", "", leaf)
        stub = slugify(leaf)
        ext = EXT_MAP.get(lang, "txt")
        fn = f"{idx:02d}-{stub}.{ext}"
        # Deduplicate
        orig = fn
        k = 2
        while fn in seen_names:
            fn = orig.replace(f".{ext}", f"-{k}.{ext}")
            k += 1
        seen_names.add(fn)

        header = (
            f"// Extracted from sources/blogs/{slug}.md by scripts/extract_blog_code.py\n"
            f"// Heading: {heading_path}\n"
            f"// Original fence language: {lang}\n"
            f"// See artifacts/blogs/{slug}/PROVENANCE.yaml for origin + license metadata.\n\n"
            if ext in ("cu", "cuh", "cpp", "ptx", "h", "hpp")
            else f"# Extracted from sources/blogs/{slug}.md by scripts/extract_blog_code.py\n"
                 f"# Heading: {heading_path}\n"
                 f"# Original fence language: {lang}\n"
                 f"# See artifacts/blogs/{slug}/PROVENANCE.yaml for origin + license metadata.\n\n"
        )
        content = header + body
        (code_dir / fn).write_text(content, encoding="utf-8")

        content_bytes = content.encode("utf-8")
        sha = sha256_bytes(content_bytes)
        # MANIFEST.yaml sits at the parent (bundle/) level, so its paths are
        # bundle-relative ("code/<fn>"). PROVENANCE.yaml lives at code/ (which
        # IS the asset-bundle root), so its local_path entries are just "<fn>".
        manifest_files.append({
            "local_path": f"code/{fn}",
            "heading_path": heading_path,
            "fence_lang": lang,
            "sha256": sha,
        })
        files_entries.append({
            "local_path": fn,
            "role": "extracted-block",
            "mode": "extracted",
            "upstream_path": "inline-in-blog-markdown",
            "heading_path": heading_path,
            "sha256": sha,
        })

    # Write MANIFEST.yaml (bundle-relative)
    manifest_path.write_text(yaml.dump({
        "slug": slug,
        "origin_url": origin_url,
        "code_present": True,
        "total_blocks": len(manifest_files),
        "generated_by": "scripts/extract_blog_code.py",
        "files": manifest_files,
    }, sort_keys=False), encoding="utf-8")

    # Write PROVENANCE.yaml for the code/ bundle root
    prov_code_path = code_dir / "PROVENANCE.yaml"
    prov_code_path.write_text(yaml.dump({
        "origin_url": origin_url,
        "upstream_repo": "blog",
        "upstream_sha": "none",
        "license": "inherits-from-source-blog",
        "retrieved_at": retrieved or "",
        "asset_mode": "extracted",
        "generated_by": "scripts/extract_blog_code.py",
        "size_cap_truncated": False,
        "files": files_entries,
    }, sort_keys=False), encoding="utf-8")

    return len(manifest_files), True


def check_one_blog(slug):
    bundle = OUT_DIR / slug
    manifest_path = bundle / "MANIFEST.yaml"
    code_dir = bundle / "code"
    if not manifest_path.is_file():
        return [f"{slug}: MANIFEST.yaml not found"]
    try:
        manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as e:
        return [f"{slug}: MANIFEST.yaml parse error: {e}"]

    errors = []
    if not manifest.get("code_present"):
        # Nothing to check
        return []

    # Recompute blocks from source blog
    blog_md = BLOGS_DIR / f"{slug}.md"
    if not blog_md.is_file():
        errors.append(f"{slug}: source blog not found at {blog_md.relative_to(REPO_ROOT)}")
        return errors

    fresh_blocks = [(hp, lang, body) for (hp, lang, body) in parse_markdown(blog_md)
                    if lang in EXT_MAP and body.strip()]

    manifest_count = len(manifest.get("files", []))
    if len(fresh_blocks) != manifest_count:
        errors.append(
            f"{slug}: markdown-vs-manifest drift "
            f"(markdown has {len(fresh_blocks)} code blocks, manifest has {manifest_count})"
        )

    for entry in manifest.get("files") or []:
        lp = entry.get("local_path")
        declared_sha = entry.get("sha256")
        if not lp or not declared_sha:
            continue
        fp = bundle / lp
        if not fp.is_file():
            errors.append(f"{slug}/{lp}: file missing")
            continue
        actual = sha256_bytes(fp.read_bytes())
        if actual != declared_sha:
            errors.append(f"{slug}/{lp}: SHA-256 mismatch (hand-edit detected)")

    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--check", metavar="SLUG", help="Idempotent check for one blog")
    parser.add_argument("--check-all", action="store_true", help="Check every extracted blog")
    parser.add_argument("--only", metavar="SLUG", help="Extract only one blog (debugging)")
    args = parser.parse_args()

    BLOGS_DIR.mkdir(parents=True, exist_ok=True)

    if args.check or args.check_all:
        all_errors = []
        if args.check_all:
            for bundle in sorted(OUT_DIR.iterdir()) if OUT_DIR.is_dir() else []:
                if bundle.is_dir():
                    all_errors.extend(check_one_blog(bundle.name))
        elif args.check:
            all_errors.extend(check_one_blog(args.check))
        if all_errors:
            for e in all_errors:
                print(f"  FAIL: {e}", file=sys.stderr)
            sys.exit(1)
        print("All checked blogs match their source markdown.")
        sys.exit(0)

    if not BLOGS_DIR.is_dir():
        print(f"No sources/blogs/ directory; nothing to extract.")
        sys.exit(0)

    total = 0
    with_code = 0
    for blog_md in sorted(BLOGS_DIR.glob("*.md")):
        if args.only and blog_md.stem != args.only:
            continue
        n, had_code = extract_one_blog(blog_md)
        total += 1
        if had_code:
            with_code += 1
            print(f"  {blog_md.stem}: extracted {n} code block(s)")
        else:
            print(f"  {blog_md.stem}: code_present: false (no fenced blocks)")

    print(f"\nProcessed {total} blog(s), {with_code} with extractable code.")


if __name__ == "__main__":
    main()
