from flask import Flask, render_template, request, jsonify
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Load your data
data = pd.read_csv('data/data_interpolated.csv')

# Load the US States Shapefile
shapefile_path = 'data/us_states_shapefile/cb_2021_us_state_20m.shp'
us_states_map = gpd.read_file(shapefile_path)
us_states_map = us_states_map.rename(columns={'STUSPS': 'StateName'})

@app.route('/')
def index():
    # Extract unique dates for dropdown
    unique_dates = data['Date'].sort_values().unique().tolist()
    return render_template('index.html', dates=unique_dates)

@app.route('/update_plot', methods=['POST'])
def update_plot():
    selected_date = request.form['selected_date']
    filtered_data = data[data['Date'] == selected_date]
    average_hai_per_state = filtered_data.groupby('StateName')['HAI'].mean().reset_index()
    
    # Merge and plot
    merged_map_data = us_states_map.merge(average_hai_per_state, on='StateName', how='left')
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    merged_map_data.plot(column='HAI', ax=ax, legend=True, cmap='OrRd', edgecolor='black', linewidth=0.3)
    plt.axis('off')
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf-8')
    
    return jsonify({'plot_url': f'data:image/png;base64,{plot_url}'})

if __name__ == '__main__':
    app.run(debug=True)
