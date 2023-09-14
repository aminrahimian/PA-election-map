import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import contextily
import geopandas as gpd

# Read the new CSV file containing longitude and latitude data
new_csv_file = 'merged_file.csv'
new_data = pd.read_csv(new_csv_file)
new_x_points = new_data['Longitude']
new_y_points = new_data['Latitude']

# Set seaborn style
sns.set(style="ticks", color_codes=True)

# Create a jointplot with longitude and latitude as axes, Party Code as hue
joint_grid = sns.jointplot(x="Longitude", y="Latitude", data=new_data, kind="scatter", s=0.02)
ax = joint_grid.ax_joint

# Set limits for the axes
plt.xlim([-81, -74.5])
plt.ylim([39.5, 42.5])

# Use contextily to add the specified basemap
contextily.add_basemap(ax, crs="EPSG:4326", source=contextily.providers.CartoDB.PositronNoLabels, attribution=False, zoom=12)

# Add the new points (Polling Stations) as green triangles
ax.scatter(new_x_points, new_y_points, color='Green', marker='^', label='Polling Station', s=0.1, linewidths=0.1, facecolor='green')

# Set plot parameters
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_title('PA Voter Map  with Polling Stations')

# Save the plot as a PNG file
plt.savefig("PAmap_PollingStation.png", dpi=1600)
plt.show()
