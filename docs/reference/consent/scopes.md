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

| Scope | Intended use | Default duration | Max duration |
|---|---|---|---|
| `debt.unsecured.presentation` | Solely for displaying the debt info | 10 min | 365 days |
| `debt.unsecured.processing` | Credit processing, for example refinancing of existing debt | 10 min | 28 days |

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

The debt info can be collected any number of times using consents with an extended duration.

!!! info "User visibility"
    Users can log into [norskgjeld.no](http://www.norskgjeld.no) and see every time their
    consent has been used to collect debt info.

## Optional: openid scope

It is also possible to ask for the openid scope. This is used to contain the ssn and consentID of
the flow.

If you request the openid scope, it must be the last scope given in the request.  
Correct: "debt.unsecured.presentation openid".  
Incorrect: "openid debt.unsecured.presentation"

| Scope | Intended use | Description |
|---|---|---|---|
| `openid` | Receive consentID and ssn securely for verifying correct person has consented to share debt information. Can be used to go directly to the Client Credentials Flow from the Authorization Code Flow by extracting the consentID from the ID Token. | ID Token as a JWT-token with:<br>`"pid": <ssn>`<br>and<br>`"consent_id": <consentID>`<br><br>Note: The `"sub"` field should not be stored |