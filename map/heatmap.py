import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('yourfile.csv')

# Create a pivot table
heatmap_data = pd.pivot_table(data, values='Mean Distance', index='County', columns='Party', aggfunc='mean')

# Fill missing values
heatmap_data = heatmap_data.fillna(0)

# Plot the heatmap
plt.figure(figsize=(60, 60))
sns.heatmap(heatmap_data, cmap='YlOrRd', annot=False, fmt=".2f", cbar=True)

plt.title('Heatmap of Mean Distance of Polling Stations', fontsize=80)  # Adjust the title font size
plt.xlabel('Party Code', fontsize=60)  # Adjust the x-axis label font size
plt.ylabel('County', fontsize=60)  # Adjust the y-axis label font size
plt.xticks(fontsize=40)  # Adjust the x-axis tick font size
plt.yticks(fontsize=40)  # Adjust the y-axis tick font size

# Get the colorbar axes object
cax = plt.gcf().axes[-1]

# Adjust the colorbar label font size
cax.tick_params(labelsize=60)

plt.savefig('heatmapMean.png')
# Show the plot
plt.show()
