# Belgian registration contract

Observed 2026-09-10 through free Weft discovery and its full contract.
Provider: Strale. Operation: `strale-belgian-company-data`.

- `GET https://api.strale.io/x402/v2/belgian-company-data`
- Query: `enterprise_number=<10-digit Belgian number>`.
- Indexed price: $0.054 per request; current quote/challenge controls.
- x402, synchronous terminal JSON, read-only data acquisition.
- Complete contract: https://weft.network/contracts/curated-marketplace/2847179cf73aa1250871f230aa0546ccb7d6262433af7445956d5f5ca5997007/strale-belgian-company-data.json
- Provider OpenAPI: https://api.strale.io/openapi.json

The contract also offers `company_name`, `name`, `query` and `task` aliases.
They can resolve fuzzy names or the first match. This workflow deliberately
uses only the exact identifier. Although no input is marked required by the
provider schema, the workflow requires a jurisdiction and identifier to prevent
unintended account matching.

Expected output fields: `company_name`, `registration_number`, `jurisdiction`,
`business_type`, `status`, `address`, `registration_date`, `establishments_count`,
`vat_number`, plus optional `industry`, `abbreviation` and `commercial_name`.
The normalized output schema is null; the nested description includes a schema
and an example. Nullable fields occur in the example despite string types.
Treat missing/null fields as unknown, not a parsing failure or invented value.
The provider describes KBO/BCE data delivered through CBEAPI.be, and the VAT
number can be derived from the enterprise number. No VIES, credit or ownership
verification is promised.

For CLI execution, discover its installed flags with `weft fetch --help`, then
use the exact GET URL and `--max-cost-usd` at the current quote. Do not invent
JSON-body or attribution options absent from help. Read `data.body` or the
reported artifact and preserve receipt fields separately.
