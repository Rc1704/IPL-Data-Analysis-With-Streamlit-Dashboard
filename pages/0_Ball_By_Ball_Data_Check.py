import streamlit as st
from utils.data_loader import load_ball_by_ball

st.set_page_config(page_title="Ball By Ball Data Check", layout="wide")

st.header("Ball By Ball Data Loader Check")

df = load_ball_by_ball()

st.success("Ball-by-ball data loaded successfully!")
st.write("Shape:", df.shape) 

st.subheader("Sample Rows")
st.write(df.head(10))