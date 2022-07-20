from flask import request, render_template
from flask import current_app as app

from app.sun_pos import sun_pos
from app.is_glare import is_glare


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/detect_glare', methods=['GET', 'POST'])
def detect_glare():
    # Get the JSON payload
    payload = request.get_json()

    # Input variables
    # lat = payload['lat']                 # Lattitude (deg)
    # lon = payload['lon']                 # Longitude (deg)
    # epoch = payload['epoch']             # time (Linux epoch in seconds)
    orientation = payload['orientation']   # Orientation (deg)

    # The sun's position (altitude, azimuth) using [Pysolar](https://pysolar.org/)
    sun = sun_pos(payload)

    return {
        "glare": is_glare(sun, orientation),
    }
