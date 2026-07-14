from embedding import embedding  # Your HuggingFaceEmbeddings instance
from vecotordb import collection
from langchain_community.vectorstores import chroma

query = input("Enter your question")

query_embedding = embedding.embed_query(query)

results = collection.query(
    query_embeddings=[query_embedding],n_results=2)

documents = results["documents"][0]
print("\nTop Result:\n")


documents = results["documents"][0]
distance  = results["distances"][0]
metadatas = results["metadatas"][0]

for i,(doc,distance,meta) in enumerate(zip(documents,distance,metadatas),start=1):
    print(f"\nResult {i}")
    print(f"Distance : {distance:.4f}")
    print(doc)
    print("-" * 60)