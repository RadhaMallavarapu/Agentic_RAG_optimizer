# generator.py
from transformers import AutoTokenizer,AutoModelForSeq2SeqLM
model_name = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
def simple_llm(prompt, max_length=200):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=max_length)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
   
def generate_answer(query, docs):
    """
    generate an answer based on query and retrieved docs
    
    """
    if not docs:
        return "no relevant documents found."

    valid_docs = [doc.page_content.strip() for doc in docs if doc.page_content.strip()]
    

    
    if not valid_docs:
        return "retriever documents are empty."
    context = " ".join(valid_docs[:2])
    prompt = f""" you are a helpful AI assistant. Use the following context to answer the question .if the answer is not in the context , say "i dont know."
    context:{context}
    Question:{query}
    Answer:
    """
    answer = simple_llm(prompt, max_length=256)
    
    
    return answer.strip()
    
