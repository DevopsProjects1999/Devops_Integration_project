# genai-tutor/app/__init__.py
from flask import Flask
from app.routes import main as main_blueprint
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(main_blueprint)

    return app