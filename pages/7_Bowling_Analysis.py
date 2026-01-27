import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Bowling Analysis", layout="wide")
st.title("Bowling Analysis (Top Bowlers & Specialists)")

st.markdown("""
This analysis focuses on **bowling excellence** across IPL seasons:
- Wicket-taking consistency
- Run control (economy)
- High-pressure death overs performance
""")

@st.cache_data
def load_ball_data():
    return pd.read_csv("data/clean_ball_by_ball.csv")

df = load_ball_data()
df["legal_ball"] = ~df["type_of_extras"].isin(["wides", "noballs"])
df["is_wicket"] = df["wicket_confirmation"] == 1

def assign_phase(over):
    if over <= 6:
        return "Powerplay"
    elif over <= 15:
        return "Middle Overs"
    else:
        return "Death Overs"

df["phase"] = df["ball_no"].apply(assign_phase)

st.subheader("Top Bowlers By Wickets")

bowler_wickets = (
    df[df["is_wicket"]]
    .groupby("bowler")
    .size()
    .sort_values(ascending=False)
)

bowler_wickets = bowler_wickets[bowler_wickets >= 50].head(15)

fig1, ax1 = plt.subplots(figsize=(10, 6))
colors = plt.cm.Purples(np.linspace(0.4, 0.9, len(bowler_wickets)))

bars = ax1.barh(
    bowler_wickets.index[::-1],
    bowler_wickets.values[::-1],
    color=colors
)

ax1.set_xlabel("Total Wickets")
ax1.set_title("Top Bowlers By Wickets(Min 50 Wickets)")
ax1.grid(axis="x", linestyle="--", alpha=0.6)

for bar in bars:
    width = bar.get_width()
    ax1.text(width + 1, bar.get_y() + bar.get_height()/2,
             f"{int(width)}", va="center", fontsize=9)

plt.tight_layout()
st.pyplot(fig1)

st.subheader("Most Economical Bowlers(Control Specialists)")

economy_df = (
    df[df["legal_ball"]]
    .groupby("bowler")
    .agg(
        runs_conceded=("runs_scored", "sum"),
        balls=("legal_ball", "sum")
    )
)

economy_df["overs"] = economy_df["balls"] / 6
economy_df["economy"] = economy_df["runs_conceded"] / economy_df["overs"]
economy_df = economy_df[economy_df["balls"] >= 300]
economy_df = economy_df.sort_values("economy").head(15)

fig2, ax2 = plt.subplots(figsize=(10, 6))
colors = plt.cm.Greens(np.linspace(0.4, 0.9, len(economy_df)))

bars = ax2.barh(
    economy_df.index[::-1],
    economy_df["economy"].values[::-1],
    color=colors
)

ax2.set_xlabel("Economy Rate")
ax2.set_title("Most Economical Bowlers (Min 50 Overs Bowled)")
ax2.grid(axis="x", linestyle="--", alpha=0.6)

for bar in bars:
    width = bar.get_width()
    ax2.text(width + 0.05, bar.get_y() + bar.get_height()/2,
             f"{width:.2f}", va="center", fontsize=9)

plt.tight_layout()
st.pyplot(fig2)

st.subheader("Death Overs Specialists (Overs 16–20)")

death_df = df[
    (df["phase"] == "Death Overs") &
    (df["legal_ball"])
]

death_stats = (
    death_df.groupby("bowler")
    .agg(
        runs_conceded=("runs_scored", "sum"),
        balls=("legal_ball", "sum"),
        wickets=("is_wicket", "sum")
    )
)

death_stats["overs"] = death_stats["balls"] / 6
death_stats["economy"] = death_stats["runs_conceded"] / death_stats["overs"]


death_stats = death_stats[death_stats["balls"] >= 120]
death_stats = death_stats.sort_values(
    ["wickets", "economy"],
    ascending=[False, True]
).head(15)

fig3, ax3 = plt.subplots(figsize=(10, 6))
colors = plt.cm.Reds(np.linspace(0.4, 0.9, len(death_stats)))

bars = ax3.barh(
    death_stats.index[::-1],
    death_stats["wickets"].values[::-1],
    color=colors
)

ax3.set_xlabel("Wickets in Death Overs")
ax3.set_title("Best Death Overs Bowlers (Min 20 Overs)")
ax3.grid(axis="x", linestyle="--", alpha=0.6)

for i, bowler in enumerate(death_stats.index[::-1]):
    wkts = death_stats.loc[bowler, "wickets"]
    eco = death_stats.loc[bowler, "economy"]
    ax3.text(wkts + 0.2, i,
             f"Wkts: {wkts} | Eco: {eco:.2f}",
             va="center", fontsize=8)

plt.tight_layout()
st.pyplot(fig3)

st.subheader("Key Insights")

st.markdown("""
- Wicket-taking ability and economy often **do not overlap**, highlighting different bowling roles.
- Control specialists thrive by **minimizing run flow**, not chasing wickets.
- Death overs demand **precision under pressure**, where only elite bowlers succeed consistently.
- The best death bowlers combine **wickets + low economy**, not just one metric.
""")