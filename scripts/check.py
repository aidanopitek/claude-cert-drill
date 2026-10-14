"""Validate the question banks. Exits non-zero on structural errors; prints a length-balance report.

Usage: python scripts/check.py [--strict-balance]
"""
import collections
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = json.loads((ROOT / "site.json").read_text())
errors, report = [], []
ALLOWED_REF = re.compile(r"^https://(platform\.claude\.com/docs|code\.claude\.com/docs|www\.anthropic\.com/|trust\.anthropic\.com|"
                         r"privacy\.claude\.com|modelcontextprotocol\.io|gdpr-info\.eu|eur-lex\.europa\.eu|digital-strategy\.ec\.europa\.eu)")

for exam in SITE["exams"]:
    d = ROOT / "data" / exam
    cert = json.loads((d / "exam.json").read_text())
    weights = cert["weights"]
    ids = set()
    for bank, _ in cert["banks"]:
        if not bank:
            continue
        f = d / f"questions-{bank}.json"
        if not f.exists():
            errors.append(f"{exam}: bank '{bank}' listed in exam.json but {f.name} is missing")
            continue
        qs = json.loads(f.read_text())
        ranks = collections.Counter()
        for q in qs:
            where = f"{exam}/{bank}/{q.get('id')}"
            if q["id"] in ids:
                errors.append(f"{where}: duplicate id")
            ids.add(q["id"])
            if q.get("set") != bank:
                errors.append(f"{where}: set is '{q.get('set')}', expected '{bank}'")
            if q["domain"] not in weights:
                errors.append(f"{where}: unknown domain '{q['domain']}'")
            ref = q.get("reference") or ""
            if ref and not ALLOWED_REF.match(ref):
                errors.append(f"{where}: reference is not Anthropic documentation: {ref}")
            if q.get("type") == "matrix":
                if not q.get("rows") or len(q.get("choices", [])) < 2:
                    errors.append(f"{where}: matrix needs rows and at least two choices")
                for r in q.get("rows", []):
                    if r["answer"] not in q["choices"]:
                        errors.append(f"{where}: row answer '{r['answer']}' is not one of the choices")
                continue
            keys = [o["key"] for o in q["options"]]
            if len(set(keys)) != len(keys):
                errors.append(f"{where}: duplicate option keys")
            if not q["correct"] or not set(q["correct"]) <= set(keys):
                errors.append(f"{where}: correct keys {q['correct']} not all in options {keys}")
            if q.get("selectCount", 1) != len(q["correct"]):
                errors.append(f"{where}: selectCount {q.get('selectCount')} != number of correct answers")
            if set(q.get("distractorNotes") or {}) & set(q["correct"]):
                errors.append(f"{where}: distractorNotes contains a correct key")
            if len(q["correct"]) == 1:
                order = [o["key"] for o in sorted(q["options"], key=lambda o: -len(o["text"]))]
                ranks[order.index(q["correct"][0]) + 1] += 1
        n = sum(ranks.values())
        if n:
            longest = ranks[1] / n
            report.append(f"{exam}/{bank}: {len(qs)} questions; correct option is the longest in {ranks[1]}/{n} "
                          f"single-answer items ({longest:.0%}; about 25% is chance)")
            if "--strict-balance" in sys.argv and longest > 0.35:
                errors.append(f"{exam}/{bank}: correct option is the longest in {longest:.0%} of items")

print("\n".join(report))
if errors:
    print(f"\n{len(errors)} problem(s):\n  " + "\n  ".join(errors))
    sys.exit(1)
print("\nAll checks passed.")
