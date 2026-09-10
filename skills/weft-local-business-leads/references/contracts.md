# Contract — inspected 2026-09-10

[Immutable Weft contract](https://weft.network/contracts/curated-marketplace/d29cfafb9253c9f21d4d307b040fabc579f9db9321bf4b03684320daccaa6f1d/bazaar-x402-atlas-152.json).
Operation `bazaar-x402-atlas-152`, access `bazaar-x402-atlas-152-x402`.
GET `https://places.use.x402atlas.com/local`, no body, synchronous terminal response.
Indexed USD 0.02/request; current quote wins.

## Contract access and envelopes

Use the current search contract_url. If legacy CLI search omits it, read the
exact immutable link above; never invent a contract API path. An authenticated
read may use the existing Weft credential in memory only for the exact Weft
origin, with redirects disabled. Never print credentials or send them to Atlas.

CLI v2 can return `{ok, meta, data}` with `data.body` as a JSON string and
`data.status` as merchant HTTP status. `ok` alone does not prove success.
Read `meta.saved_path` if output was saved; it is a path, not the data body.
Decode body_base64 when present. Actual MCP envelopes can differ. Observed
CLI receipt names are paidUsd, heldUsd, paymentStatus, txHash, artifactId;
normalize from the actual envelope, preserving unknown fields as unknown.
Count paid plus held. Record attribution if the installed CLI cannot send it.

The normalized output schema is null. Typed source fields are at
`operation.input.source_contract.properties.output.properties.example`. The
catalog example wrapper is not proof of a runtime wrapper. Establish the
actual decoded body root before using the candidate pointers below. Contract
callability was classified incomplete in the catalog. A separate paid live
smoke returned HTTP200 with query, queried_at and 20 results at the body root;
see the evaluation notes. That observed delivery does not change the catalog
classification or prove coverage beyond the tested request.

## Request and output

URL query: required q (string up to400 chars); optional gl/hl (country/language
strings up to8), ll (viewport up to64 chars). Put category and city in q,
e.g. `dental clinics in Austin, Texas, United States`, gl=us, hl=en. ll is
only a bias and not required; do not fabricate coordinates. No limit or page
parameter is declared.

Candidate root requires query, queried_at (timestamp), results (array).
`/results/i/title` is required. Optional row fields: place_id, data_id,
address, type, website, phone, open_state, price (strings); position and
reviews (integers); rating (number); gps_coordinates.latitude/longitude
(numbers); hours and service_options (objects with upstream-specific fields).
Do not infer opening hours or services from arbitrary object keys.

Map title/type/address to branch identity/category/area. place_id is the
preferred branch dedup key. website/phone are optional; do not fill them
from another similarly named branch. queried_at is retrieval time, not
business record update time. A request URL with place_id is provenance,
not proof that an independent business website was read.
