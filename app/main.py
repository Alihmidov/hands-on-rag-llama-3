from fastapi import FastAPI 
from app.routes.api import router 

app = FastAPI(title="DATASCIENCE-RAG-BOT-API")

app.include_router(router, prefix="/api")

@app.get("/")
def health_check():
    return {"status": "online", "message": "ContextFlow backend is running!"}