---
tags:
  - consent
---

# OpenAPI specification

This page provides an interactive OpenAPI (Swagger) specification for the Consent APIs.
You can expand each endpoint to see request parameters, response schemas, and example values.

The spec covers these APIs:

| API | Endpoints | Description |
|---|---|---|
| **Agreement API** | `PUT /v1/consent/agreement` | Register a consent after an individual has granted permission |
| **Debt API** | `GET /v1/debt` | Retrieve debt information using an access token from the authorization code flow |
| **Debt API** | `GET /v1/debt/{id}` | Retrieve debt information by consent ID (client credentials flow) |
| **Debt API** | `DELETE /v1/debt/{id}` | Revoke an existing consent |
| **Debt API** | `GET /v1/debt/{id}/status` | Check whether a consent is still active |
| **Consents Feed API** | `GET /feed/v1/consent` | Poll for consent lifecycle events (created, archived) |
| **Consents Feed API** | `GET /feed/v1/consent/lastSequenceNr` | Get the newest sequence number in the feed |
| **Consents Feed API** | `GET /feed/v1/consent/firstSequenceNr` | Get the oldest sequence number in the feed |

!!! tip "Looking for structured reference pages?"
    Each topic is also covered in detail with tables and flow diagrams:
    - [Consent API overview](consent/index.md) — base URLs, auth flows, and scopes
    - [Auth endpoint](consent/auth-endpoint.md) — authorization request parameters
    - [Token endpoint](consent/token-endpoint.md) — token exchange and response format
    - [Collect debt](consent/collect-debt.md) — debt retrieval by consent
    - [Consent feed](consent/consent-feed.md) — event polling guide
    - [Scopes](consent/scopes.md) — available scopes and duration options

!!swagger openapi.json!!
