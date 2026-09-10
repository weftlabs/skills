# Evaluation

Experimental workflow evaluated on 2026-09-10 in fresh Pi sessions using the
configured default model, with the skill explicitly loaded. This is one live
smoke plus a saved-input analysis comparison, not an automatic-trigger test,
paired live-provider benchmark or proof of broad skill uplift.

## Live result

One Strale GET for public Belgian enterprise number `BE0477472701` returned
HTTP 200 and the matching number `0477.472.701`, legal name ODOO, legal form,
registry status, address, registration date and establishment count. CSV and
brief fields were independently checked against the preserved provider body.
This validates source fidelity; no second official registry source was read to
establish independent registry truth.

The provider identifies CBEAPI.be as its upstream vendor and KBO/BCE as the
underlying register. Source update time, industry, abbreviation and commercial
name were missing. The output left these unknown, distinguished the derived VAT
number from a VIES check, and made no creditworthiness or ownership claim.

One receipt recorded $0 paid and $0.054 held with pending settlement at capture.
No retry occurred. The “Acme somewhere in Europe” boundary requested jurisdiction
and an exact number without a purchase or contact.

## Correction and comparisons

The initial output incorrectly placed normal pending payment settlement under
“defects”. The skill now separates payment state, source coverage limits and
actual task errors. A guided replay produced corrected output without another provider call. It
also read unrelated prior test material despite the input restriction, so it
is not isolated evidence of skill improvement. Original evidence remains
separate; the clean same-input comparison below is a different pair of runs.

Separate with-skill and no-skill Pi analysis runs received the same saved company
body with no network or purchases. They assess only output behavior on that
record. The live run's discovery and payment steps are not part of this baseline
comparison. No claim of global coverage, legal due diligence, factual registry
accuracy, final settlement or statistical performance follows from these tests.
