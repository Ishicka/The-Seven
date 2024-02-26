from flask import Flask, render_template, request
from myapp.heatmap import plot_housing_affordability

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def home():
    year = None
    plot_url = None
    if request.method == 'POST':
        year = request.form.get('year')
        plot_url = f'/plot/{year}'
    return render_template('index.html', year=year, plot_url=plot_url)

@app.route('/plot/<int:year>')
def plot(year):
    return plot_housing_affordability(year)

if __name__ == '__main__':
    app.run(debug=True)