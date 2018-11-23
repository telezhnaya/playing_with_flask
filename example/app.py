from flask import Flask

from .config import config
from .routes import bp


def create_app():
    app = Flask(__name__)
    config_object = config[app.env]
    app.config.from_object(config_object)
    config_object.init_app(app)
    app.register_blueprint(bp)

    return app
