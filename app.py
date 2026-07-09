# Import Libraries

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Configuration

st.set_page_config(
    page_title="Sales Performance Analysis",
    page_icon="📈",
    layout="wide"
)

# Title

st.title("📈 Sales Performance Analysis Dashboard")

st.write("Analyze business sales using Python, Pandas and Visualization")

# Load Dataset

df = pd.read_csv("sales_data.csv")

# Convert Date Column

df["Date"] = pd.to_datetime(df["Date"])

# Revenue Column

df["Revenue"] = df["Quantity"] * df["Price"]

# KPI Calculations

total_revenue = df["Revenue"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
average_order = total_revenue / total_orders

# KPI Cards

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"₹{total_revenue:,.0f}")
col2.metric("Total Profit", f"₹{total_profit:,.0f}")
col3.metric("Total Orders", total_orders)
col4.metric("Average Order Value", f"₹{average_order:,.0f}")

st.divider()

# Monthly Revenue Trend

st.subheader("Monthly Revenue Trend")

monthly_sales = (
    df.groupby(df["Date"].dt.to_period("M"))["Revenue"]
    .sum()
    .reset_index()
)

monthly_sales["Date"] = monthly_sales["Date"].astype(str)

fig, ax = plt.subplots(figsize=(10,4))
ax.plot(monthly_sales["Date"], monthly_sales["Revenue"], marker="o")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue")
plt.xticks(rotation=45)
st.pyplot(fig)

# Top Selling Products

st.subheader("Top Selling Products")

top_products = (
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(8,5))
top_products.plot(kind="bar", ax=ax)
ax.set_ylabel("Revenue")
st.pyplot(fig)

# Sales by Region

st.subheader("Sales by Region")

region_sales = df.groupby("Region")["Revenue"].sum()

fig, ax = plt.subplots(figsize=(6,6))
ax.pie(
    region_sales,
    labels=region_sales.index,
    autopct="%1.1f%%"
)
st.pyplot(fig)

# Profit by Category

st.subheader("Profit by Category")

category_profit = df.groupby("Category")["Profit"].sum()

fig, ax = plt.subplots(figsize=(8,4))
category_profit.plot(kind="bar", ax=ax)
ax.set_ylabel("Profit")
st.pyplot(fig)

# Dataset

st.subheader("Sales Dataset")

st.dataframe(df)

# Footer

st.success("Sales Performance Analysis Completed Successfully.")