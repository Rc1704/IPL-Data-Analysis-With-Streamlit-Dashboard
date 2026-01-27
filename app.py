import streamlit as st

st.set_page_config(
    page_title="IPL Data Analysis (2008–2024)",
    page_icon="🏏",
    layout="wide"
)

st.title("IPL Data Analysis Dashboard (2008–2024)")

st.markdown("""
This dashboard presents an end-to-end analysis of the Indian Premier League
using ball-by-ball data from 2008 to 2024.

Use the sidebar to navigate between analysis sections.
""")

st.success("Dashboard initialized successfully.")
