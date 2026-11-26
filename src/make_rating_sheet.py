import csv
import json
import random
from pathlib import Path

from load_questions import load_questions

# The 10 questions whose explanations will be rated, for every model.
SELECTED = ["Q2", "Q4", "Q5", "Q8", "Q11", "Q14", "Q17", "Q20", "Q23", "Q25"]

questions = {
    q["id"]: q
    for q in load_questions("data/programming_fundamentals.md", "programming_fundamentals")
}

rows = []
for path in sorted(Path("results").glob("*_programming_fundamentals.jsonl")):
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        record = json.loads(line)
        if record["id"] in SELECTED:
            rows.append(record)

# Group by question, then shuffle inside each group so the model order is hidden.
random.seed(42)
ordered = []
for qid in SELECTED:
    group = [r for r in rows if r["id"] == qid]
    random.shuffle(group)
    ordered.extend(group)

sheet_path = Path("results/rating_sheet.csv")
key_path = Path("results/rating_key.csv")

with sheet_path.open("w", newline="", encoding="utf-8-sig") as sheet, \
        key_path.open("w", newline="", encoding="utf-8-sig") as key:
    sheet_writer = csv.writer(sheet)
    key_writer = csv.writer(key)

    sheet_writer.writerow([
        "blind_id", "question_id", "question", "options", "correct_answer",
        "model_response", "correctness_1to5", "clarity_1to5", "notes",
    ])
    key_writer.writerow(["blind_id", "model"])

    for number, record in enumerate(ordered, start=1):
        q = questions[record["id"]]
        options = "\n".join(f"{letter}) {text}" for letter, text in q["options"].items())
        blind_id = f"R{number:02d}"
        sheet_writer.writerow([
            blind_id, record["id"], q["question"], options, q["answer"],
            record["raw_response"], "", "", "",
        ])
        key_writer.writerow([blind_id, record["model"]])

print(f"Wrote {len(ordered)} rows to {sheet_path}")
print(f"Model names are in {key_path}. Don't open that file until you've finished rating.")
