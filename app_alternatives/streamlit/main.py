"""Streamlit application entry point.

Run with: make run
Or: streamlit run src/app/main.py --server.port 8000
"""

import streamlit as st

from project_core import greet
from project_core.config import config

st.set_page_config(
    page_title=config.app_name,
    page_icon=":wave:",
    layout="centered",
)

st.title(config.app_name)
st.write("Enter your name to receive a greeting.")

with st.sidebar:
    st.header("About")
    st.write(f"Version: {config.app_version}")
    st.write(f"Debug: {config.debug}")

name = st.text_input("Your Name", placeholder="Enter your name...")

if st.button("Greet"):
    if name:
        greeting = greet(name)
        st.success(greeting.message)
    else:
        greeting = greet("World")
        st.info(greeting.message)
