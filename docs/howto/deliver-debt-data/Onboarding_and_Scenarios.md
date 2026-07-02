---
tags:
  - debt-delivery
---

# Deliver debt data — Onboarding

Before you can deliver debt data to Norsk Gjeldsinformasjon, a signed agreement must be in place and your technical setup must be registered.

!!! info "Understanding the concepts"
    For a conceptual overview of roles (FI, provider, providerID) and how mergers, provider changes, and portfolio transfers work, see [Managing changes in data delivery](../../explanation/delivery-changes.md).

## Choose your scenario

| Scenario | Description |
|---|---|
| [1. New financial institution](#1-new-financial-institution) | First-time integration with no prior connection to Norsk Gjeldsinformasjon |
| [2. New IT service provider](#2-new-it-service-provider) | Migrating to a new provider — existing integration or not |
| [3. Merger with another FI](#3-merger-with-another-financial-institution) | Handling data transfer between merging institutions |
| [4. Provider serving a new FI client](#4-provider-serving-a-new-fi-client) | An IT service provider starts serving a new financial institution |

---

## 1. New financial institution

Send a request to [post@norskgjeld.no](mailto:post@norskgjeld.no) with:

- Organisation number and legal name of the financial institution
- Organisation number and legal name of the IT service provider (if applicable)
- Base URL for `getalldata` in both production and test — must end with `/ws.norskgjeld.no/push/rest/v1/debt`
- Static IP addresses for push updates in both environments
- Enterprise certificate (SEID 2.0) — issued by Buypass or Commfides

!!! note "What happens next"
    Norsk Gjeldsinformasjon will configure your FI in both test and production. You will receive test access details and can begin [mandatory testing](Testing_and_go-live.md). See [Security requirements](../../reference/security-requirements.md) for certificate and authentication requirements.

---

## 2. New IT service provider

**If the new provider already has an integration with Norsk Gjeldsinformasjon**, they only need to establish a new `getalldata` URL and assess whether to reuse or update static IP addresses.

**If not**, follow Scenario 1.

!!! danger "Critical: cutover procedure"
    The old provider must respond with an **empty list** (HTTP 200 + empty array) — never an error. An error causes previously retrieved data to be reused, resulting in duplicate debt records.

    Perform switches at the **start of a business week**. No support on weekends or public holidays.

---

## 3. Merger with another financial institution

| Party | Required API behaviour |
|---|---|
| Transferring FI | HTTP 200 with empty customer array. Must not return 4xx, 5xx, or timeouts. |
| Acquiring FI | HTTP 200 with the complete dataset. |

!!! warning "Note"
    An error instead of an empty list causes duplicate debt records. Mergers should be executed at the start of a business week.

---

## 4. Provider serving a new FI client

An IT service provider that already has an integration with Norsk Gjeldsinformasjon starts serving a new financial institution client.

Provide to [post@norskgjeld.no](mailto:post@norskgjeld.no):

- A new `getalldata` URL for the new FI client
- Static IP addresses
- Organisation number and legal name of the financial institution being served

!!! tip "The provider handles the technical side"
    Since the provider already has an established integration, this is primarily about configuring a new endpoint and certificate for the new FI client — not a full new setup.
