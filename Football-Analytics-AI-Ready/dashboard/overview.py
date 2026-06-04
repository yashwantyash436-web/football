import streamlit as st
import pandas as pd
import plotly.express as px

def show_overview():

    df = pd.read_csv("data/results.csv")

    st.header("Overview")

    total_matches = len(df)

    total_teams = len(
        set(df["home_team"]).union(
            set(df["away_team"])
        )
    )

    total_tournaments = df["tournament"].nunique()

    total_goals = (
        df["home_score"].sum() +
        df["away_score"].sum()
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Matches", total_matches)
    c2.metric("Teams", total_teams)
    c3.metric("Tournaments", total_tournaments)
    c4.metric("Goals", total_goals)

    st.subheader("Top 10 Tournaments")

    tournament_count = (
        df["tournament"]
        .value_counts()
        .head(10)
    )

    fig = px.bar(
        tournament_count,
        x=tournament_count.index,
        y=tournament_count.values,
        title="Top Tournaments"
    )

    st.plotly_chart(fig, use_container_width=True)
