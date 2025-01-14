from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

from src.manager.embedding_manager import EmbeddingManager

router = APIRouter()

class QueryRequest(BaseModel):
    vector: List[float]
    top_k: int = 5

@router.post("/query-embeddings/")
async def query_embeddings(request: QueryRequest):
    embedding_manager = EmbeddingManager()
    try:
        results = embedding_manager.pinecone_handler.query_embeddings(request.vector, top_k=request.top_k)
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Query error: {str(e)}")
