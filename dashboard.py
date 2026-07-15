import streamlit as st
import pandas as pd

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