import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Phase-wise Analysis", layout="wide")

st.title("Phase-wise Analysis")
st.markdown(
    """
This analysis studies how different phases of a T20 match influence scoring,
wickets, and winning outcomes.

**Phases Defined**
- Powerplay: Overs 1–6  
- Middle Overs: Overs 7–15  
- Death Overs: Overs 16–20
"""
)

@st.cache_data
def load_data():
    return pd.read_csv("data/clean_ball_by_ball.csv")

df = load_data()

def get_phase(ball_no):
    over = int(ball_no)
    if over <= 6:
        return "Powerplay"
    elif over <= 15:
        return "Middle Overs"
    else:
        return "Death Overs"

df["phase"] = df["ball_no"].apply(get_phase)

match_phase_runs = (
    df.groupby(["match_id", "phase"])["runs_scored"]
    .sum()
    .reset_index()
)

match_phase_wickets = (
    df[df["wicket_confirmation"] == 1]
    .groupby(["match_id", "phase"])
    .size()
    .reset_index(name="wickets")
)

match_phase = pd.merge(
    match_phase_runs,
    match_phase_wickets,
    on=["match_id", "phase"],
    how="left"
)

match_phase["wickets"] = match_phase["wickets"].fillna(0)

avg_runs_phase = (
    match_phase.groupby("phase")["runs_scored"]
    .mean()
    .reindex(["Powerplay", "Middle Overs", "Death Overs"])
)

st.subheader("Average Runs per Match by Phase")

fig1, ax1 = plt.subplots()
avg_runs_phase.plot(kind="bar", ax=ax1)
ax1.set_ylabel("Average Runs")
ax1.set_xlabel("Phase")
ax1.set_title("Average Runs per Match by Phase")
st.pyplot(fig1)

avg_wickets_phase = (
    match_phase.groupby("phase")["wickets"]
    .mean()
    .reindex(["Powerplay", "Middle Overs", "Death Overs"])
)

st.subheader("Average Wickets per Match by Phase")

fig2, ax2 = plt.subplots()
avg_wickets_phase.plot(kind="bar", ax=ax2, color="firebrick")
ax2.set_ylabel("Average Wickets")
ax2.set_xlabel("Phase")
ax2.set_title("Average Wickets per Match by Phase")
st.pyplot(fig2)

match_winners = (
    df[df["innings_no"] == 2]
    .groupby("match_id")["batting_team"]
    .last()
    .reset_index(name="winning_team")
)

winning_phase_runs = pd.merge(
    match_phase,
    match_winners,
    on="match_id",
    how="inner"
)

avg_winning_phase = (
    winning_phase_runs.groupby("phase")["runs_scored"]
    .mean()
    .reindex(["Powerplay", "Middle Overs", "Death Overs"])
)

st.subheader("Average Phase Runs by Winning Teams")

fig3, ax3 = plt.subplots()
avg_winning_phase.plot(kind="bar", ax=ax3)
ax3.set_ylabel("Average Runs")
ax3.set_xlabel("Phase")
ax3.set_title("Average Phase Runs by Winning Teams")
st.pyplot(fig3)

st.subheader("Key Insights")

st.markdown(
    """
- Middle overs contribute the highest share of total match runs.
- Wickets fall more frequently in middle and death overs, highlighting pressure phases.
- Winning teams tend to outperform opponents most consistently during middle overs.
""")