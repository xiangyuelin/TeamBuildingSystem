# -*- coding: utf-8 -*-

from extension import db
from models.model import FruitVotingResult


def get_fruit_voting_result(id):
    vote = FruitVotingResult.query.get(id)
    return vote


def add_fruit_voting_result(user_id, item_id):
    vote = FruitVotingResult(user_id=user_id, item_id=item_id)
    db.session.add(vote)
    db.session.commit()


def delete_fruit_voting_result(id):
    vote = FruitVotingResult.query.get(id)
    db.session.delete(vote)
    db.session.commit()


def update_fruit_voting_result(id, item_id):
    vote = FruitVotingResult.query.get(id)
    vote.item_id = item_id


def clear_fruit_voting_result(item_id):
    votes = FruitVotingResult.query.filter(item_id=item_id).all()
    for vote in votes:
        db.session.delete(vote)
    db.session.commit()


def get_fruit_voting_result_count(item_id):
    count = FruitVotingResult.query.filter(item_id=item_id).count()
    return count
