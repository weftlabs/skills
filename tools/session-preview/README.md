# Session previews

Render a real skill run as a chat-style HTML page, then capture that page for
a marketplace listing. `examples/session-previews/` contains reviewed examples.
This is an asset generator, not a live chat client or a dashboard integration.

## Commands

```sh
# Import visible messages into a PRIVATE draft. Never publish a raw import.
python3 tools/session-preview/render.py import /path/to/pi-session.jsonl --output /tmp/draft.json

# Render all reviewed example JSON files and a browsing index.
python3 tools/session-preview/render.py build examples/session-previews --output /tmp/skill-previews

# Export PNG screenshots. Requires Playwright and its Chromium browser.
# PLAYWRIGHT_MODULE may name an existing absolute Playwright module path.
# CHROMIUM_EXECUTABLE may name an existing Chromium executable.
node tools/session-preview/capture.cjs /tmp/skill-previews

python3 -m unittest discover -s tools/session-preview -p 'test_*.py'
```

Open the generated `index.html` to browse; each example has a PNG download.
Screenshots use 1600px width and at least 1000px height, extending for long
results rather than silently clipping them. Capture also checks a 390px view.
The generator uses Python's standard library. Browser export is optional.

## Public example contract

One JSON file per example: `id`, `skill`, `title`, `date`, `mode` (`live` or
`replay`), `prompt`, `intro`, `blocks`, `limits`, `providers`, `provenance`,
and `reviewed: true`. Text is plain text; HTML is always escaped.
Blocks are text, a table (`columns`, `rows`), or an artifact (`name`, `detail`).
Providers have `name`, a local `logo` path, `service`, and `receipts`. Each
receipt supplies decimal-string `paid_usd`, `held_usd`, and `status`.
For a replay these receipts belong to the original retrieval; new spend is zero.
Missing costs stay unknown. Zero paid does not mean free when funds are held.
Do not sum estimates, caps, credits, or provider list prices as paid costs.

`provenance` lists source filenames and SHA-256 hashes. Private absolute paths,
credentials, tool output, reasoning, wallets and receipt identifiers are not
needed in public examples. An import preserves visible message text but is
explicitly unreviewed: choose a task excerpt, remove private details, attach
receipt amounts, and review against the source before creating a public input.
Never relabel a blocked run, synthetic fixture, or unpaid replay as a live run.
The page identifies text as an edited excerpt; it is not a literal Pi screenshot.

## Architecture and acceptance

Pi JSONL → private visible-message draft → reviewed public JSON → escaped HTML
→ browser screenshot. No LLM, account, provider call or network request is made
by import/build/capture. Logos are copied from Weft's existing catalog assets.
The standalone renderer uses the approved Weft palette and chat layout; its
stylesheet is the owner for this new export surface. Font fallback is local.

Acceptance: visible-text-only import; HTML escaping; exact decimal accounting;
unknown versus zero costs; replay labeling; readable desktop/mobile exports;
all sample claims traceable to saved evidence. Tests cover those boundaries.
Private source inventory is retained with the original evaluation artifacts.
Publishing these files does not add them automatically to the dashboard gallery:
that consumer currently loads covers and starter prompts only.
