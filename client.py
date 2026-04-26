import requests
import streamlit as st

# Function to call Ollama API (poem endpoint)
def get_ollama_response(input_text):
    response = requests.post(
        "http://localhost:8000/poem/invoke",
        json={'input': {'topic': input_text}}
    )
    return response.json()['output']

# Streamlit UI
st.title('LangChain Demo with LLaMA 3 (Ollama)')

input_text = st.text_input("Write a poem on")

if input_text:
    st.write(get_ollama_response(input_text))