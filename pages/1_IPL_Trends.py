import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from utils.data_loader import load_ball_by_ball

st.set_page_config(page_title="IPL Trends", layout="wide")

st.title("IPL Trends")
st.subheader("Question")
st.write(
    "How has the overall scoring pattern in the IPL evolved over time?\n"
    "Are matches becoming more high-scoring as seasons progress?"
)

df = load_ball_by_ball()

df["season_year"] = (
    df["season"]
    .astype(str)
    .str.extract(r"(\d{4})")[0]
    .astype(int)
)

season_summary = (
    df.groupby(["season_year", "season"])
    .agg(
        total_runs=("runs_scored", "sum"),
        matches=("match_id", "nunique")
    )
    .reset_index()
    .sort_values("season_year")
)

season_summary["avg_runs_per_match"] = (
    season_summary["total_runs"] / season_summary["matches"]
)

season_summary["season_label"] = season_summary["season"].astype(str)

st.subheader("IPL Total Runs Scored Per Season")

fig1, ax1 = plt.subplots(figsize=(11, 5))
ax1.plot(
    season_summary["season_label"],
    season_summary["total_runs"],
    marker="o",
    linewidth=2
)

ax1.set_xlabel("Season")
ax1.set_ylabel("Total Runs")
ax1.set_title("Total Runs per Season (2008–2024)")
ax1.grid(True)
plt.xticks(rotation=45)
st.pyplot(fig1)

st.subheader("Number of Matches Per Season")

fig2, ax2 = plt.subplots(figsize=(11, 5))
ax2.bar(
    season_summary["season_label"],
    season_summary["matches"]
)

ax2.set_xlabel("Season")
ax2.set_ylabel("Matches")
ax2.set_title("Matches Per Season")
ax2.grid(axis="y")
plt.xticks(rotation=45)
st.pyplot(fig2)

st.subheader("IPL Average Runs Per Match Per Season")

fig3, ax3 = plt.subplots(figsize=(11, 5))
ax3.plot(
    season_summary["season_label"],
    season_summary["avg_runs_per_match"],
    marker="o",
    linewidth=2,
    color="orange"
)

ax3.set_xlabel("Season")
ax3.set_ylabel("Average Runs per Match")
ax3.set_title("Average Runs Per Match Per Season")
ax3.grid(True)
plt.xticks(rotation=45)
st.pyplot(fig3)

st.subheader("Key Insights")
st.write("""
     - Total runs per season have increased over time, but this is influenced by both scoring rate and number of matches.
     - The number of matches expanded during league growth phases, contributing to higher seasonal run totals.
     - Average runs per match show a clear upward trend in recent seasons, confirming a genuine shift toward higher-scoring games rather than just more fixtures.
""")