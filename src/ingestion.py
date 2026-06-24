import os
from llama_index.readers.file import PyMuPDFReader


def load_documents():
    reader = PyMuPDFReader()
    
    docs = []
    
    for file in os.listdir("data"):
        if file.endswith(".pdf"):
            docs.extend(reader.load_data(
                file_path=f"data/{file}"
            ))

    print("DEBUG TEXT:")
    if docs:
        print(docs[0].text[:500])

    return docs
