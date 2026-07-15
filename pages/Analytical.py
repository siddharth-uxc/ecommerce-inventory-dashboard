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
# KPI CARDS
# ==================================================

st.subheader("📌 Business Overview")

col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        "Total Products",
        df["name"].nunique()
    )


with col2:
    st.metric(
        "Total Stock",
        df["quantity"].sum()
    )


with col3:
    st.metric(
        "Average Discount",
        f"{df['discountPercent'].mean():.2f}%"
    )


with col4:
    st.metric(
        "Low Stock Items",
        len(df[df["quantity"] < 10])
    )


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
# NUMBER OF PRODUCTS BY CATEGORY
# ==================================================

st.subheader("📦 Number of Products by Category")


category_count = (
    df.groupby("Category")["name"]
    .count()
    .reset_index()
    .rename(
        columns={
            "name": "Product Count"
        }
    )
)


fig3 = px.bar(
    category_count,
    x="Category",
    y="Product Count",
    title="Products Available in Each Category"
)


st.plotly_chart(
    fig3,
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
        [
            "name",
            "Category",
            "quantity"
        ]
    ],
    use_container_width=True
)