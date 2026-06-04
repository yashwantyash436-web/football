import streamlit as st
import pandas as pd
import plotly.express as px

def show_country_analysis():

    df = pd.read_csv("data/results.csv")

    teams = sorted(
        list(
            set(df["home_team"]).union(
                set(df["away_team"])
            )
        )
    )

    team = st.selectbox(
        "Select Team",
        teams
    )

    home = df[df["home_team"] == team]
    away = df[df["away_team"] == team]

    matches = len(home) + len(away)

    wins = 0
    draws = 0
    losses = 0

    for _, row in home.iterrows():

        if row["home_score"] > row["away_score"]:
            wins += 1
        elif row["home_score"] == row["away_score"]:
            draws += 1
        else:
            losses += 1

    for _, row in away.iterrows():

        if row["away_score"] > row["home_score"]:
            wins += 1
        elif row["away_score"] == row["home_score"]:
            draws += 1
        else:
            losses += 1

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Matches", matches)
    c2.metric("Wins", wins)
    c3.metric("Draws", draws)
    c4.metric("Losses", losses)

    chart = pd.DataFrame({
        "Result": ["Wins", "Draws", "Losses"],
        "Count": [wins, draws, losses]
    })

    fig = px.pie(
        chart,
        values="Count",
        names="Result"
    )

    st.plotly_chart(fig, use_container_width=True)
