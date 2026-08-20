---
tags:
  - debt-delivery
  - certificate
---

# Enterprise certificates

This page describes the enterprise client certificates (SEID 2.0 / Virksomhetssertifikat) used by Norsk Gjeldsinformasjon to authenticate when connecting to financial institutions.

These certificates are presented during the mTLS handshake when NoGi calls your endpoints (`getalldata`, `getDataForSSN`) to retrieve debt information. Your server must verify this certificate to confirm that the connecting party is Norsk Gjeldsinformasjon.

## Applicability

- **Relevant for**: Financial institutions obliged to deliver debt information.
- **Not applicable to**: Search API or consent solution users.

## Certificate details

### Production

| Property | Value |
|---|---|
| Subject | `C = NO, O = NORSK GJELDSINFORMASJON AS, CN = NORSK GJELDSINFORMASJON AS` |
| Organization identifier | `NTRNO-920013015` |
| Issuer | `CN = Buypass Class 3 CA G2 ST Business, O = Buypass AS` |
| Valid from | Jan 2, 2025 |
| Valid until | Feb 9, 2028 |
| Key usage | Digital Signature, Key Encipherment (critical) |
| Key size | RSA 3072 bit |
| SHA-256 fingerprint | `BE:70:14:F9:DD:45:96:56:87:6C:14:EE:A8:DB:E0:9C:5A:8B:44:FD:5F:A3:32:68:27:F7:20:37:74:7B:9A:6C` |

[Download production certificate](assets/certificates/nogi-enterprise-production.crt)

### Test (pre-production)

| Property | Value |
|---|---|
| Subject | `C = NO, O = NORSK GJELDSINFORMASJON AS, CN = NORSK GJELDSINFORMASJON AS test` |
| Organization identifier | `NTRNO-920013015` |
| Issuer | `CN = Buypass Class 3 Test4 CA G2 ST Business, O = Buypass AS` |
| Valid from | Jan 2, 2025 |
| Valid until | Jan 2, 2028 |
| Key usage | Digital Signature, Key Encipherment (critical) |
| Key size | RSA 3072 bit |
| SHA-256 fingerprint | `44:F3:65:44:7B:B9:67:A2:85:8D:3F:38:62:7B:92:AF:D3:FC:63:D6:1B:C1:15:B9:7B:B4:41:4C:76:50:07:8E` |

[Download test certificate](assets/certificates/nogi-enterprise-test.crt)

## Verification

You can verify the certificate using OpenSSL:

```bash
# Extract issuer to confirm it's NoGi's certificate
openssl x509 -noout -issuer -in nogi-enterprise-production.crt

# Check validity dates
openssl x509 -noout -dates -in nogi-enterprise-production.crt

# Verify SHA-256 fingerprint
openssl x509 -noout -fingerprint -sha256 -in nogi-enterprise-production.crt
```

The test certificate can be identified by the issuer containing **Test4** in the CA name and by **CN = ... test** in the subject.

## When the certificate is used

- **GetAllData** — Runs daily (once every 24 hours). NoGi connects using the enterprise certificate to retrieve all debt data.
- **getDataForSSN** — On-demand lookups. Synthetic test traffic in pre-production generates lookups on synthetic individuals typically every few minutes.

## CA chain

NoGi's enterprise certificates are issued under the following chain:

- **Production**: Buypass Class 3 CA G2 ST Business → Buypass Class 3 Root CA G2 ST
- **Test**: Buypass Class 3 Test4 CA G2 ST Business → Buypass Class 3 Test4 Root CA G2 ST

Your server needs the **Buypass root CA bundle** installed in your Trusted Root store to validate NoGi's client certificate.

!!! note "Root CA endpoints"

    Production:
    - CRL: `http://crl.buypassca.com/BPCl3CaG2STBS.crl`
    - OCSP: `http://ocspbs.buypassca.com`
    - CA certificate: `http://crt.buypassca.com/BPCl3CaG2STBS.cer`

