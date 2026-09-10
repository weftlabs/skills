# Observed operation contracts

These are recoverable contracts from one run, with separate documentation
checks on 2026-09-10. They are not a claim that the current Weft catalog is
complete. Rediscover operations and copy current attribution; IDs below are
historical evidence, not a substitute for search.

## Apify prepaid access

| Field | Observed contract |
|---|---|
| Provider / operation | Apify / `bazaar-apify-0` |
| Purpose | Fund access to the comments actor |
| Request | `GET https://agi.apify.com/protocols/x402/prepaid-tokens?amount=1&currency=usd` |
| Query inputs | `amount`: required decimal string, minimum `1`; `currency`: required string `usd` |
| Body / path | No body or variable path |
| Headers | Payment handled by Weft; do not construct payment proofs |
| Execution | Synchronous HTTP 201; no result poll |
| Price / protocol | Source purchase $1.00 held, x402 exact; live quote controls |
| Output | `/token`: secret string; `/remainingBalanceUsd`: number; `/expiresAt`: expiry string |

Decode the Weft body privately. The token is an output credential intended
only for Apify. Store it in memory or a mode-0600 task file if needed, never
in the skill or a transcript. A returned balance is credit, not a refund.

[Apify's current AGI documentation](https://agi.apify.com/) confirms the
bodyless purchase, minimum $1, direct bearer-authenticated API use, and
non-refundable credit with account expiry. Read the returned expiry and current
terms; do not promise a fixed lifetime. The source observed a 14-day expiry.

Current MCP search on 2026-09-10 supplies an immutable
[Apify access contract](https://weft.network/contracts/curated-marketplace/65d682303e260ce392a17af87bdaa0a95de45e218747e9197775a314c4837be9/bazaar-apify-0.json). Read it through an authenticated Weft connection;
an unauthenticated HTTP 401 does not establish that the contract is missing.
The reviewed contract contains typed token fields under
`operation.input.source_contract.properties.output.properties.example`, while
`operation.output.schema` is null and callability is still marked incomplete.
The `example` wrapper describes the source schema, not the runtime response.
This reconciles the legacy CLI omission; it does not establish fresh execution
or independent outcome validation.

## LinkedIn comments actor

| Field | Observed contract |
|---|---|
| Provider / actor | Apify / `harvestapi/linkedin-post-comments` |
| Purpose | Comments and author profile headlines from the supplied post |
| Request | `POST https://api.apify.com/v2/acts/harvestapi~linkedin-post-comments/run-sync-get-dataset-items` |
| Path binding | Actor name with `/` represented by `~`; fixed actor for this contract |
| Query | None in the successful source request |
| Headers | `Content-Type: application/json`; issued token bound to `Authorization: Bearer <token>` |
| Execution | Synchronous root JSON array; no polling was used |
| Cost | Metered against prepaid credit, not another Weft payment; final usage unknown |

Observed body, with the task input substituted:

```json
{
  "posts": ["<supplied LinkedIn post URL>"],
  "maxItems": 100,
  "scrapeReplies": false,
  "profileScraperMode": "short"
}
```

The workflow requires `posts` as a one-element string array even if the actor
schema calls it optional. `maxItems` is an integer coverage limit;
`scrapeReplies` is boolean; `profileScraperMode` is the string `short`.
Other actor modes and reply scraping are outside the observed workflow.
The [current actor input schema](https://apify.com/harvestapi/linkedin-post-comments/input-schema)
confirms these input fields. Review its pricing before execution.

Successful rows expose the following required shortlist fields:

| Pointer, for each array item `i` | Type | Behavior |
|---|---|---|
| `/i/actor/name` | string | Name as supplied; missing/empty excludes row |
| `/i/actor/position` | string | Source headline; may be absent in future responses |
| `/i/actor/linkedinUrl` | string | Profile URL; validate before rendering |
| `/i/commentary` | string | Comment text; missing/empty excludes row |
| `/i/linkedinUrl` | string | Source comment URL; optional for the output |

Unknown fields can be ignored. There is no required structured company field
in short mode. Preserve a headline when role/company cannot be separated
without guessing. All 100 observed rows had position and profile URL; this is
not a guarantee for other posts.

The [Apify sync endpoint reference](https://docs.apify.com/api/v2/actor-run-sync-get-dataset-items-post)
now documents the `/v2/actors/` spelling. The source used `/v2/acts/`.
Confirm the current accepted route before execution. The reference documents
a 300-second sync ceiling and a possible HTTP 408; a lost response does not
prove that work stopped. It also documents `maxTotalChargeUsd` and
`restartOnError` query controls. These were not used in the source run and
need calibration before they are claimed as tested safeguards. Do not
interpret the body field `maxItems` as a monetary cap.

## Pipe and lifecycle boundary

The token is the only service-output-to-service-input credential edge.
The post URL is a user input. Actor rows feed the local analysis and the artifact described in SKILL.md.
Post text, when needed for interpretation, comes from the supplied post or
the user; this contract does not retrieve post content or media.

Stop on a contract gap, invalid response, missing token, refused payment,
timeout, or ambiguous submission. Never repeat the token purchase or actor
POST to discover status. A future async alternative needs its own documented
run-ID extraction, free read lifecycle, status values, and terminal dataset
mapping before it becomes an active path.
