---
tags:
  - debt-delivery
---

# Managing changes in data delivery

Over time, financial institutions merge, change IT service providers, or transfer debt portfolios between entities. This page explains the concepts and what happens to your data during these transitions.

!!! info "Looking for step-by-step instructions?"
    See [Onboarding & scenarios](../howto/deliver-debt-data/Onboarding_and_Scenarios.md) for the operational how-to guide.

---

## Roles and terminology

Understanding the distinction between the legal owner of debt and the technical operator of an integration is key to following the scenarios below.

| Term | What it is | Examples |
|---|---|---|
| **Creditor / Financial Institution (FI)** | The legal entity that owns the debt relationship with the individual. This is who the debt belongs to. | A bank, a credit card company |
| **IT service provider** | The technical entity that operates the integration with Norsk Gjeldsinformasjon. Can be the FI itself or a third-party company. | A bank's internal IT department, a fintech platform, a core banking system vendor |
| **ProviderID** | Identifies the technical integration (ISO 6523 format: `{Authority}:{Identifier}`). One FI can use multiple providers. | `9908:999888777` |
| **financialInstitutionID** | Identifies the legal entity that owns the customer relationship. Norwegian entities use the organisation number. Non-Norwegian entities use ISO 6523 format (e.g. `0007:5561234123`). | `999888777` |

### Common relationships

| Relationship | Description |
|---|---|
| **FI is its own provider** | A bank runs its own integration directly with Norsk Gjeldsinformasjon. The FI and the provider are the same legal entity. |
| **FI uses a third-party provider** | A bank contracts a fintech or core banking vendor to operate the integration. The FI owns the debt, the provider operates the technical connection. |
| **Provider serves multiple FIs** | A single provider operates integrations for several creditor clients. Each FI client has its own `getalldata` URL. |

---

## The general cutover principle

All transition scenarios — mergers, provider changes, and portfolio transfers — follow the same fundamental pattern:

| Party | Required API behaviour |
|---|---|
| **Transferring party** | Returns HTTP 200 with an **empty `customers` array**. Must not return 4xx, 5xx, or timeouts. |
| **Acquiring party** | Returns HTTP 200 with the **complete dataset** for the customers being transferred. |

!!! danger "Empty list, never an error"
    An error instead of an empty list causes Norsk Gjeldsinformasjon to reuse previously retrieved data. This results in **duplicate debt records** for the affected individuals.

The two parties coordinate the switch between themselves. The critical operation is Norsk Gjeldsinformasjon's morning `getalldata` call: one provider must return an empty `customers` array, while the other returns the complete dataset. The exact timing must be agreed so that no gap or overlap occurs.

!!! warning "Timing matters"
    Perform switches at the **start of a business week**. By following the procedure described here, no support from Norsk Gjeldsinformasjon is needed during the transition.

---

## Scenario: A creditor switches IT service provider

A financial institution moves from one IT service provider to another. The FI itself stays the same, and the debt ownership does not change.

- The **old provider** stops returning data (empty array).
- The **new provider** starts returning the complete dataset.

This applies whether the FI was previously self-providing and moving to a third party, or moving between two third-party providers.

!!! tip "Same cutover pattern"
    This is identical to the general cutover principle above. No special handling is needed beyond the coordination between the two providers.

See [New IT service provider](../howto/deliver-debt-data/Onboarding_and_Scenarios.md#2-new-it-service-provider) for the how-to steps.

---

## Scenario: Two creditor organizations merge

When FI A merges into FI B, the debt data must follow the legal entity.

- The **transferring FI** (the entity being absorbed) stops returning data (empty array).
- The **acquiring FI** (the surviving entity) returns the complete dataset, including the transferred debt.

!!! warning "Combined scenarios"
    If a merger and a provider change happen at the same time, the cutover procedure is the same — handle them simultaneously by coordinating both sides as described in the general principle above.

See [Merger with another FI](../howto/deliver-debt-data/Onboarding_and_Scenarios.md#3-merger-with-another-financial-institution) for the how-to steps.

---

## Scenario: A debt portfolio moves between providers

A subset of debt moves from one provider to another. This can happen in two situations:

### Portfolio moves between providers for the same FI

The FI keeps the same legal identity but splits or reassigns its debt portfolios across providers:

- A portfolio is moved from provider A to provider B (both serving the same FI).
- Provider A returns an empty array for the moved customers.
- Provider B returns the complete data for those customers.

### Portfolio moves from one FI to another FI

Debt ownership transfers from FI A to FI B (e.g., a loan book sale):

- FI A's provider returns an empty array for the transferred customers.
- FI B's provider returns the complete data for those customers.
- The providers may be the same technical company (if both FIs use the same provider) or different ones — the cutover pattern is identical.

!!! tip "Same cutover pattern"
    Whether it's the same FI with two providers or two different FIs, the API-level cutover follows the general principle exactly. The providers coordinate the switch.

---

## Scenario: A provider starts serving a new FI client

An IT service provider that already has an integration with Norsk Gjeldsinformasjon begins serving a new financial institution client. This is the standard "new FI" setup, but the provider can reuse its existing technical connection.

- If the provider already has an integration: a new `getalldata` URL is configured for the new FI. The provider's existing technical setup (IP addresses, server certificate) can typically be reused.
- If the provider has no existing integration: a full setup is required (see [New financial institution](../howto/deliver-debt-data/Onboarding_and_Scenarios.md#1-new-financial-institution)).

Over time, as the new FI's own portfolio setup matures or their previous provider is decommissioned, the portfolio transfer cutover from the old provider to the new one follows the general principle above.

See [Provider serving a new FI client](../howto/deliver-debt-data/Onboarding_and_Scenarios.md#4-provider-serving-a-new-fi-client) for the how-to steps.