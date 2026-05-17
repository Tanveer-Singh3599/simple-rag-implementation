from langchain.chat_models import init_chat_model

class ResponseGeneration:

    def __init__(self, augmented_query: str, model: str, base_url: str, model_provider: str = "Ollama"):
        self.augmented_query = augmented_query
        self.model = model
        self.base_url = base_url
        self.model_provider = model_provider
        
        self.response = None

    def _generate_response(self):
        try:
            chat_model = init_chat_model(
                model=self.model,
                model_provider=self.model_provider,
                base_url=self.base_url
            )

            self.response = chat_model.invoke(input=self.augmented_query)
        except Exception as e:
            print(f"An error occured while invoking chat model: {e}")
    
    def _store_response(self):
        with open("RESPONSE.md", mode='w', encoding='utf-8') as f:
            f.write(self.response.content)
        
        print("Your answer is stored in 'RESPONSE.md' in current directory.")
    
    def execute_response_generation_pipeline(self):
        self._generate_response()
        self._store_response()