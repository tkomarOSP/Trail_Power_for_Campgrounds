# Observation — Multi-Agent Workflow Pattern Emerging

**Date:** 2026-06-10
**Observer:** SE Knowledge Partner
**Status:** Informational — early pattern, worth tracking

---

## Observation

A natural multi-agent workflow pattern is emerging on the Trail Power for Campgrounds program, with two Claude instances operating in complementary roles under human direction.

## Pattern Description

| Agent | Context | Primary Role |
|---|---|---|
| SE Knowledge Partner (Claude in chat) | claude.ai conversation | SE reasoning, model querying, artifact management, knowledge capture, procurement analysis |
| Claude Code | VS Code / terminal | Direct file editing, Python implementation, MCP service development, Git operations |

The two agents share the same underlying model (Claude) but operate in different tool environments with different strengths. The human engineer (Tony) acts as the coordinator — assigning work packages to the appropriate capability and integrating the outputs.

## Division of Labor Observed

In today's session this played out concretely:

- **SE Knowledge Partner** identified the author identity gap in `apply_model_patch`, reasoned about the engineering implications, and captured the requirement as a formal issue artifact with implementation guidance
- **Claude Code** is implementing the actual `git_service.py` and `mcp_server.py` changes to resolve it

Neither agent could do the other's job as effectively in their respective contexts. Claude Code has direct filesystem and terminal access; the SE Knowledge Partner has MCP tool access to the Capella model and artifact repository.

## Why This Is Significant

This is a practical example of multi-agent MBSE tooling — not a theoretical architecture. Two AI agents with different capabilities are contributing to the same engineering program, coordinated by the engineer, with outputs traceable in a shared GitHub repository. The knowledge repo on `main` and the model on `master` together form a shared context both agents can read from and contribute to.

## Implications

- As the program grows, consider defining clearer interface agreements between agents — what each one owns, what requires human approval before either agent acts
- The log book and artifact repo serve as the shared memory between agents across sessions — neither agent has persistent context without it
- This pattern could be documented as a reusable MBSE workflow for other open-source or small-team programs operating with AI assistance

## Note on Terminology

The human engineer coined the term "cousin" to describe the relationship between the two Claude instances. It captures something real — same family, different role, complementary rather than redundant.
