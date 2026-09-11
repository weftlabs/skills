# Real skill runs

These screenshots show edited task/result excerpts from Pi runs on
10 September 2026. They are rendered examples, not captures of Pi's native UI.
The JSON inputs preserve source-file hashes. Full traces and receipts remain
private; no API was called to generate these images.

| Skill | Screenshot | Evidence type |
|---|---|---|
| IBAN bank lookup | [PNG](screenshots/iban-bank-lookup.png) | German public example, live Strale lookup |
| Company financial snapshot | [PNG](screenshots/company-financial-snapshot.png) | Corrected replay of saved Atlas data |
| SEC filings brief | [PNG](screenshots/sec-filings-brief.png) | Revised live Massive run plus SEC source reads |
| Stock news sentiment | [PNG](screenshots/stock-news-sentiment.png) | Corrected replay of a historical Massive news sample |
| Watchlist technical screen | [PNG](screenshots/watchlist-technical-screen.png) | Corrected replay of four Massive indicator responses |
| YouTube to text | [PNG](screenshots/youtube-to-text.png) | Live Atlas extraction |
| Transcript to podcast | [PNG](screenshots/transcript-to-podcast.png) | Live BlockRun speech using an existing transcript/script |

Stock-news and watchlist skill publication is owned by
[PR 23](https://github.com/weftlabs/skills/pull/23); the screenshots describe the
recorded candidate runs, not a claim that the skills are installed everywhere.

For replay examples the provider panel shows the **original retrieval** cost;
the replay made no new purchase. Pending receipts are shown as held, never as
settled. The podcast run reused a transcript whose separate original retrieval
held $0.02; its panel shows only the speech generation. Model-inference costs
are excluded. No current price or final settlement is claimed.

## Earlier runs

The revised examples supersede the initial company/market outputs for display.
The earlier UK IBAN response was partial; the German example shows a complete
bank mapping. Invalid IBAN and synthetic finance cases were unpaid boundary
checks, not successful provider calls. The first YouTube attempt stopped on a
contract-discovery gap. The local-TTS experiment was rejected and is not a
supported podcast workflow. The failed APIToll SEC call remains in the private
evaluation ledger; it is not part of the later Massive run's receipt.

The earlier LinkedIn trial is evidence for comment retrieval, not a completed
sentiment evaluation. It is not rendered as a successful sentiment run.

## Regenerate

See [generator commands and input contract](../../tools/session-preview/README.md).
Build into a temporary directory, capture, inspect, then copy approved PNGs
to `screenshots/`. This does not replace workflow covers or automatically add
screenshots to the dashboard marketplace.

Provider logos are reused from Weft's catalog (`weft-app/public/logos/catalog/`):
Massive, x402 Atlas, Strale and BlockRun. Provider marks identify the services
used and do not imply endorsement.

## Full recorded sessions

[Browse all ten Pi runs and their 30 screenshots](pi-sessions/README.md).
These preserve the recorded messages with Markdown formatting and explicit
private-detail redactions, including failed and rejected test attempts.
