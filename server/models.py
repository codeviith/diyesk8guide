from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

### ------------------ USER (ONE) ------------------ ###


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serializer_rule = ('-boards.users', '-questions.users', '-forums.users')

    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String, nullable=False)
    rider_style = db.Column(db.String, nullable=False)



    boards = db.relationship('Board', back_populates='users')
    questions = db.relationship('Question', back_populates='users')
    forums = db.relatioship('Qna', back_populates='users')

    def __repr__(self):
        return f''


### ------------------ BOARD (ONE) ------------------ ###


class Board(db.Model, SerializerMixin):
    __tablename__ = 'boards'

    serializer_rule = ('-users.boards',)

    id = db.Column(db.Integer, primary_key=True, unique=True)


    deck_id = db.Column(db.Integer, db.ForeignKey('decks.id'))
    wheel_id = db.Column(db.Integer, db.ForeignKey('wheels.id'))
    truck_id = db.Column(db.Integer, db.ForeignKey('trucks.id'))
    motor_id = db.Column(db.Integer, db.ForeignKey('motors.id'))
    battery_id = db.Column(db.Integer, db.ForeignKey('batteries.id'))
    controller_id = db.Column(db.Integer, db.ForeignKey('controllers.id'))
    remote_id = db.Column(db.Integer, db.ForeignKey('remotes.id'))
    max_speed_id = db.Column(db.Integer, db.ForeignKey('max_speeds.id'))
    range_id = db.Column(db.Integer, db.ForeignKey('ranges.id'))


    deck = db.relationship('Deck', back_populates='boards')
    wheel = db.relationship('Wheel', back_populates='boards')
    truck = db.relationship('Truck', back_populates='boards')
    motor = db.relationship('Motor', back_populates='boards')
    battery = db.relationship('Battery', back_populates='boards')
    controller = db.relationship('Controller', back_populates='boards')
    remote = db.relationship('Remote', back_populates='boards')
    max_speed = db.relationship('Max_speed', back_populates='boards')
    range = db.relationship('Range', back_populates='boards')

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    users = db.relationship('User', back_populates='boards')



### ------------------ DECK (MANY) ------------------ ###
class Deck(db.Model, SerializerMixin):
    __tablename__ = 'decks'

    serializer_rule = ('-boards.deck',)

    id = db.Column(db.Integer, primary_key=True, unique=True)
    type = db.Column(db.String, nullable=False)
    length = db.Column(db.String, nullable=False)
    material = db.Column(db.String, nullable=False)

    boards = db.relationship('Board', back_populates='deck')


### ------------------ WHEEL (MANY) ------------------ ###
class Wheel(db.Model, SerializerMixin):
    __tablename__ = 'wheels'

    serializer_rule = ('-boards.wheel',)

    id = db.Column(db.Integer, primary_key=True, unique=True)
    size = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    
    boards = db.relationship('Board', back_populates='wheel')


### ------------------ TRUCK (MANY) ------------------ ###
class Truck(db.Model, SerializerMixin):
    __tablename__ = 'trucks'

    serializer_rule = ('-boards.truck',)

    id = db.Column(db.Integer, primary_key=True, unique=True)
    type = db.Column(db.String, nullable=False)
    width = db.Column(db.String, nullable=False)

    boards = db.relationship('Board', back_populates='truck')


### ------------------ MOTOR (MANY) ------------------ ###
class Motor(db.Model, SerializerMixin):
    __tablename__ = 'motors'

    serializer_rule = ('-boards.motor',)

    id = db.Column(db.Integer, primary_key=True, unique=True)
    size = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    kv = db.Column(db.String, nullable=False)

    boards = db.relationship('Board', back_populates='motor')


### ------------------ BATTERY (MANY) ------------------ ###
class Battery(db.Model, SerializerMixin):
    __tablename__ = 'batteries'

    serializer_rule = ('-boards.battery',)

    id = db.Column(db.Integer, primary_key=True, unique=True)
    voltage = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    capacity = db.Column(db.String, nullable=False)
    configuration = db.Column(db.String, nullable=False)

    boards = db.relationship('Board', back_populates='battery')


### ------------------ CONTROLLER (MANY) ------------------ ###
class Controller(db.Model, SerializerMixin):
    __tablename__ = 'controllers'

    serializer_rule = ('-boards.controller',)

    id = db.Column(db.Integer, primary_key=True, unique=True)
    features = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)

    boards = db.relationship('Board', back_populates='controller')


### ------------------ REMOTE (MANY) ------------------ ###
class Remote(db.Model, SerializerMixin):
    __tablename__ = 'remotes'

    serializer_rule = ('-boards.remote',)

    id = db.Column(db.Integer, primary_key=True, unique=True)
    features = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)

    boards = db.relationship('Board', back_populates='remote')


### ------------------ MAX_SPEED (MANY) ------------------ ###
class Max_speed(db.Model, SerializerMixin):
    __tablename__ = 'max_speeds'

    serializer_rule = ('-boards.max_speed',)

    id = db.Column(db.Integer, primary_key=True, unique=True)
    speed = db.Column(db.String, nullable=False)

    boards = db.relationship('Board', back_populates='max_speed')


### ------------------ RANGE (MANY) ------------------ ###
class Range(db.Model, SerializerMixin):
    __tablename__ = 'ranges'

    serializer_rule = ('-boards.range',)

    id = db.Column(db.Integer, primary_key=True, unique=True)
    range = db.Column(db.String, nullable=False)

    boards = db.relationship('Board', back_populates='range')








### unsure where these go ###


### ------------------ QUESTION (MANY) ------------------ ###


class Question(db.Model, SerializerMixin):
    __tablename__ = 'questions'

    serializer_rule = ('-users.questions',)

    id = db.Column(db.Integer, primary_key=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


    users = db.relationship('User', back_populates='questions')




### ------------------ FORUM (ONE) ------------------ ###


class Forum(db.Model, SerializerMixin):
    __tablename__ = 'forums'

    serializer_rule = ('-users.forums',)

    id = db.Column(db.Integer, primary_key=True, unique=True)


    users = db.relationship('User', back_populates='forums')



