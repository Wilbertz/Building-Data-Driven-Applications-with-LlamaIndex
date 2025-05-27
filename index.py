
import os
from llama_index.core import StorageContext, load_index_from_storage, VectorStoreIndex

INDEX_ID = "vector"
PERSIST_DIR = "./index_cache"

def build_index(documents):
    try:
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context, INDEX_ID)
        print("All indices loaded from storage")
    except Exception as e:
        index = VectorStoreIndex.from_documents(documents)
        index.set_index_id(INDEX_ID)
        index.storage_context.persist(persist_dir=PERSIST_DIR)
        print("All indices saved to storage")

    return index

def save_index(index):
    index.storage_context.persist(persist_dir=PERSIST_DIR)

def load_index():
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)
    return index

def clear_index_cache():
    for f in os.listdir(PERSIST_DIR):
        os.remove(os.path.join(PERSIST_DIR, f))

if __name__ == "__main__":
    clear_index_cache()