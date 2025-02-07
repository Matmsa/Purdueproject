import pandas as pd

# Load datasets
shootings = pd.read_csv("filtered_shootings.csv")
incidents_crimes = pd.read_csv("filtered_incidents_crimes.csv")

# Rename location_block to location
incidents_crimes.rename(columns={"location_block": "location"}, inplace=True)

# Drop rows with missing values in "point_x" and "point_y"
shootings = shootings.dropna(subset=["point_x", "point_y"])
incidents_crimes = incidents_crimes.dropna(subset=["point_x", "point_y"])

# Merge based on point_x and point_y
matching_rows = shootings.merge(incidents_crimes, on=["point_x", "point_y"], how="inner", suffixes=("_x", "_y"))

# Save results
matching_rows.to_csv("1.6.point_x_point_y_matching.csv", index=False)

print("Comparison by 'point_x' and 'point_y' completed. Results saved in '1.6.point_x_point_y_matching.csv'.")