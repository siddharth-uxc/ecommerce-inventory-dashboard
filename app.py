import pandas as pd

df = pd.read_csv("data/zepto_v2.csv", encoding="latin1")


print(df.head())
print("\nshape:", df.shape)
print("\ncolumns:", df.columns)
print("\ninfo:")
print(df.info())