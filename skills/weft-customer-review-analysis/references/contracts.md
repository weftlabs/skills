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

## Reviews

Endpoint: `https://api.strale.io/x402/v2/product-reviews-extract`.
Observed quote: USD 0.27. Legacy discovery operation `bazaar-strale-42`, access
`bazaar-strale-42-x402`; do not pretend these are new v2 operation identifiers.
[Legacy contract](https://weft.network/contracts/curated-marketplace/e653c796aa4bc4ac7be863d1b8a091846efbbbeaea44926345ce539637d7818d/bazaar-strale-42.json).

The url description explicitly rejects Trustpilot, Glassdoor and LinkedIn.
One source URL feeds one extraction response. No documented date/count inputs.

| Pointer | Documented type / interpretation |
|---|---|
| `/common_pros`, `/common_cons` | arrays; items untyped, provider-generated summaries |
| `/review_count`, `/average_rating` | numbers; site aggregates, not delivered sample size |
| `/rating_distribution` | object; buckets not fully typed |

The full OpenAPI example additionally shows `url`, `source`, `product_name`,
`recent_reviews` (empty array), `sentiment_summary` and null aggregate values.
Thus schema and example disagree about nullability; handle null as unavailable.
There is no guaranteed review-text field, per-review URL, date, or rating-scale
contract. Validate actual records before deriving themes, labels or counts.
Absent raw reviews means provider-summary-only output and no local accuracy claim.
The edge is URL → extraction → validated local evidence ledger → brief, with
no second paid service.

## Live shape observed 2026-09-10

One WooCommerce response returned root `product_name`, `source`, `url`,
`average_rating`, `review_count`, `rating_distribution`, `common_pros`,
`common_cons`, `sentiment_summary` and `recent_reviews`.
Each recent review had `title` and relative `date` strings, but `text`, `rating`
and `verified` were null. No per-review ID or URL arrived. This does not establish
what another source will return. Null text cannot ground a body-text theme.
Do not map repeated titles to unique identities without source evidence.

Free original-source recovery followed the supplied page's review permalinks
and read original customer posts. Staff replies were excluded from the sample.
The provider's 10 titles and site count of 4,823 were separate from 15 source
review bodies; never join these counts as one corpus. See [evaluation](evaluation.md).
