from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from app.core.retrieval import retrieve_context
from config.settings import settings

def ask_bot(question: str):
    context = retrieve_context(question)
    
    template = """
    You are an extremely strict Data Science assistant. 
    YOU MUST FOLLOW THESE RULES WITHOUT EXCEPTION:
    
    1. YOUR ONLY SOURCE OF KNOWLEDGE IS THE PROVIDED CONTEXT.
    2. If the answer is NOT explicitly stated in the context, you MUST reply: "I'm sorry, but that information is not available in the provided document."
    3. YOU ARE FORBIDDEN FROM USING EXTERNAL KNOWLEDGE, OPINIONS, OR CREATIVE WRITING UNDER ANY CIRCUMSTANCES.
    4. If the user asks about anything not found in the context (including general knowledge, personal questions, or creative tasks), you must refuse to answer using the phrase in Rule 2.
    5. If you are not 100% sure about an answer based on the context, you must not answer it.
    6. Do not engage in casual conversation. Only provide professional answers derived from the context.
    7. PROVIDE A DETAILED AND COMPREHENSIVE ANSWER. If the context contains multiple pieces of information related to the question, synthesize them into a well-structured, multi-paragraph response. Do not truncate your explanation.     
    
    Context: {context}
    
    Question: {question}
    
    Answer:
    """
    
    prompt = ChatPromptTemplate.from_template(template)
    
    model = ChatOllama(model=settings.LLM_MODEL)
    
    chain = prompt | model
    
    response = chain.invoke({"context": context, "question": question})
    
    return response.content