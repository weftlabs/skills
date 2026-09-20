# US RentCast data through Weft

RentCast supplies US rental records and estimates. It is not an exact-date
booking engine. Discover live operations with `weft_search` and check inputs,
coverage, price, and access method. Do not apply this provider to another
country without a documented coverage change.

## Documented fallback when catalog discovery misses

Provider documentation: https://paywithlocus.com/x402/rentcast.md

OpenAPI: https://rentcast.x402.paywithlocus.com/openapi.json

The documented x402 base is
`https://rentcast.x402.paywithlocus.com/rentcast/`.
Read current docs before using these POST routes:

- `rental-listings`: city/state, bedroom and price ranges, Active status, limit.
- `rent-estimate`: full address OR exact latitude/longitude, plus verified
  propertyType, bedrooms, bathrooms, squareFootage where known, and compCount.

A catalog miss does not authorize invented attribution. Use fresh matching
attribution if available; otherwise record the official-doc fallback without
inventing operation IDs or borrowing them from unrelated results.

An illustrative listings body is:

```json
{"city":"USER_CITY","state":"USER_STATE","bedrooms":"2","price":"0:6000","status":"Active","limit":5}
```

Replace all filters from the user's request. Listing range inputs are strings;
estimate bedrooms, bathrooms, floor area, coordinates, and compCount are numbers.
Do not send a guessed input merely to fill a field. Use the live schema to
decide whether an unknown input can be omitted.

## Locus request identity

The provider requires the `x-locus-request-id` from the initial unpaid HTTP 402
challenge to accompany the paid request. The response can expose `requestId`
in its body and `locus-request-id` in its headers. The input header includes
the `x-` prefix. This is a request identifier, not a credential or payment proof.

If the current Weft runtime handles this documented handshake, use it. If
manual challenge preparation is required, the optional standard-library helper
[locus_challenge.py](../scripts/locus_challenge.py) makes one unpaid request.
It never signs or pays. It accepts only the documented listing and estimate
routes, validates the challenge, and outputs the exact `next_fetch` arguments.

On a shell-capable host:

```sh
python3 scripts/locus_challenge.py \
  https://rentcast.x402.paywithlocus.com/rentcast/rental-listings \
  /absolute/path/to/request.json > /absolute/path/to/challenge.json
```

Resolve the script relative to this skill directory. For an estimate, use its
own URL, request file, and challenge output. Save and read the helper output
before making one authorized `weft_fetch` with `next_fetch`; check the task
allowance and add only valid current attribution. Preserve the exact body and
request ID. Do not forward raw payment-required or payment-signature headers.

On a host without a shell, use an available ordinary HTTPS client for this
unpaid request. If neither it nor the current Weft runtime can preserve request
identity, report the integration blocker rather than making a blind paid call.
The helper's fixed $0.05 single-call ceiling is conservative; the live quote
is authoritative. A higher price requires a deliberate updated decision within
the user's allowance, not an automatic retry or silent increase.

After HTTP 200, require successful merchant output and parse its `data`.
Read clipped results through `weft_read_result`. Preserve receipt IDs, account
for `paid_usd + held_usd`, and show actual service contribution. An uncertain
call must not trigger a new challenge and another purchase. Idempotency keys
are not a guarantee that a repeated purchase is free.

## Interpretation

Listing fields can already contain sufficient property detail: do not buy a
separate detail lookup that repeats those fields. Check estimate subject
identity and positive, ordered rent bounds. Inspect comparable status and
dates, remove same-unit aliases, and do not describe old records as current
inventory. Missing consumer listing URLs require an independent original-page
search and identity match, not a generated URL.

In a September 2026 rehearsal, listing and estimate calls cost $0.033 each.
This is historical calibration, not a current price promise. The two-call
US data path succeeded; it did not verify portal availability, furnished
premiums, or a complete relocation recommendation.
