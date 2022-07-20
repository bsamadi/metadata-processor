from flask import Flask, request, render_template
from markupsafe import escape
import datetime
from pysolar import solar

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect_glare', methods=['GET', 'POST'])
def detect_glare():
    # Get the JSON payload
    payload = request.get_json()

    # Input variables
    lat = payload['lat']                 # Lattitude (deg)
    lon = payload['lon']                 # Longitude (deg)
    epoch = payload['epoch']             # time (Linux epoch in seconds)
    orientation = payload['orientation'] # Orientation (deg)

    # Calculate UTC time
    date = datetime.datetime.fromtimestamp(epoch, tz=datetime.timezone.utc)

    # Calculate the azimuth and altitude of the sun using [Pysolar](https://pysolar.org/)
    altitude_sun = solar.get_altitude(lat, lon, date) # Sun's altitude (deg)
    azimuth_sun = solar.get_azimuth(lat, lon, date)   # Sun's azimuth (deg)

    # There is a possibility of a direct glare if the azimuthal difference between the sun and the direction of the car travel (and hence 
    # the direction of forward-facing camera) is less than 30 degrees and the altitude of the sun is less than 45 degrees.
    if abs(orientation - azimuth_sun) <= 30.0 and 45.0 >= altitude_sun >= 0:
       glare="true"
    else:
       glare="false"

    return {
        "glare": glare,
    }