import streamlit as st
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage # specially get 3 typees of messages bcz used langchain

from core.model import load_model 


def init_chat(system_prompt: str):
    """Initialize session state for chat history and display messages."""
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = [SystemMessage(content=system_prompt)]
    if "messages" not in st.session_state:
        st.session_state["messages"] = []


def get_reply(user_input: str, hf_token: str) -> str:
    """
    This is the core chat logic : append user message -> call model with full history -> append AI reply. [for better user experience] 
    """
    st.session_state["chat_history"].append(HumanMessage(content=user_input))

    if not hf_token:
        return "Please add your HuggingFace API token in the sidebar to start chatting."

    try:
        model = load_model(hf_token)
        result = model.invoke(st.session_state["chat_history"])
        reply = result.content
        st.session_state["chat_history"].append(AIMessage(content=reply))
        return reply
    except Exception as e:
        return f"Something went wrong: {e}"


def clear_chat(system_prompt: str):
    st.session_state["chat_history"] = [SystemMessage(content=system_prompt)]
    st.session_state["messages"] = []
