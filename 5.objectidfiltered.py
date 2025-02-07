import pandas as pd

# Load datasets
shootings = pd.read_csv("filtered_shootings.csv")
incidents_crimes = pd.read_csv("filtered_incidents_crimes.csv")

# Rename location_block to location
incidents_crimes.rename(columns={"location_block": "location"}, inplace=True)

# Drop rows with missing values in "objectid"
shootings = shootings.dropna(subset=["objectid"])
incidents_crimes = incidents_crimes.dropna(subset=["objectid"])

# Merge based on objectid
matching_rows = shootings.merge(incidents_crimes, on="objectid", how="inner", suffixes=("_x", "_y"))

# Save results
matching_rows.to_csv("1.1.objectid_matching.csv", index=False)

print("Comparison by 'objectid' completed. Results saved in '1.1.objectid_matching.csv'.")