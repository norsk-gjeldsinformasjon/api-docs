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

All endpoints in this section use the pre-production base URLs. Replace with production URLs (without the `-preprod` suffix) when you go live.

## Quick start: Integrated consent flow (pre-production)

The fastest way to verify your integration is to run through the full consent lifecycle using `curl`. You need your **client ID** and **client secret** from Norsk Gjeldsinformasjon.

!!! tip "Which integration?"
    These examples illustrate the "integrated consent" flow where the client (you) receives and manages consent from the person.

### 1. Get an access token for the consent API

The consent API (`/v1/consent/agreement`) requires a token with the `consent.create` scope.

```bash
curl -X POST https://access-preprod.norskgjeld.no/oauth2/token \
  -u "YOUR_CLIENT_ID:YOUR_CLIENT_SECRET" \
  -d "grant_type=client_credentials" \
  -d "audience=https://api-preprod.norskgjeld.no/v1/consent/agreement" \
  -d "scope=consent.create"
```

A successful response looks like this:

```json
{
  "access_token": "eyJ...",
  "expires_in": 3599,
  "scope": "consent.create",
  "token_type": "bearer"
}
```

Save this `access_token` — you'll use it to register the consent.

### 2. Register a consent

Create a consent for a test individual (use one of the synthetic NINs: `14842249091` or `29868099311`):

```bash
curl -X PUT https://api-preprod.norskgjeld.no/v1/consent/agreement \
  -H "Authorization: Bearer ACCESS_TOKEN_FROM_STEP_1" \
  -H "Content-Type: application/json" \
  -d '{
    "nin": "14842249091",
    "scope_of_consent": "debt.unsecured.presentation",
    "consent_duration_days": 30,
    "client_consent_id": "my-unique-id-001"
  }'
```

Response:

```json
{
  "client_consent_id": "my-unique-id-001",
  "consent": {
    "id": "0dcec3d5-6844-4d2c-b972-83086064b111",
    "expires_at": "2025-08-26T00:00:00Z",
    "scope_of_consent": "debt.unsecured.presentation"
  }
}
```

Save the `id` field — that's the consent ID you'll use to fetch debt.

### 3. Get a token for the debt API

The debt API requires a different token with the `debt.unsecured.presentation` scope.

```bash
curl -X POST https://access-preprod.norskgjeld.no/oauth2/token \
  -u "YOUR_CLIENT_ID:YOUR_CLIENT_SECRET" \
  -d "grant_type=client_credentials" \
  -d "audience=https://api-preprod.norskgjeld.no/v1/debt" \
  -d "scope=debt.unsecured.presentation"
```

Save the returned `access_token` — you'll use it to look up and revoke debt data.

### 4. Look up debt using the consent

```bash
curl -X GET https://api-preprod.norskgjeld.no/v1/debt/0dcec3d5-6844-4d2c-b972-83086064b111 \
  -H "Authorization: Bearer ACCESS_TOKEN_FROM_STEP_3"
```

Response:

```json
{
  "ssn": "14842249091",
  "loans": [
    {
      "creditorName": "EXAMPLE LENDER",
      "loan": {
        "type": "chargeCard",
        "timestamp": "2022-11-03T00:00:00Z",
        "coBorrower": 2,
        "interestBearingBalance": 6069400,
        "nonInterestBearingBalance": 641000
      }
    }
  ],
  "numberOfCreditorsAnswered": 1,
  "numberOfcreditorsMissing": 0,
  "consent": {
    "exp": 1785312537,
    "id": "3649911c-a58a-4b76-9794-edd8c692e84f",
    "scope": "debt.unsecured.presentation"
  }
}
```

### 5. Revoke a consent

When an individual withdraws their consent, revoke it by consent ID (use the debt API token):

```bash
curl -X DELETE https://api-preprod.norskgjeld.no/v1/debt/0dcec3d5-6844-4d2c-b972-83086064b111 \
  -H "Authorization: Bearer ACCESS_TOKEN_FROM_STEP_3"
```

A `204 No Content` response means the consent was successfully revoked.

For more details on each step, see the [Authorization how-to](../howto/authorize.md), [debt lookup with consent](../howto/lookup-debt-with-consent.md), and the [Consent API reference](../reference/consent/index.md).


## Quick start: Regular consent flow (pre-production)

With regular consent, individuals are redirected from your platform to Norsk Gjeldsinformasjon.
They identify with ID-porten and confirm the consent before being redirected back to you.
The service uses a redirect-based flow adhering to OAuth 2.0 and OpenID Connect standards.

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

Once you have a client with registered callback URIs, you can run through the consent flow in
preprod without provisioning a test user yourself: at the ID-porten login screen, choose
**TestID** and enter one of the synthetic NINs `14842249091` or `29868099311`. No password
required. These two NINs have mocked debt data, so the debt API will return a populated response
for them.

For more on TestID, see
[Digdir's ID-porten test users documentation](https://docs.digdir.no/docs/idporten/idporten/idporten_testbrukere.html).

If you specifically need to exercise the BankID UI instead, see
[How do I test the consent flow with BankID](../howto/test-with-bankid.md).

### Authorize

You can test authorization by following [How-to: Authorize](../howto/authorize.md). This is typically handled by a library in production code.

You should now be able to use your credentials to fetch access tokens.

To get an access token for a specific individual, redirect them to the authorization endpoint:

```
https://access-preprod.norskgjeld.no/oauth2/auth
  ?client_id=YOUR_CLIENT_ID
  &response_type=code
  &scope=debt.unsecured.presentation
  &state=thisShouldBeARandomValue
  &redirect_uri=https://your-callback-url.no/v1/callback
```

After the individual consents, they are redirected to your `redirect_uri` with an authorization code:

```
https://your-callback-url.no/v1/callback?code=AUTH_CODE&state=thisShouldBeARandomValue
```

Exchange the code for an access token:

```bash
curl -X POST https://access-preprod.norskgjeld.no/oauth2/token \
  -u "YOUR_CLIENT_ID:YOUR_CLIENT_SECRET" \
  -d "grant_type=authorization_code" \
  -d "code=AUTH_CODE" \
  -d "redirect_uri=https://your-callback-url.no/v1/callback"
```


### Fetch debt

To fetch debt, you will need to call `/v1/debt` endpoint and provide an access token from the previous step.

See our [OpenAPI definition](../reference/openapi.md) for details.
