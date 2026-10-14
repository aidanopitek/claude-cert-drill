# Claude Code — Cheat Sheet

## What it is
- Anthropic's agentic coding tool that operates in your terminal/repo, with several distinct configuration and extension mechanisms.

## When to use it
- Coding tasks in a real codebase; automating dev workflows; scripting Claude into CI or pipelines (headless).

## Key mechanics — the primitives (know the differences)
- **CLAUDE.md** — project/user memory that is **auto-loaded** into context. **Hierarchical**: higher-level files combine with more specific ones.
- **Rules** — persistent constraints/guidance applied to the agent's work.
- **Skills** — packaged capabilities that Claude can load automatically when relevant (**model-invoked**) and that you can also invoke with `/name`; `disable-model-invocation: true` makes one user-only.
- **Commands** — **user-invoked** slash-command shortcuts; custom commands (`.claude/commands/`) have been merged into skills and work the same way.
- **Agents (subagents)** — delegate work to a separate agent with **isolated context**; the result returns to the main session.
- **Hooks** — **deterministic** handlers (shell commands, HTTP, MCP tool calls; also prompt/agent-based ones that use a model) configured in `settings.json` (or skills/plugins), fired at defined lifecycle events (not model-decided).

## Headless / automation
- Run non-interactively with `-p` (print mode).
- **Signals via exit code**: success/failure is reported through the process **exit code** — check it in scripts/CI.

## Permissions
- **Least privilege**: grant only the tools/paths/commands needed; don't blanket-allow.

## Common traps
- Confusing **model-invoked** (Skills by default) with **user-invoked** (slash commands), or **deterministic** (Hooks) with model-decided behavior.
- Forgetting CLAUDE.md is auto-loaded and hierarchical — stray instructions high up affect everything.
- Not checking the headless exit code and assuming success.
- Running with broad permissions instead of scoping them.
- Expecting subagents to share the parent's full context — they are isolated.

---
verified against official Anthropic docs as of 2026-09-09; re-check version-sensitive figures.
