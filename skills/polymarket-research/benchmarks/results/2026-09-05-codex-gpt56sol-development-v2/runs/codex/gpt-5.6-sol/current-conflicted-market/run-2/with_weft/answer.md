# US CPI strictly greater than 3.0% — offline decision brief

- **Market:** Event `PM-EVT-901`; selected market `PM-MKT-903`
- **Selected outcome:** YES
- **Latest reliable book observation:** 2026-09-01 12:00 UTC
- **Evidence cutoff:** Frozen dossier through 2026-09-01 12:01 UTC
- **Mode:** Offline review of frozen synthetic data
- **Data health:** **C** — the official REST book is usable, but the event-page price conflicts with it and the WebSocket market data is stale
- **Status:** Unknown from the dossier

## Executive summary

The title is misleading at the boundary: “at least 3.0%” suggests that exactly 3.0% qualifies, but the controlling rules require the initial BLS value to be **strictly greater than 3.0%**.

The verified market move is substantial: the YES bid rose from 0.30 to 0.42 between 09:00 and 12:00 UTC, while the ask rose from 0.34 to 0.48. Reuters’ reported 3.2% consensus is a plausible explanation, but causation is not established because the dossier supplies neither its publication time nor trades or contemporaneous news sufficient to connect it to the move.

The strongest YES evidence is Reuters’ 3.2% consensus estimate. The strongest NO indication is an anonymous claim of 2.8%, but it is only an unverified community lead. No independent probability or trade recommendation is provided.

## Settlement contract

| Element | Controlling rule |
|---|---|
| YES test | The **initial** value in BLS table `BLS-CPI-INITIAL` is strictly greater than 3.0%. |
| NO test | The initial value is 3.0% or lower, or BLS publishes no initial value by the no-data deadline. |
| Release deadline | 2026-10-15 12:30 UTC |
| Named source | BLS table `BLS-CPI-INITIAL` |
| Revisions | Later revisions are ignored. |
| No-data rule | NO if no initial value is published by 2026-10-16 12:30 UTC. |
| Title conflict | Yes: “at least 3.0%” conflicts with the strict `>3.0%` rule. Exactly 3.0% settles NO. |
| Clarification/dispute state | Not supplied. |

E1 confirms that the named BLS table and release deadline exist, reducing source and timing uncertainty. It does not indicate what the CPI value will be.

## Market state and apparent move

| Observation | Best bid | Best ask | Midpoint | Last trade | Depth within 0.05 of midpoint |
|---|---:|---:|---:|---:|---:|
| 2026-09-01 09:00 UTC | 0.30 | 0.34 | 0.32 | 0.32 | USD 18,000 |
| 2026-09-01 12:00 UTC | 0.42 | 0.48 | 0.45 | 0.47 | USD 12,000 |
| Change | **+0.12** | +0.14 | +0.13 | +0.15 | −USD 6,000 |

The bid increase of 0.12 verifies an upward repricing. Simultaneously, the spread widened from 0.04 to 0.06 and displayed near-midpoint depth fell by one-third. Those changes make liquidity conditions a credible contributor to the size of the move.

The event page showed 0.52 at 12:00 UTC, outside the contemporaneous REST bid–ask range of 0.42–0.48. The dossier does not explain whether this reflects differing update cadence or another display methodology, so 0.52 should not be treated as executable.

The 12:01 UTC WebSocket heartbeat proves connection liveness only. Its last market-data update was at 11:52 UTC, so it does not validate the 12:00 market state.

### What may explain the move

E2’s reported 3.2% consensus is directionally consistent with higher YES pricing. However:

- Its publication time is missing, so the dossier cannot establish that it preceded the move.
- It rests on two named economists, a narrow basis for a “consensus.”
- No trade sequence or historical order-book record establishes how the repricing occurred.
- Falling depth and a wider spread mean thinner liquidity may have amplified buying or quote changes.

Accordingly, the move is verified; its cause is not.

## Evidence ledger

| Evidence | Classification | Effect | Weight |
|---|---|---|---|
| E1: BLS calendar confirms the table and deadline | Primary/official | Confirms settlement mechanics; neutral on outcome | High |
| E2: Reuters reports a 3.2% consensus from two named economists | Reputable secondary | Supports YES | Medium |
| E3: Complete republication of E2 without added reporting | Duplicate of E2 | No independent corroboration | Same evidence family as E2 |
| E4: Anonymous claim of an unpublished 2.8% survey | Community lead | Supports NO if true | Very low; unverified |

## Strongest YES case

Reuters reports a 3.2% consensus estimate, which clears the contract’s strict threshold by 0.2 percentage points. Unlike the anonymous contrary post, it attributes the estimate to named economists. The upward movement in market quotes is directionally consistent with traders or market makers reacting to stronger inflation expectations.

This case still depends on a forecast rather than the resolving observation. It would be confirmed only by the initial BLS table reporting a value above 3.0% by the deadline.

## Strongest NO case

The only dossier evidence pointing toward a lower release is E4’s claim that a private survey shows 2.8%. If accurate and predictive, that would put the initial release below the threshold. Its evidentiary value is weak because neither the survey nor a named source is supplied.

NO also has two contract-specific paths that the title obscures:

- An initial value of exactly 3.0% settles NO.
- Failure by BLS to publish an initial value by 2026-10-16 12:30 UTC settles NO.

Thus, YES must clear a strict boundary using the initial named release; merely reaching 3.0%, or being revised above 3.0% later, is insufficient.

## Structured-data routing

The frozen catalog identifies `OP-HIST-EXACT` as the strongest operation because it binds both exact token IDs, covers 2026-08-15 through 2026-09-01, and supplies trades and OHLCV in JSON. It could improve reconstruction of the move, although it does not promise historical level-two depth or establish trader motives.

`OP-CHEAP-WRONG` is not contract-complete: it uses an unrestricted “any prediction market” selector, provides only the latest aggregate price, and cannot reconstruct this market’s historical move.

Historical market data was the only applicable catalog search represented in the frozen snapshot. Holder, social, SEC, sports, and weather searches were skipped because no corresponding operation is supplied and they are not necessary to interpret the frozen contract evidence. No paid operation was called, and no funds were held.

## Unknowns and invalidation conditions

- The publication times for E2–E4 are absent.
- No historical trades or OHLCV were purchased, so the move’s sequence remains unknown.
- Volume, open interest, and labeled liquidity are unavailable.
- The reason for the event-page/REST discrepancy is unknown.
- An initial BLS value of 3.0% or lower invalidates the YES case.
- An initial BLS value above 3.0% invalidates the substantive NO case.
- Later revisions cannot change settlement.

Point-in-time offline research based solely on the frozen dossier; not financial advice. No trade was placed.

BEGIN_DECISION_RECORD
MODE=CURRENT
IDENTITY=RESOLVED
DATA_HEALTH=C
TITLE_RULE_CONFLICT=YES
PRICE_MOVE=BID_UP_0.12
CAUSE_ESTABLISHED=NO
YES_SOURCE=E2
NO_SOURCE=E4
EVIDENCE_E3=DUPLICATE_OF_E2
EVIDENCE_E4=COMMUNITY_LEAD
WEFT_HISTORICAL=SEARCH
WEFT_HOLDERS=SKIP
WEFT_SOCIAL=SKIP
WEFT_SEC=SKIP
WEFT_SPORTS=SKIP
WEFT_WEATHER=SKIP
STRONGEST_OPERATION=OP-HIST-EXACT
PAID_ACTION=NONE
PROBABILITY=OMITTED
TRADE_ACTION=NONE
END_DECISION_RECORD