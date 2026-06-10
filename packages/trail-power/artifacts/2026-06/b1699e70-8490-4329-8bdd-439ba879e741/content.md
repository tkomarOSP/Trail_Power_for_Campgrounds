# Issue — Capella Fabric MCP: Write/Patch Capability + Author Identity on Commits

**Date:** 2026-06-10
**Type:** Capability Enhancement Request
**Status:** Partially Resolved / Amendment Open
**Priority:** High

---

## Background

The `capella-fabric` MCP currently supports browsing and exporting Capella models to YAML (read-only). This issue captures two related enhancements:

1. **Write/Patch Capability** — three new MCP tools to enable model write-back
2. **Author Identity Amendment** — author/committer identity on all patch commits

---

## Part 1 — Write/Patch Capability (Implemented)

### Goal

Add three new MCP tools to the existing `capella-fabric` MCP (port 8001) covering structural model changes, verification, and GitHub sync.

`py-capellambse >= 0.6` has a built-in declarative modeling API (`capellambse.decl`) that applies YAML patch documents to a live model object and persists via `model.save()`. The existing session (`clone + session.json`) already carries the git remote URL with embedded PAT, so pushing requires no extra credentials.

### New Tools

| Tool | Description |
|---|---|
| `apply_model_patch` | Apply a declarative YAML patch, save, and git-commit |
| `push_model_changes` | Push committed changes to the remote GitHub repo |
| `verify_model` | Scan a phase for common quality issues (missing names, unallocated functions) |

### Files to Modify

- `Capella_Fabric_Generator/capella_service.py` — add `apply_patch()` and helper functions
- `Capella_Fabric_Generator/git_service.py` — add `commit_changes()` and `push_changes()`
- `Capella_Fabric_Generator/mcp_server.py` — register 3 new `@mcp.tool()` endpoints

### Scope Convention for `apply_model_patch`

Limit creation to structure (components/entities), functions, and activities. Use `!uuid <uuid>` to target existing elements, `set:` to update properties, `extend:` to add children, and `promise_id:` / `!promise` for forward references within the same patch.

### Status

**Implemented and validated** — first live patch applied 2026-06-10, commit `4a95517d` on `master`. Renamed `Bat Power` → `Chg Power` on Cell 2 PA charge path exchange (UUID `25520ebc`). Both `apply_model_patch` and `push_model_changes` confirmed working. `verify_model` available but not yet exercised.

---

## Part 2 — Amendment: Author Identity on Patch Commits (Open)

### Problem

All commits made via `apply_model_patch` and `push_artifacts` currently carry the MCP server's default Git identity, not the identity of the engineer making the change. This reduces traceability and audit value of the Git history on both `master` (model changes) and `main` (artifact changes).

### Desired Behavior

Commits should reflect the actual engineer's identity:

```
Author:    Tony Komar <tony@trailpower.org>
Committer: SE Knowledge Partner (capella-fabric MCP)
```

### Proposed Solution

Expose optional `author_name` and `author_email` parameters on:
- `apply_model_patch` — for model change commits on `master`
- `push_artifacts` (artifact repo MCP) — for knowledge artifact commits on `main`

Pass these through to `git commit --author="Name <email>"` in the underlying `git_service.py` implementation.

### Workaround (interim)

Embed authorship in the commit message as a convention:
```
[Tony Komar] Fix exchange naming: Bat Power → Chg Power (PA layer)
```

### Files to Modify

- `Capella_Fabric_Generator/git_service.py` — add `author_name` and `author_email` args to `commit_changes()`
- `Capella_Fabric_Generator/mcp_server.py` — expose params on `apply_model_patch` tool signature
- Artifact repo MCP equivalent — same pattern for `push_artifacts`

### Status

**Open** — not yet implemented. Workaround (commit message attribution) available in the interim.
