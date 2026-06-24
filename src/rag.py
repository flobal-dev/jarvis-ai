import os
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from ingestion import load_documents

# Speicherort für Index
PERSIST_DIR = "storage"

# 🔥 GLOBALS (werden nur einmal beim Start geladen)
llm = Ollama(
    model="mistral",
    request_timeout=120.0
)

embed_model = HuggingFaceEmbedding(
    model_name="all-MiniLM-L6-v2"
)


def build_index():
    # ✅ Wenn Index existiert → laden
    if os.path.exists(PERSIST_DIR):
        print("Lade bestehenden Index ⚡")

        storage_context = StorageContext.from_defaults(
            persist_dir=PERSIST_DIR
        )

        index = load_index_from_storage(
            storage_context,
            embed_model=embed_model
        )

    # ✅ sonst neu bauen
    else:
        print("Baue neuen Index (first run) ⏳")

        docs = load_documents()

        print(f"{len(docs)} Dokumente gefunden")

        index = VectorStoreIndex.from_documents(
            docs,
            embed_model=embed_model,
        )

        print("Speichere Index...")

        index.storage_context.persist(
            persist_dir=PERSIST_DIR
        )

        print("Index gespeichert ✅")

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