---
tags:
  - faq
---

# Frequently asked questions

<!--
FAQ - cross-cutting

Answers are organized by user group so you can focus on what's relevant to you.
-->

## Questions for debt-lookup services (consent-based)

These questions apply if you are integrating with the consent API to look up unsecured debt for individuals.

### How do I get started?

Reach out to [Norsk Gjeldsinformasjon](https://www.norskgjeld.no/kontakt-oss/) to establish an agreement and receive your client ID and client secret.

See [Get started](get-started/index.md) for step-by-step instructions for the pre-production environment.

### What is the difference between regular consent and integrated consent?

With **regular consent**, the individual is redirected from your platform to Norsk Gjeldsinformasjon, where they authenticate with ID-porten and confirm the consent before being redirected back to you.

With **integrated consent**, you handle the consent process yourself — you identify the individual and manage the consent within your own platform. The individual never leaves your site.

See [Select an integration](howto/select-integration.md) to decide which is right for you.

### What OAuth 2.0 flows are supported?

We support:

- **Authorization Code flow** — used when an individual needs to authenticate and grant consent (regular consent).
- **Client Credentials flow** — used to obtain an access token for server-to-server communication, e.g. registering a consent or looking up debt with an existing consent.

See the [Reference](reference/index.md) page for details on each flow.

### What scopes are available?

| Scope | Use |
|---|---|
| `debt.unsecured.presentation` | Debt data will be presented to the individual |
| `debt.unsecured.processing` | Debt data will be used for assessing a loan/credit application |

Scopes can be extended with a duration suffix: `debt.unsecured.presentation.100` grants a consent valid for 100 days.

See [Scopes](reference/consent/scopes.md) for the full reference.

### What is consent duration and how do I set it?

If no duration is specified, a single-use consent is created — usable within a few minutes, once only. To set a duration, append the number of days to the scope identifier: `debt.unsecured.presentation.100` makes the consent active for 100 days.

Note that individuals can withdraw their consent at any time, regardless of duration.

### Do I need client certificates (Virksomhetssertifikat, SEID)?

No. The consent and debt APIs do **not** require 2-way TLS, so client certificates are not needed.

### How do I test with synthetic National Identity Numbers?

In pre-production, use one of these synthetic NINs:

- `14842249091`
- `29868099311`

At the ID-porten login screen, choose **TestID** — no password required. These NINs have mocked debt data that will return a populated response.

See [Get started](get-started/index.md) for a full step-by-step test walkthrough.

### What base URLs should I use?

| Environment | Base URL |
|---|---|
| Pre-production | `https://access-preprod.norskgjeld.no` |
| Production | `https://access.norskgjeld.no` |

The debt API uses `https://api-preprod.norskgjeld.no` in pre-production and `https://api.norskgjeld.no` in production.

### How often is the debt data updated?

On every query we contact the financial institutions where the individual has debt to fetch the latest data. If a financial institution fails to answer within the allotted time, we fall back to cached data. Our cached data is fetched every morning and updated by the financial institutions throughout the day as soon as debt for an individual is changed.

### What happens if a creditor doesn't respond?

If a creditor fails to answer within the allotted time, we fall back to cached data. This is reported in the debt information response so you can see which creditors were missing.

### How do I get notified about changes to consents?

You can subscribe to the consent event feed to receive notifications when consents are created, changed, or revoked. See [Get notified about changes to consents](howto/consent-notifications.md) for details.

---

## Questions for debt-lookup services (without consent)

These questions apply if you are a financial institution (credit bureau or lender) querying debt information directly without requiring individual consent.

### Who can access debt information without consent?

Access is regulated by the [Norwegian Debt Information Act](https://lovdata.no/dokument/NL/lov/2017-06-16-47) (Gjeldsinformasjonsloven). Only financial institutions that are permitted under this regulation can query the Search API without consent.

### How is this different from the consent-based API?

The consent-based API requires an individual to grant consent before you can look up their debt. The Search API (without consent) is available to authorized financial institutions directly. The debt data format is the same, but the consent-based response includes the names of creditors.

---

## Questions for debt data delivery

These questions apply if your financial institution sends debt data to Norsk Gjeldsinformasjon (the "deliver debt data" APIs).

### What endpoints does my system need to expose?

Your system must expose two endpoints that Norsk Gjeldsinformasjon calls:

- **`getalldata`** — Daily batch retrieval of all customer debt data
- **`getDataForSSN`** — On-demand lookup for a single National Identity Number

You also call **`pushUpdates`** on Norsk Gjeldsinformasjon to push credit events within 5 minutes.

See the [Deliver debt data API reference](reference/deliver-debt-data/index.md) for details.

### How are monetary amounts encoded?

All monetary amounts are in **NOK × 100**. Example: 100 NOK = `10000`. Interest rates: 10.20% = `1020`.

### What validation rules apply to the data I deliver?

All data is validated against a set of rules — any violation causes the data to be rejected. See [Data validation](reference/deliver-debt-data/validation.md) for the full rule set.

---

## Questions about quarterly debt reports

These questions apply if you receive quarterly packaged data via SFTP.

### When must the NIN list be ready?

The NIN list must be present on the SFTP server **by the last day of each quarter** (the day before the quarterly run). For example, for the Q2 run on April 1, the file must be available by March 31. If the file is missing, a failure report will be generated indicating "NIN list not found."

### When can I delete the NIN list?

When the job is complete and the data package is present on your SFTP server, it is safe to remove the NIN list.

### Why are some NINs' loan arrays empty?

If Norsk Gjeldsinformasjon does not find any debt linked to a specific NIN in the debt registry, an empty array is returned for that NIN.

### What do the different report files contain?

| File | Contents |
|---|---|
| Data package (`{orgno}.gzip`) | Packaged debt data for all NINs on your list |
| Progress report | List of invalid NINs, duplicate NINs, receiver organization number, and timestamp |
| Failure report | Triggered when the NIN list is missing, has wrong file name, or has an invalid organization number |

---

## General questions

### How do I contact Norsk Gjeldsinformasjon?

- General inquiries and onboarding: [contact form](https://www.norskgjeld.no/kontakt-oss/)
- Support: [support@norskgjeld.no](mailto:support@norskgjeld.no)

### What is unsecured debt?

Unsecured debt includes credit card debt, personal loans, and other forms of non-secured borrowing.

### How do I contribute to this documentation?

See [Contribute](contributing.md) for instructions on how to suggest changes or additions to this documentation site.

### What is the difference between pre-production and production?

Pre-production (`preprod`) is a test environment where you can verify your integration using synthetic National Identity Numbers. Once your integration is verified, you switch to production URLs (without the `-preprod` suffix). You need to coordinate the go-live with Norsk Gjeldsinformasjon.