print("\n" + "=" * 50)
print("TOP 10 PRODUCTS BY MRP")
print("=" * 50)

top_mrp_products = df.sort_values(
    by="mrp",
    ascending=False
).head(10)

print(top_mrp_products[["name", "Category", "mrp"]])