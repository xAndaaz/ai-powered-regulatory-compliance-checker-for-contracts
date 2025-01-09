'''
local store embeddings

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class EmbeddingManager:
    def __init__(self):
        # Initialize Hugging Face embedding model
        self.model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        self.index = faiss.IndexFlatL2(384)  # Adjust dimensions for your model
    def embed_and_store(self, chunks: list[str]) -> str:
        # Generate embeddings
        embeddings = self.model.encode(chunks)
        
        # Add embeddings to FAISS index
        self.index.add(np.array(embeddings))
        
        # Save index locally
        faiss.write_index(self.index, "local_faiss_index")

        return "Embedding and storage successful"
        '''

from sentence_transformers import SentenceTransformer
from src.utils.pinecone_handler import PineconeHandler

class EmbeddingManager:
    def __init__(self):
        # Initialize Hugging Face embedding model and Pinecone handler
        self.model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        self.pinecone_handler = PineconeHandler()

    def embed_and_store(self, chunks: list[str]):
        # Generate embeddings
        embeddings = self.model.encode(chunks)
        
        # Create metadata for each chunk
        metadata = [{"text": chunk} for chunk in chunks]
        
        # Store embeddings in Pinecone
        self.pinecone_handler.upsert_embeddings(embeddings, metadata)

        return "Embeddings stored successfully in Pinecone"