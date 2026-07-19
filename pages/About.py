import streamlit as st

# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

# ==================================================
# PAGE TITLE
# ==================================================

st.title("ℹ️ About This Project")

st.write(
    "Learn more about the Zepto Inventory Dashboard."
)


# ==================================================
# PROJECT OVERVIEW
# ==================================================

st.header("📌 Project Overview")

st.write("""
The Zepto Inventory Dashboard is an interactive business intelligence
application developed using Python, Pandas, Plotly, and Streamlit.

The dashboard helps analyze inventory, monitor stock levels,
track discounts, estimate revenue, and gain business insights
through interactive visualizations.
""")


# ==================================================
# FEATURES
# ==================================================

st.header("🚀 Features")

st.markdown("""
- 📊 Interactive Dashboard
- 📦 Inventory Management
- 🔍 Product Search
- 📂 Category Filters
- 📉 Discount Analysis
- 💰 Revenue Analysis
- 🔥 Correlation Heatmap
- 📥 CSV Export
""")# ==================================================
# TECH STACK
# ==================================================

st.header("🛠️ Technology Stack")

st.markdown("""
- Python
- Pandas
- Plotly
- Streamlit
- Git & GitHub
""")


# ==================================================
# DATASET
# ==================================================

st.header("📂 Dataset Information")

st.write("""
Dataset Used: Zepto Inventory Dataset

Contains product information including:

- Product Name
- Category
- MRP
- Discount Percentage
- Quantity Available
- Stock Status
""")




# ==================================================
# PROJECT STATISTICS
# ==================================================

st.header("📈 Project Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Products",
        "3730"
    )

with col2:
    st.metric(
        "Categories",
        "14"
    )

with col3:
    st.metric(
        "Dashboard Pages",
        "4"
    )


# ==================================================
# DEVELOPER
# ==================================================

st.header("👨‍💻 Developer")

st.write("""
Developed by: Siddharth Jha

BCA Student | Lovely Professional University

Passionate about Data Analytics, Python,
and Business Intelligence.
""")


# ==================================================
# FUTURE ENHANCEMENTS
# ==================================================

st.header("🔮 Future Enhancements")

st.markdown("""
- 🌙 Dark Mode Support
- 📱 Mobile Responsive Design
- 🤖 AI-Based Inventory Predictions
- 📊 Advanced Business Analytics
- ☁️ Cloud Deployment
- 🔔 Stock Alert System
""")



# ==================================================
# GITHUB
# ==================================================

st.header("🔗 Project Repository")

st.markdown(
    "[View Project on GitHub](https://github.com/siddharth-uxc/ecommerce-inventory-dashboard)"
)




st.markdown("---")

st.caption(
    "Zepto Inventory Dashboard • Built with Python, Pandas, Plotly & Streamlit"
)
