# Evaluation — 2026-09-10

One fresh Pi CLI session exercised the candidate and core Weft skill with
explicit skill loading. This is a shared-account live smoke test, not a paired
benchmark or an automatic-trigger test.

AAPL financials returned HTTP 200 from Atlas. The receipt at capture recorded
paid USD 0, held USD 0.01, pending. No repeat financial purchase occurred.
SEC company facts were independently read and matched by concept, unit,
accession and period for revenue, net income and operating cash flow.
Filing HTML bodies were not read for the financial task.

The paid dataset lacked cash and debt; the output kept them unavailable.
Quarterly operating cash flow covered 2025-09-28 through 2025-12-27, while
quarterly revenue and net income covered 2026-03-29 through 2026-06-27. The
output flagged this mismatch rather than treating all rows as one quarter.
The ambiguous Mercury boundary asked for the issuer and made no paid call.

Revisions clarify per-metric freshness, missing duration versus instant facts,
CLI body/receipt decoding, and exact immutable contract retrieval. These
revisions can reuse the saved response; they do not justify another purchase.
Final settlement, broad issuer coverage and causal skill improvement are
unproven. Private traces, wallet settings and request identifiers are omitted.

The initial run used a USD 0.03 per-call cap despite lower known route prices.
It stayed within authorization but did not follow the intended tight cap.
The revision explicitly separates task allowance from the quoted per-call cap.

## Revised saved-data check

The second fresh Pi session reused the original Atlas body and previously
read SEC facts. It made zero new financial purchases. The revised snapshot
kept cash/debt unavailable and separated Q1 operating cash flow from Q3
revenue/net income. Its historical receipt remained distinct from the replay's
zero new cost.

A separate synthetic unpaid boundary supplied revenue with an end date and
no start date. The output correctly labeled duration unknown, not an instant
balance. This is a constructed interpretation check, not live provider data.
