# Model Selection — Cheat Sheet

## What it is
- Choosing the right Claude model for a task as a cost / latency / capability trade-off — not "always pick the biggest."

## Current models (Oct 2026)
- **Fable 5.1** (`claude-fable-5-1`) — demanding reasoning and long-horizon agentic work; highest cost/latency ($10/$50 per MTok).
- **Opus 5.5** (`claude-opus-5-5`) — long-running agentic coding and knowledge work; docs' default starting point ($4/$20).
- **Sonnet 5.5** (`claude-sonnet-5-5`) — best speed/intelligence balance for most production tasks ($2/$10).
- **Haiku 5.5** (`claude-haiku-5-5`) — fastest, cheapest; classification, extraction, routing (from $0.10/$0.50).
- Legacy but still available: Opus 5, Sonnet 5, Fable 5, Opus 4.x, Sonnet 4.6, Haiku 4.5. Mythos 5.1 is also listed in the lineup.

## When to use which
- Simple/high-volume (classification, routing, extraction, short replies) → **Haiku 5.5**.
- Standard production work (chat, summarization, tool use, coding help) → **Sonnet 5.5**.
- Hardest multi-step reasoning where cost/latency are secondary → **Opus 5.5** (or **Fable 5.1** for the most demanding long-horizon work).
- Rule of thumb: start at Sonnet; drop to Haiku if it meets quality cheaper; escalate to Opus only when Sonnet demonstrably falls short.

## Key mechanics
- **Constraints** drive the choice: latency budget, cost per call, context window needs, quality bar.
- **Sampling & non-determinism**:
  - `temperature` (0 ≈ most deterministic; higher = more varied). `top_p` for nucleus sampling — tune one, not both. On Claude Opus 4.7+ (incl. Opus 5.5) any non-default `temperature`/`top_p`/`top_k` returns a 400 error — omit them and steer by prompting.
  - Even at `temperature: 0`, output is **not guaranteed identical** across runs/versions.
- **Pin exact model versions** for reproducibility. Every current model ID (including dateless ones like `claude-sonnet-5-5`) is a pinned snapshot; for pre-4.6 models, aliases are pointers that resolve to a dated ID and can move.
- **Cost levers beyond model choice**: prompt caching, batch/async APIs.
- **Migration** (new model version): run **shadow / canary** traffic + **re-run your eval suite** before switching. Don't swap blind.
- **Tokenizer differences**: newer models/tokenizers may emit **more tokens** for the same text — re-check cost and `max_tokens` after migrating.

## Common traps
- Defaulting to the most powerful model "to be safe" — wastes cost/latency and is penalized on the exam.
- Tuning `temperature` and `top_p` together.
- Assuming `temperature: 0` gives byte-identical results forever.
- Using floating aliases in production and losing reproducibility.
- Migrating models without re-running evals or re-checking token counts/pricing.

---
verified against official Anthropic docs as of 2026-09-09; re-check version-sensitive figures.
