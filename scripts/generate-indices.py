#!/usr/bin/env python3
"""Generate query index pages from YAML frontmatter in sources/ and wiki/."""

import re
import yaml
from pathlib import Path
from collections import defaultdict

REPO_ROOT = Path(__file__).parent.parent
SOURCES_DIR = REPO_ROOT / "sources"
WIKI_DIR = REPO_ROOT / "wiki"
QUERIES_DIR = REPO_ROOT / "queries"


def extract_frontmatter(filepath):
    with open(filepath) as f:
        content = f.read()
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return None
    try:
        return yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None


def qlink(path):
    """Make a link relative from the queries/ directory."""
    return f"../{path}"


def load_valid_languages():
    """Load valid language tags from data/tags.yaml."""
    tags_path = REPO_ROOT / "data" / "tags.yaml"
    if tags_path.exists():
        with open(tags_path) as f:
            return set(yaml.safe_load(f).get("languages", []))
    return set()


def collect_all_pages():
    pages = []
    for search_dir in [SOURCES_DIR, WIKI_DIR]:
        if not search_dir.exists():
            continue
        for md_file in sorted(search_dir.rglob("*.md")):
            fm = extract_frontmatter(md_file)
            if fm and isinstance(fm, dict):
                fm["_path"] = str(md_file.relative_to(REPO_ROOT))
                fm["_dir"] = str(search_dir.relative_to(REPO_ROOT))
                pages.append(fm)
    return pages


def generate_by_problem(pages):
    lines = [
        "# Query: By Problem / Symptom",
        "",
        "> Auto-generated. Do not edit manually.",
        "",
        "| Symptom | Pattern Page | Candidate Techniques | Sources |",
        "|---------|-------------|---------------------|---------|",
    ]
    for p in sorted(
        (p for p in pages if p.get("type") == "pattern"),
        key=lambda x: x.get("title", ""),
    ):
        symptoms = ", ".join(p.get("symptoms", []))
        title = p.get("title", "Untitled")
        path = qlink(p["_path"])
        techniques = ", ".join(p.get("candidate_techniques", []))
        src_count = len(p.get("sources", []))
        lines.append(f"| {symptoms} | [{title}]({path}) | {techniques} | {src_count} sources |")
    return "\n".join(lines) + "\n"


def generate_by_technique(pages):
    lines = [
        "# Query: By Technique",
        "",
        "> Auto-generated. Do not edit manually.",
        "",
        "| Technique | Tags | Architectures | Confidence | Reproducibility | Sources |",
        "|-----------|------|--------------|------------|-----------------|---------|",
    ]
    for t in sorted(
        (p for p in pages if p.get("type") == "technique"),
        key=lambda x: x.get("title", ""),
    ):
        title = t.get("title", "Untitled")
        path = qlink(t["_path"])
        tags = ", ".join(t.get("tags", [])[:4])
        archs = ", ".join(t.get("architectures", []))
        conf = t.get("confidence", "")
        repro = t.get("reproducibility", "")
        src_count = len(t.get("sources", []))
        lines.append(f"| [{title}]({path}) | {tags} | {archs} | {conf} | {repro} | {src_count} |")
    return "\n".join(lines) + "\n"


def generate_by_hardware_feature(pages):
    lines = [
        "# Query: By Hardware Feature",
        "",
        "> Auto-generated. Do not edit manually.",
        "",
    ]
    tags_path = REPO_ROOT / "data" / "tags.yaml"
    hw_tag_set = set()
    if tags_path.exists():
        with open(tags_path) as f:
            hw_tag_set = set(yaml.safe_load(f).get("hardware_features", []))

    feature_pages = defaultdict(list)
    for p in pages:
        for feat in p.get("hardware_features", []):
            feature_pages[feat].append(p)
        for tag in p.get("tags", []):
            if tag in hw_tag_set:
                feature_pages[tag].append(p)

    # Add dedicated hardware pages under their canonical tags (from tags field)
    hw_pages = [p for p in pages if p.get("type") == "hardware"]
    for hp in hw_pages:
        for tag in hp.get("tags", []):
            if tag in hw_tag_set and hp not in feature_pages.get(tag, []):
                feature_pages[tag].append(hp)

    lines.append("| Feature | Related Pages |")
    lines.append("|---------|--------------|")
    for feat in sorted(feature_pages.keys()):
        page_links = []
        seen = set()
        for p in feature_pages[feat]:
            pid = p.get("id", p.get("_path", ""))
            if pid not in seen:
                seen.add(pid)
                title = p.get("title", pid)
                path = qlink(p["_path"])
                page_links.append(f"[{title}]({path})")
        lines.append(f"| `{feat}` | {', '.join(page_links)} |")
    return "\n".join(lines) + "\n"


def generate_by_repo(pages):
    lines = [
        "# Query: By Repository",
        "",
        "> Auto-generated. Do not edit manually.",
        "",
    ]
    repos = defaultdict(list)
    for p in pages:
        if "repo" in p and "pr" in p:
            repos[p["repo"]].append(p)

    for repo in sorted(repos.keys()):
        prs = sorted(repos[repo], key=lambda x: x.get("date", ""), reverse=True)
        # Stable anchor: repo slug without count (so index.md links don't break)
        slug = repo.lower().replace("/", "")
        lines.append(f"## {repo}")
        lines.append(f"<!-- anchor: {slug} -->")
        lines.append(f"{len(prs)} PRs")
        lines.append("")
        lines.append("| PR | Title | Date | Techniques | Tags |")
        lines.append("|-----|-------|------|------------|------|")
        for pr in prs:
            pr_num = pr.get("pr", "?")
            title = pr.get("title", "Untitled")
            date = pr.get("date", "")
            path = qlink(pr["_path"])
            techniques = ", ".join(pr.get("techniques", [])[:3])
            tags = ", ".join(pr.get("tags", [])[:3])
            lines.append(f"| [#{pr_num}]({path}) | {title} | {date} | {techniques} | {tags} |")
        lines.append("")
    return "\n".join(lines) + "\n"


def generate_by_kernel_type(pages):
    lines = [
        "# Query: By Kernel Type",
        "",
        "> Auto-generated. Do not edit manually.",
        "",
        "| Kernel Type | Pages |",
        "|-------------|-------|",
    ]
    type_pages = defaultdict(list)
    for p in pages:
        for kt in p.get("kernel_types", []):
            type_pages[kt].append(p)

    for kt in sorted(type_pages.keys()):
        page_links = []
        seen = set()
        for p in type_pages[kt]:
            pid = p.get("id", p.get("_path", ""))
            if pid not in seen:
                seen.add(pid)
                title = p.get("title", pid)
                path = qlink(p["_path"])
                page_links.append(f"[{title}]({path})")
        lines.append(f"| `{kt}` | {', '.join(page_links)} |")
    return "\n".join(lines) + "\n"


def generate_by_language(pages):
    lines = [
        "# Query: By Language / DSL",
        "",
        "> Auto-generated. Do not edit manually.",
        "",
    ]
    valid_langs = load_valid_languages()

    # Map: canonical language tag -> {guide: page, consumers: [pages]}
    lang_data = {}
    for lang in sorted(valid_langs):
        lang_data[lang] = {"guide": None, "consumers": []}

    # Find dedicated language guide pages
    for p in pages:
        if p.get("type") == "language":
            lang_id = p.get("id", "")
            lang_tag = lang_id.replace("lang-", "") if lang_id.startswith("lang-") else ""
            if lang_tag in lang_data:
                lang_data[lang_tag]["guide"] = p

    # Find consumer pages (pages that use each language)
    for p in pages:
        if p.get("type") != "language":
            for lang in p.get("languages", []):
                if lang in lang_data:
                    lang_data[lang]["consumers"].append(p)

    lines.append("| Language | Guide | Related Pages |")
    lines.append("|----------|-------|--------------|")

    for lang in sorted(lang_data.keys()):
        data = lang_data[lang]
        if not data["guide"] and not data["consumers"]:
            continue
        guide_link = ""
        if data["guide"]:
            g = data["guide"]
            guide_link = f"[{g.get('title', lang)}]({qlink(g['_path'])})"
        related = []
        seen = set()
        for p in data["consumers"]:
            pid = p.get("id", p.get("_path", ""))
            if pid not in seen:
                seen.add(pid)
                related.append(f"[{p.get('title', pid)}]({qlink(p['_path'])})")
        lines.append(f"| `{lang}` | {guide_link} | {', '.join(related)} |")

    return "\n".join(lines) + "\n"


def main():
    QUERIES_DIR.mkdir(exist_ok=True)
    pages = collect_all_pages()
    print(f"Collected {len(pages)} pages from sources/ and wiki/")

    generators = {
        "by-problem.md": generate_by_problem,
        "by-technique.md": generate_by_technique,
        "by-hardware-feature.md": generate_by_hardware_feature,
        "by-repo.md": generate_by_repo,
        "by-kernel-type.md": generate_by_kernel_type,
        "by-language.md": generate_by_language,
    }

    for filename, gen_func in generators.items():
        content = gen_func(pages)
        outpath = QUERIES_DIR / filename
        outpath.write_text(content)
        print(f"  Generated {outpath.relative_to(REPO_ROOT)}")

    print("Done.")


if __name__ == "__main__":
    main()
