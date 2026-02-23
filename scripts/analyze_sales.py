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

# Best selling region
print("\n=== Sales by region ===")
sales_by_region = df.groupby("region")["amount"].sum()
print(sales_by_region)

#Find the highest single sale
print(df.loc[df["amount"].idxmax()])

#Filter only West region
print(df[df["region"] == "West"])

print("End Here: next script")


import pandas as pd

# Load CSV
df = pd.read_csv("sales.csv")

# Total sales by product
sales_by_product = (
    df.groupby("product", as_index=False)["amount"].sum()
)

# Total sales by region
sales_by_region = (
    df.groupby("region", as_index=False)["amount"].sum()
)

# Save results
sales_by_product.to_csv("sales_by_product.csv", index=False)
sales_by_region.to_csv("sales_by_region.csv", index=False)

print("✅ Analysis complete.")
print("Generated:")
print("- sales_by_product.csv")
print("- sales_by_region.csv")
