import streamlit as st

# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.markdown("""
<style>

.main-title{
    text-align:center;
    padding:20px;
    border-radius:15px;
    background: linear-gradient(135deg,#7c3aed,#4f46e5);
    color:white;
    margin-bottom:20px;
}

.feature-card{
    background:#1E1E1E;
    padding:15px;
    border-radius:12px;
    border:1px solid #333;
    text-align:center;
    margin:5px;
}

.feature-card:hover{
    transform:translateY(-3px);
}

.tech-card{
    background:#262730;
    padding:12px;
    border-radius:10px;
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

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

c1,c2,c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="feature-card">
    <h4>📦 Inventory Tracking</h4>
    <p>Monitor stock levels efficiently.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="feature-card">
    <h4>📊 Analytics</h4>
    <p>Interactive business insights.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="feature-card">
    <h4>💰 Revenue Analysis</h4>
    <p>Track revenue opportunities.</p>
    </div>
    """, unsafe_allow_html=True)

# ==================================================
# TECH STACK
# ==================================================

st.header("🛠️ Technology Stack")

t1,t2,t3,t4,t5 = st.columns(5)

t1.markdown('<div class="tech-card">🐍 Python</div>', unsafe_allow_html=True)
t2.markdown('<div class="tech-card">📊 Pandas</div>', unsafe_allow_html=True)
t3.markdown('<div class="tech-card">📈 Plotly</div>', unsafe_allow_html=True)
t4.markdown('<div class="tech-card">⚡ Streamlit</div>', unsafe_allow_html=True)
t5.markdown('<div class="tech-card">🌐 GitHub</div>', unsafe_allow_html=True)

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

st.success("""
Siddharth Jha

BCA Student - Lovely Professional University

Python | Data Analytics | Web Development
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


st.markdown("---")

st.markdown(
    "<h4 style='text-align:center;'>🚀 Built with Python, Pandas, Plotly & Streamlit</h4>",
    unsafe_allow_html=True
)