# Decision — Continue Evaluation with Panasonic NCR18650B

**Date:** 2026-06-10
**Decision Type:** Component Selection
**Status:** Approved
**Decider:** Trail Power for Campgrounds Program

---

## Decision Statement

The Trail Power for Campgrounds program will continue component evaluation using the Panasonic NCR18650B as the selected lithium-ion cell for the `Battery Holder` within the `Charge Box` assembly.

## Rationale

1. **Model alignment** — The NCR18650B is the cell specified in the Capella Physical Architecture model, allocated to the `Store Energy` function. Continuing with this part maintains fidelity to the MBSE baseline.

2. **Performance confidence** — Supplier documentation and end-user evidence indicates the NCR18650B meets its published specifications (3350–3400 mAh, 6.8 A max discharge). The cell's optimal operating range (1–2 A continuous) is well matched to the low-to-medium drain profile of the Trail Power application.

3. **Supply chain availability** — Multiple bulk suppliers have been identified (Liion Wholesale, Octopart, Alibaba), and an RFP (TP-BAT-2026-001) has been issued to solicit formal pricing and delivery terms.

4. **Panasonic brand credibility** — The NCR18650B is a well-established, widely-used cell manufactured in Japan by Panasonic Corporation, with a strong track record in DIY and commercial power applications.

## Conditions and Next Steps

This decision is conditional on the following evaluation activities being completed satisfactorily:

- [ ] Receipt and review of RFP responses (TP-BAT-2026-001)
- [ ] Bench testing of procured cells against the `Store Energy` function performance envelope
- [ ] Confirmation of cell authenticity via Certificate of Conformance from selected supplier
- [ ] Full system integration test within the Charge Box assembly

## Alternatives Considered

| Alternative | Reason Not Selected |
|---|---|
| Generic 18650 cells | Insufficient specification traceability; higher counterfeit risk |
| Alternative high-capacity 18650 (e.g., Samsung 30Q, LG MJ1) | Not specified in current model baseline; would require model change |
| Rechargeable AA/AAA cells | Insufficient capacity and voltage for the system design |

## References

- Battery Subsystem Analysis — PA Layer [11f5f77d]
- Observation — Panasonic NCR18650B Meets Specified Performance [f8869c15]
- RFP TP-BAT-2026-001 — NCR18650B Procurement [03591bcc]
