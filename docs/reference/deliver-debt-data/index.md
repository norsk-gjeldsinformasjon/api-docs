---
tags:
  - debt-delivery
---

# API reference — Delivering debt data

Your system **exposes** `getalldata` and `getDataForSSN` — NoGi calls these. Your system **calls** NoGi's `pushUpdates` endpoint when debt changes.

!!! tip "Amount encoding"
    All monetary amounts are in NOK × 100. Example: 100 NOK = `10000`. Interest rates: 10.20% = `1020`.

## Endpoints

| Endpoint | Direction | Description |
|---|---|---|
| [getalldata](getalldata.md) | NoGi → your system | Daily batch retrieval of all customer debt data |
| [getDataForSSN](getDataForSSN.md) | NoGi → your system | On-demand lookup for a single National Identity Number |
| [pushUpdates](pushUpdates.md) | your system → NoGi | Push credit events within 5 minutes |

## Validation

[Data validation rules](validation.md) apply to all endpoints. All data will be rejected if any rule is violated.