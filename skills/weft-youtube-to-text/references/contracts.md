# YouTube transcript contract evidence

## Current discovery, 2026-09-10

- Provider: x402 Atlas.
- Operation: `bazaar-x402-atlas-201`.
- Access: `bazaar-x402-atlas-201-x402`.
- GET `https://youtube.use.x402atlas.com/transcript?v=<encoded-video-id>`.
- Required `v`: string, at most 500 characters, an 11-character ID or full URL.
- Query binding is explicit in `operation.input.source_contract` at
  `properties.input.properties.queryParams`. No body or additional headers.
- Protocol: x402. Indexed price: $0.02/request, observed 2026-09-10.
- Execution: synchronous; do not invent a polling or job endpoint.
- [Inspected catalog contract](https://weft.network/contracts/curated-marketplace/37b1a38ac80cb0aca2c5ba703c97be96cfd44b6e1519d2800a0c1676afb553e6/bazaar-x402-atlas-201.json).

The normalized `operation.output.schema` is null. Callability is `incomplete`,
with reason `response schema (operation probed, not paid)`. The nested source
contract contains a typed output example schema, and the earlier session
provides observed body fields. These are separate kinds of evidence. The live CLI calibration below confirms
one successful request; an advertised example alone does not prove a live run.

## Nested source schema

At `operation.input.source_contract.properties.output.properties.example`:

| Provider body field | Type and meaning |
|---|---|
| `/video_id` | Required string; normalized video ID |
| `/queried_at` | Required date-time string |
| `/text` | Required string; transcript text |
| `/language_code` | Optional string; language actually served |
| `/segments` | Required array; items require integer `start_ms` and string `text`; optional integer `end_ms`, string `start_time_text` |
| `/chapters` | Required array; item properties include integer `start_ms`, integer `end_ms`, string `title`, string `start_time_text` |
| `/available_transcripts` | Required array; item properties include string `language_code`, boolean `selected`, string `type`, string `title` |
| `/note` | Optional string; identifies a canned sample in the documented case |

Only text is necessary for the outcome; do not promise optional metadata from
its presence in an example. Language/track selection is described, but its
request parameters are not in the selected input schema. No active language
selection or paid re-fetch stage is defined by this skill.

## Observed source session

Private source trace: Pi session `01a08087-ec71-76d1-8459-047dc322756a`,
2026-09-08, worker artifact
`188a5b0e-c35f-49ca-8ed8-5389b02c31ee_worker_transcript.jsonl`.

The worker used a $0.02 cap and received HTTP 200. The CLI envelope's
`/data/body` was a JSON string; decoding yielded `/video_id`, `/language_code`,
`/queried_at`, and `/text` strings. This envelope is an observation of that
CLI, not a universal MCP wrapper. Inspect the current transport before
locating the provider body. Segments and chapters were not independently
verified from that result.

At capture, the receipt showed paid $0 and held $0.02 with settlement pending.
That proves delivery with a pending reservation, not a final zero-cost call.
The trial did not establish captionless-video transcription, translation,
episode discovery, voice synthesis, or video generation.

## Legacy CLI recovery

The CLI can return a legacy `data.results[].endpoints[]` envelope without
`contract_url`. The contract URL above is a lookup reference, not permission
to skip live search. Match its operation ID, method, URL and price to live
search before use. Fetch it with a normal authenticated HTTPS GET to
`weft.network`, never `weft fetch` (which is for purchases).

When the existing connection uses `WEFT_API_KEY`, an HTTP client can read the
variable in memory and set `Authorization: Bearer <value>` for this exact Weft
host. Do not print the variable, put it in command arguments, or forward it to
the merchant. Save only the public contract JSON. Refuse redirects so the
credential cannot be forwarded to another host. If only a stored CLI credential
exists, use its documented secure credential mechanism; do not dump its file.

Within the full JSON, the typed schema is at:
`operation.input.source_contract.properties.output.properties.example`.
The query schema is at:
`operation.input.source_contract.properties.input.properties.queryParams`.
These are schemas with `properties`, `type`, and `required`, not merely sample
values. Read them before concluding that the response schema is unknown.

After current discovery and a balance check, the observed CLI request is:

```sh
weft fetch 'https://youtube.use.x402atlas.com/transcript?v=VIDEO_ID' --max-cost-usd 0.02
```

Replace VIDEO_ID with the validated input; the cap must fit current price and
user authorization. Inspect current help before adding method or attribution
flags. GET is the observed default. Save stdout to a private response file,
then decode its provider body and receipt. Never print an entire transcript
just to inspect its shape; report keys, lengths, identity, and receipt status.

## Live CLI calibration, 2026-09-10

A fresh Pi run followed the legacy recovery path, retrieved the authenticated
full contract, matched the nested query and output schemas, and made one GET
with a $0.02 cap. It returned HTTP 200, `application/json`, and UTF-8 body text.
The response identified the requested video, contained 8,010 words and 441
valid segments, and reported language `en`. The saved JSON text matched the
provider text; the text file added only a terminal newline. At receipt capture,
paid was $0.00 and held was $0.02, pending. No paid retry occurred.

This validates request construction and response handling on one video. It
does not verify caption accuracy against the recording or prove all videos,
languages, caption tracks, and hosts work. Source session and raw artifacts
remain in the private test directory; do not publish the raw video transcript
as a skill fixture.
