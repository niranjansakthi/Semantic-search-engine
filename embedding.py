from langchain_huggingface import HuggingFaceEmbeddings
from upload import documents
from chunk import chunks


embedding = HuggingFaceEmbeddings(model_name = "all-MiniLM-L6-v2")
text = [doc.page_content for doc in chunks]
embedding_result = embedding.embed_documents(text)
