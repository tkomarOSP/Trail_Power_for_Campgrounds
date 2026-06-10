# Battery Subsystem Analysis — Physical Architecture
**Model:** Trail Power for Campgrounds
**Layer:** Physical Architecture (PA)
**Date:** 2026-06-10
**Analyst:** SE Knowledge Partner

---

## 1. Component Structure

The battery subsystem is contained within the `Battery Holder` component, a child of `Charge Box`.

| Component | Type | Parent | Notes |
|---|---|---|---|
| Battery Holder | PhysicalComponent | Charge Box | Container for cells and fuse |
| LI 18650 (1) | PhysicalComponent | Battery Holder | Panasonic NCR18650B |
| LI 18650 (2) | PhysicalComponent | Battery Holder | Panasonic NCR18650B |
| Fuse | PhysicalComponent | Battery Holder | Overcurrent protection |

Each LI 18650 is modeled as both a Physical Node (hardware enclosure) and a Behavior Component (functional representation deployed into the node) — standard Capella PA decomposition.

## 2. Specified Part

- **Manufacturer:** Panasonic Corporation
- **Part Number:** NCR18650B
- **Nominal Voltage:** 3.6 V
- **Typical Capacity:** 3400 mAh
- **Max Continuous Discharge:** 6.8 A
- **Form Factor:** 18650 cylindrical, flat top
- **Dimensions:** 65.1 mm (L) × 18.3 mm (D)
- **Weight:** 47 g
- **Protection:** Unprotected
- **Country of Origin:** Japan
- **Model Reference:** Amazon link embedded in component description

## 3. Allocated Functions

Each LI 18650 cell carries a single allocated function:

| Cell | Allocated Function | LA Trace |
|---|---|---|
| LI 18650 (1) | Store Energy | LA: Store Energy → Charge Storage Device |
| LI 18650 (2) | Store Energy | LA: Store Energy → Charge Storage Device |

The Fuse carries two protection functions:
- `Protect charge overcurrent`
- `Protect drain overcurrent`

## 4. Functional Exchange Chain

Power flow through the battery subsystem:

```
Chg Power / Bat Power  ←  Protect charge overcurrent (Fuse)
        ↓
  LI 18650 (1) / LI 18650 (2)  [Store Energy]
        ↓
  Store Power / Bat Output  →  Protect drain overcurrent (Fuse)
        ↓
  Battery Power  →  Distribute Bat Power
                →  Charger Indication Board
                →  Boost Voltage to USB
```

Root PA functional exchanges identified:
- `Battery Charge Voltage`
- `Battery Voltage`
- `Battery Power` (×3 — to Boost Voltage to USB and root level)

## 5. Open Modeling Issues

| Issue | Detail | Priority |
|---|---|---|
| Exchange naming inconsistency | Cell 1 charge path uses `Chg Power`; Cell 2 uses `Bat Power` — may indicate design intent or naming gap | Medium |
| Unnamed LA constraint | `Store Energy` (LA) has an attached constraint (ref: 06eef073) with empty description — likely incomplete requirement | Low |

## 6. Supplier Information

- **Primary (model-linked):** Amazon — https://www.amazon.com/NCR18650B-Storage-Holder-doorbell-Flashlight/dp/B083XK5HDG
- **US Wholesale:** Liion Wholesale — https://liionwholesale.com
- **Component Distributor:** Octopart — https://octopart.com/ncr18650b-panasonic-30796917
- **Bulk Marketplace:** Alibaba — https://www.alibaba.com/showroom/wholesale-ncr18650b-panasonic.html

> Note: Verify authenticity carefully — 18650 counterfeits are common on marketplace platforms.
