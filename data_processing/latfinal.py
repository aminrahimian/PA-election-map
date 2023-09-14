import os
import requests
import json
import csv
import pandas as pd
from tqdm import tqdm

data = pd.read_csv('add1.csv')


file_name = os.path.splitext('add1.csv')[0]

output_file = f'{file_name}_lat.csv'

data['Latitude'] = ''
data['Longitude'] = ''

for index, row in tqdm(data.iterrows(), total=len(data)):

    address = row['Address']
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key=AIzaSyDOYNHx20lr_3J7c4VKa0lnrAmSmAbd_M8"
    response = requests.get(url)
    result = json.loads(response.text)

    try:
 
        lat = result["results"][0]["geometry"]["location"]["lat"]
        lng = result["results"][0]["geometry"]["location"]["lng"]

    except (IndexError, KeyError):

        lat = ''
        lng = ''
        print(f"Error: {address}")


    data.at[index, 'Latitude'] = lat
    data.at[index, 'Longitude'] = lng