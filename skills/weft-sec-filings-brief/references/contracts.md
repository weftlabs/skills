# SEC filings contract

## Active route: Massive

Inspected 2026-09-10. [Immutable Weft contract](https://weft.network/contracts/curated-marketplace/67d1cf97ff60a758f9b79f05362270d10a690b13dcf421eca0b97a9b1a82097b/massive-sec-filing-index.json)
and [official output documentation](https://massive.com/docs/rest/stocks/filings/index).
The full contract provides more inputs than the compact search summary.

Read the current search `contract_url` when present. If legacy search omits
it, use this exact known link and current first-party documentation; never
invent an API path such as `/api/v1/contracts/{operation}`. A 401 requires
an existing Weft credential through a secure HTTP executor bound to the exact
Weft origin, with redirects disabled. Never print the credential or put it in
a URL. Never forward it to Massive or SEC. If this read is unavailable, report
that limitation rather than inventing schema or requesting a new secret.

- Operation `massive-sec-filing-index`; access `massive-sec-filing-index-x402-base`.
- GET `https://agent.massive.com/stocks/filings/vX/index`; no body.
- Observed USD 0.01 per request, x402 Base, synchronous terminal coverage.
  The live challenge is authoritative. Set a tight cap.
- Full contract callability is complete. Normalized output schema is null;
  the response points to the provider OpenAPI at
  `/paths/~1stocks~1filings~1vX~1index/get/responses/200/content/application~1json`.
  The official documentation supplies the response fields below.

### Request bindings

All fields below are URL-encoded query parameters with the same wire name.
Use one exact ticker or CIK for this workflow; omit unrelated filters.

| Field | Rule |
|---|---|
| ticker or cik | String; preserve CIK as a string |
| filing_date.gte | Inclusive YYYY-MM-DD lower bound |
| filing_date.lte | Optional inclusive upper bound |
| form_type | Exact base form when amendments excluded |
| form_type.any_of | Comma-separated base and amendment, e.g. `8-K,8-K/A`; omit form_type when using it |
| limit | Integer 1–10000; set workflow default 5 rather than provider default 1000 |
| sort | Set `filing_date.desc` |

Example: GET the active URL with `ticker=AAPL`,
`form_type.any_of=8-K,8-K/A`, `filing_date.gte=2026-06-01`, `limit=5`,
`sort=filing_date.desc`. Do not send APIToll `includeAmendments`, `form` or
`since` parameters here. The live test returned HTTP 200 with status OK, two AAPL records and no
next_url; the records matched the SEC submissions read in that test.

### Response fields

The provider documentation defines root `/results` (array), `/status` (`OK`),
`/request_id` (string) and optional `/next_url` (string). Each result's optional
strings are `accession_number`, `cik`, `filing_date`, `filing_url`, `form_type`,
`issuer_name`, `ticker`. Thus `/results/i/filing_url` supplies the source link
and `/results/i/accession_number` supplies the filing key. Validate missing
fields; no report date or filing text is defined. [Official schema](https://massive.com/docs/rest/stocks/filings/index).

Read the returned SEC URL to summarize actual content. A link can identify a
full submission text rather than one HTML document: verify issuer/accession,
then use its document boundaries to distinguish primary filing and exhibits.
Do not invent claims from a filename. Optional `next_url` means more results;
a subsequent page is not a documented free poll and needs its own payment
contract and authorization. The one-call workflow reports its coverage limit.

### Weft and CLI envelopes

The tested CLI uses `{schema_version: "2", ok, meta, data}`. `data.status` is
the merchant HTTP code; `ok: true` can coexist with merchant HTTP 404. Parse
JSON string `data.body`, or decode `body_base64` when supplied. If the body is
saved, read the file named by `meta.saved_path`; the path itself is not JSON.
`meta.receipt_path` names a receipt file. Direct MCP envelopes can differ.

Observed CLI receipt fields are `data.paidUsd`, `heldUsd`, `paymentStatus`,
`txHash`, `artifactId`, `protocol`; MCP may expose snake_case. Read actual
fields and report paid plus held, even when the merchant body says no charge.
Record current search identifiers when CLI cannot send attribution. Inspect
help rather than adding invented flags. Never repeat an ambiguous purchase.

## Historical failed candidate: APIToll

The initial `bazaar-apitoll-13` query for AAPL, 8-K, since 2026-06-01,
limit 5 and amendments true returned HTTP 404 `no_results`. SEC submissions
contained two matching records. Receipt: paid USD 0, held USD 0.003, pending,
despite the merchant's no-charge message. Later free coverage inspection
reported an old latest-8-K date despite a fresh retrieval timestamp. This
route does not support a current-coverage claim and is not the active recipe.
