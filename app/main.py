from fastapi import FastAPI 
from app.routes.api import router 

app = FastAPI(title="DATASCIENCE RAG BOT API")

@app.get("/health_check", summary = "Check server status")
def health_check():
    return {"status": "online", "message": "API is running!"}

app.include_router(router)