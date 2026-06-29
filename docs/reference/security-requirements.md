---
tags:
  - debt-delivery
  - debt-search
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
| CA | Standard Mozilla trusted CA list — no need to send to Norsk Gjeldsinformasjon |

## Your enterprise client certificate

| Requirement | Value |
|---|---|
| KeyUsage | `digitalSignature` (critical) |
| Subject.organizationIdentifier | Your organisation number with `NTR` prefix, per **ETSI EN 319 412-1**. Example: `NTRNO-920013015`. Only `NTR` (National Trade Registry) identifier type is supported. |
| Ownership | Must be owned by the legal entity sending data |
| Environments | Separate certificates for test and production |

For details on the `organizationIdentifier` format, see [ETSI EN 319 412-1 V1.6](https://www.etsi.org/deliver/etsi_en/319400_319499/31941201/01.06.01_60/en_31941201v010601p.pdf).

| Environment | Certificate type | Accepted issuers |
|---|---|---|
| Test | Enterprise client certificate (SEID 2.0) | Buypass or Commfides |
| Production | Enterprise client certificate (SEID 2.0) | Buypass or Commfides |
| Non-Norwegian FIs | PSD2 / eIDAS QWAC | Approved QTSP |

## Certificate renewal timelines

| Environment | Notify Norsk Gjeldsinformasjon | Norsk Gjeldsinformasjon installs |
|---|---|---|
| Test | 10 business days before expiry | Within 5 business days |
| Production | 20 business days before expiry | Within 10 business days |

!!! note "Transitions"

    Norsk Gjeldsinformasjon accepts both old and new enterprice certificates during transitions — no downtime required if timelines are followed.

    For rotating or renewing TLS certificates, there's typically no need to coordinate with Norsk Gjeldsinformasjon.
