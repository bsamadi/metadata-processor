from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect_glare', methods=['GET', 'POST'])
def detect_glare():
    # payload: 'lat', 'lon', 'epoch', 'orientation'
    payload = request.get_json()
    

    return {
        "lattitude": payload['lat'],
        "longitude": payload['lon'],
        "epoch": payload['epoch'],
        "orientation": payload['orientation'],
        "glare": "false",
    }