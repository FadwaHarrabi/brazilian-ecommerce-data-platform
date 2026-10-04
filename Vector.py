from langchain_ollama import OllamaEmbeddings
from langchain_community.document_loaders import csv_loader
from langchain_chroma import Chroma
from langchain_core.documents import Document
import pandas as pd
import os
import glob

db_location = "./chromaDB"
add_documents = not os.path.exists(db_location)

embeddings = OllamaEmbeddings(model="mxbai-embed-large")
csv_files = glob.glob("Data/*.csv")
documents = []
ids = []

if add_documents:
    for file_path in csv_files:
        df = pd.read_csv(file_path)
        file_name = os.path.basename(file_path)
        for i, row in df.iterrows():
            text = " ".join(str(v) for v in row.values)
            documents.append(
                Document(
                    page_content=text,
                    metadata={"source_file": file_name, "Index": i}
                )
            )
            ids.append(f"{file_name}_{i}")  # globally unique, not just per-file index

vector_store = Chroma(
    collection_name="brazillian_data",
    persist_directory=db_location,
    embedding_function=embeddings
)

if add_documents:
    batch_size = 50
    for i in range(0, len(documents), batch_size):
        batch_docs = documents[i:i + batch_size]
        batch_ids = ids[i:i + batch_size]
        print(f"Embedding batch {i} to {i + len(batch_docs)} of {len(documents)}")
        vector_store.add_documents(documents=batch_docs, ids=batch_ids)
retriever = vector_store.as_retriever(search_kwargs={"k": 5})