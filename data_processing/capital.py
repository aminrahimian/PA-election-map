import csv

def capitalize_words(csv_file):
    rows = []

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            new_row = []
            for i, value in enumerate(row):
                if i < 3:
                    # Keep the first letter of each word in the first three columns capitalized and the rest lowercase
                    new_value = ' '.join([word.capitalize() for word in value.split()])
                else:
                    new_value = value
                new_row.append(new_value)
            rows.append(new_row)

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

# Specifies the path to the CSV file
csv_file_path = 'data0.csv'

# Capitalize the first letter of the data in the first three columns
capitalize_words(csv_file_path)
