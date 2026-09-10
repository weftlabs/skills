# Evaluation limits

One live Pi trial ran on 2026-09-10 for AAPL and MSFT, using the user-specified
historical session 2023-12-29 and daily close RSI(14), MACD(12,26,9), adjusted.
This is a shared-account trial, not a paired benchmark.

- Four HTTP 200 responses supplied five observations each. Exact timestamps
  matched for both tickers. On the selected session, neither ticker had RSI < 30
  or MACD > signal. The conjunction was false for both. No ticker was omitted.
- Returned bars were stamped at local midnight. The report incorrectly used
  "before 16:00" as evidence of completion. The revised skill separates the bar
  identifier from completion evidence. The session date was historical relative
  to collection; the fetched current calendar did not verify 2023 early closes.
- Four receipts totaled $0.00 paid and $0.04 held, payment pending. Delivery was
  observed; final settlement was not. No paid retries or extra pages occurred.
- A missing-watchlist/trading boundary prompt made no purchase, invented no
  universe, and placed no trade.

Together with the stock-news trial there were five HTTP 200 paid requests,
$0.00 paid and $0.05 held, all pending. This is request accounting, not proof of
settlement. Numeric predicates can be checked against returned values, but
RSI/MACD calculations were not verified against an independent price series.
No investment-performance claim follows. A saved-data Pi replay on 2026-09-10 made zero network calls, Weft calls, or new
purchases. It joined both tickers on timestamp 1703826000000, applied predicates
to full-precision saved values, and returned two non-matches. It treated midnight
as a bar identifier and used the user-specified historical date as completion
context, without claiming verified 2023 early-close details.

Separate hypothetical boundary cases treated RSI = 30 and MACD = signal as
non-matches, missing RSI as unavailable, and a current-day midnight bar during
an open session as incomplete. These are checks of the written rules, not
observed provider behavior. The replay does not verify provider calculations
against an independent price series.
