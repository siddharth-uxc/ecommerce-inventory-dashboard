import pandas as pd

# ==================================================
# LOAD THE CLEANED DATASET
# Read the cleaned Zepto inventory dataset into a
# Pandas DataFrame. All further analysis is performed
# on this cleaned data.
# ==================================================

df = pd.read_csv("data/zepto_cleaned.csv")


# ==================================================
# DATASET OVERVIEW
# Understand the structure of the dataset before
# performing any analysis.
#
# head()     -> Displays first 5 rows
# shape      -> Shows rows and columns
# columns    -> Lists all column names
# info()     -> Shows data types and memory usage
# ==================================================

print(df.head())

print("\nShape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nInfo:")
df.info()


# ==================================================
# DATA QUALITY CHECKS
# Ensure the dataset is clean and suitable for
# analysis.
#
# - Missing Values
# - Duplicate Rows
# - Unique Categories
# - Number of Categories
# - Stock Availability
# ==================================================

print("\n" + "=" * 50)
print("MISSING VALUES")
print("=" * 50)
print(df.isnull().sum())

print("\n" + "=" * 50)
print("DUPLICATE ROWS")
print("=" * 50)
print(df.duplicated().sum())

print("\n" + "=" * 50)
print("UNIQUE CATEGORIES")
print("=" * 50)
print(df["Category"].unique())

print("\n" + "=" * 50)
print("NUMBER OF CATEGORIES")
print("=" * 50)
print(df["Category"].nunique())

print("\n" + "=" * 50)
print("OUT OF STOCK")
print("=" * 50)
print(df["outOfStock"].value_counts())


# ==================================================
# DATA CLEANING
# Remove duplicate rows to ensure that every record
# is unique before performing analysis.
# ==================================================

rows_before = df.shape[0]
print(f"Rows before cleaning: {rows_before}")

df = df.drop_duplicates()

rows_after = df.shape[0]
print(f"Rows after cleaning: {rows_after}")

duplicates_removed = rows_before - rows_after
print(f"Duplicates removed: {duplicates_removed}")


# ==================================================
# SAVE CLEANED DATASET
# Store the cleaned dataset so future analysis can
# directly use this file instead of cleaning again.
# ==================================================

df.to_csv("data/zepto_cleaned.csv", index=False)


# ==================================================
# EDA 1 : PRODUCT COUNT BY CATEGORY
# Count how many products belong to each category.
# This helps understand inventory distribution.
# ==================================================

print("\n" + "=" * 50)
print("PRODUCT COUNT BY CATEGORY")
print("=" * 50)

category_counts = df["Category"].value_counts()

print(category_counts)


# ==================================================
# EDA 2 : TOP 10 PRODUCTS BY MRP
# Sort products by Maximum Retail Price (MRP) in
# descending order and display the 10 most expensive
# products.
# ==================================================

print("\n" + "=" * 50)
print("TOP 10 PRODUCTS BY MRP")
print("=" * 50)

top_mrp_products = df.sort_values(
    by="mrp",
    ascending=False
).head(10)

print(top_mrp_products[["name", "Category", "mrp"]])


# ==================================================
# EDA 3 : OUT OF STOCK PRODUCTS BY CATEGORY
# Filter only out-of-stock products, group them by
# category, count the number of products in each
# category and sort the result in descending order.
# ==================================================

print("\n" + "=" * 50)
print("OUT OF STOCK PRODUCTS BY CATEGORY")
print("=" * 50)

out_of_stock = df[df["outOfStock"] == True]

out_of_stock_count = out_of_stock.groupby("Category").size()

print(out_of_stock_count.sort_values(ascending=False))

# ==================================================
# EDA 4 : OUT OF STOCK PERCENTAGE BY CATEGORY
# Calculate the percentage of out-of-stock products
# in each category.
#
# Formula:
# (Out-of-Stock Products / Total Products in Category) × 100
#
# This helps identify which categories are facing
# the highest stock shortage relative to their total
# inventory, making comparison fair across categories.
# ==================================================

print("\n" + "=" * 50)
print("OUT OF STOCK PERCENTAGE BY CATEGORY")
print("=" * 50)

out_of_stock_percentage = (
    out_of_stock_count / category_counts
) * 100

print(out_of_stock_percentage)



# ==================================================
# EDA 5 : AVERAGE MRP BY CATEGORY
# Calculate the average Maximum Retail Price (MRP)
# for each product category.
#
# This helps identify which categories are generally
# more expensive and which are more affordable.
# ==================================================

print("\n" + "=" * 50)
print("AVERAGE MRP BY CATEGORY")
print("=" * 50)

average_mrp = (
    df.groupby("Category")["mrp"]
      .mean()
      .round(2)
      .sort_values(ascending=False)
)

print(average_mrp)










# ==================================================
# EDA 6 : AVERAGE SELLING PRICE BY CATEGORY
# Calculate the average discounted selling price for
# each category.
#
# This helps understand the actual average price
# customers pay after discounts.
# ==================================================

print("\n" + "=" * 50)
print("AVERAGE SELLING PRICE BY CATEGORY")
print("=" * 50)

average_selling_price = (
    df.groupby("Category")["discountedSellingPrice"]
      .mean()
      .round(2)
      .sort_values(ascending=False)
)

print(average_selling_price)



