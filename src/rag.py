from llama_index.core import VectorStoreIndex
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from ingestion import load_documents


def build_index():
    print("Lade Dokumente...")
    docs = load_documents()

    print(f"{len(docs)} Dokumente gefunden")

    # Lokales Embedding Modell (für Vektoren)
    embed_model = HuggingFaceEmbedding(
        model_name="all-MiniLM-L6-v2"
    )

    # Lokales LLM über Ollama
    llm = Ollama(
        model="mistral",
        request_timeout=120.0  # verhindert Timeout
    )

    print("Erstelle Index...")

    index = VectorStoreIndex.from_documents(
        docs,
        embed_model=embed_model,
    )

    print("Index fertig ✅")

    return index, llm


def query(index, llm, question):
    query_engine = index.as_query_engine(
        llm=llm,
        response_mode="tree_summarize",
        similarity_top_k=2
    )

    prompt = f"""
Du bist ein intelligenter Studienassistent.

Beantworte die Frage NUR anhand des Dokuments.

WICHTIG:
- Antworte auf Deutsch
- Gib konkrete Inhalte wieder
- Erkläre kurz die Inhalte
- Nutze Stichpunkte
- Keine allgemeinen Aussagen

Frage:
{question}
"""

    response = query_engine.query(prompt)

    return response