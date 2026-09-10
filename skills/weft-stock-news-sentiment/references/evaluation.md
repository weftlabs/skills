# Evaluation limits

One live Pi trial ran on 2026-09-10 against Massive stock news for AAPL,
2024-01-02 through 2024-01-05 UTC, with a five-article cap. This is a shared-account
trial, not a paired benchmark or a test of current-news freshness.

- One HTTP 200 response returned five articles. Two were excluded because their
  title/description did not show AAPL relevance; three remained. No duplicates.
- Every returned article lacked provider insights. Provider sentiment was
  unknown for all three included articles. A next-page link was not followed;
  all returned articles were dated January 5, so earlier-window coverage is unknown.
- Agent analysis labeled all three included articles negative, then used
  "mixed-to-negative" in its summary. That inconsistency failed the intended
  output contract. The revised skill requires agent counts and prose to agree.
- The receipt showed $0.00 paid and $0.01 held, payment pending. Delivery was
  observed; final settlement was not. No paid retries occurred.
- An ambiguous-company boundary prompt asked for the exact ticker with no purchase.

Only article metadata was used. No independent human sentiment labels or
publisher full-text fact check established accuracy. Contract shape and receipt
checks cannot establish sentiment correctness. A saved-data Pi replay on 2026-09-10 reused the original five records without
network calls, Weft calls, or new purchases. It retained three included and two
excluded records, counted provider unknown = 3 separately from agent negative = 3,
and used "negative in this sample" in its summary. This corrects the observed
count/prose inconsistency on this dataset; it does not verify the sentiment
labels against independent human judgments.
