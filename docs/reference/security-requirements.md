---
tags:
  - debt-delivery
  - debt-search
---

# Security requirements

All APIs exchanging debt information use mutual TLS (mTLS). The type of certificate you need depends on which role your system plays:

- **You are the client** calling NoGi's push or search APIs → you need an **enterprise client certificate (SEID 2.0 / Virksomhetssertifikat)** for your system to identify itself.
- **NoGi is the client** calling your exposed endpoints (`getalldata`, `getDataForSSN`) → your server needs a **TLS server certificate** and must verify NoGi's enterprise client certificate.

!!! note "Consent APIs use bearer tokens"
    The consent and debt-lookup APIs use OAuth 2.0 access tokens (bearer tokens) for authentication, not mTLS. Enterprise client certificates are not required for these APIs.

!!! danger "No tokens or OAuth for debt delivery"
    The debt delivery API uses **certificate-based mutual TLS only**. There is no application-level authentication using tokens, sessions, or OAuth.

---

## Checklist

- [ ] TLS 1.2 or newer on all your endpoints
- [ ] Mutual TLS (mTLS) configured — both client and server authenticate
- [ ] TLS server certificate on your endpoint (Mozilla trusted CA)
- [ ] Enterprise client certificate (SEID 2.0 / Virksomhetssertifikat) — from Buypass or Commfides — for client authentication
- [ ] NoGi's outbound IP `92.62.32.241` whitelisted (if using IP-based access control)
- [ ] Buypass root CA bundle installed to verify NoGi's client certificate (if using Buypass)

---

## Your server TLS certificate

This applies when your system acts as a **server** — NoGi connects to your endpoints (`getalldata`, `getDataForSSN`).

| Requirement | Notes |
|---|---|
| Issuer | Any CA in the Mozilla trusted root store |
| Minimum TLS version | TLS 1.2 |
| SAN | Must cover your API hostname. Wildcard (`*.example.com`) is accepted. |
| Notify NoGi | Not required — use standard TLS certificate renewal procedures |

A standard TLS/SSL certificate from any Mozilla-trusted CA is sufficient. You do **not** need to send your server TLS certificate to Norsk Gjeldsinformasjon.

---

## Your enterprise client certificate (SEID 2.0 / Virksomhetssertifikat)

This applies when your system acts as a **client** — you call NoGi's push or search APIs.

| Requirement | Value |
|---|---|
| KeyUsage | `digitalSignature` (critical) — additional KeyUsage flags are acceptable |
| Subject.organizationIdentifier | Your organisation number with `NTR` prefix, per [ETSI EN 319 412-1](https://www.etsi.org/deliver/etsi_en/319400_319499/31941201/01.06.01_60/en_31941201v010601p.pdf). Example: `NTRNO-920013015`. Only `NTR` (National Trade Registry) identifier type is supported. |
| Ownership | Must be owned by the legal entity sending data |
| Approved CAs | Buypass or Commfides |

| Environment | Certificate type | Accepted issuers |
|---|---|---|
| Test | Enterprise client certificate (SEID 2.0) | Buypass or Commfides |
| Production | Enterprise client certificate (SEID 2.0) | Buypass or Commfides |
| Non-Norwegian FIs | PSD2 / eIDAS QWAC | Approved QTSP |

---

## NoGi's enterprise client certificate

When Norsk Gjeldsinformasjon connects to your endpoints (`getalldata`, `getDataForSSN`), NoGi identifies itself using its own enterprise client certificate (Virksomhetssertifikat). Your server must be configured to **verify** this certificate — not just accept any client certificate — to confirm that the connecting party is Norsk Gjeldsinformasjon.

- NoGi's outbound traffic originates from **`92.62.32.241`** (both pre-production and production).
- Your server needs the **Buypass root CA bundle** (or equivalent for Commfides) installed to validate NoGi's client certificate.

For details on NoGi's enterprise certificate, see [Enterprise certificates](enterprise-certificates.md).

---

## Certificate renewal timelines

| Environment | Notify Norsk Gjeldsinformasjon | NoGi installs |
|---|---|---|
| Test | 10 business days before expiry | Within 5 business days |
| Production | 20 business days before expiry | Within 10 business days |

!!! note "Transition overlap"

    Norsk Gjeldsinformasjon accepts both old and new enterprise certificates during transitions — no downtime required if timelines are followed.

    For rotating or renewing **TLS server certificates**, there is typically no need to coordinate with Norsk Gjeldsinformasjon.