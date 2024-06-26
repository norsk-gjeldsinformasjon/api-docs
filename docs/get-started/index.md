# Get started

<!--
Tutorials - Learning Oriented

Teach users how to achieve something step-by-step, aimed at beginners. Focus on a specific goal with clear, sequential instructions.
-->

Norsk Gjeldsinformasjon provides API for retrieving information about debt for individuals. Financial institutions that act as credit bureaus or lenders can query information when assessing lenders for loans or credit. Other organizations can ask individuals for consent to access information about their debt.

If you need help choosing what type of integration is right for you, see [How-to: Choose integration](../howto/choose_integration.md).

Reach out to [Norsk Gjeldsinformasjon](https://www.norskgjeld.no/kontakt-oss/) for more information about using these services.


## Integrating with Norsk Gjeldsinformasjon API

When integrating with Norsk Gjeldsinformasjon, you will initially get access to a preproduction environment.

## Regular consent

### Preparation

Before using regular consent, you will need sign up by contacting [Norsk Gjeldsinformasjon](https://www.norskgjeld.no/kontakt-oss/). You will be provided with client credentials to the preproduction environment.

You should decide on what [OAuth 2.0 flow](../reference/index.md) you want to use.

You should provide us with:

| Parameter       | Explanation                                                                                              |
|-----------------|----------------------------------------------------------------------------------------------------------|
| Organization ID | Your organization ID in Enhetsregisteret                                                                 |
| Callback URI(s) | The URL(s) you want the browser returned, ex: https://api-eksempel.no/v1/callback                        |
| Purpose         | Whether the debt data will be used for `presentation` or `processing`                                    |
| Duration        | By default, consents are single-use. Specify duration if required. See [duration](../reference/index.md) |
| Flow            | The flow you plan on using                                                                               |

You will receive a clientId and credentials that can be used when talking to our API.


### Authorize

You can test authorization by following [How-to: Authorize](../howto/consent_authorize.md). This is typically handled by a library in production code.

You should now be able to use your credentials to fetch access tokens.


### Fetch debt

To fetch debt, you will need to call `/v1/debt` endpoint and provide an access token from the previous step.

See our [OpenAPI definition](../reference/openapi.md) for details.


## Integrated consent

### Preparation

Before using integrated consent, you will need sign up by contacting [Norsk Gjeldsinformasjon](https://www.norskgjeld.no/kontakt-oss/). You will be provided with client credentials to the preproduction environment.

### Authorize

You can test authorization by following [How-to: Authorize](../howto/consent_authorize.md). This is typically handled by a library in production code.

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
