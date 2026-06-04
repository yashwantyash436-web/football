import streamlit as st
import pandas as pd
import plotly.express as px

def show_scorer_analysis():

    df = pd.read_csv("data/goalscorers.csv")

    st.header("Goal Scorer Analysis")

    top = (
        df["scorer"]
        .value_counts()
        .head(20)
    )

    fig = px.bar(
        x=top.values,
        y=top.index,
        orientation="h",
        title="Top 20 Goal Scorers"
    )

    st.plotly_chart(fig, use_container_width=True)
