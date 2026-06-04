import streamlit as st
import pandas as pd
import plotly.express as px

def show_tournament_analysis():

    df = pd.read_csv("data/results.csv")

    st.header("Tournament Analysis")

    tournament = st.selectbox(
        "Tournament",
        sorted(df["tournament"].unique())
    )

    filtered = df[
        df["tournament"] == tournament
    ]

    total_matches = len(filtered)

    total_goals = (
        filtered["home_score"].sum() +
        filtered["away_score"].sum()
    )

    c1, c2 = st.columns(2)

    c1.metric(
        "Matches",
        total_matches
    )

    c2.metric(
        "Goals",
        total_goals
    )

    yearly = (
        filtered.groupby("date")
        .size()
        .reset_index(name="matches")
    )

    fig = px.line(
        yearly,
        x="date",
        y="matches",
        title="Tournament Activity"
    )

    st.plotly_chart(fig, use_container_width=True)
