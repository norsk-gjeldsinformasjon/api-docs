# General

<!--
Explanation - Understanding Oriented

Provide in-depth information to help users understand concepts, mechanisms, or principles. Offer detailed context and background for intermediate to advanced users.
-->

[comment]: # (FAQ should be moved to its own page if this page/section gets crowded)
## FAQ

### How do I start using a service?

Reach out to [Norsk Gjeldsinformasjon](https://www.norskgjeld.no/kontakt-oss/) for more information about using one of our services.

### What is unsecuredt debt?

Unsecured debt include credit card debt, personal loans, and other forms of non-secured borrowing.


### How often is the debt information updated?

The information you receive are always updated to the best of our effort. On every query we contact the financial institutions where the user have debt to fetch the latest data.

If a financial institution fail to answer within the allotted time, we will fall back to cached data. Our cached data are fetched every morning and updated by the financial institutions throughout the day as soon as debt for an individual is changed. This is reported in the debt information response.

## Authorization

### Does the token endpoint return id tokens?

Token endpoint does not deliver id tokens. To verify the identity of the user you can check the identity-number which is delivered in the debt response json.

### Does the token endpoint return refresh tokens?

No, the token endpoint does not deliver refresh tokens. To collect debt information with a consent for an extended duration you will have to obtain an access token from the token endpoint using the client [credentials flow](../reference/consent_flows.md).
