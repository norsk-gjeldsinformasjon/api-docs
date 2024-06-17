# Reference

<!--
Reference - Information Oriented

Offer precise, factual information for quick lookup. Structured and concise, aimed at advanced users needing specific details.
-->

## Consent purpose

When individuals agree to consent to sharing information about their debt, the scope need to be specified. A scope defines what a consent will be used for.

We currently offer these scopes:

| Purpose      | Description                                                                            |
|--------------|----------------------------------------------------------------------------------------|
| Presentation | The debt will be presented to the individual                                           |
| Processing   | The debt will be used for assessing an application from the individual for loan/credit |

## Consent duration

Consents can requested with a duration. A duration specifies *how long* the organization can look up information about debt. If no duration in specified, then a single-use scope will be created. This scope can be used within a few minutes and only used once.

Note that individuals can withdraw consents at any time.

| Purpose (scope) | Duration                        |
|-----------------|---------------------------------|
| Presentation    | 10m (default), 365 days maximum |
| Processing      | 10m (default), 28 days maximum  |

Duration is specified by appending the number to the scope. Example: `debt.unsecured.presentation.100` to specify a presentation scope that should be active for 100 days.

## Regular consent flows

We are offering two OAuth2.0 flows, Authorization Code and Client Credentials.

### Authorization Code Flow

[Authorization Code flow](https://oauth.net/2/grant-types/authorization-code/) is used to authenticate a user and obtain a consent to share their debt information. It is initiated by redirecting the users browser to our /auth endpoint with the required parameters in the URL.

After the customer have accepted/declined the consent, he will be redirected to your system in the callback-uri that you provided.


### <a name="client-credentials-flow"></a> Client Credentials Flow

The [Client Credentials flow](https://oauth.net/2/grant-types/client-credentials/) is used to obtain an access token to identify the client when collecting debt information with a consent which was granted for an extended duration.

The access token received on this request is used in addition to the id of the consent when querying the debt API.
