import pandas as pd
import streamlit as st

DATA_DIR = "data"

@st.cache_data
def load_ball_by_ball():
    try:
        return pd.read_csv(f"{DATA_DIR}/clean_ball_by_ball.csv")
    except FileNotFoundError:
        st.error("clean_ball_by_ball.csv not found in data folder.")
        st.stop()
    except Exception as e:
        st.error(f"Error loading ball-by-ball data: {e}")
        st.stop()


@st.cache_data
def load_team_performance():
    try:
        return pd.read_csv(f"{DATA_DIR}/clean_team_performance.csv")
    except FileNotFoundError:
        st.error("clean_team_performance.csv not found.")
        st.stop()


@st.cache_data
def load_players_info():
    try:
        return pd.read_csv(f"{DATA_DIR}/clean_players_info.csv")
    except FileNotFoundError:
        st.error("clean_players_info.csv not found.")
        st.stop()


@st.cache_data
def load_teams_info():
    try:
        return pd.read_csv(f"{DATA_DIR}/clean_teams_info.csv")
    except FileNotFoundError:
        st.error("clean_teams_info.csv not found.")
        st.stop()