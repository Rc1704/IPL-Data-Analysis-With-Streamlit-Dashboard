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
├── notebooks/
│   ├── IPL_Data_Analysis_Colab_Notebook.ipynb
│   └── README.md
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
```


## Dashboard Pages Overview

0. Data Validation

   i. Dataset loading checks

   ii. Column verification

   iii. Ensures clean pipeline execution

1. IPL Trends
   
   i. Matches per season

   ii. Average runs & scoring evolution

   iii. League-wide growth patterns

2. Team Dominance

   i. Wins by team

   ii. Seasonal dominance patterns

   iii. Long-term consistency comparison

3. Toss Impact Analysis

   i. Toss win vs match win
   
   ii. Batting first vs chasing success
   
   iii. Toss impact across seasons

4. Venue Analysis

   i. Average first-innings scores
   
   ii. Venue-wise chasing success
   
   iii.Matches played per venue
   
   iv. Venue-team dominance patterns

6. Phase-wise Match Analysis

   i. Powerplay, Middle, Death overs breakdown
   
   ii. Runs and wickets by phase
   
   iii. Phase dominance in winning matches

7. Batting Analysis

   i. Top batters by total runs
   
   ii. Most explosive batters (strike rate focus)
   
   iii. Phase-wise batting contribution

8. Bowling Analysis

   i. Top wicket-taking bowlers
   
   ii. Most economical bowlers
   
   iii. Death-over specialists

9. Player Deep-Dive Analysis

   A. Batters (Legendary Indian Players):

   1. Runs per season (longevity & peaks)
   2. Phase-wise batting roles

   B. Bowlers (Legendary Indian Players):

   1. Wickets per season
   2. Phase-wise bowling impact

9. Final Insights & Conclusion

   i. Key findings summary
   
   ii. Strategic interpretations
   
   iii. Future scope & extensions


## Key Insights

1. The IPL has evolved strategically, not just explosively
2. Middle overs play a decisive role in match outcomes
3. Toss decisions matter — but context matters more
4. Certain venues strongly influence match dynamics
5. Legendary players stand out through consistency and adaptability, not just peak seasons


## Tech Stack

1. Python
2. Pandas, NumPy
3. Matplotlib, Seaborn
4. Streamlit 


## How to Run the Project Locally

1️. Clone the Repository

git clone <your-repo-url>
cd IPL-Data-Analysis-With-Streamlit-Dashboard

2️. Install Dependencies

pip install -r requirements.txt

3️. Run the Streamlit App

streamlit run app.py

The dashboard will open automatically in browser.


## Deployment Notes

1. The app is Streamlit Cloud compatible
2. All file paths are relative
3. No hardcoded system dependencies
4. Graceful error handling included for missing data


## Future Enhancements

1. Match outcome prediction using ML
2. Player performance forecasting
3. Venue-adjusted team strength models
4. Head-to-head matchup analytics


## Author

Ram
IPL Data Analytics Project

Built for applied analytics demonstration


## Final Note

This project is designed to tell the story of IPL through data from league evolution to individual brilliance while maintaining analytical rigor and visual clarity.
