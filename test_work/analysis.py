import pandas as pd

df = pd.read_csv("trade.csv")

print(df)
print("\nTotal Revenue Per Row:")
df["revenue"] = df["price"] * df["quantity"]
print(df)

print("\nTotal Revenue:", df["revenue"].sum())

print("\nPhone Sales:")
print(df[df["product"] == "Phone"])

print("\nRevenue by Product:")
print(df.groupby("product")["revenue"].sum())
