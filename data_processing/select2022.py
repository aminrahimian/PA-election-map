import os
import pandas as pd
import random

# Define input folder path and output folder path
input_folder = "input_folder"  # Input folder path
output_folder = "output_folder"  #Output folder path

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Get all CSV files in the input folder
csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]

#Process each CSV file
for csv_file in csv_files:
    # Build the input file's full path
    input_file = os.path.join(input_folder, csv_file)

    # Read the original CSV file
    df = pd.read_csv(input_file)

    # Calculate the number of rows to sample (10%)
    num_rows = int(df.shape[0] * 0.1)

    # Randomly sample the specified number of rows
    sampled_data = df.sample(n=num_rows)

    # Build the output file's full path
    output_file = os.path.join(output_folder, csv_file)

    # Save the sampled data as a new CSV file

    sampled_data.to_csv(output_file, index=False)

    print(f"Processed {csv_file} and saved sampled data to {output_file}")
