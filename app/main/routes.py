from datetime import datetime as dt

from flask import Blueprint

from app.models.models import User

routes = Blueprint('routes', __name__)


@routes.route('/time')
def time():
    return str(dt.utcnow())


@routes.route('/users')
def users():
    return str(User.query.all())


# @routes.route('/create')
# def create():
#     db.drop_all()
#     db.create_all()
#
#     meme1 = Meme(url='https://memepedia.ru/wp-content/uploads/2017/04/'
#                      'Philosoraptor.jpg')
#     meme2 = Meme(url='http://weknowmemes.com/wp-content/uploads/2011/09/'
#                      'sucess-kid-mom-took-my-nose-got-it-back.jpg')
#     db.session.add_all({meme1, meme2})
#     db.session.commit()
#
#     user1 = User(name='Olya', meme=meme1)
#     user2 = User(name='Kolya', meme=meme2)
#     user3 = User(name='Nastya', meme=meme2)
#     db.session.add_all({user1, user2, user3})
#     db.session.commit()
#
#     return 'Congrats!'
