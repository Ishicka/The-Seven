import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import requests
import zipfile
import io
from flask import send_file

def plot_housing_affordability(year):
    # Load the data from the uploaded CSV file
    file_path = 'Resources/data_interpolated.csv'
    data = pd.read_csv(file_path)

    # Step 2: Filter and Aggregate the Data for the specified year
    data_year = data[data['Year'] == year]
    average_hai_per_state = data_year.groupby('StateName')['HAI'].mean().reset_index()

    # Load the shapefile
    shapefile_path = "us_states_shapefile/cb_2021_us_state_20m.shp"
    us_states_map = gpd.read_file(shapefile_path)

    # Rename columns to match the housing affordability data
    us_states_map = us_states_map.rename(columns={'STUSPS': 'StateName'})

    # Step 4: Merge the Data with the Map
    merged_map_data = us_states_map.merge(average_hai_per_state, on='StateName', how='left')

    # Step 5: Plot the Map
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    merged_map_data.plot(column='HAI', ax=ax, legend=True, cmap='OrRd', edgecolor='black', linewidth=0.3)
    ax.set_title(f'Average Housing Affordability by State in {year}', fontsize=15)
    plt.axis('off')

    # Save the plot to a BytesIO object
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    plt.close(fig)

    return send_file(bytes_image, mimetype='image/png')