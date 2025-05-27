import streamlit as st
from index import build_index
from documents import get_documents
from settings import initialize_settings

# Streamed response emulator

def response_generator(prompt):
    yield st.session_state.chat_engine.chat(prompt).response

def get_chat_engine():
        azure_api_key = st.secrets["AZURE_OPEN_API_KEY"]
        initialize_settings(azure_api_key)
        documents = get_documents()
        index = build_index(documents)
        chat_engine = index.as_chat_engine()
        return chat_engine

st.title("Everything you wanted to know about KPMG Denmark but were afraid to ask:")

if "chat_engine" not in st.session_state:
    st.session_state.chat_engine = get_chat_engine()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(prompt))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})