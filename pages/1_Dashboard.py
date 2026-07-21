import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

sales = pd.read_csv("data/processed/sales_daily.csv")

risk = pd.read_csv("data/processed/risk_scores.csv")

sales["InvoiceDate"] = pd.to_datetime(sales["InvoiceDate"])

st.title("📊 Dashboard")

# KPIs
revenue = sales["Revenue"].sum()
products = sales["StockCode"].nunique()
high_risk = (risk["Stockout_Risk"] == "High").sum()
healthy = (risk["Recommendation"] == "Healthy").sum()

c1, c2, c3, c4 = st.columns(4)

c1.metric("💰 Revenue", f"£{revenue:,.0f}")
c2.metric("📦 Products", products)
c3.metric("⚠ High Risk", high_risk)
c4.metric("✅ Healthy", healthy)

st.divider()

# Revenue Chart
monthly = (
    sales.groupby(sales["InvoiceDate"].dt.to_period("M"))["Revenue"]
    .sum()
    .reset_index()
)

monthly["InvoiceDate"] = monthly["InvoiceDate"].astype(str)

fig = px.line(
    monthly,
    x="InvoiceDate",
    y="Revenue",
    markers=True,
    title="Monthly Revenue"
)

st.plotly_chart(fig, width="stretch")

st.subheader("🌍 Revenue by Country")

country = (
    sales.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig = px.bar(
    country,
    x="Country",
    y="Revenue",
    color="Revenue",
    title="Top 10 Countries by Revenue"
)

st.plotly_chart(fig, width="stretch")

st.subheader("📦 Top 10 Products")

products = (
    sales.groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig = px.bar(
    products,
    x="Revenue",
    y="Description",
    orientation="h",
    title="Top Products"
)

st.plotly_chart(fig, width="stretch")

st.subheader("⚠ Inventory Recommendations")

recommend = (
    risk["Recommendation"]
    .value_counts()
    .reset_index()
)

recommend.columns = ["Recommendation", "Count"]

fig = px.pie(
    recommend,
    names="Recommendation",
    values="Count",
    hole=0.4
)

st.plotly_chart(fig, width="stretch")

st.download_button(
    "📥 Download Risk Report",
    data=risk.to_csv(index=False),
    file_name="risk_scores.csv",
    mime="text/csv"
)