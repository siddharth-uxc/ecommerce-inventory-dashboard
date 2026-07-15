import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Zepto Inventory Dashboard",
    page_icon="🛒",
    layout="wide"
)

# Dashboard Title
st.title("🛒 Zepto Inventory Dashboard")

# Load cleaned dataset
df = pd.read_csv("data/zepto_cleaned.csv")

# Display first five rows
st.subheader("Dataset Preview")
st.dataframe(df.head())




# ==================================================
# KPI CALCULATIONS
# Calculate important business metrics to display
# at the top of the dashboard.
# ==================================================

total_products = len(df)

total_categories = df["Category"].nunique()

out_of_stock = df["outOfStock"].sum()

average_selling_price = round(
    df["discountedSellingPrice"].mean(),
    2
)






# Create four columns for KPI cards
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "📦 Total Products",
    total_products
)

col2.metric(
    "📂 Categories",
    total_categories
)

col3.metric(
    "❌ Out of Stock",
    out_of_stock
)

col4.metric(
    "💰 Avg Selling Price",
    f"₹{average_selling_price}"
)



# ==================================================
# PRODUCT COUNT BY CATEGORY
# Count the number of products in each category.
# ==================================================

category_count = (
    df["Category"]
    .value_counts()
    .reset_index()
)

category_count.columns = [
    "Category",
    "Product Count"
]




# ==================================================
# BAR CHART
# ==================================================

fig = px.bar(
    category_count,
    x="Product Count",
    y="Category",
    orientation="h",
    title="Products Available in Each Category"
)

st.plotly_chart(
    fig,
    use_container_width=True
)