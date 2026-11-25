import re
from collections import Counter
from pathlib import Path


def load_questions(path, area):
    text = Path(path).read_text(encoding="utf-8")
    blocks = re.split(r"(?m)^## ", text)[1:]
    questions = []

    for block in blocks:
        lines = block.strip().splitlines()
        qid, topic, difficulty = [p.strip() for p in lines[0].split("|")]

        options = {}
        answer = None
        question_lines = []

        for line in lines[1:]:
            if line.startswith("Answer:"):
                answer = line.split(":", 1)[1].strip()
            elif re.match(r"^[A-D]\) ", line):
                options[line[0]] = line[3:].strip()
            else:
                question_lines.append(line)

        assert len(options) == 4, f"{qid}: expected 4 options, found {len(options)}"
        assert answer in options, f"{qid}: answer '{answer}' is not one of the options"

        questions.append({
            "id": qid,
            "area": area,
            "topic": topic,
            "difficulty": difficulty,
            "question": "\n".join(question_lines).strip(),
            "options": options,
            "answer": answer,
            "source": "ai_drafted",
        })

    return questions


if __name__ == "__main__":
    qs = load_questions("data/programming_fundamentals.md", "programming_fundamentals")
    print(f"Loaded {len(qs)} questions")
    print(Counter(q["difficulty"] for q in qs))
    print()
    print(qs[3]["question"])
    print(qs[3]["options"])
    print("Answer:", qs[3]["answer"])
