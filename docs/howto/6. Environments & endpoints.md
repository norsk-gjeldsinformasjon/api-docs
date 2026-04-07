# Environments & endpoints

All integrations must be verified in the **pre-production (test) environment** before production access is granted.

---

## Lookup API

| Environment | URL |
|---|---|
| Test / Pre-prod | `https://ws.preprod.norskgjeld.no/api/rest/v2/debt/search` |
| OpenAPI spec (test) | `https://ws.preprod.norskgjeld.no/api/rest/swagger.json` |
| Production | Provided during onboarding — do not hard-code from examples |

## Delivery API

The delivery API endpoints are hosted **on your infrastructure**. NoGi calls your endpoints.

| Operation | URL format |
|---|---|
| `getalldata` | `https://<your-host>/debt-information/v1/loans/{financialInstitutionID}` |
| `getDataForSSN` | `https://<your-host>/debt-information/v1/loans/{financialInstitutionID}/customer` |
| `pushUpdates` | NoGi endpoint — provided during onboarding |

!!! warning "Data availability"
    All debt data must be updated and available from **05:00 UTC daily**.

## Certificate environments

!!! danger "Separate certificates required"
    You must use **separate** enterprise certificates (virksomhetssertifikat) for test and production. These must never be shared.

| Environment | Certificate type | Accepted issuers |
|---|---|---|
| Test | Enterprise client certificate (SEID 2.0) | Buypass or Commfides |
| Production | Enterprise client certificate (SEID 2.0) | Buypass or Commfides |
| Non-Norwegian FIs | PSD2 / eIDAS QWAC | Approved QTSP |

## Token endpoints (consent API only)

| Environment | Token endpoint |
|---|---|
| Test | `https://access-preprod.norskgjeld.no/oauth2/token` |
| Production | `https://access.norskgjeld.no/oauth2/token` |
