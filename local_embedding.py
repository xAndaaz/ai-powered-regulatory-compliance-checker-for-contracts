from sentence_transformers import SentenceTransformer

# Load the embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Input the query text
query_text = "Find contracts related to payment terms"
query_vector = model.encode(query_text)

# Print the query vector
print(query_vector.tolist())
