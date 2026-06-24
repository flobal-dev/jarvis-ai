from llama_index.core import SimpleDirectoryReader

def load_documents():
    return SimpleDirectoryReader("data").load_data()
