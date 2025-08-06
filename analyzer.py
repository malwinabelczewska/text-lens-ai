from openai import OpenAI
import os
from dotenv import load_dotenv
from tiktoken import encoding_for_model
from prompts import get_system_prompt

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chunk_text(text, max_words=700):
    words = text.split()
    return [" ".join(words[i:i + max_words]) for i in range(0, len(words), max_words)]

def analyze_text(text, lens):
    chunks = chunk_text(text)
    system_prompt = get_system_prompt(lens)

    analyses = []
    for i, chunk in enumerate(chunks, 1):
        print(f"Analyzing chunk {i}/{len(chunks)}...")
        user_prompt = f"Analyze the following chunk of text:\n\n{chunk}"
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        analysis = response.choices[0].message.content.strip()
        analyses.append(analysis)

    combined = "\n\n".join(analyses)
    print("\nSynthesizing final analysis...")

    synthesis_prompt = (
        f"You have just written several partial analyses of a longer text "
        f"through the lens of {lens}. Combine these into a single, cohesive literary analysis. "
        f"Ensure the result reads like one continuous critique and not as disjointed parts.\n\n"
        f"Partial analyses:\n{combined}"
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": synthesis_prompt}
        ]
    )
    return response.choices[0].message.content.strip()
