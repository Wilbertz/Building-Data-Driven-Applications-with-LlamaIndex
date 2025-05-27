import streamlit as st
from index import build_index
from documents import get_documents
from settings import initialize_settings

def main():
    st.title("Everything you wanted to know about KPMG Denmark but were afraid to ask:")
    st.write(st.secrets["AZURE_OPEN_API_KEY"])

    initialize_settings()

    documents = get_documents()
    index = build_index(documents)
    chat_engine = index.as_chat_engine()



if __name__ == "__main__":
    main()
