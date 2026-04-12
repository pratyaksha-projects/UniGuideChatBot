import streamlit as st
from core.chat import get_reply


def render_chat(hf_token: str):
    """Renders chat history and handles new messages."""

    # show all previous messages
    for msg in st.session_state["messages"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # handle sidebar quick-question button clicks
    if "quick_q" in st.session_state and st.session_state["quick_q"]:
        user_input = st.session_state.pop("quick_q")
        _handle_message(user_input, hf_token)
        st.rerun()

    # handle typed input
    if user_input := st.chat_input("Ask about HBTU - faculty, departments, facilities..."):
        _handle_message(user_input, hf_token)


def _handle_message(user_input: str, hf_token: str):
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state["messages"].append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        with st.spinner("Looking that up..."):
            reply = get_reply(user_input, hf_token)
        st.markdown(reply)
    st.session_state["messages"].append({"role": "assistant", "content": reply})
