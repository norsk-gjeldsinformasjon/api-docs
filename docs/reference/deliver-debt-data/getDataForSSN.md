---
tags:
  - debt-delivery
---

# getDataForSSN

```
GET /debt-information/v1/loans/{financialInstitutionID}/customer
customerID: {11-digit NIN}  (request header)
```

Called by NoGi on demand. Must respond in **&lt; 500 ms for 99%** of requests at **≥ 50 req/sec**.