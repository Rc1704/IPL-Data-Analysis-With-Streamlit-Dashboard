import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from utils.data_loader import load_team_performance

st.set_page_config(page_title="Ground / Venue Analysis", layout="wide")

st.title("Ground / Venue Analysis")

st.markdown("""
**Key Questions**
- Which venues host the most IPL matches?
- Do certain grounds favor high first-innings scores?
- Is chasing or batting first more successful at specific venues?
- Which teams dominate particular venues?
""")

df = load_team_performance()

required_cols = {
    "venue", "match_winner",
    "first_innings_score", "second_innings_score",
    "toss_decision"
}
missing = required_cols - set(df.columns)

if missing:
    st.error(f"Missing required columns: {missing}")
    st.stop()

st.subheader("Matches Played Per Venue")

top_n = 12
venue_counts = (
    df["venue"]
    .value_counts()
    .head(top_n)
)

fig, ax = plt.subplots(figsize=(12, 6))
venue_counts.plot(kind="bar", ax=ax, color="#1f77b4")

ax.set_title("Most Frequently Used IPL Venues")
ax.set_xlabel("Venue")
ax.set_ylabel("Matches Played")
plt.xticks(rotation=40, ha="right")
plt.tight_layout()

st.pyplot(fig)

st.subheader("Average First-Innings Score by Venue")

avg_first_innings = (
    df.groupby("venue")["first_innings_score"]
    .mean()
    .sort_values(ascending=False)
    .head(top_n)
)

fig, ax = plt.subplots(figsize=(10, 6))
avg_first_innings.sort_values().plot(
    kind="barh",
    ax=ax,
    color="#ff7f0e"
)

ax.set_title("Average First-Innings Score (Top Venues)")
ax.set_xlabel("Runs")
ax.set_ylabel("Venue")
plt.tight_layout()

st.pyplot(fig)

st.subheader("Batting First vs Chasing Success By Venue")

df["batting_first_win"] = (
    (df["toss_decision"] == "bat") &
    (df["match_winner"].notna())
)

df["chasing_win"] = (
    (df["toss_decision"] == "field") &
    (df["match_winner"].notna())
)

venue_strategy = (
    df.groupby("venue")[["batting_first_win", "chasing_win"]]
    .sum()
    .loc[venue_counts.index]
)

fig, ax = plt.subplots(figsize=(12, 6))
venue_strategy.plot(kind="bar", ax=ax)

ax.set_title("Batting First vs Chasing Wins (Top Venues)")
ax.set_xlabel("Venue")
ax.set_ylabel("Matches Won")
plt.xticks(rotation=40, ha="right")
plt.legend(["Batting First Wins", "Chasing Wins"])
plt.tight_layout()

st.pyplot(fig)

st.subheader("Venue-wise Team Dominance")

top_venues = venue_counts.index
top_teams = df["match_winner"].value_counts().head(10).index

dominance = (
    df[df["venue"].isin(top_venues) & df["match_winner"].isin(top_teams)]
    .groupby(["match_winner", "venue"])
    .size()
    .unstack(fill_value=0)
)

fig, ax = plt.subplots(figsize=(14, 6))
sns.heatmap(
    dominance,
    cmap="YlGnBu",
    linewidths=0.5,
    annot=True,
    fmt="d",
    ax=ax
)

ax.set_title("Team Wins by Venue (Top Teams & Venues)")
ax.set_xlabel("Venue")
ax.set_ylabel("Team")
plt.xticks(rotation=40, ha="right")
plt.tight_layout()

st.pyplot(fig)

st.subheader("Key Insights")

st.markdown("""
- A small set of venues host a disproportionate number of IPL matches.
- Certain grounds consistently produce higher first-innings totals.
- Chasing success varies strongly by venue, reinforcing toss-strategy importance.
- Venue–team heatmaps clearly reveal home-ground dominance patterns.
""")