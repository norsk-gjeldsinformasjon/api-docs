---
tags:
  - consent
---

# Consent feed

Updates to consents are available as a feed for customers of the consent service.

This service can be used to "subscribe" to changes instead of checking the status of each individual consent you have registered.

This log will show the last 7 days of events for all consents given to you.

!!! tip "Base URLs"
    - Preprod: `https://api-preprod.norskgjeld.no`
    - Prod: `https://api.norskgjeld.no`

You will need to use an access token with scope="client.access.consent.events" and audience set to "https://api-preprod.norskgjeld.no/feed/v1/consent" (for preprod) or "https://api.norskgjeld.no/feed/v1/consent" (for production) when calling this API.

!!! note "Sequence numbers and timing"
    The sequence numbers you receive will not necessarily correlate to the time a change happened.
    You must check the timestamps inside the events if you need to order them by when they happened.
    Sequence number 3 might contain an event that occurred _after_ sequence number 4.

!!! note "Non-contiguous sequence numbers"
    The sequence numbers are not guaranteed to be contiguous. You might receive a response containing {seq. nr: 7, seq. nr: 8, seq. nr: 13}.
    The sequence numbers 9-12 are not missing.

The API is defined in the [OpenAPI spec](../openapi.md) (under the **Consents Feed API** tag).

## Example implementation

An example implementation of fetching updates to consents in python can be found [here](../assets/fetch-feed.py)