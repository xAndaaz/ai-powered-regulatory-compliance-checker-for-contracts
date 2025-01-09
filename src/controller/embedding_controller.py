from fastapi import APIRouter, HTTPException
from src.manager.embedding_manager import EmbeddingManager

router = APIRouter()

@router.post("/embed-data/")
async def embed_and_store(chunks: list[str]):
    embedding_manager = EmbeddingManager()
    try:
        result = embedding_manager.embed_and_store(chunks)
        return {"message": "Chunks embedded and stored successfully", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Embedding error: {str(e)}")