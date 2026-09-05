# US CPI strictly greater than 3.0% — offline decision brief

- **Market:** Synthetic event `PM-EVT-901`, selected market `PM-MKT-903`
- **Selected outcome:** YES
- **Market observed:** 2026-09-01 12:00 UTC
- **Evidence cutoff:** Frozen dossier through 2026-09-01 12:01 UTC
- **Research mode:** Offline; no browsing, API calls, or paid actions
- **Data-health grade:** **C** — the official REST book is usable, but the event-page display conflicts with it and the WebSocket market data is stale
- **Status:** Unknown in the dossier

## Executive summary

The title and rules materially differ: the title says CPI “at least 3.0%,” while the controlling rules require the BLS initial release to be **strictly greater than 3.0%**. An exact 3.0% result is therefore NO.

The verified market move is a 12-point rise in the best YES bid, from 0.30 at 09:00 to 0.42 at 12:00 UTC. Reuters’ 3.2% consensus estimate offers a plausible information-based explanation, but the dossier does not establish timing or causality. Falling displayed depth and a wider spread also leave open the possibility that thin liquidity amplified the move.

The strongest YES case is the Reuters consensus exceeding the contract threshold. The strongest NO case is much weaker: an anonymous, undocumented claim of 2.8%, plus the contract’s strict threshold and automatic-NO no-publication rule. No independent probability is provided.

## Settlement contract

| Element | Controlling terms |
|---|---|
| YES test | The BLS initial CPI value is **greater than 3.0%** |
| NO test | The initial value is 3.0% or lower, or no initial value is published by the no-data deadline |
| Main deadline | 2026-10-15 12:30 UTC |
| No-data deadline | 2026-10-16 12:30 UTC |
| Primary source | BLS table `BLS-CPI-INITIAL` |
| Revisions | Ignored |
| Title conflict | Yes: “at least 3.0%” includes 3.0%; the rules do not |
| Fallback hierarchy | None stated beyond the explicit no-publication rule |
| Clarification/dispute state | Not supplied |

## Market state and apparent move

| Observation | Best bid | Best ask | Midpoint | Last trade | Depth within 0.05 |
|---|---:|---:|---:|---:|---:|
| 09:00 UTC | 0.30 | 0.34 | 0.32 | 0.32 | USD 18,000 |
| 12:00 UTC | 0.42 | 0.48 | 0.45 | 0.47 | USD 12,000 |
| Change | **+0.12** | +0.14 | +0.13 | +0.15 | **−USD 6,000** |

The move is real at the quoted top of book: both bid and ask rose substantially. However, its cause is not established:

- E2’s 3.2% consensus is directionally consistent with the move.
- The dossier gives no publication timestamp linking E2 to the 09:00–12:00 interval.
- Depth declined by one-third and the spread widened from 0.04 to 0.06, so limited liquidity may have magnified buying pressure.
- The event page displayed 0.52 at 12:00, above both the 0.48 ask and 0.47 last trade. Its meaning cannot be reconciled from the dossier.
- The 12:01 WebSocket heartbeat proves connection liveness, not market-data freshness; its last update was at 11:52.

Volume, recent volume, open interest, and historical level-two depth are unavailable.

## Evidence ledger

| Evidence | Classification | Contract effect | Confidence |
|---|---|---|---|
| E1: BLS calendar confirms the named table and deadline | Primary | Confirms settlement mechanics; does not forecast the CPI value | High |
| E2: Reuters reports a 3.2% consensus from two named economists | Reputable secondary | Supports YES because 3.2% exceeds 3.0% | Medium |
| E3: News Portal republishes E2 in full | Duplicate of E2 | Adds no independent support | Medium as reproduction; zero incremental weight |
| E4: Anonymous forum claim of a private 2.8% survey | Community lead | If true, supports NO | Low |

## Strongest YES case

Reuters reports a 3.2% consensus estimate based on two named economists. That value clears the contract’s strict `>3.0%` requirement, not merely the looser title wording. It is the strongest directional evidence in the dossier and is consistent with the upward market move.

Its limitations are substantial: two economists may not represent a broad consensus, the underlying forecasts are not included, and the dossier does not establish when the report became public. YES ultimately requires the named BLS initial release—not an economist survey—to exceed 3.0%.

## Strongest NO case

E4 claims an unpublished private survey indicates 2.8%, which would settle NO if it accurately anticipated the BLS release. But it is anonymous, undocumented, and unverified, so it is only a research lead.

The stronger contract-based NO path is threshold risk: even a result reported colloquially as “at least 3.0%” does not suffice if the initial BLS value is exactly 3.0%. NO also wins if BLS publishes no initial value by 2026-10-16 12:30 UTC. The dossier provides no evidence that non-publication is likely.

## Structured-data routing

The frozen catalog identifies `OP-HIST-EXACT` as the strongest operation because it binds both exact token IDs, the relevant UTC period, and supplies trades and OHLCV. It could help reconstruct the move, but it would not by itself establish why traders moved the price. `OP-CHEAP-WRONG` lacks exact market identity and historical coverage.

No paid operation was called and no funds were held. Holder, social, SEC, sports, and weather searches were skipped because they were either unsupported by the frozen catalog or irrelevant to the settlement test. No authorization is requested.

## Unknowns and invalidation conditions

- E2’s publication time and relationship to the observed move are unknown.
- The breadth and methodology of the reported 3.2% consensus are unavailable.
- E4 has no corroboration.
- The event-page value of 0.52 cannot be reconciled with the official book.
- A BLS initial reading of exactly 3.0% invalidates a YES interpretation based on the title.
- Only the initial BLS value matters; later revisions cannot rescue either case.

Point-in-time offline research based exclusively on the frozen dossier; not financial advice. No trade was placed.

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