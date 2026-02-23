import pandas as pd

# Create a small dataset
data = {
    "Name": ["Samson", "Ada", "Tunde", "Aisha"],
    "Role": ["DevOps", "Backend", "Frontend", "Data"],
    "Experience_Years": [2, 3, 1, 4]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the data
print("\n📊 Team Data:")
print(df)

# Basic analysis
print("\n📈 Average Experience:")
print(df["Experience_Years"].mean())
