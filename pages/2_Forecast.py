import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
col1, col2, col3 = st.columns(3)

col1.metric("MAE", "17.89")
col2.metric("RMSE", "68.81")
col3.metric("R² Score", "0.372")

st.markdown("""
### Model Summary

The Random Forest model predicts demand using:

- Lag Features
- Rolling Average
- Calendar Features

This model supports inventory planning by estimating future demand.
""")