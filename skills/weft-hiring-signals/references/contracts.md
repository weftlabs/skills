# Hiring evidence contract — inspected 2026-09-10

## Active route: Linkup

[Immutable Weft contract](https://weft.network/contracts/curated-marketplace/2d4255be719952fc2a521404a77e024b0ed7017f55e07e5453c8742e4571f44b/linkup-search.json).
Operation `linkup-search`; access `linkup-search-x402-base`.
POST `https://api.linkup.so/v1/search`, Content-Type application/json.
Synchronous terminal read-only search, observed USD0.01 per request. The
live quote wins; stop if it exceeds the approved tight cap.

Required JSON fields: q string, depth enum fast/standard/deep, outputType
searchResults/sourcedAnswer. Optional maxResults integer and includeDomains
or excludeDomains arrays of domain strings. Use only searchResults here.
Example body: `{"q":"Find individual software engineer job postings in Austin, Texas, United States. Return employer career or job posting pages with role, employer and location evidence.","depth":"standard","outputType":"searchResults","maxResults":10}`.
Do not send Atlas location/country/language parameters to Linkup.

The full Weft contract has complete callability but no normalized output
schema. The [official response reference](https://docs.linkup.so/pages/documentation/endpoints/search/reference)
defines a root results array with name, url and content for text results.
Map `/results/i/url` to source_url and derive role/employer/location only
from `/results/i/content` and name. These are snippets, not typed job facts.
Reject images and non-posting pages. There is no guaranteed posting date,
company field, job ID or geographic filter in this selected response.
Use local UTC retrieval time for searched_at, with that meaning disclosed.

## Search response shapes

Inspect the actual envelope before reading a quote. The live SDK REST search
returned legacy `results[]` with `provider.provider_id` and `display_name`,
and an `endpoints[]` array. Select the endpoint by `endpoint_id` or
`operation.id` equal to `linkup-search`; its URL is `url`, method is
`call.method`, and input schema is `call.input_schema`. Select the exact
`access_methods[]` entry by `access_method_id` or `id` equal to
`linkup-search-x402-base`; its quote is `price.indexed_usd`. The endpoint
also has `price.indexed_usd`. The response-level `query_trace_id` identifies
this search. This legacy result had no contract_url; use the immutable link.
Compact search responses can instead provide `operation`, `access`, `request`
and `contract_url` directly. Do not read compact `access.price` from a legacy
result or substitute a null quote for the actual endpoint quote.

## Transport

Read the current search contract URL or the exact immutable link above when
legacy CLI omits it. Authenticated contract GET uses existing Weft credential
in memory, exact Weft origin only, redirects refused. Never invent a contract
API or expose credentials. No separate Linkup key is needed through Weft.

CLI v2 can return `{ok, meta, data}`. `data.status` is merchant HTTP status;
`ok=true` can accompany HTTP502. Parse JSON string `data.body`, decode
body_base64 when present, or read meta.saved_path. A saved_path is not the
merchant data itself. Preserve actual paidUsd, heldUsd, paymentStatus (or
the current equivalent), plus receipt identifiers. Count paid plus held even
when a merchant claims no charge. CLI attribution flags may be absent; record
current search IDs and state the limitation rather than inventing flags.

## Historical failed route

Atlas `GET https://jobs.use.x402atlas.com/search` was tested once for software
engineer in Austin. HTTP502 upstream_error returned no jobs array. Receipt
held USD0.05 pending despite no-charge merchant wording. No retry occurred.
This was not a successful hiring discovery; do not infer zero jobs from it.
Its `/jobs` and apply_options mappings do not apply to Linkup.

For this POST route, confirm the executor can send a JSON body before payment.
The tested CLI help has no body flag; do not invent one or send an empty POST.
Use Weft MCP fetch with body and headers or the supported Weft SDK fetch
interface after reading its current docs. If neither is available, stop with
the specific executor gap; do not install a separate provider integration.

The tested SDK used `WeftClient.fetch` with `url`, `method: "POST"`,
`body` containing serialized JSON, `headers`, `maxCostUsd: "0.01"`,
`searchId`, `operationId` and `accessMethodId`; the second options argument
carried a saved `idempotencyKey`. Read current SDK declarations first; SDK
field names are camelCase while raw REST attribution is snake_case. Decode
its `bodyBase64` when present. The live request returned HTTP200 with ten
root results; only three were individual job pages suitable for the CSV.
That observation does not guarantee current vacancies or complete coverage.
