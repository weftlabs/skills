# IBAN lookup contract

Inspected 2026-09-10. Provider: Strale. Operation: `strale-iban-to-bank`.
[Immutable Weft contract](https://weft.network/contracts/curated-marketplace/622290688cb70564de5698513096f04c1e1498cfeb5c070d842e2ba500e4c6c5/strale-iban-to-bank.json).

- Method: `GET`.
- URL: `https://api.strale.io/x402/v2/iban-to-bank`.
- Required query: `iban`, string. Encode with a URL query builder.
- No provider body or separate provider credential.
- Access: `strale-iban-to-bank-x402-base`, x402 on Base through Weft.
- Indexed price: $0.0216/request; current quote is authoritative.
- Lifecycle: synchronous terminal JSON; no async submit or poll.

The full contract stores output fields under
`operation.output.description.schema.properties`, even though
`operation.output.schema` is null. Its documented fields are `bic` (string),
`bank_code` (string), `bank_name` (string), `valid_iban` (boolean),
`country_code` (string), and `country_name` (string). No output fields are
declared universally required. The example also contains `branch: null` and
an `iban` echo. Preserve missing/null values; never promote example values to
facts about another input.

One normalized input maps to `request.query.iban`. After decoding the Weft
body, the root provider fields map directly to the result table. There is no
second provider stage. A structurally valid IBAN does not prove account
existence, ownership, beneficiary name, available funds, or transfer eligibility.
