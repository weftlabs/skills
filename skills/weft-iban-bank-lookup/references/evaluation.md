# Evaluation — 2026-09-10

Two fresh Pi CLI sessions exercised real Weft calls using public example
IBANs. These are shared-account smoke tests, not a paired benchmark. The
candidate and core skill files were explicitly loaded with automatic workspace
context and skill loading disabled. This does not test automatic triggering.

| Case | Observed outcome | Paid USD | Held USD |
|---|---|---:|---:|
| GB82 WEST example | Valid checksum, GB and WEST returned; bank name/BIC null; partial result disclosed | 0 | 0.0216 |
| GB83 invalid variant | Checksum failed; input preserved; no purchase | 0 | 0 |
| DE89 3704 example | Valid checksum; Commerzbank, COBADEFFXXX, Germany returned | 0 | 0.0216 |
| DE00 invalid variant | Checksum failed; no repair or purchase | 0 | 0 |

Both Weft requests returned HTTP 200 with pending receipts. These amounts are
capture-time paid/held accounting, not a claim of final settlement. No transfer,
retry, alternate provider billing, or account change occurred.

The first run exposed incomplete bank-table coverage. The revised instructions
make checksum rejection mandatory before spending, distinguish CLI envelopes
from provider data, tolerate extra metadata, and label missing bank name/BIC
as a partial lookup. Review also restricted this recipe to the documented
Strale route to avoid misattributing other providers' fields.

An independent evaluator checked the initial trace: positive partial, invalid
boundary passed, no observed safety failure. Local arithmetic independently
checks checksum behavior. Provider agreement alone does not verify bank
identity, account existence, ownership, or worldwide coverage. Failed-payment
recovery and other hosts were not exercised. Private raw traces and receipts
are excluded from this repository.
