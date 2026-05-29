---
id: exp-r-20260529-0004-mcp-allowed-dirs-bind-mount
title: MCP filesystem server rejects /home/ paths when allowed_dirs only contains
  /data/ bind-mount spelling
experience_type: repair
source_category: agent-experiment
architectures:
- sm90
tags:
- attention
kernel_types:
- attention
languages:
- cuda-cpp
captured_at: '2026-05-29'
confidence: inferred
reproducibility: concept
---

## Key Lessons

- On bind-mount machines (/home/ <-> /data/), MCP filesystem server needs BOTH path spellings in allowed_dirs — string prefix comparison cannot see through bind mounts
- os.path.samefile() can fail silently (OSError caught) — always have a stat-based (st_dev, st_ino) fallback for bind-mount detection
- Run mirror detection on BOTH raw and resolved paths — if resolve() canonicalizes one spelling, you need to detect mirrors from the other direction too
- When MCP filesystem denials occur during autoresearch, check allowed_dirs list for missing bind-mount spellings before blaming the agent's path choice
- The Python adapter rewrites paths via resolve(), but the MCP server validates against its startup args — both must be correct
