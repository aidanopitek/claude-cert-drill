# Claude Cert Drill Desk

Free, unofficial study site for two Anthropic certification exams:

- **Claude Certified Architect – Professional (CCAR-P)**: scenario guide by official objective, quick-recall notes,
  and 112 practice questions.
- **Claude Certified Developer – Foundations (CCDV-F)**: cheat sheets and study notes, and 426 practice questions.

Every question shows its answer, an explanation and a link to the relevant Anthropic documentation the moment you
answer. Answer options are shuffled each time, and option lengths are balanced in every bank so the longest option
is not a tell. Scores are kept in your own browser only.

**Open the site:** https://aidanopitek.github.io/claude-cert-drill/

## How the content was checked

All questions and cheat sheets were checked against Anthropic's documentation in October 2026 (platform.claude.com,
code.claude.com, anthropic.com engineering posts, the MCP specification). Outdated items were corrected or
removed, and every question's reference points to Anthropic documentation, except a few general-engineering items
that have none. Model features and limits change often: if something looks wrong, use **Report on GitHub** on the
question card, or open an issue.

## Project layout

```
data/<exam>/exam.json            exam facts, domain weights, banks, tabs
data/<exam>/questions-<bank>.json question banks
data/ccarp/guide.json, recall.json  CCAR-P scenario guide and quick recall
data/ccdvf/docs/                 CCDV-F cheat sheets (Markdown) and their index
src/index.template.html          the page (HTML, CSS and JavaScript)
scripts/build.py                 builds dist/index.html
scripts/check.py                 validates the banks (run in CI on every pull request)
```

## Build locally

```bash
pip install -r requirements.txt
python scripts/check.py
python scripts/build.py
open dist/index.html
```

Pushes to `main` are checked, built and deployed to GitHub Pages by `.github/workflows/deploy.yml`.

## Question format

Single and multiple choice:

```json
{"id": "BZ-D2-001", "set": "breeganzo", "domain": "Applications and Integration", "type": "single",
 "selectCount": 1, "question": "...", "options": [{"key": "A", "text": "..."}], "correct": ["A"],
 "explanation": "...", "distractorNotes": {"B": "why B is wrong"}, "reference": "https://platform.claude.com/docs/..."}
```

"Assess each statement" questions use `"type": "matrix"` with `choices` and `rows` (`text`, `answer`, `note`).

## Licence

Code and original content: [MIT](LICENSE). Third-party material and its licences: [NOTICE.md](NOTICE.md).
Not affiliated with or endorsed by Anthropic.
