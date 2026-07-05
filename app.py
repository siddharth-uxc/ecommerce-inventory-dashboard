import pandas as pd

# Load dataset
df = pd.read_csv("data/zepto_v2.csv", encoding="latin1")

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