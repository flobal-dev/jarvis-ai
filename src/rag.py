from llama_index.core import VectorStoreIndex
from ingestion import load_documents

def build_index():
    docs = load_documents()
    return VectorStoreIndex.from_documents(docs)

def query(index, question):
    return index.as_query_engine().query(question)