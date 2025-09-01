# 📄 Document Difference Summarizer  

A simple Streamlit app that compares two documents (`.txt`, `.pdf`, `.docx`) and generates a **clean, human-readable summary of differences** using **OpenAI GPT-4o-mini**.  

No messy redlines. No complex diff views. Just clear insights.  

---

## 🚀 Features  
- Upload and compare two documents (`.txt`, `.pdf`, `.docx`)  
- Summarized differences in **natural language**  
- Minimal, distraction-free UI  
- Powered by **OpenAI GPT-4o-mini**  

---

## 🛠️ Tech Stack  
- **Python**  
- **Streamlit** (UI)  
- **pdfplumber** & **python-docx** (file parsing)  
- **OpenAI SDK** (LLM integration)  
- **dotenv** (API key management)  

---

## 📦 Installation  

1. Clone the repo:  
   ```bash
   git clone https://github.com/your-username/document-difference-summarizer.git
   cd document-difference-summarizer
   
2. Create a virtual environment & activate it:
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

3. Install dependencies:
pip install -r requirements.txt

4. Set up your OpenAI API key:
Create a .env file in the project root.
Add the line:
OPENAI_API_KEY=your_api_key_here

▶️ Usage
Run the Streamlit app:
streamlit run app.py
Open your browser at http://localhost:8501 and start comparing!

📈 Example
Upload two drafts of a document.
Get a concise summary of additions, removals, and wording changes.

📜 License
This project is licensed under the MIT License.
