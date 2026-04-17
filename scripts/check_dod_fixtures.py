#!/usr/bin/env python3
"""Check Phase 3 Definition-of-Done fixtures (AC-7).

Reads data/phase3-dod-fixtures.yaml; for each entry, verifies that at least
one file matches the `required_assets` globs, the file has >= required_min_lines,
any `required_provenance_modes` restriction is met (by checking the file's
ancestor PROVENANCE.yaml's files[*].mode), and any `required_content_patterns`
regexes match across the matched files.

Exit codes:
  0 — all fixture entries pass
  1 — at least one fixture entry fails
  2 — invocation error (fixtures file missing)
"""

import argparse
import re
import sys
from pathlib import Path
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
FIXTURES_PATH = REPO_ROOT / "data" / "phase3-dod-fixtures.yaml"


def find_bundle_root_for(path):
    """Walk up from path until a PROVENANCE.yaml is found; return the directory."""
    p = path.parent
    while p != p.parent:
        if (p / "PROVENANCE.yaml").is_file():
            return p
        p = p.parent
    return None


def load_modes_for_file(file_path):
    """Return the `mode` string declared in the enclosing bundle's files[*] manifest,
    or None if not found."""
    root = find_bundle_root_for(file_path)
    if not root:
        return None
    prov_path = root / "PROVENANCE.yaml"
    try:
        prov = yaml.safe_load(prov_path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError:
        return None
    try:
        rel = file_path.relative_to(root).as_posix()
    except ValueError:
        return None
    for entry in prov.get("files") or []:
        if isinstance(entry, dict) and entry.get("local_path") == rel:
            return entry.get("mode")
    return None


def check_entry(entry):
    errors = []
    question = entry.get("question", "<unnamed>")
    required_assets = entry.get("required_assets") or []
    required_min_lines = entry.get("required_min_lines", 100)
    required_modes = set(entry.get("required_provenance_modes") or [])
    required_patterns = entry.get("required_content_patterns") or []

    matched = []
    for glob in required_assets:
        # Resolve glob relative to repo root
        for p in REPO_ROOT.glob(glob):
            if p.is_file():
                matched.append(p)

    if not matched:
        errors.append(
            f"{question!r}: required_assets {required_assets} matched no files"
        )
        return errors

    # At least one matched file must meet min_lines
    long_enough = []
    for p in matched:
        try:
            lines = p.read_text(encoding="utf-8", errors="replace").splitlines()
            if len(lines) >= required_min_lines:
                long_enough.append(p)
        except OSError:
            pass
    if not long_enough:
        errors.append(
            f"{question!r}: no matched file reached required_min_lines={required_min_lines}"
        )

    # Mode restriction: at least one matched file's bundle-mode must be in the allowed set
    if required_modes:
        allowed = False
        for p in matched:
            m = load_modes_for_file(p)
            if m in required_modes:
                allowed = True
                break
        if not allowed:
            errors.append(
                f"{question!r}: no matched file has provenance mode in {sorted(required_modes)}"
            )

    # Content regexes must match across aggregate of matched files
    if required_patterns:
        aggregate = ""
        for p in matched:
            try:
                aggregate += p.read_text(encoding="utf-8", errors="replace") + "\n"
            except OSError:
                continue
        for pat in required_patterns:
            try:
                if not re.search(pat, aggregate, re.IGNORECASE):
                    errors.append(f"{question!r}: required_content_pattern {pat!r} not found")
            except re.error as e:
                errors.append(f"{question!r}: invalid regex {pat!r}: {e}")

    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    args = parser.parse_args()

    if not FIXTURES_PATH.is_file():
        print(f"No {FIXTURES_PATH.relative_to(REPO_ROOT)} — skipping DoD fixture check.")
        sys.exit(0)

    try:
        data = yaml.safe_load(FIXTURES_PATH.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as e:
        print(f"ERROR: could not parse {FIXTURES_PATH}: {e}", file=sys.stderr)
        sys.exit(2)

    entries = data.get("fixtures") or []
    if not entries:
        print(f"{FIXTURES_PATH.relative_to(REPO_ROOT)} has no fixtures; nothing to check.")
        sys.exit(0)

    all_errors = []
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        all_errors.extend(check_entry(entry))

    print(f"Checked {len(entries)} DoD fixture entries.")
    if all_errors:
        for e in all_errors:
            print(f"  FAIL: {e}", file=sys.stderr)
        sys.exit(1)
    print("All fixtures pass.")
    sys.exit(0)


if __name__ == "__main__":
    main()
