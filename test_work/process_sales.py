import pandas as pd
import boto3
from io import StringIO

# AWS S3 client
s3 = boto3.client('s3')

bucket = "samson-tf-audit-bucket"
input_key = "sales.csv"
output_key = "processed_sales.csv"

# Read CSV from S3
obj = s3.get_object(Bucket=bucket, Key=input_key)
df = pd.read_csv(obj['Body'])

# --- Practical Data Cleaning ---
# Fill missing values
df["amount"] = df["amount"].fillna(0)
df["region"] = df["region"].fillna("Unknown")

# Filter sales above 1000
df = df[df["amount"] > 1000]

# Sort by date
df = df.sort_values(by="date")

# --- Save back to S3 ---
csv_buffer = StringIO()
df.to_csv(csv_buffer, index=False)
s3.put_object(Bucket=bucket, Key=output_key, Body=csv_buffer.getvalue())

print("Processing complete. Saved to:", output_key)
