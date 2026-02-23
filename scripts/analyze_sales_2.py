import pandas as pd

# Load dat
df = pd.read_csv("sales.csv")

print("\n📊 Raw Data:")
print(df)

# Filter: only Laptop sales
laptop_sales = df[df["product"] == "Laptop"]

print("\n💻 Laptop Sales Only:")
print(laptop_sales)

# Group by region and sum revenue
summary = (
    laptop_sales
    .groupby("region")["amount"]
    .sum()
    .reset_index()
)

print("\n📈 Revenue by Region (Laptops):")
print(summary)

# Export results
summary.to_csv("sales_by_region.csv", index=False)

print("\n✅ File exported: sales_by_region.csv")
