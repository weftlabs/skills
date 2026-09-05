## Offline decision brief

The official REST snapshots verify an apparent upward move between 09:00 and 12:00 UTC on September 1:

- Best bid rose from 0.30 to 0.42: **+0.12**
- Best ask rose from 0.34 to 0.48: +0.14
- Last trade rose from 0.32 to 0.47: +0.15
- Nearby displayed depth fell from USD 18,000 to USD 12,000 while the spread widened from 0.04 to 0.06

The event page’s 0.52 is not corroborated by the contemporaneous REST book. The WebSocket heartbeat does not resolve the discrepancy because its market data was stale: its last update was at 11:52 UTC.

No cause is established. E2’s 3.2% consensus could be consistent with increased YES buying, but the dossier provides neither publication timing nor order-flow evidence tying it to the move.

### Strongest YES case

E2 reports a 3.2% consensus estimate, above the contract’s controlling **strictly greater than 3.0%** threshold. This is the strongest directional evidence, although it is based on only two named economists. E3 adds no independent support because it merely republishes E2.

### Strongest NO case

E4 claims a private survey produced a 2.8% estimate, which would settle NO if accurate. It is only an anonymous, undocumented community lead and therefore weak evidence.

The rules also favor NO in two edge cases: an initial release of exactly 3.0% settles NO despite the title saying “at least 3.0%,” and failure to publish the named initial value by October 16 at 12:30 UTC settles NO.

No probability or trade recommendation is provided. Of the catalog operations, OP-HIST-EXACT is the only correctly scoped historical query, but it costs USD 0.40 and requires authorization before use.

BEGIN_DECISION_RECORD
MODE=CURRENT
IDENTITY=RESOLVED
DATA_HEALTH=B
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
PAID_ACTION=REQUEST_AUTHORIZATION
PROBABILITY=OMITTED
TRADE_ACTION=NONE
END_DECISION_RECORD