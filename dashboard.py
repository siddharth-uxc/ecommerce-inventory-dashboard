import streamlit as st
import pandas as pd
import plotly.express as px

# ==================================================
# PAGE CONFIGURATION
# Configure the dashboard page.
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

st.sidebar.header("🔍 Dashboard Filters")

# Category Filter
categories = sorted(df["Category"].unique())

selected_category = st.sidebar.selectbox(
    "Select Category",
    ["All"] + list(categories)
)

# Out of Stock Filter
show_out_of_stock = st.sidebar.checkbox(
    "Show only Out of Stock products"
)

# Search Product
search_product = st.sidebar.text_input(
    "Search Product"
)
# ==================================================
# SORT PRODUCTS
# Allow users to sort the filtered dataset.
# ==================================================

sort_option = st.sidebar.selectbox(
    "Sort Products",
    (
        "Default",
        "Highest Price",
        "Lowest Price",
        "Highest Discount",
        "Product Name (A-Z)"
    )
)


# ==================================================
# FILTER DATA
# ==================================================

if selected_category == "All":
    filtered_df = df
else:
    filtered_df = df[df["Category"] == selected_category]

if show_out_of_stock:
    filtered_df = filtered_df[
        filtered_df["outOfStock"] == True
    ]

if search_product:
    filtered_df = filtered_df[
        filtered_df["name"].str.contains(
            search_product,
            case=False,
            na=False
        )
    ]

# ==================================================
# APPLY SORTING
# ==================================================

if sort_option == "Highest Price":
    filtered_df = filtered_df.sort_values(
        by="discountedSellingPrice",
        ascending=False
    )

elif sort_option == "Lowest Price":
    filtered_df = filtered_df.sort_values(
        by="discountedSellingPrice",
        ascending=True
    )

elif sort_option == "Highest Discount":
    filtered_df = filtered_df.sort_values(
        by="discountPercent",
        ascending=False
    )

elif sort_option == "Product Name (A-Z)":
    filtered_df = filtered_df.sort_values(
        by="name"
    )

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
# CHART 1 : PRODUCT COUNT BY CATEGORY
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

fig1 = px.bar(
    category_count,
    x="Product Count",
    y="Category",
    orientation="h",
    title="Products Available in Each Category"
)

# ==================================================
# CHART 2 : AVERAGE SELLING PRICE BY CATEGORY
# ==================================================

average_price = (
    filtered_df.groupby("Category")["discountedSellingPrice"]
    .mean()
    .round(2)
    .reset_index()
)

fig2 = px.bar(
    average_price,
    x="discountedSellingPrice",
    y="Category",
    orientation="h",
    title="Average Selling Price by Category"
)

# ==================================================
# FIRST ROW OF CHARTS
# ==================================================

chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.plotly_chart(
        fig1,
        use_container_width=True
    )

with chart_col2:
    st.plotly_chart(
        fig2,
        use_container_width=True
    )

# ==================================================
# CHART 3 : STOCK AVAILABILITY
# ==================================================

stock_status = (
    filtered_df["outOfStock"]
    .value_counts()
    .reset_index()
)

stock_status.columns = [
    "Stock Status",
    "Count"
]

stock_status["Stock Status"] = stock_status[
    "Stock Status"
].replace({
    True: "Out of Stock",
    False: "In Stock"
})

fig3 = px.pie(
    stock_status,
    names="Stock Status",
    values="Count",
    title="Stock Availability"
)

# ==================================================
# CHART 4 : TOP 10 HIGHEST DISCOUNT PRODUCTS
# ==================================================

top_discount_products = (
    filtered_df
    .sort_values(
        by="discountPercent",
        ascending=False
    )
    .head(10)
)

fig4 = px.bar(
    top_discount_products,
    x="discountPercent",
    y="name",
    orientation="h",
    title="Top 10 Highest Discount Products"
)

# ==================================================
# SECOND ROW OF CHARTS
# ==================================================

chart_col3, chart_col4 = st.columns(2)

with chart_col3:
    st.plotly_chart(
        fig3,
        use_container_width=True
    )

with chart_col4:
    st.plotly_chart(
        fig4,
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