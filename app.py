# App.py

import streamlit as st
import os

# Optional: Set Streamlit page configuration
st.set_page_config(
    page_title="Employee Attrition Portfolio App",
    page_icon="📊",
    layout="wide"
)

# Sidebar navigation (Streamlit multipage support will handle this)
st.sidebar.title("📁 Navigation")
st.sidebar.info("Use the menu above to navigate between pages.")

# You can also provide a simple welcome or landing message
st.title("👋 Welcome to My Portfolio")
st.markdown(
    """
    This interactive portfolio demonstrates my data analytics skills using real tools like:
    - **pandas** for data wrangling
    - **SQLite** for lightweight relational queries
    - **Streamlit** for building dynamic dashboards and query interfaces

    Explore the pages using the menu above!
    """
)
