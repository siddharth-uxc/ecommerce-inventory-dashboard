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

st.markdown("""
# 🛒 Zepto Inventory Intelligence Dashboard

### Real-Time Inventory & Business Analytics Platform
""")

st.info(
    "📊 Monitor inventory • 💰 Analyze pricing • 📦 Track stock levels • 🚀 Business insights in real time"
)

# ==================================================
# LOAD DATASET
# ==================================================

df = pd.read_csv("data/zepto_cleaned.csv")

# ==================================================
# SIDEBAR FILTERS
# ==================================================

st.sidebar.header("🔍 Dashboard Filters")

categories = sorted(df["Category"].unique())

selected_category = st.sidebar.selectbox(
    "Select Category",
    ["All"] + list(categories)
)

show_out_of_stock = st.sidebar.checkbox(
    "Show only Out of Stock products"
)

search_product = st.sidebar.text_input(
    "Search Product"
)

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
    filtered_df = df.copy()
else:
    filtered_df = df[
        df["Category"] == selected_category
    ]

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
# KPI CARDS CSS
# ==================================================

st.markdown("""
<style>
.card {
    background: linear-gradient(
        135deg,
        #1E1E1E,
        #2A2A2A
    );
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    border: 1px solid #333;
    transition: all 0.3s ease;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 0 20px rgba(124,58,237,0.5);
}

.card h3 {
    margin: 0;
    font-size: 18px;
}

.card h1 {
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# ==================================================
# KPI CARDS
# ==================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="card">
        <h3>📦 Total Products</h3>
        <h1>{total_products}</h1>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card">
        <h3>📂 Categories</h3>
        <h1>{total_categories}</h1>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="card">
        <h3>❌ Out of Stock</h3>
        <h1>{out_of_stock}</h1>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="card">
        <h3>💰 Avg Selling Price</h3>
        <h1>₹{average_selling_price}</h1>
    </div>
    """, unsafe_allow_html=True)

# ==================================================
# CHART 1
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
# CHART 2
# ==================================================

average_price = (
    filtered_df.groupby("Category")[
        "discountedSellingPrice"
    ]
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
# CHART 3
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

stock_status["Stock Status"] = (
    stock_status["Stock Status"]
    .replace({
        True: "Out of Stock",
        False: "In Stock"
    })
)

fig3 = px.pie(
    stock_status,
    names="Stock Status",
    values="Count",
    title="Stock Availability"
)

# ==================================================
# CHART 4
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
# APPLY THEME TO ALL CHARTS
# ==================================================

for fig in [fig1, fig2, fig3, fig4]:
    fig.update_layout(
        template="plotly_dark",
        height=450
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

st.subheader("📋 Dataset Preview")

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
    ],
    use_container_width=True
)