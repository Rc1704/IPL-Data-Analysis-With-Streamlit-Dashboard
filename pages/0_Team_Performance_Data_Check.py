import streamlit as st
import pandas as pd

st.set_page_config(page_title="Team Performance Data Check", layout="wide")

st.title("Team Performance Data Loader Check")

@st.cache_data
def load_team_performance():
    return pd.read_csv("data/clean_team_performance.csv")

try:
    df = load_team_performance()
    st.success("Team Performance Data loaded successfully!")
except FileNotFoundError:
    st.error("Team Performance Data not found in the data folder.")
    st.stop()

st.subheader("Dataset Shape")
st.write(f"Rows: {df.shape[0]} | Columns: {df.shape[1]}")

st.subheader("Sample Rows")
st.dataframe(df.head(10))