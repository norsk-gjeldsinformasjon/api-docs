---
tags:
  - debt-delivery
---

# getalldata

```
GET /debt-information/v1/loans/{financialInstitutionID}
```

Called by NoGi daily, queued some time after **05:00 UTC**. Returns the complete dataset for all customers.

!!! warning "Data availability"
    All debt data must be updated and available from **05:00 UTC daily**. NoGi's call is queued after this time.

## Query parameters

| Parameter | Required | Description |
|---|---|---|
| `financialInstitutionID` | Optional | Organisation number of the FI. A 9-digit integer or string of 9–16 characters. Supports foreign organisation numbers (e.g. 10-digit `5569622441`). If omitted, data for all FIs under this provider are returned. |
| `page` | Optional | 0-based page index. Required if the total response exceeds 100 MB. Each page must be at least 50 MB. NoGi requests pages sequentially until a page with fewer items than the page size is returned. |

## Response schema

The response body is a JSON object with the following top-level fields:

| Field | Type | Description |
|---|---|---|
| `providerID` | string | Provider identifier in ISO 6523 format: `{Authority}:{Identifier}` (e.g. `9908:999888777`). 9908 = ISO 6523 ICD for Norwegian organisation numbers. |
| `customers` | array of objects | List of customers, each containing their loan data. |

### Customer object

| Field | Type | Description |
|---|---|---|
| `customerID` | string | 11-digit NIN or D-number |
| `financialInstitutionID` | string | Organisation number of the FI that owns this customer relationship |
| `loans` | array of objects | List of loans for this customer. Each loan is one of: `repaymentLoan`, `creditFacility`, or `chargeCard`. |

### Loan object — common fields

| Field | Type | Description |
|---|---|---|
| `type` | string | Loan type: `repaymentLoan`, `creditFacility`, or `chargeCard` |
| `coBorrower` | integer | `0` = single debtor / not a co-borrower, `1` = co-borrower, `2` = primary debtor with co-borrower |
| `accountID` | string | Account identifier for the loan |
| `timestamp` | string (ISO 8601) | Timestamp for when the data was extracted from your system |

### Loan object — repayment loan (`repaymentLoan`)

| Field | Type | Description |
|---|---|---|
| `originalBalance` | integer | Original loan amount in NOK × 100 |
| `balance` | integer | Current balance in NOK × 100 |
| `terms` | integer | Remaining terms in months |
| `nominalInterestRate` | integer | Nominal interest rate (10.20% = `1020`) |
| `installmentCharges` | integer | Monthly installment charges in NOK × 100 |
| `installmentChargePeriod` | string | Charge interval; if not monthly, recalculate to monthly |

### Loan object — credit facility (`creditFacility`)

| Field | Type | Description |
|---|---|---|
| `creditLimit` | integer | Maximum credit in NOK × 100 |
| `interestBearingBalance` | integer | Interest-bearing balance in NOK × 100 |
| `nonInterestBearingBalance` | integer | Non-interest-bearing balance (booked balance minus interest-bearing) in NOK × 100 |
| `nominalInterestRate` | integer | Nominal interest rate (10.20% = `1020`) |
| `installmentCharges` | integer | Monthly installment charges in NOK × 100 |
| `installmentChargePeriod` | string | Charge interval; if not monthly, recalculate to monthly |

### Loan object — charge card (`chargeCard`)

| Field | Type | Description |
|---|---|---|
| `interestBearingBalance` | integer | Interest-bearing balance in NOK × 100 |
| `nonInterestBearingBalance` | integer | Non-interest-bearing balance in NOK × 100 |

## Example response

```json
{
  "providerID": "9908:999888777",
  "customers": [{
    "customerID": "12345678901",
    "financialInstitutionID": "999888777",
    "loans": [{
      "type": "repaymentLoan",
      "accountID": "ACC-001",
      "timestamp": "2026-06-25T06:00:00Z",
      "originalBalance": 500000,
      "balance": 320000,
      "nominalInterestRate": 820,
      "coBorrower": 0
    }]
  }]
}
```

| Code  | Meaning                                  | Action                                    |
|-------|------------------------------------------|-------------------------------------------|
| `200` | Success                                  | Parse response, log, continue             |
| `400` | Invalid or missing input data            | Do not retry. Fix input and resubmit.     |
| `401` | Authentication is missing or not correct | Not authenticated to access resource      |
| `403` | Not authorised                           | Not allowed to access resource            |
| `429` | Too many requests                        | Signal client to back off                 |
| `5xx` | Server error                             | NoGi will retry. Investigate and resolve. |
