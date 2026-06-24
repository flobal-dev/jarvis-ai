<div align="center">

# 🧠 Jarvis AI

**Chat with your documents. Fully offline.**

A local AI assistant powered by Retrieval-Augmented Generation (RAG) — query your PDFs with natural language, no cloud required.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![LlamaIndex](https://img.shields.io/badge/LlamaIndex-RAG-8A2BE2?style=flat)](https://www.llamaindex.ai/)
[![Ollama](https://img.shields.io/badge/Ollama-Mistral-black?style=flat)](https://ollama.ai/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat)](LICENSE)

</div>

---

## ✨ Features

| Feature | Description |
|---|---|
| 📄 **PDF Chat** | Ask questions about your own documents in plain language |
| 🔒 **100% Offline** | No API keys, no cloud — your data stays on your machine |
| ⚡ **Persistent Index** | Documents are indexed once and reused for fast startup |
| 🤖 **Local LLM** | Powered by Mistral via Ollama — runs entirely on-device |
| 🖥️ **Web UI** | Clean, interactive chat interface built with Streamlit |
| 🔄 **Modular Design** | Ingestion, retrieval, and generation are fully decoupled |

---

## 🚀 Demo

```
> What topics are covered in this document?

  Jarvis AI: The document covers the following topics:
  • Machine Learning fundamentals
  • Neural network architectures
  • Data science workflow and best practices
```

---

## 🧱 Tech Stack

| Layer | Technology |
|---|---|
| **Language** | Python 3.10+ |
| **RAG Framework** | LlamaIndex |
| **LLM Runtime** | Ollama (Mistral 7B) |
| **Embeddings** | HuggingFace Sentence Transformers |
| **Vector Store** | FAISS |
| **PDF Parsing** | PyMuPDF |
| **Frontend** | Streamlit |

---

## 📂 Project Structure

```
jarvis-ai/
│
├── src/
│   ├── app.py          # Streamlit UI & chat interface
│   ├── ingestion.py    # PDF loading, chunking & indexing
│   └── rag.py          # Retrieval & response generation
│
├── data/               # Place your PDF files here
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Setup

### Prerequisites

- Python 3.10+
- [Ollama](https://ollama.ai/) installed and running

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/jarvis-ai.git
cd jarvis-ai
```

### 2. Create a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the Mistral model via Ollama

```bash
ollama run mistral
```

---

## 📄 Add Your Documents

Drop your PDF files into the `/data` directory:

```
jarvis-ai/
└── data/
    ├── my-report.pdf
    ├── research-paper.pdf
    └── ...
```

Documents are indexed automatically on first run and cached for subsequent sessions.

---

## ▶️ Run the App

```bash
streamlit run src/app.py
```

Open your browser at `http://localhost:8501` and start chatting.

---

## 🧠 How It Works

```
PDF Files  →  Text Extraction  →  Chunking  →  Embeddings  →  FAISS Index
                                                                     ↓
User Query  →  Query Embedding  →  Vector Search  →  Context Retrieval
                                                                     ↓
                                               Mistral LLM  →  Answer
```

1. **Ingestion** — PDFs are parsed with PyMuPDF, split into chunks, and embedded via HuggingFace
2. **Indexing** — Embeddings are stored in a persistent FAISS vector index
3. **Retrieval** — Incoming queries are embedded and matched against the index
4. **Generation** — Relevant chunks are passed to Mistral as context for grounded answers

---

## 🗺️ Roadmap

- [x] Core RAG pipeline
- [x] Streamlit chat UI
- [ ] In-app PDF upload
- [ ] Conversation memory
- [ ] Voice interface
- [ ] Multi-document source attribution
- [ ] Raspberry Pi deployment

---

## 👨‍💻 Author

**Florian Balzer**

Built as a fully local, privacy-first alternative to cloud-based document Q&A tools.  
Contributions and feedback welcome — feel free to open an issue or PR.

---

<div align="center">
  <sub>Made with ❤️ and local compute — no data leaves your machine.</sub>
</div>
