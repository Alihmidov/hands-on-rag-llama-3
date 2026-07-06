from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    
    APP_NAME: str = "My Application" 
    
    EMBEDDING_MODEL: str = "nomic-embed-text" 
    LLM_MODEL: str = "llama3" 
    
    CHROMA_PATH: str = "./chroma.db" 
    
    CHUNK_SIZE: int = 500
    CHUNK_OVERLAP: int = 100
    
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()