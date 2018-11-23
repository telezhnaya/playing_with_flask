import datetime

from flask import Blueprint

bp = Blueprint('routes', __name__)


@bp.route('/time')
def time():
    return datetime.datetime.utcnow().isoformat()
