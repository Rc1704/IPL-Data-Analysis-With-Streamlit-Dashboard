import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Players Deep Dive Analysis", layout="wide")

st.title("Players Deep-Dive Analysis")
st.markdown("Legendary Indian Batters & Bowlers — Longevity, Roles, and Phase Impact")

@st.cache_data
def load_data():
    return pd.read_csv("data/clean_ball_by_ball.csv")

df = load_data()

def normalize_season(season):
    if isinstance(season, str) and "/" in season:
        return int(season.split("/")[0]) + 1
    return int(season)

df["season_year"] = df["season"].apply(normalize_season)

ALL_SEASONS = list(range(2008, 2025))

def get_phase(ball):
    if ball <= 6:
        return "Powerplay"
    elif ball <= 15:
        return "Middle Overs"
    return "Death Overs"

df["phase"] = df["ball_no"].apply(get_phase)

legendary_batters = [
    "V Kohli", "RG Sharma", "S Dhawan", "SK Raina", "MS Dhoni"
]

legendary_bowlers = [
    "YS Chahal", "B Kumar", "JJ Bumrah", "R Ashwin", "RA Jadeja"
]

st.header("Batters: Runs per Season (Longevity & Peaks)")

for batter in legendary_batters:
    batter_df = df[df["striker"] == batter]
    season_runs = (
        batter_df.groupby("season_year")["runs_scored"]
        .sum()
        .reindex(ALL_SEASONS, fill_value=0)
    )

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(
        season_runs.index,
        season_runs.values,
        marker="o",
        linewidth=2
    )
    ax.set_title(f"{batter} – Runs Per Season")
    ax.set_xlabel("Season")
    ax.set_ylabel("Runs")
    ax.grid(alpha=0.3)

    st.pyplot(fig)

st.header("Batters: Phase-wise Batting Contribution")

phase_data = (
    df[df["striker"].isin(legendary_batters)]
    .groupby(["striker", "phase"])["runs_scored"]
    .sum()
    .unstack()
    .fillna(0)
)

fig, ax = plt.subplots(figsize=(10, 5))
phase_data.plot(kind="bar", ax=ax)
ax.set_title("Phase-wise Runs Scored By Legendary Batters")
ax.set_xlabel("Batter")
ax.set_ylabel("Total Runs")
ax.legend(title="Phase")
ax.grid(axis="y", alpha=0.3)

st.pyplot(fig)

st.header("Bowlers: Wickets per Season (Longevity)")

df["is_wicket"] = df["wicket_confirmation"].astype(int)

for bowler in legendary_bowlers:
    bowler_df = df[df["bowler"] == bowler]
    season_wickets = (
        bowler_df.groupby("season_year")["is_wicket"]
        .sum()
        .reindex(ALL_SEASONS, fill_value=0)
    )

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(
        season_wickets.index,
        season_wickets.values,
        marker="s",
        linestyle="--",
        linewidth=2
    )
    ax.set_title(f"{bowler} – Wickets Per Season")
    ax.set_xlabel("Season")
    ax.set_ylabel("Wickets")
    ax.grid(alpha=0.3)

    st.pyplot(fig)

st.header("Bowlers: Phase-wise Bowling Impact")

phase_wickets = (
    df[df["bowler"].isin(legendary_bowlers)]
    .groupby(["bowler", "phase"])["is_wicket"]
    .sum()
    .unstack()
    .fillna(0)
)

phases = ["Powerplay", "Middle Overs", "Death Overs"]
angles = np.linspace(0, 2 * np.pi, len(phases), endpoint=False).tolist()
angles += angles[:1]  # close radar

for bowler in legendary_bowlers:
    values = phase_wickets.loc[bowler, phases].tolist()
    values += values[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    ax.plot(angles, values, linewidth=2)
    ax.fill(angles, values, alpha=0.25)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(phases)

    ax.set_title(f"{bowler} – Phase-wise Bowling Impact", pad=20)
    ax.grid(alpha=0.3)

    st.pyplot(fig)

st.subheader("Key Insights")
st.markdown("""
- Individual season trends reveal **longevity vs peak performance** clearly.
- Middle overs dominate batting output for most legendary batters.
- Death overs highlight **finisher roles** (notably MS Dhoni).
- Bowling impact varies sharply by phase — Bumrah & B Kumar dominate death overs.
- Phase-wise breakdown avoids misleading aggregate interpretations.
""")