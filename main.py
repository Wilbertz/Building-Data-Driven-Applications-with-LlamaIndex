from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

from mock_settings import initialize_mock_settings, print_token_counts
from settings import initialize_settings

#initialize_settings()
token_counter = initialize_mock_settings()

documents = SimpleDirectoryReader(
    input_files=["./documents/dk-KPMG-Annual-report 2024_Digital-final.pdf"]
    #input_files=["./documents/sample_document1.txt"]
).load_data()

index = VectorStoreIndex.from_documents(documents)

query = "What are famous buildings in Rome?"
query_engine = index.as_query_engine()
answer = query_engine.query(query)

# print(answer.get_formatted_sources())
# print("query was:", query)
# print("answer was:", answer)

print_token_counts(token_counter)



