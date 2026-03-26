[choose_integration.md](https://github.com/user-attachments/files/26276250/choose_integration.md)
# Select an integration

There are a few different options for integrating with Norsk Gjeldsinformasjon. Skip to the heading that suits your need.

## We are a Financial Institution (credit bureaus or lender)

Which companies and institutions that can access information about unsecured debt is regulated in gjeldsinformasjonsloven. If your organization is allowed to access this information you can integrate with the Search API.

!!! note "Note"
    Documentation for this service is being migrated. See the new [Look up debt without consent](lookup-noconsent.md) section for updated documentation.

## We provide a service to individuals where we need to access debt information

If you provide a service to individuals where you need to access information about their debt, you can ask users to issue a consent. There are two ways to ask users to issue a consent:

### Regular consent

Norsk Gjeldsinformasjon handles the consent process. The user is redirected from your platform to Norsk Gjeldsinformasjon. The user will have to identify in ID-porten and confirm the consent before being redirected back to your platform.

### Integrated consent

You handle the consent process yourself. You are responsible for sufficiently identifying the user and managing the consents. The benefit of this option is that the user does not leave your platform.
