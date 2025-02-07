import pandas as pd

# Load datasets
shootings = pd.read_csv("filtered_shootings.csv")
incidents_crimes = pd.read_csv("filtered_incidents_crimes.csv")

# Rename location_block to location
incidents_crimes.rename(columns={"location_block": "location"}, inplace=True)

# Drop rows with missing values in "lat" and "lng"
shootings = shootings.dropna(subset=["lat", "lng"])
incidents_crimes = incidents_crimes.dropna(subset=["lat", "lng"])

# Merge based on lat and lng
matching_rows = shootings.merge(incidents_crimes, on=["lat", "lng"], how="inner", suffixes=("_x", "_y"))

# Save results
matching_rows.to_csv("1.7.lat_lng_matching.csv", index=False)

print("Comparison by 'lat' and 'lng' completed. Results saved in '1.7.lat_lng_matching.csv'.")