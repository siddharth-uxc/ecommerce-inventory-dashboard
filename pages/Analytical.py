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

