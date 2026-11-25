import json
from collections import defaultdict
from pathlib import Path


def load_rows(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    return [json.loads(line) for line in lines if line.strip()]


def fmt(correct, total):
    if total == 0:
        return "n/a"
    return f"{correct}/{total} ({100 * correct / total:.0f}%)"


def summarise(rows, key):
    groups = defaultdict(list)
    for row in rows:
        groups[row[key]].append(row)
    return groups


def main():
    files = sorted(Path("results").glob("*.jsonl"))
    if not files:
        print("No results files found in the results folder.")
        return

    for path in files:
        rows = load_rows(path)
        if not rows:
            continue

        model = rows[0]["model"]
        correct = sum(1 for r in rows if r["is_correct"] is True)
        unparsed = sum(1 for r in rows if r["predicted"] is None)

        print("=" * 60)
        print(f"Model: {model}")
        print(f"Overall: {fmt(correct, len(rows))}")
        if unparsed:
            print(f"Answers I could not read: {unparsed} (check raw_response for these)")

        print("\nBy difficulty:")
        by_difficulty = summarise(rows, "difficulty")
        for level in ["easy", "medium", "hard"]:
            group = by_difficulty.get(level, [])
            c = sum(1 for r in group if r["is_correct"] is True)
            print(f"  {level:<7} {fmt(c, len(group))}")

        print("\nBy topic:")
        for topic, group in summarise(rows, "topic").items():
            c = sum(1 for r in group if r["is_correct"] is True)
            print(f"  {topic:<28} {fmt(c, len(group))}")

        wrong = [r for r in rows if r["is_correct"] is not True]
        if wrong:
            print("\nQuestions to look at:")
            for r in wrong:
                print(
                    f"  {r['id']} ({r['topic']}, {r['difficulty']}): "
                    f"model said {r['predicted']}, correct is {r['correct_answer']}"
                )
        else:
            print("\nNo wrong answers.")
        print()


if __name__ == "__main__":
    main()
