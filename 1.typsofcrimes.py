import pandas as pd

# Path CSV file
file_path = 'incidents_part1_part2.csv'

# Reading file
data = pd.read_csv(file_path)

# Analyse unique typs of crimes
unique_crime_types = data['text_general_code'].unique()

# Show unique types of crimes
print("Tipos únicos de crimes:")
for crime in unique_crime_types:
    print(crime)
