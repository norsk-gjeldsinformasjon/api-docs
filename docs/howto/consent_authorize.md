# How do I authorize

## Prerequisites

You have been gives access to the consent APIs and have been given a client id. See [FAQ: How do I start using a service?](../explanation/index.md#how-do-i-start)


## Library support

Developers will typically use one of the many available [OAuth 2.0 library](https://oauth.net/code/) and not hand-roll their own code for authorizing. But the steps described in this HowTo can be useful during debugging or verifying access.


## Fetching an access token

Before you call Norsk Gjeldsinformasjon API, you will need to fetch an access token. You must provide the access token when calling our APIs.

There are two ways to retrieve access tokens: *Client credentials* and *Authorization code*. An authorization code gives you access to operate on a single consent, client credentials allow you to operate on any consent you are allowed to access.

For example, if you look up debt with a:

- Authorization code: You can access debt for the one consent that provided you with the particular authorization code
- Client credentials: You can access debt for any active consents you are allowed to use

Access-tokens are requested by POSTing a reguest to the /token endpoint:

- https://access-preprod.norskgjeld.no/oauth2/token
- https://access.norskgjeld.no/oauth2/token


### Client credentials

To request an access token using client credentials, you make a HTTP POST to the /token endpoint and provide the following parameters:

| Parameter  | Description                                                                                                                |
|------------|----------------------------------------------------------------------------------------------------------------------------|
| grant_type | Must be set to “client_credentials”                                                                                        |
| audience   | [See reference for the service you want to call](../reference/index.md#reference-consent-authorization-audience-and-scope) |
| scope      | [See reference for the service you want to call](../reference/index.md#reference-consent-authorization-audience-and-scope) |

Example response:

```json
{
    "access_token":"C2EzneyuE2lEK8VBYZS7TxBUMF16Ns6gTuU5DybZbY.6pcF_rv3muje47_GDucYJrQZvDioc8O7oCmvKMZKHEg",
    "expires_in":3599,
    "scope":"debt.unsecured.presentation debt.unsecured.processing",
    "token_type":"bearer"
}
```

`access_token` is your access token that should be provided when calling Norsk Gjeldsinformasjon APIs

You can also see the example [create-agreementbased.py](../reference/assets/create-agreementbased.py) for how this can be implemented in Python.

See also: [Client credentials](https://oauth.net/2/grant-types/client-credentials/)


### Authorization code

This is only available if you use Authorization code flow with [Regular consent](../reference/index.md#regular-consent-flows).

You get an access-token by redirecting the individual to `access.norskgjeld.no`:

```
GET: https://access-preprod.norskgjeld.no/oauth2/auth?client_id=your_client_id_here&response_type=code&scope=debt.unsecured.presentation&state=thisShouldBeARandomValue&redirect_uri=https://api-eksempelbank.no/v1/callback
```

You will need to provide your own values for these parameters:

| Param        | Description                                                       |
|--------------|-------------------------------------------------------------------|
| client_id    | Your assigned client ID                                           |
| scope        | Select scope depending on what part of our API you intend to call |
| state        | unique string that you will receive on callback                   |
| redirect_uri | URI where we will redirect the client when finished               |

You can expect a response that indicates success or error:

```
# Example success response:
https://api-eksempelbank.no/v1/callback?code=wi-w8zIdwwBHggkHhSjR24wH8pN6MDqxdObTBDuzaZo.sciTzz9qgwMlGBZ6X0jYIDyib8MupoIp5gbIJBxnTCs&scope=debt.unsecured.presentation&state=thisShouldBeARandomValue

# Example error response:
# The error code can be "consent_denied", "server_error", "invalid_scopes" or "login_cancelled"
https://api-eksempelbank.no/v1/callback?error=consent_denied&error_description=&state=thisShouldBeARandomValue
```

If the individual was redirected back with a successful response it means that the user have consented. The `code` parameter contains _authorization code_ which then can be used to request an _access token_.

To request an access token using client credentials, you make a HTTP POST to the /token endpoint and provide the following parameters:

| Parameter    | Description                           |
|--------------|---------------------------------------|
| grant_type   | Must be set to “authorization_code”   |
| client_id    | Your assigned client id               |
| redirect_uri | Redirect URI that was used            |
| code         | Authorization code you received above |

Example response:

```json
{
    "access_token":"YcvXKoiuOwnbJkxso2Oe6bhp2cXcoHdZ1pdgE_QpDww.cAu8_J51evXtBQxfTMzkRA414_mOla1zryE1e_-r-1k",
    "expires_in":3599,
    "scope":"debt.unsecured.presentation",
    "token_type":"bearer"
}
```

`access_token` is your access token that should be provided when calling Norsk Gjeldsinformasjon APIs

See also: [Authorization code](https://oauth.net/2/grant-types/authorization-code/)
