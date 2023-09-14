import csv

def add_header(csv_file, header):
    with open(csv_file, 'r') as file:
        lines = file.readlines()

    lines.insert(0, header + '\n')

    with open(csv_file, 'w', newline='') as file:
        file.writelines(lines)

#Specifies the path to the CSV file
csv_file_path = 'data52.csv'

# Specifies the header to add
header = 'name,address,zipcode'

# Add header to CSV file
add_header(csv_file_path, header)
