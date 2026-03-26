[deliver-api.md](https://github.com/user-attachments/files/26278576/deliver-api.md)
# API reference — Delivering debt data

Your system **exposes** `getalldata` and `getDataForSSN` — NoGi calls these. Your system **calls** NoGi's `pushUpdates` endpoint when debt changes.

!!! tip "Amount encoding"
    All monetary amounts are in NOK × 100. Example: 100 NOK = `10000`. Interest rates: 10.20% = `1020`.

## 1. getalldata

```
GET /debt-information/v1/loans/{financialInstitutionID}
```

Called by NoGi daily at **05:00 UTC**. Returns the complete dataset for all customers. Paging required if > 100 MB.

### Query parameters

| Parameter | Required | Description |
|---|---|---|
| `financialInstitutionID` | Optional | Organisation number of the FI. If omitted, all FIs for this provider are included. |
| `page` | Optional | 0-based page index. Required if dataset > 100 MB. Min page size: 50 MB. |

### Example response

```json
{
  "providerID": "9908:999888777",
  "customers": [{
    "customerID": "12345678901",
    "financialInstitutionID": "999888777",
    "loans": [{
      "type": "repaymentLoan",
      "accountID": "ACC-001",
      "originalBalance": 500000,
      "balance": 320000,
      "nominalInterestRate": 820,
      "coBorrower": 0
    }]
  }]
}
```

## 2. pushUpdates

```
POST {nogi-endpoint}/loans
```

Call within **5 minutes** of: new credit/loan, credit limit change, loan repaid/closed.

!!! note "Balance and interest changes do NOT require a push"
    These are picked up in the next daily `getalldata` call.

### Required fields per loan type

| Field | Repayment loan | Credit facility | Charge card |
|---|---|---|---|
| `type`, `accountID`, `coBorrower` | ✓ | ✓ | ✓ |
| `originalBalance`, `balance`, `terms` | ✓ | — | — |
| `creditLimit` | — | ✓ | — |
| `interestBearingBalance`, `nonInterestBearingBalance` | — | ✓ | ✓ |
| `nominalInterestRate`, `installmentCharges` | ✓ | ✓ | — |

## 3. getDataForSSN

```
GET /debt-information/v1/loans/{financialInstitutionID}/customer
customerID: {11-digit SSN}  (request header)
```

Called by NoGi on demand. Must respond in < 500 ms for 99% of requests at ≥ 50 req/sec.

## Data validation rules

!!! danger "All data will be rejected if any rule is violated"
    - No duplicate customers (same `customerID` + `financialInstitutionID`)
    - All amounts must be ≥ 0 (no negative values)
    - All SSNs and D-numbers must be valid (11 digits, valid checksum)
    - `coBorrower` must be explicitly set: `0`, `1`, or `2`
