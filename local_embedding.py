from sentence_transformers import SentenceTransformer

# Load the embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Input the query text
query_text = "what HOF accepts"
query_vector = model.encode(query_text)

# Print the query vector
print(query_vector.tolist())
