# Retriever.py
# Handles embeddings and vector store (FAISS)

from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

def create_embeddings():
  """ 
  creating embedding model
  """
  embeddings = HuggingFaceEmbeddings()
  return embeddings

def create_vector_store(chunks,embeddings):
  """
  Store document chunks in FAISS vector database.
  """
  vectorstore = FAISS.from_documents(chunks, embeddings)
  return vectorstore

def get_retriever(vectorstore):
  """
  create retriever from vector store.
  """
  retriever = vectorstore.as_retriever()
  return retriever
