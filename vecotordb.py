import chromadb
from embedding import embedding,embedding_result
from chunk import chunks

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection("texts")

def store_data(chunks, embeddings):

    collection.add(
        ids=[str(i) for i in range(len(chunks))],
        documents=[doc.page_content for doc in chunks],
        embeddings=embeddings
    )

store_data(chunks, embedding_result)

print(collection.count())