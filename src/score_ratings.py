import csv
import re
from collections import defaultdict


def read_csv(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def letter_in(response):
    match = re.search(r"Answer:\s*\**\s*([A-D])\b", response or "", re.IGNORECASE)
    return match.group(1).upper() if match else None


sheet = read_csv("results/rating_sheet.csv")
key = {row["blind_id"]: row["model"] for row in read_csv("results/rating_key.csv")}

data = defaultdict(lambda: {"correctness": [], "clarity": [], "letter_right": 0, "lucky": 0, "n": 0})
skipped = []

for row in sheet:
    blind_id = row["blind_id"]
    try:
        correctness = float(row["correctness_1to5"])
        clarity = float(row["clarity_1to5"])
    except ValueError:
        skipped.append(blind_id)
        continue

    model = key[blind_id]
    entry = data[model]
    entry["correctness"].append(correctness)
    entry["clarity"].append(clarity)
    entry["n"] += 1

    if letter_in(row["model_response"]) == row["correct_answer"].strip().upper():
        entry["letter_right"] += 1
        if correctness <= 3:
            entry["lucky"] += 1  # right letter, but weak reasoning

print(f"{'Model':<24}{'Rated':>6}{'Avg correct':>13}{'Avg clarity':>13}{'Letter right':>14}{'Right letter, weak reasoning':>30}")
for model, e in sorted(data.items()):
    avg_c = sum(e["correctness"]) / e["n"]
    avg_k = sum(e["clarity"]) / e["n"]
    print(f"{model:<24}{e['n']:>6}{avg_c:>13.2f}{avg_k:>13.2f}{e['letter_right']:>14}{e['lucky']:>30}")

if skipped:
    print(f"\nRows with a missing or non-numeric rating (skipped): {', '.join(skipped)}")
