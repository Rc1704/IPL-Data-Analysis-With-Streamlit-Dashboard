# IPL Data Analysis Dashboard (2008–2024)

An end-to-end exploratory data analysis (EDA) dashboard built using Python, Pandas, and Streamlit, offering deep insights into the Indian Premier League (IPL) across seasons, teams, venues, match phases, and legendary players.

This project transforms raw IPL data into a structured, interactive analytics experience — suitable for academic evaluation, portfolio review, and real-world analytics demonstrations.


## Project Objectives

1. Analyze macro trends in the IPL over time
2. Understand team dominance, toss impact, and venue influence
3. Break down matches by phases (Powerplay, Middle, Death)
4. Study batting and bowling performance in depth
5. Perform player-level deep-dive analysis for legendary Indian players
6. Present insights through a clean, navigable Streamlit dashboard


## Project Structure

```text
IPL-Data-Analysis-With-Streamlit-Dashboard/
│
├── data/
│   ├── clean_ball_by_ball.csv
│   ├── clean_players_info.csv
│   ├── clean_team_performance.csv
│   └── clean_teams_info.csv
│
├── pages/
│   ├── 0_Data_Check.py
│   ├── 0_Team_Performance.py
│   ├── 1_Macro_IPL_Trends.py
│   ├── 2_Team_Dominance.py
│   ├── 3_Toss_Impact.py
│   ├── 4_Venue_Analysis.py
│   ├── 5_Phase_Wise_Analysis.py
│   ├── 6_Batting_Analysis.py
│   ├── 7_Bowling_Analysis.py
│   ├── 8_Players_Deep_Dive_Analysis.py
│   └── 9_Final_Insights_Conclusion.py
│
├── utils/
│   └── data_loader.py
│
├── app.py
├── requirements.txt
└── README.md
```text

Dashboard Pages Overview

0. Data Validation

Dataset loading checks
Column verification
Ensures clean pipeline execution

1️. IPL Trends

Matches per season
Average runs & scoring evolution
League-wide growth patterns

2️. Team Dominance

Wins by team
Seasonal dominance patterns
Long-term consistency comparison

3️. Toss Impact Analysis

Toss win vs match win
Batting first vs chasing success
Toss impact across seasons

4️. Venue Analysis

Average first-innings scores
Venue-wise chasing success
Matches played per venue
Venue-team dominance patterns

5️. Phase-wise Match Analysis

Powerplay, Middle, Death overs breakdown
Runs and wickets by phase
Phase dominance in winning matches

6️. Batting Analysis

Top batters by total runs
Most explosive batters (strike rate focus)
Phase-wise batting contribution

7️. Bowling Analysis

Top wicket-taking bowlers
Most economical bowlers
Death-over specialists

8️. Player Deep-Dive Analysis

Batters (Legendary Indian Players):

Runs per season (longevity & peaks)
Phase-wise batting roles

Bowlers (Legendary Indian Players):

Wickets per season
Phase-wise bowling impact

9️. Final Insights & Conclusion

Key findings summary
Strategic interpretations
Future scope & extensions


Key Insights

1. The IPL has evolved strategically, not just explosively
2. Middle overs play a decisive role in match outcomes
3. Toss decisions matter — but context matters more
4. Certain venues strongly influence match dynamics
5. Legendary players stand out through consistency and adaptability, not just peak seasons


Tech Stack

Python
Pandas, NumPy
Matplotlib, Seaborn
Streamlit 


How to Run the Project Locally

1️. Clone the Repository

git clone <your-repo-url>
cd IPL-Data-Analysis-With-Streamlit-Dashboard

2️. Install Dependencies

pip install -r requirements.txt

3️. Run the Streamlit App

streamlit run app.py

The dashboard will open automatically in browser.


Deployment Notes

1. The app is Streamlit Cloud compatible
2. All file paths are relative
3. No hardcoded system dependencies
4. Graceful error handling included for missing data


Future Enhancements

1. Match outcome prediction using ML
2. Player performance forecasting
3. Venue-adjusted team strength models
4. Head-to-head matchup analytics


Author

Ram
IPL Data Analytics Project
Built for applied analytics demonstration


Final Note

This project is designed to tell the story of IPL through data from league evolution to individual brilliance while maintaining analytical rigor and visual clarity.