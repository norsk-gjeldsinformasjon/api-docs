# Select an integration

This HowTo helps you to find the correct type of integration.

There are a few different options for integrating with Norsk Gjeldsinformasjon. Skip to the heading that suits your need for pointers.

## We are a Financial Institution (credit bureaus or lender)

Which companies and institutions that can access information about unsecured debt is regulated in gjeldsinformasjonsloven.

If your organization is allowed to access this information you can integrate with the Search API.

Documentation for this service is not yet migrated, please refer to [API for query](https://norskgjeld.atlassian.net/wiki/spaces/GJEL/pages/851985)


## We provide a service to individuals where we need to access debt information

If you provide a service to individuals where you need to access information about their debt, you can ask users to issue a consent. When issuing a consent, the user will need to be properly identified.

There are two ways to ask users to issue a consent: _regular consent_ and _integrated consent_

### Regular consent

Norsk Gjeldsinformasjon handles the consent process. The user is redirected from your platform to Norsk Gjeldsinformasjon. The user will have to identify in ID-porten and confirm the consent before being redirected back to your platform.

See: [How to get started with regular consent](get_started_regular.md)


### Integrated consent

You handle the consent process yourself. You are responsible for sufficently identifying the user and managing the consents. The benefit of this option is that the user does not leave your platform.

See: [How to get started with integrated consent](get_started_integrated.md)
