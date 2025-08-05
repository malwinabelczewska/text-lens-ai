import os
import fitz
import docx
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from openai import OpenAI
from tiktoken import encoding_for_model

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
    chunks = chunk_text(text)
    system_prompt = (
        f"You are a literary critic analyzing texts through the lens of {lens}."
    )

    analyses = []

    for i, chunk in enumerate(chunks, 1):
        print(f"Analyzing chunk {i}/{len(chunks)}...")
        user_prompt = f"Analyze the following chunk of text:\n\n{chunk}"

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
        analysis = response.choices[0].message.content.strip()
        analyses.append(f"--- Analysis of chunk {i} ---\n{analysis}\n")

    # Combine all analyses into a single result
    combined_analysis = "\n".join(analyses)
    return combined_analysis


def extract_text_from_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    elif ext == ".pdf":
        doc = fitz.open(file_path)
        text = "\n".join(page.get_text() for page in doc)
        doc.close()
        return text
    elif ext == ".docx":
        doc = docx.Document(file_path)
        return "\n".join(p.text for p in doc.paragraphs)
    else:
        raise ValueError("Unsupported file format")

def extract_text_from_url(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        return soup.get_text(separator="\n", strip=True)
    except Exception as e:
        raise ValueError(f"Error fetching URL: {e}")

def get_user_input_text():
    print("\nHow would you like to input your text?")
    print("1. Paste text")
    print("2. Upload file (.txt, .pdf, .docx)")
    print("3. Enter URL")
    choice = input("Choose option (1/2/3): ").strip()

    if choice == "1":
        print("\nPaste the text you'd like to analyze. Finish input with an empty line:")
        lines = []
        while True:
            line = input()
            if line.strip() == "":
                break
            lines.append(line)
        return "\n".join(lines)

    elif choice == "2":
        file_path = input("\nEnter the full path to your file: ").strip()
        if not os.path.exists(file_path):
            print("File not found.")
            exit(1)
        return extract_text_from_file(file_path)

    elif choice == "3":
        url = input("\nEnter the URL: ").strip()
        return extract_text_from_url(url)

    else:
        print("Invalid choice. Exiting.")
        exit(1)

def chunk_text(text, max_words=700):
    words = text.split()
    chunks = []

    for i in range(0, len(words), max_words):
        chunk = " ".join(words[i:i + max_words])
        chunks.append(chunk)

    return chunks

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

    text = get_user_input_text()

    print(f"\nAnalyzing through the lens of {lens}...\n")
    result = analyze_text(text, lens)
    print(f"\n--- Analysis ({lens}) ---\n{result}")
