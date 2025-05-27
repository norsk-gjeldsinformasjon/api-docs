# Norsk Gjeldsinformasjon technical reference

Norsk Gjeldsinformasjon is a debt registry which collects information about individuals unsecured debt from various financial institutions. We provide lenders and individuals with an overview of unsecured debt, which can include credit card debt, personal loans, and other forms of non-secured borrowing.

Norsk Gjeldsinformasjon aims to improve transparency in the financial sector, helping lenders assess the creditworthiness of borrowers more accurately. By providing comprehensive debt information, Norsk Gjeldsinformasjon helps prevent individuals from taking on unsustainable levels of debt and supports responsible lending practices. It is part of a broader effort in Norway to promote financial stability and consumer protection.

Migration of the public documentation is currently a work in progress,
the documentation that is not yet migrated can be found
[on confluence](https://norskgjeld.atlassian.net/wiki/spaces/GJEL/overview)


## Offerings

### Information for individuals

Individuals can see an overview of their own unsecured debt and any consents that has the individual has given, and when consents have been used. Users can also choose to withdraw any consents given.

This information can be viewed by individuals by logging in to ["Min Gjeld"](https://www.norskgjeld.no/)


### Accessing debt with consent from individuals

Individuals can consent to allowing organizations to access information about their unsecured debt.

An overview of consents and how they are used is available for the user by logging in to ["Min Gjeld"](https://www.norskgjeld.no/)

Organizations that want to display an individuals debt or assess an individuals creditworthiness can establish an integration to Norsk Gjeldsinformasjon.


### Credit bureaus and lenders

These organizations can establish an integration with Norsk Gjeldsinformasjon in order to assess creditworthiness when considering an application for credit. This is only available for financial institutions. Regular companies that have a need to evaluate creditworthiness (e.g. telecom companies) will not have access to this service.

Which companies and institutions that can access this information is regulated in gjeldsinformasjonsloven.


### Receiving collected debt info about own customers

Finacial instituions can receive a data package containing all debt for their customers once every fiscal quarter.
- 
* Details regarding restrictions to this service - [See domain documentation](https://norskgjeld.atlassian.net/wiki/spaces/GJEL/pages/492273665/API+Data+Packaging+-+collecting+debt+information+about+your+customers)
* Technical documentation regarding setting up this service - [See our technical documentation](https://norsk-gjeldsinformasjon.github.io/api-docs/howto/recieve_quarterly_debt-reports/)
