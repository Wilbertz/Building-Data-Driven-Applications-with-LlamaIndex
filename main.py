from mock_settings import initialize_mock_settings, print_token_counts
from index import get_index
from documents import get_documents
from settings import initialize_settings

def run_query(query, use_mock = False):
    token_counter = None
    if use_mock:
        token_counter = initialize_mock_settings()
    else:
        initialize_settings()

    documents = get_documents()
    index = get_index(documents)
    query_engine = index.as_query_engine()
    answer = query_engine.query(query)

    # print(answer.get_formatted_sources())
    print("query was:", query)
    print("answer was:", answer)

    if token_counter:
        print_token_counts(token_counter)

if __name__ == "__main__":
    run_query("Is there a fair representation of women in the Board of Directors?")



