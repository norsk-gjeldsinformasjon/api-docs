---
tags:
  - consent
---

# OpenID configuration

The OpenID-configuration returns metadata which can be used to configure your client library.

_**Example request**_

```
GET:https://access-preprod.norskgjeld.no/.well-known/openid-configuration
```

_**Example response**_

```json
{
    "issuer":"https://access-preprod.norskgjeld.no/",
    "authorization_endpoint":"https://access-preprod.norskgjeld.no/oauth2/auth",
    "token_endpoint":"https://access-preprod.norskgjeld.no/oauth2/token",
    "jwks_uri":"https://access-preprod.norskgjeld.no/.well-known/jwks.json",
    "subject_types_supported":[
      "pairwise"
    ],
    "response_types_supported":[
      "code"
    ],
    "claims_supported":[
      "sub"
    ],
    "grant_types_supported":[
      "authorization_code",
      "client_credentials"
    ],
    "response_modes_supported":[
      "query",
      "fragment"
    ],
    "userinfo_endpoint":"https://access-preprod.norskgjeld.no/userinfo",
    "scopes_supported":[
      "openid"
    ],
    "token_endpoint_auth_methods_supported":[
      "client_secret_basic"
    ],
    "userinfo_signing_alg_values_supported":[
      "none",
      "RS256"
    ],
    "id_token_signing_alg_values_supported":[
      "RS256"
    ],
    "request_parameter_supported":true,
    "request_uri_parameter_supported":true,
    "require_request_uri_registration":true,
    "claims_parameter_supported":false,
    "revocation_endpoint":"https://access-preprod.norskgjeld.no/oauth2/revoke",
    "end_session_endpoint":"https://access-preprod.norskgjeld.no/oauth2/sessions/logout",
    "request_object_signing_alg_values_supported":[
      "RS256",
      "none"
    ]
}
```