---
tags:
  - integration
  - ip-address
  - security
  - important
---

# Outbound IP address change

!!! danger "Action required by October 6, 2026"
    Norsk Gjeldsinformasjon is updating its outbound IP addresses. All integration partners **must update their firewall rules or IP whitelists** to include the new IPs.

---

We are updating our external outbound IP addresses to improve network segmentation and security across our environments. This page provides all the technical details you need to update your firewall rules or IP whitelists.

## Who needs to act

This change affects integration partners in these scenarios:

- **Debt data delivery** — if your system exposes `getAllData` or `getDataForSSN` endpoints that Norsk Gjeldsinformasjon calls to retrieve debt data
- **Quarterly debt reports** — if you receive data packages from Norsk Gjeldsinformasjon

If neither applies to you, no action is needed.

## Current setup

- **Single shared IP for all environments:** `92.62.32.241`

## New setup (effective October 6, 2026)

| Environment | New outbound IP |
|---|---|
| Pre-production (Preprod) | `217.144.76.6` |
| Production (Prod) | `217.144.76.7` |

The change will take effect on **October 6, 2026**. During the transition period, traffic may originate from both the old and new IPs.

## Action required

Please update your firewall or IP whitelist to include **all three** IP addresses:

1. `92.62.32.241` — existing (will be phased out)
2. `217.144.76.6` — new (Preprod)
3. `217.144.76.7` — new (Prod)

We recommend adding the new IPs as soon as possible to ensure uninterrupted service during the transition.

## FAQ

**Q: Will the old IP (`92.62.32.241`) stop working immediately on October 6?**

No. There will be a transition period where both old and new IPs are active. We will notify you before the old IP is fully decommissioned.

**Q: What if I only integrate with one environment (e.g., only Prod)?**

You still need to add the new production IP (`217.144.76.7`) and keep the old IP (`92.62.32.241`) during the transition. You do not need to add the Preprod IP.

**Q: When exactly will the change happen?**

The change will take effect on October 6, 2026. A reminder will be sent closer to the date.

**Q: Who do I contact if I have issues?**

Please contact our support team at [support@norskgjeld.no](mailto:support@norskgjeld.no).

## Timeline

| Date | Event |
|---|---|
| **Before October 6, 2026** | Reminder email sent to all integration partners |
| **October 6, 2026** | Change takes effect |
| **Transition period** | Both old and new IPs active (duration to be confirmed) |
| **TBD** | Old IP decommissioned — notified separately |