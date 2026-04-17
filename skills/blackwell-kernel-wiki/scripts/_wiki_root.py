"""Shared wiki-root resolution for skill scripts.

Resolution order:
  1. BLACKWELL_WIKI_ROOT environment variable (explicit override)
  2. Autodetect: walk up from this script until a directory containing
     both `data/tags.yaml` and `wiki/` is found
  3. Autodetect from current working directory (same check)
  4. Hard error with a clear, actionable message

The first resolved path whose layout validates is returned. If none
validate we exit with an informative error describing the fix.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path


def _looks_like_wiki_root(p: Path) -> bool:
    return (p / "data" / "tags.yaml").is_file() and (p / "wiki").is_dir()


def _walk_up(start: Path):
    start = start.resolve()
    for candidate in [start, *start.parents]:
        yield candidate


def resolve_wiki_root() -> Path:
    # 1. env override
    env = os.environ.get("BLACKWELL_WIKI_ROOT")
    if env:
        p = Path(env).expanduser()
        if _looks_like_wiki_root(p):
            return p.resolve()
        print(
            f"ERROR: BLACKWELL_WIKI_ROOT={env!r} does not point at a valid "
            f"Blackwell kernel wiki (missing data/tags.yaml or wiki/).",
            file=sys.stderr,
        )
        sys.exit(2)

    # 2. walk up from script location (works for in-place install)
    script_dir = Path(__file__).resolve().parent
    for p in _walk_up(script_dir):
        if _looks_like_wiki_root(p):
            return p

    # 3. walk up from cwd (useful when running inside a checkout of the repo)
    for p in _walk_up(Path.cwd()):
        if _looks_like_wiki_root(p):
            return p

    print(
        "ERROR: Could not locate the Blackwell kernel wiki root.\n"
        "       Expected a directory containing `data/tags.yaml` and `wiki/`.\n"
        "       Fix: set the BLACKWELL_WIKI_ROOT environment variable, e.g.\n"
        "            export BLACKWELL_WIKI_ROOT=/path/to/blackwell-kernel-wiki",
        file=sys.stderr,
    )
    sys.exit(2)


WIKI_ROOT = resolve_wiki_root()
