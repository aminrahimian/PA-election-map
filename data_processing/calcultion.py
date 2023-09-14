import os
import pandas as pd
import numpy as np

# Folder path
folder_path = 'E:\python\distance'

# Get all CSV files in the folder
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# Create an empty list to store the results
result_data = []

# Iterate through CSV files
for file in csv_files:
    file_path = os.path.join(folder_path, file)
    
    # Read the CSV file
    data = pd.read_csv(file_path)
    
    # Calculate mean, max, min, and variance of the 'Distance' column
    mean_distance = data['Distance'].mean()
    max_distance = data['Distance'].max()
    min_distance = data['Distance'].min()
    variance = data['Distance'].var()
    
    # Get the file name (remove the file extension)
    file_name = os.path.splitext(file)[0]
      
    # Append the results to the result list
    result_data.append({'County': file_name, 'Mean Distance': mean_distance,
                        'Max Distance': max_distance, 'Min Distance': min_distance,
                        'Variance': variance})

# Convert the results into a DataFrame
result_df = pd.DataFrame(result_data)

# Save the results to a new CSV file
result_file_path = 'result111.csv'
result_df.to_csv(result_file_path, index=False)
