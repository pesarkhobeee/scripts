from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.faiss import FaissVectorStore
from llama_index.llms.ollama import Ollama
import faiss
import os

# Set up Ollama LLM
Settings.llm = Ollama(model="llama3.2", request_timeout=120.0)

# Step 1: Load markdown files from a directory
print("Loading documents...")
documents = SimpleDirectoryReader("docs").load_data()
print(f"Loaded {len(documents)} document(s)")

# Step 2: Set embedding model
print("Setting up embedding model...")
Settings.embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Step 3: Create FAISS vector index
print("Creating vector index...")
vector_store = FaissVectorStore(faiss_index=faiss.IndexFlatL2(384))  # 384 is the embedding dim
index = VectorStoreIndex.from_documents(documents, vector_store=vector_store)

# Step 4: Show both raw retrieval and LLM-powered query results
query = input("Enter your query: ")
if not query:
    print("No query provided. Exiting.")
    exit()

# First demonstrate raw retrieval
print("\n--- Raw Retrieval Results ---")
retriever = index.as_retriever(similarity_top_k=2)
retrieved_nodes = retriever.retrieve(query)

for i, node in enumerate(retrieved_nodes):
    print(f"Result {i+1} (Score: {node.score:.4f})")
    print(f"Content: {node.node.text}")
    print("---")

# Then demonstrate LLM-powered query
print("\n--- LLM-Powered Response ---")
query_engine = index.as_query_engine()
response = query_engine.query(query)
print(response)

# Save the index for future use (optional)
index.storage_context.persist("./storage")

