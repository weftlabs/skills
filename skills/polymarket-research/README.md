# Polymarket Research

Create a cited, timestamped decision brief from a Polymarket link. The skill
separates settlement rules, live market state, outside evidence, and inference.
It is read-only and never places a trade.

## Install

```sh
npx skills add weft-labs/skills --skill polymarket-research
```

## Reproduce the benchmark

This is a development instruction-following pilot on three synthetic offline
dossiers: a conflicted current market, a historical cutoff, and an unresolved
market identity. It does not measure live research quality, source freshness,
probability calibration, forecast accuracy, trading performance, financial
returns, or paid-provider execution. The cases and scorer informed development,
so this evidence does not estimate skill efficacy.

From the repository root:

```sh
python3 scripts/benchmark.py run --manifest skills/polymarket-research/benchmarks/manifest.json --target codex:gpt-5.6-sol --out benchmark-results/polymarket-research
```

The cases and scorer informed development. This measured run started after the
scorer version was frozen, but the tasks remain a development regression suite
rather than a held-out test set.

<!-- weft-benchmark:start -->
## Benchmark

**Claim scope:** Development pilot that measures whether the model follows the committed Polymarket Research procedure on three synthetic offline dossiers: a current conflicted market, a historical-cutoff request, and an unresolved market identity. It does not estimate skill efficacy or measure live web or API research, source freshness, probability calibration, forecast accuracy, trading performance, profitability, or paid-provider execution.

**Evidence class: Development pilot.** These tasks were used while the skill and scorer were developed. They are regression evidence, not held-out efficacy evidence.

The same clean-room tasks run without the skill and with the skill. Repeated generations are nested within each task; they do not increase the number of independent tasks. Results are descriptive paired observations. Headline metrics are maintainer-recorded harness process time, all committed checks passed, and total agent tokens.

The evidence writer redacts host paths, clean-room temporary paths, and opaque harness trace IDs from published native transcripts. Answers and token telemetry remain inspectable.

![Benchmark chart](benchmarks/chart.svg)

| Harness / model | Arm | Harness process time, median | All committed checks passed | Tokens, median | Complete / excluded pairs |
|---|---|---:|---:|---:|---:|
| Codex / `gpt-5.6-sol` | without weft | 24.315s | 66.7% | 19150 | 9 / 0 |
| Codex / `gpt-5.6-sol` | with weft | 25.795s | 66.7% | 36605 | 9 / 0 |
| Codex / `gpt-5.6-sol` | Paired case-level difference | +14.02s | +0 pp | +18957 | — |

**Separately calculated native token-field medians:**
- Codex / `gpt-5.6-sol` / without weft: input 17972 (cached input 8320), output 826 (reasoning output 195), cache write input 0.
- Codex / `gpt-5.6-sol` / with weft: input 35578 (cached input 19712), output 1072 (reasoning output 309), cache write input 0.
These category medians are supporting telemetry. They can come from different runs, and overlapping native fields such as cached input are not additive.

Case-level analysis units: 3 unique cases. Actual repetitions per case: 3. Required complete pairs per target and case: 3. Excluded matched pairs: 0.
The reported time and token differences are the medians of the per-case paired differences. The accomplishment difference is the mean of the per-case rate differences.
Measured: 2026-09-05T19:56:54Z. Skill digest: `9116abb6a401f568d4299b1255dc08e58ec049274e35a67d67f224aa594d683e`. Manifest digest: `7c5ceb1a274f4c50e08301acfadc68940c11c22d251bd9e3a956890fcd391f35`.
[Raw benchmark evidence](benchmarks/results/2026-09-05-codex-gpt56sol-development-v2/raw.json)
<!-- weft-benchmark:end -->
