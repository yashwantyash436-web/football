import streamlit as st
from overview import show_overview
from country_analysis import show_country_analysis
from scorer_analysis import show_scorer_analysis
from tournament_analysis import show_tournament_analysis

st.set_page_config(
    page_title="Football Analytics AI",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ Football Analytics AI Dashboard")

page = st.sidebar.radio(
    "Navigation",
    [
        "Overview",
        "Country Analysis",
        "Scorer Analysis",
        "Tournament Analysis"
    ]
)

if page == "Overview":
    show_overview()

elif page == "Country Analysis":
    show_country_analysis()

elif page == "Scorer Analysis":
    show_scorer_analysis()

elif page == "Tournament Analysis":
    show_tournament_analysis()
