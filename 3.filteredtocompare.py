import pandas as pd

# File paths (update these to match your files)
shootings_path = "shootings.csv"  # Path to shooting victims dataset
incidents_crimes_path = "filtered_crimes.csv"  # Path to incidents crimes dataset

# Columns to keep for each dataset
shootings_columns_to_keep = [
    "the_geom", "the_geom_webmercator", "objectid", "dc_key",
    "location", "point_x", "point_y", "lat", "lng"
]

incidents_columns_to_keep = [
    "the_geom", "the_geom_webmercator", "objectid", "dc_key",
    "location_block", "point_x", "point_y", "lat", "lng"
]

# Filter shooting victims dataset
shootings = pd.read_csv(shootings_path)
filtered_shootings = shootings[shootings_columns_to_keep]
filtered_shootings.to_csv("filtered_shootings.csv", index=False)
print("Filtered shootings dataset saved as 'filtered_shootings.csv'.")

# Filter incidents crimes dataset
incidents_crimes = pd.read_csv(incidents_crimes_path)
filtered_incidents_crimes = incidents_crimes[incidents_columns_to_keep]
filtered_incidents_crimes.to_csv("filtered_incidents_crimes.csv", index=False)
print("Filtered incidents crimes dataset saved as 'filtered_incidents_crimes.csv'.")
