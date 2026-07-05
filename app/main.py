from fastapi import FastAPI

app = FastAPI(title="ContextFlow API")

@app.get("/")
def health_check():
    return {"status": "online", "message": "ContextFlow backend is running!"}