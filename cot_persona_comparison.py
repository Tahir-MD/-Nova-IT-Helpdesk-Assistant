import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
MODEL = "llama-3.3-70b-versatile"

PROBLEM = (
    "A bat and a ball cost $1.10 in total. "
    "The bat costs $1.00 more than the ball. "
    "How much does the ball cost?"
)

plain_prompt = PROBLEM

cot_persona_prompt = (
    "You are an expert accountant who is extremely careful with numbers "
    "and never skips a step when checking a calculation.\n\n"
    f"{PROBLEM}\n\n"
    "Think step-by-step before answering. Show your reasoning clearly, "
    "then state your final answer on its own line at the end."
)


def ask(prompt):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    if not os.environ.get("GROQ_API_KEY"):
        print("ERROR: GROQ_API_KEY environment variable is not set.")
        raise SystemExit(1)

    print("PROBLEM")
    print(PROBLEM)

    print("\nRUN 1 — PLAIN PROMPT")
    print(ask(plain_prompt))

    print("\nRUN 2 — CHAIN-OF-THOUGHT + PERSONA PROMPT")
    print(ask(cot_persona_prompt))
