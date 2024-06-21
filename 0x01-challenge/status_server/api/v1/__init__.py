# status_server/api/v1/__init__.py
""" v1 module initialization """
from flask import Flask
from api.v1.views import app_views

def create_app():
    app = Flask(__name__)
    app.register_blueprint(app_views)
    return app
