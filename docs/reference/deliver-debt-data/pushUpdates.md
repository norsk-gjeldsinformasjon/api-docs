---
tags:
  - debt-delivery
---

# pushUpdates

```
POST {nogi-endpoint}/loans
```

Call within **5 minutes** of: new credit/loan, credit limit change, loan repaid/closed.

!!! note "Balance and interest changes do NOT require a push"
    These are picked up in the next daily `getalldata` call.

## Required fields per loan type

| Field | Repayment loan | Credit facility | Charge card |
|---|---|---|---|
| `type`, `accountID`, `coBorrower` | ✓ | ✓ | ✓ |
| `originalBalance`, `balance`, `terms` | ✓ | — | — |
| `creditLimit` | — | ✓ | — |
| `interestBearingBalance`, `nonInterestBearingBalance` | — | ✓ | ✓ |
| `nominalInterestRate`, `installmentCharges` | ✓ | ✓ | — |