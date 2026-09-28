# Evaluation — 2026-09-16

One fresh Pi CLI session exercised the candidate and core Weft skill with
explicit skill loading. This is a shared-account live smoke test, not a paired
benchmark or an automatic-trigger test.

## Provider

Strale secret scan (`strale-secret-scan`) via `https://api.strale.io/x402/v2/secret-scan`.
Provider: Strale (strale.dev). Observed price: USD 0.0216 per request.
Protocol: x402 on Base mainnet. The live fetch returned HTTP 200 with
structured findings.

## Test input

```javascript
const config = {
AWS_ACCESS_KEY_ID = 'AKIAIOSFODNN7EXAMPLE',
DATABASE_URL = 'postgres://admin:password123@db.example.com:5432/myapp',
ADMIN_EMAIL = 'admin@company.com',
SLACK_WEBHOOK = 'https://example.com/slack-webhook/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX'
};
```

6 lines submitted. The test included an AWS access key, a database connection
string with embedded credentials, an email address, and a Slack webhook URL.

## Findings

The provider returned 2 findings out of 4 embedded secrets/PII:

| # | Type | Line | Severity | Masked Value |
|---|---|---|---|---|
| 1 | aws_access_key | 2 | critical | AKIA...MPLE |
| 2 | database_url | 3 | critical | post...yapp |

Summary: 2 critical, 0 high, 0 medium. Lines scanned: 6. Clean: false.

The Slack webhook URL and email address were not detected. This may indicate
the provider focuses on cloud credentials and connection strings rather than
all secret types or PII. This is a coverage limitation, not a false negative
for the provider's documented scope.

## Receipt

| Field | Value |
|---|---|
| paid_usd | $0.00 |
| held_usd | $0.0216 |
| payment_status | pending |
| tx_hash | 0x4f902fd34e14790be73a65132896abd646de2cbdf8a90545fafdfe2e652732e7 |
| protocol | x402 |
| artifact_id | 1718 |

Settlement was pending at capture. The receipt cost is paid + held = $0.0216
total committed.

## Observations

- Latency: 7ms (provider-side).
- The provider accepts a `text` query parameter via GET. The input schema is
  simple: `{text: string}`. No authentication or API key is required beyond
  the x402 micropayment.
- The response schema is `{findings: [...], total_findings, clean,
  severity_summary, lines_scanned, _meta}`.
- Each finding includes `type`, `line_number`, `masked_value`, `severity`,
  and `pattern_matched`.
- The provider uses `masked_value` rather than the full matched text, which
  is appropriate for a security scanning service.
- This was the only code security provider found in the marketplace search.
  Broader searches (e.g., "PII scanner", "credential detection") should be
  tested to discover additional providers.

## Pending validation

- Broader provider discovery with alternative search queries.
- PII detection scope (the current test's email was not flagged).
- Multi-file or repository-level scanning workflows.
- Redacted output generation from provider findings.
- Session preview JSON creation with real data.
