# How do I authorize

## Prerequisites

You have been gives access to the consent APIs and have been given a client id. See [FAQ: How do I start using a service?](../explanation/index.md#how-do-i-start)


## Library support

Developers will typically use one of the many available [OAuth 2.0 library](https://oauth.net/code/) and not hand-roll their own code for authorizing. But the steps described in this HowTo can be useful during debugging or verifying access.


## Fetching an access token

When calling our consent API you will need to provide an access token:

You get an access-token by requesting it from *access.norskgjeld.no*

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
# Success response:
https://api-eksempelbank.no/v1/callback?code=wi-w8zIdwwBHggkHhSjR24wH8pN6MDqxdObTBDuzaZo.sciTzz9qgwMlGBZ6X0jYIDyib8MupoIp5gbIJBxnTCs&scope=debt.unsecured.presentation&state=thisShouldBeARandomValue

# Error response:
https://api-eksempelbank.no/v1/callback?error=consent_denied&error_description=&state=thisShouldBeARandomValue
```

The error code can be "consent_denied", "server_error", "invalid_scopes" or "login_cancelled"

You can also see the example [create-agreementbased.py](../reference/assets/create-agreementbased.py) for how this can be achieved in Python.
