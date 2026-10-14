# Evaluation & Debugging — Cheat Sheet

## What it is
- Measuring LLM output quality systematically (evaluation) and isolating faults when an app misbehaves (debugging).

## When to use it
- Before shipping prompt/model changes (catch regressions).
- Whenever output quality drops or an integration breaks.

## Key mechanics — evaluation
- **Golden eval dataset**: a fixed set of inputs + expected results; re-run it to catch **regressions** when prompts/models change.
- **Grading methods**:
  - **Exact / assertion-based** — deterministic checks (equality, contains, schema valid). Cheap, precise, best for structured output.
  - **Model-graded** — an LLM judges quality against a rubric. Use for open-ended output; less deterministic.
- **Reproducibility**: pin the model **version**, hold prompt/tools constant, and (on models that still accept it) set **temperature 0** to reduce variance — but results are **not guaranteed identical**. Claude Opus 4.7+ models reject non-default `temperature`/`top_p`/`top_k` with a 400, so omit them there.
- **Test levels**: **unit** (pure logic) → **integration** (your code + the API wired together) → **eval** (output quality on the golden set).

## Key mechanics — debugging
- **Read the trace** — inspect the actual request/response, tool calls, and stop reasons.
- **Isolate the layer**:
  - **Integration-layer bug** (your code): a **400** is usually **yours** — malformed request, bad roles, missing `max_tokens`, wrong schema.
  - **Model-output bug**: request is valid but the content is wrong/low quality → prompt/model/eval problem.

## Common traps
- Shipping prompt/model changes with no golden set → silent regressions.
- Assuming temperature 0 + pinned version gives byte-identical output — it reduces, not eliminates, variance (and newer models reject non-default temperature altogether).
- Using model-graded scoring where a cheap deterministic assertion would do (and vice versa).
- Blaming the model for a **400** — that's almost always a request/integration bug.
- Skipping the trace and guessing at the cause.

---
verified against official Anthropic docs as of 2026-09-09; re-check version-sensitive figures.
