# Recorded Pi session screenshots

Thirty PNGs from ten real Pi sessions run on 10 September 2026. These use the
Weft session template and rendered Markdown. No API calls were made to produce
the screenshots. Each run includes an opening view, its final visible message
with the provider panel, and the complete visible conversation.

Local paths, account balances/policies and internal identifiers were replaced
with explicit removal markers before capture. Messages were not summarized.
Tool output and reasoning are omitted. Raw transcripts and HTML remain private.
The manifest records the original source hash and each published PNG hash.

These are test records, not ten successful marketplace workflows. The rejected
local-TTS experiment is historical evidence only; the supported podcast skill
uses Weft. Initial/blocked attempts are retained with their original outcomes.
Receipt amounts are those observed at the time: held is not settled, and
Unknown means no verified amount was supplied to the panel. Model costs are
excluded. Corrected summary examples remain in the parent directory.

| Run | Evidence type | Screenshots |
|---|---|---|
| Make a short podcast from a transcript | Live BlockRun speech test | [Opening](distill-pi-blockrun-speech-test/session.png) · [Result](distill-pi-blockrun-speech-test/session-result.png) · [Full](distill-pi-blockrun-speech-test/session-full.png) |
| Podcast attempt — rejected local TTS | Rejected local-TTS experiment; unsupported | [Opening](distill-pi-podcast-local-test/session.png) · [Result](distill-pi-podcast-local-test/session-result.png) · [Full](distill-pi-podcast-local-test/session-full.png) |
| YouTube and podcast — blocked initial attempt | Blocked initial attempt | [Opening](distill-pi-youtube-podcast-test/session.png) · [Result](distill-pi-youtube-podcast-test/session-result.png) · [Full](distill-pi-youtube-podcast-test/session-full.png) |
| Turn a YouTube video into text | Live YouTube transcript extraction | [Opening](distill-pi-youtube-podcast-test-2/session.png) · [Result](distill-pi-youtube-podcast-test-2/session-result.png) · [Full](distill-pi-youtube-podcast-test-2/session-full.png) |
| Company Run | Initial live financials / failed SEC request | [Opening](finance-skill-evals-company-run/session.png) · [Result](finance-skill-evals-company-run/session-result.png) · [Full](finance-skill-evals-company-run/session-full.png) |
| Company Run2 | Live SEC request + financials replay | [Opening](finance-skill-evals-company-run2/session.png) · [Result](finance-skill-evals-company-run2/session-result.png) · [Full](finance-skill-evals-company-run2/session-full.png) |
| Look up bank details from an IBAN — run | Initial live UK IBAN lookup; partial response | [Opening](finance-skill-evals-iban-run/session.png) · [Result](finance-skill-evals-iban-run/session-result.png) · [Full](finance-skill-evals-iban-run/session-full.png) |
| Look up bank details from an IBAN — run2 | Revised live German IBAN lookup | [Opening](finance-skill-evals-iban-run2/session.png) · [Result](finance-skill-evals-iban-run2/session-result.png) · [Full](finance-skill-evals-iban-run2/session-full.png) |
| News and technical screen — saved-data replay | Saved-data replay; no new purchase | [Opening](finance-skill-evals-market-replay/session.png) · [Result](finance-skill-evals-market-replay/session-result.png) · [Full](finance-skill-evals-market-replay/session-full.png) |
| Market Run | Initial live news and indicator requests | [Opening](finance-skill-evals-market-run/session.png) · [Result](finance-skill-evals-market-run/session-result.png) · [Full](finance-skill-evals-market-run/session-full.png) |

Renderer and capture commands: [session preview tool](../../../tools/session-preview/README.md).
