import csv
import math
import os

def haversine_distance(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Apply haversine formula to calculate distance
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    radius = 6371  # Earth's average radius in kilometers
    distance = radius * c

    return distance

def find_nearest_location(csv_folder_path, csv2_file_path, output_folder_path):
    # Create the output folder
    os.makedirs(output_folder_path, exist_ok=True)

    # Get all CSV files in the specified folder
    csv_files = [file for file in os.listdir(csv_folder_path) if file.endswith('.csv')]

    with open(csv2_file_path, 'r') as file2:
        reader2 = csv.reader(file2)
        csv2_data = list(reader2)

    for csv_file in csv_files:
        csv1_file_path = os.path.join(csv_folder_path, csv_file)

        with open(csv1_file_path, 'r') as file1:
            reader1 = csv.reader(file1)
            csv1_data = list(reader1)

        results = []

        # Add column names to the results list
        header = csv1_data[0][:3] + ["Latitude", "Longitude", "Distance"]
        results.append(header)

        lat_lon_index_csv1 = []
        lat_lon_index_csv2 = []

        # Find the index of the 'Latitude' and 'Longitude' columns in the first file
        for idx, column in enumerate(csv1_data[0]):
            if column.lower() == "latitude" or column.lower() == "longitude":
                lat_lon_index_csv1.append(idx)

        # Find the index of the 'Latitude' and 'Longitude' columns in the second file
        for idx, column in enumerate(csv2_data[0]):
            if column.lower() == "latitude" or column.lower() == "longitude":
                lat_lon_index_csv2.append(idx)

        for row1 in csv1_data[1:]:  # Skip the header row
            if len(row1) >= 4:  # Ensure there are enough columns in the row
                try:
                    lat1, lon1 = [float(row1[i]) for i in lat_lon_index_csv1]
                    min_distance = float('inf')
                    nearest_location = None

                    for row2 in csv2_data[1:]:  # Skip the header row
                        if len(row2) >= 4:  # Ensure there are enough columns in the row
                            try:
                                lat2, lon2 = [float(row2[i]) for i in lat_lon_index_csv2]
                                distance = haversine_distance(lat1, lon1, lat2, lon2)
                                if distance < min_distance:
                                    min_distance = distance
                                    nearest_location = row2
                            except (ValueError, IndexError):
                                continue

                    if nearest_location is not None:
                        result = row1[:3] + [nearest_location[i] for i in lat_lon_index_csv2] + [min_distance]
                        results.append(result)

                except (ValueError, IndexError):
                    continue

        # Save the results to a new CSV file with the same name as the original CSV file
        output_file = os.path.join(output_folder_path, csv_file)

        with open(output_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(results)

        print(f"Results saved to file: {output_file}")


# Specify the folder path containing CSV files
csv_folder_path = "E:\python\PA"
csv2_file_path = "E:\python\merged_file.csv"
output_folder_path = "E:\python\distance"  # Customize the output folder path

# Find the nearest latitude and longitude for each latitude-longitude pair in the first CSV file
# and save the results to new CSV files
find_nearest_location(csv_folder_path, csv2_file_path, output_folder_path)
