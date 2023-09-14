import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import contextily

# Define the folder path where CSV files are located
folder_path = 'E:\python\PA'

# Create an empty DataFrame to store all the data
all_data = pd.DataFrame()

# Read all CSV files in the folder and merge the data
for file_name in os.listdir(folder_path):
    if file_name.endswith(".csv"):
       
        file_path = os.path.join(folder_path, file_name)
        
        voter_data = pd.read_csv(file_path)
        
        all_data = pd.concat([all_data, voter_data], ignore_index=True)

#Set seaborn style and plot size
sns.set(style="ticks", color_codes=True)
plt.figure(figsize=(200, 200))

#read border (choose the needed one)
#website to download data 
#congressional: https://www.pasda.psu.edu/uci/DataSummary.aspx?dataset=38  
#county: https://www.pasda.psu.edu/uci/DataSummary.aspx?dataset=24 
#senate: https://data-pennshare.opendata.arcgis.com/datasets/PennShare::pennsylvania-senate-districts/about
#county_boundary = gpd.read_file("yourfilepath") 
#congressional_boundary = gpd.read_file("yourfilepath")
#senate_boundary = gpd.read_file("yourfilepath")

#Set seaborn style and plot size
# Create a jointplot with longitude and latitude as axes, Party Code as hue
joint_grid = sns.jointplot(x="Longitude", y="Latitude", data=all_data, hue="Party Code", palette={"D": "blue", "R": "red", "Other": "black"}, kind="scatter", s=0.02)
ax = joint_grid.ax_joint
# Set limits for the axes
plt.xlim([-81, -74.5])
plt.ylim([39, 42.5])

# Use contextily to add a basemap
contextily.add_basemap(ax, crs="EPSG:4326", source=contextily.providers.CartoDB.PositronNoLabels, attribution=False,zoom=12)

#plot border (choose the needed one)
#congressional_boundary.plot(ax=ax, edgecolor='choose color', linewidth=0.15, facecolor='none')
#county_boundary.plot(ax=ax, edgecolor='choose color', linewidth=0.15, facecolor='none')
#senate_boundary.plot(ax=ax, edgecolor='choose color', linewidth=0.15, facecolor='none')

#plot the title
plt.text(0.5, -0.3, "PA voter map (Congressional/county/senate)", ha='center', va='bottom', fontsize=12, fontweight='bold', transform=plt.gca().transAxes)
# save png
ax.legend(fontsize='xx-small')
plt.savefig("PAmap", dpi=3200)
plt.close()  
