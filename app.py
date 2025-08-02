import streamlit as st
import pdfplumber
import docx
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables 
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# File Readers 
def read_pdf(file):
    with pdfplumber.open(file) as pdf:
        return "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())

def read_docx(file):
    doc = docx.Document(file)
    return "\n".join(paragraph.text for paragraph in doc.paragraphs)

def get_text(file):
    if file.name.endswith(".pdf"):
        return read_pdf(file)
    elif file.name.endswith(".docx"):
        return read_docx(file)
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    else:
        return "Unsupported file type"

#  GPT Summary 
def summarize_diff(text1, text2):
    prompt = f"""Compare the following two documents and summarize the key differences:

Document 1:
{text1[:2000]}

Document 2:
{text2[:2000]}
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# Streamlit App 
st.set_page_config(page_title="📄 Document Difference Summarizer", layout="centered")
st.title("🧠 Document Difference Summarizer")

file1 = st.file_uploader("Upload First Document", type=["txt", "pdf", "docx"])
file2 = st.file_uploader("Upload Second Document", type=["txt", "pdf", "docx"])

if file1 and file2:
    text1 = get_text(file1)
    text2 = get_text(file2)

    if st.button("Summarize Differences"):
        with st.spinner("Analyzing documents with GPT..."):
            summary = summarize_diff(text1, text2)
            st.markdown("### 📝 Summary of Key Differences")
            st.write(summary)
