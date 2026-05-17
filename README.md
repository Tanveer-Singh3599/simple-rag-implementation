# Local RAG Pipeline using Ollama + ChromaDB

A simple local RAG (Retrieval-Augmented Generation) pipeline built using LangChain, Ollama, and ChromaDB.

This project reads PDFs, converts them into embeddings, stores them in a vector database, retrieves relevant chunks based on user queries, and generates answers using a fully local LLM setup.

No paid APIs. No OpenAI keys. Everything runs locally.

------------------------------------------------------------
FEATURES
------------------------------------------------------------

- Load PDFs from a folder
- Split documents into chunks
- Generate embeddings using Ollama
- Store embeddings in ChromaDB
- Perform similarity search
- Augment prompts with retrieved context
- Generate answers using a local LLM

------------------------------------------------------------
PIPELINE OVERVIEW
------------------------------------------------------------

PDFs -> Chunking -> Embeddings -> ChromaDB -> Similarity Search -> Prompt Augmentation -> LLM Response

------------------------------------------------------------
PROJECT STRUCTURE
------------------------------------------------------------

.

-> ingestion.py          # Loads PDFs and stores embeddings

-> retrieval.py          # Similarity search from vector DB

-> augmentation.py       # Formats retrieved chunks into prompt

-> generation.py         # Generates final response

-> database_config.py    # ChromaDB setup

-> main.py               # Main pipeline

------------------------------------------------------------
REQUIREMENTS
------------------------------------------------------------

user requirements.txt to install requirements.

------------------------------------------------------------
INSTALL OLLAMA
------------------------------------------------------------

Download and install Ollama from:

https://ollama.com

------------------------------------------------------------
PULL REQUIRED MODELS
------------------------------------------------------------

Run the following commands:

ollama pull qwen3-embedding:0.6b

ollama pull qwen3.5:2b

------------------------------------------------------------
START OLLAMA
------------------------------------------------------------

ollama serve

By default, Ollama usually runs on:

http://127.0.0.1:11434

------------------------------------------------------------
STEP 1 — INGEST PDFs
------------------------------------------------------------

Put your PDFs inside a folder.

Then open ingestion.py and change:

dir = "PATH_TO_YOUR_BASE_DIRECTORY"

to your actual PDF directory path.

Now run:

python ingestion.py

This process will:

- Load PDFs
- Chunk text
- Generate embeddings
- Store vectors in ChromaDB

------------------------------------------------------------
STEP 2 — ASK QUESTIONS
------------------------------------------------------------

Run:

python main.py

Then enter a query like:

Enter your query: what is reinforcement learning?

The pipeline will:

- Retrieve relevant chunks
- Create augmented prompt
- Send context to local model
- Generate final response
- Save response to RESPONSE.md

------------------------------------------------------------
OUTPUT FILES
------------------------------------------------------------

augmented_data.txt
Contains formatted prompt with retrieved chunks.

RESPONSE.md
Final generated answer from model.

chromadb/
Local vector database storage.

------------------------------------------------------------
MODELS USED
------------------------------------------------------------

Embedding Model:
qwen3-embedding:0.6b

Chat Model:
qwen3.5:2b

You can change these models inside main.py

------------------------------------------------------------
HOW RETRIEVAL WORKS
------------------------------------------------------------

The user query is converted into embeddings first.

ChromaDB performs similarity search and returns the top matching chunks.

Current TOP_K value:

TOP_K = 10

------------------------------------------------------------
CURRENT LIMITATIONS
------------------------------------------------------------

- No proper error handling
- No streaming responses
- Prompt formatting is basic
- Only PDF support currently
- No UI

But overall, the pipeline works well for learning purposes.

------------------------------------------------------------
FUTURE IMPROVEMENTS
------------------------------------------------------------

- Add FastAPI backend
- Add Streamlit or gradio UI
- Better prompt engineering
- Metadata filtering
- Hybrid search
- Reranking
- Support TXT/DOCX files
- Conversational memory

------------------------------------------------------------
LICENSE
------------------------------------------------------------

Do whatever you want with it honestly.
