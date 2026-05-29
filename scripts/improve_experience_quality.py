#!/usr/bin/env python3
"""Improve quality of KernelWiki experience pages by re-reading source JSON."""

import argparse
import hashlib
import json
import re
import sys
import yaml
from pathlib import Path


def wiki_id_to_source_id(wiki_id):
    """Reverse the sanitize_id transform: exp-foo-bar → exp_foo_bar."""
    if wiki_id.startswith("exp-"):
        return "exp_" + wiki_id[4:].replace("-", "_")
    return wiki_id.replace("-", "_")


def build_source_index(source_root):
    """Build a dict mapping source_id → JSON file path."""
    index = {}
    scan_dirs = [
        source_root / "library_experiences",
        source_root / "kerneldataset_imports",
        source_root / "kerneldataset_llm_v2",
        source_root / "kerneldataset_llm",
    ]
    for d in scan_dirs:
        if not d.exists():
            continue
        for jf in d.rglob("*.json"):
            if jf.name in ("index.json",) or jf.name.startswith("_"):
                continue
            source_id = jf.stem
            if source_id not in index:
                index[source_id] = jf

    curated_dir = source_root / "curated_datasets"
    if curated_dir.exists():
        for jsonl_file in curated_dir.glob("*.jsonl"):
            with open(jsonl_file, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    pointer = json.loads(line)
                    sp = pointer.get("source_path", "")
                    if sp:
                        full = source_root / sp
                        if full.exists():
                            sid = full.stem
                            if sid not in index:
                                index[sid] = full
    return index


def load_source_json(path):
    """Load and return source JSON data."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def parse_page(filepath):
    """Parse a wiki page into (frontmatter_dict, body_string, raw_text)."""
    text = filepath.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, None, text
    fm = yaml.safe_load(parts[1])
    body = parts[2].lstrip("\n")
    return fm, body, text


def write_page(filepath, fm, body):
    """Write frontmatter + body back to file."""
    fm_yaml = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
    content = f"---\n{fm_yaml}---\n\n{body}"
    filepath.write_text(content, encoding="utf-8")


def is_bad_title(title):
    """Check if a title needs improvement."""
    if not title:
        return True
    if title == "unknown":
        return True
    if re.match(r"^exp-[a-z0-9-]+$", title):
        return True
    if title.startswith("exp_"):
        return True
    if title.startswith("## "):
        return True
    return False


def synthesize_title(fm, body, source):
    """Generate a descriptive title from available data."""
    if source:
        ctx = source.get("context", {})
        task_name = ctx.get("task_name") or ""
        summary = ctx.get("summary") or ""

        if task_name and len(task_name) > 15 and not task_name.startswith("exp_"):
            if not re.match(r"^[a-z0-9_]+$", task_name):
                return task_name[:120]

        if summary and len(summary) > 15:
            return summary[:120]

    sol_line = extract_solution_first_line(body)
    if sol_line and len(sol_line) > 20:
        title = sol_line[:80]
        if not title[0].isupper():
            title = title[0].upper() + title[1:]
        return title

    if source:
        desc = source.get("challenge", {}).get("description") or ""
        if desc and len(desc) > 20:
            first_sent = desc.split(". ")[0].split(", ")[0]
            if len(first_sent) > 15:
                return first_sent[:80]

        rag = source.get("rag_text", "")
        if rag:
            challenge_line = extract_rag_field(rag, "Challenge")
            if challenge_line and len(challenge_line) > 20:
                return challenge_line[:80]

    kernel_types = fm.get("kernel_types", [])
    exp_type = fm.get("experience_type", "")
    if kernel_types and exp_type:
        kt = kernel_types[0].replace("-", " ")
        first_lesson = extract_first_lesson_phrase(body)
        if first_lesson:
            return f"{kt.title()} {exp_type}: {first_lesson}"[:80]
        return f"{kt.title()} kernel {exp_type}"

    return None


def extract_solution_first_line(body):
    """Extract the first text line after ## Solution."""
    lines = body.split("\n")
    for i, line in enumerate(lines):
        if line.strip().startswith("## Solution"):
            for j in range(i + 1, min(i + 5, len(lines))):
                candidate = lines[j].strip()
                if candidate and not candidate.startswith("#"):
                    return candidate
    return None


def extract_first_lesson_phrase(body):
    """Extract a short phrase from the first Key Lesson."""
    lines = body.split("\n")
    for i, line in enumerate(lines):
        if line.strip().startswith("## Key Lessons"):
            for j in range(i + 1, min(i + 5, len(lines))):
                candidate = lines[j].strip()
                if candidate.startswith("- "):
                    phrase = candidate[2:].split(" — ")[0].split("; ")[0]
                    return phrase[:60]
    return None


def extract_rag_field(rag_text, field_name):
    """Extract a field value from structured rag_text."""
    for line in rag_text.split("\n"):
        if line.startswith(f"{field_name}: "):
            return line[len(field_name) + 2:].strip()
        if line.startswith(f"{field_name}:"):
            return line[len(field_name) + 1:].strip()
    return None


def extract_challenge_text(source):
    """Extract challenge text from source JSON."""
    ch = source.get("challenge", {})
    desc = ch.get("description") or ""
    if desc:
        return desc
    problem = ch.get("problem") or ""
    if problem:
        return problem
    rag = source.get("rag_text", "")
    if rag:
        return extract_rag_field(rag, "Challenge") or ""
    return ""


def extract_speedup(source):
    """Extract speedup from performance_claim."""
    pc = source.get("solution", {}).get("performance_claim") or ""
    if not pc:
        return None
    match = re.match(r"([\d.]+)x", pc)
    if match:
        return f"{match.group(1)}x"
    return None


def body_has_section(body, section_name):
    """Check if body contains a markdown section."""
    return f"## {section_name}" in body or f"### {section_name}" in body


def insert_challenge_section(body, challenge_text):
    """Insert ## Challenge before ## Solution in body."""
    lines = body.split("\n")
    insert_idx = None
    for i, line in enumerate(lines):
        if line.strip().startswith("## Solution"):
            insert_idx = i
            break

    challenge_block = f"## Challenge\n\n{challenge_text}\n\n"
    if insert_idx is not None:
        lines.insert(insert_idx, challenge_block)
        return "\n".join(lines)
    else:
        return challenge_block + body


def insert_results_section(body, speedup_str):
    """Insert ## Results section before ## Key Lessons."""
    lines = body.split("\n")
    insert_idx = None
    for i, line in enumerate(lines):
        if line.strip().startswith("## Key Lessons"):
            insert_idx = i
            break

    results_block = f"## Results\n\n- **speedup**: {speedup_str}\n\n"
    if insert_idx is not None:
        lines.insert(insert_idx, results_block)
        return "\n".join(lines)
    else:
        return body.rstrip("\n") + "\n\n" + results_block


def insert_code_snippet(body, code):
    """Insert ### Implementation code block after ## Solution section."""
    lines = body.split("\n")
    sol_end = None
    in_solution = False
    for i, line in enumerate(lines):
        if line.strip().startswith("## Solution"):
            in_solution = True
            continue
        if in_solution and line.strip().startswith("## "):
            sol_end = i
            break
    if sol_end is None:
        for i, line in enumerate(lines):
            if line.strip().startswith("## Key Lessons") or line.strip().startswith("## Results"):
                sol_end = i
                break

    code_block = f"### Implementation\n\n```cuda\n{code.rstrip()}\n```\n\n"
    if sol_end is not None:
        lines.insert(sol_end, code_block)
        return "\n".join(lines)
    return body.rstrip("\n") + "\n\n" + code_block


def insert_key_changes(body, key_changes):
    """Insert key_changes as a sub-list under ## Solution."""
    if not key_changes or not isinstance(key_changes, list):
        return body
    changes_text = "\n".join(f"- {c}" for c in key_changes if isinstance(c, str) and len(c) > 10)
    if not changes_text:
        return body

    lines = body.split("\n")
    sol_end = None
    in_solution = False
    for i, line in enumerate(lines):
        if line.strip().startswith("## Solution"):
            in_solution = True
            continue
        if in_solution and line.strip().startswith("## "):
            sol_end = i
            break

    insert_block = f"\n### Key Changes\n\n{changes_text}\n\n"
    if sol_end is not None:
        lines.insert(sol_end, insert_block)
        return "\n".join(lines)
    return body.rstrip("\n") + "\n" + insert_block


def remove_body_title_echo(body, title):
    """Remove the title echoed as the first line of body (common in bad conversions)."""
    lines = body.split("\n")
    if lines and lines[0].strip() == title:
        return "\n".join(lines[1:]).lstrip("\n")
    if lines and lines[0].strip() == "unknown":
        return "\n".join(lines[1:]).lstrip("\n")
    return body


def dedup_pages(exp_dir):
    """Find and remove content-duplicate pages. Returns list of deleted paths."""
    pages = list(exp_dir.glob("*.md"))
    hash_groups = {}
    for p in pages:
        text = p.read_text(encoding="utf-8")
        parts = text.split("---", 2)
        if len(parts) < 3:
            continue
        body = parts[2].strip()
        h = hashlib.md5(body.encode()).hexdigest()
        if h not in hash_groups:
            hash_groups[h] = []
        hash_groups[h].append(p)

    deleted = []
    for h, group in hash_groups.items():
        if len(group) <= 1:
            continue
        scored = []
        for p in group:
            fm, _, _ = parse_page(p)
            title = fm.get("title", "") if fm else ""
            score = 0
            if not is_bad_title(title):
                score += 10
            if fm and fm.get("confidence") == "source-reported":
                score += 5
            if fm and fm.get("reproducibility") == "snippet":
                score += 3
            scored.append((score, p))
        scored.sort(key=lambda x: -x[0])
        keep = scored[0][1]
        for _, p in scored[1:]:
            deleted.append(p)
    return deleted


def main():
    parser = argparse.ArgumentParser(
        description="Improve quality of KernelWiki experience pages"
    )
    parser.add_argument("--source", required=True,
                        help="Path to KernelOwl knowledge/ directory")
    parser.add_argument("--experiences", required=True,
                        help="Path to KernelWiki sources/experiences/ directory")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview changes without writing files")
    parser.add_argument("--skip-dedup", action="store_true",
                        help="Skip duplicate removal step")
    parser.add_argument("--only-titles", action="store_true",
                        help="Only fix titles, skip other enrichments")
    args = parser.parse_args()

    source_root = Path(args.source)
    exp_dir = Path(args.experiences)

    if not source_root.exists():
        print(f"ERROR: source directory not found: {source_root}")
        sys.exit(1)
    if not exp_dir.exists():
        print(f"ERROR: experiences directory not found: {exp_dir}")
        sys.exit(1)

    print("Building source JSON index...")
    source_index = build_source_index(source_root)
    print(f"  Indexed {len(source_index)} source JSON files")

    pages = sorted(exp_dir.glob("*.md"))
    print(f"  Found {len(pages)} experience pages\n")

    stats = {
        "total": len(pages),
        "titles_fixed": 0,
        "challenges_added": 0,
        "speedups_added": 0,
        "snippets_added": 0,
        "key_changes_added": 0,
        "body_cleaned": 0,
        "source_not_found": 0,
        "duplicates_removed": 0,
    }

    if not args.skip_dedup and not args.only_titles:
        print("Step 0: Removing content duplicates...")
        deleted = dedup_pages(exp_dir)
        stats["duplicates_removed"] = len(deleted)
        if args.dry_run:
            print(f"  Would delete {len(deleted)} duplicate pages")
            for d in deleted[:5]:
                print(f"    {d.name}")
            if len(deleted) > 5:
                print(f"    ... and {len(deleted) - 5} more")
        else:
            for d in deleted:
                d.unlink()
                print(f"  Deleted: {d.name}")
        pages = sorted(exp_dir.glob("*.md"))
        print(f"  {len(pages)} pages remaining\n")

    print("Enriching pages...")
    for i, page_path in enumerate(pages):
        fm, body, raw = parse_page(page_path)
        if fm is None or body is None:
            continue

        wiki_id = fm.get("id", page_path.stem)
        source_id = wiki_id_to_source_id(wiki_id)
        source_path = source_index.get(source_id)
        source = None
        if source_path:
            try:
                source = load_source_json(source_path)
            except Exception:
                pass

        if not source:
            stats["source_not_found"] += 1

        changed = False
        title = str(fm.get("title", ""))

        if is_bad_title(title):
            new_title = synthesize_title(fm, body, source)
            if new_title and new_title != title:
                fm["title"] = new_title
                stats["titles_fixed"] += 1
                changed = True

        body = remove_body_title_echo(body, title)
        if body != (raw.split("---", 2)[2].lstrip("\n") if len(raw.split("---", 2)) >= 3 else ""):
            stats["body_cleaned"] += 1
            changed = True

        if args.only_titles:
            if changed and not args.dry_run:
                write_page(page_path, fm, body)
            continue

        if not body_has_section(body, "Challenge") and source:
            challenge_text = extract_challenge_text(source)
            if challenge_text and len(challenge_text) > 10:
                body = insert_challenge_section(body, challenge_text)
                stats["challenges_added"] += 1
                changed = True

        if not fm.get("speedup") and source:
            speedup = extract_speedup(source)
            if speedup:
                fm["speedup"] = speedup
                if not body_has_section(body, "Results"):
                    pc = source.get("solution", {}).get("performance_claim", "")
                    body = insert_results_section(body, pc or speedup)
                stats["speedups_added"] += 1
                changed = True

        if fm.get("reproducibility") == "concept" and source and not args.only_titles:
            code = source.get("solution", {}).get("code_after") or ""
            if 50 < len(code) < 3000 and not body_has_section(body, "Implementation"):
                body = insert_code_snippet(body, code)
                fm["reproducibility"] = "snippet"
                stats["snippets_added"] += 1
                changed = True

        if source and not args.only_titles:
            kc = source.get("solution", {}).get("key_changes")
            if kc and isinstance(kc, list) and not body_has_section(body, "Key Changes"):
                old_body = body
                body = insert_key_changes(body, kc)
                if body != old_body:
                    stats["key_changes_added"] += 1
                    changed = True

        if changed and not args.dry_run:
            write_page(page_path, fm, body)

        if (i + 1) % 500 == 0:
            print(f"  Processed {i + 1}/{len(pages)}...")

    print(f"\n{'DRY RUN ' if args.dry_run else ''}Summary:")
    print(f"  Total pages processed: {stats['total']}")
    print(f"  Duplicates removed: {stats['duplicates_removed']}")
    print(f"  Titles fixed: {stats['titles_fixed']}")
    print(f"  Challenge sections added: {stats['challenges_added']}")
    print(f"  Speedup data added: {stats['speedups_added']}")
    print(f"  Code snippets added: {stats['snippets_added']}")
    print(f"  Key changes added: {stats['key_changes_added']}")
    print(f"  Body title echoes cleaned: {stats['body_cleaned']}")
    print(f"  Source JSON not found: {stats['source_not_found']}")


if __name__ == "__main__":
    main()
