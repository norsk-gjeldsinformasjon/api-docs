---
tags:
  - debt-delivery
---

# getDataForSSN

```
GET /debt-information/v1/loans/{financialInstitutionID}/customer
```

Called by Norsk Gjeldsinformasjon on demand. Must respond in **&lt; 500 ms for 99%** of requests at **≥ 50 req/sec**.

## Request headers

| Header | Required | Description |
|---|---|---|
| `customerID` | **YES** | 11-digit NIN or D-number of the customer to look up |

## Response schema

The response body is a JSON object representing the customer and their loans — see the [getalldata response schema](getalldata.md#response-schema) for the full field reference.

| Field | Type | Description |
|---|---|---|
| `customerID` | string | 11-digit NIN or D-number matching the request header |
| `financialInstitutionID` | string | Organisation number of the FI |
| `loans` | array of objects | List of loans for this customer. Each loan is one of: `repaymentLoan`, `creditFacility`, or `chargeCard`. |

## Example response

```json
{
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
}
```

If the customer has no registered debt, return HTTP 200 with an empty `loans` array (not a 404 error):

```json
{
  "customerID": "12345678901",
  "financialInstitutionID": "999888777",
  "loans": []
}
```

## Error response

| Field | Type | Description |
|---|---|---|
| `error` | string | Error description |
| `error_description` | string | Optional short description of the error |
| `timestamp` | string (ISO 8601) | Timestamp when the error was handled |
| `trace_id` | string | Unique ID for debugging. Set to the value of the `X-Trace-ID` header if provided. |

## Status codes

| Code  | Meaning                                  | Action                                    |
|-------|------------------------------------------|-------------------------------------------|
| `200` | Success                                  | Parse response, log, continue             |
| `400` | Invalid or missing input data            | Do not retry. Fix input and resubmit.     |
| `401` | Authentication is missing or not correct | Not authenticated to access resource      |
| `403` | Not authorised                           | Not allowed to access resource            |
| `429` | Too many requests                        | Signal client to back off                 |
| `5xx` | Server error                             | Norsk Gjeldsinformasjon will retry. Investigate and resolve. |
