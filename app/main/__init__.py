from flask import Blueprint

main = Blueprint('main', __name__)

# That's so ugly, are we sure that we can't do this better?
from . import routes
