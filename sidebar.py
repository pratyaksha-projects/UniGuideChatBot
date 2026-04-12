import streamlit as st


SAMPLE_QUESTIONS = [
    "Where is the CSE department?",
    "Who is the Dean of Academic Affairs?",
    "Where is the library?",
    "Where is the canteen?",
    "How do I apply for B.Tech?",
    "Where is the hostel?",
    "What is the student ERP portal?",
]


def render_sidebar(system_prompt: str, clear_fn) -> str:
    """Renders the sidebar and returns the HuggingFace token."""
    with st.sidebar:
        st.markdown("## UniGuideChatBot")
        st.markdown("HBTU Kanpur — Campus Navigator")
        st.divider()

        hf_token = st.text_input(
            "HuggingFace API Token",
            type="password",
            placeholder="hf_xxxxxxxxxxxx",
            help="Get a free token at huggingface.co/settings/tokens"
        )

        st.divider()
        st.markdown("**Try asking:**")
        for q in SAMPLE_QUESTIONS:
            if st.button(q, use_container_width=True):
                st.session_state["quick_q"] = q

        st.divider()
        if st.button("Clear Chat", use_container_width=True):
            clear_fn(system_prompt)
            st.rerun()

    return hf_token
