import streamlit as st
import os
from dotenv import load_dotenv
from analyzer import analyze_text
from extractors import extract_text_from_file, extract_text_from_url
from prompts import LENSES, LENS_DESCRIPTIONS

load_dotenv()

st.set_page_config(page_title="Literary Lens AI", layout="wide")

with st.sidebar:
    st.header("📖 About Literary Lenses")
    st.markdown("Choose a lens from the dropdown to see its description below.")

    if "lens" in locals():
        st.markdown(f"### {lens.title()}")
        st.write(LENS_DESCRIPTIONS.get(lens, "No description available."))

st.title("🔍 Literary Lens AI")
st.markdown("Analyze any text using a literary or philosophical lens powered by AI.")

lens = st.selectbox("Choose your lens of analysis:", LENSES)

input_method = st.radio("How would you like to input your text?", ["Paste text", "Upload file", "Enter URL"])

text = ""

if input_method == "Paste text":
    text = st.text_area("Paste your text here:", height=300)

elif input_method == "Upload file":
    uploaded_file = st.file_uploader("Upload a .txt, .pdf, or .docx file", type=["txt", "pdf", "docx"])
    if uploaded_file is not None:
        with open(f"temp_{uploaded_file.name}", "wb") as f:
            f.write(uploaded_file.read())
        text = extract_text_from_file(f.name)
        os.remove(f.name)

elif input_method == "Enter URL":
    url = st.text_input("Enter the URL to fetch text from:")
    if url:
        try:
            text = extract_text_from_url(url)
        except Exception as e:
            st.error(str(e))

if text:
    st.subheader("Preview of input text:")
    st.text(text[:1000] + ("..." if len(text) > 1000 else ""))

    if st.button("Analyze Text"):
        with st.spinner("Analyzing... This may take a moment."):
            result = analyze_text(text, lens)
        st.subheader(f"Analysis ({lens}):")
        st.write(result)

        filename = f"{lens.replace(' ', '_')}_analysis.txt"
        st.download_button(
            label="📥 Download Analysis as .txt",
            data=result,
            file_name=filename,
            mime="text/plain",
        )

        markdown_result = f"# Analysis: {lens}\n\n{result}"
        st.download_button(
            label="📥 Download Analysis as .md",
            data=markdown_result,
            file_name=f"{lens.replace(' ', '_')}_analysis.md",
            mime="text/markdown"
        )
