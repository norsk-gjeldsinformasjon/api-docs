# Consuming event feeds

## Polling the feed

Updates to consents are available as a feed for customers of the consent service. This feed can be polled in order to get notifications about events related to your consents. When consents are created or archived (revoked), this feed will be updated with relevant information.

This feed will show the last 7 days of events for all consents given to you.

The response contains a "metadata" portion with parameters for `startSequenceNr` and `endSequenceNr` which can be inspected to see if you should poll further (fetch the next segment), or if all the available data has been fetched.

```json
{
  "startSequenceNr": 1,
  "endSequenceNr": 2,
  "generatedAt": "2024-05-21T12:51:57.383110992Z",
  "result": [
    ....
  ]
}
```

If `endSequenceNr` in a response is an event that you have received (typically the last event in the response), you have consumed all information that is currently available. In summary, events should be polled until you have received the event that is indicated by the `endSequenceNr` property.


## Sequence numbers

Sequence numbers will not necessarily correlate to the time a change happened. You must check the timestamps inside the events if you need to order them by when they happened. (Sequence number 3 might contain an event that occurred after sequence number 4.)

Sequence numbers are not guaranteed to be contiguous. You might receive a response containing {seq. nr: 7, seq. nr: 8, seq. nr: 13}.  (The sequence numbers 9-12 are not missing).

Sequence numbers increase and will never decrease.
