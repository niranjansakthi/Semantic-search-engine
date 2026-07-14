from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("C:/Users/niran/Downloads/nke-10k-2023.pdf")
documents = loader.load_and_split()
print(documents)
