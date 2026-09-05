## Offline brief

**As of:** 2026-05-10T12:00:00Z  
**Mode:** Historical snapshot

Only evidence published or observed by the cutoff is admissible:

- **E-A** was published on 2026-05-09 at 10:00Z and is included despite later retrieval.
- **E-C-ORIGINAL** was published on 2026-05-08 and is included. Its later correction was not yet public.
- **H1** records a trade observation from 2026-05-10 at 11:30Z and is included.

Excluded:

- **E-B**, because it was not published until 2026-05-11, notwithstanding its pre-cutoff event time.
- **E-C-CORRECTION**, because it was published on 2026-05-12.
- **C1**, because it is a current quote observed on 2026-09-01 and cannot reconstruct the cutoff snapshot.

The supplied dossier contains no substantive evidence text, numerical historical trade price, or archived bid, ask, spread, or depth. It therefore does not support a defensible probability estimate or actionable trade proposal.

BEGIN_DECISION_RECORD
MODE=HISTORICAL
SOURCE_CUTOFF=2026-05-10T12:00:00Z
ACCEPTED_EVIDENCE=E-A,E-C-ORIGINAL,H1
EXCLUDED_EVIDENCE=E-B,E-C-CORRECTION,C1
CURRENT_SNAPSHOT_USED=NO
HISTORICAL_BID_ASK=UNAVAILABLE
HISTORICAL_DEPTH=UNAVAILABLE
RETRIEVAL_AFTER_CUTOFF=ALLOWED
PROBABILITY=OMITTED
TRADE_ACTION=NONE
END_DECISION_RECORD