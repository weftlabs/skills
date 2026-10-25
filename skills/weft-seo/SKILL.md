---
name: weft-seo
description: Audit organic search with one money query. Prefer Search Console exports; never buy GSC through Weft. Then buy only missing SERP, demand, or ranking evidence. Use for SEO audits and Blitz vs wait.
metadata:
  category: Content
---

# Weft SEO

Turn an organic-search goal into **one** money query, **one** page, and a
`Blitz` / `wait` / `kill` call. Inspect the target and any Search Console
export first. Use Weft only for evidence the target cannot prove.

Load the `weft` skill before discovery. When `weft_*` tools are missing, use
the `weft` CLI (`search`, `balance`, `fetch --max-cost-usd`) or `weft-setup`.

Read when needed:

- [Ilias kernel](references/ilias-kernel.md) — concentration, GSC, Blitz rules;
- [provider routing](references/provider-routing.md) — live contracts, wallet rail, CLI;
- [report contract](references/report-contract.md) — decision card and ledger;
- [primary sources](references/primary-sources.md) — Google's current docs.

## Outcome Contract

| Field | Contract |
|---|---|
| Goal | Name the money query and page, the Blitz/wait/kill call, and the next honest actions |
| Inputs | Target URL or domain, market, language, GSC export if any, ≤3 commercial seeds, spend cap |
| Output | Decision card, evidence-led findings, prioritized actions, unknowns, spend ledger |
| Acceptance | Every important finding has evidence or an inference label; every action has impact, effort, confidence, and a completion test |
| Limits | No ranking promise, no hidden purchase, no automatic paid retry, no unobserved volume claim, no parallel paid fetches |
| Non-goals | Editing the site, buying links or reviews, publishing content, changing Search Console, storing a provider catalog |

## Required Flow

### 1. Define the decision

Record the business outcome (qualified non-brand traffic, local visits, recovery
from a drop). Record target, market, language, competitors, time range, GSC
access, and spend cap. Missing optional inputs lower confidence; they do not
block a first pass.

If the user set a cap, stop before any fetch that would exceed remaining
**spendable** balance on the merchant's asset.

### 2. Inspect the target first

Observe only what matters: response and redirects, robots, sitemap, canonicals,
titles, headings, copy, internal links, structured data vs visible content,
duplicates. Record URLs, timestamps, and sample size. A blocked page is
unknown, not a pass.

Do not recommend meta keywords. Do not promise indexing or rank.

### 3. Apply the Ilias kernel

Follow [ilias-kernel.md](references/ilias-kernel.md) **before** Weft spend.

Parse GSC `Queries.csv` / `Pages.csv` when supplied. Brand-only means **wait**
on new URLs. Do not Blitz a slogan with zero impressions.

### 4. Name gaps that can change the call

Buy nothing because it exists. Write the decision each purchase must support:

- domain rankings vs GSC (are we missing non-brand queries?);
- demand for **one** user-stated commercial seed (volume, or Trends if no volume contract — label it);
- Google SERP for that seed (can this page win?);
- backlinks only if a **complete** contract exists.

Stop when the call is already `wait` or `kill` and more data cannot change it.

### 5. Discover live, then pay once per contract

Search Weft with the capability, market, language, and required outputs.
Reformulate weak matches. Do not use a remembered vendor name as a URL.

Select the cheapest exact contract per [provider routing](references/provider-routing.md).
`weft_balance` before **each** paid call. Serialise payments. State expected
cost and asset. Tight `max_cost_usd`. One fetch per selected contract. No retry
after pending, timeout, or `INSUFFICIENT_BALANCE`.

Decode the body. Cost is `paid_usd + held_usd`. Keep artifact / tx / protocol.

### 6. Analyze without false precision

For each finding: claim, class (observed / provider / inference), source,
why it matters, severity, confidence, smallest test. No invented SEO score.
Trends is not volume. Two typo keywords are not a content calendar.

### 7. Deliver the report

Follow [report-contract.md](references/report-contract.md). Lead with the
decision card. Then the few actions that change the outcome.

## Completion Gate

Not complete until:

- money query, money page, and Blitz/wait/kill are explicit;
- important facts have sources; inferences are labeled;
- every paid result used a live exact contract;
- every priority has impact, effort, confidence, and a completion test;
- missing evidence stays visible (including “no complete backlink contract”);
- provenance, receipt state, and real spend are reported.

If evidence is thin, return a partial report. Do not fill with generic SEO.

## Safety

- Do not buy or recommend deceptive links, reviews, traffic, or content.
- Do not bypass access controls, robots, or authenticated systems.
- Do not expose private analytics, GSC, customer data, or credentials.
- Do not change a site or third-party account without a separate explicit ask.
