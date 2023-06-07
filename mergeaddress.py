import csv

def merge_columns(csv_file):
    rows = []

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            new_row = row[:1]  #  Keep the data in the first column

            merged_value = ','.join(row[1:4])  # Merge the data from column 2 to column 4, separated by commas
            new_row.append(merged_value)

            new_row.extend(row[4:])  # Add the data from column 5 onwards

            rows.append(new_row)

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

# Specify the path of the CSV file
csv_file_path = 'data0.csv'

# Merge columns 2 to 4, separated by commas
merge_columns(csv_file_path)
