import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import geopandas as gpd
import contextily as ctx
from matplotlib.colors import Normalize
import matplotlib.cm as cm
# Read the CSV file
data = pd.read_csv('result111.csv')

# Create a pivot table without considering the 'Party' column
heatmap_data = pd.pivot_table(data, values='Mean Distance', index='County', aggfunc='mean')

# Fill missing values
heatmap_data = heatmap_data.fillna(0)

# Plot the heatmap
plt.figure(figsize=(60, 60))
sns.heatmap(heatmap_data, cmap='YlOrRd', annot=False, fmt=".2f", cbar=True)

plt.title('Heatmap of Mean Distance of Polling Stations', fontsize=80)  # Adjust the title font size
plt.xlabel('County', fontsize=60)  # Adjust the x-axis label font size (No Party Code)
plt.ylabel('County', fontsize=60)  # Adjust the y-axis label font size (No Party Code)
plt.xticks(fontsize=40)  # Adjust the x-axis tick font size
plt.yticks(fontsize=40)  # Adjust the y-axis tick font size

# Get the colorbar axes object
cax = plt.gcf().axes[-1]

# Adjust the colorbar label font size
cax.tick_params(labelsize=60)


# Read the GeoJSON file for Pennsylvania counties' boundaries

county_boundaries = gpd.read_file("E:\python\PaCounty2023_04.geojson")
# Merge the heatmap data with the county boundary data based on the correct column name
merged_data = county_boundaries.merge(heatmap_data, left_on='COUNTY_NAM', right_index=True)

# Plot the Pennsylvania map with county colors based on the heatmap data
fig, ax = plt.subplots(figsize=(20, 20))
ax.set_aspect('equal')
ax.set_axis_off()

# Plot county boundaries
county_boundaries.plot(ax=ax, edgecolor='blue', linewidth=1, facecolor='none')

# Create a ScalarMappable to create the colorbar
cmap = cm.get_cmap('YlOrRd')
norm = Normalize(vmin=heatmap_data.min().min(), vmax=heatmap_data.max().max())
sm = cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])

# Plot filled counties with colors from the heatmap data
merged_data.plot(column='Mean Distance', cmap='YlOrRd', linewidth=0.5, ax=ax, legend=False, vmin=heatmap_data.min().min(), vmax=heatmap_data.max().max())

# Add the colorbar manually
cbar = fig.colorbar(sm, ax=ax, aspect=50, pad=0.02,shrink=0.6)
cbar.ax.tick_params(labelsize=15)

plt.title('Mean Distance of Polling Stations in Pennsylvania with County Boundaries', fontsize=20)
plt.xlabel('Longitude', fontsize=15)
plt.ylabel('Latitude', fontsize=15)

plt.savefig('heatmap.png')
# Show the plot
plt.show()
