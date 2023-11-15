from flask import Flask, request, render_template, redirect, url_for
import part1_mbta_helper
app = Flask(__name__)
mapbox_access_token = "pk.eyJ1IjoiamVmZnJ5emhhbmciLCJhIjoiY2xveXA4cDBoMDViZDJqbzUxd2xsMzB1MiJ9.KNQqcz1W-NEqGyLC6nhYsA"
mbta_api_key = "f1b5807a6651432ea9b82af220367e1a"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        place_name = request.form['place_name']
        return redirect(url_for('nearest_mbta', place_name=place_name))
    return render_template('index.html')

@app.route('/nearest_mbta/<place_name>')
def nearest_mbta(place_name):
    try:
        # Use mbta_helper module's function to get the nearest MBTA stop
        result = part1_mbta_helper.combined_tool(place_name, mapbox_access_token, mbta_api_key)
        return render_template('mbta_station.html', result=result)
    except Exception as e:
        return render_template('error.html', error=str(e))

@app.route('/error')
def error():
    return 'Error occurred. <a href="/">Go back</a>'

if __name__ == '__main__':
    app.run(debug=True)

