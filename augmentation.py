from typing import List

class DataAugmentation:

    def __init__(self, data: List[str], query: str):
        self.data = data
        self.query = query
    
    def _data_formatting(self):

        with open("augmented_data.txt", mode='w', encoding='utf-8') as f:
            f.write(
                "You are a helpful assistant. Use the following retrieved documents to answer the user's question.\n\nDocuments:\n"
            )

            for chunks in self.data['documents'][0]:
                f.write(f"-> {chunks.replace('\n', ' ')}\n")
            
            f.write(f"\nUser question: {self.query}")
    
    def execute_augmentation_pipeline(self):
        self._data_formatting()

        print("Augmented data stored in 'augmented_data.txt' in current directory")