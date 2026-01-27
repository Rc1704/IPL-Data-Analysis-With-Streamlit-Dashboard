import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from utils.data_loader import load_ball_by_ball

st.set_page_config(page_title="Teams Dominance", layout="wide")

st.title("Teams Dominance in IPL (2008–2024)")

st.markdown(
    """
### Question  
Which teams have dominated the IPL across different seasons, and which teams have shown
consistent performance rather than isolated peak years?

"""
)

df = load_ball_by_ball()

def normalize_season(season):
    season = str(season)

    if season == "2007/08":
        return 2008
    if season == "2009/10":
        return 2010
    if season == "2020/21":
        return 2020

    if "/" in season:
        return int(season.split("/")[0])

    return int(season)

df["season_year"] = df["season"].apply(normalize_season)

df = df[df["season_year"].between(2008, 2024)]

match_runs = (
    df.groupby(["match_id", "season_year", "batting_team"])["runs_scored"]
    .sum()
    .reset_index()
)

winners = (
    match_runs.sort_values("runs_scored", ascending=False)
    .drop_duplicates(["match_id", "season_year"])
)

wins_df = (
    winners.groupby(["batting_team", "season_year"])
    .size()
    .reset_index(name="wins")
)

def clean_team_name(name):
    return name.replace("_", " ").title()

wins_df["team"] = wins_df["batting_team"].apply(clean_team_name)

ALL_SEASONS = list(range(2008, 2025))

heatmap_df = (
    wins_df
    .pivot_table(
        index="team",
        columns="season_year",
        values="wins",
        aggfunc="sum",
        fill_value=0
    )
    .reindex(columns=ALL_SEASONS, fill_value=0)
    .sort_index()
)

st.subheader("Wins By Team Per Season (Heatmap)")

fig, ax = plt.subplots(figsize=(18, 9))
sns.heatmap(
    heatmap_df,
    cmap="YlGnBu",
    linewidths=0.5,
    linecolor="gray",
    cbar_kws={"label": "Wins"},
    ax=ax
)

ax.set_title("IPL Wins By Team Per Season(2008–2024)", fontsize=16)
ax.set_xlabel("Season")
ax.set_ylabel("Team")

st.pyplot(fig)

st.subheader("Overall Wins By Teams (All Seasons)")

overall_wins = (
    wins_df.groupby("team")["wins"]
    .sum()
    .sort_values(ascending=False)
)

fig2, ax2 = plt.subplots(figsize=(14, 6))
overall_wins.plot(kind="bar", ax=ax2)

ax2.set_title("Total IPL Wins By Each Team (2008–2024)")
ax2.set_xlabel("Team")
ax2.set_ylabel("Wins")

plt.xticks(rotation=45, ha="right")

st.pyplot(fig2)

st.markdown(
    """
### Key Insights
- Teams like **Mumbai Indians** and **Chennai Super Kings** demonstrate sustained dominance across multiple seasons.
- Some franchises show short-lived peaks, indicating era-specific success rather than long-term consistency.
- The heatmap clearly reveals performance cycles and transition phases in IPL team dominance.
""")