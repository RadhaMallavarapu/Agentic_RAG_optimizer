# ingestion.py
# Handles documents loading and text splitting

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_documents(Agentic rag optimizer/Data/Raw/Research_Paper_on_Artificial_Intelligence.pdf):
    """
    Load documents from a PDF file 
    """
    loader = PyPDFLoader(Agentic rag optimizer/Data/Raw/Research_Paper_on_Artificial_Intelligence.pdf)
    documents = loader.load()
    return documents
def split_documents(documents, chunk_size=500, chunk_overlap=50):
  """
  split documents into smaller chunks for better retrieval.
  """
  splitter =  RecursiveCharacterTextSplitter(chunk_size=chunk_size,
                                            chunk_overlap=chunk_overlap)
  chunks = splitter.split_documents(documents)
  return chunks


