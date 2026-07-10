print("\n" + "=" * 50)
print("OUT OF STOCK PRODUCTS BY CATEGORY")
print("=" * 50)

out_of_stock = df[df["outOfStock"] == True]

out_of_stock_count = out_of_stock.groupby("Category").size()

print(out_of_stock_count.sort_values(ascending=False))