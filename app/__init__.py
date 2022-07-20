from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect_glare', methods=['GET', 'POST'])
def detect_glare():
    return {
        "glare": "false",
    }