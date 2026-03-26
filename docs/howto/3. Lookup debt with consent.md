[lookup-consent.md](https://github.com/user-attachments/files/26277557/lookup-consent.md)
# Look up debt with consent

## Prerequisites

You know [how to authorize](consent_authorize.md) and retrieve access tokens. You have collected consent from an individual.

## 1. Retrieve access token

See [how to authorize](consent_authorize.md). Use `audience=https://api.norskgjeld.no/v1/debt` and `scope=debt.unsecured.presentation`.

## 2. Look up debt

Once authorized, use the access token to look up debt:

```
GET /v1/debt/{id}
Authorization: Bearer {your-token-here}
```

Where `{id}` is your consent-id and `{your-token-here}` is your access token. See the [OpenAPI reference](../reference/openapi/index.md) for a detailed description.
