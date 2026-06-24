# 🧠 Jarvis AI

> Local AI assistant powered by Retrieval-Augmented Generation (RAG)  
> Query and understand your personal documents — fully offline.

---

## ✨ Features

- 📄 Chat with your own PDF documents  
- 🧠 Retrieval-Augmented Generation (RAG)  
- 🤖 Fully local LLM (Mistral via Ollama)  
- 🔒 100% offline – no API keys needed  
- ⚡ Semantic search using embeddings  

---

## 🎯 Demo

```
Du: Erkläre die wichtigsten Inhalte
Jarvis:
- Machine Learning beschreibt, wie Systeme aus Daten lernen
- Neural Networks bestehen aus mehreren Schichten von Neuronen
- Data Science umfasst Analyse und Interpretation von Daten
```

---

## 🧱 Tech Stack

- Python  
- LlamaIndex  
- Ollama (Mistral)  
- FAISS (vector database)  
- HuggingFace embeddings  
- PyMuPDF (PDF parsing)  

---

## 📂 Project Structure

jarvis-ai/
│
├── src/
│   ├── ingestion.py
│   ├── rag.py
│   └── main.py
│
├── data/           # your PDFs (ignored in Git)
├── README.md
└── .gitignore

---

## ⚙️ Setup

### Clone & Setup

python -m venv venv
venv\Scripts\activate

pip install llama-index
pip install llama-index-llms-ollama
pip install llama-index-embeddings-huggingface
pip install llama-index-readers-file
pip install pymupdf pypdf faiss-cpu python-dotenv

---

### Start local model

ollama run mistral

---

## ▶️ Run

python src/main.py

---

## 🧠 How it works

PDF → Text extraction → Embeddings → Vector Search → LLM → Answer

---

## 🚀 Roadmap

- Voice interface  
- Memory  
- Web UI  
- Raspberry Pi integration  

---

## 👨‍💻 Author

Florian Balzer
