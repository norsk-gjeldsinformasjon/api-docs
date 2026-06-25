---
tags:
  - debt-delivery
---

# Data validation rules

!!! danger "All data will be rejected if any rule is violated"

- **No duplicate customers** — same `customerID` + `financialInstitutionID`
- **All amounts must be ≥ 0** — no negative values
- **All NINs and D-numbers must be valid** — 11 digits, valid checksum
- **`coBorrower` must be explicitly set** — `0` (single debtor / not a co-borrower), `1` (co-borrower), or `2` (primary debtor with co-borrower)