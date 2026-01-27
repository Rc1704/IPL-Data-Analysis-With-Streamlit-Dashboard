import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from utils.data_loader import load_team_performance

st.set_page_config(page_title="Toss Analysis", layout="wide")

st.title("Toss Impact Analysis")

st.markdown("""
### Question  
How much does winning the toss influence match outcomes in the IPL?  
Does choosing to bat or chase after winning the toss improve winning chances, and how has this impact evolved over seasons?
""")

df = load_team_performance()

df["season"] = pd.to_datetime(df["date"]).dt.year

df["toss_match_win"] = df["toss_winner"] == df["match_winner"]

df["bat_first_win"] = (
    (df["toss_decision"] == "bat") &
    (df["match_winner"] == df["toss_winner"])
)

df["chase_win"] = (
    (df["toss_decision"] == "field") &
    (df["match_winner"] == df["toss_winner"])
)

st.subheader("Toss Win vs Match Win (Overall)")

toss_win_counts = df["toss_match_win"].value_counts()

fig1, ax1 = plt.subplots()
ax1.bar(
    ["Lost Match After Toss", "Won Match After Toss"],
    [toss_win_counts.get(False, 0), toss_win_counts.get(True, 0)]
)
ax1.set_ylabel("Number of Matches")
ax1.set_title("Toss Result vs Match Result")

st.pyplot(fig1)

st.subheader("Win Percentage After Winning the Toss")

toss_win_percentage = df["toss_match_win"].mean() * 100

st.metric(
    label="Match Win % After Winning Toss",
    value=f"{toss_win_percentage:.2f}%"
)

st.subheader("Batting First vs Chasing Success")

bat_vs_chase = pd.DataFrame({
    "Bat First Wins": [df["bat_first_win"].sum()],
    "Chasing Wins": [df["chase_win"].sum()]
}).T

fig2, ax2 = plt.subplots()
ax2.bar(bat_vs_chase.index, bat_vs_chase[0])
ax2.set_ylabel("Number of Matches")
ax2.set_title("Match Wins After Winning Toss")

st.pyplot(fig2)

st.subheader("Toss Impact Over Seasons (Overall)")

seasonal_impact = (
    df.groupby("season")["toss_match_win"]
      .mean()
      .mul(100)
      .reindex(range(2008, 2025))
)

fig3, ax3 = plt.subplots(figsize=(12, 6))

ax3.plot(
    seasonal_impact.index,
    seasonal_impact.values,
    marker="o",
    linewidth=2
)

ax3.set_xticks(seasonal_impact.index)
ax3.set_xticklabels(seasonal_impact.index, rotation=45)

ax3.set_xlabel("Season")
ax3.set_ylabel("Toss Win → Match Win (%)")
ax3.set_title("Season-wise Toss Impact on Match Outcome (2008–2024)")
ax3.grid(True)

st.pyplot(fig3)

st.markdown("""
### Key Takeaways
- Winning the toss provides a **moderate but consistent advantage**, not a guarantee.
- Chasing has historically been **slightly more successful** than batting first.
- Toss impact **varies by season**, peaking in certain high-scoring or chasing-friendly years.
- Toss advantage has **not grown monotonically**, indicating tactical adaptation over time.
""")