"""Streamlit application entry point.

Run with: make run-streamlit
Or: streamlit run src/streamlit_app/main.py

Streamlit is great for:
- Data dashboards
- Interactive reports
- Data exploration tools
"""

import streamlit as st

from project_core import greet
from project_core.settings import settings

# Page configuration
st.set_page_config(
    page_title=settings.app_name,
    page_icon="👋",
    layout="centered",
)

# Header
st.title(settings.app_name)
st.markdown("A simple greeting demo using Streamlit")

# Input
name = st.text_input(
    "Your Name",
    value="World",
    placeholder="Enter your name...",
)

# Process and display
if st.button("Greet", type="primary"):
    if not name.strip():
        name = "World"
    greeting = greet(name)
    st.success(greeting.message)

# Sidebar with info
with st.sidebar:
    st.header("About")
    st.markdown(
        """
        This is a demo Streamlit app showing how to
        integrate with the shared `project_core` package.

        The business logic is completely separated from
        the UI layer.
        """
    )
    st.divider()
    st.caption(f"Version: {settings.app_version}")
