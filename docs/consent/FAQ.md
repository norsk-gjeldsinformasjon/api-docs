# FAQ

## How often is the debt information updated?

We request updated information from the banks on every request, so the debt information that you
receive should be up to date. If one of the banks fails to respond in the allotted time we will fall
back to cached data which is updated once a day. This is reported in the debt information json.

## Does the token endpoint return id tokens?

No, the token endpoint does not deliver id tokens. To verify the identity of the user you have to
check the SSN which is delivered in the debt response json.

## Does the token endpoint return refresh tokens?

No, the token endpoint does not deliver refresh tokens. To collect debt information when a user has
consented to sharing their debt information for an extended duration you have to obtain an access
token from the token endpoint using the client credentials flow.

## How do I start using the service?

Contact Norsk Gjeldsinformasjon AS to enter into an agreement and receive your client credentials.

## How should I inform Norsk Gjeldsinformasjon about an end user revoking their consent

When an end user has revoked their consent in your service, use the ["Revoke a consent by ID" (/v1/debt/{consent-id})](../Open API/#debt-api#revoke-a-consent-by-id) endpoint to inform us that the consent has been revoked
