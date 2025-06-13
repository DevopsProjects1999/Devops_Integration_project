# app/__init__.py
import os
from flask import Flask
from app.routes import main as main_blueprint
from config import Config

def create_app():
    app = Flask(__name__, template_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates'))
    app.config.from_object(Config)

    app.register_blueprint(main_blueprint)

    return app