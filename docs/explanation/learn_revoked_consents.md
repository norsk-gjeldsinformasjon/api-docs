# Learn when a consent is revoked or inactive

There are two ways you can find out if a consent is inactive. Which one you choose depende on your needs.

Consents can become inactive

## I need to check the current state of a consent

If you have the consentId of the consent that you want to check, you can call us on `/v1/debt/{consentId}/status`. The response will indicate whether the consent is active and the expiration time.

See our [OpenAPI](../reference/openapi.md) documentation for more information.

## I need to be notified about changes as they happen

You can also be notified about changes to consents as they happen by subscribing to Consent Feed API. See the [OpenAPI](../reference/openapi.md) reference for more information.
