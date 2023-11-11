from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

### ------------------ USER (ONE) ------------------ ###


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serializer_rule = ('-boards.users', '-questions.users', '-qnas.users')

    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String, nullable=False)
    rider_style = db.Column(db.String, nullable=False)

    boards = db.relationship('Board', back_populates='users')
    questions = db.relationship('Question', back_populates='users')
    qnas = db.relatioship('Qna', back_populates='users')

    def __repr__(self):
        return f''


### ------------------ BOARD (MANY) ------------------ ###


class Board(db.Model, SerializerMixin):
    __tablename__ = 'boards'

    serializer_rule = ('-users.boards',)

    id = db.Column(db.Integer, primary_key=True, unique=True)
    battery = db.Column(db.String, nullable=False)
    motor = db.Column(db.String, nullable=False)
    deck = db.Column(db.String, nullable=False)
    trucks = db.Column(db.String, nullable=False)
    wheels = db.Column(db.String, nullable=False)
    ESC = db.Column(db.String, nullable=False)
    controller = db.Column(db.String, nullable=False)

    users = db.relationship('User', back_populates='boards')






### ------------------ QUESTION (MANY) ------------------ ###


class Question(db.Model, SerializerMixin):
    __tablename__ = 'questions'

    serializer_rule = ('-users.questions',)

    id = db.Column(db.Integer, primary_key=True, unique=True)


    users = db.relationship('User', back_populates='questions')




### ------------------ QNA (MANY) ------------------ ###


class Qna(db.Model, SerializerMixin):
    __tablename__ = 'qnas'

    serializer_rule = ('-users.qnas',)

    id = db.Column(db.Integer, primary_key=True, unique=True)


    users = db.relationship('User', back_populates='qnas')



