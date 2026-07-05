from pydantic import BaseSettings

class Settings(BaseSettings):
    
    APP_NAME: str = "My Application" 
    
    EMBEDDING_MODEL: str = "nomic-embedded-text"
    LLM_MODEL: str = "llama3" 
    
    CHROMA_PATH: str = "./chroma.db" 
    
    CHUNK_SIZE: int = 500
    CHUNK_OVERLAP: int = 100
    
    class Config:
        env_file = ".env"

settings = Settings()