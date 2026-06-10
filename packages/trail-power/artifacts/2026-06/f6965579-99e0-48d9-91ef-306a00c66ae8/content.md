# Issue — Binary File Upload to Artifact Repo Not Yet Supported

**Date:** 2026-06-10
**Type:** Capability Gap
**Status:** Open
**Priority:** Medium

---

## Issue

The artifact repository MCP currently supports text/JSON/YAML artifacts only. Binary files such as `.docx`, `.pdf`, `.xlsx`, and other generated deliverables cannot be uploaded directly to the knowledge repo. This leaves a gap in the traceability chain between reference artifacts and their associated file deliverables.

## Current Workaround

A text artifact is written to the repo describing the document (name, reference number, scope, derivation), but the actual file remains local only. Example:

- `RFP TP-BAT-2026-001 — NCR18650B Procurement` [03591bcc] exists in the repo as a reference record
- `RFP_NCR18650B_TrailPower.docx` exists locally at `/mnt/user-data/outputs/` but is not in the repo

## Desired Capability

A file upload mechanism that allows binary deliverables to be committed alongside their reference artifacts, either:
- Via a new MCP tool (e.g., `upload_file_artifact`) that accepts base64-encoded content and commits it to the repo
- Via direct Git commit of binary files to a `deliverables/` folder on the `main` branch

## Affected Artifacts

- `RFP_NCR18650B_TrailPower.docx` — needs to be uploaded to `main` branch once capability is available

## Notes

- This item should be revisited when new MCP services come online
- All future document deliverables (reports, RFPs, analysis exports) will have the same gap until resolved
