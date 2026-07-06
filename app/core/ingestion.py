import os 
import fitz 
from config.settings import settings 
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_chroma import Chroma 

def ingest_document(file_name: str):
    file_path = os.path.join("data","raw", file_name)
    
    if not os.path.exists(file_path):
        return f"Error: {file_path} not found!"
    
    doc = fitz.open(file_path)
    text = "".join([page.get_text() for page in doc])
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = settings.CHUNK_SIZE,
        chunk_overlap = settings.CHUNK_OVERLAP
    )
    chunks = splitter.split_text(text)
    
    vectorstore = Chroma.from_texts(
        texts = chunks,
        embedding = OllamaEmbeddings(model=settings.EMBEDDING_MODEL),
        persist_directory = settings.CHROMA_PATH
    )
    
    return f"Successfully ingested {len(chunks)} chunks from {file_name} into vector store."