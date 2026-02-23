import pandas as pd

# Create sample dataset
data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 35, 40],
    "salary": [50000, 60000, 70000, 80000]
}

df = pd.DataFrame(data)

print("Full Data:")
print(df)

print("\nAverage Salary:")
print(df["salary"].mean())
print("\nHigh Earners (>60000):")
print(df[df["salary"] > 60000])
