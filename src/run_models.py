import argparse
import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

from load_questions import load_questions

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    sys.exit("GROQ_API_KEY not found. Check that your .env file is in the repo's top folder.")

client = Groq(api_key=API_KEY)

SYSTEM_PROMPT = (
    "You are a tutor helping undergraduate computer science students at a "
    "Nigerian university. Answer the multiple-choice question."
)

FORMAT_INSTRUCTIONS = (
    "Reply in exactly this format:\n"
    "Answer: <one letter: A, B, C or D>\n"
    "Explanation: <a short explanation a student could learn from>"
)


def build_prompt(q):
    options = "\n".join(f"{letter}) {text}" for letter, text in q["options"].items())
    return f"{q['question']}\n{options}\n\n{FORMAT_INSTRUCTIONS}"


def parse_letter(text):
    match = re.search(r"Answer:\s*\**\s*([A-D])\b", text or "", re.IGNORECASE)
    return match.group(1).upper() if match else None


def ask(model, prompt, retries=3):
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt},
                ],
                temperature=0,
                max_completion_tokens=2000,
            )
            return response.choices[0].message.content or ""
        except Exception as error:
            wait = 10 * (attempt + 1)
            print(f"  error: {error}. Waiting {wait}s, then retrying...")
            time.sleep(wait)
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True, help="Groq model name")
    parser.add_argument("--limit", type=int, default=None, help="only run the first N questions")
    parser.add_argument("--pause", type=float, default=2.0, help="seconds to wait between calls")
    args = parser.parse_args()

    questions = load_questions("data/programming_fundamentals.md", "programming_fundamentals")
    if args.limit:
        questions = questions[: args.limit]

    Path("results").mkdir(exist_ok=True)
    out_path = Path("results") / f"{args.model.replace('/', '_')}_programming_fundamentals.jsonl"

    done = set()
    if out_path.exists():
        for line in out_path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                done.add(json.loads(line)["id"])

    with out_path.open("a", encoding="utf-8") as f:
        for q in questions:
            if q["id"] in done:
                print(f"{q['id']}: already done, skipping")
                continue

            raw = ask(args.model, build_prompt(q))
            predicted = parse_letter(raw) if raw is not None else None

            record = {
                "id": q["id"],
                "area": q["area"],
                "topic": q["topic"],
                "difficulty": q["difficulty"],
                "source": q["source"],
                "model": args.model,
                "run_date": datetime.now().isoformat(timespec="seconds"),
                "correct_answer": q["answer"],
                "predicted": predicted,
                "is_correct": (predicted == q["answer"]) if predicted else None,
                "raw_response": raw,
            }
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
            f.flush()

            print(f"{q['id']}: model said {predicted}, correct is {q['answer']}")
            time.sleep(args.pause)

    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()
