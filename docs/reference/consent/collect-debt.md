---
tags:
  - consent
---

# Collect debt info

!!! tip "Base URLs"
    - Preprod: `https://api-preprod.norskgjeld.no`
    - Prod: `https://api.norskgjeld.no`

After you have received an access token from the Authorization server you can use it to collect the
debt information from the API which is documented in the
[OpenAPI spec](../openapi.md) (under the **Debt API** tag).

The endpoint to call depends on the OAuth flow used:

| Flow | Endpoint | Description |
|---|---|---|
| Authorization Code | `GET /v1/debt` | Token contains the consent context |
| Client Credentials | `GET /v1/debt/{consentId}` | Requires the consent ID from the ID Token |
| Client Credentials | `DELETE /v1/debt/{consentId}` | Revoke a consent |
| Client Credentials | `GET /v1/debt/{consentId}/status` | Check if consent is still active |

See the How-to guides for walkthroughs:
- [Look up debt with consent](../../howto/lookup-debt-with-consent.md)
- [Get notified about changes to consents](../../howto/consent-notifications.md)