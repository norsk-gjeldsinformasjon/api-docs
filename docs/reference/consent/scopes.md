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

## Extended duration

It is possible to ask the user for a consent with an extended duration. This is done by appending
the requested duration of the consent **in days** after the scope.

Starting the flow with the scope "debt.unsecured.presentation.365" would prompt the user to consent
to sharing their debt information for 365 days, which is the maximum duration for this type of
consent. Note that this is a way to specify duration. The scope name displayed in redirect URLs will
still be "debt.unsecured.presentation".

The two scopes have different max numbers of days that you can request, and if provided a number
higher than this we will default to the boundary value.

It is possible to choose a shorter duration than the maximum duration if that is more suitable for
you, for example debt.unsecured.presentation.50 would prompt the user to consent to sharing their
debt information for 50 days.

The debt info can be collected any number of times using consents with an extended duration, but
keep in mind that users can log into [www.norskgjeld.no](http://www.norskgjeld.no) and see every
single time their consent has been used to collect debt info.

## Optional: openid scope

It is also possible to ask for the openid scope. This is used to contain the ssn and consentID of
the flow.

If you request the openid scope, it must be the last scope given in the request.  
Correct: "debt.unsecured.presentation openid".  
Incorrect: "openid debt.unsecured.presentation"

<table data-table-width="760" data-layout="default" data-local-id="48c8c426-5c7b-462a-9158-88489d33270d" class="confluenceTable"><colgroup><col style="width: 94.0px;"><col style="width: 421.0px;"><col style="width: 245.0px;"></colgroup><tbody><tr><td class="confluenceTd"><p><strong>Scope</strong></p></td><td class="confluenceTd"><p><strong>Intended use</strong></p></td><td class="confluenceTd"><p><strong>Description</strong></p></td></tr><tr><td class="confluenceTd"><p>openid</p></td><td class="confluenceTd"><p>Receive consentID and ssn securely for verifying correct person has consented to share debt information.</p><p>Can be used to go directly to the Client Credentials Flow from the Authorization Code Flow by extracting the consentID from the ID Token.</p></td><td class="confluenceTd"><p>ID Token as a JWT-token with:<br>"pid": &lt;ssn&gt;<br>and<br>"consent_id": &lt;consentID&gt;</p><p>Note: The "sub" field should not be stored</p></td></tr></tbody></table>