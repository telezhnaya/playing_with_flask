from app.db import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    meme_id = db.Column(db.Integer, db.ForeignKey('memes.id'))

    def __repr__(self):
        return f'User {self.id} {self.name} {self.meme_id}'


class Meme(db.Model):
    __tablename__ = 'memes'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String)
    users = db.relationship(User, backref='meme', lazy='dynamic')
