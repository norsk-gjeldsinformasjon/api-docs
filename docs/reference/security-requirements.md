---
tags:
  - debt-delivery
  - fi-lookup
---

# Security requirements

All APIs exchanging debt information must use mutual TLS (mTLS) with valid enterprise certificates. These are **mandatory prerequisites** before any test or production access is granted.

!!! danger "No tokens or OAuth"
    The debt delivery API uses **certificate-based mutual TLS only**. There is no application-level authentication using tokens, sessions, or OAuth.

## Checklist

- TLS 1.2 or newer on all your endpoints
- Mutual TLS (mTLS) configured — both client and server authenticate
- EV or OV TLS certificate on your server endpoint (Mozilla trusted CA)
- Enterprise client certificate (SEID 2.0) from Buypass or Commfides — for business/client authentication, not server TLS
- **Separate** certificates for test and production
- Buypass root CA bundle installed in your Trusted Root store
- Only NSM-recommended cipher suites in use

## Your server TLS certificate

| Requirement | Value |
|---|---|
| Hash algorithm | SHA-256 or stronger |
| Key size | RSA ≥ 2048 bits (3072 preferred) or EC ≥ 256 bits |
| ExtendedKeyUsage | TLS Web Server Authentication |
| SAN | `DNS:<your API FQDN>` |
| CA | Standard Mozilla trusted CA list — no need to send to NoGi |

## Your enterprise client certificate

| Requirement | Value |
|---|---|
| KeyUsage | `digitalSignature` (critical) |
| Subject.organizationIdentifier | Your organisation number (ISO 6523, NTR prefix). Example: `NTRNO-920013015` |
| Ownership | Must be owned by the legal entity sending data |
## Your enterprise client certificate

| Requirement | Value |
|---|---|
| KeyUsage | `digitalSignature` (critical) |
| Subject.organizationIdentifier | Your organisation number (ISO 6523, NTR prefix). Example: `NTRNO-920013015` |
| Ownership | Must be owned by the legal entity sending data |
| Environments | Separate certificates for test and production |

| Environment | Certificate type | Accepted issuers |
|---|---|---|
| Test | Enterprise client certificate (SEID 2.0) | Buypass or Commfides |
| Production | Enterprise client certificate (SEID 2.0) | Buypass or Commfides |
| Non-Norwegian FIs | PSD2 / eIDAS QWAC | Approved QTSP |

## Certificate renewal timelines

| Environment | Notify NoGi | NoGi installs |
|---|---|---|
| Test | 10 business days before expiry | Within 5 business days |
| Production | 20 business days before expiry | Within 10 business days |

!!! note "Transitions"

    NoGi accepts both old and new enterprice certificates during transitions — no downtime required if timelines are followed.

    For rotating or renewing TLS certificates, there's typically no need to coordinate with Norsk Gjeldsinformasjon.
