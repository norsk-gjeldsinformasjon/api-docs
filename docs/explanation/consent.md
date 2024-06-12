# Consents

Individuals can consent to share information about their debt with other organizations. When a user have consented, the organization will be able to look up information about the individuals debt. Consents have a defined purpose which limits what the information should be used for.

## <a name="client-revokes-consent"></a> Notify Norsk Gjeldsinformasjon when your customers/users revokes consent

When one of your customers or users revokes his/her consent on your platform, Norsk Gjeldsinformasjon must be called in order for the consent to be revoked.

When a consent is revoked, you must call the "Revoke a consent by ID" endpoint (/v1/debt/{consent-id}) endpoint to actually revoke the consent.

Note that users can also revoke consents when logged inn on [norskgjeld.no](http://www.norskgjeld.no/). If you need to be notified when one of your customers/users revokes a consent, please see [Learn when a consent is revoked](../explanation/consent.md#consent-events)

## Learn when a consent is revoked or inactive

There are two ways you can find out if a consent is inactive. Which one you choose depends on your needs:

1. You can call our API and check the state of a consent
2. You can poll our API and receive a change feed with events for consents given to you

## I need to check the current state of a consent

If you have the consentId of the consent that you want to check, you can call us on `/v1/debt/{consentId}/status`. The response will indicate whether the consent is active and the expiration time.

See our [OpenAPI](../reference/openapi.md) documentation for more information.

## <a name="consent-events"></a> I need to be notified about changes as they happen

You can also be notified about changes to consents as they happen by subscribing to Consent Feed API. See the [OpenAPI](../reference/openapi.md) reference for more information.


## Inactive or expired consents

Consents can become inactive for different reasons

- Single use consents expire after use
- Consent expiration time have passed
- User revokes consent through your service
- User revokes consent at norskgjeld.no
