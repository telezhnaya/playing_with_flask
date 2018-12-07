from flask import Flask

from app.config import config
from app.db import db
from app.mail import mail
from app.main.routes import routes
from app.main.mail import mail_bp


def create_app():
    app = Flask(__name__)
    config_obj = config[app.env]
    app.config.from_object(config_obj)
    config_obj.init_app(app)
    app.register_blueprint(routes)
    app.register_blueprint(mail_bp)
    db.init_app(app)
    mail.init_app(app)

    return app
