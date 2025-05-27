from index import build_index
from documents import get_documents
from settings import initialize_settings

def repl():
    initialize_settings()

    documents = get_documents()
    index = build_index(documents)
    chat_engine = index.as_chat_engine()

    chat_engine.chat_repl()

if __name__ == "__main__":
    repl()