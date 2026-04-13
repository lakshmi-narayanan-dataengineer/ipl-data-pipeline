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

# Fix 4: Convert date from text to real date
matches['date'] = pd.to_datetime(matches['date'])

# Fix 5: Fill missing result_margin with 0
matches['result_margin'] = matches['result_margin'].fillna(0)

print("\nAfter cleaning:")
print(f"Missing city values: {matches['city'].isnull().sum()}")
print(f"Missing method values: {matches['method'].isnull().sum()}")
print(f"Missing winner values: {matches['winner'].isnull().sum()}")

# Check date column is fixed
print("\nDate column type now:")
print(matches['date'].dtype)

# Save the cleaned data as a new file
matches.to_csv("../data/matches_cleaned.csv", index=False)

print("\n Cleaned data saved to data/matches_cleaned.csv!")