from fastapi import APIRouter
from app.schemas.request_body import ChatRequest
from app.core.ingestion import ingest_document
from app.core.llm_logic import ask_bot

router = APIRouter()

@router.post("/ingest")
def ingest(file_name: str):
    
    return {"result": ingest_document(file_name)}

@router.post("/chat")
def chat(request: ChatRequest):

    answer = ask_bot(request.query)
    return {"answer": answer}