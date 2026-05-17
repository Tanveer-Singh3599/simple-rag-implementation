from uuid import uuid4
from typing import List
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from database_config import my_vector_collection

class DataIngestion:

    def __init__(self, dir: str, ollama_embedding_model: str, base_url: str, chunk_size: int = 1000, chunk_overlap: int = 200):
        self.dir = dir
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.ollama_embedding_model = ollama_embedding_model
        self.base_url = base_url
        
        self.chunks: List[str] = None
        self.documents: List[Document] = None

    
    def _load_to_document(self):
        self.documents = PyPDFDirectoryLoader(self.dir).load()

    def _chunk_data(self):
        splitter = RecursiveCharacterTextSplitter(chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap)
        self.chunks = splitter.split_documents(documents=self.documents)
    
    def _embed_data(self):
        try:
            embedding_model = OllamaEmbeddings(model=self.ollama_embedding_model, dimensions=1024, base_url=self.base_url)
        except Exception as e:
            print(f"Error occured during embedding model initialization: {e}")
        
        # creating embedding structure and storing in chromadb
        contents = [chunk.page_content for chunk in self.chunks]
        metadatas = [chunk.metadata for chunk in self.chunks]
        embeddings = embedding_model.embed_documents(texts=contents)

        my_vector_collection.upsert(
            ids=[str(uuid4()) for i in range(len(embeddings))],
            embeddings=embeddings,
            documents=contents,
            metadatas=metadatas
        )

    # main pipeline
    def execute_data_ingestion_pipeline(self):
        self._load_to_document()
        self._chunk_data()
        self._embed_data()

if __name__ == '__main__':

    i = DataIngestion(
        ollama_embedding_model="qwen3-embedding:0.6b",
        base_url="http://127.0.0.1:11434/",
        dir="PATH_TO_YOUR_BASE_DIRECTORY"
    )

    i.execute_data_ingestion_pipeline()