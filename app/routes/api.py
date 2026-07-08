from fastapi import APIRouter
from app.schemas.request_body import ChatRequest
from app.core.llm_logic import ask_bot

router = APIRouter()

@router.post("/chat", summary= "Get an answer basend on document context")
def chat(request: ChatRequest):

    return {"answer": ask_bot(request.query)}