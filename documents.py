from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

def get_documents():
    documents = SimpleDirectoryReader(
        input_files=["./documents/dk-KPMG-Annual-report 2024_Digital-final.pdf"]
        #input_files=["./documents/sample_document1.txt"]
    ).load_data()

    return documents