from datetime import datetime as dt

from flask import Blueprint

routes = Blueprint('routes', __name__)


@routes.route('/time')
def time():
    return str(dt.utcnow())
