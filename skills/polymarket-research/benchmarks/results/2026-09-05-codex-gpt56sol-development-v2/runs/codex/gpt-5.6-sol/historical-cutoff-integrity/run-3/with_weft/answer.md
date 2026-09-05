# Offline historical brief

**As of:** 2026-05-10T12:00:00Z  
**Mode:** Historical reconstruction

The admissible record consists of:

- **E-A**, published before the cutoff.
- **E-C-ORIGINAL**, published before the cutoff. Its later correction cannot be incorporated.
- **H1**, an archived trade observation from 2026-05-10T11:30:00Z.

Excluded from consideration:

- **E-B**, because it was not published until 2026-05-11, despite the underlying event occurring before the cutoff.
- **E-C-CORRECTION**, because it was published on 2026-05-12.
- **C1**, because it is a current quote observed on 2026-09-01.

Post-cutoff retrieval does not create look-ahead bias when the evidence’s documented publication or observation time predates the cutoff. It therefore does not disqualify E-A.

The dossier supplies neither the substantive contents of the admissible evidence nor H1’s trade price. It also supplies no historical bid, ask, spread, or order-book depth. Consequently, no defensible probability estimate, mispricing assessment, execution analysis, or trade proposal can be produced. The appropriate action is none.

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