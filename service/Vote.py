# -*- coding: utf-8 -*-

from extension import db
from models.model import Vote


def get_vote(id):
    vote = Vote.query.get(id)
    return vote


def add_vote(user_id, item_id):
    vote = Vote(user_id=user_id, item_id=item_id)
    db.session.add(vote)
    db.session.commit()


def delete_vote(id):
    vote = Vote.query.get(id)
    db.session.delete(vote)
    db.session.commit()


def update_vote(id, item_id):
    vote = Vote.query.get(id)
    vote.item_id = item_id


def clear_item_vote(item_id):
    votes = Vote.query.filter(item_id=item_id).all()
    for vote in votes:
        db.session.delete(vote)
    db.session.commit()


