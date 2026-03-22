#src,agent.py

from src.generator import generate_answer
from src.utils import clean_text, truncate_text

def agentic_rag(query, retriever, max_docs=3, max_answer_length=500):
    """
    Agentic RAG pipeline:
    1.Retrieve top N relevant documents
    2.Generate answers for each document
    3.clean and truncate answers
    4.Retry with slightly modified query if no good answer
    5.Aggregate multiple answers into one coherent answer
    """
    docs = retriever.get_relevant_documents(query)
    if not docs:
        return "No relevant documents found."

    docs = docs[:max_docs]
    answers = []
    for doc in docs:
        ans = generate_answer(query, [doc])
        ans_clean = clean_text(ans)
        if ans_clean and ans_clean.lower() != "i dont know":
            answers.append(truncate_text(ans_clean, max_answer_length))

    if not answers:
        
        retry_query = query + "explain in simple term."
        for doc in docs:
            ans_retry = generate_answer(retry_query, [doc])
            ans_retry_clean = clean_text(ans_retry)
            if ans_retry_clean and ans_retry_clean.lower() != "i dont know":
                answers.append(truncate_text(ans_retry_clean, max_answer_length))

    if not answers: # if still empty flag insufficient info
        return "not enough information in retrieved documents."

    final_answer = " ".join(answers)
    return final_answer
            
        
        
        
        
            
           

        
            

    
