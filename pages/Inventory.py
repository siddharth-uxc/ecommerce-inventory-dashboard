import streamlit as st
import pandas as pd

# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Inventory",
    page_icon="📦",
    layout="wide"
)

# ==================================================
# PAGE TITLE
# ==================================================

st.title("📦 Inventory Management")

st.write("Manage and monitor product inventory.")

# ==================================================
# LOAD DATASET
# ==================================================

df = pd.read_csv("data/zepto_cleaned.csv")

# ==================================================
# KPI CARDS
# ==================================================

st.subheader("📊 Inventory Overview")

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
        "Categories",
        df["Category"].nunique()
    )

with col4:
    st.metric(
        "Low Stock Items",
        len(df[df["quantity"] < 10])
    )

# ==================================================
# PRODUCT SEARCH
# ==================================================

st.subheader("🔍 Search Products")

search_term = st.text_input(
    "Enter Product Name"
)

# ==================================================
# CATEGORY FILTER
# ==================================================

category_filter = st.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

# ==================================================
# APPLY FILTERS
# ==================================================

filtered_df = df[
    (df["name"].str.contains(
        search_term,
        case=False,
        na=False
    )) &
    (df["Category"].isin(category_filter))
]

filtered_df = filtered_df.copy()

# ==================================================
# STOCK STATUS
# ==================================================

filtered_df["Stock Status"] = filtered_df["quantity"].apply(
    lambda x: "🔴 Low Stock" if x < 10
    else "🟡 Limited Stock" if x <= 20
    else "🟢 In Stock"
)

# ==================================================
# INVENTORY TABLE
# ==================================================

st.subheader("📋 Inventory Table")

st.dataframe(
    filtered_df[
        [
            "name",
            "Category",
            "mrp",
            "discountPercent",
            "quantity",
            "Stock Status"
        ]
    ],
    use_container_width=True
)


# ==================================================
# DOWNLOAD INVENTORY
# ==================================================

csv = filtered_df.to_csv(index=False)

st.download_button(
    label="📥 Download Inventory Data",
    data=csv,
    file_name="inventory_data.csv",
    mime="text/csv"
)