# Get notified about changes to consents as they happen

By calling the Consent Feed API, you can retrieve relevant changes to your consents, for example recently revoked/expired consents.

See explanation [Consuming event feeds](../explanation/consume-events-feed.md) for an explanation on how event feeds works and how they should be consumed.

## Prerequisites

You know [how to authorize](../howto/consent_authorize.md) and retrieve access tokens. You have collected consent from an individual.

## 1. Retrieve access-token

See [how to authorize](../howto/consent_authorize.md) for the details on how to authenticate. To subscribe to consent changes, you can use params: `audience=https://api-preprod.norskgjeld.no/feed/v1/consent` and `scope=client.access.consent.events`. (See [reference](../reference/index.md#reference-consent-authorization-audience-and-scope) for what you should use)

## 2. Poll consent events feed

The feed is read by reading an event stream from `/feed/v1/consent` by specifying parameters:

- `fromSequenceNr`: Where in the event stream to start
- `limit`: Number of events to read

The response will contain changes to consents that you care about and metadata which indicates if you need to poll again (further events are available), and the start point (`fromSequenceNr` for the next call).

The endpoints `/feed/v1/consent/firstSequenceNr` and `/feed/v1/consent/lastSequenceNr` can be polled to get the first/last available sequence numbers.

The response will look like this:

```json
{
  "startSequenceNr": 1,
  "endSequenceNr": 2,
  "generatedAt": "2024-05-21T12:51:57.383110992Z",
  "result": [
    {
      "sequenceNr": 1,
      "eventId": "a499c700-7e36-4bd5-9b6b-19024b4f94f9",
      "consentId": "c8ff2ad5-4140-481d-a7cd-6c7deee7203c",
      "timestamp": "2024-05-20T12:51:52.184886875Z",
      "eventType": "SAMTYKKE_OPPRETTET",
      "samtykkeOpprettetEvent": {
        "clientId": "f8c4da9f-4c93-4904-8de4-b5942776f9c2",
        "consentId": "c8ff2ad5-4140-481d-a7cd-6c7deee7203c",
        "scope": "debt.unsecured.presentation",
        "externalConsentId": "cddda7ed-33be-432e-90d2-0179fbf60cb7"
      },
      "samtykkeArkivertEvent": null
    },
    {
      "sequenceNr": 2,
      "eventId": "47e34ae1-022f-46d4-b3e5-e8ef2dd2761c",
      "consentId": "c8ff2ad5-4140-481d-a7cd-6c7deee7203c",
      "timestamp": "2024-05-21T12:51:53.334608446Z",
      "eventType": "SAMTYKKE_ARKIVERT",
      "samtykkeOpprettetEvent": null,
      "samtykkeArkivertEvent": {
        "clientId": "f8c4da9f-4c93-4904-8de4-b5942776f9c2",
        "consentId": "cddda7ed-33be-432e-90d2-0179fbf60cb7"
      }
    }
  ]
}
```

See the [OpenAPI reference](../reference/openapi.md) for a detailed description.
