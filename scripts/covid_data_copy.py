import pandas as pd

df = pd.read_csv("covid19_data.csv")

print(df.head())  # shows first 5 rows
print(df.columns)  # shows column names
print(df.info())  # shows data types & missing values
