from flask import Flask, request, render_template
from markupsafe import escape


def create_app():
    app = Flask(__name__)

    with app.app_context():
        from . import routes  # Import routes

        return app
