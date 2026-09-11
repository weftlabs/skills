# Weft Skills

Canonical agent skills for [Weft](https://weft.network) — search the agent
web and pay any x402/MPP endpoint from a wallet the user controls.

**This repo is the single source of truth.** Every other place a Weft
skill appears — `weft.network`, the Claude plugin, the `@weftlabs/cli`
npm package — is a byte-identical mirror pinned to one commit of this repo
by a `SKILLS_REF` file and enforced by that consumer's CI drift check.
Never edit a mirror. To change a skill: PR this repo, merge, then bump
each consumer's `SKILLS_REF` and re-vendor.

## Skills

| Skill | Job | Lifecycle |
|---|---|---|
| [`weft`](skills/weft/SKILL.md) | Find and buy paid data, APIs, and real-world actions: the search → choose → fetch loop, receipts, spending safety. [`rules/cli.md`](skills/weft/rules/cli.md) adds the machine-local CLI surface. | Installed; persists on the host |
| [`weft-setup`](skills/weft-setup/SKILL.md) | Connect a user's Weft Account from any surface: plugin, MCP config ([per-host shapes](skills/weft-setup/rules/hosts.md)), connector UI, or bootstrap a new account. | One-shot; fetched, executed, discarded |
| [`weft-flights-search`](skills/weft-flights-search/SKILL.md) | Experimental Weft-powered flight research with route, schedule, fare, nearby-airport, and ground-transfer evidence. | Experimental outcome workflow |
| [`weft-gtm-lead-enrichment`](skills/weft-gtm-lead-enrichment/SKILL.md) | Enrich a LinkedIn profile, find or verify a work email, or retrieve a social newsfeed through OneShot Agent. | Optional workflow; experimental |
| [`weft-linkedin-commenter-discovery`](skills/weft-linkedin-commenter-discovery/SKILL.md) | Find relevant leads among a LinkedIn post's comments, with profile links and comment evidence. | Experimental candidate; live validation pending |
| [`weft-linkedin-post-sentiment`](skills/weft-linkedin-post-sentiment/SKILL.md) | Analyze sentiment, recurring themes, and uncertainty in comments on one LinkedIn post. | Experimental candidate; live validation pending |
| [`weft-youtube-to-text`](skills/weft-youtube-to-text/SKILL.md) | Extract a supplied YouTube video's transcript into reusable text and timestamped JSON. | Experimental workflow; one live Pi test |
| [`weft-transcript-to-podcast`](skills/weft-transcript-to-podcast/SKILL.md) | Summarize a saved transcript and generate a short MP3 through Weft and BlockRun. | Experimental workflow; one live Pi test |
| [`weft-company-financial-snapshot`](skills/weft-company-financial-snapshot/SKILL.md) | Summarize one company’s reported financial facts with periods, units and filing evidence. | Experimental workflow; live test and saved-data replay |
| [`weft-sec-filings-brief`](skills/weft-sec-filings-brief/SKILL.md) | Brief one company’s SEC filings with dated links, verified summaries and coverage limits. | Experimental workflow; live Massive test with SEC source checks |
| [`weft-iban-bank-lookup`](skills/weft-iban-bank-lookup/SKILL.md) | Identify the bank and country behind a supplied IBAN, with validity and account-verification limits. | Experimental workflow; two live Pi examples |
| [`weft-stock-news-sentiment`](skills/weft-stock-news-sentiment/SKILL.md) | Summarize bounded ticker news with dated sources and sentiment evidence. | Experimental; one live Pi trial |
| [`weft-watchlist-technical-screen`](skills/weft-watchlist-technical-screen/SKILL.md) | Screen a supplied watchlist with dated RSI and MACD values. | Experimental; one live Pi trial |
| [`weft-local-business-leads`](skills/weft-local-business-leads/SKILL.md) | Build a bounded local business prospect list with location and contact evidence. | Experimental workflow; guided Pi test completed |
| [`weft-hiring-signals`](skills/weft-hiring-signals/SKILL.md) | Find relevant job postings and group hiring evidence by company for GTM research. | Experimental workflow; guided Pi test completed |
| [`weft-customer-review-analysis`](skills/weft-customer-review-analysis/SKILL.md) | Analyze review evidence into sourced customer themes and explicit sample limits. | Experimental workflow; guided Pi test completed |
| [`weft-competitor-pricing`](skills/weft-competitor-pricing/SKILL.md) | Compare supplied competitor pricing pages with billing units and missing-data limits. | Experimental workflow; guided Pi test completed |
| [`weft-company-registration-check`](skills/weft-company-registration-check/SKILL.md) | Check a Belgian company’s registered identity and status before account enrichment. | Experimental workflow; guided Pi test completed |

## Install and update

Install every Weft skill, then choose which agents to use:

```sh
npx skills add weftlabs/skills --skill '*'
```

Run this from your project directory for a project install. Add `--global` to
make the skills available across projects. Keep the quotes around `'*'` so the
shell does not expand it into filenames. For an unattended install to **all
supported agents**, use `npx skills add weftlabs/skills --all`.

Update installed skills:

```sh
npx skills update
```

The updater asks which scope to update. Use `npx skills update --global` for
global installs or `npx skills update --project` for the current project. This
updates installed skills from all sources, not only Weft. To refresh only Weft
or include newly added Weft skills, rerun the all-Weft install command above
with the same scope and agent selection.

The commands follow the [Skills CLI documentation](https://github.com/vercel-labs/skills#readme).

### Install selected skills

Install only the core skills:

```sh
npx skills add weftlabs/skills --skill weft --skill weft-setup
```

Install an optional workflow separately:

```sh
npx skills add weftlabs/skills --skill weft-flights-search
npx skills add weftlabs/skills --skill weft-gtm-lead-enrichment
npx skills add weftlabs/skills --skill weft-linkedin-commenter-discovery
npx skills add weftlabs/skills --skill weft-linkedin-post-sentiment
npx skills add weftlabs/skills --skill weft-youtube-to-text
npx skills add weftlabs/skills --skill weft-transcript-to-podcast
npx skills add weftlabs/skills --skill weft-company-financial-snapshot
npx skills add weftlabs/skills --skill weft-sec-filings-brief
npx skills add weftlabs/skills --skill weft-iban-bank-lookup
npx skills add weftlabs/skills --skill weft-stock-news-sentiment
npx skills add weftlabs/skills --skill weft-watchlist-technical-screen
npx skills add weftlabs/skills --skill weft-local-business-leads
npx skills add weftlabs/skills --skill weft-hiring-signals
npx skills add weftlabs/skills --skill weft-customer-review-analysis
npx skills add weftlabs/skills --skill weft-competitor-pricing
npx skills add weftlabs/skills --skill weft-company-registration-check
```

Use the space-separated `--skill <name>` form. Do not use
`--skill=<name>`; affected Skills CLI versions can ignore that filter and
install every skill in the repository.

### GTM research workflows

Start with local business leads or hiring signals to find candidate accounts.
Use review analysis and competitor pricing to prepare a sourced research brief.
The company registration check resolves a supplied Belgian enterprise number;
it does not verify creditworthiness or VAT validity. Combine these records with
lead enrichment when named business contacts are needed. These workflows do not
send outreach or write to a CRM.

### Screenshots of real runs

[Session previews](examples/session-previews/README.md) show a task, its result,
the API providers used, and recorded paid/held amounts. They use existing Pi
evidence, with edited excerpts clearly labeled. Use the
[preview generator](tools/session-preview/README.md) to import a Pi session,
review its public excerpt, and export HTML plus PNG screenshots.

Each optional workflow also owns a `1600x900` `cover.webp` beside its
`SKILL.md`. The public repository contains the finished cover, not Weft's
internal mascot source or generation workflow. Core skills do not appear in the
gallery and do not need a cover.

Each optional workflow also declares a concise `metadata.category` in its
`SKILL.md` frontmatter. The gallery reads this value directly and creates its
filters from the categories that are present. Current categories are
`Sales & GTM`, `Finance`, `Travel`, and `Content`. Reuse an existing label when
it describes the outcome; add a new label only when the workflow does not fit.

Each skill also includes a `512x512` PNG named `logo.png` beside its
`SKILL.md` for square directory listings, including agency.io. Use this image
for the listing logo and `cover.webp` for a wide workflow gallery card.

| Skill | Square logo |
|---|---|
| Weft | [logo.png](skills/weft/logo.png) |
| Setup | [logo.png](skills/weft-setup/logo.png) |
| Flight search | [logo.png](skills/weft-flights-search/logo.png) |
| Lead enrichment | [logo.png](skills/weft-gtm-lead-enrichment/logo.png) |
| Commenter discovery | [logo.png](skills/weft-linkedin-commenter-discovery/logo.png) |
| Post sentiment | [logo.png](skills/weft-linkedin-post-sentiment/logo.png) |
| YouTube to text | [logo.png](skills/weft-youtube-to-text/logo.png) |
| Transcript to podcast | [logo.png](skills/weft-transcript-to-podcast/logo.png) |
| Local business leads | [logo.png](skills/weft-local-business-leads/logo.png) |
| Hiring signals | [logo.png](skills/weft-hiring-signals/logo.png) |
| Customer review analysis | [logo.png](skills/weft-customer-review-analysis/logo.png) |
| Competitor pricing | [logo.png](skills/weft-competitor-pricing/logo.png) |
| Company registration check | [logo.png](skills/weft-company-registration-check/logo.png) |

Or point an agent at the hosted copies:

- Setup (start here): `https://weft.network/setup.md`
- Usage: `https://weft.network/skills/weft/SKILL.md`

## Distribution

| Mirror | Mechanism |
|---|---|
| `weft.network/setup.md` + `/skills/weft/SKILL.md` | vendored into `weft-app` at its `SKILLS_REF` commit, drift-checked in its CI |
| Claude plugin `weftlabs/weft-claude-plugin` | vendors `skills/weft/` at its `SKILLS_REF` commit, drift-checked in its CI |
| `@weftlabs/cli` npm package | bundles `skills/weft/` at its `SKILLS_REF` commit, drift-checked in its CI |

## License

MIT
