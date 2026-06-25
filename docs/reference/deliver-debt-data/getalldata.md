---
tags:
  - debt-delivery
---

# getalldata

```
GET /debt-information/v1/loans/{financialInstitutionID}
```

Called by NoGi daily, queued some time after **05:00 UTC**. Returns the complete dataset for all customers. Paging required if &gt; 100 MB.

## Query parameters

| Parameter | Required | Description |
|---|---|---|
| `financialInstitutionID` | Optional | Organisation number of the FI. If omitted, all FIs for this provider are included. |
| `page` | Optional | 0-based page index. Required if dataset &gt; 100 MB. Min page size: 50 MB. |

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
      "originalBalance": 500000,
      "balance": 320000,
      "nominalInterestRate": 820,
      "coBorrower": 0
    }]
  }]
}
```