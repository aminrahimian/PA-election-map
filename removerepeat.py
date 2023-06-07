import csv

def remove_duplicates(csv_file):
    rows = []
    seen = set()

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            key = tuple(row)

            if key not in seen:
                rows.append(row)
                seen.add(key)

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

csv_file_path = 'data0.csv'

remove_duplicates(csv_file_path)
