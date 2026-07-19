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

st.markdown("---")

# ==================================================
# PROJECT OVERVIEW
# ==================================================

st.header("📌 Project Overview")

st.write("""
The Zepto Inventory Dashboard is a data analytics and inventory
management application built using Python and Streamlit.

The dashboard helps businesses monitor inventory levels,
analyze product pricing, track discounts, identify low-stock
items, and gain valuable business insights through interactive
visualizations.
""")

# ==================================================
# FEATURES
# ==================================================

st.header("🚀 Key Features")

st.markdown("""
✅ Interactive Dashboard

✅ Category Filtering

✅ Product Search

✅ Inventory Management

✅ Revenue Analysis

✅ Stock Availability Tracking

✅ Heatmap Analysis

✅ Top Discounted Products Analysis

✅ Low Stock Monitoring

✅ Downloadable Inventory Data
""")

# ==================================================
# TECH STACK
# ==================================================

st.header("🛠️ Technology Stack")

st.markdown("""
- Python
- Pandas
- Streamlit
- Plotly Express
- Git & GitHub
""")

# ==================================================
# DATASET INFORMATION
# ==================================================

st.header("📊 Dataset Information")

st.write("""
Dataset used: Zepto Product Inventory Dataset

The dataset contains product information such as:

• Product Name

• Category

• MRP

• Discount Percentage

• Selling Price

• Quantity Available

• Stock Availability

The dataset was cleaned and analyzed using Pandas.
""")

# ==================================================
# PROJECT MODULES
# ==================================================

st.header("📂 Project Modules")

st.markdown("""
### 🏠 Dashboard
Business overview and key performance indicators.

### 📊 Analytics
Advanced analytics, revenue insights, and heatmap analysis.

### 📦 Inventory
Inventory tracking, product search, and stock management.

### ℹ️ About
Project documentation and information.
""")

# ==================================================
# DEVELOPER
# ==================================================

st.header("👨‍💻 Developer")

st.write("""
Developed by Siddharth Jha

Bachelor of Computer Applications (BCA)

Lovely Professional University
""")

# ==================================================
# GITHUB
# ==================================================

st.header("🔗 GitHub Repository")

st.write(
    "https://github.com/siddharth-uxc/ecommerce-inventory-dashboard"
)

# ==================================================
# FUTURE ENHANCEMENTS
# ==================================================

st.header("🔮 Future Enhancements")

st.markdown("""
- Real-Time Inventory Updates
- Machine Learning Forecasting
- Supplier Management
- Inventory Alerts
- Sales Prediction Models
- Cloud Database Integration
""")

st.markdown("---")

st.success(
    "Thank you for exploring the Zepto Inventory Dashboard 🚀"
)