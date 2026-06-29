---
tags:
  - consent
---

# Token endpoint — POST /oauth2/token

!!! tip "Base URLs"
    - Preprod: `https://access-preprod.norskgjeld.no`
    - Prod: `https://access.norskgjeld.no`

The token endpoint is used to obtain an access token which is used when collecting debt information
from the debt-API. This can either be completed with the code received on the callback after the
user has finished delivering their consent (Authorization Code Flow), or the client can identify
directly with their credentials to obtain an access token directly (Client Credentials Flow).

## Authentication

The client must authenticate using HTTP Basic authentication with its client ID and client secret in
the Authorization header, as described in the
[Basic authentication scheme](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication#basic_authentication_scheme).

## Authorization Code Flow

When requesting an access token using authorization code flow the following parameters have to be
present in the body which should be of type application/x-www-form-urlencoded

| Parameter | Description |
|---|---|
| grant_type | Must be set to "authorization_code" |
| client_id | Client id received from Norsk Gjeldsinformasjon |
| redirect_uri | Whitelisted URI where the user will be redirected after consenting |
| code | Authorization received on the authorization callback |

_**Example request**_

```
POST:https://access-preprod.norskgjeld.no/oauth2/token
```

HEADERS and BODY as described above.

_**Example response**_
```json
{
    "access_token":"YcvXKoiuOwnbJkxso2Oe6bhp2cXcoHdZ1pdgE_QpDww.cAu8_J51evXtBQxfTMzkRA414_mOla1zryE1e_-r-1k",
    "expires_in":3599,
    "scope":"debt.unsecured.presentation",
    "token_type":"bearer"
}
```

## Client Credentials Flow

When requesting an access token using the client credential flow the following parameters have to be
present in the body which should be of type application/x-www-form-urlencoded

| Parameter | Description |
|---|---|
| grant_type | Must be set to "client_credentials" |
| audience | Must be set to "https://api.norskgjeld.no/v1/debt" in prod and "https://api-preprod.norskgjeld.no/v1/debt" in preprod |
| scope | Must contain a space separated string with the scopes that you are going to fetch debt information for. It should usually be set to: `debt.unsecured.presentation debt.unsecured.processing` |

_**Example request**_

```
POST:https://access-preprod.norskgjeld.no/oauth2/token
```

HEADERS and BODY as described above.

_**Example response**_

```json
{
    "access_token":"C2EzneyuE2lEK8VBYZS7TxBUMF16Ns6gTuU5DybZbY.6pcF_rv3muje47_GDucYJrQZvDioc8O7oCmvKMZKHEg",
    "expires_in":3599,
    "scope":"debt.unsecured.presentation debt.unsecured.processing",
    "token_type":"bearer"
}
```