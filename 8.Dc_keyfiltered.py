import pandas as pd

# Load datasets
shootings = pd.read_csv("filtered_shootings.csv")
incidents_crimes = pd.read_csv("filtered_incidents_crimes.csv")

# Rename location_block to location
incidents_crimes.rename(columns={"location_block": "location"}, inplace=True)

# Drop rows with missing values in "dc_key"
shootings = shootings.dropna(subset=["dc_key"])
incidents_crimes = incidents_crimes.dropna(subset=["dc_key"])

# Merge based on dc_key
matching_rows = shootings.merge(incidents_crimes, on="dc_key", how="inner", suffixes=("_x", "_y"))

# Save results
matching_rows.to_csv("1.4.dc_key_matching.csv", index=False)

print("Comparison by 'dc_key' completed. Results saved in '1.4.dc_key_matching.csv'.")