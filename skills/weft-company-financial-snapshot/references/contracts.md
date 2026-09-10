# Financial snapshot contract evidence

Inspected 2026-09-10 from a Weft full contract whose source capture was
2026-08-26. One AAPL paid response was observed on 2026-09-10. Re-search
and read the live contract before use; prices and availability can change.

[Immutable Weft contract](https://weft.network/contracts/curated-marketplace/350b7f79aa40e214a5368155048ec5d1146beef15abfc2970e46c02cc6187626/bazaar-x402-atlas-162.json).
Read the current search contract URL when supplied. If legacy search omits it,
use this known link and current first-party evidence; never invent a contracts
API path. A 401 requires the existing Weft credential through a secure HTTP
executor bound only to the exact Weft origin with redirects disabled. Never
print that credential, put it in a URL or forward it to the merchant. If the
executor cannot make this authenticated read, report the limitation.

## Candidate request

- Operation: `bazaar-x402-atlas-162`; access: `bazaar-x402-atlas-162-x402`.
- `GET https://sec.use.x402atlas.com/financials/:ticker`.
- Substitute the URL-encoded ticker in `:ticker`, e.g. `/financials/AAPL`.
- Ticker is case-insensitive and matches `^[A-Za-z0-9][A-Za-z0-9.-]{0,9}$`.
- Source input requires HTTP type, GET method and `pathParams.ticker`.
  Query properties are empty. Do not add period or metric filters.
- Observed price: USD 0.01 per request; runtime challenge is authoritative.
- Synchronous, terminal-response coverage, Base x402 supported.
- Normalized input/output schemas are null. Callability is `incomplete` with
  `response schema (operation probed, not paid)`. This is calibration evidence,
  not a guarantee of coverage. The later live AAPL call returned HTTP 200.

## Nested output evidence

The source schema lives at
`operation.input.source_contract.properties.output.properties.example`.
The catalog example is wrapped in `output.example.example`; neither location
proves that a merchant response uses an `example` wrapper. Inspect the decoded
body and establish its root before applying the candidate body paths below.
Stop if its structure cannot be established from the response and contract.

| Candidate body pointer | Source type and meaning |
|---|---|
| `/ticker` | Required string |
| `/cik`, `/company_name`, `/note` | Optional integer, string, string |
| `/metrics` | Required array; can be empty |
| `/metrics/i/key`, `/metrics/i/label` | Required strings; no complete key enum |
| `/metrics/i/annual`, `/metrics/i/quarterly` | Optional objects, independently absent |
| `/metrics/i/p/value`, `/metrics/i/p/unit` | Required number and string if p exists |
| `/metrics/i/p/period/end` | Required date if p exists |
| `/metrics/i/p/period/start` | Optional date |
| `/metrics/i/p/form`, `/metrics/i/p/filed`, `/metrics/i/p/accession_number` | Required string, date, string if p exists |

Here p means annual or quarterly, not a literal path component. The example
contains only `key: revenues`; it does not establish keys for other metrics.
There are no arrays of historical periods, filing document URLs, market quotes
or share prices in this schema. Do not manufacture them. Historical example
values are illustrations, not current company facts.

## Alternatives and verification

Search for another SEC financials provider if this contract cannot satisfy
scope. A Massive financials result, if found, needs its own full current schema;
these Atlas pointers do not transfer. Independently read the exact SEC filing
or company facts matched by issuer, accession, concept, unit and period. Never
claim that two provider labels alone establish the same accounting concept.

## Observed transport and live body

The tested CLI returned `{schema_version: "2", ok: true, meta, data}`.
`data.status` is merchant HTTP status; `ok: true` alone does not mean data
succeeded. Decode JSON string `data.body`, or base64-decode `body_base64`
when present. `meta.saved_path` is a local body file to read, not JSON itself;
`meta.receipt_path` points to its receipt. For a direct MCP result, inspect
the actual envelope rather than assuming a CLI `data` wrapper.

CLI receipt fields observed: `data.paidUsd`, `heldUsd`, `paymentStatus`,
`txHash`, `artifactId`, `protocol`. Normalize to paid/held/status only after
reading the actual fields. MCP can use snake_case. Missing cost is unknown.
Keep payment state independent from merchant HTTP/data state.

The decoded Atlas body root was `{ticker, cik, company_name, metrics}` with
no `example` wrapper. Returned metric keys were revenues, net_income, assets,
liabilities, stockholders_equity, operating_cash_flow and diluted_eps. Cash
and debt were absent: assets are not cash and liabilities are not debt.
These observed keys are not a complete enum for every issuer.
