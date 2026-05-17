from chromadb import PersistentClient

# initializing chromadb client
chroma_client = PersistentClient(path="./chromadb")

# initializing vector database
my_vector_collection = chroma_client.get_or_create_collection(name="my_vdb")

# fetching database for observability debugging purposes
if __name__ == '__main__':

    print("Fetching database at putting it in 'example_data_from_db.txt' file in current directory.")

    sample = my_vector_collection.get(include=["embeddings", "documents", "metadatas"])

    with open("example_data_from_db.txt", mode='w', encoding='utf-8') as f:
        f.write(str(sample))