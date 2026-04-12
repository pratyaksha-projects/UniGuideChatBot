import streamlit as st

from core.loader import load_data, build_context
from core.prompt import build_system_prompt
from core.chat import init_chat, clear_chat
from ui.sidebar import render_sidebar
from ui.chat_window import render_chat


st.set_page_config(page_title="UniGuide – HBTU", layout="centered")

# load data and build system prompt once
data = load_data()
context = build_context(data)
system_prompt = build_system_prompt(context)

# initialize chat memory
init_chat(system_prompt)

# render sidebar (returns HF token)
hf_token = render_sidebar(system_prompt, clear_chat)

# main page header
st.markdown("## UniGuide — HBTU Kanpur")
st.caption("Ask me anything about HBTU — departments, faculty, facilities, admissions and more.")
st.divider()

# render chat
render_chat(hf_token)
