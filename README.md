# 📖 Literary Lens AI

**Literary Lens AI** is a Streamlit app that uses OpenAI’s GPT to analyze any text — pasted, uploaded, or fetched from a URL — through a chosen philosophical or literary lens.

Whether you're a student, teacher, writer, or just a curious thinker, this app helps you explore texts through frameworks like feminism, postcolonialism, Stoicism, and more.

---

## ✨ Features

* 🔍 **Analyze through 7 lenses**:

  * Feminist Theory
  * Postcolonialism
  * Existentialism
  * Stoicism
  * Marxist Criticism
  * Psychoanalytic Theory
  * Deconstruction

* 📥 **Input text** in 3 ways:

  * Paste it directly
  * Upload `.txt`, `.pdf`, or `.docx` files
  * Provide a URL for web scraping

* 🤖 **AI-powered interpretation** using OpenAI's GPT-3.5

* 📄 **Text preview** before analysis

* 💾 **Download output** as `.txt` or `.md`

---

## 🧠 How It Works

1. Text is split into chunks (\~700 words).
2. Each chunk is analyzed with GPT using a **custom system prompt** tailored to your chosen lens.
3. A final **synthesis step** merges all analyses into one coherent critique.

This process ensures the result is both accurate and stylistically consistent, even for long texts.

---

## 📚 Literary Lenses Explained

| Lens                      | Description                                                                        |
| ------------------------- | ---------------------------------------------------------------------------------- |
| **Feminist Theory**       | Focuses on gender roles, patriarchy, representation of women, and power dynamics.  |
| **Postcolonialism**       | Explores effects of colonialism, identity, cultural domination, and resistance.    |
| **Existentialism**        | Analyzes themes like free will, absurdity, alienation, and the search for meaning. |
| **Stoicism**              | Considers rationality, self-control, virtue, and detachment from external events.  |
| **Marxist Criticism**     | Examines class struggle, economic power, labor, and material conditions.           |
| **Psychoanalytic Theory** | Focuses on unconscious desires, repression, identity, and psychological conflict.  |
| **Deconstruction**        | Questions binary oppositions, hidden assumptions, and unstable meanings in text.   |

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/literary-lens-ai.git
cd literary-lens-ai
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up API key

Create a `.env` file with your [OpenAI API key](https://platform.openai.com/account/api-keys):

```env
OPENAI_API_KEY=your-openai-key
```

---

## 🚀 Usage

```bash
streamlit run app.py
```

The app will open in your browser at [http://localhost:8501](http://localhost:8501).

---

## 📂 Project Structure

```
.
├── app.py               # Streamlit frontend
├── analyzer.py          # GPT-based chunked analysis and synthesis
├── extractors.py        # File/URL text extraction
├── prompts.py           # Literary lens prompts and descriptions
├── requirements.txt     # Python dependencies
└── .env                 # API key (not included in repo)
```

---

## 📦 Dependencies

Core packages:

* `streamlit`
* `openai`
* `tiktoken`
* `pymupdf` (`fitz`) – PDF parsing
* `python-docx` – DOCX parsing
* `beautifulsoup4`, `requests` – Web scraping
* `python-dotenv` – Environment variable loading

Full list in `requirements.txt`.

---

## 🧪 Example Workflow

1. Upload a `.pdf` of *Heart of Darkness*.
2. Choose **Postcolonialism** as the lens.
3. Click **"Analyze Text"**.
4. Review the AI's interpretation and download it.

---

## 🙌 Contributing

Contributions and feedback are welcome! Feel free to:

* Open issues for bugs or ideas
* Submit pull requests for improvements
* Suggest new lenses or prompt enhancements

---

