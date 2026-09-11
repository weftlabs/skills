# Evaluation — 2026-09-10

A fresh Pi run with explicit candidate/core skill loading called Atlas job
search for software engineer in Austin. It returned HTTP502 upstream_error,
not a jobs array. The CSV had headers only; no successful hiring discovery
was claimed. Receipt at capture: paid USD0, held USD0.05, pending. Merchant
no-charge wording did not erase that hold. No paid retry occurred. An unpaid
ambiguous boundary asked for scope and rejected guaranteed buying-budget claims.

A fresh no-skill run analyzed the identical saved error body with no network
or purchase. Both runs avoided invented jobs. This compares error handling
only; the baseline had no receipt input, so it cannot compare historical
hold accounting.

The revised candidate uses Linkup source search with a documented JSON body.
The installed CLI had no POST body flag, so Pi used the supported Weft SDK.
Initial free prerequisite checks stopped on unavailable wallet balance and
HTTP504. A later free check exposed a harness parser defect: it read compact
access.price pointers on legacy results[].endpoints[]. No paid Linkup request
had occurred. After reading the actual legacy schema and correcting the
parser, one guarded SDK submission at a USD0.01 cap returned HTTP200. Receipt
at capture: paid USD0, held USD0.01, pending. No paid retry occurred.

Ten returned source pages produced three individual job observations from
three employers, with seven article/index pages excluded. Aggregator posting
dates were preserved; current application status and employer-site accuracy
were not verified. Analysis used only the returned body, with no external
page reads. No contacts, applications or recurring actions occurred.

The source instructions now document compact versus legacy search shapes.
They also clarify mutually exclusive unresolved, excluded, capped-out and
delivered count buckets. This general count clarification was made after the
live run; it is not presented as a separately tested edge case.

Independent review matched all three records to the returned source text and
accepted the valid CSV, 10 = 7 excluded + 3 delivered counts, and explicit
limits on current application status.

A fresh no-skill analysis used the byte-identical successful provider body
with no network or purchase. It returned ten rows by also using nested links
from articles and indexes. Broader coverage is a tradeoff, not inherently
worse. However, six baseline rows had inconsistent CSV field counts, and it
counted an Indeed search URL as a discrete posting. The revised skill output
avoided those observed defects.

The live retest had read earlier baseline/report and initial-run outputs
before acquisition. It was a guided retest with prior-context exposure, not a
blind comparison or proof that the skill caused these differences. The fresh
baseline read only the supplied provider body. No paired acquisition
benchmark, general improvement claim, automatic trigger test, broad coverage
claim or final settlement verification is made. Private traces and account
data are omitted.
