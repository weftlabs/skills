# Evaluation — 2026-09-10

The first fresh Pi CLI smoke used APIToll for AAPL's five most recent 8-Ks
since 2026-06-01, including amendments. It made one paid call. HTTP 404
`no_results` returned no filings; the receipt recorded paid USD 0 and held
USD 0.003, pending. The body said no charge; that did not erase the hold.
No retry occurred. This is a failed paid discovery result.

Independent free SEC submissions contained an 8-K/A filed 2026-09-01 and an
8-K filed 2026-07-30. Pi read their primary documents and produced a sourced
brief, but that recovery does not prove the Weft-paid APIToll route worked.
The July filing's Exhibit 99.1 was not read. The Form 4 boundary made no paid
call and did not silently substitute a supported form.

The revision replaces the active listing route with Massive after reading
its full Weft contract and official output documentation. It also fixes
contract-link retrieval, CLI envelope decoding and receipt interpretation.

These are shared-account smoke results with explicit skill loading, not a
paired benchmark, automatic-trigger test or proof of all-company coverage.
Final settlement is not verified. Private traces and account data are omitted.

The initial run used a USD 0.03 per-call cap despite lower known route prices.
It stayed within authorization but did not follow the intended tight cap.
The revision explicitly separates task allowance from the quoted per-call cap.

## Revised live result

A second fresh Pi session used Massive with the same AAPL 8-K-family date
window, limit 5 and descending filing dates. One separately authorized paid
request returned HTTP 200, status OK, two records and no next_url. Their
accessions matched the two records in an independently read SEC submissions
window. Pi read the complete SEC submission texts, distinguished primary
filings from exhibits, and cited both filings in the brief. It also read the
original April filing to explain the amendment, without counting that older
filing in the requested date window. The July Exhibit 99.1 was read in this
second run, unlike the first run.

The current quote and per-call cap were both USD 0.01, below the USD 0.03
task allowance. Receipt at capture: paid USD 0, held USD 0.01, pending. No
paid retry or second page was requested. APIToll was not used. The known
immutable contract was read with existing Weft authentication and redirects
disabled. CLI attribution identifiers were recorded but not sent because
the installed fetch command had no corresponding flags.

This verifies one live listing-to-source-brief path. It does not establish
all-company coverage, settlement completion or comparative skill uplift.
