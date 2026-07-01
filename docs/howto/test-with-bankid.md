---
tags:
  - consent
---

# How do I test the consent flow with BankID

Use this guide if you need to exercise the BankID UI in the consent flow —
for example, to validate your own copy around BankID or to test the netcentric
one-time code prompt end-to-end.

For everyday testing, prefer the **TestID** path described in the
[Get started Testing section](../get-started/index.md#testing). TestID has no
password, no provisioning step, and lets you log in as the same synthetic NIN
that has mocked debt data.

## Generate a BankID test user

1. Go to [https://ra-preprod.bankidnorge.no/#/generate](https://ra-preprod.bankidnorge.no/#/generate).
2. Generate an NIN and set the BankID type to **netcentric**.
3. The first time you use this BankID with ID-porten, you will be asked to add
   additional info — you can skip that step.

## Preprod credentials

In preprod (BankID TestBank) the one-time code is always `otp`, and the
password is `qwer1234`.

## Seeing mocked debt data

The BankID test person you generate has no loan information in our test
environment, so the debt API will return an empty list for them. If you also
want to see a populated debt response, pass one of the synthetic NINs
`14842249091` or `29868099311` when calling the debt API, even though you
logged in as a different person.
