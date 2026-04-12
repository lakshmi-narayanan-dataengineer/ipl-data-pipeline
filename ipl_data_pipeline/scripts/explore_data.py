import pandas as pd

# Load the data
matches = pd.read_csv(r"D:\IPL End to End Data Analysis Pipeline Project\ipl_data_pipeline\data\extracted\matches.csv")
deliveries = pd.read_csv(r"D:\IPL End to End Data Analysis Pipeline Project\ipl_data_pipeline\data\extracted\deliveries.csv")

# First look
print("Shape of matches data:")
print(matches.shape)

print("\nShape of deliveries data:")
print(deliveries.shape)

print("\nFirst 5 rows of matches:")
print(matches.head())

print("\nColumn names:")
print(matches.columns.tolist())