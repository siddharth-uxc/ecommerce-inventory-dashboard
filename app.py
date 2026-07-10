import pandas as pd

# Load dataset
df = pd.read_csv("data/zepto_cleaned.csv")

print(df.head())

print("\nShape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nInfo:")
df.info()

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

rows_before = df.shape[0]
print(f"Rows before cleaning: {rows_before}")

df= df.drop_duplicates()

rows_after = df.shape[0]
print(f"Rows after cleaning: {rows_after}")

duplicates_removed = rows_before - rows_after
print(f"Duplicates removed: {duplicates_removed}")

df.to_csv("data/zepto_cleaned.csv", index=False)

print("\n" + "=" * 50)
print("Product count by category")
print("=" * 50)
 
category_counts = df["Category"].value_counts()
print(category_counts)



print("\n" + "=" * 50)
print("TOP 10 PRODUCTS BY MRP")
print("=" * 50)

top_mrp_products = df.sort_values(
    by="mrp",
    ascending=False
).head(10)

print(top_mrp_products[["name", "Category", "mrp"]])


print("\n" + "=" * 50)
print("OUT OF STOCK PRODUCTS BY CATEGORY")
print("=" * 50)

out_of_stock = df[df["outOfStock"] == True]

out_of_stock_count = out_of_stock.groupby("Category").size()

print(out_of_stock_count.sort_values(ascending=False))