# prompts.py

LENSES = [
    "feminist theory",
    "postcolonialism",
    "existentialism",
    "Stoicism",
    "Marxist criticism",
    "psychoanalytic theory",
    "deconstruction"
]

def get_system_prompt(lens):
    return f"You are a literary critic analyzing texts through the lens of {lens}."
