#!/usr/bin/env python3
"""Validate YAML frontmatter in all source and wiki pages against schemas."""

import re
import sys
import yaml
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
SOURCES_DIR = REPO_ROOT / "sources"
WIKI_DIR = REPO_ROOT / "wiki"
DATA_DIR = REPO_ROOT / "data"

REPRO_ORDER = ["concept", "pseudocode", "snippet", "runnable", "benchmarked"]


def load_yaml_file(path):
    with open(path) as f:
        return yaml.safe_load(f)


def extract_frontmatter(filepath):
    """Extract YAML frontmatter from a markdown file."""
    with open(filepath) as f:
        content = f.read()
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return None
    try:
        return yaml.safe_load(match.group(1))
    except yaml.YAMLError as e:
        return {"_parse_error": str(e)}


def read_body(filepath):
    """Read the body (post-frontmatter) of a markdown file."""
    with open(filepath) as f:
        content = f.read()
    match = re.match(r'^---\s*\n.*?\n---\s*\n', content, re.DOTALL)
    if match:
        return content[match.end():]
    return content


def detect_page_type(filepath, fm):
    """Detect page type from filepath and frontmatter."""
    rel = filepath.relative_to(REPO_ROOT)
    parts = rel.parts

    if parts[0] == "sources":
        if parts[1] == "prs":
            return "source-pr"
        elif parts[1] == "docs":
            return "source-doc"
        elif parts[1] == "blogs":
            return "source-blog"
        elif parts[1] == "contests":
            return "source-contest"
    elif parts[0] == "wiki":
        t = fm.get("type", "")
        if t:
            return f"wiki-{t}"
        subdir = parts[1] if len(parts) > 1 else ""
        type_map = {
            "hardware": "wiki-hardware",
            "techniques": "wiki-technique",
            "patterns": "wiki-pattern",
            "kernels": "wiki-kernel",
            "languages": "wiki-language",
            "migration": "wiki-migration",
        }
        return type_map.get(subdir, "unknown")
    return "unknown"


def repro_at_least(level, minimum):
    if level not in REPRO_ORDER or minimum not in REPRO_ORDER:
        return False
    return REPRO_ORDER.index(level) >= REPRO_ORDER.index(minimum)


def has_fenced_code(body):
    """Check if body contains at least one fenced code block."""
    return bool(re.search(r'^```[^\n]*\n.*?\n```', body, re.MULTILINE | re.DOTALL))


def validate_file(filepath, schemas, valid_tags, all_source_ids):
    """Validate a single file. Returns list of error strings."""
    errors = []
    rel = filepath.relative_to(REPO_ROOT)

    fm = extract_frontmatter(filepath)
    if fm is None:
        errors.append(f"{rel}: missing YAML frontmatter")
        return errors
    if "_parse_error" in fm:
        errors.append(f"{rel}: YAML parse error: {fm['_parse_error']}")
        return errors

    page_type = detect_page_type(filepath, fm)
    if page_type == "unknown":
        errors.append(f"{rel}: unknown page type")
        return errors

    schema = schemas.get(page_type)
    if not schema:
        errors.append(f"{rel}: no schema defined for type '{page_type}'")
        return errors

    constraints = schema.get("constraints", {})

    # Check required fields
    for field in schema.get("required", []):
        if field not in fm or fm[field] is None:
            errors.append(f"{rel}: missing required field '{field}'")

    # Validate id_prefix
    id_prefix = constraints.get("id_prefix")
    if id_prefix and "id" in fm:
        if not str(fm["id"]).startswith(id_prefix):
            errors.append(f"{rel}: id '{fm['id']}' must start with '{id_prefix}'")

    # Build per-field vocabulary sets
    # "tags" is special: accepts any tag from any category
    all_valid = set()
    for category in valid_tags.values():
        if isinstance(category, list):
            all_valid.update(category)

    field_vocab = {
        "tags": all_valid,
        "techniques": set(valid_tags.get("techniques", [])),
        "hardware_features": set(valid_tags.get("hardware_features", [])),
        "kernel_types": set(valid_tags.get("kernel_types", [])),
        "languages": set(valid_tags.get("languages", [])),
    }

    # Check list type for all list-valued fields
    list_fields = ["tags", "techniques", "hardware_features", "kernel_types", "languages",
                    "architectures", "related", "sources", "symptoms", "candidate_techniques",
                    "prerequisites", "aliases"]
    for tag_field in list_fields:
        if tag_field in fm:
            if not isinstance(fm[tag_field], list):
                errors.append(f"{rel}: field '{tag_field}' must be a YAML list, got {type(fm[tag_field]).__name__}")
                continue

    # Validate each structured field against its own vocabulary
    for tag_field, vocab in field_vocab.items():
        if tag_field in fm and isinstance(fm[tag_field], list):
            for tag in fm[tag_field]:
                if tag not in vocab:
                    errors.append(f"{rel}: '{tag}' is not a valid {tag_field} value")

    # Validate architectures
    valid_archs = set(valid_tags.get("architectures", []))
    if "architectures" in fm and isinstance(fm["architectures"], list):
        for arch in fm["architectures"]:
            if arch not in valid_archs:
                errors.append(f"{rel}: unknown architecture '{arch}'")

    # Validate confidence
    valid_conf = set(valid_tags.get("confidence", []))
    if "confidence" in fm and fm["confidence"] not in valid_conf:
        errors.append(f"{rel}: invalid confidence '{fm['confidence']}'")

    # Validate reproducibility
    valid_repro = set(valid_tags.get("reproducibility", []))
    if "reproducibility" in fm:
        if fm["reproducibility"] not in valid_repro:
            errors.append(f"{rel}: invalid reproducibility '{fm['reproducibility']}'")

    # Check reproducibility minimum
    repro_min = constraints.get("reproducibility_minimum")
    if repro_min and "reproducibility" in fm:
        if not repro_at_least(fm["reproducibility"], repro_min):
            errors.append(
                f"{rel}: reproducibility '{fm['reproducibility']}' below "
                f"minimum '{repro_min}' for {page_type}"
            )

    # Validate source_category against schema constraints
    valid_cats = set(valid_tags.get("source_categories", []))
    if "source_category" in fm:
        cat = fm["source_category"]
        if cat not in valid_cats:
            errors.append(f"{rel}: invalid source_category '{cat}'")
        # Check schema-specific category constraints
        cat_constraint = constraints.get("source_category")
        if cat_constraint:
            allowed = cat_constraint if isinstance(cat_constraint, list) else [cat_constraint]
            if cat not in allowed:
                errors.append(f"{rel}: source_category '{cat}' not in allowed {allowed}")

    # Validate status enum
    status_constraint = constraints.get("status")
    if status_constraint and "status" in fm:
        allowed = status_constraint if isinstance(status_constraint, list) else [status_constraint]
        if fm["status"] not in allowed:
            errors.append(f"{rel}: status '{fm['status']}' not in {allowed}")

    # Check merge_sha_required_when
    if constraints.get("merge_sha_required_when") == "status == merged":
        if fm.get("status") == "merged" and not fm.get("merge_sha"):
            errors.append(f"{rel}: merge_sha required when status is 'merged'")

    # Check type field matches constraint
    if "type" in constraints and "type" in fm:
        if fm["type"] != constraints["type"]:
            errors.append(
                f"{rel}: type '{fm['type']}' does not match "
                f"expected '{constraints['type']}' for {page_type}"
            )

    # Check blackwell_relevance required for any wiki page with sm90 but not sm100
    # (Blackwell-first scope: Hopper content must justify its inclusion)
    if page_type.startswith("wiki-"):
        archs = set(fm.get("architectures", []) if isinstance(fm.get("architectures"), list) else [])
        hopper_archs = archs & {"sm90", "sm90a"}
        if hopper_archs and "blackwell_relevance" not in fm:
            errors.append(
                f"{rel}: page includes Hopper architecture {hopper_archs} but missing "
                f"'blackwell_relevance' (required by Blackwell-first scope)"
            )

    # Check performance_claims structure (including shape and numeric value)
    if "performance_claims" in fm and isinstance(fm["performance_claims"], list):
        for i, claim in enumerate(fm["performance_claims"]):
            if isinstance(claim, dict):
                for req in ["gpu", "dtype", "shape", "metric", "value", "source_id"]:
                    if req not in claim:
                        errors.append(f"{rel}: performance_claims[{i}] missing '{req}'")
                if "value" in claim and not isinstance(claim["value"], (int, float)):
                    errors.append(
                        f"{rel}: performance_claims[{i}].value must be numeric, "
                        f"got {type(claim['value']).__name__}: {claim['value']}"
                    )

    # Check wiki sources reference existing source ids
    if page_type.startswith("wiki-") and "sources" in fm and isinstance(fm["sources"], list):
        for src_id in fm["sources"]:
            if all_source_ids and src_id not in all_source_ids:
                errors.append(f"{rel}: references unknown source id '{src_id}'")

    # AC-9: Enforce evidence_basis for verified wiki pages
    if page_type.startswith("wiki-") and fm.get("confidence") == "verified":
        eb = fm.get("evidence_basis")
        if not eb or not isinstance(eb, list) or len(eb) == 0:
            errors.append(
                f"{rel}: confidence 'verified' requires non-empty 'evidence_basis' field"
            )
        else:
            eb_types = {entry.get("evidence_type") for entry in eb if isinstance(entry, dict)}
            if "official-doc" not in eb_types:
                errors.append(
                    f"{rel}: evidence_basis for 'verified' must include at least one "
                    f"'official-doc' entry (found: {eb_types})"
                )
            if "upstream-code" not in eb_types:
                errors.append(
                    f"{rel}: evidence_basis for 'verified' must include at least one "
                    f"'upstream-code' entry (found: {eb_types})"
                )
            # Cross-check evidence_basis source_ids against page sources
            page_sources = set(fm.get("sources", []))
            for entry in eb:
                if isinstance(entry, dict):
                    sid = entry.get("source_id", "")
                    if sid and sid not in page_sources:
                        errors.append(
                            f"{rel}: evidence_basis references '{sid}' "
                            f"not listed in page sources"
                        )

    # Check technique/kernel/language pages have fenced code
    if page_type in ("wiki-technique", "wiki-kernel", "wiki-language"):
        body = read_body(filepath)
        if not has_fenced_code(body):
            errors.append(f"{rel}: {page_type} page must contain fenced code block (reproducibility >= snippet)")

    return errors


def main():
    tags = load_yaml_file(DATA_DIR / "tags.yaml")
    schemas = load_yaml_file(DATA_DIR / "schemas.yaml")

    all_errors = []
    file_count = 0
    ids_seen = {}

    # First pass: collect all source IDs
    all_source_ids = set()
    for md_file in sorted(SOURCES_DIR.rglob("*.md")) if SOURCES_DIR.exists() else []:
        fm = extract_frontmatter(md_file)
        if fm and isinstance(fm, dict) and "id" in fm:
            all_source_ids.add(fm["id"])

    # Second pass: validate everything
    for search_dir in [SOURCES_DIR, WIKI_DIR]:
        if not search_dir.exists():
            continue
        for md_file in sorted(search_dir.rglob("*.md")):
            file_count += 1
            fm = extract_frontmatter(md_file)

            # Check for duplicate ids
            if fm and isinstance(fm, dict) and "id" in fm:
                fid = fm["id"]
                if fid in ids_seen:
                    all_errors.append(
                        f"{md_file.relative_to(REPO_ROOT)}: duplicate id '{fid}' "
                        f"(also in {ids_seen[fid]})"
                    )
                else:
                    ids_seen[fid] = str(md_file.relative_to(REPO_ROOT))

            errors = validate_file(md_file, schemas, tags, all_source_ids)
            all_errors.extend(errors)

    print(f"Validated {file_count} files ({len(all_source_ids)} source IDs collected)")
    if all_errors:
        print(f"\n{len(all_errors)} errors found:\n")
        for err in all_errors:
            print(f"  ERROR: {err}")
        sys.exit(1)
    else:
        print("All files valid.")
        sys.exit(0)


if __name__ == "__main__":
    main()
