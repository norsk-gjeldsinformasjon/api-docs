---
tags:
  - consent
---

# Consent API reference

The Consent API lets you ask users for consent to share unsecured debt information, and
fetch that information based on the consent. It uses a redirect-based flow adhering to
OAuth2.0 and OpenID Connect standards.

> See [Get started](../../get-started/index.md#regular-consent) for prerequisites, setup,
> and testing instructions.

## Endpoints and topics

| Topic | Description |
|---|---|
| [Scopes](scopes.md) | Scope definitions, intended use, extended duration, and the optional openid scope |
| [OpenID configuration](openid-configuration.md) | `/.well-known/openid-configuration` metadata |
| [Auth endpoint](auth-endpoint.md) | `GET /oauth2/auth` — parameters and examples |
| [Token endpoint](token-endpoint.md) | `POST /oauth2/token` — Authorization Code and Client Credentials flows |
| [Collect debt info](collect-debt.md) | Using access tokens to retrieve debt information |
| [Consent feed](consent-feed.md) | Reading updates about consents via the feed API |
| [OpenAPI spec](../openapi.md) | Interactive OpenAPI specification |