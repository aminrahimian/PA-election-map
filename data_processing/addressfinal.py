import os
import pandas as pd

# Define input folder path and output folder path
# where to find original data \"https://www.pavoterservices.pa.gov/Pages/PurchasePAFULLVoterExport.aspx?ID=%20PA_EXPORT_8454847762230114235637&Langcode=%20en-US\
# save the original data csv in input folder
input_folder = "input_folder"  # Input folder path
output_folder = "output_folder"  # Output folder path

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

#Get all CSV files in the input folder
csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]

# Iterate over each CSV file for processing
for csv_file in csv_files:
    #  Build the complete path of the input file
    input_file = os.path.join(input_folder, csv_file)

    #  Read the original CSV file
    df = pd.read_csv(input_file, encoding='latin1')

    # Perform specific operations, such as modifying column names, adding new columns, etc.
    df["Street Name"] = df["Street Name"].apply(lambda x: x.title())
    df["Address Line 2"] = df["Address Line 2"].apply(lambda x: x.title())
    df["City"] = df["City"].apply(lambda x: x.title())
    df["Address"] = df["House Number"].astype(str) + ' ' + df["Street Name"].astype(str) + ',' + df["City"].astype(
        str) + ',' + df["State"].astype(str) + ',' + df["Zip"].astype(str) + ',USA'
    df["Address"] = df["Address"].str.replace('"', '')

    #Define the list of column names to export
    column_names = ["ID Number", "Address", "Party Code", "Zip","Last Vote Date"]

 # Get the DataFrame object with the specified columns
    exported_df = df[column_names]

    #  Build the complete path of the output file
    output_file = os.path.join(output_folder, os.path.splitext(csv_file)[0] + "_party.csv")

    # Export the DataFrame object as a new CSV file
    exported_df.to_csv(output_file, index=False)

    print(f"Processed {csv_file} and saved processed data to {output_file}")
    
