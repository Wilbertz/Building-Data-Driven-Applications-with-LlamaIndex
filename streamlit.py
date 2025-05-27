import streamlit as st

def main():
    st.title("Everything you wanted to know about KPMG Denmark but were afraid to ask:")
    st.write(st.secrets["AZURE_OPEN_API_KEY"])

if __name__ == "__main__":
    main()
