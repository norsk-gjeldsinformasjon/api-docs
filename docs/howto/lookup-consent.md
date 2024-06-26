## Look up debt information with a consent

## Prerequisites

You know [how to authorize](../howto/consent_authorize.md) and retrieve access tokens. You have collected consent from an individual.

## 1. Retrieve access-token

See [how to authorize](../howto/consent_authorize.md) for the details on how to authenticate. To look up debt, you can use params: `audience=https://api.norskgjeld.no/v1/debt` and `scope=debt.unsecured.presentation`. (See [reference](../reference/index.md#reference-consent-authorization-audience-and-scope) for what you should use)

## 2. Look up debt

Once authorized, you should have an access token that you can use against our API to look up debt:

```http request
GET /v1/debt/{id}
Authorization: Bearer {your-token-here}
```

Where `{id}` and `{your-token-here}` are substituted with your consent-id and access-token.

The response will be a JSON-document with the debt information.

See the [OpenAPI reference](../reference/openapi.md) for a detailed description.
