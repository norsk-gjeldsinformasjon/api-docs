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

## Request body

The request body is a JSON object using the same structure as the [getalldata response](getalldata.md#response-schema). Each push contains a `providerID` and one or more customers with their loans.

### Example

```json
{
  "providerID": "9908:985815534",
  "customers": [
    {
      "customerID": "12120799663",
      "financialInstitutionID": "985815534",
      "loans": [
        {
          "type": "creditFacility",
          "timestamp": "2018-02-05T12:54:12Z",
          "accountID": "261a0283883de9a6ea9c860a",
          "coBorrower": 0,
          "creditLimit": 1200000,
          "interestBearingBalance": 120000,
          "nonInterestBearingBalance": 220000,
          "nominalInterestRate": 123,
          "installmentCharges": 10000,
          "installmentChargePeriod": "MONTHLY"
        }
      ]
    }
  ]
}
```

| Code  | Meaning                                  | Action                                    |
|-------|------------------------------------------|-------------------------------------------|
| `200` | Success                                  | Parse response, log, continue             |
| `400` | Invalid or missing input data            | Do not retry. Fix input and resubmit.     |
| `401` | Authentication is missing or not correct | Not authenticated to access resource      |
| `403` | Not authorised                           | Not allowed to access resource            |
| `429` | Too many requests                        | Signal client to back off                 |
| `5xx` | Server error                             | Norsk Gjeldsinformasjon will retry. Investigate and resolve. |
