---
tags:
  - consent
---

# Consents with an extended duration

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