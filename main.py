from retrieval import DataRetrieval
from augmentation import DataAugmentation
from generation import ResponseGeneration

# setting up important parameters
OLLAMA_EMBEDDING_MODEL="qwen3-embedding:0.6b"
BASE_URL="http://127.0.0.1:11434/"
TOP_K=10
CHAT_MODEL="qwen3.5:2b"


def main():

    # input
    query: str = input("Enter your query: ")

    # retrieval
    data = DataRetrieval(
        query=query,
        ollama_embedding_model=OLLAMA_EMBEDDING_MODEL,
        base_url=BASE_URL,
        top_k=TOP_K
    ).execute_data_retrieval_pipeline()

    # augmentation
    augmented_data = DataAugmentation(
        data=data,
        query=query
    ).execute_augmentation_pipeline()

    # generation
    try:
        with open("augmented_data.txt", mode='r', encoding='utf-8') as f:
            augmented_query = f.read()
    except Exception as e:
        print(f"Error occured duing fetching augmented data from the 'augmented_data.txt' file: {e}")

    model_response = ResponseGeneration(
        augmented_query=augmented_query,
        model=CHAT_MODEL,
        base_url=BASE_URL
    ).execute_response_generation_pipeline()

if __name__ == "__main__":
    main()