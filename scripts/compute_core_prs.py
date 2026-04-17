#!/usr/bin/env python3
"""Compute the deterministic Phase 3 core-PR set + CuTe DSL / Triton universes.

Sources of truth (union, deduplicated, sorted):
  A. Graph-closure of wiki/**.md frontmatter `sources:` that point to a PR ID.
  B. PR IDs referenced anywhere inside any sources/contests/**/*.md body.
  C. PRs in data/cute-dsl-universe.yaml that `captured: true` after applying
     the cute-dsl lane of data/inclusion-policy.yaml.
  D. PRs in data/triton-universe.yaml that `captured: true` after applying
     the triton lane of data/inclusion-policy.yaml.
  E. Additions from data/core-prs-allowlist.yaml (subtract exclusions).

Outputs (all written to data/):
  - core-prs.yaml        (the captured set; deterministic ordering; sha256)
  - cute-dsl-universe.yaml  (all cute-dsl PRs, captured or skipped + reason)
  - triton-universe.yaml    (all triton PRs,    captured or skipped + reason)

Re-running on an unchanged corpus produces byte-identical output files
(AC-1 deterministic regeneration check).
"""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCES = REPO_ROOT / "sources"
WIKI = REPO_ROOT / "wiki"
DATA = REPO_ROOT / "data"

PR_ID_RE = re.compile(r"pr-[a-z0-9\-]+-\d+")


def extract_frontmatter(md_path):
    try:
        text = md_path.read_text(encoding="utf-8")
    except OSError:
        return None, ""
    m = re.match(r"^---\s*\r?\n(.*?)\r?\n---\s*\r?\n(.*)", text, re.DOTALL)
    if not m:
        return None, text
    try:
        return yaml.safe_load(m.group(1)), m.group(2)
    except yaml.YAMLError:
        return None, m.group(2)


def load_all_prs():
    """Load the complete set of PR pages under sources/prs/.

    Returns a dict keyed by PR ID: {id: {frontmatter..., '_path': str}}.
    """
    prs = {}
    for md in sorted((SOURCES / "prs").rglob("PR-*.md")):
        fm, _ = extract_frontmatter(md)
        if not fm or "id" not in fm:
            continue
        rec = dict(fm)
        rec["_path"] = str(md.relative_to(REPO_ROOT))
        prs[fm["id"]] = rec
    return prs


def graph_closure_from_wiki():
    """Collect every PR ID referenced in any wiki/**.md frontmatter `sources:` list."""
    ids = set()
    for md in sorted(WIKI.rglob("*.md")):
        fm, _ = extract_frontmatter(md)
        if not fm:
            continue
        for sid in (fm.get("sources") or []):
            if isinstance(sid, str) and sid.startswith("pr-"):
                ids.add(sid)
    return ids


def contest_referenced_prs():
    """Collect every PR ID mentioned inside a sources/contests/**/*.md body."""
    ids = set()
    for md in sorted((SOURCES / "contests").rglob("*.md")):
        try:
            text = md.read_text(encoding="utf-8")
        except OSError:
            continue
        for match in PR_ID_RE.findall(text):
            ids.add(match)
    return ids


def path_matches_any(paths, globs):
    from fnmatch import fnmatch
    return any(fnmatch(p, g) for p in paths for g in globs)


def apply_cute_dsl_policy(policy, pr):
    """Return (captured: bool, skipped_reason: str|None)."""
    rules = policy.get("cute-dsl", {}) or {}
    langs = set(pr.get("languages") or [])
    tags = set(pr.get("tags") or [])
    changed_paths = pr.get("changed_paths") or []

    # Match: languages contains cute-dsl OR tags contains cute-dsl OR
    # changed_paths match any of the cute-dsl globs.
    cute_globs = []
    for crit in rules.get("capture_criteria", []):
        if isinstance(crit, dict) and "changed_paths_match" in crit:
            cute_globs.extend(crit["changed_paths_match"])
    matches_glob = path_matches_any(changed_paths, cute_globs) if cute_globs else False
    matches = "cute-dsl" in langs or "cute-dsl" in tags or matches_glob

    if not matches:
        return False, "not a cute-dsl PR"

    # Skip rule: docs/CHANGELOG/release_notes only
    skip_globs = []
    for crit in rules.get("skip_criteria", []):
        if isinstance(crit, dict) and "changed_paths_match_only" in crit:
            skip_globs.extend(crit["changed_paths_match_only"])
    if skip_globs and changed_paths:
        from fnmatch import fnmatch
        if all(any(fnmatch(p, g) for g in skip_globs) for p in changed_paths):
            return False, "documentation-only CuTe DSL PR"

    return True, None


def apply_triton_policy(policy, pr):
    """Return (captured: bool, skipped_reason: str|None)."""
    rules = policy.get("triton", {}) or {}
    langs = set(pr.get("languages") or [])
    if "triton" not in langs and "triton" not in set(pr.get("tags") or []):
        return False, "not a triton PR"

    archs = set(pr.get("architectures") or [])
    symptoms = set(pr.get("symptoms") or [])
    changed_paths = pr.get("changed_paths") or []
    desc = str(pr.get("description") or "").lower() + " " + str(pr.get("title") or "").lower()

    # Skip pure Hopper
    if archs and archs.issubset({"sm90", "sm90a"}):
        return False, "pure Hopper Triton (no SM100 relevance)"
    # Skip runtime-config-only
    if changed_paths:
        from fnmatch import fnmatch
        runtime_only_globs = ["**/config/**", "**/__init__.py"]
        if all(any(fnmatch(p, g) for g in runtime_only_globs) for p in changed_paths):
            return False, "runtime-config-only Triton PR"

    # Sub-scope matching
    # memory-bound-kernel
    if symptoms & {"memory-bound", "low-sm-utilization"}:
        return True, None
    # sm100-integration
    if "sm100" in archs:
        from fnmatch import fnmatch
        integ_globs = ["**/triton_kernels/**", "**/triton/**"]
        if any(fnmatch(p, g) for p in changed_paths for g in integ_globs):
            return True, None
    # backend-fallback (heuristic string match)
    for kw in ("fallback", "sm100 path", "cutlass is unavailable"):
        if kw in desc:
            return True, None

    return False, "Triton PR outside the three in-policy sub-scopes"


def dump_sorted(d, sort_keys=False):
    """Stable dump for reproducibility."""
    return yaml.dump(d, allow_unicode=True, sort_keys=sort_keys, default_flow_style=False)


def compute_sha256_of_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def build_universe(policy, all_prs, apply_fn):
    """Return list of {id, captured, skipped_reason?} for all PRs that the lane
    considers candidates."""
    entries = []
    for pid in sorted(all_prs.keys()):
        pr = all_prs[pid]
        captured, reason = apply_fn(policy, pr)
        if captured:
            entries.append({"id": pid, "captured": True})
        else:
            entries.append({"id": pid, "captured": False, "skipped_reason": reason})
    return entries


def build_cute_universe(policy, all_prs):
    """CuTe lane universe: iterate the full PR corpus (no prefilter) and record
    every PR that the policy has an opinion on.

    A PR belongs to the CuTe universe iff at least one of the capture criteria
    matches (language tag, tag, or changed_paths glob). We record whether the
    policy captured it or explicitly skipped it (e.g., docs-only). PRs that
    match no CuTe entry condition at all are NOT included in the universe —
    recording every one of the 460 PRs would dilute the lane's meaning.
    """
    entries = []
    rules = (policy.get("cute-dsl") or {})
    cute_globs = []
    for crit in rules.get("capture_criteria", []):
        if isinstance(crit, dict) and "changed_paths_match" in crit:
            cute_globs.extend(crit["changed_paths_match"])

    for pid in sorted(all_prs.keys()):
        pr = all_prs[pid]
        langs = set(pr.get("languages") or [])
        tags = set(pr.get("tags") or [])
        changed_paths = pr.get("changed_paths") or []
        path_match = path_matches_any(changed_paths, cute_globs) if cute_globs else False
        if not ("cute-dsl" in langs or "cute-dsl" in tags or path_match):
            continue  # not a CuTe candidate at all
        captured, reason = apply_cute_dsl_policy(policy, pr)
        if captured:
            entries.append({"id": pid, "captured": True})
        else:
            entries.append({"id": pid, "captured": False, "skipped_reason": reason})
    return entries


def filter_candidates(universe, predicate):
    """Return list of universe entries where predicate(pr) is True."""
    return [e for e in universe if predicate(e)]


def write_universe_file(path, entries, lane_name, captured_count, skipped_count):
    payload = {
        "lane": lane_name,
        "generated_by": "scripts/compute_core_prs.py",
        "total": len(entries),
        "captured": captured_count,
        "skipped": skipped_count,
        "prs": entries,
    }
    text = (
        f"## Auto-generated by scripts/compute_core_prs.py — DO NOT EDIT BY HAND.\n"
        f"## Re-run the script after any corpus change.\n\n"
        + dump_sorted(payload)
    )
    path.write_text(text, encoding="utf-8")


def main():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument(
        "--output-dir",
        default=str(DATA),
        help="Directory to write core-prs.yaml, cute-dsl-universe.yaml, and "
             "triton-universe.yaml into. Defaults to ./data. Used by "
             "scripts/verify_core_prs.py to regenerate into a temp dir "
             "without dirtying the working tree.",
    )
    args = parser.parse_args()
    out_dir = Path(args.output_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    policy_path = DATA / "inclusion-policy.yaml"
    if not policy_path.is_file():
        print("ERROR: data/inclusion-policy.yaml not found", file=sys.stderr)
        sys.exit(2)
    policy = yaml.safe_load(policy_path.read_text(encoding="utf-8")) or {}

    allowlist_path = DATA / "core-prs-allowlist.yaml"
    allowlist = {}
    if allowlist_path.is_file():
        allowlist = yaml.safe_load(allowlist_path.read_text(encoding="utf-8")) or {}

    all_prs = load_all_prs()

    # Per-lane universes.
    # CuTe lane: the policy admits three alternative entry conditions
    # (languages contains cute-dsl, tags contains cute-dsl, or changed_paths
    # match a CuTe glob). We therefore evaluate the full PR corpus against
    # the policy rather than prefiltering by tag/language — otherwise PRs
    # that only touch examples/cute/... tutorial paths would be invisible to
    # the lane even though the declared policy captures them.
    cute_entries = build_cute_universe(policy, all_prs)

    # Triton lane: still prefilter by language/tag since the policy's match
    # criteria are all gated on languages_contains triton. Triton PRs without
    # the language tag are not candidates.
    triton_candidates = {pid: pr for pid, pr in all_prs.items()
                         if "triton" in (pr.get("languages") or []) or "triton" in (pr.get("tags") or [])}
    triton_entries = build_universe(policy, triton_candidates, apply_triton_policy)

    cute_captured = {e["id"] for e in cute_entries if e["captured"]}
    triton_captured = {e["id"] for e in triton_entries if e["captured"]}

    # Core PR set: union of (graph closure, contest references, CuTe captured, Triton captured, allowlist additions)
    graph_ids = graph_closure_from_wiki() & set(all_prs.keys())
    contest_ids = contest_referenced_prs() & set(all_prs.keys())
    core = set()
    source_of = {}  # id -> first-seen source

    def add(pid, src):
        if pid in all_prs and pid not in core:
            core.add(pid)
            source_of[pid] = src

    for pid in sorted(graph_ids):
        add(pid, "wiki-graph-closure")
    for pid in sorted(contest_ids):
        if pid not in core:
            add(pid, "contest-reference")
    for pid in sorted(cute_captured):
        if pid not in core:
            add(pid, "cute-dsl-tutorial")
    for pid in sorted(triton_captured):
        if pid not in core:
            add(pid, "triton-in-policy")

    # Apply allowlist additions / exclusions
    additions = (allowlist.get("additions") or []) if isinstance(allowlist.get("additions"), list) else []
    for e in additions:
        if isinstance(e, dict) and "pr" in e:
            add(e["pr"], "allowlist")
    exclusions = set()
    for e in (allowlist.get("exclusions") or []) if isinstance(allowlist.get("exclusions"), list) else []:
        if isinstance(e, dict) and "pr" in e:
            exclusions.add(e["pr"])
    core -= exclusions
    for x in list(source_of):
        if x in exclusions:
            del source_of[x]

    # Build the core-prs.yaml payload
    prs_list = []
    for pid in sorted(core):
        prs_list.append({"id": pid, "source_of_inclusion": source_of[pid]})

    # Checksum is computed over the prs_list (deterministic-regeneration check)
    checksum_body = yaml.dump(prs_list, allow_unicode=True, sort_keys=False, default_flow_style=False)
    checksum = compute_sha256_of_text(checksum_body)

    from datetime import date
    core_payload = {
        "generated_by": "scripts/compute_core_prs.py",
        "generated_at": date.today().isoformat(),
        "sources": ["wiki-graph-closure", "contest-reference", "cute-dsl-tutorial", "triton-in-policy", "allowlist"],
        "total_captured": len(prs_list),
        "checksum_sha256": checksum,
        "prs": prs_list,
    }
    core_text = (
        "## Auto-generated by scripts/compute_core_prs.py — DO NOT EDIT BY HAND.\n"
        "## Use data/core-prs-allowlist.yaml to add or exclude PRs; then re-run the script.\n\n"
        + yaml.dump(core_payload, allow_unicode=True, sort_keys=False, default_flow_style=False)
    )
    (out_dir / "core-prs.yaml").write_text(core_text, encoding="utf-8")

    # Universe files
    write_universe_file(
        out_dir / "cute-dsl-universe.yaml",
        cute_entries,
        "cute-dsl",
        sum(1 for e in cute_entries if e["captured"]),
        sum(1 for e in cute_entries if not e["captured"]),
    )
    write_universe_file(
        out_dir / "triton-universe.yaml",
        triton_entries,
        "triton",
        sum(1 for e in triton_entries if e["captured"]),
        sum(1 for e in triton_entries if not e["captured"]),
    )

    # Summary to stdout
    print(f"core-prs.yaml: {len(prs_list)} PRs captured (checksum {checksum[:12]}...)")
    print(f"cute-dsl-universe.yaml: {len(cute_entries)} candidates "
          f"({sum(1 for e in cute_entries if e['captured'])} captured)")
    print(f"triton-universe.yaml: {len(triton_entries)} candidates "
          f"({sum(1 for e in triton_entries if e['captured'])} captured)")


if __name__ == "__main__":
    main()
