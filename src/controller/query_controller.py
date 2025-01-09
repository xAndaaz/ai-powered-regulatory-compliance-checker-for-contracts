from fastapi import APIRouter, HTTPException
from src.manager.embedding_manager import EmbeddingManager

router = APIRouter()

@router.post("/query-embeddings/")
async def query_embeddings(vector: list[float], top_k: int = 5):
    embedding_manager = EmbeddingManager()
    try:
        results = embedding_manager.pinecone_handler.query_embeddings(vector, top_k=top_k)
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Query error: {str(e)}")