import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Batting Analysis", layout="wide")
st.title("Batting Analysis (Top Batters & Roles)")

st.markdown("""
This section explores **individual batting excellence** in the IPL:
- Consistency through total runs
- Explosiveness via strike rate
- Phase-wise contribution across match situations
""")

# -----------------------------
# Load Data
# -----------------------------
@st.cache_data
def load_ball_data():
    return pd.read_csv("data/clean_ball_by_ball.csv")

df = load_ball_data()

# -----------------------------
# Phase Mapping
# -----------------------------
def assign_phase(over):
    if over <= 6:
        return "Powerplay"
    elif over <= 15:
        return "Middle Overs"
    else:
        return "Death Overs"

df["phase"] = df["ball_no"].apply(assign_phase)

# -----------------------------
# SECTION 1: Top Batters by Total Runs
# -----------------------------
st.subheader("Top Batters By Total Runs")

batter_runs = (
    df.groupby("striker")["runs_scored"]
    .sum()
    .sort_values(ascending=False)
    .head(15)
)

fig1, ax1 = plt.subplots(figsize=(10, 6))

colors = plt.cm.Blues(np.linspace(0.4, 0.9, len(batter_runs)))

bars = ax1.barh(
    batter_runs.index[::-1],
    batter_runs.values[::-1],
    color=colors
)

ax1.set_xlabel("Total Runs")
ax1.set_title("Top Batters(All Seasons)")
ax1.grid(axis="x", linestyle="--", alpha=0.6)

# Value labels
for bar in bars:
    width = bar.get_width()
    ax1.text(
        width + 50,
        bar.get_y() + bar.get_height() / 2,
        f"{int(width)}",
        va="center",
        fontsize=9
    )

plt.tight_layout()
st.pyplot(fig1)

# -----------------------------
# SECTION 2: Most Explosive Batters (Strike Rate)
# -----------------------------
st.subheader("Explosive Batters (Strike Rate Focus)")

balls_faced = df.groupby("striker").size()
runs_scored = df.groupby("striker")["runs_scored"].sum()

strike_rate = (runs_scored / balls_faced) * 100

sr_df = (
    pd.DataFrame({
        "runs": runs_scored,
        "balls": balls_faced,
        "strike_rate": strike_rate
    })
    .query("balls >= 300")
    .sort_values("strike_rate", ascending=False)
    .head(15)
)

fig2, ax2 = plt.subplots(figsize=(10, 6))

colors = plt.cm.Oranges(np.linspace(0.4, 0.9, len(sr_df)))

bars = ax2.barh(
    sr_df.index[::-1],
    sr_df["strike_rate"].values[::-1],
    color=colors
)

ax2.set_xlabel("Strike Rate")
ax2.set_title("Most Explosive Batters (Min 300 Balls Faced)")
ax2.grid(axis="x", linestyle="--", alpha=0.6)

# Value labels
for bar in bars:
    width = bar.get_width()
    ax2.text(
        width + 1,
        bar.get_y() + bar.get_height() / 2,
        f"{width:.1f}",
        va="center",
        fontsize=9
    )

plt.tight_layout()
st.pyplot(fig2)

# -----------------------------
# SECTION 3: Phase-wise Batting Contribution
# -----------------------------
st.subheader("Phase-wise Batting Contribution (Top Batters)")

top_batters = batter_runs.head(10).index

phase_runs = (
    df[df["striker"].isin(top_batters)]
    .groupby(["striker", "phase"])["runs_scored"]
    .sum()
    .unstack()
    .fillna(0)
)

fig3, ax3 = plt.subplots(figsize=(12, 6))

x = np.arange(len(phase_runs.index))
width = 0.25

ax3.bar(x - width, phase_runs["Powerplay"], width, label="Powerplay")
ax3.bar(x, phase_runs["Middle Overs"], width, label="Middle Overs")
ax3.bar(x + width, phase_runs["Death Overs"], width, label="Death Overs")

ax3.set_xticks(x)
ax3.set_xticklabels(phase_runs.index, rotation=45, ha="right")
ax3.set_ylabel("Runs")
ax3.set_title("Phase-wise Runs Contribution By Top Batters")
ax3.legend()
ax3.grid(axis="y", linestyle="--", alpha=0.6)

plt.tight_layout()
st.pyplot(fig3)

# -----------------------------
# Key Insights (Plain Text – No Box)
# -----------------------------
st.subheader("Key Insights")

st.markdown("""
- Elite batters dominate through **long-term consistency**, not short peaks.
- Strike rate highlights **modern power hitters**, often different from total-run leaders.
- Middle overs remain the **highest run-contributing phase** for top batters.
- Death overs separate finishers from accumulators.
""")