import pandas as pd

# Load datasets
print("Loading datasets...")
shootings = pd.read_csv("filtered_shootings.csv")
incidents_crimes = pd.read_csv("filtered_incidents_crimes.csv")
print("Datasets loaded successfully.")

# Rename "location_block" in incidents_crimes to "location"
if "location_block" in incidents_crimes.columns:
    print("Renaming 'location_block' to 'location' for consistency...")
    incidents_crimes.rename(columns={"location_block": "location"}, inplace=True)

# Identify common columns
common_columns = list(set(shootings.columns) & set(incidents_crimes.columns))
print(f"Common columns for comparison: {common_columns}")

# Ensure column names and data types match
for col in common_columns:
    shootings[col] = shootings[col].astype(str).str.strip()
    incidents_crimes[col] = incidents_crimes[col].astype(str).str.strip()

# Perform merge on all common columns
matching_rows = shootings.merge(incidents_crimes, on=common_columns, how="inner")

# Find non-matching rows
shootings_non_matching = shootings[~shootings.index.isin(matching_rows.index)]
incidents_crimes_non_matching = incidents_crimes[~incidents_crimes.index.isin(matching_rows.index)]

# Debugging: Print dataset sizes
print(f"Total rows in shootings: {len(shootings)}")
print(f"Total rows in shootings_non_matching: {len(shootings_non_matching)}")
print(f"Total rows in incidents_crimes: {len(incidents_crimes)}")
print(f"Total rows in incidents_crimes_non_matching: {len(incidents_crimes_non_matching)}")

# Save results to CSV
print("Saving results to CSV files...")
matching_rows.to_csv("matching_rows.csv", index=False)
shootings_non_matching.to_csv("shootings_non_matching.csv", index=False)
incidents_crimes_non_matching.to_csv("incidents_crimes_non_matching.csv", index=False)

print("Comparison complete. Results saved as:")
print(" - 'matching_rows.csv'")
print(" - 'shootings_non_matching.csv'")
print(" - 'incidents_crimes_non_matching.csv'")

# Validate results
filtered_shootings = pd.read_csv("filtered_shootings.csv")
filtered_incidents_crimes = pd.read_csv("filtered_incidents_crimes.csv")

if shootings_non_matching.equals(filtered_shootings):
    print("The file 'shootings_non_matching.csv' is identical to 'filtered_shootings.csv'.")
else:
    print("The file 'shootings_non_matching.csv' is NOT identical to 'filtered_shootings.csv'.")

if incidents_crimes_non_matching.equals(filtered_incidents_crimes):
    print("The file 'incidents_crimes_non_matching.csv' is identical to 'filtered_incidents_crimes.csv'.")
else:
    print("The file 'incidents_crimes_non_matching.csv' is NOT identical to 'filtered_incidents_crimes.csv'.")

print(" - 'incidents_crimes_non_matching.csv'")

# Validate results
filtered_shootings = pd.read_csv("filtered_shootings.csv")
filtered_incidents_crimes = pd.read_csv("filtered_incidents_crimes.csv")

if shootings_non_matching.equals(filtered_shootings):
    print("The file 'shootings_non_matching.csv' is identical to 'filtered_shootings.csv'.")
else:
    print("The file 'shootings_non_matching.csv' is NOT identical to 'filtered_shootings.csv'.")

if incidents_crimes_non_matching.equals(filtered_incidents_crimes):
    print("The file 'incidents_crimes_non_matching.csv' is identical to 'filtered_incidents_crimes.csv'.")
else:
    print("The file 'incidents_crimes_non_matching.csv' is NOT identical to 'filtered_incidents_crimes.csv'.")