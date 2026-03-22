# Agentic RAG Optimizer

## Overview
This project implements a **modular Agentic RAG(Retrieved-Augmented Generation) pipeline**:
it allows you to ask questions about documents(PDFs) and get intelligent answers using LLMs with vector-based retrieval.

**Key Features:**
-PDF ingestion and chunking
-Vector-based retrieval using FAISS
-Answer generation with FLAN-T5
-Agentic behaviour: multi-document reasoning, query rephrasing, answer aggregation
-safe: handles missing information and avoids hallucinations
-mudular : easy to swap LLm or retriever

## Folder Structure
Agentic RAG :
       1.src:--
           1.ingestion.py # Load and chunk documents
           2.retriever.py # Embedding + FAISS retriever
           3.generator.py # FLAN-T5 answer generator
           4.agents.py # Agentic RAG logic
           5.utils.py # Helper functions(clean_text,truncate)
       2.notebooks:--
           1.final_agentic_RAG.ipynb # notebook to run queries 
       3.requirements.txt # libraries used in project
       4.README.md # project overview and instructions
## installation
1.clone the repo:
git clone<your-github-repo-url>
2.Navigate into the project
cd Agentic RAG
3.install required libraries
pip install -r requirements.txt

## usage
1.Replace "abc.pdf" in notebooks/final_agentic_RAG.ipynb with your own PDF file.
2.Open and run the notebook
3.Example queries you can try:
   queries = [ "what is this document about?",
   "what is the main topic of the document.?",
   "List key points mentioned in the document."]

## How it works
1.**ingestion** - PDFs are Loaded and split into chunks for processing .
2.**retriever**- chunks are embedded and stored in FAISS vector store. Top-k relevant chunks are retrieved based on your query.
3.**generator**- FLAN-T5 generates  answers for each retrieved chunks.
4.**Agentic Layer**- combines multiple answers ,retries queries if the answer is missing and produces a coherent final answer.

## Example outputs
question:what is this document about
Answer: intelligence
--------------------------------------------------
question:what is the main topic of the document?
Answer: artificial intelligence intelligence constructing human-like machines or robots
--------------------------------------------------
question:List key points mentioned in the documents.
Answer: not enough information in retrieved documents.

## Future enhancements
-support for multiple file formates(word. txt, etc)
-multi-step reasoning and advanced query rewriting
-confidance scoring for answers
-integration with larger LLMs for more comprehensive answers.