# Code security audit contract evidence

Inspected 2026-09-16. This skill searches the Weft marketplace at runtime for
a code security or secret scanning provider. No specific provider contract is
pre-committed because the marketplace catalog may change. The agent must run
`weft_search` with relevant query terms and inspect the current results before
any paid fetch.

## Search strategy

Use `weft_search` with one or more of these query patterns:

- `"code security scan"`
- `"secret detection"`
- `"PII scanner"`
- `"credential scanner"`
- `"source code analysis"`

Inspect results for providers that:

1. Accept source code as input (inline text, file content, or base64-encoded
   payload).
2. Return structured findings with location, type, and matched text.
3. Support synchronous response lifecycle.

## Required contract fields

Before calling `weft_fetch`, verify the chosen contract exposes:

| Field | Requirement |
|---|---|
| Method | POST preferred (body carries source code); GET acceptable if input is URL-encoded |
| Input schema | Must include a `source` or `code` field of type string |
| Output schema | Must include a `findings` array with per-finding `type`, `location`, and `matched_text` |
| Price | Decimal string in `access.price.indexed_usd`; use as `max_cost_usd` cap |
| Callability | Must not be `unsupportable` |

## Transport and receipt

Decode the Weft envelope as documented in the core weft skill. The decoded
body root is expected to be:

```json
{
  "findings": [
    {
      "type": "aws_access_key",
      "location": {"line": 12, "column": 8, "end_column": 28},
      "matched_text": "AKIA...",
      "risk": "high",
      "confidence": 0.95
    }
  ],
  "summary": {
    "total_findings": 1,
    "critical": 0,
    "high": 1,
    "medium": 0,
    "low": 0
  }
}
```

This is the expected shape based on common secret scanning API conventions.
The actual provider may differ; the agent must adapt to the real response
schema. Do not hardcode this structure as a requirement. Normalize the output
to the audit report format regardless of the provider's exact field names.

CLI receipt fields: `paidUsd`, `heldUsd`, `paymentStatus`, `txHash`,
`artifactId`, `protocol`. Normalize to paid/held/status only after reading
the actual fields. Missing cost is unknown. Keep payment state independent
from merchant data state.

## Alternatives

If no code security provider is found in the marketplace, the agent must stop
before payment and inform the user. Do not fall back to sending code to a
general-purpose text analysis API or any provider whose contract does not
explicitly handle source code scanning.
