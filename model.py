import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint 


@st.cache_resource(show_spinner="Loading model...")
def load_model(hf_token: str) -> ChatHuggingFace:
    llm = HuggingFaceEndpoint(
        repo_id="mistralai/Mistral-7B-Instruct-v0.2",
        huggingfacehub_api_token=hf_token,
        task="text-generation",
        max_new_tokens=512,
        temperature=0.4,
    )
    return ChatHuggingFace(llm=llm)
