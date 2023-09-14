# PA-election-map

PA's map of election security and information integrity

This project provides python scripts to find and clean the data of voters and polling stations and draw different types of map to show how the accessibility of polling stations varies across different  demographics

## Getting started

### software

  + Python 3.11.1 [download](https://www.python.org/downloads/)
  
  + Google Geocoding API [source](https://developers.google.com/maps/documentation/geocoding/start)
  
  + Chromedriver [download](https://sites.google.com/chromium.org/driver/?pli=1)


## Methods:

### Data-Processing

  + Random Sampling :
     - [select voters from 2022](https://github.com/aminrahimian/PA-election-map/blob/main/data_processing/voter2022.py)
     - [randomly select 10% for each county](https://github.com/aminrahimian/PA-election-map/blob/main/data_processing/select2022.py)
      
  + Get Longitude and Latitude for each address
     - [let original address can be recoginized by Google](https://github.com/aminrahimian/PA-election-map/blob/main/data_processing/addressfinal.py)
     - [Get Longtitude and Latitude](https://github.com/aminrahimian/PA-election-map/blob/main/data_processing/addressfinal.py)

  + polling station
    
     - [get polling station in order](https://github.com/aminrahimian/PA-election-map/blob/main/data_collection/get_polling_station_in_order.py)
     - [get randomly](https://github.com/aminrahimian/PA-election-map/blob/main/data_collection/get_polling_station_randomly.py)
     - polling station will be save as a .txt file and for futher process we need to convert it into .csv file. [code here](https://github.com/aminrahimian/PA-election-map/blob/main/data_processing/txt2csv.py)
     - [remove repeat result](https://github.com/aminrahimian/PA-election-map/blob/main/data_processing/removerepeat.py)
     - [add column title](https://github.com/aminrahimian/PA-election-map/blob/main/data_processing/title.py)

  + Mean distance between voters and polling stations
     - [calculate distance between voters and polling stations](https://github.com/aminrahimian/PA-election-map/blob/main/data_processing/distance.py)
     - [calculate mean distance](https://github.com/aminrahimian/PA-election-map/blob/main/data_processing/calcultion.py)

### Data-Visualization

  + [Map Voters](https://github.com/aminrahimian/PA-election-map/blob/main/map/mapPA.py)
    - [result sample](https://github.com/aminrahimian/PA-election-map/blob/main/map/PAmapCounty.png)

  + [Map polling stations](https://github.com/aminrahimian/PA-election-map/blob/main/map/code/maponlypollingstation.py)
     - [result sample](https://github.com/aminrahimian/PA-election-map/blob/main/map/PAmap_PollingStation.png)
    

  + [heatmap](https://github.com/aminrahimian/PA-election-map/blob/main/map/code/heatmap.py)
      - [result sample](https://github.com/aminrahimian/PA-election-map/blob/main/map/heatmap.png)
