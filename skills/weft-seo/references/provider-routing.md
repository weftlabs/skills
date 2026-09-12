# Provider Routing

Use this after the Ilias kernel names a real evidence gap. The current `weft`
skill owns tool syntax and payment safety. When `weft_*` tools are missing,
the `weft` CLI is the same loop: `weft search`, `weft balance`,
`weft fetch <url> --max-cost-usd <n>`.

Never treat a remembered provider, URL, or price as a current contract.
Search live every time.

## Convert Gaps Into Capabilities

| Decision | Useful capability query | Required contract inputs | Minimum useful output |
|---|---|---|---|
| Which keywords does this domain already rank for? | domain keyword rankings with position, landing URL, and volume | domain, market/location, language | keyword, rank, url, volume definition, market, timestamp |
| Which pages compete for a query? | current Google SERP for query, market, and language | query, country, language | ranked URLs, titles or snippets, query, location, timestamp |
| Is a seed worth a test? | keyword demand **or** (if no volume contract) Trends-style interest | keyword, geography, language, period | **metric definition**, values, unit, geography, period |
| Which sites link here? | backlinks for exact URL or domain | target, target type, freshness | source URL, target URL, link attributes, date |

These are shapes, not vendors.

## Selection Checklist

Before payment, answer from the **current** search hit or its `contract_url`:

1. Can every material input map to a declared typed input?
2. Does the request bind each input to path, query, body, or header?
3. Does the output contain the evidence for **this** decision (volume is not
   Trends; Google SERP is not a generic web search)?
4. Are geography, language, and sample size explicit? If the schema defaults to
   another country, bind the user's market or reject.
5. Sync vs async: if async, the full contract must define a **free** poll.
6. Is the live price within **the spendable asset** and the tight cap?
7. Copy attribution fields when the tool surface has them.

Reject when any required answer is no.

### Incomplete `callability`

- **Reject** when `inputSchema` is missing, or `exampleRequest` is only a type
  map, or the output cannot satisfy the decision.
- **May pay** when inputs bind, the example output matches the decision, and
  the only gap is “response schema not yet paid-probed”. Still the cheapest
  exact fit. Label the metric honestly.

### Relabeling is a bug

- Google Trends `value` 0–100 is relative interest, not search volume.
- Trends `rising` integers (often huge) are rising-score, not monthly volume.
- Generic “web search” JSON is not a Google SERP.
- Domain-ranking `searchVolume` is provider-defined; keep its market.

## Wallet and fetch order

Call `weft_balance` before **each** paid fetch, not only the first in the
session.

- `wallet.totalUsd` can include assets the merchant will not take.
- Base mainnet x402 USDC quotes need `wallet.balanceUsdc` ≥ indexed price.
- Tempo USD does not pay a USDC challenge.
- `INSUFFICIENT_BALANCE` is a hard stop. Tell the user which asset ran out.
  Do not retry. Do not start parallel paid fetches.
- `wallet.balanceUsdc` can still overstate headroom: **held** x402 amounts are
  not free to spend. If a 402 says `required` > live `balance`, stop.
- Some SEO stats settle on **Tempo MPP**, not Base USDC. Match the merchant
  rail. Do not assume Tempo USD pays a USDC quote, or the reverse.

Serialise paid calls. A parallel pair can race the same USDC balance.

CLI: always pass `--max-cost-usd`. POST bodies are JSON with
`--header Content-Type: application/json`. GET inputs go on the query string
only when the contract says so.

## Purchase Record

Before pay:

```text
purpose | provider | operation | inputs | expected output | indexed price | max_cost_usd | spendable asset
```

After pay:

```text
timestamp | payment_status | paid_usd | held_usd | artifact_id or tx | returned scope
```

Cost is `paid_usd + held_usd`. `pending` plus `held_usd` means money likely
moved — do not retry.

## Failure Rules

- Empty or `matchQuality: weak`: reformulate the free search. A remembered
  brand (including Ahrefs) missing from live results is not a catalog bug you
  work around with a stored URL.
- Incomplete contract: do not pay.
- Over-policy or insufficient asset: stop.
- Pending or ambiguous payment: keep the receipt; no retry.
- Partial rows: use returned rows with their sample limit.
