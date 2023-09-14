import csv

def txt_to_csv(txt_file, csv_file):
    with open(txt_file, 'r') as file:
        lines = file.readlines()

    max_columns = max(len(line.strip().split(',')) for line in lines)

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        for line in lines:
            values = line.strip().split(',')
            # 如果列数不足，补充空白值
            if len(values) < max_columns:
                values.extend([''] * (max_columns - len(values)))
            writer.writerow(values)

def sort_csv_by_city(csv_file):
    with open(csv_file, 'r') as file:
        lines = file.readlines()

    sorted_lines = sorted(lines[1:], key=lambda x: x.strip().split(',')[-3].lower()) 
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(lines[0].strip().split(','))
        for line in sorted_lines:
            writer.writerow(line.strip().split(','))


txt_file_path = "data_51.txt"
csv_file_path = 'data51.csv'

# Write each line of the text file into a CSV file
txt_to_csv(txt_file_path, csv_file_path)
# Sort the CSV file by the first letter of the city name
sort_csv_by_city(csv_file_path)
