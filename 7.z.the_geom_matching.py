import pandas as pd

# Load the matching CSV file
df = pd.read_csv("1.3.the_geom_webmercator_matching.csv")

# Identify column pairs (_x and _y)
columns_to_compare = ["the_geom", "the_geom_webmercator", "objectid", "dc_key", 
                      "location", "point_x", "point_y", "lat", "lng"]

# Create a new DataFrame to store only the matching values
filtered_df = pd.DataFrame()

# Iterate over each column pair and keep only matching values
for col in columns_to_compare:
    col_x, col_y = f"{col}_x", f"{col}_y"
    
    if col_x in df.columns and col_y in df.columns:
        # Create a new column that keeps the value only if _x and _y are equal
        filtered_df[col] = df[col_x].where(df[col_x] == df[col_y])

# Add a column to keep track of the original index
filtered_df["original_index"] = df.index  

# Save the new DataFrame
filtered_df.to_csv("1.3.z.the_geom_webmercator_matching_filtered.csv", index=False)

print("Filtered CSV saved with only matching columns for each row!")