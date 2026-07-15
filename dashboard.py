import streamlit as st
import pandas as pd
import plotly.express as px

# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Zepto Inventory Dashboard",
    page_icon="🛒",
    layout="wide"
)

# ==================================================
# DASHBOARD TITLE
# ==================================================

st.title("🛒 Zepto Inventory Dashboard")

# ==================================================
# LOAD CLEANED DATASET
# ==================================================

df = pd.read_csv("data/zepto_cleaned.csv")

# ==================================================
# SIDEBAR FILTERS
# ==================================================

st.sidebar.header("Filters")

categories = sorted(df["Category"].unique())

selected_category = st.sidebar.selectbox(
    "Select Category",
    ["All"] + list(categories)
)

show_out_of_stock = st.sidebar.checkbox(
    "Show only Out of Stock products"
)

# ==================================================
# FILTER DATA
# ==================================================

if selected_category == "All":
    filtered_df = df
else:
    filtered_df = df[df["Category"] == selected_category]

# Apply Out of Stock filter
if show_out_of_stock:
    filtered_df = filtered_df[
        filtered_df["outOfStock"] == True
    ]

# ==================================================
# KPI CALCULATIONS
# ==================================================

total_products = len(filtered_df)

total_categories = filtered_df["Category"].nunique()

out_of_stock = filtered_df["outOfStock"].sum()

average_selling_price = round(
    filtered_df["discountedSellingPrice"].mean(),
    2
)

# ==================================================
# KPI CARDS
# ==================================================

col1, col2, col3, col4 = st.columns(4)

col1.metric("📦 Total Products", total_products)

col2.metric("📂 Categories", total_categories)

col3.metric("❌ Out of Stock", out_of_stock)

col4.metric(
    "💰 Avg Selling Price",
    f"₹{average_selling_price}"
)

# ==================================================
# PRODUCT COUNT BY CATEGORY
# ==================================================

category_count = (
    filtered_df["Category"]
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

# ==================================================
# DATASET PREVIEW
# ==================================================

st.subheader("Dataset Preview")

st.dataframe(
    filtered_df[
        [
            "Category",
            "name",
            "mrp",
            "discountedSellingPrice",
            "discountPercent",
            "outOfStock"
        ]
    ]
)