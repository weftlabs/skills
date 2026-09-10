---
name: weft-watchlist-technical-screen
description: Screen a supplied, bounded list of stock tickers using dated RSI and MACD values. Use for "screen my watchlist", "which of these stocks has RSI below 30", or "compare RSI and MACD for these tickers". Return rule matches, numeric evidence, timestamps, and missing-data limits. Does not discover an entire market universe, place trades, or monitor automatically. Load the weft skill for discovery and payment.
---

# Screen a supplied stock watchlist

Compare a user's stock watchlist against explicit RSI and MACD rules in one run.
This experimental workflow has one live Pi trial for two tickers. Numeric
screen results were returned, but the explanation of session completion needed
correction. A saved-data replay addressed that wording with no new requests.
See [the evaluation limits](references/evaluation.md). No independent
indicator accuracy or investment performance is claimed.

## User Goal

| Field | Contract |
|---|---|
| Required input | Exact bounded ticker list. Ask for it if missing; do not invent a market universe. |
| Optional inputs | As-of session, indicator settings, predicate, maximum spend. |
| Default scope | At most 10 unique supplied US stock tickers; daily close RSI(14), MACD(12,26,9); last completed session. |
| Default rule | Report RSI < 30, MACD > signal, and their conjunction. These are descriptive flags, not recommendations. |
| Outcome | One row per supplied unique ticker, values and timestamps, match/not-match/unavailable, settings, receipt. |
| Acceptance | Rule is explicit; exact ticker/time joins; no missing value becomes zero or false; every ticker is accounted for. |
| Independent truth | Recompute predicates from saved provider values; indicator accuracy needs separate price-series calculations under the same adjustment and initialization method. |
| Non-goals | Trades, market-wide stock discovery, live quote claims, price targets, backtests, or recurring monitoring. |

## Before spending

Load the canonical [weft skill](https://weft.network/skills/weft/SKILL.md).
Use its setup and current CLI or MCP flow. Search for RSI and MACD and inspect
both current contracts. Read [references/contracts.md](references/contracts.md)
for typed fields and complete request bindings. Do not guess endpoint
bindings or treat `callability: complete` as proof of live results.

Deduplicate supplied tickers and show the final list. Ask the user to narrow a
list longer than 10 before buying. If the budget cannot cover two calls per
ticker, ask for a smaller list; do not silently drop tickers. Reuse matching data
already acquired in the task. Call `weft_balance` before the first paid fetch;
state expected calls and cost, use tight `max_cost_usd`, and preserve current
search attribution locally; send it only if the execution tool supports it. Do
not invent CLI attribution flags. Exposure is `paid_usd + held_usd` for every request, including
failures. Policy, balance, denylist, and price-cap refusals are hard stops. Do
not retry paid calls, top up, increase caps, or switch wallets automatically.

## Required Flow

1. State settings, rule, and as-of cutoff before acquisition. Resolve the last
   completed session using a current authoritative exchange calendar, including
   holidays and early closes, or use a user-specified historical session. Do not
   use an unfinished daily bar. A daily timestamp, including local midnight,
   identifies a bar; it does not say the session has closed. Establish completion
   separately from current time plus the exchange session schedule, or from a
   user-specified historical session whose date precedes the collection date.
   Disclose any unverified historical holiday or early-close details. Never say
   "timestamp is before 16:00, so the bar is complete". If completion cannot be established,
   disclose the gap and ask for an explicit as-of session before spending.
2. For each unique ticker, fetch RSI and MACD once with daily close settings,
   newest first, `limit=5`, and the same upper timestamp bound through the end
   of the chosen session. This bounded history permits exact joins. Do not buy
   more pages to repair missing coverage.
3. Require successful merchant JSON objects and numeric indicator rows. Attach
   the requested ticker to each response: these rows do not echo the ticker.
   Keep raw timestamps and verify that they are milliseconds before conversion.
   Reject non-finite numbers, invalid timestamps, or RSI outside 0..100. Count
   invalid and duplicate rows. Conflicting rows at one timestamp are unusable.
4. Join each ticker's RSI and MACD on exact timestamp, not array position.
   Select the newest common completed-session timestamp at/before the cutoff.
   Show the actual session and requested session. Older data remains visible as
   stale/unavailable for the requested-session screen; do not silently substitute
   it as current. Preserve unmatched observations and count them.
5. Apply the exact numeric predicates locally to full precision, then round
   for display. `RSI < 30` excludes 30; `MACD > signal` excludes equality. Report
   each flag and their conjunction. Missing/invalid/stale data is `unavailable`,
   not `not match`. Do not rank cross-ticker MACD magnitudes: they are price-scale
   dependent. A positive histogram is a state, not proof of a new crossover.
6. If the user explicitly requests crossovers, require two consecutive completed
   session observations for the same ticker and settings, with prior difference
   <= 0 and current difference > 0 for an upward crossing (reverse for downward).
   Prove session adjacency against the calendar; otherwise report unavailable.
7. Return one row per unique input ticker, settings, omissions, and paid/held
   receipt. Stop a failed paid stage and show remaining tickers as not attempted;
   do not imply that the incomplete watchlist passed the screen.

## Output

State the supplied list and removed duplicate count, requested as-of session,
collection time, time zone, interval, price series, windows, adjustment basis,
and exact rule. Cite the provider routes/contracts and retain request IDs.

| Ticker | Session date / returned bar timestamp | RSI14 | MACD | Signal | Histogram | RSI < 30 | MACD > signal | Both / status |
|---|---|---:|---:|---:|---:|---|---|---|

Reconcile unique inputs = matches + non-matches + unavailable/not-attempted.
For unavailable rows state why: missing field, no common timestamp, stale bar,
failed request, or budget stop. Explain that the indicator state describes
historical price data and does not establish future returns or suitability.

| Request / ticker | Paid USD | Held USD | Status | Result |
|---|---:|---:|---|---|

Unknown accounting fields stay unknown. Include failed/held requests. Pending
settlement is not completed settlement. Keep analysis separate from raw values.

## Provenance

Free contracts and full official OpenAPI schemas reviewed 2026-09-10. One
Pi trial made four HTTP 200 indicator requests for AAPL/MSFT and the historical
2023-12-29 session. Both failed the conjunction on returned values. Receipts:
$0.00 paid, $0.04 held, pending. This does not verify indicator calculations
against an independent price series. An offline replay preserved both non-matches
and separated bar identity from completion evidence. See [the evaluation note](references/evaluation.md).
