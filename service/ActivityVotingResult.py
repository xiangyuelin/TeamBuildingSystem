# -*- coding: utf-8 -*-

from extension import db
from models.model import ActivityVotingResult


def get_activity_vote_result(id):
    vote = ActivityVotingResult.query.get(id)
    return vote


def add_activity_vote_result(user_id, item_id):
    vote = ActivityVotingResult(user_id=user_id, item_id=item_id)
    db.session.add(vote)
    db.session.commit()


def delete_activity_vote_result(id):
    vote = ActivityVotingResult.query.get(id)
    db.session.delete(vote)
    db.session.commit()


def update_activity_vote_result(id, item_id):
    vote = ActivityVotingResult.query.get(id)
    vote.item_id = item_id


def clear_activity_vote_result(item_id):
    votes = ActivityVotingResult.query.filter(item_id=item_id).all()
    for vote in votes:
        db.session.delete(vote)
    db.session.commit()


def get_item_vote_count(item_id):
    count = ActivityVotingResult.query.filter(item_id=item_id).count()
    return count
