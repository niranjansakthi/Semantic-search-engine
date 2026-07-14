from langchain_text_splitters import RecursiveCharacterTextSplitter
from upload import documents


text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000,chunk_overlap=200)

chunks = text_splitter.split_documents(documents)

print(len(chunks))