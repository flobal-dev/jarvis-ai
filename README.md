# Jarvis AI 🧠

Local AI assistant powered by Retrieval-Augmented Generation (RAG) to query and understand personal documents.

---

## 🚀 Features

- 📄 Chat with your own PDF documents  
- 🧠 Retrieval-Augmented Generation (RAG)  
- 🤖 Fully local LLM using **Mistral (via Ollama)**  
- 🔒 Runs completely offline (no API keys required)  
- ⚡ Semantic search using embeddings  

---

## 🧱 Tech Stack

- Python  
- LlamaIndex  
- Ollama (Mistral)  
- FAISS (vector database)  
- HuggingFace embeddings  
- PyMuPDF (robust PDF parsing)  

---

## 📂 Project Structure

jarvis-ai/
│
├── src/
│   ├── ingestion.py
│   ├── rag.py
│   └── main.py
│
├── data/             # your PDFs (not tracked by git)
├── README.md
├── requirements.txt
└── .gitignore
---

## ⚙️ Setup

### 1. Clone repository
git clone https://github.com/flobal-dev/jarvis-ai.git
cd jarvis-ai
---

### 2. Create virtual environment
python -m venv venv
venv\Scripts\activate
---

### 3. Install dependencies
pip install llama-index
pip install llama-index-llms-ollama
pip install llama-index-embeddings-huggingface
pip install llama-index-readers-file
pip install pymupdf pypdf faiss-cpu python-dotenv
---

### 4. Install Ollama

Download and install:

👉 https://ollama.com

Run:
ollama run mistral
---

## 📄 Add your documents

Create a folder:
/data
Add your PDF files there.

---

## ▶️ Run the project
python src/main.py
---

## 💬 Example
Du: Erkläre die wichtigsten Inhalte
Jarvis:

-Machine Learning beschreibt, wie Systeme aus Daten lernen
-Neural Networks bestehen aus mehreren Schichten von Neuronen
-Data Science umfasst Datenanalyse und Interpretation
---

## 🧠 How it works

1. PDFs are parsed using PyMuPDF  
2. Text is split into chunks  
3. Embeddings are generated  
4. Relevant chunks are retrieved  
5. Local LLM (Mistral) generates the answer  

---

## 🚀 Future Improvements

- 🎤 Voice interface ("Hey Jarvis")  
- ⚡ Faster retrieval (persisted index)  
- 🧠 Memory support  
- 🌐 Web UI (Streamlit)  
- 🍓 Raspberry Pi integration  

---

## 👨‍💻 Author

Florian Balzer