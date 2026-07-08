import streamlit as st
import requests

st.set_page_config(page_title="RAG Bot", page_icon="🤖")
st.title("🤖 DataScience RAG Bot")

API_URL = "http://127.0.0.1:8000/chat"

query = st.text_input("Enter your question:")

if st.button("Submit"):
    if query:
        with st.spinner("Bot is thinking..."):
            try:
                response = requests.post(API_URL, json={"query": query})
                if response.status_code == 200:
                    st.success("Response:") 
                    answer = response.json().get("answer")
                    st.markdown(answer)     
                else:
                    st.error(f"Error: {response.status_code}")
            except requests.exceptions.ConnectionError:
                st.error("Backend server is not running! Check your FastAPI.")
    else:
        st.warning("Please type a question first.")