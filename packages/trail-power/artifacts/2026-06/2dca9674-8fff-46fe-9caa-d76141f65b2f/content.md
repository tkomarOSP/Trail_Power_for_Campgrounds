# Trail Power for Campgrounds — Engineering Work Log

This log book records engineering sessions, analyses, decisions, and deliverables for the Trail Power for Campgrounds MBSE program.

**Repository:** https://github.com/tkomarOSP/Trail_Power_for_Campgrounds
**Model Tool:** Capella (via capella-fabric MCP)

---

## 2026-06-10T12:18:53Z — milestone

## Battery Subsystem Analysis & Procurement Initiation

**Session focus:** Physical Architecture (PA) battery subsystem — analysis and procurement kickoff

### Work Completed

**1. Model Exploration — Battery Components (PA Layer)**
Queried the Capella PA layer for all battery-related components, functions, and physical exchanges. Identified the full battery subsystem structure:
- Two Panasonic NCR18650B cells modeled as Physical Nodes + Behavior Components inside the `Battery Holder` (child of `Charge Box`)
- Each cell allocated to the `Store Energy` function, which traces back to the LA `Charge Storage Device`
- Fuse component handling both `Protect charge overcurrent` and `Protect drain overcurrent` functions
- Power flow traced downstream to `Distribute Bat Power`, `Charger Indication Board`, and `Boost Voltage to USB`

**2. Supplier Research**
Identified four bulk suppliers for the Panasonic NCR18650B:
- Amazon (model-linked, retail/marketplace)
- Liion Wholesale (US specialist, recommended for authenticity)
- Octopart (authorized distributor aggregator)
- Alibaba (bulk marketplace, counterfeit risk noted)

**3. RFP Generation**
Generated formal RFP document `RFP_NCR18650B_TrailPower.docx` (reference: TP-BAT-2026-001) covering:
- Full technical specification from model
- Four quantity pricing tiers (100 / 500 / 1,000 / 5,000 cells)
- Authenticity, documentation, and compliance requirements
- Weighted evaluation criteria (authenticity weighted 30%)
- 21-day response deadline

### Open Issues Identified
- Exchange naming inconsistency between Cell 1 (`Chg Power`) and Cell 2 (`Bat Power`) on the charge path — may indicate design intent or naming gap; recommend review
- Unnamed LA constraint on `Store Energy` function (ref: 06eef073) — empty description, likely incomplete requirement

### Artifacts Produced
- `Battery Subsystem Analysis — PA Layer` [11f5f77d] — full model analysis with component structure, functional allocations, and exchange chain
- `RFP TP-BAT-2026-001 — NCR18650B Procurement` [03591bcc] — RFP reference record with supplier list and evaluation criteria
- `RFP_NCR18650B_TrailPower.docx` — Word document deliverable (local output, not yet uploaded to repo)

### Next Steps (suggested)
- Resolve exchange naming inconsistency in Capella model
- Complete the unnamed LA constraint on `Store Energy`
- Distribute RFP to identified suppliers
- Trace charging path upstream to solar charger in PA
- Trace `Supplied Power` exchange from `Store Energy` → `Boost Voltage to USB` in PA


**References:** `11f5f77d-592f-4355-b2b6-0879123fbab5`, `03591bcc-7db6-42ad-ae67-dd4117b021a8`

---

## 2026-06-10T12:22:00Z — observation

## Panasonic NCR18650B Appears to Meet Specified Performance

Based on supplier documentation and customer feedback gathered during procurement research, Panasonic NCR18650B cells appear to meet or exceed the performance specifications allocated to the `Store Energy` function in the PA model.

Key supporting points:
- Cells charge as expected and runtime aligns with 3400 mAh capacity rating
- Liion Wholesale independently tests and authenticates NCR18650B stock — confirmed to perform to published Panasonic specs
- Low-to-medium drain profile of the Trail Power application is well within the cell's optimal operating range (1–2 A continuous, up to 6.8 A max)

**Caveat:** Evidence is from supplier documentation and end-user reviews, not independent bench testing. Authenticity of cells is a prerequisite. Formal verification against model requirements would require testing actual cells against the `Store Energy` function performance envelope.

**Artifact:** Observation — Panasonic NCR18650B Meets Specified Performance [f8869c15]


**References:** `f8869c15-c7cc-47d9-8295-618d0274b50c`

---

## 2026-06-10T12:23:19Z — decision

## Decision: Continue Evaluation with Panasonic NCR18650B

The program will continue component evaluation using the Panasonic NCR18650B as the selected lithium-ion cell for the `Battery Holder` / `Charge Box` assembly.

**Rationale summary:**
- Maintains fidelity to the MBSE model baseline (cell is specified in PA layer)
- Performance evidence supports confidence in spec compliance
- RFP TP-BAT-2026-001 is in flight to establish formal supplier pricing
- Strong brand credibility and supply chain availability confirmed

**Conditions for full approval:**
- RFP responses reviewed and supplier selected
- Bench testing of cells against `Store Energy` function performance envelope
- Certificate of Conformance confirmed from selected supplier
- System integration test within Charge Box assembly completed

**Artifact:** Decision — Continue Evaluation with Panasonic NCR18650B [49f24a67]


**References:** `49f24a67-4910-4e2e-bc09-a2cf3d9eab20`

---

## 2026-06-10T12:27:30Z — observation

## MBSE-Driven Engineering Approach Shows Strong Value

Reflecting on this session, the Trail Power program is demonstrating MBSE working as intended — the Capella model is acting as a living source of truth that actively drives downstream work, not a static reference artifact.

Key observations:

**Model-to-action traceability** — The RFP was derived directly from PA layer data, not authored independently. The link between system design and procurement is explicit and recoverable.

**Artifact lineage as program memory** — The knowledge repo now holds a clean, timestamped, version-controlled traceability chain from model analysis through observation and decision to procurement document. Rationale is recoverable with a single artifact lookup.

**Incidental issue discovery** — Two open modeling issues (exchange naming inconsistency, unnamed LA constraint) were surfaced as a natural byproduct of querying the model, not as the session focus. The model surfaces gaps whether you are looking for them or not.

**Compounding value potential** — As more subsystems are explored the same way, the knowledge repo becomes a living program record any engineer can walk into and get oriented quickly — without relying on tribal knowledge.

**Implications:** Establish a regular cadence for model-driven analysis sessions; resolve the two open model issues in Capella; extend the repo package structure consistently as new subsystems are explored.

**Artifact:** Observation — MBSE-Driven Engineering Approach Shows Strong Value [25a05fcf]


**References:** `25a05fcf-50da-4bd3-a07a-9d27daa162cd`

---

## 2026-06-10T12:39:23Z — issue

## Issue: Binary File Upload to Artifact Repo Not Yet Supported

The artifact repo MCP currently supports text/JSON/YAML only — binary deliverables like `.docx`, `.pdf`, and `.xlsx` files cannot be committed directly to the knowledge repo. This leaves the traceability chain incomplete between reference artifacts and their associated file deliverables.

**Immediate impact:** `RFP_NCR18650B_TrailPower.docx` exists locally but is not in the repo. The reference artifact [03591bcc] describes it but cannot link to the file itself.

**To do:** Revisit when new MCP services come online — candidate for a new `upload_file_artifact` tool or direct Git binary commit to a `deliverables/` folder on `main`.

**Artifact:** Issue — Binary File Upload to Artifact Repo Not Yet Supported [f6965579]


**References:** `f6965579-99e0-48d9-91ef-306a00c66ae8`

---

## 2026-06-10T13:08:47Z — decision

## Model Change — Exchange Naming Inconsistency Resolved

**Change:** Renamed `Bat Power` → `Chg Power` on Cell 2 charge path (PA layer)
**UUID patched:** 25520ebc-aea6-456d-a64a-7d30211165fd
**Commit:** 4a95517d on master
**Tool:** capella-fabric:apply_model_patch

Both LI 18650 cell charge path exchanges now consistently named `Chg Power`, matching the naming convention established on Cell 1. This resolves the open issue flagged during the battery subsystem analysis session.

Verified post-patch: both UUIDs (6395bb62, 25520ebc) return `Chg Power` on search. Change pushed to master.

---

## 2026-06-10T13:21:41Z — issue

## Issue: Capella Fabric MCP — Write/Patch Capability + Author Identity Amendment

**Part 1 — Write/Patch Capability:** Three new tools (`apply_model_patch`, `push_model_changes`, `verify_model`) added to `capella-fabric` MCP using `py-capellambse >= 0.6` declarative API. Files modified: `capella_service.py`, `git_service.py`, `mcp_server.py`. Status: **Implemented and validated** — first patch applied 2026-06-10 (commit `4a95517d`).

**Part 2 — Author Identity Amendment (Open):** All commits via `apply_model_patch` and `push_artifacts` currently carry the MCP server's default Git identity, not the engineer's. Proposed fix: expose optional `author_name` and `author_email` parameters on both tools, passed through to `git commit --author`. Applies to both `master` (model) and `main` (artifacts). Interim workaround: embed `[Author Name]` in commit message.

**Artifact:** Issue — Capella Fabric MCP: Write/Patch Capability + Author Identity on Commits [b1699e70]


**References:** `b1699e70-8490-4329-8bdd-439ba879e741`
