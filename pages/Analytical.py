import streamlit as st
import pandas as pd
import plotly.express as px

# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Analytics",
    page_icon="📊",
    layout="wide"
)

# ==================================================
# PAGE TITLE
# ==================================================

st.title("📊 Zepto Analytics")

st.write("Detailed business insights and analytics.")

# ==================================================
# LOAD DATASET
# ==================================================

df = pd.read_csv("data/zepto_cleaned.csv")

# ==================================================
# TOP 10 MOST EXPENSIVE PRODUCTS
# ==================================================

st.subheader("🏆 Top 10 Most Expensive Products")

top_products = (
    df.sort_values(
        by="mrp",
        ascending=False
    )
    .head(10)
)

fig = px.bar(
    top_products,
    x="mrp",
    y="name",
    orientation="h",
    title="Top 10 Most Expensive Products"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==================================================
# AVERAGE DISCOUNT BY CATEGORY
# Calculate the average discount percentage
# for each category.
# ==================================================

st.subheader("📉 Average Discount by Category")

average_discount = (
    df.groupby("Category")["discountPercent"]
      .mean()
      .round(2)
      .reset_index()
)

fig2 = px.bar(
    average_discount,
    x="discountPercent",
    y="Category",
    orientation="h",
    title="Average Discount by Category"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ==================================================
# STOCK ANALYSIS
# ==================================================

st.subheader("📦 Stock Analysis by Category")

stock_category = (
    df.groupby("Category")["quantity"]
      .sum()
      .reset_index()
)

fig4 = px.bar(
    stock_category,
    x="Category",
    y="quantity",
    title="Total Stock Available by Category"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)


# ==================================================
# LOW STOCK PRODUCTS
# ==================================================

st.subheader("⚠️ Low Stock Products")

low_stock = (
    df[df["quantity"] < 10]
    .sort_values(
        by="quantity"
    )
)

st.dataframe(
    low_stock[
        ["name", "Category", "quantity"]
    ],
    use_container_width=True
)