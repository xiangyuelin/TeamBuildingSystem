# -*- coding: utf-8 -*-

from datetime import datetime

from extension import db
from models.model import FruitVoting


def get_fruit_voting(id):
    fruit_voting = FruitVoting.query.get(id)
    return fruit_voting


def add_fruit_voting(title, member):
    fruit_voting = FruitVoting(title=title, member=member)
    db.session.add(fruit_voting)
    db.session.commit()


def delete_fruit_voting(id):
    fruit_voting = FruitVoting.query.get(id)
    db.session.delete(fruit_voting)
    db.session.commit()


def invalidate_fruit_voting(id):
    fruit_voting = FruitVoting.query.get(id)
    fruit_voting.is_validated = False
    db.session.commit()


def update_fruit_voting(id, member):
    fruit_voting = Activity.query.get(id)
    fruit_voting.member = member
    db.session.commit()


def get_all_fruit_votings():
    fruit_votings = FruitVoting.query.all()
    return fruit_votings


def get_all_current_fruit_votings():
    fruit_votings = fruit_votings.query.filter_by(show=True).all()
    return fruit_votings






