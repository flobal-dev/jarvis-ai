# Jarvis AI 🧠

Local AI assistant powered by Retrieval-Augmented Generation (RAG) to query and understand personal documents.

---

## 🚀 Features

- 📄 Chat with your own PDF documents
- 🧠 RAG (Retrieval-Augmented Generation)
- 🤖 Fully local LLM using **Mistral (via Ollama)**
- 🔒 No API keys required (runs completely offline)
- ⚡ Fast semantic search using embeddings

---

## 🧱 Tech Stack

- Python
- LlamaIndex
- Ollama (Mistral)
- FAISS (vector database)
- HuggingFace embeddings

---

## 📂 Project Structure

jarvis-ai/
│
├── src/              # main code
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
pip install llama-index python-dotenv pypdf faiss-cpu
pip install llama-index-llms-ollama llama-index-embeddings-huggingface
---

### 4. Install Ollama

Download from:

👉 https://ollama.com

Then run:
ollama run mistral
(This downloads and starts the local model)

---

## 📄 Add your documents

Create a folder:
/data
Add your own PDF files there.

---

## ▶️ Run the project
python src/main.py
---

## 💬 Example
You: What is the document about?
Jarvis: ...
---

## 🧠 How it works

1. PDFs are loaded and split into chunks  
2. Text is converted into embeddings  
3. Relevant chunks are retrieved  
4. Local LLM (Mistral) generates the answer  

---

## 🚀 Future Improvements

- 🎤 Voice interface (Jarvis-style assistant)
- 🧠 Memory system
- 🌐 Web UI (Streamlit)
- 🍓 Raspberry Pi integration

---

## 👨‍💻 Author

Florian Balzer