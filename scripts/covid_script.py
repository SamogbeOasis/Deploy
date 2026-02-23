import pandas as pd

# Read CSV
df = pd.read_csv("covid-19.csv")

# Inspect
print(df.head())
print(df.info())
print(df.describe())
print(df.Nationality())
print(df.Names())
