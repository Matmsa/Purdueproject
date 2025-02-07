import pandas as pd

# Load the CSV file
filepath = "incidents_part1_part2.csv"
df = pd.read_csv(filepath)

# List of crime types to filter
crime_types = [
    "Thefts",
    "Rape",
    "Aggravated Assault Firearm",
    "Theft from Vehicle",
    "Robbery Firearm",
    "Burglary Residential",
    "Burglary Non-Residential",
    "Homicide - Criminal",
    "All Other Offenses",
    "Other Assaults",
    "Narcotic / Drug Law Violations",
    "Other Sex Offenses (Not Commercialized)",
    "Weapon Violations",
    "Motor Vehicle Theft"
]

# Filter the data based on the specified crime types
filtered_df = df[df['text_general_code'].isin(crime_types)]

# Save the filtered data to a new CSV file
filtered_df.to_csv("filtered_crimes.csv", index=False)

# Show
print("Dataset filtered!")