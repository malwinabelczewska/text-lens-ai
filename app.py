# app/main.py

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Available lenses
LENSES = [
    "feminist theory",
    "postcolonialism",
    "existentialism",
    "Stoicism",
    "Marxist criticism",
    "psychoanalytic theory",
    "deconstruction"
]

def analyze_text(text, lens):
    system_prompt = f"You are a literary critic analyzing texts through the lens of {lens}."
    user_prompt = f"Analyze the following text:\n\n{text}"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    print("\nAvailable lenses:")
    for i, lens in enumerate(LENSES, 1):
        print(f"{i}. {lens}")

    try:
        lens_choice = int(input("\nChoose a lens (1-{}): ".format(len(LENSES))))
        lens = LENSES[lens_choice - 1]
    except (ValueError, IndexError):
        print("Invalid choice. Exiting.")
        exit(1)

    print("\nPaste the text you'd like to analyze. Finish input with an empty line:")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    text = "\n".join(lines)

    print(f"\nAnalyzing through the lens of {lens}...\n")
    result = analyze_text(text, lens)
    print(f"\n--- Analysis ({lens}) ---\n{result}")
