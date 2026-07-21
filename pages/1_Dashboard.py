import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

sales = pd.read_csv("data/processed/sales_daily.csv")
risk = pd.read_csv("data/processed/risk_scores.csv")

# Correct column names
sales["Date"] = pd.to_datetime(sales["Date"])

st.title("📊 Dashboard")

# KPIs
total_revenue = sales["revenue"].sum()
total_products = sales["StockCode"].nunique()
total_units = sales["units_sold"].sum()
high_risk = (risk["Stockout_Risk"] == "High").sum()

c1, c2, c3, c4 = st.columns(4)

c1.metric("💰 Revenue", f"£{total_revenue:,.2f}")
c2.metric("📦 Products", total_products)
c3.metric("🛒 Units Sold", int(total_units))
c4.metric("⚠ High Risk", high_risk)

st.divider()

# Daily Revenue Chart
daily = sales.groupby("Date")["revenue"].sum().reset_index()

fig = px.line(
    daily,
    x="Date",
    y="revenue",
    title="Daily Revenue"
)

st.plotly_chart(fig, use_container_width=True)

# Inventory Recommendation Chart
recommend = risk["Recommendation"].value_counts().reset_index()
recommend.columns = ["Recommendation", "Count"]

fig = px.pie(
    recommend,
    names="Recommendation",
    values="Count",
    hole=0.4
)

st.plotly_chart(fig, use_container_width=True)
