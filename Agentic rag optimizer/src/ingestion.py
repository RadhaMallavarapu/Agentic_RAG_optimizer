# ingestion.py
# Handles documents loading and text splitting
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_documents(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    return documents


def split_documents(documents, chunk_size=500, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = splitter.split_documents(documents)
    return chunks
docs = load_documents("../Data/Raw/Research_Paper_on_Artificial_Intelligence.pdf")
chunks = split_documents(docs)
print(len(chunks))