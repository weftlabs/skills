# Strale contract evidence

The complete [official OpenAPI](https://api.strale.io/openapi.json) and unpaid
v2 payment challenge were inspected 2026-09-10. Weft search exposed the legacy
route, not v2, even when queried with the exact v2 URL. The v2 route below comes
from official provider documentation and its own challenge, not a guessed path.
Use free discovery first; report this catalog gap. Old agent-card prose says
POST, while OpenAPI and live challenge specify GET; follow the latter.

GET the endpoint below with a URL-encoded required `url` string query. No body
or user-supplied credential header. Read-only extraction, synchronous JSON; no
async job or polling contract. Weft manages x402 Base USDC payment. Current quote
controls spend. No automatic retries or paid pagination.

The output has typed root properties but does not define complete nested item
schemas. Example fields are hints, not guarantees; inspect actual body before
mapping. Stop unsupported interpretations, not honest partial delivery. Do not
manufacture missing fields from a catalog example.

Legacy immutable Weft contracts can require authentication: use the existing
Weft connection, credentials only in memory, exact Weft origin, redirects refused.
Never expose credentials or forward them to Strale/source pages. CLI output can
wrap data under `data.body` (JSON string), `body_base64`, or a body file at
`meta.saved_path`. Read actual status and receipt separately. CLI `ok` alone is
not merchant success. Normalize actual paid/held fields; do not invent flags.

## Pricing

Endpoint: `https://api.strale.io/x402/v2/pricing-page-extract`.
Observed quote: USD 0.324 per source URL; two pages cost USD 0.648 before any
known compulsory fee. Legacy operation `bazaar-strale-41`, access
`bazaar-strale-41-x402`; record actual discovery, not invented v2 identifiers.
[Legacy contract](https://weft.network/contracts/curated-marketplace/1dc5c3a3d84bac7ce82e380043b5f9882dc2f128f720515696fcd7da6a527426/bazaar-strale-41.json).

| Pointer | Documented type / interpretation |
|---|---|
| `/plans` | array; nested plan schema unspecified |
| `/pricing_model` | string |
| `/enterprise_cta`, `/free_trial_available` | booleans; absence is unknown |

Example-only fields: root `url`, `annual_discount`, `free_tier_available`,
`money_back_guarantee`; each plan `name`, `price` (string), `currency`, `features`,
`highlighted`, `price_amount`, `billing_period`. Example permits nulls for custom
pricing and compound rates. Do not force price_amount from a compound price.
The documented example uses a percentage plus fixed transaction fee; that is
not a monthly subscription. No price-effective date or seat-minimum schema is
established. Preserve raw text and verify conditions from source.
Two URLs → two separately attributed result sets → local normalization →
comparison. No provider output is submitted to another paid service.

## Live shape and source checks observed 2026-09-10

Both Slack and Notion responses returned `plans` with `name`, `price`,
`price_amount`, `currency`, `billing_period`, `features`, `highlighted`.
Custom `price_amount` was null. Root free-tier/trial and annual-discount fields
also appeared. These are observed fields, not a complete guarantee.

Slack combined two USD prices into one string; the independently fetched page
showed EUR. Its features array appeared to include comparison-grid row labels
without respecting inclusion marks, so those feature claims stayed unverified.
Notion's $10/$20 cards were labeled monthly by the extractor; source toggle and
annual totals established per-month equivalents billed annually. Keep the
original discrepancy and source basis, not just a corrected number. Hidden
Enterprise amounts in source application data were not advertised prices:
the visible Contact-us offer remained custom. See [evaluation](evaluation.md).
