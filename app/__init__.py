from flask import Flask
from config import config
from app.main.routes import routes


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.register_blueprint(routes)

    return app
