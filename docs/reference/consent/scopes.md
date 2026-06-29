---
tags:
  - consent
---

# Scopes

Scopes are space-separated lists of identifiers used to specify what access privileges are being
requested. See [Consent purpose](../index.md#consent-purpose) and
[Consent duration](../index.md#consent-duration) in the main reference for an overview.

Due to legal reasons a consent is required to have a specific purpose; you can therefore only ask
the user to consent to one scope at a time.

The scopes also contain the purpose of the consent, which can either be presentation of debt
information (gjeldsinformasjonen) - or credit processing.

This is done by supplying the corresponding scope when you initiate the flow, and the request to
/auth must therefore contain one and only one of the following scopes:

<table data-table-width="760" data-layout="default" data-local-id="665a77b0-ea6f-4be9-8a55-ab597da672c2" class="confluenceTable"><colgroup><col style="width: 230.0px;"><col style="width: 264.0px;"><col style="width: 142.0px;"><col style="width: 120.0px;"></colgroup><tbody><tr><td class="confluenceTd"><p><strong>Scope</strong></p></td><td class="confluenceTd"><p><strong>Intended use</strong></p></td><td class="confluenceTd"><p><strong>Default duration</strong></p></td><td class="confluenceTd"><p><strong>Max duration</strong></p></td></tr><tr><td class="confluenceTd"><p>debt.unsecured.presentation</p></td><td class="confluenceTd"><p>Solely for displaying the debt info</p></td><td class="confluenceTd"><p>10 min</p></td><td class="confluenceTd"><p>365 days</p></td></tr><tr><td class="confluenceTd"><p>debt.unsecured.processing</p></td><td class="confluenceTd"><p>Credit processing, for example refinancing of existing debt</p></td><td class="confluenceTd"><p>10 min</p></td><td class="confluenceTd"><p>28 days</p></td></tr></tbody></table>

A default consent allows you to collect the debt info one time within 10 minutes.

See [Extended duration](extended-duration.md) for consents with an extended duration.

## Optional: openid scope

It is also possible to ask for the openid scope. This is used to contain the ssn and consentID of
the flow.

If you request the openid scope, it must be the last scope given in the request.  
Correct: "debt.unsecured.presentation openid".  
Incorrect: "openid debt.unsecured.presentation"

<table data-table-width="760" data-layout="default" data-local-id="48c8c426-5c7b-462a-9158-88489d33270d" class="confluenceTable"><colgroup><col style="width: 94.0px;"><col style="width: 421.0px;"><col style="width: 245.0px;"></colgroup><tbody><tr><td class="confluenceTd"><p><strong>Scope</strong></p></td><td class="confluenceTd"><p><strong>Intended use</strong></p></td><td class="confluenceTd"><p><strong>Description</strong></p></td></tr><tr><td class="confluenceTd"><p>openid</p></td><td class="confluenceTd"><p>Receive consentID and ssn securely for verifying correct person has consented to share debt information.</p><p>Can be used to go directly to the Client Credentials Flow from the Authorization Code Flow by extracting the consentID from the ID Token.</p></td><td class="confluenceTd"><p>ID Token as a JWT-token with:<br>"pid": &lt;ssn&gt;<br>and<br>"consent_id": &lt;consentID&gt;</p><p>Note: The "sub" field should not be stored</p></td></tr></tbody></table>