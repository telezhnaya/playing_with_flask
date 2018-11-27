from flask import Flask

from app.db import db
from app.config import config
from app.main.routes import routes


def create_app():
    app = Flask(__name__)
    config_obj = config[app.env]
    app.config.from_object(config_obj)
    config_obj.init_app(app)
    app.register_blueprint(routes)
    db.init_app(app)

    return app
