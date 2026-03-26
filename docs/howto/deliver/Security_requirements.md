[deliver-security.md](https://github.com/user-attachments/files/26279613/deliver-security.md)
# Security requirements

All APIs exchanging debt information must use mutual TLS (mTLS) with valid enterprise certificates. These are **mandatory prerequisites** before any test or production access is granted.

!!! danger "No tokens or OAuth"
    The debt delivery API uses **certificate-based mutual TLS only**. There is no application-level authentication using tokens, sessions, or OAuth.

## Checklist

- [ ] TLS 1.2 or newer on all your endpoints
- [ ] Mutual TLS (mTLS) configured — both client and server authenticate
- [ ] EV or OV TLS certificate on your server endpoint
- [ ] Enterprise client certificate (SEID 2.0) from Buypass or Commfides
- [ ] **Separate** certificates for test and production
- [ ] Buypass root CA bundle installed in your Trusted Root store
- [ ] Only NSM-recommended cipher suites in use

## Your server TLS certificate

| Requirement | Value |
|---|---|
| Hash algorithm | SHA-256 or stronger |
| Key size | RSA ≥ 2048 bits (3072 preferred) or EC ≥ 256 bits |
| ExtendedKeyUsage | TLS Web Server Authentication |
| SAN | `DNS:<your API FQDN>` |
| Norwegian issuers | Comfides or Buypass (EV or OV) — no need to send to NoGi |
| Non-Norwegian FIs | EV from Mozilla trusted CA list, or PSD2/eIDAS QWAC — must send to NoGi |

## Your enterprise client certificate

| Requirement | Value |
|---|---|
| KeyUsage | `digitalSignature` (critical) |
| Subject.SerialNumber | Your organisation number (ISO 6523) |
| Ownership | Must be owned by the legal entity sending data |
| Environments | Separate certificates for test and production — mandatory |

## Certificate renewal timelines

| Environment | Notify NoGi | NoGi installs |
|---|---|---|
| Test | 10 business days before expiry | Within 5 business days |
| Production | 20 business days before expiry | Within 10 business days |

!!! note "Transitions"
    NoGi accepts both old and new certificates during transitions — no downtime required if timelines are followed.
