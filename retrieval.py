from typing import List
from database_config import my_vector_collection
from langchain_ollama import OllamaEmbeddings

class DataRetrieval:

    def __init__(self, query: str, ollama_embedding_model: str, base_url: str, top_k: int = 10):
        self.query = query
        self.ollama_embedding_model = ollama_embedding_model
        self.base_url = base_url
        self.top_k = top_k

        self.embedding: str = None
        self.retrived_data: List[str] = None

    def _generate_embedding(self):
        try:
            embedding_model = OllamaEmbeddings(model=self.ollama_embedding_model, dimensions=1024, base_url=self.base_url)
        except Exception as e:
            print(f"Error occured during embedding model initialization: {e}")
        
        self.embedding = embedding_model.embed_query(text=self.query)

    def _similarity_search(self):
        self.retrived_data = my_vector_collection.query(
            query_embeddings=self.embedding,
            n_results=self.top_k
        )
    
    def execute_data_retrieval_pipeline(self) -> List[str]:
        self._generate_embedding()
        self._similarity_search()

        return self.retrived_data