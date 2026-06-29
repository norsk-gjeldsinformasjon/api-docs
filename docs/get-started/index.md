---
tags:
  - consent
---

# Get started

<!--
Tutorials - Learning Oriented

Teach users how to achieve something step-by-step, aimed at beginners. Focus on a specific goal with clear, sequential instructions.
-->

Norsk Gjeldsinformasjon provides API for retrieving information about debt for individuals. Financial institutions that act as credit bureaus or lenders can query information when assessing lenders for loans or credit. Other organizations can ask individuals for consent to access information about their debt.

If you need help choosing what type of integration is right for you, see [How-to: Select an integration](../howto/select-integration.md)

Reach out to [Norsk Gjeldsinformasjon](https://www.norskgjeld.no/kontakt-oss/) for more information about using these services.


## Integrating with Norsk Gjeldsinformasjon API

When integrating with Norsk Gjeldsinformasjon, you will initially get access to a preproduction environment.

## Integrated consent

### Preparation

Before using integrated consent, you will need sign up by contacting [Norsk Gjeldsinformasjon](https://www.norskgjeld.no/kontakt-oss/). You will be provided with client credentials to the preproduction environment.

### Authorize

You can test authorization by following [How-to: Authorize](../howto/authorize.md). This is typically handled by a library in production code.

You should now be able to use your credentials to fetch access tokens.

### Register consent

When you have received a consent from an individual, you need to register this with Norsk Gjeldsinformasjon.

This is done by calling `/v1/consent/agreement`.

The consent can now be used to fetch debt information. The individual will see the consent when logged in to "Min Gjeld"

See our [OpenAPI definition](../reference/openapi.md) for details.

### Delete consent

If an individual withdraws their consent, you will need to register this with Norsk Gjeldsinformasjon.

This is done by calling `/v1/debt/{consent-id}`

The consent can no longer be used to fetch debt information. The individual will see the consent as "archived" when logged in to "Min Gjeld"

See our [OpenAPI definition](../reference/openapi.md) for details.

## Regular consent

With regular consent, individuals are redirected from your platform to Norsk Gjeldsinformasjon.
They identify with ID-porten and confirm the consent before being redirected back to you.
The service uses a redirect-based flow adhering to OAuth2.0 and OpenID Connect standards.

The debt information is delivered in the same format as our debt query API, but since it is
provided with the end user's consent, we also include the name of the creditors.

### Preparation

Before using regular consent, you need to enter into an agreement with Norsk Gjeldsinformasjon
by emailing us at [support@norskgjeld.no](mailto:support@norskgjeld.no).

When you have signed an agreement, we will send your client id and client secret. You must provide
us with the URLs where you want to receive the callback after the consent flow finishes. This is
not required if you only intend to [manage consents externally](../howto/external-consent-management.md).

You should also decide on what [OAuth 2.0 flow](../reference/index.md) you want to use.

You should provide us with:

| Parameter       | Explanation                                                                                              |
|-----------------|----------------------------------------------------------------------------------------------------------|
| Organization ID | Your organization ID in Enhetsregisteret                                                                 |
| Callback URI(s) | The URL(s) you want the browser returned, ex: https://api-eksempel.no/v1/callback                        |
| Purpose         | Whether the debt data will be used for `presentation` or `processing`                                    |
| Duration        | By default, consents are single-use. Specify duration if required. See [duration](../reference/index.md) |
| Flow            | The flow you plan on using                                                                               |

You will receive a clientId and credentials that can be used when talking to our API.

!!! note "TLS not required"
    This service does not require 2-way TLS, so client certificates (Virksomhetssertifikat, SEID)
    are **not** required.

!!! tip "Outbound IP addresses"
    If you plan to run from a provider where you share multiple outbound IP addresses (e.g. cloud
    providers), you should purchase fixed outbound IP address(es).

### Testing

Before you can start testing you will need a client with registered callback URIs and a BankID test
user.

This can be created
at [https://ra-preprod.bankidnorge.no/#/generate](https://ra-preprod.bankidnorge.no/#/generate).
Generate an NIN and set the BankID type to netcentric. When you use this BankID with ID-porten for
the first time, you will be asked if you want to add additional info which you can skip.

In preprod (BankID TestBank) the one-time code is always `otp`, and the password is `qwer1234`

!!! note "Mocked debt data"
    There will not be any loan information stored on the BankID test person you have created in
    our test environment, so the debt API will not list any creditors. Mocked debt data is
    available on these synthetic personal numbers: `14842249091` and `29868099311`.

### Authorize

You can test authorization by following [How-to: Authorize](../howto/authorize.md). This is typically handled by a library in production code.

You should now be able to use your credentials to fetch access tokens.


### Fetch debt

To fetch debt, you will need to call `/v1/debt` endpoint and provide an access token from the previous step.

See our [OpenAPI definition](../reference/openapi.md) for details.
