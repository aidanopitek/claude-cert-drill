# Claude Cert Drill Desk

Free, unofficial study site for three Anthropic certification exams:

- **Claude Certified Architect – Professional (CCAR-P)**: scenario guide by official objective, quick-recall notes,
  and 117 practice questions, including assess-each-statement items.
- **Claude Certified Developer – Foundations (CCDV-F)**: cheat sheets and study notes, and 456 practice questions.
- **Claude Certified Associate – Foundations (CCAO-F)**: a cheat sheet on Claude's app features and safe-use rules,
  and 110 practice questions.

Every question shows its answer, an explanation and a link to the relevant Anthropic documentation the moment you
answer. Answer options are shuffled each time, and option lengths are balanced in every bank so the longest option
is not a tell. Scores are kept in your own browser only.

**Open the site:** https://aidanopitek.github.io/claude-cert-drill/

## How the content was checked

All questions and cheat sheets were checked against Anthropic's documentation in October 2026 (platform.claude.com,
code.claude.com, the Claude Help Center, anthropic.com engineering posts, the MCP specification). Outdated items were corrected or
removed, and every question's reference points to Anthropic documentation, except a few general-engineering items
that have none. Model features and limits change often: if something looks wrong, use **Report on GitHub** on the
question card, or open an issue.

## Project layout

```
data/<exam>/exam.json            exam facts, domain weights, banks, tabs
data/<exam>/questions-<bank>.json question banks
data/ccarp/guide.json, recall.json  CCAR-P scenario guide and quick recall
data/<exam>/docs/                cheat sheets (Markdown) and their index, for CCDV-F and CCAO-F
src/index.template.html          the page (HTML, CSS and JavaScript)
scripts/build.py                 builds dist/index.html
scripts/check.py                 validates the banks (run in CI on every pull request)
```

## Quiz modes

- **Practice** (every question, not answered yet, or ones you got wrong): filter by bank and domain.
- **Mock exam**: 63 (CCAR-P), 53 (CCDV-F) or 60 (CCAO-F) questions drawn from all banks in the official domain proportions.

Click an option to select it, then **Submit**. **Back** and **Next** move through the set.

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
