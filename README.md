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
   
2. Create a virtual environment & activate it:<br>
python -m venv venv <br>
source venv/bin/activate   # macOS/Linux <br>
venv\Scripts\activate      # Windows <br>

3. Install dependencies: <br>
pip install -r requirements.txt <br>

4. Set up your OpenAI API key: <br>
Create a .env file in the project root. <br>
Add the line:<br> 
OPENAI_API_KEY=your_api_key_here<br>

▶️ Usage <br>
Run the Streamlit app:<br>
streamlit run app.py<br>
Open your browser at http://localhost:8501 and start comparing!<br>

📈 Example<br>
Upload two drafts of a document.<br>
Get a concise summary of additions, removals, and wording changes.<br>

📜 License<br>
This project is licensed under the MIT License.
