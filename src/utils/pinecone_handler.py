import os
import pinecone  # Import the Pinecone library
from src.config.settings import settings

from pinecone import Pinecone, ServerlessSpec

class PineconeHandler:
    
    """def __init__(self):
        # Initialize Pinecone
        pinecone.init(api_key=settings.PINECONE_API_KEY, environment=settings.PINECONE_ENVIRONMENT)
        self.index_name = settings.PINECONE_INDEX_NAME.lower()  # Convert to lowercase

        # Validate index name
        if not self.index_name.replace("-", "").isalnum():
            raise ValueError(f"Invalid Pinecone index name: {self.index_name}")

        # Create or connect to the index
        if self.index_name not in pinecone.list_indexes():
            pinecone.create_index(self.index_name, dimension=384)  # Adjust dimension for embedding model
        self.index = pinecone.Index(self.index_name)

    """ 
    def __init__(self):
        # Create a Pinecone instance
        self.pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))
        self.index_name = os.environ.get("PINECONE_INDEX_NAME", "ai_compliance_embeddings")

        # Create the index if it doesn't exist
        if self.index_name not in [index.name for index in self.pc.list_indexes()]:
            self.pc.create_index(
                name=self.index_name,
                dimension=384,  # Adjust to match your embedding model's dimensions
                metric="cosine",  # Choose metric like cosine, euclidean, etc.
                spec=ServerlessSpec(cloud="aws", region=os.environ.get("PINECONE_REGION", "us-west-1"))
            )

        # Access the index
        self.index = self.pc.Index(self.index_name) 

    def upsert_embeddings(self, embeddings, metadata):
        # Prepare data for upsertion
        data = [
            {"id": str(i), "values": embedding, "metadata": meta}
            for i, (embedding, meta) in enumerate(zip(embeddings, metadata))
        ]
        self.index.upsert(vectors=data)

    def query_embeddings(self, vector, top_k=5):
        # Query the Pinecone index
        return self.index.query(vector=vector, top_k=top_k, include_metadata=True)