import pandas as pd

# Load data
matches = pd.read_csv(r"D:\IPL End to End Data Analysis Pipeline Project\ipl_data_pipeline\data\extracted\matches.csv")

print("Before cleaning:")
print(f"Missing city values: {matches['city'].isnull().sum()}")
print(f"Missing method values: {matches['method'].isnull().sum()}")
print(f"Missing winner values: {matches['winner'].isnull().sum()}")

# Fix 1: Fill missing city with Unknown
matches['city'] = matches['city'].fillna("Unknown")

# Fix 2: Fill missing method with Normal
matches['method'] = matches['method'].fillna("Normal")

# Fix 3: Fill missing winner with No Result
matches['winner'] = matches['winner'].fillna("No Result")

print("\nAfter cleaning:")
print(f"Missing city values: {matches['city'].isnull().sum()}")
print(f"Missing method values: {matches['method'].isnull().sum()}")
print(f"Missing winner values: {matches['winner'].isnull().sum()}")