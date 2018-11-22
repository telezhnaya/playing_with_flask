from datetime import datetime as dt
from . import main


@main.route('/time')
def time():
    return str(dt.utcnow())
