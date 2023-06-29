import os
import pandas as pd

# Define input folder path and output folder path
input_folder = "input_folder"  # Input folder path
output_folder = "output_folder"  #Output folder path

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Get all CSV files in the input folder
csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]

# Process each CSV file
for csv_file in csv_files:
    # Build the input file's full path
    input_file = os.path.join(input_folder, csv_file)

    # Read the original CSV file
    df = pd.read_csv(input_file)

    # Filter the data based on the condition (Last Vote Date contains "2022")
    extracted_data = df[df['Last Vote Date'].str.contains('2022', na=False)]

    # Build the output file's full path
    output_file = os.path.join(output_folder, os.path.splitext(csv_file)[0] + "_2022.csv")

    # Save the sampled data as a new CSV file
    extracted_data.to_csv(output_file, index=False)

    print(f"Processed {csv_file} and saved extracted data to {output_file}")
