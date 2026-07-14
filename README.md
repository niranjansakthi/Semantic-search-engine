Semantic Search Engine
Overview

A Semantic Search Engine built from scratch to understand the retrieval pipeline behind modern AI applications like Retrieval-Augmented Generation (RAG).

Unlike traditional keyword search, this project retrieves documents based on their semantic meaning using sentence embeddings and vector similarity search.

This project intentionally does not use an LLM. The goal is to deeply understand document retrieval before integrating language models.

Features
📄 PDF document ingestion
✂️ Intelligent text chunking
🧠 Sentence embedding generation
🗄️ Vector storage using ChromaDB
🔍 Semantic similarity search
📊 Ranked document retrieval
Tech Stack

Backend

Python

Libraries

LangChain
ChromaDB
HuggingFace Embeddings
Sentence Transformers
PyPDFLoader

Embedding Model

all-MiniLM-L6-v2
