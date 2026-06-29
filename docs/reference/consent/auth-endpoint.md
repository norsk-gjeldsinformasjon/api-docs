---
tags:
  - consent
---

# Auth endpoint — GET /oauth2/auth

!!! tip "Base URLs"
    - Preprod: `https://access-preprod.norskgjeld.no`
    - Prod: `https://access.norskgjeld.no`

The auth endpoint is the starting point for the OAuth 2.0 Authorization code flow. This request
authenticates the user and returns a code on the callback which can be exchanged for an access token
towards the /token endpoint.

It is important that you show the user some kind of confirmation that the consent has been received
on the callback. This could for example be a landing page if you intend to redirect the user to
another service.

| Parameter | Description | Required |
|---|---|---|
| client_id | client id received from Norsk Gjeldsinformasjon | yes |
| response_type | Must be set to "code" | yes |
| scope | Must contain one and only one debt-related scope. It may optionally contain the "openid" scope | yes |
| redirect_uri | Whitelisted URI where the user will be redirected after consenting | yes |
| state | This is mirrored back in the callback request. Should be set to a random value for each request | yes |

_**Example request:**_

```
GET:https://access-preprod.norskgjeld.no/oauth2/auth?client_id=your_client_id_here&response_type=code&scope=debt.unsecured.presentation&state=thisShouldBeARandomValue&redirect_uri=https://api-eksempelbank.no/v1/callback
```

_**Example response:**_

```
Success response:
https://api-eksempelbank.no/v1/callback?code=wi-w8zIdwwBHggkHhSjR24wH8pN6MDqxdObTBDuzaZo.sciTzz9qgwMlGBZ6X0jYIDyib8MupoIp5gbIJBxnTCs&scope=debt.unsecured.presentation&state=thisShouldBeARandomValue

Error response:
https://api-eksempelbank.no/v1/callback?error=consent_denied&error_description=&state=thisShouldBeARandomValue
```

The error code can be "consent\_denied", "server\_error", "invalid\_scopes" or "login\_cancelled"