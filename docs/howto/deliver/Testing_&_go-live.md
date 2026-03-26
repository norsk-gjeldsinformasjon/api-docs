[deliver-testing.md](https://github.com/user-attachments/files/26279643/deliver-testing.md)
# Testing & go-live

All three API operations must be successfully tested in pre-production before production access is granted.

!!! note "To get test access"
    Contact [post@norskgjeld.no](mailto:post@norskgjeld.no) with: organisation details, test endpoint URL, test IP addresses, and test enterprise certificate.

!!! warning "Synthetic SSNs only"
    Real or production SSNs must **never** be used in non-production environments.

## Mandatory tests — getalldata

| Test | How to test | Pass criteria |
|---|---|---|
| Full dataset retrieval | NoGi triggers a `getalldata` call against your test endpoint | HTTP 200 with all test customers returned correctly |
| Data validation | Internally validate data before the call | NoGi accepts without validation errors |
| Paging (if applicable) | Configure test data > 100 MB | All pages returned; no customer split across pages |

## Mandatory tests — pushUpdates

| Test | Pass criteria |
|---|---|
| New loan account | NoGi receives push; subsequent getDataForSSN returns the new loan |
| Credit limit change | Updated limit reflected in NoGi |
| Repaid loan (all amounts = 0) | Loan no longer shown as active |
| Balance change — no push sent | Confirms you are not over-pushing |

## Mandatory tests — getDataForSSN

| Test | Pass criteria |
|---|---|
| Customer with repayment loan | Full loan details returned correctly |
| Customer with multiple loan types | All loan objects returned |
| Customer with no debt | HTTP 200 with empty `loans` array (not an error) |
| Response time under load | <500 ms for 99% of requests; ≥50 req/sec capacity |

## Go-live process

1. **Complete all mandatory tests** — document your results
2. **Request production access** — send confirmation + production details to [post@norskgjeld.no](mailto:post@norskgjeld.no)
3. **NoGi configures production** — endpoints, IPs, and certificate registered
4. **Monitor first production cycle** — verify 05:00 UTC getalldata completes and push updates flow correctly
