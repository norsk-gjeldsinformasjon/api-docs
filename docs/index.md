# Norsk Gjeldsinformasjon technical reference

Norsk Gjeldsinformasjon AS was established by financial institutions in Norway to provide the
industry with its own supplier of debt information. The company is licensed by the Ministry of
Children and Families and is supervised by the Financial Supervisory Authority of Norway (FSA). All
financial institutions that offer unsecured consumer debt in Norway are required, under the
[Norwegian Debt Information Act](https://lovdata.no/dokument/NL/lov/2017-06-16-47), to make their
debt information available to us.

We have established a national infrastructure based on modern technology for the collection and
distribution of debt information. Debt information is made available to financial institutions and
other entities authorized to obtain such information. We offer a secure, stable, and user-friendly
solution.

Migration of the public documentation is currently a work in progress, the
documentation that has not yet been migrated can be
found [on confluence](https://norskgjeld.atlassian.net/wiki/spaces/GJEL/overview).

## Lookup for Credit Assessments

Financial institutions can retrieve unsecured debt information as part of credit application
processing or when modifying existing loan terms. The response includes data from all financial
institutions offering unsecured debt in Norway and provides a consolidated overview of the
applicant’s credit cards, credit lines, installment loans, and charge cards. Creditor identities are
not included in the response.

## Tagging of Own Debt Entries

When processing a credit application and performing a lookup on a national identification number,
you can easily identify which debt entries belong to your financial institution. This provides a
clear overview of how much unsecured debt the applicant has with you and how much they hold with
other financial institutions.

## Consent Solution

The consent solution enables individuals to authenticate and grant consent for a financial
institution to retrieve unsecured debt information. Integrators must ensure that a valid consent
exists at the time of each data request. When debt information is retrieved based on consent, the
financial institution or loan intermediary is presented with the same level of detail as the
individual, including the name of the creditor.

Retrieved debt information may be used for:

* Presentation to the individual
* Credit assessment and credit decisioning

Debt information is retrieved via the APIs and may be fully presented within the financial
institution’s or loan intermediary’s own user interface. The integrator has full control over the
end-user experience.

Customers can easily withdraw their consent via your website or ours. They will also have full
visibility of all consents given and when they were utilized, accessible through our website.

## Statistics/Data Analysis

The statistics service provides aggregated and anonymized insights into unsecured consumer debt in
Norway and is delivered using Microsoft Power BI. Access via Power BI is read-only. Users can view
and filter data but cannot modify the underlying datasets. All data is processed and stored within
Norway.

Customers must ensure that internal prerequisites for accessing the service are addressed. This may
include:

* access to Power BI Pro licenses for relevant users
* IP whitelisting of Microsoft Azure endpoints, depending on internal security policies
* use of Microsoft Authenticator for user authentication

In addition to interactive access, statistical data can also be delivered as files once per day
for import into internal systems.

The service enables analysis and comparison of own portfolios against market-level data and is
intended for reporting, analysis, and risk assessment.

## Quarterly Debt Information on All Your Loan Customers

Each quarter, you can retrieve debt information for all your loan customers to establish or update
credit scoring models. This ensures access to up-to-date data for credit scoring and model
development. Debt information is available for all loan customers, regardless of whether they hold
secured or unsecured debt.

## Customized Letters of Notification

Financial institutions issuing credit cards on behalf of other institutions may use customized
letters of notification, specifying the product or financial institution on whose behalf the inquiry
was made. This service is available to institutions that have integrated directly with our system.

## Integration Options

Financial institutions and other entities authorized to retrieve debt information for credit
processing can choose to integrate directly with us or access debt information through a credit
reporting agency. All necessary information is readily available upon request.