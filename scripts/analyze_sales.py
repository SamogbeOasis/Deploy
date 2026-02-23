import pandas as pd

# Load CSV
df = pd.read_csv("sales.csv")

# Basic inspection
print("=== First rows ===")
print(df.head())

print("\n=== Summary ===")
print(df.describe())

# Total sales by product
print("\n=== Total sales by product ===")
sales_by_product = df.groupby("product")["amount"].sum()
print(sales_by_product)

# Sales by region
print("\n=== Sales by region ===")
sales_by_region = df.groupby("region")["amount"].sum()
print(sales_by_region)

# Highest single sale
print("\n=== Highest sale ===")
print(df.loc[df["amount"].idxmax()])

# Filter West region
print("\n=== West region only ===")
print(df[df["region"] == "West"])

print("End Here")
