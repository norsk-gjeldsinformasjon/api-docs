[consent_authorize.md](https://github.com/user-attachments/files/26277399/consent_authorize.md)
# How do I authorize

## Prerequisites

You have been given access to the consent APIs and have been given a client id. See [Get started](../index.md) for how to begin.

## Library support

Developers will typically use one of the many available [OAuth 2.0 libraries](https://oauth.net/code/) and not hand-roll their own code for authorizing. But the steps described in this how-to can be useful during debugging or verifying access.

## Fetching an access token

Before you call Norsk Gjeldsinformasjon API, you will need to fetch an access token. There are two ways: *Client credentials* and *Authorization code*.

Access tokens are requested by POSTing to the `/token` endpoint:

- `https://access-preprod.norskgjeld.no/oauth2/token` (test)
- `https://access.norskgjeld.no/oauth2/token` (production)

### Client credentials

| Parameter | Description |
|---|---|
| `grant_type` | Must be set to `"client_credentials"` |
| `audience` | See reference for the service you want to call |
| `scope` | See reference for the service you want to call |

```json
{
  "access_token": "C2EzneyuE2lEK8VBYZS7TxBUMF16Ns6gTuU5DybZbY...",
  "expires_in": 3599,
  "scope": "debt.unsecured.presentation debt.unsecured.processing",
  "token_type": "bearer"
}
```

### Authorization code

This is only available with [Regular consent](../reference/consent.md). Redirect the individual to `access.norskgjeld.no`:

```
GET: https://access-preprod.norskgjeld.no/oauth2/auth
  ?client_id=your_client_id_here
  &response_type=code
  &scope=debt.unsecured.presentation
  &state=thisShouldBeARandomValue
  &redirect_uri=https://api-eksempelbank.no/v1/callback
```

Possible error codes on callback: `consent_denied`, `server_error`, `invalid_scopes`, `login_cancelled`.
