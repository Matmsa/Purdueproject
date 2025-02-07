import pandas as pd

# Load datasets
shootings = pd.read_csv("filtered_shootings.csv")
incidents_crimes = pd.read_csv("filtered_incidents_crimes.csv")

# Rename location_block to location
incidents_crimes.rename(columns={"location_block": "location"}, inplace=True)

# Drop rows with missing values in "the_geom"
shootings = shootings.dropna(subset=["the_geom"])
incidents_crimes = incidents_crimes.dropna(subset=["the_geom"])

# Merge based on the_geom
matching_rows = shootings.merge(incidents_crimes, on="the_geom", how="inner", suffixes=("_x", "_y"))

# Save results
matching_rows.to_csv("1.2.the_geom_matching.csv", index=False)

print("Comparison by 'the_geom' completed. Results saved in '1.2.the_geom_matching.csv'.")