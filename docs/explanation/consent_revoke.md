# Notify Norsk Gjeldsinformasjon when your customers/users revokes consent

When one of your customers or users revokes his/her consent on your platform, Norsk Gjeldsinformasjon must be called in order for the consent to be revoked.

When a consent is revoked, you must call the "Revoke a consent by ID" endpoint (/v1/debt/{consent-id}) endpoint to actually revoke the consent.

Note that users can also revoke consents when logged inn on [norskgjeld.no](http://www.norskgjeld.no/). If you need to be notified when one of your customers/users revokes a consent, please see [Learn when a consent is revoked](../explanation/learn_revoked_consents.md)