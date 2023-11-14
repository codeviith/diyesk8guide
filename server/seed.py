#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc
import random
from faker import Faker

# Local imports
from app import app
from models import db, User, Question, Forum, Board, Deck, Wheel, Truck, Motor, Battery, Controller, Remote, Max_speed, Range


if __name__ == '__main__':
    with app.app_context():
        print("Starting seed...")
        
        print("Clearing db...")
        faker = Faker()

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


        print("Creating users...")
        user1 = User(email="user1@example.com", password="pwd1")
        db.session.add(user1)


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
        decks = []
        for _ in range(50):
            deck = Deck(

            )
            decks.append(deck)
            db.session.add_all(decks)
            db.session.commit()


        print("Seeding complete!")