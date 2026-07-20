import streamlit as st
import pandas as pd
import plotly.express as px

risk = pd.read_csv("data/processed/risk_scores.csv")

option = st.selectbox(
    "Filter Recommendation",
    ["All", "Healthy", "Reorder", "Markdown"]
)

if option != "All":
    filtered = risk[risk["Recommendation"] == option]
else:
    filtered = risk

st.dataframe(filtered)