#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc
import random
# from faker import Faker

# Local imports
from app import app
from models import db, User, Question, Forum, Board, Deck, Wheel, Truck, Motor, Battery, Controller, Remote, Max_speed, Range


if __name__ == '__main__':
    with app.app_context():
        print("Starting seed...")
        
        print("Clearing db...")
        # faker = Faker()

        User.query.delete()
        Question.query.delete()
        Forum.query.delete()
        Board.query.delete()
        Deck.query.delete()
        Wheel.query.delete()
        Truck.query.delete()
        Motor.query.delete()
        Battery.query.delete()
        Controller.query.delete()
        Remote.query.delete()
        Max_speed.query.delete()
        Range.query.delete()


        # print("Creating users...")
        # user1 = User(email="user1@example.com", password="pwd1")
        # db.session.add(user1)


        print("Creating boards...")
        boards = []
        for _ in range(5):
            board = Board(
                board=faker.word()
            )
            boards.append(board)
            db.session.add_all(boards)
            db.session.commit()


        print("Creating decks...")
        deck1 = Deck(type="Drop-through deck for stability and comfort",
            length="38 inches",
            materal="7-ply maple"
            )
        db.session.add(deck1)
        db.session.commit()


        print("Seeding complete!")



        # Create wheels
        wheel1 = Wheel(size='Size1', type='Type1')
        wheel2 = Wheel(size='Size2', type='Type2')

        # Create trucks
        truck1 = Truck(type='Type1', width='Width1')
        truck2 = Truck(type='Type2', width='Width2')

        # Create motors
        motor1 = Motor(size='Size1', type='Type1', kv='KV1')
        motor2 = Motor(size='Size2', type='Type2', kv='KV2')

        # Create batteries
        battery1 = Battery(voltage='Voltage1', type='Type1', capacity='Capacity1', configuration='Config1')
        battery2 = Battery(voltage='Voltage2', type='Type2', capacity='Capacity2', configuration='Config2')

        # Create controllers
        controller1 = Controller(features='Features1', type='Type1')
        controller2 = Controller(features='Features2', type='Type2')

        # Create remotes
        remote1 = Remote(features='Features1', type='Type1')
        remote2 = Remote(features='Features2', type='Type2')

        # Create max_speeds
        max_speed1 = Max_speed(speed='Speed1')
        max_speed2 = Max_speed(speed='Speed2')

        # Create ranges
        range1 = Range(range='Range1')
        range2 = Range(range='Range2')

        # Create questions
        question1 = Question(user=user1)
        question2 = Question(user=user2)

        # Create forums
        forum1 = Forum(user=user1)
        forum2 = Forum(user=user2)

        # Commit to the database
        db.session.add_all([user1, user2, board1, board2, deck1, deck2, wheel1, wheel2, truck1, truck2,
                            motor1, motor2, battery1, battery2, controller1, controller2, remote1, remote2,
                            max_speed1, max_speed2, range1, range2, question1, question2, forum1, forum2])
        db.session.commit()
