# Regular consent flows

We are offering two OAuth2.0 flows, Authorization Code and Client Credentials.

## Authorization Code Flow

[Authorization Code flow](https://oauth.net/2/grant-types/authorization-code/) is used to authenticate a user and obtain a consent to share their debt information. It is initiated by redirecting the users browser to our /auth endpoint with the required parameters in the URL.

After the customer have accepted/declined the consent, he will be redirected to your system in the callback-uri that you provided.


## <a name="client-credentials-flow"></a> Client Credentials Flow

The [Client Credentials flow](https://oauth.net/2/grant-types/client-credentials/) is used to obtain an access token to identify the client when collecting debt information with a consent which was granted for an extended duration.

The access token received on this request is used in addition to the id of the consent when querying the debt API.
