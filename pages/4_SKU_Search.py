import streamlit as st
import pandas as pd

risk = pd.read_csv("data/processed/risk_scores.csv")

st.title("🔍 SKU Search")

sku = st.text_input("Enter SKU")

if sku:

    result = risk[
        risk["StockCode"].astype(str) == sku
    ]

    if not result.empty:
        st.success("SKU Found")
        st.dataframe(result)

    else:
        st.error("SKU Not Found")