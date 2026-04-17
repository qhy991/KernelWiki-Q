# blackwell-kernel-wiki — Claude Code Skill

A Claude Code skill for querying the Blackwell GPU kernel optimization knowledge base.

The skill package (SKILL.md + scripts + references) is self-contained, but **the data it queries is not** — the scripts operate over the surrounding `data/`, `wiki/`, `sources/`, `queries/` directories of the blackwell-kernel-wiki repository. Any install option that separates the skill directory from the data must point the scripts back to it via `BLACKWELL_WIKI_ROOT`.

## What This Skill Provides

- **SKILL.md** — when-to-use spec, frontmatter (name, description, argument-hint, allowed-tools), and navigation paths
- **scripts/query.py** — unified search across 545 pages (keyword + tag + repo + language + architecture + symptom filters; alias-aware)
- **scripts/get_page.py** — fetch any page by `id` or path; `--follow-sources` expands cited sources
- **scripts/grep_wiki.py** — regex text search across wiki bodies and source PR pages
- **references/primer.md** — topic map: hardware features, techniques, kernels, symptoms → canonical page IDs
- **references/schema.md** — condensed schema reference (page types, required fields, controlled vocabulary)
- **references/examples.md** — 10 worked query patterns with commands and synthesis templates

## Installation

### Option 1 — Run in place (recommended)

Use the skill directly from a checkout of this repository. No setup beyond `pip install -r requirements.txt`:

```bash
python3 skills/blackwell-kernel-wiki/scripts/query.py --tag nvfp4 --type kernel --compact
```

The scripts auto-detect the wiki root by walking up the filesystem.

### Option 2 — Project-local skill

Claude Code auto-detects skills in `.claude/skills/` or `skills/` at the project root. This repository already satisfies that layout, so no copying is needed when you're working inside the checkout.

### Option 3 — User-wide install (requires extra config)

To make the skill available across projects, symlink the skill directory into `~/.claude/skills/` and export the wiki root:

```bash
# Symlink is preferred over copy — it stays in sync with repo updates
ln -s "$(pwd)/skills/blackwell-kernel-wiki" ~/.claude/skills/blackwell-kernel-wiki

# Tell the scripts where the data lives (required when the skill dir is separated from the repo)
export BLACKWELL_WIKI_ROOT="$(pwd)"
```

`cp -r` also works but the scripts still need `BLACKWELL_WIKI_ROOT` to find `data/tags.yaml`, `wiki/`, `sources/`. Plain copy without the env var will fail with a clear error from the scripts — they no longer silently fall back to `Path.cwd()`-unrelated paths.

## Root Resolution Precedence

All three scripts resolve the wiki root in this order:

1. `BLACKWELL_WIKI_ROOT` environment variable (explicit override).
2. Walk upward from the script's own directory looking for a valid root (`data/tags.yaml` + `wiki/`).
3. Walk upward from the current working directory with the same check.
4. Exit with a clear error telling you to set `BLACKWELL_WIKI_ROOT`.

If `BLACKWELL_WIKI_ROOT` is set but points somewhere invalid, the scripts refuse to continue rather than silently running against a wrong location.

## Dependencies

Pure Python 3 + PyYAML. From the repo root:

```bash
pip install -r requirements.txt
```

## Quick Smoke Test

From inside a checkout of the repo:

```bash
# Should list 4 NVFP4 kernel pages (nvfp4-gemm, nvfp4-gemv, gated-dual-gemm, grouped-gemm)
python3 skills/blackwell-kernel-wiki/scripts/query.py --tag nvfp4 --type kernel --compact

# Should print FlashAttention-4 frontmatter (no path header)
python3 skills/blackwell-kernel-wiki/scripts/get_page.py kernel-flash-attention-4 --frontmatter-only

# Should find files mentioning tcgen05.fence across wiki + sources
python3 skills/blackwell-kernel-wiki/scripts/grep_wiki.py "tcgen05\\.fence" --files-only

# Invalid regex produces a clean error, not a traceback
python3 skills/blackwell-kernel-wiki/scripts/grep_wiki.py "[" ; echo "exit=$?"
```

Also verify the env-override path from outside the repo:

```bash
cd /tmp
BLACKWELL_WIKI_ROOT=/path/to/blackwell-kernel-wiki \
  python3 /path/to/blackwell-kernel-wiki/skills/blackwell-kernel-wiki/scripts/query.py \
  --tag tcgen05 --compact
```

## How Claude Should Use This Skill

1. Read `SKILL.md` to decide when to engage (see "When To Use This Skill" and the negative triggers).
2. For broad questions, open `references/primer.md` first — it resolves most questions without further file reads.
3. For natural-language questions, use `scripts/query.py "<keywords>"` (alias-aware) or with `--tag`/`--type`/`--repo` filters.
4. Fetch specific pages via `scripts/get_page.py <id>` and cite them by ID + path.
5. Follow `sources:` IDs via `--follow-sources` for primary evidence; respect `confidence` levels.
6. Report performance claims with all six fields (`gpu`, `dtype`, `shape`, `metric`, `value`, `source_id`).
