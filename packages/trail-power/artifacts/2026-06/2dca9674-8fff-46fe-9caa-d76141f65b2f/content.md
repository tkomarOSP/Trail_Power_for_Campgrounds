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
