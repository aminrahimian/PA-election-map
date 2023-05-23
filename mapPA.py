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

# Create a jointplot with longitude and latitude as axes, Party Code as hue
joint_grid = sns.jointplot(x="Longitude", y="Latitude", data=all_data, hue="Party Code", palette={"D": "blue", "R": "red", "Other": "black"}, kind="scatter", s=0.02)
ax = joint_grid.ax_joint
# Set limits for the axes
plt.xlim([-81, -74.5])
plt.ylim([39, 42.5])

# Use contextily to add a basemap
contextily.add_basemap(ax, crs="EPSG:4326", source=contextily.providers.CartoDB.PositronNoLabels, attribution=False,zoom=12)
# save png
output_file = os.path.join(folder_path, "combined_plot.png")
ax.legend(fontsize='xx-small')
plt.savefig("PAmap", dpi=3200)
plt.close()  
