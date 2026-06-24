# 🧠 Jarvis AI

> Local AI assistant powered by Retrieval-Augmented Generation (RAG)  
> Query and understand your personal documents — fully offline.

---

## ✨ Features

- 📄 Chat mit eigenen PDF-Dokumenten  
- 🧠 Retrieval-Augmented Generation (RAG)  
- 🤖 Lokales LLM (Mistral via Ollama)  
- 🔒 100% offline – keine API Keys nötig  
- ⚡ Persistenter Index für schnelle Startzeit  
- 🖥️ Web UI mit Streamlit  

---

## 🎯 Demo

Frage: Welche Themen werden im Dokument behandelt?

Antwort:
- Machine Learning
- Neuronale Netze
- Data Science Workflow

---

## 🧱 Tech Stack

- Python
- LlamaIndex
- Ollama (Mistral)
- HuggingFace Embeddings
- FAISS
- PyMuPDF
- Streamlit

---

## 📂 Projektstruktur

jarvis-ai/
│
├── src/
│   ├── app.py
│   ├── ingestion.py
│   └── rag.py
│
├── README.md
├── requirements.txt
└── .gitignore

---

## ⚙️ Setup

### 1. Repository klonen

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

---

### 2. Ollama starten

ollama run mistral

---

## 📄 Dokumente hinzufügen

/data

Füge hier deine PDF-Dateien ein.

---

## ▶️ Anwendung starten

streamlit run src/app.py

---

## 🧠 Funktionsweise

PDF → Text → Embeddings → Vector Search → LLM → Antwort

---

## 🚀 Roadmap

- Chat UI
- PDF Upload
- Voice Interface
- Memory System
- Raspberry Pi

---

## 👨‍💻 Author

Florian Balzer
