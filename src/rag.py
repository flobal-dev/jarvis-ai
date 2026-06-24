import os
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from ingestion import load_documents

PERSIST_DIR = "storage"

# ✅ GLOBAL (nur einmal geladen)
llm = Ollama(
    model="mistral",
    request_timeout=120.0
)

embed_model = HuggingFaceEmbedding(
    model_name="all-MiniLM-L6-v2"
)


def build_index():
    if os.path.exists(PERSIST_DIR):
        print("Lade bestehenden Index ⚡")

        storage_context = StorageContext.from_defaults(
            persist_dir=PERSIST_DIR
        )

        index = load_index_from_storage(
            storage_context,
            embed_model=embed_model
        )

    else:
        print("Baue neuen Index (first run) ⏳")

        docs = load_documents()

        index = VectorStoreIndex.from_documents(
            docs,
            embed_model=embed_model,
        )

        print("Speichere Index...")
        index.storage_context.persist(persist_dir=PERSIST_DIR)
        print("Index gespeichert ✅")

    return index, llm


def query(index, llm, question):
    query_engine = index.as_query_engine(
        llm=llm,
        response_mode="tree_summarize",
        similarity_top_k=2
    )

    # 🔥 BESSERER PROMPT (natürliches Deutsch)
    prompt = f"""
Du bist ein hilfreicher und verständlicher Assistent.

Beantworte die Frage NUR anhand des Dokuments.

WICHTIG:
- Schreibe natürliches, einfaches Deutsch
- Erkläre die Inhalte klar und verständlich
- Nutze Stichpunkte
- Schreibe kurz und präzise
- NICHT wie ein Fachbuch oder Wikipedia

Frage:
{question}
"""

    response = query_engine.query(prompt)

    return response